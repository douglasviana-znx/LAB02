# LAB02 - Projeto de Pesquisa de Repositórios GitHub  

## Colaboradores  

- Douglas Viana Fernandes  
- Raul Fernandes Goulart  
- Henrique Povoa Peixoto  

## Descrição  

O objetivo deste projeto é fazer uma pesquisa na API do GitHub para buscar repositórios populares na linguagem Java. A aplicação coleta informações sobre repositórios, como o nome, URL, número de estrelas, forks, data de criação, último push, tamanho e número de issues abertas. Além disso, são analisadas métricas de processo e qualidade para uma melhor compreensão das características dos repositórios. Os dados são então salvos em um arquivo CSV para análise posterior.  

A análise inclui a coleta de métricas utilizando a ferramenta **CK (Chidamber & Kemerer Java Metrics)**, que extrai métricas de qualidade do código-fonte dos repositórios. Os resultados são utilizados para gerar **relatórios estatísticos e gráficos**, auxiliando na compreensão das tendências dos repositórios Java.  

## Funcionalidades  

- Conectar à API do GitHub para buscar repositórios na linguagem Java.  
- Ordenar os repositórios por número de estrelas.  
- Armazenar os resultados em um arquivo CSV com as informações relevantes.  
- Suporte a autenticação via token de acesso pessoal para evitar limites de taxa de API.  
- **Coletar métricas de qualidade do código-fonte usando CK.**  
- **Gerar relatórios estatísticos e gráficos para análise das métricas coletadas.**  
- Analisar métricas de processo, como popularidade, tamanho, atividade e maturidade.  
- Analisar métricas de qualidade, como CBO, DIT e LCOM.  

## Métricas Coletadas  

### Métricas de Processo:  
- **Popularidade:** Número de estrelas  
- **Tamanho:** Linhas de código (LOC) e Linhas de comentários  
- **Atividade:** Número de releases  
- **Maturidade:** Idade (em anos) do repositório  

### Métricas de Qualidade (extraídas com CK):  
- **CBO (Coupling Between Objects):** Grau de acoplamento entre classes  
- **DIT (Depth of Inheritance Tree):** Profundidade da árvore de herança  
- **LCOM (Lack of Cohesion of Methods):** Falta de coesão entre os métodos  

## Pré-requisitos  

- Python 3.x instalado.  
- Bibliotecas Python: `requests`, `pandas`, `matplotlib`, `numpy`.  
- Conta no GitHub (para criar um token de acesso pessoal).  
- **Ferramenta CK para análise de código Java** ([Chidamber & Kemerer Java Metrics](https://github.com/mauricioaniche/ck)).  

## Instalação  

1. **Clone este repositório:**  

   ```bash
   git clone https://github.com/douglasviana-znx/LAB02.git
   cd LAB02
