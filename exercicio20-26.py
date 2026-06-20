import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QLCDNumber,
    QVBoxLayout, QLabel
)
from PyQt6.QtCore import QTimer, QTime, QDate, Qt


class RelogioDigital(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Relógio Digital")
        self.setFixedSize(500, 220)

        # Estilo da janela
        self.setStyleSheet("""
            QWidget {
                background-color: #121212;
            }

            QLabel {
                color: white;
                font-size: 18px;
                font-family: Arial;
            }

            QLCDNumber {
                background-color: #1E1E1E;
                color: #00FF88;
                border: 3px solid #00FF88;
                border-radius: 20px;
                padding: 15px;
            }
        """)

        layout = QVBoxLayout()
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(15)

        self.lcd = QLCDNumber()
        self.lcd.setDigitCount(8)
        self.lcd.setSegmentStyle(QLCDNumber.SegmentStyle.Flat)

        self.data_label = QLabel()
        self.data_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        layout.addWidget(self.lcd)
        layout.addWidget(self.data_label)

        self.setLayout(layout)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.atualizar)
        self.timer.start(1000)

        self.atualizar()

    def atualizar(self):
        hora = QTime.currentTime().toString("hh:mm:ss")
        data = QDate.currentDate().toString("dd/MM/yyyy")

        self.lcd.display(hora)
        self.data_label.setText(data)


app = QApplication(sys.argv)

janela = RelogioDigital()
janela.show()

sys.exit(app.exec())