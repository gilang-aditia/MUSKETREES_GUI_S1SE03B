# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector as mc
import random
from PyQt5.QtWidgets import QApplication,QPlainTextEdit, QWidget, QLineEdit, QPushButton, QVBoxLayout, QLabel,QComboBox,QSpinBox



class windowSukses(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Error')
        self.setFixedWidth(260)
        self.setStyleSheet("""
            
            QLabel{
                font-size: 15px
            }
            """)
        mainLayout = QVBoxLayout()
        
        self.nama = QLabel()
        self.ok = QPushButton('OK')
        mainLayout.addWidget(self.nama)
        mainLayout.addWidget(self.ok)
        self.nama.setText('Jumlah Anggota tidak boleh Kosong')
        self.ok.clicked.connect(self.close)
        mainLayout.addWidget(self.ok)

        self.setLayout(mainLayout)

    def displayInfo(self):
        self.show()

class Hasil(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Hasil')
        self.setFixedWidth(500)
        self.setStyleSheet("""
            QLineEdit{
                font-size: 30px
            }
            QPushButton{
                font-size: 30px
            }
            QComboBox{
                font-size: 30px
            }
            QPlainTextEdit{
                font-size: 20px
            }
            """)
        mainLayout = QVBoxLayout()

        self.text2 = QPlainTextEdit()
        mainLayout.addWidget(self.text2)


        self.setLayout(mainLayout)
        
    def closeEvent(self, event):
        self.text2.clear()
        event.accept()

    def displayInfo(self):
        self.show()

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(575, 420)
        Form.setFixedSize(575,420)
        self.windowOke = windowSukses()
        self.secondWin = Hasil()
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(30, 40, 141, 16))
        self.label.setStyleSheet("*\n"
"{\n"
"    font-size:20px;\n"
"    color:#FFFFFF;\n"
"}")
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(30, 70, 231, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(400, 40, 91, 16))
        self.label_3.setStyleSheet("*\n"
"{\n"
"    font-size:20px;\n"
"    color:#FFFFFF;\n"
"}")
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(30, 100, 75, 23))
        self.pushButton.setStyleSheet("QPushButton{\n"
"    background:#FFFFFF;\n"
"    border-radius:10px;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"    color:white;\n"
"    border-radius:10px;\n"
"    background:#7CA5FF;\n"
"}\n"
"*{\n"
"    font-size:14px;\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(30, 160, 75, 23))
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"    background:#FFFFFF;\n"
"    border-radius:10px;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"    color:white;\n"
"    border-radius:10px;\n"
"    background:#7CA5FF;\n"
"}\n"
"*{\n"
"    font-size:14px;\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(30, 195, 235, 31))
        self.label_4.setStyleSheet("*\n"
"{\n"
"    font-size:20px;\n"
"    color:#FFFFFF;\n"
"}")
        self.label_4.setObjectName("label_4")

        self.label4 = QtWidgets.QLabel(Form)
        self.label4.setGeometry(QtCore.QRect(170, 10, 231, 16))
        self.label4.setStyleSheet("*\n"
"{\n"
"    font-size:20px;\n"
"    color:#FFFFFF;\n"
"}")
        self.label4.setObjectName("label4")

        self.lineEdit_3 = QtWidgets.QSpinBox(Form)
        self.lineEdit_3.setGeometry(QtCore.QRect(30, 230, 231, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(100, 280, 131, 51))
        self.pushButton_4.setStyleSheet("QPushButton{\n"
"    background:#FFFFFF;\n"
"    border-radius:10px;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"    color:white;\n"
"    border-radius:10px;\n"
"    background:#7CA5FF;\n"
"}\n"
"*{\n"
"    font-size:18px;\n"
"}")
        self.pushButton_4.setObjectName("pushButton_4")
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(325, 71, 231, 251))
        self.tableWidget.setRowCount(3)
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setHorizontalHeaderLabels(['id','Nama'])
        self.tableWidget.setColumnWidth(0,15)
        self.pushButton_5 = QtWidgets.QPushButton(Form)
        self.pushButton_5.setGeometry(QtCore.QRect(140, 160, 101, 23))
        self.pushButton_5.setStyleSheet("QPushButton{\n"
"    background:#FFFFFF;\n"
"    border-radius:10px;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"    color:white;\n"
"    border-radius:10px;\n"
"    background:#7CA5FF;\n"
"}\n"
"*{\n"
"    font-size:14px;\n"
"}")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton2 = QtWidgets.QPushButton(Form)
        self.pushButton2.setGeometry(QtCore.QRect(140, 100, 75, 23))
        self.pushButton2.setStyleSheet("QPushButton{\n"
"    background:#FFFFFF;\n"
"    border-radius:10px;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"    color:white;\n"
"    border-radius:10px;\n"
"    background:#7CA5FF;\n"
"}\n"
"*{\n"
"    font-size:14px;\n"
"}")
        self.pushButton2.setObjectName("pushButton2")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(0, -1, 581, 421))
        self.frame.setStyleSheet("QFrame{\n"
"    background:#3575FE;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"    color:#FFFFF;\n"
"    border-radius:10px;\n"
"    background:#7CA5FF;\n"
"}\n"
"*{\n"
"    font-size:18px;\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame.raise_()
        self.label.raise_()
        self.lineEdit.raise_()
        self.label_3.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        self.label_4.raise_()
        self.label4.raise_()
        self.lineEdit_3.raise_()
        self.pushButton_4.raise_()
        self.tableWidget.raise_()
        self.pushButton_5.raise_()
        self.pushButton2.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.pushButton.clicked.connect(self.addButtonClick)
        self.pushButton2.clicked.connect(self.selectData)
        self.pushButton_2.clicked.connect(self.hapus)
        self.pushButton_2.clicked.connect(self.selectData)
        self.pushButton_5.clicked.connect(self.hapusAll)
        self.pushButton_5.clicked.connect(self.selectData)
        self.pushButton_4.clicked.connect(self.randomCek)

        mydb = mc.connect(
            host="localhost",
            user="root",
            password="",
            database="randomgg"

        )
        mycursor = mydb.cursor()
        mycursor.execute("SELECT id,nama from hasil")
        result = mycursor.fetchall()
        self.tableWidget.setRowCount(0)

        for row_number,row_data in enumerate(result):
            self.tableWidget.insertRow(row_number)
            for column_number,data in enumerate(row_data):
                self.tableWidget.setItem(row_number,column_number,QtWidgets.QTableWidgetItem(str(data)))

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "masukan nama"))
        self.label_3.setText(_translate("Form", "List Nama"))
        self.pushButton.setText(_translate("Form", "Tambah"))
        self.pushButton_2.setText(_translate("Form", "Hapus"))
        self.label_4.setText(_translate("Form", "jumlah anggota pada grup"))
        self.label4.setText(_translate("Form", "Random Team Generator"))
        self.pushButton_4.setText(_translate("Form", "Buat grup"))
        self.pushButton_5.setText(_translate("Form", "Hapus Semua"))
        self.pushButton2.setText(_translate("Form", "Refresh"))

    def addButtonClick(self):
        try:
            nama = self.lineEdit.text()
            mydb = mc.connect(
                host="localhost",
                user="root",
                password="",
                database="randomgg"
            )

            mycursor = mydb.cursor()
            
            query = "INSERT INTO hasil (nama) VALUES (%s)"
            value = (nama,)
            mycursor.execute(query,value)
            mydb.commit()
            self.lineEdit.clear()
            self.selectData()
        except mc.Error as e:
            print('gagal')
            print(nama)

    def selectData(self):
        mydb = mc.connect(
            host="localhost",
            user="root",
            password="",
            database="randomgg"

        )
        mycursor = mydb.cursor()
        mycursor.execute("SELECT id,nama from hasil")
        result = mycursor.fetchall()
        self.tableWidget.setRowCount(0)

        for row_number,row_data in enumerate(result):
            self.tableWidget.insertRow(row_number)
            for column_number,data in enumerate(row_data):
                self.tableWidget.setItem(row_number,column_number,QtWidgets.QTableWidgetItem(str(data)))

    def hapus(self):
        
        try:
            row = self.tableWidget.currentRow()
            thing = self.tableWidget.item(row,0)
            thing1 = self.tableWidget.item(row,1)
            if thing is not None or thing1 is not None and thing.text() != '':
                currentid = (self.tableWidget.item(row, 0).text() )
                mydb = mc.connect(
                host="localhost",
                user="root",
                password="",
                database="randomgg"
                )

                mycursor = mydb.cursor()
                query = "DELETE FROM hasil WHERE id=%s"
                value = (currentid,)
                mycursor.execute(query,value)
                mydb.commit()
        except mc.Error as e:
            print('gagal')

    def hapusAll(self):
        
        try:
            row = self.tableWidget.currentRow()
            thing = self.tableWidget.item(row,0)
            thing1 = self.tableWidget.item(row,1)
            
            mydb = mc.connect(
            host="localhost",
            user="root",
            password="",
            database="randomgg"
            )

            mycursor = mydb.cursor()
            query = "DELETE FROM hasil"
            mycursor.execute(query)
            mydb.commit()
        except mc.Error as e:
            print('gagal')

    def randomCek(self):
        try:
            if self.lineEdit_3.text() != '0':
                mydb = mc.connect(
                    host="localhost",
                    user="root",
                    password="",
                    database="randomgg"

                )
                mycursor = mydb.cursor()
                mycursor.execute("SELECT nama from hasil")
                result = mycursor.fetchall()
                item = []
                participants = [item[0] for item in result] 
                
                members = int(self.lineEdit_3.text())
                random.shuffle(participants)
                for i in range(len(participants) // members + 1):
                    self.secondWin.text2.appendPlainText('')
                    print('==============')
                    print('Kelompok {} Terdiri Dari:'.format(i + 1))
                    group = participants[i*members:i*members + members]
                    self.secondWin.text2.appendPlainText('Kelompok {} Terdiri Dari:'.format(i + 1))
                    for participant in group:
                        print(participant)
                        self.secondWin.text2.appendPlainText(participant)
                        self.secondWin.displayInfo()
            else:
                self.windowOke.displayInfo()
        except mc.Error as e:
            print('gagal')

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
