import sys
import requests
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QComboBox, QPushButton, QGridLayout

# --- Funções (Slots) ---
def buscar_taxas():
    try:
        url = "https://open.er-api.com/v6/latest/USD"
        resposta = requests.get(url)
        if resposta.status_code == 200:
            return resposta.json().get('rates', {})
        return {}
    except requests.exceptions.RequestException:
        return {}

def converter():
    if not taxas: return
    try:
        valor = float(campo_valor.text())
        moeda_de = combo_de.currentText()
        moeda_para = combo_para.currentText()
        valor_em_usd = valor / taxas[moeda_de]
        valor_final = valor_em_usd * taxas[moeda_para]
        label_resultado.setText(f"{valor:.2f} {moeda_de} = {valor_final:.2f} {moeda_para}")
    except (ValueError, KeyError):
        label_resultado.setText("Erro: Valor ou moeda inválida.")

# --- Interface ---
app = QApplication(sys.argv)
janela = QWidget()
janela.setWindowTitle("Conversor de Moedas")
layout = QGridLayout()

# Carrega os dados da API
taxas = buscar_taxas()

# Widgets
campo_valor = QLineEdit("100")
combo_de = QComboBox()
combo_para = QComboBox()
botao_converter = QPushButton("Converter")
label_resultado = QLabel("Resultado:")

if taxas:
    moedas = sorted(taxas.keys())
    combo_de.addItems(moedas)
    combo_para.addItems(moedas)
    combo_de.setCurrentText("USD")
    combo_para.setCurrentText("BRL")
else:
    label_resultado.setText("Erro ao carregar taxas.")

# Conecta o botão à função de conversão
botao_converter.clicked.connect(converter)

# Adiciona widgets ao layout
layout.addWidget(QLabel("Valor:"), 0, 0)
layout.addWidget(campo_valor, 0, 1)
layout.addWidget(QLabel("De:"), 1, 0)
layout.addWidget(combo_de, 1, 1)
layout.addWidget(QLabel("Para:"), 2, 0)
layout.addWidget(combo_para, 2, 1)
layout.addWidget(botao_converter, 3, 0, 1, 2)
layout.addWidget(label_resultado, 4, 0, 1, 2)

janela.setLayout(layout)
janela.show()
sys.exit(app.exec())