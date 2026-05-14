from PyQt5 import QtCore, QtGui

def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Interference Simulator"))

        self.slider_label_1.setText(_translate("MainWindow", "Wavelength (λ)"))
        self.slider_label_2.setText(_translate("MainWindow", "Screen distance (D)"))
        self.slider_label_3.setText(_translate("MainWindow", "Slit separation (b)"))
        self.slider_label_4.setText(_translate("MainWindow", "Slit width (a)"))    

        self.slider_value_1.setText(_translate("MainWindow", "520 nm"))
        self.slider_value_2.setText(_translate("MainWindow", "200 cm"))
        self.slider_value_3.setText(_translate("MainWindow", "20 μm"))
        self.slider_value_4.setText(_translate("MainWindow", "2 μm"))

        # Configurar la fuente
        font = QtGui.QFont()
        font.setPointSize(15)

        #self.title.setText(_translate("MainWindow", "# **INTERFERENCE SIMULATOR**"))
        self.label_0.setFont(font)
        self.label_0.setWordWrap(True)  # Permitir salto de línea
        self.label_0.setAlignment(QtCore.Qt.AlignJustify)  # Justificar texto
        self.label_0.setText(
                _translate("MainWindow", 
                        "Un làser que incideix sobre una superfície amb dues escletxes, en aquestes la llum es difracta, fent que les " \
                        "parets de l'escletxa es comportin com fronts d'ona. Aleshores la llum viatja fins a la pantalla, on es veu " \
                        "el patró."
                        ))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Experiment"))
        
        self.label_1.setFont(font)
        self.label_1.setWordWrap(True)
        self.label_1.setAlignment(QtCore.Qt.AlignJustify)
        self.label_1.setText(
                _translate("MainWindow", 
                        "En modificar la longitud d’ona, la distància a la qual es produeixen les franges augmenta de forma " \
                        "proporcional. La causa és que les distàncies a les quals es produeixen les franges són on la diferència de " \
                        "camí òptic coincideix amb múltiples enters de lambda. " \
                        "\n\nPer tant, com major fem lambda més augmenta les distàncies on es produeix la interferència constructiva. "
                        ))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab1), _translate("MainWindow", "Longitud d'ona"))

        self.label_2.setFont(font)
        self.label_2.setWordWrap(True)
        self.label_2.setAlignment(QtCore.Qt.AlignJustify)
        self.label_2.setText(
                _translate("MainWindow", 
                        "En modificar la distància a la pantalla observem que la distància relativa entre els màxims no varia. No " \
                        "obstant això, com l’angle on es propaga la llum és constant, la grandària aparent de la imatge augmenta en " \
                        "allunyar-se. " \
                        "\n\nCom que la pantalla que simulem té grandària fixa, sembla que la distància entre els màxims augmenta. "
                        ))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab2), _translate("MainWindow", "Distància a la pantalla"))

        self.label_3.setFont(font)
        self.label_3.setWordWrap(True)
        self.label_3.setAlignment(QtCore.Qt.AlignJustify)
        self.label_3.setText(
                _translate("MainWindow", 
                        "Quan augmenta la distància entre les reixetes, hi ha més combinacions de camins que compleixen la condició de " \
                        "màxim, és a dir, que la diferència de camí òptic sigui un múltiple enter de lambda. "
                        ))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab3), _translate("MainWindow", "Separació de les reixetes"))

        self.label_4.setFont(font)
        self.label_4.setWordWrap(True)
        self.label_4.setAlignment(QtCore.Qt.AlignJustify)
        self.label_4.setText(
                _translate("MainWindow", 
                        "En augmentar l’amplada de la reixeta, hi ha més punts que actuen com a fonts secundàries d’ones esfèriques i " \
                        "el patró resultant presenta menys difracció. " \
                        "\n\nEn el límit en què fem l’amplada molt gran, tenim infinits fronts d’ones esfèriques que tenen un " \
                        "comportament equivalent al d’una ona plana (principi de Huygens). "
                        ))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab5), _translate("MainWindow", "Amplada de les reixetes"))