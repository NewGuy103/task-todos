import logging
import typing

from datetime import datetime, timedelta, UTC

from PySide6.QtCore import QObject, Qt, Signal, Slot, QDateTime
from PySide6.QtWidgets import QMessageBox, QDialogButtonBox

from ..models import (
    BuiltinCategories,
    DeadlineFilterState,
    DeadlineSortingEnum,
    SortState,
    FilterState,
    SortAndFilterState,
    AlphabeticalSortingEnum,
    SortingModeEnum,
    FilterCompletedTasksEnum,
)

if typing.TYPE_CHECKING:
    from ..main import MainWindow


logger: logging.Logger = logging.getLogger("task-todos")


class SortFilterOptionsController(QObject):
    updateSortFilterState = Signal(SortAndFilterState)

    def __init__(self, mw_parent: "MainWindow"):
        super().__init__(mw_parent)
        self.mw_parent = mw_parent

        self.ui = mw_parent.ui
        self.app_data = mw_parent.app_data

        self.setup()

    def setup(self):
        self.ui.categoryFilterComboBox.addItems(
            [
                BuiltinCategories(val).name.capitalize().replace("_", " ")
                for val in range(0, BuiltinCategories.custom + 1)
            ]
        )

        self.ui.actionSorting_options.triggered.connect(self.switch_to_sorting_tab)
        self.ui.actionFiltering_options.triggered.connect(self.switch_to_filtering_tab)

        self.ui.sortAndFilterButtonBox.clicked.connect(self.buttonbox_clicked)
        self.ui.sortingModeComboBox.currentIndexChanged.connect(self.auto_toggle_sort_option_enabled)

        future_dt = datetime.now(UTC) + timedelta(weeks=12)  # 3 mo.
        qt_date = QDateTime.fromSecsSinceEpoch(int(future_dt.timestamp()), Qt.TimeSpec.UTC)

        self.ui.notBeforeDeadlineDateTimeEdit.setDateTime(QDateTime.currentDateTimeUtc())
        self.ui.notAfterDeadlineDateTimeEdit.setDateTime(qt_date)

    @Slot()
    def switch_to_sorting_tab(self):
        self.ui.mainStackedWidget.setCurrentIndex(1)
        self.ui.sortAndFilterTabWidget.setCurrentIndex(0)

        self._set_normal_defaults()

    @Slot()
    def switch_to_filtering_tab(self):
        self.ui.mainStackedWidget.setCurrentIndex(1)
        self.ui.sortAndFilterTabWidget.setCurrentIndex(1)

        self._set_normal_defaults()

    @Slot()
    def auto_toggle_sort_option_enabled(self, index: int):
        self.ui.sortingOptionComboBox.clear()

        match index:
            case SortingModeEnum.disabled:
                self.ui.sortingOptionComboBox.setEnabled(False)
                return
            case SortingModeEnum.deadline:
                self.ui.sortingOptionComboBox.addItems(
                    [
                        DeadlineSortingEnum(val).name.capitalize().replace("_", " ")
                        for val in range(0, DeadlineSortingEnum.farthest_to_deadline + 1)
                    ]
                )
            case SortingModeEnum.alphabetical:
                self.ui.sortingOptionComboBox.addItems(
                    [
                        AlphabeticalSortingEnum(val).name.capitalize().replace("_", " ")
                        for val in range(0, AlphabeticalSortingEnum.z_to_a + 1)
                    ]
                )
            case _:
                self.ui.sortingOptionComboBox.setEnabled(False)
                return

        self.ui.sortingOptionComboBox.setEnabled(True)

    def _set_normal_defaults(self):
        self.ui.subjectFilterComboBox.clear()
        self.ui.subjectFilterComboBox.addItems(self.app_data.subjects)

    def _reset_all(self):
        btn = QMessageBox.information(
            self.mw_parent,
            "Task to-dos - Reset to defaults",
            "Do you want to reset all sorting and filtering options to their default?",
            buttons=QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            defaultButton=QMessageBox.StandardButton.No,
        )
        if btn == QMessageBox.StandardButton.No:
            return

        future_dt = datetime.now(UTC) + timedelta(weeks=12)  # 3 mo.
        qt_date = QDateTime.fromSecsSinceEpoch(int(future_dt.timestamp()), Qt.TimeSpec.UTC)

        self.ui.notBeforeDeadlineDateTimeEdit.setDateTime(QDateTime.currentDateTimeUtc())
        self.ui.notAfterDeadlineDateTimeEdit.setDateTime(qt_date)

        self.ui.subjectFilterIncludeAllRadioButton.setChecked(True)
        self.ui.categoryFilterRulesIncludeAllRadioButton.setChecked(True)

        self.ui.enableDeadlineFilterCheckBox.setChecked(False)
        self.ui.sortingModeComboBox.setCurrentIndex(SortingModeEnum.disabled)

        self.ui.dontSortAlphabeticallyRadioButton.setChecked(True)

    @Slot()
    def buttonbox_clicked(self, btn):
        role = self.ui.sortAndFilterButtonBox.buttonRole(btn)

        match role:
            case QDialogButtonBox.ButtonRole.DestructiveRole:
                self.ui.mainStackedWidget.setCurrentIndex(0)
            case QDialogButtonBox.ButtonRole.ResetRole:
                self._reset_all()
            case QDialogButtonBox.ButtonRole.ApplyRole:
                self.update_sort_filter()

    def update_sort_filter(self):
        not_before_date = self.ui.notBeforeDeadlineDateTimeEdit.dateTime().toPython().astimezone(UTC)
        not_after_date = self.ui.notAfterDeadlineDateTimeEdit.dateTime().toPython().astimezone(UTC)

        if self.ui.subjectFilterRulesFilterNormallyRadioButton.isChecked():
            subject_idx = self.ui.subjectFilterComboBox.currentIndex()
            subject = self.app_data.subjects[subject_idx]
        elif self.ui.subjectFilterIncludeAllRadioButton.isChecked():
            subject = True
        elif self.ui.subjectFilterRulesDontIncludeRadioButton.isChecked():
            subject = False
        else:
            subject = False

        if self.ui.categoryFilterRulesFilterNormallyRadioButton.isChecked():
            category_idx = self.ui.categoryFilterComboBox.currentIndex()
            category = category_idx
        elif self.ui.categoryFilterRulesIncludeAllRadioButton.isChecked():
            category = True
        elif self.ui.categoryFilterRulesDontIncludeRadioButton.isChecked():
            category = False
        else:
            category = False

        if self.ui.filterCompletedTasksCompleteRadioButton.isChecked():
            filter_completed = FilterCompletedTasksEnum.complete
        elif self.ui.filterCompletedTasksIncompleteRadioButton.isChecked():
            filter_completed = FilterCompletedTasksEnum.incomplete
        elif self.ui.filterCompletedTasksDontFilterRadioButton.isChecked():
            filter_completed = FilterCompletedTasksEnum.dont_filter
        else:
            filter_completed = FilterCompletedTasksEnum.dont_filter

        idx = self.ui.sortingOptionComboBox.currentIndex()
        sort_state = SortState(
            sort_mode=self.ui.sortingModeComboBox.currentIndex(), sort_option=idx if idx != -1 else None
        )

        deadline_filter = DeadlineFilterState(
            enabled=self.ui.enableDeadlineFilterCheckBox.isChecked(),
            not_before=not_before_date,
            not_after=not_after_date,
        )
        filter_state = FilterState(
            subject=subject, category=category, deadline=deadline_filter, completed=filter_completed
        )

        full_state = SortAndFilterState(sort_state=sort_state, filter_state=filter_state)
        self.updateSortFilterState.emit(full_state)
        self.ui.mainStackedWidget.setCurrentIndex(0)
