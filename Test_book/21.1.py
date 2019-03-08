from PyQt5 import QtWidgets
import sys

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Заголовок окна")
window.resize(800, 200)
window.show()
sys.exit(app.exec_())

