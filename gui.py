from src.main import *
from math import *
from PyQt5.QtWidgets import QTableWidgetItem

def rejet():
    import Fortran.Pi_rejet
    N = eval(str(ui.lineEdit_Nrejet.text()))
    Pi = Fortran.Pi_rejet.pi_rejet(N)
    erreur = abs(Pi - pi)
    row = ui.tableWidget.rowCount()
    ui.tableWidget.insertRow(row)
    ui.tableWidget.setItem(row, 0, QTableWidgetItem(str(format(N, '.1f'))))
    ui.tableWidget.setItem(row, 1, QTableWidgetItem(str(format(Pi, '.20f'))))
    ui.tableWidget.setItem(row, 2, QTableWidgetItem(str(format(erreur, '.10f'))))

# def plot1():


def remrejet():
    if ui.tableWidget.rowCount() > 0:
        ui.tableWidget.removeRow(ui.tableWidget.rowCount() - 1)

def integral():
    import Fortran.Pi_integral
    N = eval(str(ui.lineEdit_Nintegral.text()))
    Pi = Fortran.Pi_integral.pi_integral(N)
    erreur = abs(Pi - pi)
    row = ui.tableWidget_2.rowCount()
    ui.tableWidget_2.insertRow(row)
    ui.tableWidget_2.setItem(row, 0, QTableWidgetItem(str(format(N, '.1f'))))
    ui.tableWidget_2.setItem(row, 1, QTableWidgetItem(str(format(Pi, '.20f'))))
    ui.tableWidget_2.setItem(row, 2, QTableWidgetItem(str(format(erreur, '.10f'))))

def remintegral():
    if ui.tableWidget_2.rowCount() > 0:
        ui.tableWidget_2.removeRow(ui.tableWidget_2.rowCount() - 1)

def buffon():
    import Fortran.Pi_buffon
    N = eval(str(ui.lineEdit_buffon.text()))
    D = eval(str(ui.lineEdit_d.text()))
    a = eval(str(ui.lineEdit_a.text()))
    Pi = Fortran.Pi_buffon.pi_buffon(N, D, a)
    erreur = abs(Pi - pi)
    row = ui.tableWidget_3.rowCount()
    ui.tableWidget_3.insertRow(row)
    ui.tableWidget_3.setItem(row, 0, QTableWidgetItem(str(format(N, '.1f'))))
    ui.tableWidget_3.setItem(row, 1, QTableWidgetItem(str(format(Pi, '.20f'))))
    ui.tableWidget_3.setItem(row, 2, QTableWidgetItem(str(format(erreur, '.10f'))))

def rombuffon():
    if ui.tableWidget_3.rowCount() > 0:
        ui.tableWidget_3.removeRow(ui.tableWidget_3.rowCount() - 1)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    # ******* calcule de Pi
    #  1 ******* rejet *********
    ui.lineEdit_Nrejet.insert('1.E5')
    ui.lineEdit.insert(str(format(pi, '.35f')))
    ui.tableWidget.setColumnWidth(0, 140)
    ui.tableWidget.setColumnWidth(1, 200)
    ui.tableWidget.setColumnWidth(2, 150)
    ui.calculer1.clicked.connect(rejet)
    ui.suppremer1.clicked.connect(remrejet)
    # ui.plot1.clicked.connect(plot1)# 2 ********* integral ****
    ui.lineEdit_Nintegral.insert('1.E5')
    ui.tableWidget_2.setColumnWidth(0, 140)
    ui.tableWidget_2.setColumnWidth(1, 200)
    ui.tableWidget_2.setColumnWidth(2, 150)
    ui.calculer2.clicked.connect(integral)
    ui.suppremer2.clicked.connect(remintegral)
    # 3 ****** buffon **********
    ui.lineEdit_buffon.insert('1.E5')
    ui.lineEdit_d.insert('10')
    ui.lineEdit_a.insert('5')
    ui.tableWidget_3.setColumnWidth(0, 140)
    ui.tableWidget_3.setColumnWidth(1, 200)
    ui.tableWidget_3.setColumnWidth(2, 150)
    ui.calculer2_2.clicked.connect(buffon)
    ui.suppremer2_2.clicked.connect(rombuffon)
    #     # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    MainWindow.show()
    sys.exit(app.exec_())
