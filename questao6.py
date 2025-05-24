#FELIPE RODRIGUES DE SOUSA - 202504000
#QUESTÃO 6

import tkinter as tk # Importa a biblioteca Tkinter para interface gráfica.
import requests # Importa requests para fazer requisições HTTP.
import time # Importa time para funções relacionadas a tempo (não usado diretamente no loop, mas útil).
from datetime import datetime # Importa datetime para trabalhar com datas e horas.

def obter_cotacao(base_currency="USD", target_currency="BRL"): # Função para buscar a cotação.
    url = f"https://api.exchangerate-api.com/v4/latest/{base_currency}" # URL da API de cotação.
    try:
        response = requests.get(url) # Faz a requisição à API.
        response.raise_for_status() # Verifica por erros na requisição HTTP.
        data = response.json() # Converte a resposta JSON.
        if 'rates' in data and target_currency in data['rates']: # Verifica se a cotação desejada existe.
            return data['rates'][target_currency], datetime.now().strftime("%Y-%m-%d %H:%M:%S") # Retorna a cotação e a hora atual.
        else:
            return None, None # Retorna nulo se a cotação não for encontrada.
    except requests.exceptions.RequestException as e: # Captura erros de requisição.
        print(f"Erro ao obter cotação: {e}")
        return None, None
    except ValueError: # Captura erros ao decodificar JSON.
        print("Erro ao decodificar JSON.")
        return None, None

historico_cotacoes = [] # Lista para armazenar o histórico de cotações.

def atualizar_cotacao(): # Função para atualizar a interface com a cotação.
    cotacao, hora_atualizacao = obter_cotacao() # Obtém a cotação e a hora.
    if cotacao is not None: # Se a cotação for válida.
        label_cotacao.config(text=f"USD para BRL: {cotacao:.4f}", fg="white") # Atualiza o texto da cotação.
        label_atualizacao.config(text=f"Última atualização: {hora_atualizacao}", fg="lightgray") # Atualiza a hora da atualização.

        historico_cotacoes.append(f"{hora_atualizacao}: {cotacao:.4f}") # Adiciona a cotação ao histórico.
        if len(historico_cotacoes) > 5: # Limita o histórico às 5 últimas.
            historico_cotacoes.pop(0) # Remove o item mais antigo.

        texto_historico.set("\n".join(historico_cotacoes)) # Atualiza o texto do histórico.
    else: # Se houver erro na cotação.
        label_cotacao.config(text="Erro ao obter cotação.", fg="red") # Exibe mensagem de erro na cotação.
        label_atualizacao.config(text="", fg="red")
        texto_historico.set("Erro ao obter dados.") # Exibe erro no histórico.

    janela.after(5000, atualizar_cotacao) # Agenda a próxima atualização em 5 segundos.

# Cria a janela principal do Tkinter.
janela = tk.Tk()
janela.title("Dashboard de Cotação") # Define o título da janela.
janela.config(bg="medium purple") # Define a cor de fundo da janela.

# Título principal do dashboard.
label_titulo = tk.Label(janela, text="Cotação em Tempo Real", font=("Arial", 20, "bold"), bg="medium purple", fg="white")
label_titulo.pack(pady=(10, 5)) # Adiciona o título à janela.

# Rótulo para exibir a cotação atual.
label_cotacao = tk.Label(janela, text="Aguardando cotação...", font=("Arial", 16), bg="medium purple", fg="white")
label_cotacao.pack(padx=20, pady=10) # Adiciona o rótulo da cotação.

# Rótulo para exibir a hora da última atualização.
label_atualizacao = tk.Label(janela, text="", font=("Arial", 10), bg="medium purple", fg="lightgray")
label_atualizacao.pack() # Adiciona o rótulo da atualização.

# Título do histórico de cotações.
label_historico_titulo = tk.Label(janela, text="Histórico de Cotações:", font=("Arial", 12, "bold"), bg="medium purple", fg="white")
label_historico_titulo.pack(pady=(10, 5)) # Adiciona o título do histórico.

# Variável de controle para o texto do histórico.
texto_historico = tk.StringVar()
# Rótulo para exibir o histórico de cotações.
label_historico = tk.Label(janela, textvariable=texto_historico, font=("Arial", 10), bg="medium purple", fg="white", justify='left')
label_historico.pack(padx=20) # Adiciona o rótulo do histórico.

atualizar_cotacao() # Inicia a primeira atualização da cotação.

janela.mainloop() # Inicia o loop principal da interface gráfica.