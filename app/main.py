import sys
import traceback
import webbrowser

from PySide6.QtGui import QCloseEvent
from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QHeaderView, QStyledItemDelegate

from .config import AppData, setup_logger
from .ui.main import Ui_MainWindow

from .controllers.tasks import TaskTodosController
from .controllers.sort_filter import SortFilterOptionsController


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.todos_ctrl: TaskTodosController = None
        self.sort_filter_ctrl: SortFilterOptionsController = None

        self.app_data: AppData = None

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.mainStackedWidget.setCurrentIndex(0)
        self.ui.actionHow_to_use.triggered.connect(lambda: webbrowser.open('https://newguy103.github.io/task-todos/guide/'))

        self.ui.actionSource_code.triggered.connect(lambda: webbrowser.open('https://github.com/newguy103/task-todos'))
        self.setup()
    
    def setup(self):
        try:
            self.app_data = AppData()
        except Exception as exc:
            tb: str = ''.join(traceback.format_exception(exc, limit=1))

            QMessageBox.critical(
                self, 'PasswordManager - Client',
                f"Could not load configuration, exiting.\nTraceback:\n\n{tb}"
            )

            QTimer.singleShot(0, self.close)
            return
        
        setup_logger(self.app_data.log_level)
        header = self.ui.tasksTableView.horizontalHeader()
        
        self.ui.tasksTableView.setWordWrap(False)
        self.ui.tasksTableView.setItemDelegate(QStyledItemDelegate())

        header.setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)
        header.setStretchLastSection(True)
        
        self.todos_ctrl = TaskTodosController(self)
        self.sort_filter_ctrl = SortFilterOptionsController(self)

        self.sort_filter_ctrl.updateSortFilterState.connect(self.todos_ctrl.update_sort_filter_state)
    
    def closeEvent(self, event: QCloseEvent):
        event.accept()
        return super().closeEvent(event)


def main():
    app = QApplication(sys.argv)

    mw = MainWindow()  # type: ignore
    mw.show()
    
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
