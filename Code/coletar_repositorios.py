import requests
import pandas as pd
import time

# Configurações da API do GitHub (insira seu token pessoal)
GITHUB_TOKEN = "token"
HEADERS = {"Authorization": f"token {GITHUB_TOKEN}"} if GITHUB_TOKEN else {}

# URL da API do GitHub para buscar os repositórios mais populares escritos em Java
URL = "https://api.github.com/search/repositories?q=language:java&sort=stars&order=desc&per_page=100"

repos = []

# Coleta os dados em 10 páginas (10 x 100 = 1000 repositórios)
for page in range(1, 11):
    print(f"Buscando página {page}...")
    response = requests.get(f"{URL}&page={page}", headers=HEADERS)
    time.sleep(1)  # Evita sobrecarga na API

    if response.status_code == 200:
        data = response.json()
        for repo in data["items"]:
            repos.append({
                "Nome": repo["name"],
                "URL": repo["html_url"],
                "Estrelas": repo["stargazers_count"],
                "Forks": repo["forks_count"],
                "Criado": repo["created_at"],
                "Último Push": repo["pushed_at"],
                "Tamanho": repo["size"],
                "Issues Abertas": repo["open_issues_count"]
            })
    else:
        print(f"Erro ao buscar dados (Status Code: {response.status_code})")
        break

# Salva os dados coletados em um arquivo CSV
df = pd.DataFrame(repos)
df.to_csv("repositorios_java.csv", index=False)
print("Arquivo CSV 'repositorios_java.csv' salvo com sucesso!")
