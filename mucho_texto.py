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
                        "Lorem ipsum dolor sit amet consectetur adipiscing elit nostra, blandit lobortis tincidunt sapien netus " \
                        "interdum cum, luctus quis accumsan mollis varius eu natoque. Tellus vivamus augue duis litora inceptos " \
                        "euismod mauris rhoncus, ultrices at habitasse facilisis et praesent. Primis risus vel arcu facilisi a vitae, " \
                        "himenaeos conubia libero penatibus porta."
                        ))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Experiment"))
        
        self.label_1.setFont(font)
        self.label_1.setWordWrap(True)
        self.label_1.setAlignment(QtCore.Qt.AlignJustify)
        self.label_1.setText(
                _translate("MainWindow", 
                        "Lorem ipsum dolor sit amet consectetur adipiscing elit nostra, blandit lobortis tincidunt sapien netus " \
                        "interdum cum, luctus quis accumsan mollis varius eu natoque. Tellus vivamus augue duis litora inceptos " \
                        "euismod mauris rhoncus, ultrices at habitasse facilisis et praesent. Primis risus vel arcu facilisi a vitae, " \
                        "himenaeos conubia libero penatibus porta."
                        ))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab1), _translate("MainWindow", "Wavelength"))

        self.label_2.setFont(font)
        self.label_2.setWordWrap(True)
        self.label_2.setAlignment(QtCore.Qt.AlignJustify)
        self.label_2.setText(
                _translate("MainWindow", 
                        "Lorem ipsum dolor sit amet consectetur adipiscing elit nostra, blandit lobortis tincidunt sapien netus " \
                        "interdum cum, luctus quis accumsan mollis varius eu natoque. Tellus vivamus augue duis litora inceptos " \
                        "euismod mauris rhoncus, ultrices at habitasse facilisis et praesent. Primis risus vel arcu facilisi a vitae, " \
                        "himenaeos conubia libero penatibus porta."
                        ))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab2), _translate("MainWindow", "Screen distance"))

        self.label_3.setFont(font)
        self.label_3.setWordWrap(True)
        self.label_3.setAlignment(QtCore.Qt.AlignJustify)
        self.label_3.setText(
                _translate("MainWindow", 
                        "Lorem ipsum dolor sit amet consectetur adipiscing elit nostra, blandit lobortis tincidunt sapien netus " \
                        "interdum cum, luctus quis accumsan mollis varius eu natoque. Tellus vivamus augue duis litora inceptos " \
                        "euismod mauris rhoncus, ultrices at habitasse facilisis et praesent. Primis risus vel arcu facilisi a vitae, " \
                        "himenaeos conubia libero penatibus porta."
                        ))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab3), _translate("MainWindow", "Slit separation"))

        self.label_4.setFont(font)
        self.label_4.setWordWrap(True)
        self.label_4.setAlignment(QtCore.Qt.AlignJustify)
        self.label_4.setText(
                _translate("MainWindow", 
                        "Lorem ipsum dolor sit amet consectetur adipiscing elit nostra, blandit lobortis tincidunt sapien netus " \
                        "interdum cum, luctus quis accumsan mollis varius eu natoque. Tellus vivamus augue duis litora inceptos " \
                        "euismod mauris rhoncus, ultrices at habitasse facilisis et praesent. Primis risus vel arcu facilisi a vitae, " \
                        "himenaeos conubia libero penatibus porta."
                        ))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab5), _translate("MainWindow", "Slit width"))