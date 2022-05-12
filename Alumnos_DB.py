import sys, csv
import mysql.connector

from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets
from fpdf import FPDF

class alumnos_DB(QMainWindow):

    def __init__(self):
        super().__init__()
        uic.loadUi(r"alumnos_DB.ui", self)
        self.fn_init_UI()

    #Generacion de Funcion Init_UI
    def fn_init_UI(self):
        #self.fn_connectDB(self) 
        self.btn_Connect_DB.clicked.connect(self.fn_connectDB)
        self.btn_Registrar.clicked.connect(self.fn_registrar)

        # Funcion buscar
        self.btn_Buscar.clicked.connect(self.fn_buscar)

        #Conectar funcion fn_eliminar al boton Eliminar
        self.btn_Eliminar.clicked.connect(self.fn_eliminar)

        # Actualizar
        self.btn_act.clicked.connect(self.fn_actualizar)

        # Gemerar PDF
        self.btn_impdf.clicked.connect(self.f_convpdf)

        #Conectar a Funcion que graba hacia la base de datos
        #self.btn_Grabar.clicked.connect(self.fn_grabar_DB)

    def fn_connectDB(self):
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="bd_alumnos"
        )

        mycursor = mydb.cursor()
        iden = self.edt_matricula.text()
        #val = [iden]
        mycursor.execute("SELECT * FROM alumnos")
        datos = mycursor.fetchall()
        if datos:
            self.Tabla_Datos.setRowCount(len(datos))
            tablerow = 0
            for i in datos:
                #QTableWidget
                self.Tabla_Datos.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(i[1])))
                self.Tabla_Datos.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(str(i[2])))
                self.Tabla_Datos.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(str(i[3])))
                self.Tabla_Datos.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(str(i[4])))
                self.Tabla_Datos.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(str(i[5])))
                self.Tabla_Datos.setItem(tablerow, 5, QtWidgets.QTableWidgetItem(str(i[6])))
                self.Tabla_Datos.setItem(tablerow, 6, QtWidgets.QTableWidgetItem(str(i[7])))
                self.Tabla_Datos.setItem(tablerow, 7, QtWidgets.QTableWidgetItem(str(i[8])))
                self.Tabla_Datos.setItem(tablerow, 8, QtWidgets.QTableWidgetItem(str(i[9])))
                self.Tabla_Datos.setItem(tablerow, 9, QtWidgets.QTableWidgetItem(str(i[10])))
                self.Tabla_Datos.setItem(tablerow, 10, QtWidgets.QTableWidgetItem(str(i[11])))
                self.Tabla_Datos.setItem(tablerow, 11, QtWidgets.QTableWidgetItem(str(i[12])))
                self.Tabla_Datos.setItem(tablerow, 12, QtWidgets.QTableWidgetItem(str(i[13])))
                self.Tabla_Datos.setItem(tablerow, 13, QtWidgets.QTableWidgetItem(str(i[14])))
                self.Tabla_Datos.setItem(tablerow, 14, QtWidgets.QTableWidgetItem(str(i[15])))
                self.Tabla_Datos.setItem(tablerow, 15, QtWidgets.QTableWidgetItem(str(i[16])))
                self.Tabla_Datos.setItem(tablerow, 16, QtWidgets.QTableWidgetItem(str(i[17])))
                self.Tabla_Datos.setItem(tablerow, 17, QtWidgets.QTableWidgetItem(str(i[18])))
                tablerow = tablerow + 1
        print("Conexión a base de datos exitosa")

    #Grabar hacia la base de datos
    def fn_registrar(self):
        #self.edt_matricula.setText("Funcion Registras a Base de Datos")
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="bd_alumnos"
        )

        mycursor = mydb.cursor()

        sql = "INSERT INTO alumnos (matricula, nombres, a_paterno, a_materno, domicilio, ciudad, estado, carrera, sexo, edad, beca, foraneo, ingles, prog, bd, contab,estadistica,inv_op) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        #val = (self.edt_matricula.text(),self.edt_nombre.text(), self.edt_apppat.text(), self.edt_appmat.text(),self.edt_domicilio.text(),self.cbx_ciudad.currentText(),self.cbx_estado.currentText(),self.cbx_carrera.currentText(), 'M')

        mat = self.edt_matricula.text()
        nom = self.edt_nombre.text()
        app = self.edt_apppat.text()
        apm = self.edt_appmat.text()
        dom = self.edt_domicilio.text()
        mun = self.cbx_ciudad.currentText()
        edo = self.cbx_estado.currentText()
        car = self.cbx_carrera.currentText()
        if self.radio_hombre.isChecked():
            sex = 'M'
        if self.radio_mujer.isChecked():
            sex = 'F'
        #edad
        eda = self.spinEdad.text()

        #beca
        if self.radio_cero.isChecked():
            bec = '0'
        elif self.radio_50.isChecked():
            bec = '50'
        elif self.radio_80.isChecked():
            bec = '80'
        elif self.radio_100.isChecked():
            bec = '100'

        #foraneo
        if self.chk_foraneo.isChecked():
            foraneo = 1
        else:
            foraneo = 0
        #ingles
        if self.chk_ingles.isChecked():
            ingles = 1
        else:
            ingles = 0

        #materias
        if self.chk_prog.isChecked():
            pro = 1
        else:
            pro = 0

        if self.chk_bd.isChecked():
            bad = 1
        else:
            bad = 0

        if self.chk_contab.isChecked():
            contab = 1
        else:
            contab = 0

        if self.chk_estadistica.isChecked():
            esta = 1
        else:
            esta = 0

        if self.chk_inv_op.isChecked():
            inv = 1
        else:
            inv = 0

        val = (mat,nom,app,apm,dom,mun,edo,car,sex,eda,bec,foraneo,ingles,pro,bad,contab,esta,inv)



        print(sql)
        print(val)
        mycursor.execute(sql, val)
        mydb.commit()
        print(mycursor.rowcount, "record inserted.")


        #Generacion de Funcion Consultar
    def fn_consultar(self):
        #self.edt_nombre.setText('Funcion Consultar')
        varb = self.edt_matricula.text()
        #self.edt_matricula.setText("Funcion Registras a Base de Datos")
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="bd_alumnos"
        )

        mycursor = mydb.cursor()

        sql = "SELECT * FROM alumnos WHERE matricula = "+varb

        mycursor.execute(sql)

        myresult = mycursor.fetchall()

        for x in myresult:
            self.edt_matricula.setText(x[1])
            self.edt_nombre.setText(x[2])
            self.edt_apppat.setText(x[3])
            self.edt_appmat.setText(x[4])
            self.edt_domicilio.setText(x[5])
            self.cbx_ciudad.setCurrentText(x[6])
            #--> Agregar funcionalidad del resto de los datos

            #print(x[3])

    def fn_eliminar(self):
        #self.spinedad.setValue(21)
        #self.edt_matricula.setText("Funcion Registras a Base de Datos")
        varb = self.edt_matricula.text()
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="bd_alumnos"
        )

        mycursor = mydb.cursor()
        sql = "DELETE FROM alumnos WHERE matricula = "+varb
        mycursor.execute(sql)
        mydb.commit()
        print(mycursor.rowcount, "record(s) deleted")

    def fn_grabar_DB(self):

        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="bd_alumnos"
        )

        mycursor = mydb.cursor()

        sql = "INSERT INTO alumnos (matricula, nombres, a_paterno, a_materno, domicilio, ciudad, estado, carrera, sexo) VALUES (%s, %s,  %s, %s, %s, %s, %s, %s, %s)"
        val = ""
        #create datafram object recordset
        for row in range(self.Tabla_Datos.rowCount()):
            for col in range(self.Tabla_Datos.columnCount()):
                #var1 = self.Tabla_Datos.item(row,col).text()

                if col == 0:
                    mat=self.Tabla_Datos.item(row,col).text()
                elif col == 1:
                    nom = self.Tabla_Datos.item(row,col).text()
                elif col == 2:
                    app = self.Tabla_Datos.item(row,col).text()
                elif col == 3:
                    apm = self.Tabla_Datos.item(row,col).text()
                elif col == 4:
                    dom = self.Tabla_Datos.item(row,col).text()
                elif col == 5:
                    mun = self.Tabla_Datos.item(row,col).text()
                elif col == 6:
                    edo = self.Tabla_Datos.item(row,col).text()
                elif col == 7:
                    car = self.Tabla_Datos.item(row,col).text()
                elif col == 8:
                    sex = self.Tabla_Datos.item(row,col).text()

            val =(mat,nom,app,apm,dom,mun,edo,car,sex)

            #print(val)
            mycursor.execute(sql, val)
            mydb.commit()
            print(mycursor.rowcount, "record inserted.")

    def fn_buscar(self):
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="bd_alumnos"
        )
        mycursor = mydb.cursor()
        iden = self.edt_matricula.text()
        val = [iden]
        mycursor.execute("SELECT * FROM alumnos where matricula = %s", (val))
        datos = mycursor.fetchall()
        if datos:
            self.Tabla_Datos.setRowCount(1)
            tablerow = 0
            for i in datos:
                #QTableWidget
                self.Tabla_Datos.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(i[1])))
                self.Tabla_Datos.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(str(i[2])))
                self.Tabla_Datos.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(str(i[3])))
                self.Tabla_Datos.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(str(i[4])))
                self.Tabla_Datos.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(str(i[5])))
                self.Tabla_Datos.setItem(tablerow, 5, QtWidgets.QTableWidgetItem(str(i[6])))
                self.Tabla_Datos.setItem(tablerow, 6, QtWidgets.QTableWidgetItem(str(i[7])))
                self.Tabla_Datos.setItem(tablerow, 7, QtWidgets.QTableWidgetItem(str(i[8])))
                self.Tabla_Datos.setItem(tablerow, 8, QtWidgets.QTableWidgetItem(str(i[9])))
                self.Tabla_Datos.setItem(tablerow, 9, QtWidgets.QTableWidgetItem(str(i[10])))
                self.Tabla_Datos.setItem(tablerow, 10, QtWidgets.QTableWidgetItem(str(i[11])))
                self.Tabla_Datos.setItem(tablerow, 11, QtWidgets.QTableWidgetItem(str(i[12])))
                self.Tabla_Datos.setItem(tablerow, 12, QtWidgets.QTableWidgetItem(str(i[13])))
                self.Tabla_Datos.setItem(tablerow, 13, QtWidgets.QTableWidgetItem(str(i[14])))
                self.Tabla_Datos.setItem(tablerow, 14, QtWidgets.QTableWidgetItem(str(i[15])))
                self.Tabla_Datos.setItem(tablerow, 15, QtWidgets.QTableWidgetItem(str(i[16])))
                self.Tabla_Datos.setItem(tablerow, 16, QtWidgets.QTableWidgetItem(str(i[17])))
                self.Tabla_Datos.setItem(tablerow, 17, QtWidgets.QTableWidgetItem(str(i[18])))
                tablerow +=1

        varb = self.edt_matricula.text()
        for row in range(self.Tabla_Datos.rowCount()):
            for col in range(self.Tabla_Datos.columnCount()):
                if varb == self.Tabla_Datos.item(row,col).text():
                    self.edt_nombre.setText(self.Tabla_Datos.item(row,1).text())
                    self.edt_apppat.setText(self.Tabla_Datos.item(row,2).text())
                    self.edt_appmat.setText(self.Tabla_Datos.item(row,3).text())
                    self.edt_domicilio.setText(self.Tabla_Datos.item(row,4).text())
                    self.cbx_ciudad.setCurrentText(self.Tabla_Datos.item(row,5).text())
                    self.cbx_estado.setCurrentText(self.Tabla_Datos.item(row,6).text())
                    self.cbx_carrera.setCurrentText(self.Tabla_Datos.item(row,7).text())
                    #self.spinEdad.setText(self.Tabla_Datos.item(row,8).text())

                    # Sexo
                    if self.Tabla_Datos.item(row,8).text() == "M":
                        self.radio_hombre.setChecked(True)
                    else:
                        self.radio_mujer.setChecked(True)

                    # Edad
                    if self.Tabla_Datos.item(row,9).text():
                        eda = self.Tabla_Datos.item(row,9).text()
                        self.spinEdad.setValue(int(eda))

                    # Beca
                    if self.Tabla_Datos.item(row,10).text() == "0":
                        self.radio_cero.setChecked(True)
                    elif self.Tabla_Datos.item(row,10).text() == "50":
                        self.radio_50.setChecked(True)
                    elif self.Tabla_Datos.item(row,10).text() == "80":
                        self.radio_80.setChecked(True)
                    elif self.Tabla_Datos.item(row,10).text() == "100":
                        self.radio_100.setChecked(True)
                        self.Tabla_Datos.selectRow(row)
                    else:
                        self.radio_cero.setChecked(True)
                        break

                    # Foraneo
                    if self.Tabla_Datos.item(row,11).text() == "1":
                        self.chk_foraneo.setChecked(True)
                    else:
                        self.chk_foraneo.setChecked(False)

                    # Ingles
                    if self.Tabla_Datos.item(row,12).text() == "1":
                        self.chk_ingles.setChecked(True)
                    else:
                        self.chk_ingles.setChecked(False)


                    if self.Tabla_Datos.item(row,13).text() == "1":
                        self.chk_prog.setChecked(True)
                    else:
                        self.chk_prog.setChecked(False)

                    if self.Tabla_Datos.item(row,14).text() == "1":
                        self.chk_bd.setChecked(True)
                    else:
                        self.chk_bd.setChecked(False)

                    if self.Tabla_Datos.item(row,15).text() == "1":
                        self.chk_contab.setChecked(True)
                    else:
                        self.chk_contab.setChecked(False)

                    if self.Tabla_Datos.item(row,16).text() == "1":
                        self.chk_estadistica.setChecked(True)
                    else:
                        self.chk_estadistica.setChecked(False)

                    if self.Tabla_Datos.item(row,17).text() == "1":
                        self.chk_inv_op.setChecked(True)
                    else:
                        self.chk_inv_op.setChecked(False)


    def fn_actualizar(self):
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="bd_alumnos"
        )
        mat = self.edt_matricula.text()
        nom = self.edt_nombre.text()
        appat = self.edt_apppat.text()
        apmat = self.edt_appmat.text()
        dom = self.edt_domicilio.text()
        ciud = self.cbx_ciudad.currentText()
        est = self.cbx_estado.currentText()
        carr = self.cbx_carrera.currentText()
        if self.radio_hombre.isChecked():
            sex = "M"
        else:
            sex = "F"
        eda = self.spinEdad.text()
        if self.radio_cero.isChecked():
            bec = "0"
        elif self.radio_50.isChecked():
            bec = "50"
        elif self.radio_80.isChecked():
            bec = "80"
        elif self.radio_100.isChecked():
            bec = "100"

        # Foraneo
        if self.chk_foraneo.isChecked():
            foran = 1
        else:
            foran = 0

        # Ingles
        if self.chk_ingles.isChecked():
            ingl = 1
        else:
            ingl = 0

        if self.chk_prog.isChecked():
            pro = "1"
        else:
            pro = "0"

        if self.chk_bd.isChecked():
            bad = "1"
        else:
            bad = "0"

        if self.chk_contab.isChecked():
            contab = "1"
        else:
            contab = "0"

        if self.chk_estadistica.isChecked():
            esta = "1"
        else:
            esta = "0"

        if self.chk_inv_op.isChecked():
            inv = "1"
        else:
            inv = "0"
        mycursor = mydb.cursor()
        mycursor.execute("""UPDATE alumnos SET nombres = %s, a_paterno = %s, a_materno = %s, domicilio = %s, ciudad = %s, estado = %s, \
            carrera = %s,  sexo = %s, edad = %s, beca = %s, foraneo = %s,  ingles = %s, prog = %s, bd = %s, contab = %s, \
            estadistica = %s, inv_op = %s WHERE Matricula = %s""", (nom, appat, apmat, dom, ciud, est, carr, sex, eda, bec, foran, ingl, pro, bad, contab, esta, inv, mat))
        mydb.commit()
        self.edt_matricula.clear()
        self.edt_nombre.clear()
        self.edt_apppat.clear()
        self.edt_appmat.clear()
        self.edt_domicilio.clear()
        self.spinEdad.clear()
        self.chk_prog.setChecked(False)
        self.chk_bd.setChecked(False)
        self.chk_contab.setChecked(False)
        self.chk_estadistica.setChecked(False)
        self.chk_inv_op.setChecked(False)
        if self.radio_50.isChecked():
            self.radio_cero.setChecked(True)
        if self.radio_80.isChecked():
            self.radio_cero.setChecked(True)
        if self.radio_100.isChecked():
            self.radio_cero.setChecked(True)
        self.edt_matricula.setFocus()


    def f_convpdf(self):
        print("Generacion PDF")
        class PDF(FPDF):
            def header(self):
                self.set_font('Arial', 'B', 15)
                self.cell(10, 10, 'Alumnos')
                self.ln(20)
        pdf = PDF()
        pdf.alias_nb_pages()
        pdf.add_page()
        pdf.set_font('Arial', '', 10)
        for row in range(self.Tabla_Datos.rowCount()):
            pdf.multi_cell(0, 10, "Matricula: "+str(self.Tabla_Datos.item(row,0).text())+" | "+"Nombre: "+str(self.Tabla_Datos.item(row,1).text())+" | "+"Apellido P: "+str(self.Tabla_Datos.item(row,2).text())+" | "+"Apellido M: "+str(self.Tabla_Datos.item(row,3).text())+" | "+"Domicilio: "+str(self.Tabla_Datos.item(row,4).text())+" | "+"Ciudad: "+str(self.Tabla_Datos.item(row,5).text())+" | "+"Estado: "+str(self.Tabla_Datos.item(row,6).text())+" | "+"Carrera: "+str(self.Tabla_Datos.item(row,7).text())+" | "+"Sexo: "+str(self.Tabla_Datos.item(row,8).text())+" | "+"Edad: "+str(self.Tabla_Datos.item(row,9).text())+" | "+"Beca: "+str(self.Tabla_Datos.item(row,10).text())+" | "+"BD: "+str(self.Tabla_Datos.item(row,11).text())+" | "+"Contab: "+str(self.Tabla_Datos.item(row,12).text())+" | "+"Estadis: "+str(self.Tabla_Datos.item(row,13).text())+" | "+"Inv. Ope: "+str(self.Tabla_Datos.item(row,14).text())+" |                                                                                                                                        ", 0, 1)
        pdf.output('alumnos.pdf', 'F')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    GUI = alumnos_DB()
    GUI.show()
    sys.exit(app.exec_())