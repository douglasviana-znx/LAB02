import requests
import pandas as pd

# Seu token de autenticação (opcional)
GITHUB_TOKEN = "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"
HEADERS = {"Authorization": f"token {GITHUB_TOKEN}"} if GITHUB_TOKEN else {}

# API do GitHub para buscar repositórios Java
URL = "https://api.github.com/search/repositories?q=language:java&sort=stars&order=desc&per_page=100"

repos = []

# O GitHub retorna no máximo 100 por página, então precisamos de 10 páginas
for page in range(1, 11):
    response = requests.get(f"{URL}&page={page}", headers=HEADERS)
    data = response.json()
    
    for repo in data["items"]:
        repos.append({
            "name": repo["full_name"],
            "stars": repo["stargazers_count"],
            "url": repo["html_url"],
            "created_at": repo["created_at"],
            "updated_at": repo["updated_at"]
        })

# Salvar em CSV
df = pd.DataFrame(repos)
df.to_csv("repositorios_java.csv", index=False)
print("Arquivo repositorios_java.csv salvo com sucesso!")
