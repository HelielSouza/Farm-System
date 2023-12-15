import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from matplotlib.animation import FuncAnimation
import numpy as np

# Inicializar os dados
dias = np.arange(1, 11)
valores = np.random.randint(100, 2000, 10)

# Criar um DataFrame Seaborn
data = {'Dias': dias, 'Valores': valores}

# Definir cores personalizadas para as colunas
cores = sns.color_palette("viridis", len(dias))

# Criar o gráfico com os dados e as cores
fig, ax = plt.subplots(figsize=(10, 6))
barplot = sns.barplot(x='Dias', y='Valores', data=data, palette=cores, ax=ax)

plt.xlabel('Dia')
plt.ylabel('Valores')
plt.title('Graus Dias')

# Inicializar anotações
anotacoes = []

# Configurar barra de rolagem horizontal
axcolor = 'lightgoldenrodyellow'
ax_slider = plt.axes([0.2, 0.02, 0.65, 0.03], facecolor=axcolor)
slider = Slider(ax_slider, 'Dias Visíveis', 1, len(data['Dias']), valinit=len(data['Dias']))

def update(val):
    dias_visiveis = int(slider.val)
    ax.set_xlim(max(0, dias_visiveis - len(data['Dias'])), dias_visiveis)
    ax.figure.canvas.draw_idle()

slider.on_changed(update)

# Função para adicionar um novo valor
def add_new_values(frame):
    # Carregar um novo valor (substitua isso pelo código real para carregar seus dados)
    novo_dia = data['Dias'][-1] + 1
    novo_valor = np.random.randint(100, 2000)

    # Adicionar novo dia e valor aos dados existentes
    data['Dias'] = np.append(data['Dias'], novo_dia)
    data['Valores'] = np.append(data['Valores'], novo_valor)

    # Atualizar os dados no gráfico
    barplot = sns.barplot(x='Dias', y='Valores', data=data, palette=cores, ax=ax)

    # Limpar anotações antigas
    for text in ax.texts:
        text.set_visible(False)

    # Adicionar anotações para todos os valores
    for dia, valor in zip(data['Dias'], data['Valores']):
        anotacao = ax.text(dia - 1, valor, f'{valor:.0f}',
                           ha='center', va='bottom', fontsize=9, color='black')
        anotacoes.append(anotacao)

    # Atualizar a posição da barra de rolagem
    slider.set_val(len(data['Dias']))

# Configurar animação
ani = FuncAnimation(fig, add_new_values, frames=np.arange(1, 100), interval=1000)

# Exibir o gráfico
plt.show()
