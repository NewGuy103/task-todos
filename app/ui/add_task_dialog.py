# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_task_dialog.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QApplication, QComboBox, QDateTimeEdit,
    QDialog, QDialogButtonBox, QFormLayout, QFrame,
    QLabel, QPlainTextEdit, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_AddTaskDialog(object):
    def setupUi(self, AddTaskDialog):
        if not AddTaskDialog.objectName():
            AddTaskDialog.setObjectName(u"AddTaskDialog")
        AddTaskDialog.setWindowModality(Qt.WindowModality.WindowModal)
        AddTaskDialog.resize(400, 300)
        self.verticalLayout = QVBoxLayout(AddTaskDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.mainDialogFrame = QFrame(AddTaskDialog)
        self.mainDialogFrame.setObjectName(u"mainDialogFrame")
        self.mainDialogFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.mainDialogFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.mainDialogFrame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.subjectLabel = QLabel(self.mainDialogFrame)
        self.subjectLabel.setObjectName(u"subjectLabel")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.subjectLabel)

        self.subjectComboBox = QComboBox(self.mainDialogFrame)
        self.subjectComboBox.setObjectName(u"subjectComboBox")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.subjectComboBox)

        self.deadlineLabel = QLabel(self.mainDialogFrame)
        self.deadlineLabel.setObjectName(u"deadlineLabel")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.deadlineLabel)

        self.deadlineDateTimeEdit = QDateTimeEdit(self.mainDialogFrame)
        self.deadlineDateTimeEdit.setObjectName(u"deadlineDateTimeEdit")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.deadlineDateTimeEdit)

        self.taskLabel = QLabel(self.mainDialogFrame)
        self.taskLabel.setObjectName(u"taskLabel")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.taskLabel)

        self.taskPlainTextEdit = QPlainTextEdit(self.mainDialogFrame)
        self.taskPlainTextEdit.setObjectName(u"taskPlainTextEdit")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.taskPlainTextEdit)

        self.categoryLabel = QLabel(self.mainDialogFrame)
        self.categoryLabel.setObjectName(u"categoryLabel")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.categoryLabel)

        self.categoryComboBox = QComboBox(self.mainDialogFrame)
        self.categoryComboBox.setObjectName(u"categoryComboBox")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.categoryComboBox)


        self.verticalLayout_2.addLayout(self.formLayout)


        self.verticalLayout.addWidget(self.mainDialogFrame)

        self.dialogButtonBox = QDialogButtonBox(AddTaskDialog)
        self.dialogButtonBox.setObjectName(u"dialogButtonBox")
        self.dialogButtonBox.setOrientation(Qt.Orientation.Horizontal)
        self.dialogButtonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)

        self.verticalLayout.addWidget(self.dialogButtonBox)


        self.retranslateUi(AddTaskDialog)
        self.dialogButtonBox.accepted.connect(AddTaskDialog.accept)
        self.dialogButtonBox.rejected.connect(AddTaskDialog.reject)

        QMetaObject.connectSlotsByName(AddTaskDialog)
    # setupUi

    def retranslateUi(self, AddTaskDialog):
        AddTaskDialog.setWindowTitle(QCoreApplication.translate("AddTaskDialog", u"Task to-dos - Add task", None))
        self.subjectLabel.setText(QCoreApplication.translate("AddTaskDialog", u"Subject:", None))
        self.deadlineLabel.setText(QCoreApplication.translate("AddTaskDialog", u"Deadline:", None))
        self.deadlineDateTimeEdit.setDisplayFormat(QCoreApplication.translate("AddTaskDialog", u"M/d/yy h:mm:ss\u202fAp", None))
        self.taskLabel.setText(QCoreApplication.translate("AddTaskDialog", u"Task:", None))
        self.categoryLabel.setText(QCoreApplication.translate("AddTaskDialog", u"Category:", None))
    # retranslateUi

