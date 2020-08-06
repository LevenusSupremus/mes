# -*- coding: utf-8 -*-


from PyQt5 import  QtWidgets
import clientui
import requests

class MyWindow(QtWidgets.QMainWindow, clientui.Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.send.pressed.connect(self.send_message)

    def send_message(self):
        name = self.name.text()
        text =  self.text.toPlainText()

        data = {'name' : name, 'text' : text}
        try:
            response = requests.post('http://127.0.0.1:5000/send',json=data)
        except:
            self.messages.append('Server is unavailable, try later...\n')
            self.messages.repaint()
            return 
        if response.status_code != 200:
            self.messages.append('Server is unavailable, try later...\n')
            self.messages.repaint()
            return

        self.text.setText(' ')
        self.text.repaint()


app = QtWidgets.QApplication([])
window = MyWindow()
window.show()
app.exec_()