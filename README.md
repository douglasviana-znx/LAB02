# LAB02 - Projeto de Pesquisa de Repositórios GitHub

## Descrição

O objetivo deste projeto é fazer uma pesquisa na API do GitHub para buscar repositórios populares na linguagem Java. A aplicação coleta informações sobre repositórios, como o nome, URL, número de estrelas, forks, data de criação, último push, tamanho e número de issues abertas. Os dados são então salvos em um arquivo CSV para análise posterior.

## Funcionalidades

- Conectar à API do GitHub para buscar repositórios na linguagem Java.
- Ordenar os repositórios por número de estrelas.
- Armazenar os resultados em um arquivo CSV com as informações relevantes.
- Suporte a autenticação via token de acesso pessoal para evitar limites de taxa de API.

## Pré-requisitos

- Python 3.x instalado.
- Bibliotecas Python: `requests`, `pandas` (para lidar com requisições e salvar dados no formato CSV).
- Conta no GitHub (para criar um token de acesso pessoal).

## Instalação

1. **Clone este repositório:**

   ```bash
   git clone https://github.com/douglasviana-znx/LAB02.git
   
