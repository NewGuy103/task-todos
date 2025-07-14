import logging
import typing
import uuid

from datetime import datetime, timedelta, timezone
from enum import StrEnum

from PySide6.QtCore import QAbstractTableModel, QModelIndex, QObject, Qt, Signal, Slot, QDateTime
from PySide6.QtWidgets import QDialog, QMessageBox, QInputDialog

from ..models import (
    DeadlineFilterState, FilterCompletedTasksEnum, FilterState, AlphabeticalSortingEnum, SortState, SortingModeEnum, SubjectTask, 
    EditedSubjectTask, EditedTaskWithID, DeadlineSortingEnum, 
    SortAndFilterState, BuiltinCategories
)
from ..ui.add_task_dialog import Ui_AddTaskDialog

if typing.TYPE_CHECKING:
    from ..main import MainWindow


logger: logging.Logger = logging.getLogger("task-todos")


class EmitDialogInfoAs(StrEnum):
    add = 'add'
    edit = 'edit'



class TaskTodosTableModel(QAbstractTableModel):
    def __init__(self, /, parent: 'TaskTodosController' = None):
        super().__init__(parent)
        self.todo_ctrl = parent

        self._display_data: list[list] = []
        self._item_data: list[SubjectTask] = []

        self._col_headers: list[str] = ["Completed", "Subject", "Category", "Task", "Deadline"]
    
    def rowCount(self, /, parent=QModelIndex()):
        return len(self._item_data)

    def columnCount(self, /, parent=QModelIndex()):
        return len(self._col_headers)
    
    def data(self, index, /, role):
        if role == Qt.ItemDataRole.UserRole:
            return self._item_data[index.row()]
        
        if role == Qt.ItemDataRole.DisplayRole:
            value = self._display_data[index.row()][index.column()]
            if isinstance(value, datetime):
                local_value = value.astimezone()
                return local_value.strftime("%x %X")
            
            if isinstance(value, bool):
                if value:
                    return "Yes"
                else:
                    return "No"
            
            if isinstance(value, int):
                if index.column() == 2:
                    return BuiltinCategories(value=value).name.capitalize().replace("_", " ")
                
                return str(value)
            
            if value is None:
                logger.debug("Received 'None' value at cell [%d, %d]", index.row(), index.column())
                return ''
            
            return value
        
        return None
    
    def headerData(self, section, orientation, /, role):
        if role != Qt.ItemDataRole.DisplayRole:
            return None
        
        if orientation == Qt.Orientation.Horizontal:
            return self._col_headers[section]

        if orientation == Qt.Orientation.Vertical:
            return super().headerData(section, orientation, role)

    def load_tasks(self, tasks: list[SubjectTask]):
        self.beginResetModel()

        self._display_data.clear()
        self._item_data.clear()

        logger.debug("Cleared all tasks")

        for task in tasks:
            display_data = [task.completed, task.subject, task.category, task.task, task.deadline]
            self._display_data.append(display_data)

            self._item_data.append(task)

        logger.debug("Added %d tasks to model", len(self._item_data))
        self.endResetModel()
    
    def add_task(self, task: SubjectTask):
        display_data = [task.completed, task.subject, task.category, task.task, task.deadline]

        self._item_data.append(task)
        self._display_data.append(display_data)

        logger.debug("Added task '%s' to model", task.task)
        self.layoutChanged.emit()
    
    def delete_task(self, index: QModelIndex):
        if not index.isValid():
            return
        
        item_data = self._item_data[index.row()]
        logger.debug("Deleted task '%s' at row %d", item_data.task, index.row())

        del self._item_data[index.row()]
        del self._display_data[index.row()]

        self.layoutChanged.emit()
    
    def update_task(self, index: QModelIndex, task: SubjectTask):
        if not index.isValid():
            return

        display_data = [task.completed, task.subject, task.category, task.task, task.deadline]
        row = index.row()

        self._item_data[row] = task
        self._display_data[row] = display_data

        top = self.index(row, 0)
        bottom = self.index(row, self.columnCount() - 1)

        logger.debug("Updated task '%s' at row %d", task.task, index.row())
        self.dataChanged.emit(top, bottom)


class TaskTodosController(QObject):
    def __init__(self, mw_parent: 'MainWindow'):
        super().__init__(mw_parent)
        self.mw_parent = mw_parent

        self.ui = mw_parent.ui
        self.app_data = mw_parent.app_data

        self.model = TaskTodosTableModel(self)

        self.subject_ctrl: SubjectItemController = SubjectItemController(self)
        self.task_ctrl: TasksItemController = TasksItemController(self)

        self.sort_filter_ctrl: SortAndFilterController = SortAndFilterController(self)
        self.setup()

    def setup(self):
        self.ui.mainStackedWidget.setCurrentIndex(0)  # main page

        self.ui.actionAdd_subject.triggered.connect(self.subject_ctrl.add_subject)
        self.ui.actionRemove_subject.triggered.connect(self.subject_ctrl.remove_subject)

        self.sort_filter_ctrl.sortFilterComplete.connect(self.task_ctrl.reload_model)
        self.task_ctrl.taskAdded.connect(self.sort_filter_ctrl.task_added)
    
    @Slot(SortAndFilterState)
    def update_sort_filter_state(self, state: SortAndFilterState):
        logger.debug("Received signal to update sort/filter state")
        self.sort_filter_ctrl.change_state(state)


class SubjectItemController(QObject):
    subjectAdded = Signal(str)
    subjectRemoved = Signal(int)  # index

    def __init__(self, ctrl_parent: 'TaskTodosController'):
        super().__init__(ctrl_parent)
        self.ctrl_parent = ctrl_parent
        self.mw_parent = ctrl_parent.mw_parent

        self.ui = ctrl_parent.ui
        self.app_data = ctrl_parent.app_data

    @Slot()
    def add_subject(self):
        text, ok = QInputDialog.getText(
            self.mw_parent,
            "Task to-dos - Add subject",
            "Enter subject name:"
        )
        if text in self.app_data.subjects:
            QMessageBox.warning(
                self.mw_parent,
                "Task to-dos - Add subject",
                "Provided subject already exists."
            )
            return
        
        if text and ok:
            self.app_data.subjects.append(text)
            self.app_data.save_settings()
            
            self.subjectAdded.emit(text)

    @Slot()
    def remove_subject(self):
        if not self.app_data.subjects:
            QMessageBox.information(
                self.mw_parent,
                "Task to-dos - Remove subject",
                "There are no subjects to remove."
            )
            return
        
        item, ok = QInputDialog.getItem(
            self.mw_parent,
            "Task to-dos - Remove subject",
            "Choose a subject to delete:",
            self.app_data.subjects
        )
        if item and ok:
            self.subjectRemoved.emit(self.app_data.subjects.index(item))

            self.app_data.subjects.remove(item)
            self.app_data.save_settings()


class TasksItemController(QObject):
    taskAdded: Signal = Signal(SubjectTask)

    def __init__(self, ctrl_parent: 'TaskTodosController'):
        super().__init__(ctrl_parent)
        self.ctrl_parent = ctrl_parent
        self.mw_parent = ctrl_parent.mw_parent

        self.ui = ctrl_parent.ui
        self.app_data = ctrl_parent.app_data

        self.task_dialog: TaskInfoDialog = TaskInfoDialog(self)
        self.model = ctrl_parent.model

        self.ui.tasksTableView.setModel(self.model)
        self.setup()
    
    def setup(self):
        self.task_dialog.addTaskRequested.connect(self.add_task_accepted)
        self.task_dialog.editTaskRequested.connect(self.edit_task_accepted)

        self.ui.tasksTableView.doubleClicked.connect(self.edit_task_triggered)

        self.ui.addTaskButton.clicked.connect(self.add_task_triggered)
        self.ui.removeTaskButton.clicked.connect(self.remove_task_triggered)
        self.ui.completeTaskButton.clicked.connect(self.complete_task_triggered)

        self.ui.actionAdd_task.triggered.connect(self.add_task_triggered)
        self.ui.actionRemove_task.triggered.connect(self.remove_task_triggered)

        self.ui.actionEdit_task.triggered.connect(self.edit_task_triggered)
        self.ui.actionMark_task_completed.triggered.connect(self.complete_task_triggered)

        self.model.load_tasks(self.app_data.tasks)

    @Slot(list)
    def reload_model(self, tasks: list[SubjectTask]):
        logger.info("Reloaded model with %d tasks", len(tasks))
        self.model.load_tasks(tasks)
    
    @Slot()
    def add_task_triggered(self):
        if not self.app_data.subjects:
            QMessageBox.warning(
                self.mw_parent,
                "Task to-dos - Add task",
                "No subjects have been defined yet, please create a subject for tasks."
            )
            return
        
        self.task_dialog.reset_data(self.app_data.subjects)
        self.task_dialog.show()
    
    @Slot()
    def add_task_accepted(self, task: EditedSubjectTask):
        new_task = SubjectTask(
            task_id=uuid.uuid4(),
            completed=False,
            **task.model_dump()
        )
        self.app_data.tasks.append(new_task)
        self.app_data.save_settings()

        logger.debug("Added new task, sending signal to add to model")
        self.taskAdded.emit(new_task)
    
    @Slot()
    def remove_task_triggered(self):
        indexes = self.ui.tasksTableView.selectedIndexes()
        if not indexes:
            return
        
        index = indexes[0]
        data: SubjectTask = index.data(Qt.ItemDataRole.UserRole)

        btn = QMessageBox.information(
            self.mw_parent,
            "Task to-dos - Delete task",
            "Do you want to delete the currently selected task?",
            buttons=QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            defaultButton=QMessageBox.StandardButton.No
        )
        if btn == QMessageBox.StandardButton.No:
            return
        
        self.app_data.tasks.remove(data)
        self.app_data.save_settings()

        self.model.delete_task(index)
        self.ui.tasksTableView.clearSelection()
    
    @Slot()
    def complete_task_triggered(self):
        indexes = self.ui.tasksTableView.selectedIndexes()
        if not indexes:
            return
        
        index = indexes[0]
        data: SubjectTask = index.data(Qt.ItemDataRole.UserRole)

        new_model = data.model_copy()
        new_model.completed = not new_model.completed

        data_index = self.app_data.tasks.index(data)
        self.app_data.tasks[data_index] = new_model

        self.app_data.save_settings()
        self.model.update_task(index, new_model)

        if not data.completed:
            QMessageBox.information(
                self.mw_parent,
                "Task to-dos - Add task",
                f"Task '{new_model.task}' successfully completed!"
            )
    
    @Slot()
    def edit_task_triggered(self):
        indexes = self.ui.tasksTableView.selectedIndexes()
        if not indexes:
            return
        
        index = indexes[0]
        data: SubjectTask = index.data(Qt.ItemDataRole.UserRole)

        self.task_dialog.reset_data(self.app_data.subjects, emit_as=EmitDialogInfoAs.edit)
        self.task_dialog.set_existing_data(data)

        self.task_dialog.show()
    
    @Slot(EditedTaskWithID)
    def edit_task_accepted(self, task: EditedTaskWithID):
        indexes = self.ui.tasksTableView.selectedIndexes()
        if not indexes:
            return
        
        index = indexes[0]
        data: SubjectTask = index.data(Qt.ItemDataRole.UserRole)

        edited_task = SubjectTask(
            **task.model_dump()
        )

        data_index = self.app_data.tasks.index(data)
        self.app_data.tasks[data_index] = edited_task

        self.app_data.save_settings()
        self.model.update_task(index, edited_task)

        self.updateSortAndFilterRequested.emit()


class SortAndFilterController(QObject):
    sortFilterComplete = Signal(list)  # list[SubjectTask]
    
    def __init__(self, ctrl_parent: 'TaskTodosController'):
        super().__init__(ctrl_parent)
        self.ctrl_parent = ctrl_parent
        self.mw_parent = ctrl_parent.mw_parent

        self.ui = ctrl_parent.ui
        self.app_data = ctrl_parent.app_data

        self.model = ctrl_parent.model
        self._sort_filter_state: SortAndFilterState = None

        self.setup()

    def setup(self):
        self._sort_filter_state = SortAndFilterState(
            sort_state=SortState(
                sort_mode=SortingModeEnum.disabled,
                sort_option=None
            ),
            filter_state=FilterState(
                subject=False,
                category=False,
                deadline=DeadlineFilterState(
                    enabled=False,
                    not_before=datetime.now(timezone.utc),
                    not_after=datetime.now(timezone.utc) + timedelta(weeks=12)
                ),
                completed=FilterCompletedTasksEnum.dont_filter
            )
        )
    
    def change_state(self, state: SortAndFilterState):
        self._sort_filter_state = state
        self._process_tasks()
    
    def _process_tasks(self):
        state = self._sort_filter_state

        final_tasks = self._filter_tasks()
        sorted_tasks = self._sort_tasks(final_tasks, state.sort_state.sort_mode)

        self.sortFilterComplete.emit(sorted_tasks)
        self.ui.statusbar.showMessage("Changed sorting/filtering options", timeout=5000)
    
    @Slot(SubjectTask)
    def task_added(self, task: SubjectTask):
        """Checks if the new task passes the filter rules before displaying."""
        state = self._sort_filter_state
        subject = state.filter_state.subject

        if isinstance(subject, bool):
            logger.debug("Passed subject filter due to value being a bool")
        elif isinstance(subject, str):
            if task.subject != subject:
                logger.debug("Failed subject filter, not adding to model")
                return
            
            logger.debug("Passed subject filter")
        
        category = state.filter_state.category
        if isinstance(category, bool):
            logger.debug("Passed category filter due to value being a bool")
        elif isinstance(category, int):
            if task.category != category:
                logger.debug("Failed category filter, not adding to model")
                return
            
            logger.debug("Passed category filter")
        
        deadline = state.filter_state.deadline
        if deadline.enabled:
            if deadline.not_before < task.deadline < deadline.not_after:
                logger.debug("Failed deadline filter, not adding to model")
                return
            
            logger.debug("Passed deadline filter")
        else:
            logger.debug("Deadline filter not enabled")

        filter_complete = state.filter_state.completed
        if filter_complete == FilterCompletedTasksEnum.dont_filter:
            logger.debug("Completed tasks filter not enabled")
        elif filter_complete == FilterCompletedTasksEnum.complete:
            logger.debug("Failed completed tasks filter, not adding to model")
            return
        elif filter_complete == FilterCompletedTasksEnum.incomplete:
            logger.debug("Passed completed tasks filter")

        logger.info("New task passed filter, adding to model")
        self.model.add_task(task)

    def _filter_tasks(self):
        # TODO: Refactor function if it becomes hard to read/understand
        state = self._sort_filter_state

        final_tasks: list[SubjectTask] | None = None
        subject = state.filter_state.subject

        if isinstance(subject, bool):
            # Do nothing when it's either "Include All" or "Don't include"
            # Because the goal ends up the same:
            # - Include All: Return the whole tasks list (match all subjects)
            # - Don't Include: Don't use this filter and let the other filters handle it
            logger.debug("Not filtering for subjects, value is '%s'", subject)
        elif isinstance(subject, str):
            final_tasks = [task for task in self.app_data.tasks if task.subject == subject]
            logger.debug("Filtered for tasks with subject '%s', received %d tasks", subject, len(final_tasks))
        
        category = state.filter_state.category
        if isinstance(category, bool):
            # Do nothing, same reason as for subject
            logger.debug("Not filtering for categories, value is '%s'", category)
        elif isinstance(category, int):
            if not final_tasks:
                final_tasks = [*self.app_data.tasks]
            
            final_tasks = [task for task in final_tasks if task.category == category]
            logger.debug("Filtered for tasks with category '%s', received %d tasks", category.name, len(final_tasks))

        deadline = state.filter_state.deadline
        if deadline.enabled:
            if not final_tasks:
                final_tasks = [*self.app_data.tasks]
            
            final_tasks = [
                task for task in final_tasks
                if deadline.not_before < task.deadline < deadline.not_after
            ]
            logger.debug(
                "Filtered for tasks with datetime not before '%s' and not after '%s'" \
                ", received %d tasks",
                deadline.not_before, deadline.not_after, len(final_tasks)
            )
        else:
            # Do nothing, same reason as for subject
            logger.debug("Not filtering for deadlines, filter is disabled")
        
        filter_complete = state.filter_state.completed
        if filter_complete == FilterCompletedTasksEnum.dont_filter:
            logger.debug("Not filtering for completed tasks, filter is disabled")
        elif filter_complete == FilterCompletedTasksEnum.complete:
            if not final_tasks:
                final_tasks = [*self.app_data.tasks]
            
            final_tasks = [task for task in final_tasks if task.completed]
            logger.debug("Filtered for complete tasks, received %d tasks", len(final_tasks))
        elif filter_complete == FilterCompletedTasksEnum.incomplete:
            if not final_tasks:
                final_tasks = [*self.app_data.tasks]
            
            final_tasks = [task for task in final_tasks if not task.completed]
            logger.debug("Filtered for incomplete tasks, received %d tasks", len(final_tasks))

        if final_tasks is None:
            # Default to showing everything when no filter is applied
            logger.debug("All filters are disabled, returning all tasks")
            final_tasks = [*self.app_data.tasks]
        
        logger.debug("Retrieved %d entries after filtering", len(final_tasks))
        return final_tasks
    
    def _sort_tasks(self, tasks: list[SubjectTask], sort_mode: SortingModeEnum):
        if sort_mode == SortingModeEnum.disabled:
            logger.debug("Sorting disabled, not sorting...")
            return tasks
        
        tasks_sorted = []
        sort_option = self._sort_filter_state.sort_state.sort_option
        
        if sort_mode == SortingModeEnum.deadline:    
            match sort_option:
                case DeadlineSortingEnum.closest_to_deadline:
                    tasks_sorted = sorted(tasks, key=lambda task: task.deadline)
                case DeadlineSortingEnum.farthest_to_deadline:
                    tasks_sorted = sorted(tasks, key=lambda task: task.deadline, reverse=True)
        elif sort_mode == SortingModeEnum.alphabetical:
            match sort_option:
                case AlphabeticalSortingEnum.a_to_z:
                    tasks_sorted = sorted(tasks, key=lambda task: task.task)
                case AlphabeticalSortingEnum.z_to_a:
                    tasks_sorted = sorted(tasks, key=lambda task: task.task, reverse=True)
        else:
            logger.error("Invalid sort mode: '%s'", sort_mode)
            return []

        if not tasks_sorted:
            logger.warning("Tasks were not sorted due to invalid sort option: %s", sort_option)
            return []
        
        logger.debug("Tasks sorted using sort option '%s.%s'", sort_option.__class__.__name__, sort_option.name)
        return tasks_sorted


class TaskInfoDialog(QDialog):
    addTaskRequested = Signal(EditedSubjectTask)
    editTaskRequested = Signal(EditedTaskWithID)

    def __init__(self, /, parent: TaskTodosController):
        super().__init__(parent.mw_parent)
        self.ui = Ui_AddTaskDialog()
        
        self.todo_parent = parent

        self._emit_as: EmitDialogInfoAs = None
        self._data: SubjectTask | None = None

        self.ui.setupUi(self)
        self.ui.categoryComboBox.addItems([
            BuiltinCategories(val).name.capitalize().replace("_", " ")
            for val in range(0, BuiltinCategories.custom + 1)
        ])

    def reset_data(self, subjects: list[str], emit_as: EmitDialogInfoAs = EmitDialogInfoAs.add):
        self._emit_as = emit_as
        self._data = None

        self.ui.categoryComboBox.setCurrentIndex(0)

        self.ui.subjectComboBox.clear()
        self.ui.subjectComboBox.addItems(subjects)

        self.ui.deadlineDateTimeEdit.setDateTime(QDateTime.currentDateTimeUtc())
        self.ui.taskPlainTextEdit.setPlainText('')

    def set_existing_data(self, data: SubjectTask):
        py_date = data.deadline.timestamp()
        qt_date = QDateTime.fromSecsSinceEpoch(int(py_date), Qt.TimeSpec.UTC)

        self.ui.deadlineDateTimeEdit.setDateTime(qt_date)
        self.ui.taskPlainTextEdit.setPlainText(data.task)

        self.ui.subjectComboBox.setCurrentText(data.subject)
        self.ui.categoryComboBox.setCurrentIndex(data.category)

        self._data = data

    def accept(self):
        task = self.ui.taskPlainTextEdit.toPlainText()
        subject = self.ui.subjectComboBox.currentText()

        qt_deadline = self.ui.deadlineDateTimeEdit.dateTime()
        py_deadline: datetime = qt_deadline.toPython()

        aware_deadline: datetime = py_deadline.astimezone(timezone.utc)
        category = self.ui.categoryComboBox.currentIndex()

        data = EditedSubjectTask(
            subject=subject,
            category=category,
            deadline=aware_deadline,
            task=task
        )

        if self._emit_as == EmitDialogInfoAs.add:
            self.addTaskRequested.emit(data)
        elif self._emit_as == EmitDialogInfoAs.edit:
            assert self._data is not None, "Edit data is invalid"

            with_id_data = EditedTaskWithID(
                task_id=self._data.task_id, 
                completed=self._data.completed,
                **data.model_dump()
            )
            self.editTaskRequested.emit(with_id_data)
        
        return super().accept()
