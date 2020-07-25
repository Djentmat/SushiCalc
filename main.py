from PyQt5 import QtWidgets
from window import Ui_MainWindow
import sys


class MainWin(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWin, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.let_rice_val.setText("800")
        self.ui.let_rice_per_sushi.setText("160")

        self.show_msg = QtWidgets.QMessageBox()
        self.ui.pbn_calc.clicked.connect(self.calc_sushi_vals)
        self.ui.pbn_reset.clicked.connect(self.reset_vals)

    def calc_sushi_vals(self):

        res = self.check_input(self.ui.let_rice_val.text())

        if res == -1:
            return
        res = self.check_input(self.ui.let_rice_per_sushi.text())

        if res == -1:
            return
        rice = float(self.ui.let_rice_val.text())
        rice_per_sushi = float(self.ui.let_rice_per_sushi.text())

        acid_calc = str(round(rice * 11 / 100))
        shugar_calc = str(round(rice * 9 / 100))
        salt_calc = str(round(rice * 1 / 100))
        water_calc = str(round(rice * 111 / 100))

        total_sushi_calc = str(round((rice + int(water_calc)) /
                                     rice_per_sushi))
        self.ui.let_acid_val.setText(acid_calc)
        self.ui.let_shugar_val.setText(shugar_calc)
        self.ui.let_salt_val.setText(salt_calc)
        self.ui.let_water_val.setText(water_calc)
        self.ui.let_total_sushu_cnt.setText(total_sushi_calc)

    def check_input(self, string):
        ciphers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        if len(string) == 0:
            self.show_msg.critical(None, "Ошибка ввода",
                                   "Пустое поле ввода")
            return -1
        for i, char in enumerate(string):
            if char not in ciphers:
                self.show_msg.critical(None, "Ошибка ввода",
                                       "В поле ввода находится не число!")
                return -1

    def reset_vals(self):
        self.ui.let_rice_val.setText("800")
        self.ui.let_rice_per_sushi.setText("160")
        self.ui.let_salt_val.clear()
        self.ui.let_shugar_val.clear()
        self.ui.let_water_val.clear()
        self.ui.let_acid_val.clear()
        self.ui.let_total_sushu_cnt.clear()


app = QtWidgets.QApplication([])
application = MainWin()
application.show()
app.setStyle('Fusion')
sys.exit(app.exec())
