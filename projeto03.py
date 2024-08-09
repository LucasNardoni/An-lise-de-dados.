import pandas as pd
import plotly.express as px

dados = pd.read_excel("vendas.xlsx")

# visualizando informações das colunas
dados.info()

# contagem de vendas por Loja
dados["loja"].value_counts()

# contagem de vendas por cidade
dados["cidade"].value_counts()

# contagem de tipos de pagamento
dados["forma_pagamento"].value_counts

# faturamento por Loja
dados.groupby("loja")["preco"].sum().to_frame()

# faturamento por Forma de Pagamento
dados.groupby("forma_pagamento")["preco"].sum().to_frame()

# faturamento por estado, cidade, loja e forma de pagamento
dados_agrupados = dados.groupby(["estado", "cidade", "loja", "forma_pagamento"])["preco"].sum().to_frame()

# transformar dados em uma tabela de Excel
dados_agrupados.to_excel("Faturamento.xlsx")

# visualização de dados com geração de gráfico
grafico = px.histogram(dados, x="loja", 
                    y="preco", 
                    text_auto=True,
                    title="Faturamento",
                    color="forma_pagamento")

grafico.show()
grafico.write_html("Faturamento.html")