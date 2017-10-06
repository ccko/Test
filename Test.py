
# coding: utf-8

# In[6]:


import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from multiprocessing import freeze_support
import traceback
import test_ui
from test_ui import Ui_MainWindow

class MyApp(Ui_MainWindow):
    def __init__(self, window):
        Ui_MainWindow.__init__(self)
        self.setupUi(window)
        
if __name__ == "__main__":
    freeze_support()
    try:
        app = QtWidgets.QApplication(sys.argv)
        window = QtWidgets.QMainWindow()
        prog = MyApp(window)
        window.show()
        app.exec_()
      
    except:
        var = traceback.format_exc()

