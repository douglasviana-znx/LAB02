import os
import pandas as pd

# Caminho para o repositório CK (baixe e extraia do GitHub)
CK_JAR_PATH = "ck-0.7.1-SNAPSHOT-jar-with-dependencies.jar"
TARGET_FOLDER = "Code/Lab02/ck-master"  # Pasta onde os repositórios serão analisados

# Comando para executar a ferramenta CK
ck_command = f"java -jar {CK_JAR_PATH} {TARGET_FOLDER} false 0 true"

# Executar a ferramenta CK
os.system(ck_command)

# Carregar os arquivos CSV gerados pela CK
ck_classes = pd.read_csv("class.csv")
ck_methods = pd.read_csv("method.csv")

# Salvar um resumo das métricas de interesse
ck_summary = ck_classes[["file", "class", "cbo", "dit", "lcom"]]
ck_summary.to_csv("metricas_ck.csv", index=False)
print("Métricas de qualidade extraídas e salvas em 'metricas_ck.csv'.")
