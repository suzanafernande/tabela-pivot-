import pandas as pd 

# 1-Importando dados
data = pd.read_csv("data/VendaCarros.xlsx - VendaCarros.csv")
#print(type(data))

# 2-Selecionando colunas específicas do dataframe
df = data[["Fabricante", "ValorVenda", "Ano"]]
print(df)

# 3-Criando a tabela pivô
pivot_table = df.pivot_table(
    index="Ano",
    columns="Fabricante",
    values="ValorVenda",
    aggfunc="sum"
)

print(pivot_table)

# 4-Exportando tabela pivô em arquivo excel
pivot_table.to_excel("data/pivot_table.xlsx", "Relatorio")