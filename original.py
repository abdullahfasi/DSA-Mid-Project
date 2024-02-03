import os
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog,QApplication, QMessageBox
from PyQt5.uic import loadUi

account_file = "E:\\DSA\\MID PROJECT\\datafile.txt"
class Login(QDialog):
    def __init__(self):
        super(Login,self).__init__()
        loadUi("E:\\DSA\\MID PROJECT\\login.ui",self)
        self.login.clicked.connect(self.loginfunction)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.createaccount.clicked.connect(self.GoTocreateaccount)

    def loginfunction(self):
        email = self.email.text()
        password = self.password.text()

        if not email or not password:
            QMessageBox.critical(self, "Error", "Please fill in both email and password fields.")
            return

        # Check if the email and password match any account in the file

        if not os.path.exists(account_file):
            QMessageBox.critical(self, "Error", "Account file does not exist. Please create an account first.")
            return

        with open(account_file, "r") as file:
            for line in file:
                stored_email, stored_password = line.strip().split(',')
                if email == stored_email and password == stored_password:
                    # Login successful, you can open the main UI form here
                    QMessageBox.information(self, "Success", "Login Successful")

                    mainpage = MainPage()
                    widget.setFixedHeight(569)
                    widget.setFixedWidth(1114)
                    widget.addWidget(mainpage)
                    widget.setCurrentIndex(widget.currentIndex() + 1) 

                    

        #QMessageBox.critical(self, "Error", "Invalid email or password. Please create an account first.")
    def GoTocreateaccount(self):

        createAcc = CreateAccount()
        widget.addWidget(createAcc)
        widget.setCurrentIndex(widget.currentIndex()+1)    

class CreateAccount(QDialog):
    def __init__(self):
        super(CreateAccount,self).__init__()
        loadUi("E:\\DSA\\MID PROJECT\\signup.ui",self)
        self.createaccount2.clicked.connect(self.createaccount)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.confirmpassword.setEchoMode(QtWidgets.QLineEdit.Password)

    def createaccount(self):
        email = self.email.text()
        password = self.password.text()
        confirm_password = self.confirmpassword.text()

        if not email or not password or not confirm_password:
            QMessageBox.critical(self, "Error", "Please fill in all fields.")
            return

        if password != confirm_password:
            QMessageBox.critical(self, "Error", "Passwords do not match.")
            return

        with open(account_file, "a") as file:
            file.write(f"{email},{password}\n")

        QMessageBox.information(self, "Success", "Account created successfully.") 
        login = Login()
        widget.addWidget(login)
        widget.setCurrentIndex(widget.currentIndex() + 1)   

class MainPage(QDialog):
    def __init__(self):
        super(MainPage,self).__init__()
        loadUi("E:\\DSA\\MID PROJECT\\mainpage.ui",self)
        self.exit.clicked.connect(self.exitfunction)

    def exitfunction(self):
        login = Login()
        widget.setFixedHeight(550)
        widget.setFixedWidth(540)
        widget.addWidget(login)
        widget.setCurrentIndex(widget.currentIndex() + 1)     

app = QApplication(sys.argv)
mainwindow = Login()
widget = QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedHeight(550)
widget.setFixedWidth(540)
widget.show()
app.exec_()
