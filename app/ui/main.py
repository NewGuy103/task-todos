# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractButton, QAbstractItemView, QApplication, QCheckBox,
    QComboBox, QDateTimeEdit, QDialogButtonBox, QFormLayout,
    QFrame, QHBoxLayout, QHeaderView, QLabel,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QRadioButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QStatusBar, QTabWidget, QTableView, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.actionAdd_task = QAction(MainWindow)
        self.actionAdd_task.setObjectName(u"actionAdd_task")
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.ListAdd))
        self.actionAdd_task.setIcon(icon)
        self.actionRemove_task = QAction(MainWindow)
        self.actionRemove_task.setObjectName(u"actionRemove_task")
        icon1 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.ListRemove))
        self.actionRemove_task.setIcon(icon1)
        self.actionAdd_subject = QAction(MainWindow)
        self.actionAdd_subject.setObjectName(u"actionAdd_subject")
        self.actionAdd_subject.setIcon(icon)
        self.actionRemove_subject = QAction(MainWindow)
        self.actionRemove_subject.setObjectName(u"actionRemove_subject")
        self.actionRemove_subject.setIcon(icon1)
        self.actionHow_to_use = QAction(MainWindow)
        self.actionHow_to_use.setObjectName(u"actionHow_to_use")
        icon2 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.HelpFaq))
        self.actionHow_to_use.setIcon(icon2)
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        self.actionMark_task_completed = QAction(MainWindow)
        self.actionMark_task_completed.setObjectName(u"actionMark_task_completed")
        icon3 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.GoUp))
        self.actionMark_task_completed.setIcon(icon3)
        self.actionEdit_task = QAction(MainWindow)
        self.actionEdit_task.setObjectName(u"actionEdit_task")
        icon4 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.DocumentProperties))
        self.actionEdit_task.setIcon(icon4)
        self.actionSource_code = QAction(MainWindow)
        self.actionSource_code.setObjectName(u"actionSource_code")
        icon5 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.HelpAbout))
        self.actionSource_code.setIcon(icon5)
        self.actionSorting_options = QAction(MainWindow)
        self.actionSorting_options.setObjectName(u"actionSorting_options")
        self.actionSorting_options.setIcon(icon4)
        self.actionFiltering_options = QAction(MainWindow)
        self.actionFiltering_options.setObjectName(u"actionFiltering_options")
        icon6 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.EditFind))
        self.actionFiltering_options.setIcon(icon6)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.mainStackedWidget = QStackedWidget(self.centralwidget)
        self.mainStackedWidget.setObjectName(u"mainStackedWidget")
        self.mainPage = QWidget()
        self.mainPage.setObjectName(u"mainPage")
        self.verticalLayout_2 = QVBoxLayout(self.mainPage)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.tasksLabel = QLabel(self.mainPage)
        self.tasksLabel.setObjectName(u"tasksLabel")
        font = QFont()
        font.setPointSize(12)
        self.tasksLabel.setFont(font)

        self.verticalLayout_2.addWidget(self.tasksLabel)

        self.tasksTableView = QTableView(self.mainPage)
        self.tasksTableView.setObjectName(u"tasksTableView")
        self.tasksTableView.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.tasksTableView.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tasksTableView.setTextElideMode(Qt.TextElideMode.ElideNone)
        self.tasksTableView.setGridStyle(Qt.PenStyle.NoPen)

        self.verticalLayout_2.addWidget(self.tasksTableView)

        self.taskOptionsFrame = QFrame(self.mainPage)
        self.taskOptionsFrame.setObjectName(u"taskOptionsFrame")
        self.taskOptionsFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.taskOptionsFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.taskOptionsFrame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.addTaskButton = QPushButton(self.taskOptionsFrame)
        self.addTaskButton.setObjectName(u"addTaskButton")
        self.addTaskButton.setIcon(icon)

        self.horizontalLayout.addWidget(self.addTaskButton)

        self.removeTaskButton = QPushButton(self.taskOptionsFrame)
        self.removeTaskButton.setObjectName(u"removeTaskButton")
        self.removeTaskButton.setIcon(icon1)

        self.horizontalLayout.addWidget(self.removeTaskButton)

        self.completeTaskButton = QPushButton(self.taskOptionsFrame)
        self.completeTaskButton.setObjectName(u"completeTaskButton")
        self.completeTaskButton.setIcon(icon3)

        self.horizontalLayout.addWidget(self.completeTaskButton)


        self.verticalLayout_2.addWidget(self.taskOptionsFrame)

        self.mainStackedWidget.addWidget(self.mainPage)
        self.sortingRulesPage = QWidget()
        self.sortingRulesPage.setObjectName(u"sortingRulesPage")
        self.verticalLayout_3 = QVBoxLayout(self.sortingRulesPage)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.sortAndFilterTabWidget = QTabWidget(self.sortingRulesPage)
        self.sortAndFilterTabWidget.setObjectName(u"sortAndFilterTabWidget")
        self.sortingTab = QWidget()
        self.sortingTab.setObjectName(u"sortingTab")
        self.horizontalLayout_2 = QHBoxLayout(self.sortingTab)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.sortOptionFormLayout = QFormLayout()
        self.sortOptionFormLayout.setObjectName(u"sortOptionFormLayout")
        self.sortingModeLabel = QLabel(self.sortingTab)
        self.sortingModeLabel.setObjectName(u"sortingModeLabel")

        self.sortOptionFormLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.sortingModeLabel)

        self.sortingModeComboBox = QComboBox(self.sortingTab)
        self.sortingModeComboBox.addItem("")
        self.sortingModeComboBox.addItem("")
        self.sortingModeComboBox.addItem("")
        self.sortingModeComboBox.setObjectName(u"sortingModeComboBox")

        self.sortOptionFormLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.sortingModeComboBox)

        self.sortingOptionLabel = QLabel(self.sortingTab)
        self.sortingOptionLabel.setObjectName(u"sortingOptionLabel")

        self.sortOptionFormLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.sortingOptionLabel)

        self.sortingOptionComboBox = QComboBox(self.sortingTab)
        self.sortingOptionComboBox.setObjectName(u"sortingOptionComboBox")
        self.sortingOptionComboBox.setEnabled(False)

        self.sortOptionFormLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.sortingOptionComboBox)


        self.horizontalLayout_2.addLayout(self.sortOptionFormLayout)

        self.sortAndFilterTabWidget.addTab(self.sortingTab, "")
        self.filterRules = QWidget()
        self.filterRules.setObjectName(u"filterRules")
        self.verticalLayout_4 = QVBoxLayout(self.filterRules)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.filterOptionsFormLayout = QFormLayout()
        self.filterOptionsFormLayout.setObjectName(u"filterOptionsFormLayout")
        self.subjectFilterLabel = QLabel(self.filterRules)
        self.subjectFilterLabel.setObjectName(u"subjectFilterLabel")

        self.filterOptionsFormLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.subjectFilterLabel)

        self.subjectFilterComboBox = QComboBox(self.filterRules)
        self.subjectFilterComboBox.setObjectName(u"subjectFilterComboBox")
        self.subjectFilterComboBox.setEnabled(False)

        self.filterOptionsFormLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.subjectFilterComboBox)

        self.categoryFilterLabel = QLabel(self.filterRules)
        self.categoryFilterLabel.setObjectName(u"categoryFilterLabel")

        self.filterOptionsFormLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.categoryFilterLabel)

        self.categoryFilterComboBox = QComboBox(self.filterRules)
        self.categoryFilterComboBox.setObjectName(u"categoryFilterComboBox")
        self.categoryFilterComboBox.setEnabled(False)

        self.filterOptionsFormLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.categoryFilterComboBox)

        self.deadlineFilterLabel = QLabel(self.filterRules)
        self.deadlineFilterLabel.setObjectName(u"deadlineFilterLabel")

        self.filterOptionsFormLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.deadlineFilterLabel)

        self.deadlineFilterWidget = QWidget(self.filterRules)
        self.deadlineFilterWidget.setObjectName(u"deadlineFilterWidget")
        self.verticalLayout_5 = QVBoxLayout(self.deadlineFilterWidget)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.notBeforeDeadlineLabel = QLabel(self.deadlineFilterWidget)
        self.notBeforeDeadlineLabel.setObjectName(u"notBeforeDeadlineLabel")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.notBeforeDeadlineLabel)

        self.notBeforeDeadlineDateTimeEdit = QDateTimeEdit(self.deadlineFilterWidget)
        self.notBeforeDeadlineDateTimeEdit.setObjectName(u"notBeforeDeadlineDateTimeEdit")
        self.notBeforeDeadlineDateTimeEdit.setEnabled(False)

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.notBeforeDeadlineDateTimeEdit)

        self.notAfterDeadlineLabel = QLabel(self.deadlineFilterWidget)
        self.notAfterDeadlineLabel.setObjectName(u"notAfterDeadlineLabel")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.notAfterDeadlineLabel)

        self.notAfterDeadlineDateTimeEdit = QDateTimeEdit(self.deadlineFilterWidget)
        self.notAfterDeadlineDateTimeEdit.setObjectName(u"notAfterDeadlineDateTimeEdit")
        self.notAfterDeadlineDateTimeEdit.setEnabled(False)

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.notAfterDeadlineDateTimeEdit)

        self.enableDeadlineFilterLabel = QLabel(self.deadlineFilterWidget)
        self.enableDeadlineFilterLabel.setObjectName(u"enableDeadlineFilterLabel")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.enableDeadlineFilterLabel)

        self.enableDeadlineFilterCheckBox = QCheckBox(self.deadlineFilterWidget)
        self.enableDeadlineFilterCheckBox.setObjectName(u"enableDeadlineFilterCheckBox")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.enableDeadlineFilterCheckBox)


        self.verticalLayout_5.addLayout(self.formLayout)


        self.filterOptionsFormLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.deadlineFilterWidget)

        self.subjectFilterRulesLabel = QLabel(self.filterRules)
        self.subjectFilterRulesLabel.setObjectName(u"subjectFilterRulesLabel")

        self.filterOptionsFormLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.subjectFilterRulesLabel)

        self.subjectFilterRulesWidget = QWidget(self.filterRules)
        self.subjectFilterRulesWidget.setObjectName(u"subjectFilterRulesWidget")
        self.horizontalLayout_4 = QHBoxLayout(self.subjectFilterRulesWidget)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.subjectFilterIncludeAllRadioButton = QRadioButton(self.subjectFilterRulesWidget)
        self.subjectFilterIncludeAllRadioButton.setObjectName(u"subjectFilterIncludeAllRadioButton")

        self.horizontalLayout_4.addWidget(self.subjectFilterIncludeAllRadioButton)

        self.subjectFilterRulesFilterNormallyRadioButton = QRadioButton(self.subjectFilterRulesWidget)
        self.subjectFilterRulesFilterNormallyRadioButton.setObjectName(u"subjectFilterRulesFilterNormallyRadioButton")

        self.horizontalLayout_4.addWidget(self.subjectFilterRulesFilterNormallyRadioButton)

        self.subjectFilterRulesDontIncludeRadioButton = QRadioButton(self.subjectFilterRulesWidget)
        self.subjectFilterRulesDontIncludeRadioButton.setObjectName(u"subjectFilterRulesDontIncludeRadioButton")
        self.subjectFilterRulesDontIncludeRadioButton.setChecked(True)

        self.horizontalLayout_4.addWidget(self.subjectFilterRulesDontIncludeRadioButton)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)


        self.filterOptionsFormLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.subjectFilterRulesWidget)

        self.categoryFilterRulesLabel = QLabel(self.filterRules)
        self.categoryFilterRulesLabel.setObjectName(u"categoryFilterRulesLabel")

        self.filterOptionsFormLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.categoryFilterRulesLabel)

        self.categoryFilterRulesWidget = QWidget(self.filterRules)
        self.categoryFilterRulesWidget.setObjectName(u"categoryFilterRulesWidget")
        self.horizontalLayout_5 = QHBoxLayout(self.categoryFilterRulesWidget)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.categoryFilterRulesIncludeAllRadioButton = QRadioButton(self.categoryFilterRulesWidget)
        self.categoryFilterRulesIncludeAllRadioButton.setObjectName(u"categoryFilterRulesIncludeAllRadioButton")

        self.horizontalLayout_5.addWidget(self.categoryFilterRulesIncludeAllRadioButton)

        self.categoryFilterRulesFilterNormallyRadioButton = QRadioButton(self.categoryFilterRulesWidget)
        self.categoryFilterRulesFilterNormallyRadioButton.setObjectName(u"categoryFilterRulesFilterNormallyRadioButton")

        self.horizontalLayout_5.addWidget(self.categoryFilterRulesFilterNormallyRadioButton)

        self.categoryFilterRulesDontIncludeRadioButton = QRadioButton(self.categoryFilterRulesWidget)
        self.categoryFilterRulesDontIncludeRadioButton.setObjectName(u"categoryFilterRulesDontIncludeRadioButton")
        self.categoryFilterRulesDontIncludeRadioButton.setChecked(True)

        self.horizontalLayout_5.addWidget(self.categoryFilterRulesDontIncludeRadioButton)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_3)


        self.filterOptionsFormLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.categoryFilterRulesWidget)

        self.completedTasksLabel = QLabel(self.filterRules)
        self.completedTasksLabel.setObjectName(u"completedTasksLabel")

        self.filterOptionsFormLayout.setWidget(5, QFormLayout.ItemRole.LabelRole, self.completedTasksLabel)

        self.completedTasksWidget = QWidget(self.filterRules)
        self.completedTasksWidget.setObjectName(u"completedTasksWidget")
        self.horizontalLayout_3 = QHBoxLayout(self.completedTasksWidget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.filterCompletedTasksCompleteRadioButton = QRadioButton(self.completedTasksWidget)
        self.filterCompletedTasksCompleteRadioButton.setObjectName(u"filterCompletedTasksCompleteRadioButton")

        self.horizontalLayout_3.addWidget(self.filterCompletedTasksCompleteRadioButton)

        self.filterCompletedTasksIncompleteRadioButton = QRadioButton(self.completedTasksWidget)
        self.filterCompletedTasksIncompleteRadioButton.setObjectName(u"filterCompletedTasksIncompleteRadioButton")

        self.horizontalLayout_3.addWidget(self.filterCompletedTasksIncompleteRadioButton)

        self.filterCompletedTasksDontFilterRadioButton = QRadioButton(self.completedTasksWidget)
        self.filterCompletedTasksDontFilterRadioButton.setObjectName(u"filterCompletedTasksDontFilterRadioButton")
        self.filterCompletedTasksDontFilterRadioButton.setChecked(True)

        self.horizontalLayout_3.addWidget(self.filterCompletedTasksDontFilterRadioButton)

        self.horizontalSpacer_4 = QSpacerItem(317, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_4)


        self.filterOptionsFormLayout.setWidget(5, QFormLayout.ItemRole.FieldRole, self.completedTasksWidget)


        self.verticalLayout_4.addLayout(self.filterOptionsFormLayout)

        self.sortAndFilterTabWidget.addTab(self.filterRules, "")

        self.verticalLayout_3.addWidget(self.sortAndFilterTabWidget)

        self.sortAndFilterButtonBox = QDialogButtonBox(self.sortingRulesPage)
        self.sortAndFilterButtonBox.setObjectName(u"sortAndFilterButtonBox")
        self.sortAndFilterButtonBox.setStandardButtons(QDialogButtonBox.StandardButton.Apply|QDialogButtonBox.StandardButton.Discard|QDialogButtonBox.StandardButton.Reset)
        self.sortAndFilterButtonBox.setCenterButtons(False)

        self.verticalLayout_3.addWidget(self.sortAndFilterButtonBox)

        self.mainStackedWidget.addWidget(self.sortingRulesPage)

        self.verticalLayout.addWidget(self.mainStackedWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 20))
        self.menuDeadlines = QMenu(self.menubar)
        self.menuDeadlines.setObjectName(u"menuDeadlines")
        self.menuSubject = QMenu(self.menubar)
        self.menuSubject.setObjectName(u"menuSubject")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        self.menuSort_Filter = QMenu(self.menubar)
        self.menuSort_Filter.setObjectName(u"menuSort_Filter")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
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
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Task To-dos", None))
        self.actionAdd_task.setText(QCoreApplication.translate("MainWindow", u"Add task", None))
        self.actionRemove_task.setText(QCoreApplication.translate("MainWindow", u"Remove task", None))
        self.actionAdd_subject.setText(QCoreApplication.translate("MainWindow", u"Add subject", None))
        self.actionRemove_subject.setText(QCoreApplication.translate("MainWindow", u"Remove subject", None))
        self.actionHow_to_use.setText(QCoreApplication.translate("MainWindow", u"How to use", None))
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.actionMark_task_completed.setText(QCoreApplication.translate("MainWindow", u"Mark task completed", None))
        self.actionEdit_task.setText(QCoreApplication.translate("MainWindow", u"Edit task", None))
        self.actionSource_code.setText(QCoreApplication.translate("MainWindow", u"Source code", None))
        self.actionSorting_options.setText(QCoreApplication.translate("MainWindow", u"Sorting Options", None))
        self.actionFiltering_options.setText(QCoreApplication.translate("MainWindow", u"Filtering Options", None))
        self.tasksLabel.setText(QCoreApplication.translate("MainWindow", u"Upcoming tasks:", None))
        self.addTaskButton.setText(QCoreApplication.translate("MainWindow", u"Add task", None))
        self.removeTaskButton.setText(QCoreApplication.translate("MainWindow", u"Remove task", None))
        self.completeTaskButton.setText(QCoreApplication.translate("MainWindow", u"Mark task completed", None))
        self.sortingModeLabel.setText(QCoreApplication.translate("MainWindow", u"Sorting Mode:", None))
        self.sortingModeComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Don't sort", None))
        self.sortingModeComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Deadline", None))
        self.sortingModeComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Alphabetical", None))

        self.sortingOptionLabel.setText(QCoreApplication.translate("MainWindow", u"Sorting Option:", None))
        self.sortAndFilterTabWidget.setTabText(self.sortAndFilterTabWidget.indexOf(self.sortingTab), QCoreApplication.translate("MainWindow", u"Sorting Options", None))
        self.subjectFilterLabel.setText(QCoreApplication.translate("MainWindow", u"Subject Filter:", None))
        self.categoryFilterLabel.setText(QCoreApplication.translate("MainWindow", u"Category Filter:", None))
        self.deadlineFilterLabel.setText(QCoreApplication.translate("MainWindow", u"Deadline Filter:", None))
        self.notBeforeDeadlineLabel.setText(QCoreApplication.translate("MainWindow", u"Not before:", None))
        self.notBeforeDeadlineDateTimeEdit.setDisplayFormat(QCoreApplication.translate("MainWindow", u"M/d/yy h:mm:ss\u202fAp", None))
        self.notAfterDeadlineLabel.setText(QCoreApplication.translate("MainWindow", u"Not after:", None))
        self.notAfterDeadlineDateTimeEdit.setDisplayFormat(QCoreApplication.translate("MainWindow", u"M/d/yy h:mm:ss\u202fAp", None))
        self.enableDeadlineFilterLabel.setText(QCoreApplication.translate("MainWindow", u"Enable deadline filter:", None))
        self.subjectFilterRulesLabel.setText(QCoreApplication.translate("MainWindow", u"Subject Filter Rules:", None))
        self.subjectFilterIncludeAllRadioButton.setText(QCoreApplication.translate("MainWindow", u"Include all", None))
        self.subjectFilterRulesFilterNormallyRadioButton.setText(QCoreApplication.translate("MainWindow", u"Filter normally", None))
        self.subjectFilterRulesDontIncludeRadioButton.setText(QCoreApplication.translate("MainWindow", u"Don't include", None))
        self.categoryFilterRulesLabel.setText(QCoreApplication.translate("MainWindow", u"Category Filter Rules:", None))
        self.categoryFilterRulesIncludeAllRadioButton.setText(QCoreApplication.translate("MainWindow", u"Include all", None))
        self.categoryFilterRulesFilterNormallyRadioButton.setText(QCoreApplication.translate("MainWindow", u"Filter normally", None))
        self.categoryFilterRulesDontIncludeRadioButton.setText(QCoreApplication.translate("MainWindow", u"Don't include", None))
        self.completedTasksLabel.setText(QCoreApplication.translate("MainWindow", u"Filter Completed Tasks:", None))
        self.filterCompletedTasksCompleteRadioButton.setText(QCoreApplication.translate("MainWindow", u"Complete", None))
        self.filterCompletedTasksIncompleteRadioButton.setText(QCoreApplication.translate("MainWindow", u"Incomplete", None))
        self.filterCompletedTasksDontFilterRadioButton.setText(QCoreApplication.translate("MainWindow", u"Don't filter", None))
        self.sortAndFilterTabWidget.setTabText(self.sortAndFilterTabWidget.indexOf(self.filterRules), QCoreApplication.translate("MainWindow", u"Filtering Options", None))
        self.menuDeadlines.setTitle(QCoreApplication.translate("MainWindow", u"Tasks", None))
        self.menuSubject.setTitle(QCoreApplication.translate("MainWindow", u"Subjects", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
        self.menuSort_Filter.setTitle(QCoreApplication.translate("MainWindow", u"Sort/Filter", None))
    # retranslateUi

