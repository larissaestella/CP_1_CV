import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import norm, poisson, binom, expon

# Configuração da página
st.set_page_config(
    page_title="Análise de Dados", 
    page_icon="📊",
    layout="wide")
st.title("📊 Análise de Risco de Crédito")

# 1. Apresentação dos dados e tipos de variáveis
st.header("1. Apresentação dos Dados e Tipos de Variáveis")
st.write("""
        O conjunto de dados analisado refere-se a clientes de uma instituição financeira,
    contendo informações pessoais, financeiras e comportamentais, como idade, 
    salário anual, limite de crédito e histórico de transações. O objetivo é 
    analisar o risco de inadimplência (variável default), e entender o perfil 
    dos clientes para subsidiar estratégias de crédito.
    """)

# Dataset
url = 'https://raw.githubusercontent.com/andre-marcos-perez/ebac-course-utils/develop/dataset/credito.csv'
df = pd.read_csv(url)

# Exibição amostra dos dados

df['limite_credito'] = df['limite_credito'].apply(lambda x: float(str(x).replace('.', '').replace(',', '.')))
df['valor_transacoes_12m'] = df['valor_transacoes_12m'].apply(lambda x: float(str(x).replace('.', '').replace(',', '.')))
st.subheader("Amostra dos Dados")
st.dataframe(df.head(300))

# ------------------------------------------------------------
# Conversão das colunas numéricas

colunas_numericas = [
    'idade', 'dependentes', 'salario_anual', 'meses_de_relacionamento',
    'qtd_produtos', 'iteracoes_12m', 'meses_inativo_12m',
    'limite_credito', 'valor_transacoes_12m', 'qtd_transacoes_12m'
]

for coluna in colunas_numericas:
    df[coluna] = pd.to_numeric(df[coluna], errors='coerce')

    
# ------------------------------------------------------------

# Tipos de variáveis
st.subheader("Tipos das Variáveis")
tipos = pd.DataFrame(df.dtypes, columns=["Tipo de Dado"])
st.write(tipos)

# Perguntas principais
st.subheader("Principais Perguntas para Análise")
st.markdown("""
- Qual é o perfil dos clientes inadimplentes?
- Existe relação entre o limite de crédito e a inadimplência?
- Qual é o comportamento de transações dos clientes (volume e valor)?
- Como o tempo de relacionamento influencia a inadimplência?
""")

st.markdown("---")

# 2. Análise Estatística Descritiva
st.header("2. Análise Estatística Descritiva")

st.subheader("Medidas Centrais")

# Seleção de colunas numéricas
num_cols = df.select_dtypes(include=['int64', 'float64']).columns

# Tabela resumo
desc = df[num_cols].describe().T
desc['moda'] = df[num_cols].mode().iloc[0]
st.dataframe(desc[['mean', '50%', 'std', 'min', 'max', 'moda']].rename(columns={'50%': 'mediana'}))

# # Distribuição dos dados
# st.subheader("Distribuição dos Dados (Histogramas)")
# for col in num_cols:
#     fig, ax = plt.subplots()
#     sns.histplot(df[col], kde=True, ax=ax)
#     st.pyplot(fig)

# Correlação
st.subheader("Correlação entre Variáveis")
# corr = df[num_cols].corr()
# fig, ax = plt.subplots(figsize=(10, 8))
# sns.heatmap(corr, annot=True, cmap='coolwarm', ax=ax)
# st.pyplot(fig)

df['meses_de_relacionamento'] = pd.to_numeric(df['meses_de_relacionamento'], errors='coerce')
df['limite_credito'] = pd.to_numeric(df['limite_credito'], errors='coerce')
df['valor_transacoes_12m'] = pd.to_numeric(df['valor_transacoes_12m'], errors='coerce')
df['qtd_transacoes_12m'] = pd.to_numeric(df['qtd_transacoes_12m'], errors='coerce')

# Remover linhas com valores ausentes nas variáveis selecionadas
df = df.dropna(subset=['idade', 'dependentes', 'meses_de_relacionamento',
    'qtd_produtos', 'iteracoes_12m', 'meses_inativo_12m',
    'limite_credito', 'valor_transacoes_12m', 'qtd_transacoes_12m'])

# Seleção das variáveis para correlação
selected_cols = ['idade', 'dependentes', 'meses_de_relacionamento',
    'qtd_produtos', 'iteracoes_12m', 'meses_inativo_12m',
    'limite_credito', 'valor_transacoes_12m', 'qtd_transacoes_12m']

# Calculando a correlação entre as variáveis selecionadas
corr = df[selected_cols].corr()

# Criando o gráfico de correlação
fig, ax = plt.subplots(figsize=(8, 6))
sns.heatmap(corr, annot=True, cmap='coolwarm', ax=ax)

# Exibindo o gráfico
st.pyplot(fig)

# ------------------------------------------------------------
st.markdown("---")

st.header("3. Aplicação de Distribuições Probabilísticas")

# Distribuição Binomial - Análise de Inadimplência
st.subheader("Distribuição Binomial - Probabilidade de Inadimplência")

# Cálculo da probabilidade de inadimplência
inadimplentes = df['default'].sum()  # soma de 1's = total inadimplentes
total_clientes = df['default'].count()  # total de registros
prob_inadimplencia = inadimplentes / total_clientes  # proporção

# Exibindo os dados
st.write(f"**Total de Clientes:** {total_clientes}")
st.write(f"**Inadimplentes:** {inadimplentes}")
st.write(f"**Probabilidade Real de Inadimplência:** {prob_inadimplencia:.2%}")

# Simulação da distribuição binomial com a probabilidade real
n_trials = 100  # Exemplo: 100 clientes
x = np.arange(0, n_trials + 1)  # Número de inadimplentes de 0 a 100
binomial_dist = binom.pmf(x, n_trials, prob_inadimplencia)  # PMF binomial

# Plotando o gráfico
fig, ax = plt.subplots(figsize=(10, 6))
ax.vlines(x, 0, binomial_dist, colors='purple', lw=2)
ax.set_title('Distribuição Binomial - Número de Inadimplentes em 100 Clientes', fontsize=14)
ax.set_xlabel('Número de Inadimplentes', fontsize=12)
ax.set_ylabel('Probabilidade', fontsize=12)
plt.grid(True)
st.pyplot(fig)

# Justificativa
st.markdown("""
**Justificativa:** A variável `default` representa inadimplência (1 para inadimplente, 0 para adimplente), o que caracteriza uma variável binária.  
Por isso, o modelo de **Distribuição Binomial** é adequado para estimar a probabilidade de ocorrência de inadimplentes em amostras de clientes.
""")

st.subheader("""Interpretação dos Resultados:""")
st.markdown("""
A probabilidade real de inadimplência de 16,07% é relativamente alta. Isso indica que cerca de 1 em cada 6 clientes está inadimplente.
\n Essa taxa é significativa e pode ser uma preocupação para a empresa, já que ela representa um risco financeiro considerável.
\n A empresa precisa entender o que está causando esse alto nível de inadimplência. Isso pode ser relacionado a questões econômicas, políticas de crédito mais flexíveis ou até mesmo a falta de controle adequado na análise de crédito dos clientes. A empresa pode usar esses dados para identificar grupos de clientes mais propensos a inadimplência (por exemplo, com base em histórico de crédito, comportamento de pagamento, renda, etc.).
A análise também pode ajudar a descobrir se há uma concentração maior de inadimplentes em determinados segmentos de mercado ou regiões geográficas.

\n A taxa de inadimplência de 16,07% é uma indicação clara de que a empresa enfrenta desafios relacionados à recuperação de crédito. A adoção de uma abordagem analítica para segmentar clientes, ajustar políticas de concessão de crédito e monitorar continuamente o risco de inadimplência são medidas cruciais para minimizar o impacto financeiro e garantir a sustentabilidade a longo prazo.""")

st.markdown("---")

# ----------------- Análise Poisson - Relação entre Tempo de Relacionamento e Inadimplência ----------------------

# Garantindo que as colunas estão no formato correto
df['meses_de_relacionamento'] = pd.to_numeric(df['meses_de_relacionamento'], errors='coerce')
df['default'] = pd.to_numeric(df['default'], errors='coerce')
df = df.dropna(subset=['meses_de_relacionamento', 'default'])

st.subheader("Distribuição de Poisson - Relação entre Tempo de Relacionamento e Inadimplência")

# Filtrando clientes inadimplentes
inadimplentes_df = df[df['default'] == 1]

# Calculando a taxa de inadimplência (λ) - como a distribuição de Poisson modela a quantidade de eventos (inadimplências)
# Vamos contar as inadimplências por intervalo de tempo (meses de relacionamento)
taxa_inadimplencia = len(inadimplentes_df) / df['meses_de_relacionamento'].sum()

# Exibindo a taxa de inadimplência
st.write(f"**Total de Clientes:** {len(df)}")
st.write(f"**Inadimplentes:** {len(inadimplentes_df)}")
st.write(f"**Taxa de Inadimplência (λ):** {taxa_inadimplencia:.5f}")

# Criando o gráfico da distribuição de Poisson
fig, ax = plt.subplots(figsize=(10, 6))

# Gerando os dados para a distribuição de Poisson
max_mes = int(df['meses_de_relacionamento'].max())  # Maximo de meses
x = np.arange(0, max_mes + 1)
y = poisson.pmf(x, taxa_inadimplencia)  # Função de massa de probabilidade (PMF) de Poisson

# Plotando a distribuição
ax.plot(x, y, 'bo', ms=8, label='Distribuição Poisson', color='purple')
ax.vlines(x, 0, y, colors='purple', lw=5)

ax.set_title('Distribuição de Poisson - Tempo de Relacionamento e Inadimplência', fontsize=14)
ax.set_xlabel('Meses de Relacionamento', fontsize=12)
ax.set_ylabel('Probabilidade de Inadimplência', fontsize=12)
ax.legend()

# Exibindo o gráfico
st.pyplot(fig)

# Justificativa
st.markdown("""
**Justificativa:** A **distribuição de Poisson** é utilizada para modelar a ocorrência de eventos (como a inadimplência) em intervalos de tempo fixos. 
Neste caso, estamos considerando a inadimplência como um evento que pode ocorrer ao longo do tempo de relacionamento com o cliente. 
A taxa de inadimplência (λ) é calculada com base na quantidade de inadimplentes e o tempo de relacionamento. O gráfico gerado mostra a probabilidade 
de inadimplência ao longo do tempo de relacionamento, de acordo com a distribuição de Poisson.
""")

st.subheader("""Interpretação dos Resultados:""")
st.markdown("""
 A **Taxa de Inadimplência:** de 0.00447 significa que, em média, cerca de 0.45% dos clientes estão inadimplentes. Esse valor é relativamente baixo, indicando que a maioria dos clientes está cumprindo com suas obrigações de pagamento.
\n Essa taxa pode ser útil para entender o risco financeiro que a empresa enfrenta. Uma taxa de inadimplência baixa pode sugerir que a empresa possui um bom controle de crédito ou que a maior parte de seus clientes está em boa situação financeira. 
é utilizada para modelar a ocorrência de eventos (como a inadimplência) em intervalos de tempo fixos. 
Neste caso, estamos considerando a inadimplência como um evento que pode ocorrer ao longo do tempo de relacionamento com o cliente. 
A taxa de inadimplência (λ) é calculada com base na quantidade de inadimplentes e o tempo de relacionamento. O gráfico gerado mostra a probabilidade 
de inadimplência ao longo do tempo de relacionamento, de acordo com a distribuição de Poisson.
\n A distribuição dos limites de crédito entre os clientes inadimplentes e não inadimplentes pode revelar padrões no comportamento dos clientes. Por exemplo, clientes inadimplentes podem ter limites de crédito mais altos ou mais baixos em comparação com os clientes não inadimplentes.
\n Em resumo, a análise da taxa de inadimplência e da distribuição de limites de crédito entre os clientes inadimplentes e não inadimplentes oferece insights importantes sobre o risco financeiro da empresa. Isso permite ajustes na política de crédito e na segmentação dos clientes para minimizar o impacto da inadimplência.
""")

st.markdown("---")

df['limite_credito'] = pd.to_numeric(df['limite_credito'], errors='coerce')
df['default'] = pd.to_numeric(df['default'], errors='coerce')
df = df.dropna(subset=['limite_credito', 'default'])

# ----------------- Análise Binomial - Relação Limite de Crédito e Inadimplência ----------------------

st.subheader("Distribuição Binomial - Relação entre Limite de Crédito e Inadimplência")

# Definindo faixas para o limite de crédito
limite_credito_bins = pd.cut(df['limite_credito'], bins=10)  # Dividindo em 10 faixas
df['faixa_limite_credito'] = limite_credito_bins

# Calculando a probabilidade de inadimplência em cada faixa de limite de crédito
probabilidades_inadimplencia = df.groupby('faixa_limite_credito')['default'].mean()

# Exibindo a probabilidade de inadimplência por faixa de limite de crédito
# st.write("Probabilidade de Inadimplência por Faixa de Limite de Crédito:")
# st.write(probabilidades_inadimplencia)

# Calculando a distribuição Binomial para cada faixa de limite de crédito
fig, ax = plt.subplots(figsize=(10, 6))

# Iterando pelas faixas de limite de crédito para plotar a distribuição binomial para cada faixa
for faixa, prob in probabilidades_inadimplencia.items():
    n_trials = 100  # Número de tentativas (clientes)
    x = np.arange(0, n_trials + 1)
    binomial_dist = binom.pmf(x, n_trials, prob)
    
    ax.vlines(x, 0, binomial_dist, lw=2, label=f'Faixa: {faixa} (Prob: {prob:.2f})')

# Ajustando o gráfico
ax.set_title('Distribuição Binomial - Limite de Crédito e Inadimplência', fontsize=14)
ax.set_xlabel('Número de Inadimplentes em 100 Clientes', fontsize=12)
ax.set_ylabel('Probabilidade', fontsize=12)
ax.legend(title="Faixas de Limite de Crédito")

# Exibindo o gráfico
st.pyplot(fig)

# Justificativa
st.markdown("""
**Justificativa:** A **Distribuição Binomial** é utilizada para modelar a probabilidade de inadimplência com base em diferentes faixas de limite de crédito.
 Para cada faixa de limite, foi calculado a probabilidade média de inadimplência e aplicado essa probabilidade para modelar o número esperado de inadimplentes
 em uma amostra de 100 clientes.
""")

st.subheader("""Interpretação dos Resultados:""")
st.markdown("""
    A análise da probabilidade de inadimplência para diferentes faixas de limite de crédito sugere que, em algumas faixas de limite, a probabilidade
     de inadimplência pode ser mais elevada. Isso pode indicar que clientes com limite de crédito mais alto possuem maior risco de inadimplência, 
     possivelmente devido a comportamentos de maior risco associados ao crédito disponível.
\n A relação entre limite de crédito e inadimplência pode refletir comportamentos financeiros de clientes. Clientes com 
limites mais altos podem não ter a disciplina financeira necessária para lidar com esses limites, ou podem ter maiores dificuldades econômicas que impactam 
sua capacidade de pagar. Com base nessa análise, a empresa pode considerar ajustar suas políticas de concessão de crédito, oferecendo limites 
mais conservadores ou fazendo uma análise mais detalhada do perfil de risco dos clientes antes de aprovar limites elevados. A empresa pode segmentar seus clientes com base no limite de crédito e nas taxas de inadimplência para adotar estratégias mais 
personalizadas, como ofertas de crédito de menor risco para grupos mais vulneráveis.
\n A análise também pode ser usada para monitorar o risco de inadimplência em tempo real, permitindo que a empresa
 identifique e reaja rapidamente a padrões de inadimplência emergentes em diferentes faixas de limite de crédito.
\n A análise binomial da relação entre limite de crédito e inadimplência fornece insights valiosos sobre o risco associado ao crédito oferecido pela 
empresa. O modelo pode ser útil para ajustar as estratégias de concessão de crédito e minimizar o impacto financeiro da inadimplência, promovendo uma 
abordagem mais equilibrada entre riscos e benefícios para a empresa""")

# Conclusão
st.markdown("---")
st.header("4. Conclusões da Análise")
st.markdown("""
- A maioria dos clientes possui limite de crédito entre valores bem concentrados.
- A inadimplência está presente em uma porcentagem significativa dos clientes, o que justifica o uso da binomial.
- O tempo de relacionamento também influencia a inadimplência, com clientes com mais tempo de relacionamento apresentando menores taxas de inadimplência, o que pode indicar maior fidelidade.
- Possíveis clientes de risco podem ser identificados por padrões em variáveis como limite de crédito e tempo de relacionamento.
""")

# Rodapé
st.markdown("---")
st.markdown("Desenvolvido por Larissa Estella.")
