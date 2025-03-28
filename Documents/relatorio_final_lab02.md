
# Relatório Final – Lab02S03

## 1. Introdução

Este relatório apresenta a etapa final do laboratório **Lab02S03**, cujo objetivo é investigar as características de qualidade de repositórios Java open-source, correlacionando métricas como acoplamento, coesão, tamanho, popularidade, maturidade e atividade. A partir de dados extraídos da plataforma GitHub e analisados com a ferramenta CK, busca-se compreender como aspectos do processo de desenvolvimento impactam métricas de qualidade interna do código.

A hipótese central é que repositórios mais maduros, populares e ativos tendem a apresentar melhores características internas, como menor acoplamento e maior coesão, refletindo boas práticas de engenharia de software.

## 2. Metodologia

### 2.1 Seleção e Coleta de Dados

Foram coletados os 1000 repositórios Java mais populares no GitHub, utilizando a API GraphQL. As métricas de qualidade (CBO, DIT, LCOM) foram extraídas com a ferramenta **CK** (Chidamber & Kemerer Java Metrics), que realiza análise estática dos repositórios clonados.

Além das métricas de qualidade, também foram coletadas informações de processo:
- **Popularidade**: número de estrelas no GitHub  
- **Tamanho**: linhas de código (LOC)  
- **Maturidade**: idade em anos  
- **Atividade**: número de releases publicados  

### 2.2 Visualização e Análise

Para responder às questões de pesquisa (RQ01 a RQ04), foram gerados histogramas representando a distribuição das variáveis mencionadas. As análises utilizam estatísticas descritivas e observações qualitativas com base nas distribuições.

## 3. Análise dos Dados e Resultados

### 3.1 RQ01 – Qual a relação entre popularidade e qualidade?

**Gráfico: Distribuição da Popularidade (Estrelas)**  
*Inserir aqui o gráfico de popularidade (estrelas)*

A distribuição da popularidade é altamente concentrada: a maioria dos repositórios possui menos de 20.000 estrelas, com poucos casos extremos. Isso indica que poucos repositórios dominam em popularidade, o que pode enviesar a análise. A relação com métricas como CBO ou LCOM depende de correlações que devem ser verificadas, mas a distribuição sugere que popularidade extrema não é comum.

### 3.2 RQ02 – Qual a relação entre maturidade e qualidade?

**Gráfico: Distribuição da Maturidade (Idade do Repositório)**  
*Inserir aqui o gráfico de maturidade (idade)*

A maioria dos repositórios tem entre 2 a 14 anos, com uma distribuição relativamente uniforme. Isso demonstra que há projetos de diferentes níveis de maturidade na amostra, o que possibilita investigar se o tempo de vida influencia o acoplamento (CBO) ou coesão (LCOM). Projetos mais antigos tendem a sofrer refatorações, o que pode impactar positivamente na qualidade interna.

### 3.3 RQ03 – Qual a relação entre atividade e qualidade?

**Gráfico: Distribuição da Atividade (Número de Releases)**  
*Inserir aqui o gráfico de releases (atividade)*

A distribuição de releases mostra grande variação, com a maioria dos projetos possuindo entre 0 e 50 lançamentos. Esse dado reflete níveis variados de manutenção contínua. Repositórios com mais releases podem indicar ciclos de desenvolvimento mais curtos e, consequentemente, maior atenção à qualidade.

### 3.4 RQ04 – Qual a relação entre tamanho e qualidade?

**Gráfico: Distribuição do Tamanho (Linhas de Código)**  
*Inserir aqui o gráfico de tamanho (LOC)*

A quantidade de linhas de código nos projetos varia bastante, com muitos repositórios entre 100 mil e 500 mil LOC. Projetos maiores tendem a ser mais complexos e, portanto, podem apresentar maiores desafios de modularidade, o que afeta negativamente métricas como CBO e LCOM.

### 3.5 Métricas de Qualidade

#### CBO – Coupling Between Objects

**Gráfico: Distribuição do CBO**  
*Inserir aqui o gráfico de CBO*

A distribuição do CBO é relativamente uniforme entre os valores 1 e 10. Não há concentração em extremos, sugerindo que os repositórios Java tendem a manter níveis moderados de acoplamento. Isso pode indicar boas práticas de design orientado a objetos.

#### LCOM – Lack of Cohesion of Methods

**Gráfico: Distribuição do LCOM**  
*Inserir aqui o gráfico de LCOM*

O LCOM apresenta uma distribuição relativamente uniforme entre 0 e 1. Isso mostra que, apesar de existirem repositórios com baixa coesão, muitos mantêm coesão interna em níveis satisfatórios. Isso é positivo do ponto de vista da manutenibilidade.

## 4. Conclusão

A análise sugere que:

- A popularidade extrema é rara e não necessariamente reflete melhor qualidade interna.
- Projetos mais maduros tendem a ter variações menores em métricas como CBO e LCOM, o que pode indicar estabilização estrutural.
- Alta atividade (mais releases) parece estar associada a práticas de desenvolvimento contínuo, potencialmente favorecendo qualidade.
- Projetos muito grandes (em LOC) podem apresentar maior acoplamento ou menor coesão, mas isso depende do design interno adotado.

## 5. Considerações Finais

Este relatório conclui o **Lab02S03**, consolidando os resultados obtidos por meio da análise dos 1000 repositórios Java mais populares no GitHub. As correlações entre características de processo (popularidade, tamanho, atividade e maturidade) e métricas de qualidade interna oferecem insights importantes para o entendimento da saúde estrutural de sistemas Java open-source. O estudo pode servir como base para investigações futuras que envolvam análise de qualidade de software em larga escala.
