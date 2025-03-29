import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import spearmanr, pearsonr

# Carregar os dados coletados
df_repos = pd.read_csv("repositorios_java.csv")
df_metricas = pd.read_csv("metricas_ck.csv")

# Unir os datasets para análise
df = df_repos.merge(df_metricas, left_on="Nome", right_on="file", how="inner")

# Estatísticas descritivas
estatisticas = df.describe()
print(estatisticas)

# Gráficos de dispersão para correlação entre métricas de qualidade e popularidade
sns.pairplot(df, vars=["Estrelas", "Tamanho", "cbo", "dit", "lcom"], diag_kind='kde')
plt.savefig("graficos_correlacao.png")
plt.show()

# Calcular correlação de Spearman e Pearson
correlacoes = {}
for col in ["Estrelas", "Tamanho", "cbo", "dit", "lcom"]:
    correlacoes[col] = {
        "Spearman": spearmanr(df[col], df["Forks"])[0],
        "Pearson": pearsonr(df[col], df["Forks"])[0]
    }

# Geração de relatório
with open("relatorio.txt", "w") as f:
    f.write("### Relatório de Análise dos Repositórios Java\n\n")
    f.write("#### Estatísticas Descritivas\n")
    f.write(str(estatisticas) + "\n\n")
    f.write("#### Correlações\n")
    for k, v in correlacoes.items():
        f.write(f"{k}: Spearman={v['Spearman']}, Pearson={v['Pearson']}\n")

print("Relatório gerado com sucesso!")
