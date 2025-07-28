import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt  

# Carregar a planilha
dados = pd.read_csv('data.csv') 

# especifica que as colunas 'id' e 'Unnamed: 32' devem ser removidas. inplace=True significa que a remoção é feita no próprio DataFrame sem criar uma cópia.
dados.drop(columns=['id', 'Unnamed: 32'], inplace=True)
dados.shape

# O método .map() é usado para transformar os valores de uma coluna (Series) com base em uma função ou um dicionário de mapeamento.
dados['diagnosis'] = dados['diagnosis'].map({'M': 1, 'B': 0})

# Correlacao entre as variaveis com relacao ao alvo diagnosis
corr_com_diagnosis = dados.corr()['diagnosis'].abs().sort_values(ascending=False)
print('Correlacao com o alvo:')
print(corr_com_diagnosis)

# Filtrar variáveis com correlação maior que 0.7
maior_corr_com_diagnosis = corr_com_diagnosis[corr_com_diagnosis > 0.7].index.tolist()


print('Variaveis com correlacao maior que 0.7 com o alvo:')
print(maior_corr_com_diagnosis)

# Plotar o pairplot com as variáveis que têm correlação maior que 0.7 com o alvo 'diagnosis'
"""
pair = sns.pairplot(dados[maior_corr_com_diagnosis], hue='diagnosis',
                    diag_kind='auto', corner=True , height=5, kind='scatter')

# Adjust the legend
legend = pair._legend
legend.set_title("Diagnosis", prop={'size': 30})  
for text in legend.texts:
    if text.get_text() == '0':
        text.set_text('Benign')
    elif text.get_text() == '1':
        text.set_text('Malignant')
    text.set_fontsize(30)

# Move legend outside
legend.set_bbox_to_anchor((0.9, 0.8))

# Show plot
plt.show()

"""