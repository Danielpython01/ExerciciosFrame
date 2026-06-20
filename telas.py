import tkinter as tk

def calcular_imc():
    try:
        peso = float(entry_peso.get())
        altura = float(entry_altura.get())
        imc = peso / (altura ** 2)
        
        if imc < 18.5:
            classificacao = "Abaixo do peso"
        elif 18.5 <= imc < 25:
            classificacao = "Peso normal"
        elif 25 <= imc < 30:
            classificacao = "Sobrepeso"
        else:
            classificacao = "Obesidade"
            
        label_resultado.config(text=f"Seu IMC é {imc:.2f}\nClassificação: {classificacao}")
    except ValueError:
        label_resultado.config(text="Por favor, digite valores numéricos válidos.")

# --- Configuração da Janela ---
janela = tk.Tk()
janela.title("Calculadora de IMC")
janela.geometry("300x200")

# --- Widgets ---
tk.Label(janela, text="Peso (kg):").grid(row=0, column=0, padx=10, pady=5)
entry_peso = tk.Entry(janela)
entry_peso.grid(row=0, column=1, padx=10, pady=5)

tk.Label(janela, text="Altura (m):").grid(row=1, column=0, padx=10, pady=5)
entry_altura = tk.Entry(janela)
entry_altura.grid(row=1, column=1, padx=10, pady=5)

botao_calcular = tk.Button(janela, text="Calcular", command=calcular_imc)
botao_calcular.grid(row=2, column=0, columnspan=2, pady=10)

label_resultado = tk.Label(janela, text="", font=("Arial", 10, "bold"))
label_resultado.grid(row=3, column=0, columnspan=2, pady=5)

# --- Inicia a Janela ---
janela.mainloop()

