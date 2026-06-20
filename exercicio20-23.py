import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel,
    QLineEdit, QPushButton, QVBoxLayout
)
from PyQt6.QtCore import Qt


class Conversor(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Conversor de Metros para KM")
        self.setFixedSize(400, 250)

        self.setStyleSheet("""
            QWidget {
                background-color: #f5f7fa;
            }

            QLabel {
                color: #2c3e50;
                font-size: 15px;
            }

            QLineEdit {
                background-color: white;
                border: 1px solid #d6dce5;
                border-radius: 8px;
                padding: 10px;
                font-size: 15px;
                color: #2c3e50;
            }

            QLineEdit:focus {
                border: 2px solid #4a90e2;
            }

            QPushButton {
                background-color: #4a90e2;
                color: white;
                border: none;
                border-radius: 8px;
                padding: 12px;
                font-size: 15px;
                font-weight: bold;
            }

            QPushButton:hover {
                background-color: #357abd;
            }

            QPushButton:pressed {
                background-color: #2d66a3;
            }

            #resultado {
                background-color: white;
                border: 1px solid #d6dce5;
                border-radius: 8px;
                padding: 12px;
                font-size: 16px;
                font-weight: bold;
            }
        """)

        layout = QVBoxLayout()
        layout.setSpacing(15)
        layout.setContentsMargins(25, 25, 25, 25)

        titulo = QLabel("Digite o valor em metros:")
        titulo.setAlignment(Qt.AlignmentFlag.AlignLeft)

        self.campo_metros = QLineEdit()
        self.campo_metros.setPlaceholderText("Ex.: 1500")

        self.botao = QPushButton("Converter")
        self.botao.clicked.connect(self.converter)

        self.label_resultado = QLabel("Resultado aparecerá aqui")
        self.label_resultado.setObjectName("resultado")
        self.label_resultado.setAlignment(Qt.AlignmentFlag.AlignCenter)

        layout.addWidget(titulo)
        layout.addWidget(self.campo_metros)
        layout.addWidget(self.botao)
        layout.addWidget(self.label_resultado)

        self.setLayout(layout)

    def converter(self):
        try:
            metros = float(self.campo_metros.text())
            km = metros / 1000
            self.label_resultado.setText(f"{metros:.2f} m = {km:.3f} km")
        except ValueError:
            self.label_resultado.setText("Digite um número válido.")


app = QApplication(sys.argv)

janela = Conversor()
janela.show()

sys.exit(app.exec())