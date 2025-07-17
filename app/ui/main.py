################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import QCoreApplication, QMetaObject, QRect, Qt
from PySide6.QtGui import QAction, QFont, QIcon
from PySide6.QtWidgets import (
    QAbstractItemView,
    QCheckBox,
    QComboBox,
    QDateTimeEdit,
    QDialogButtonBox,
    QFormLayout,
    QFrame,
    QHBoxLayout,
    QLabel,
    QMenu,
    QMenuBar,
    QPushButton,
    QRadioButton,
    QSizePolicy,
    QSpacerItem,
    QStackedWidget,
    QStatusBar,
    QTabWidget,
    QTableView,
    QVBoxLayout,
    QWidget,
)


class Ui_MainWindow:
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.actionAdd_task = QAction(MainWindow)
        self.actionAdd_task.setObjectName("actionAdd_task")
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.ListAdd))
        self.actionAdd_task.setIcon(icon)
        self.actionRemove_task = QAction(MainWindow)
        self.actionRemove_task.setObjectName("actionRemove_task")
        icon1 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.ListRemove))
        self.actionRemove_task.setIcon(icon1)
        self.actionAdd_subject = QAction(MainWindow)
        self.actionAdd_subject.setObjectName("actionAdd_subject")
        self.actionAdd_subject.setIcon(icon)
        self.actionRemove_subject = QAction(MainWindow)
        self.actionRemove_subject.setObjectName("actionRemove_subject")
        self.actionRemove_subject.setIcon(icon1)
        self.actionHow_to_use = QAction(MainWindow)
        self.actionHow_to_use.setObjectName("actionHow_to_use")
        icon2 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.HelpFaq))
        self.actionHow_to_use.setIcon(icon2)
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionMark_task_completed = QAction(MainWindow)
        self.actionMark_task_completed.setObjectName("actionMark_task_completed")
        icon3 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.GoUp))
        self.actionMark_task_completed.setIcon(icon3)
        self.actionEdit_task = QAction(MainWindow)
        self.actionEdit_task.setObjectName("actionEdit_task")
        icon4 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.DocumentProperties))
        self.actionEdit_task.setIcon(icon4)
        self.actionSource_code = QAction(MainWindow)
        self.actionSource_code.setObjectName("actionSource_code")
        icon5 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.HelpAbout))
        self.actionSource_code.setIcon(icon5)
        self.actionSorting_options = QAction(MainWindow)
        self.actionSorting_options.setObjectName("actionSorting_options")
        self.actionSorting_options.setIcon(icon4)
        self.actionFiltering_options = QAction(MainWindow)
        self.actionFiltering_options.setObjectName("actionFiltering_options")
        icon6 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.EditFind))
        self.actionFiltering_options.setIcon(icon6)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.mainStackedWidget = QStackedWidget(self.centralwidget)
        self.mainStackedWidget.setObjectName("mainStackedWidget")
        self.mainPage = QWidget()
        self.mainPage.setObjectName("mainPage")
        self.verticalLayout_2 = QVBoxLayout(self.mainPage)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tasksLabel = QLabel(self.mainPage)
        self.tasksLabel.setObjectName("tasksLabel")
        font = QFont()
        font.setPointSize(12)
        self.tasksLabel.setFont(font)

        self.verticalLayout_2.addWidget(self.tasksLabel)

        self.tasksTableView = QTableView(self.mainPage)
        self.tasksTableView.setObjectName("tasksTableView")
        self.tasksTableView.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.tasksTableView.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tasksTableView.setTextElideMode(Qt.TextElideMode.ElideNone)
        self.tasksTableView.setGridStyle(Qt.PenStyle.NoPen)

        self.verticalLayout_2.addWidget(self.tasksTableView)

        self.taskOptionsFrame = QFrame(self.mainPage)
        self.taskOptionsFrame.setObjectName("taskOptionsFrame")
        self.taskOptionsFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.taskOptionsFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.taskOptionsFrame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.addTaskButton = QPushButton(self.taskOptionsFrame)
        self.addTaskButton.setObjectName("addTaskButton")
        self.addTaskButton.setIcon(icon)

        self.horizontalLayout.addWidget(self.addTaskButton)

        self.removeTaskButton = QPushButton(self.taskOptionsFrame)
        self.removeTaskButton.setObjectName("removeTaskButton")
        self.removeTaskButton.setIcon(icon1)

        self.horizontalLayout.addWidget(self.removeTaskButton)

        self.completeTaskButton = QPushButton(self.taskOptionsFrame)
        self.completeTaskButton.setObjectName("completeTaskButton")
        self.completeTaskButton.setIcon(icon3)

        self.horizontalLayout.addWidget(self.completeTaskButton)

        self.verticalLayout_2.addWidget(self.taskOptionsFrame)

        self.mainStackedWidget.addWidget(self.mainPage)
        self.sortingRulesPage = QWidget()
        self.sortingRulesPage.setObjectName("sortingRulesPage")
        self.verticalLayout_3 = QVBoxLayout(self.sortingRulesPage)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.sortAndFilterTabWidget = QTabWidget(self.sortingRulesPage)
        self.sortAndFilterTabWidget.setObjectName("sortAndFilterTabWidget")
        self.sortingTab = QWidget()
        self.sortingTab.setObjectName("sortingTab")
        self.horizontalLayout_2 = QHBoxLayout(self.sortingTab)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.sortOptionFormLayout = QFormLayout()
        self.sortOptionFormLayout.setObjectName("sortOptionFormLayout")
        self.sortingModeLabel = QLabel(self.sortingTab)
        self.sortingModeLabel.setObjectName("sortingModeLabel")

        self.sortOptionFormLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.sortingModeLabel)

        self.sortingModeComboBox = QComboBox(self.sortingTab)
        self.sortingModeComboBox.addItem("")
        self.sortingModeComboBox.addItem("")
        self.sortingModeComboBox.addItem("")
        self.sortingModeComboBox.setObjectName("sortingModeComboBox")

        self.sortOptionFormLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.sortingModeComboBox)

        self.sortingOptionLabel = QLabel(self.sortingTab)
        self.sortingOptionLabel.setObjectName("sortingOptionLabel")

        self.sortOptionFormLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.sortingOptionLabel)

        self.sortingOptionComboBox = QComboBox(self.sortingTab)
        self.sortingOptionComboBox.setObjectName("sortingOptionComboBox")
        self.sortingOptionComboBox.setEnabled(False)

        self.sortOptionFormLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.sortingOptionComboBox)

        self.horizontalLayout_2.addLayout(self.sortOptionFormLayout)

        self.sortAndFilterTabWidget.addTab(self.sortingTab, "")
        self.filterRules = QWidget()
        self.filterRules.setObjectName("filterRules")
        self.verticalLayout_4 = QVBoxLayout(self.filterRules)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.filterOptionsFormLayout = QFormLayout()
        self.filterOptionsFormLayout.setObjectName("filterOptionsFormLayout")
        self.subjectFilterLabel = QLabel(self.filterRules)
        self.subjectFilterLabel.setObjectName("subjectFilterLabel")

        self.filterOptionsFormLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.subjectFilterLabel)

        self.subjectFilterComboBox = QComboBox(self.filterRules)
        self.subjectFilterComboBox.setObjectName("subjectFilterComboBox")
        self.subjectFilterComboBox.setEnabled(False)

        self.filterOptionsFormLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.subjectFilterComboBox)

        self.categoryFilterLabel = QLabel(self.filterRules)
        self.categoryFilterLabel.setObjectName("categoryFilterLabel")

        self.filterOptionsFormLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.categoryFilterLabel)

        self.categoryFilterComboBox = QComboBox(self.filterRules)
        self.categoryFilterComboBox.setObjectName("categoryFilterComboBox")
        self.categoryFilterComboBox.setEnabled(False)

        self.filterOptionsFormLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.categoryFilterComboBox)

        self.deadlineFilterLabel = QLabel(self.filterRules)
        self.deadlineFilterLabel.setObjectName("deadlineFilterLabel")

        self.filterOptionsFormLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.deadlineFilterLabel)

        self.deadlineFilterWidget = QWidget(self.filterRules)
        self.deadlineFilterWidget.setObjectName("deadlineFilterWidget")
        self.verticalLayout_5 = QVBoxLayout(self.deadlineFilterWidget)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.notBeforeDeadlineLabel = QLabel(self.deadlineFilterWidget)
        self.notBeforeDeadlineLabel.setObjectName("notBeforeDeadlineLabel")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.notBeforeDeadlineLabel)

        self.notBeforeDeadlineDateTimeEdit = QDateTimeEdit(self.deadlineFilterWidget)
        self.notBeforeDeadlineDateTimeEdit.setObjectName("notBeforeDeadlineDateTimeEdit")
        self.notBeforeDeadlineDateTimeEdit.setEnabled(False)

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.notBeforeDeadlineDateTimeEdit)

        self.notAfterDeadlineLabel = QLabel(self.deadlineFilterWidget)
        self.notAfterDeadlineLabel.setObjectName("notAfterDeadlineLabel")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.notAfterDeadlineLabel)

        self.notAfterDeadlineDateTimeEdit = QDateTimeEdit(self.deadlineFilterWidget)
        self.notAfterDeadlineDateTimeEdit.setObjectName("notAfterDeadlineDateTimeEdit")
        self.notAfterDeadlineDateTimeEdit.setEnabled(False)

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.notAfterDeadlineDateTimeEdit)

        self.enableDeadlineFilterLabel = QLabel(self.deadlineFilterWidget)
        self.enableDeadlineFilterLabel.setObjectName("enableDeadlineFilterLabel")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.enableDeadlineFilterLabel)

        self.enableDeadlineFilterCheckBox = QCheckBox(self.deadlineFilterWidget)
        self.enableDeadlineFilterCheckBox.setObjectName("enableDeadlineFilterCheckBox")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.enableDeadlineFilterCheckBox)

        self.verticalLayout_5.addLayout(self.formLayout)

        self.filterOptionsFormLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.deadlineFilterWidget)

        self.subjectFilterRulesLabel = QLabel(self.filterRules)
        self.subjectFilterRulesLabel.setObjectName("subjectFilterRulesLabel")

        self.filterOptionsFormLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.subjectFilterRulesLabel)

        self.subjectFilterRulesWidget = QWidget(self.filterRules)
        self.subjectFilterRulesWidget.setObjectName("subjectFilterRulesWidget")
        self.horizontalLayout_4 = QHBoxLayout(self.subjectFilterRulesWidget)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.subjectFilterIncludeAllRadioButton = QRadioButton(self.subjectFilterRulesWidget)
        self.subjectFilterIncludeAllRadioButton.setObjectName("subjectFilterIncludeAllRadioButton")

        self.horizontalLayout_4.addWidget(self.subjectFilterIncludeAllRadioButton)

        self.subjectFilterRulesFilterNormallyRadioButton = QRadioButton(self.subjectFilterRulesWidget)
        self.subjectFilterRulesFilterNormallyRadioButton.setObjectName("subjectFilterRulesFilterNormallyRadioButton")

        self.horizontalLayout_4.addWidget(self.subjectFilterRulesFilterNormallyRadioButton)

        self.subjectFilterRulesDontIncludeRadioButton = QRadioButton(self.subjectFilterRulesWidget)
        self.subjectFilterRulesDontIncludeRadioButton.setObjectName("subjectFilterRulesDontIncludeRadioButton")
        self.subjectFilterRulesDontIncludeRadioButton.setChecked(True)

        self.horizontalLayout_4.addWidget(self.subjectFilterRulesDontIncludeRadioButton)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)

        self.filterOptionsFormLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.subjectFilterRulesWidget)

        self.categoryFilterRulesLabel = QLabel(self.filterRules)
        self.categoryFilterRulesLabel.setObjectName("categoryFilterRulesLabel")

        self.filterOptionsFormLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.categoryFilterRulesLabel)

        self.categoryFilterRulesWidget = QWidget(self.filterRules)
        self.categoryFilterRulesWidget.setObjectName("categoryFilterRulesWidget")
        self.horizontalLayout_5 = QHBoxLayout(self.categoryFilterRulesWidget)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.categoryFilterRulesIncludeAllRadioButton = QRadioButton(self.categoryFilterRulesWidget)
        self.categoryFilterRulesIncludeAllRadioButton.setObjectName("categoryFilterRulesIncludeAllRadioButton")

        self.horizontalLayout_5.addWidget(self.categoryFilterRulesIncludeAllRadioButton)

        self.categoryFilterRulesFilterNormallyRadioButton = QRadioButton(self.categoryFilterRulesWidget)
        self.categoryFilterRulesFilterNormallyRadioButton.setObjectName("categoryFilterRulesFilterNormallyRadioButton")

        self.horizontalLayout_5.addWidget(self.categoryFilterRulesFilterNormallyRadioButton)

        self.categoryFilterRulesDontIncludeRadioButton = QRadioButton(self.categoryFilterRulesWidget)
        self.categoryFilterRulesDontIncludeRadioButton.setObjectName("categoryFilterRulesDontIncludeRadioButton")
        self.categoryFilterRulesDontIncludeRadioButton.setChecked(True)

        self.horizontalLayout_5.addWidget(self.categoryFilterRulesDontIncludeRadioButton)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_3)

        self.filterOptionsFormLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.categoryFilterRulesWidget)

        self.completedTasksLabel = QLabel(self.filterRules)
        self.completedTasksLabel.setObjectName("completedTasksLabel")

        self.filterOptionsFormLayout.setWidget(5, QFormLayout.ItemRole.LabelRole, self.completedTasksLabel)

        self.completedTasksWidget = QWidget(self.filterRules)
        self.completedTasksWidget.setObjectName("completedTasksWidget")
        self.horizontalLayout_3 = QHBoxLayout(self.completedTasksWidget)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.filterCompletedTasksCompleteRadioButton = QRadioButton(self.completedTasksWidget)
        self.filterCompletedTasksCompleteRadioButton.setObjectName("filterCompletedTasksCompleteRadioButton")

        self.horizontalLayout_3.addWidget(self.filterCompletedTasksCompleteRadioButton)

        self.filterCompletedTasksIncompleteRadioButton = QRadioButton(self.completedTasksWidget)
        self.filterCompletedTasksIncompleteRadioButton.setObjectName("filterCompletedTasksIncompleteRadioButton")

        self.horizontalLayout_3.addWidget(self.filterCompletedTasksIncompleteRadioButton)

        self.filterCompletedTasksDontFilterRadioButton = QRadioButton(self.completedTasksWidget)
        self.filterCompletedTasksDontFilterRadioButton.setObjectName("filterCompletedTasksDontFilterRadioButton")
        self.filterCompletedTasksDontFilterRadioButton.setChecked(True)

        self.horizontalLayout_3.addWidget(self.filterCompletedTasksDontFilterRadioButton)

        self.horizontalSpacer_4 = QSpacerItem(317, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_4)

        self.filterOptionsFormLayout.setWidget(5, QFormLayout.ItemRole.FieldRole, self.completedTasksWidget)

        self.verticalLayout_4.addLayout(self.filterOptionsFormLayout)

        self.sortAndFilterTabWidget.addTab(self.filterRules, "")

        self.verticalLayout_3.addWidget(self.sortAndFilterTabWidget)

        self.sortAndFilterButtonBox = QDialogButtonBox(self.sortingRulesPage)
        self.sortAndFilterButtonBox.setObjectName("sortAndFilterButtonBox")
        self.sortAndFilterButtonBox.setStandardButtons(
            QDialogButtonBox.StandardButton.Apply
            | QDialogButtonBox.StandardButton.Discard
            | QDialogButtonBox.StandardButton.Reset
        )
        self.sortAndFilterButtonBox.setCenterButtons(False)

        self.verticalLayout_3.addWidget(self.sortAndFilterButtonBox)

        self.mainStackedWidget.addWidget(self.sortingRulesPage)

        self.verticalLayout.addWidget(self.mainStackedWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName("menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 20))
        self.menuDeadlines = QMenu(self.menubar)
        self.menuDeadlines.setObjectName("menuDeadlines")
        self.menuSubject = QMenu(self.menubar)
        self.menuSubject.setObjectName("menuSubject")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuSort_Filter = QMenu(self.menubar)
        self.menuSort_Filter.setObjectName("menuSort_Filter")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuDeadlines.menuAction())
        self.menubar.addAction(self.menuSubject.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menubar.addAction(self.menuSort_Filter.menuAction())
        self.menuDeadlines.addAction(self.actionAdd_task)
        self.menuDeadlines.addAction(self.actionRemove_task)
        self.menuDeadlines.addAction(self.actionEdit_task)
        self.menuDeadlines.addAction(self.actionMark_task_completed)
        self.menuSubject.addAction(self.actionAdd_subject)
        self.menuSubject.addAction(self.actionRemove_subject)
        self.menuHelp.addAction(self.actionHow_to_use)
        self.menuHelp.addAction(self.actionSource_code)
        self.menuSort_Filter.addAction(self.actionSorting_options)
        self.menuSort_Filter.addAction(self.actionFiltering_options)

        self.retranslateUi(MainWindow)
        self.enableDeadlineFilterCheckBox.toggled.connect(self.notBeforeDeadlineDateTimeEdit.setEnabled)
        self.enableDeadlineFilterCheckBox.toggled.connect(self.notAfterDeadlineDateTimeEdit.setEnabled)
        self.subjectFilterRulesDontIncludeRadioButton.toggled.connect(self.subjectFilterComboBox.setDisabled)
        self.subjectFilterIncludeAllRadioButton.toggled.connect(self.subjectFilterComboBox.setDisabled)
        self.subjectFilterRulesFilterNormallyRadioButton.toggled.connect(self.subjectFilterComboBox.setEnabled)
        self.categoryFilterRulesDontIncludeRadioButton.toggled.connect(self.categoryFilterComboBox.setDisabled)
        self.categoryFilterRulesIncludeAllRadioButton.toggled.connect(self.categoryFilterComboBox.setDisabled)
        self.categoryFilterRulesFilterNormallyRadioButton.toggled.connect(self.categoryFilterComboBox.setEnabled)

        self.mainStackedWidget.setCurrentIndex(1)
        self.sortAndFilterTabWidget.setCurrentIndex(1)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", "Task To-dos", None))
        self.actionAdd_task.setText(QCoreApplication.translate("MainWindow", "Add task", None))
        self.actionRemove_task.setText(QCoreApplication.translate("MainWindow", "Remove task", None))
        self.actionAdd_subject.setText(QCoreApplication.translate("MainWindow", "Add subject", None))
        self.actionRemove_subject.setText(QCoreApplication.translate("MainWindow", "Remove subject", None))
        self.actionHow_to_use.setText(QCoreApplication.translate("MainWindow", "How to use", None))
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", "About", None))
        self.actionMark_task_completed.setText(QCoreApplication.translate("MainWindow", "Mark task completed", None))
        self.actionEdit_task.setText(QCoreApplication.translate("MainWindow", "Edit task", None))
        self.actionSource_code.setText(QCoreApplication.translate("MainWindow", "Source code", None))
        self.actionSorting_options.setText(QCoreApplication.translate("MainWindow", "Sorting Options", None))
        self.actionFiltering_options.setText(QCoreApplication.translate("MainWindow", "Filtering Options", None))
        self.tasksLabel.setText(QCoreApplication.translate("MainWindow", "Upcoming tasks:", None))
        self.addTaskButton.setText(QCoreApplication.translate("MainWindow", "Add task", None))
        self.removeTaskButton.setText(QCoreApplication.translate("MainWindow", "Remove task", None))
        self.completeTaskButton.setText(QCoreApplication.translate("MainWindow", "Mark task completed", None))
        self.sortingModeLabel.setText(QCoreApplication.translate("MainWindow", "Sorting Mode:", None))
        self.sortingModeComboBox.setItemText(0, QCoreApplication.translate("MainWindow", "Don't sort", None))
        self.sortingModeComboBox.setItemText(1, QCoreApplication.translate("MainWindow", "Deadline", None))
        self.sortingModeComboBox.setItemText(2, QCoreApplication.translate("MainWindow", "Alphabetical", None))

        self.sortingOptionLabel.setText(QCoreApplication.translate("MainWindow", "Sorting Option:", None))
        self.sortAndFilterTabWidget.setTabText(
            self.sortAndFilterTabWidget.indexOf(self.sortingTab),
            QCoreApplication.translate("MainWindow", "Sorting Options", None),
        )
        self.subjectFilterLabel.setText(QCoreApplication.translate("MainWindow", "Subject Filter:", None))
        self.categoryFilterLabel.setText(QCoreApplication.translate("MainWindow", "Category Filter:", None))
        self.deadlineFilterLabel.setText(QCoreApplication.translate("MainWindow", "Deadline Filter:", None))
        self.notBeforeDeadlineLabel.setText(QCoreApplication.translate("MainWindow", "Not before:", None))
        self.notBeforeDeadlineDateTimeEdit.setDisplayFormat(
            QCoreApplication.translate("MainWindow", "M/d/yy h:mm:ss\u202fAp", None)
        )
        self.notAfterDeadlineLabel.setText(QCoreApplication.translate("MainWindow", "Not after:", None))
        self.notAfterDeadlineDateTimeEdit.setDisplayFormat(
            QCoreApplication.translate("MainWindow", "M/d/yy h:mm:ss\u202fAp", None)
        )
        self.enableDeadlineFilterLabel.setText(
            QCoreApplication.translate("MainWindow", "Enable deadline filter:", None)
        )
        self.subjectFilterRulesLabel.setText(QCoreApplication.translate("MainWindow", "Subject Filter Rules:", None))
        self.subjectFilterIncludeAllRadioButton.setText(QCoreApplication.translate("MainWindow", "Include all", None))
        self.subjectFilterRulesFilterNormallyRadioButton.setText(
            QCoreApplication.translate("MainWindow", "Filter normally", None)
        )
        self.subjectFilterRulesDontIncludeRadioButton.setText(
            QCoreApplication.translate("MainWindow", "Don't include", None)
        )
        self.categoryFilterRulesLabel.setText(QCoreApplication.translate("MainWindow", "Category Filter Rules:", None))
        self.categoryFilterRulesIncludeAllRadioButton.setText(
            QCoreApplication.translate("MainWindow", "Include all", None)
        )
        self.categoryFilterRulesFilterNormallyRadioButton.setText(
            QCoreApplication.translate("MainWindow", "Filter normally", None)
        )
        self.categoryFilterRulesDontIncludeRadioButton.setText(
            QCoreApplication.translate("MainWindow", "Don't include", None)
        )
        self.completedTasksLabel.setText(QCoreApplication.translate("MainWindow", "Filter Completed Tasks:", None))
        self.filterCompletedTasksCompleteRadioButton.setText(QCoreApplication.translate("MainWindow", "Complete", None))
        self.filterCompletedTasksIncompleteRadioButton.setText(
            QCoreApplication.translate("MainWindow", "Incomplete", None)
        )
        self.filterCompletedTasksDontFilterRadioButton.setText(
            QCoreApplication.translate("MainWindow", "Don't filter", None)
        )
        self.sortAndFilterTabWidget.setTabText(
            self.sortAndFilterTabWidget.indexOf(self.filterRules),
            QCoreApplication.translate("MainWindow", "Filtering Options", None),
        )
        self.menuDeadlines.setTitle(QCoreApplication.translate("MainWindow", "Tasks", None))
        self.menuSubject.setTitle(QCoreApplication.translate("MainWindow", "Subjects", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", "Help", None))
        self.menuSort_Filter.setTitle(QCoreApplication.translate("MainWindow", "Sort/Filter", None))

    # retranslateUi
