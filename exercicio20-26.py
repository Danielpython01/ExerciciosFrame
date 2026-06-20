import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLCDNumber, QVBoxLayout
from PyQt6.QtCore import QTimer, QTime

def mostrar_hora():
    hora_atual = QTime.currentTime()
    texto_hora = hora_atual.toString('hh:mm:ss')
    lcd.display(texto_hora)

app = QApplication(sys.argv)
janela = QWidget()
janela.setWindowTitle("Relógio Digital")
layout = QVBoxLayout()

lcd = QLCDNumber()
lcd.setSegmentStyle(QLCDNumber.SegmentStyle.Flat)
lcd.setDigitCount(8)

timer = QTimer(janela)
timer.timeout.connect(mostrar_hora)
timer.start(1000)

layout.addWidget(lcd)
janela.setLayout(layout)
mostrar_hora()
janela.show()
sys.exit(app.exec())