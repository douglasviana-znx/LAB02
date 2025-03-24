import requests
import pandas as pd
import time

# API do GitHub
GITHUB_TOKEN = "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" 
HEADERS = {"Authorization": f"token {GITHUB_TOKEN}"} if GITHUB_TOKEN else {}

# Função para buscar os repositórios mais populares de Java
def buscar_repositorios_java():
    repos = []
    url = "https://api.github.com/search/repositories?q=language:java&sort=stars&order=desc&per_page=100"

    for page in range(1, 11):  
        print(f"Buscando página {page}...")

       
        time.sleep(1)
        
        response = requests.get(f"{url}&page={page}", headers=HEADERS)

        if response.status_code == 200:
            data = response.json()
            if "items" in data:
                for repo in data["items"]:
                    repos.append([
                        repo["name"], repo["html_url"], repo["stargazers_count"], repo["forks_count"],
                        repo["created_at"], repo["pushed_at"], repo["size"], repo["open_issues_count"]
                    ])
            else:
                print(f"Sem repositórios encontrados na página {page}.")
                break
        else:
            print(f"Erro ao buscar dados (Status Code: {response.status_code}).")
            break

    return repos


repositorios = buscar_repositorios_java()
if repositorios:
    df = pd.DataFrame(repositorios, columns=["Nome", "URL", "Estrelas", "Forks", "Criado", "Último Push", "Tamanho", "Issues Abertas"])
    df.to_csv("repositorios_java.csv", index=False)
    print("Arquivo CSV salvo com sucesso!")
else:
    print("Nenhum repositório foi encontrado.")
