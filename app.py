import streamlit as st
import matplotlib.pyplot as plt

# Função principal do app
def main():
    st.title('R&A Initiatives Dashboard')

    # Entrada para as categorias (permitindo ao usuário editar as categorias)
    categories = st.text_area('Categorias (separadas por vírgula):', 
                              "CAR's, PIP’s, JDSN, Battery, Warranty\nCancelation, Gap, Accomplished, Goal 2024\n\n(Gap + Accomplished)")
    categories = [cat.strip() for cat in categories.split(',')]

    # Entrada para os valores (permitindo ao usuário editar os valores)
    values = st.text_input('Valores (separados por vírgula):', 
                           '0, 44379, 482000, 0, 47000, 749476, 0, 1322855')
    values = [int(v.strip()) for v in values.split(',')]

    # Entrada para o fator de conversão
    conversion_factor = st.number_input('Fator de conversão ($/tr):', value=15565)

    # Entrada para os limites do eixo Y à esquerda
    y1_min = st.number_input('Limite mínimo do eixo Y esquerdo:', value=0)
    y1_max = st.number_input('Limite máximo do eixo Y esquerdo:', value=1600000)

    # Entrada para os limites do eixo Y à direita
    y2_min = st.number_input('Limite mínimo do eixo Y direito:', value=-30)
    y2_max = st.number_input('Limite máximo do eixo Y direito:', value=100)

    # Calcular o valor "Realized"
    realized_value = sum([values[1], values[2], values[4]])  # Valores 44379, 482000, 47000
    values[6] = realized_value

    # Ajustar os valores convertidos
    converted_values = [v / conversion_factor if v else 0 for v in values]

    # Plotando o gráfico
    fig, ax1 = plt.subplots(figsize=(10, 6))

    # Gráfico de barras para os dados originais
    bars = ax1.bar(categories, values, color=['#1a591e', '#1a591e', '#1a591e', '#1a591e', '#1a591e', '#ffde00', '#71a36a', '#6a5b38'])

    # Labels para os valores das barras
    for bar in bars:
        yval = bar.get_height()
        if yval > 0:
            ax1.text(bar.get_x() + bar.get_width() / 2, yval + 10000, f'${yval:,}', ha='center', va='bottom')

    # Definindo os rótulos dos eixos e título
    ax1.set_ylabel('Values in Millions $')
    ax1.set_ylim(y1_min, y1_max)
    ax1.set_title('R&A Initiatives')

    # Criar um eixo secundário para valores em $/tr
    ax2 = ax1.twinx()
    ax2.plot(categories, converted_values, color='#585858', marker='s', linestyle='', label='$/tr')
    ax2.set_ylim(y2_min, y2_max)
    ax2.set_ylabel('Values in $/tr', color='#585858')

    # Alterar a cor dos valores do eixo Y secundário para cinza
    ax2.tick_params(axis='y', colors='#585858')

    # Exibir o gráfico no Streamlit
    st.pyplot(fig)

# Rodar o aplicativo
if __name__ == '__main__':
    main()