# FIAP - Faculdade de Informática e Administração Paulista

<p align="center">
<a href= "https://www.fiap.com.br/"><img src="assets/logo-fiap.png" alt="FIAP - Faculdade de Informática e Admnistração Paulista" border="0" width=40% height=40%></a>
</p>

<br>

# FarmTech Solutions — Fase 3 Cap 1: Banco de Dados Estruturado + Machine Learning no Agronegócio

## FarmTech Solutions

## 👨‍🎓 Integrantes: 
- David Ribeiro Prado de Lacerda — RM570350
- Giselli Mayumi Takahashi Yokoyama — RM572690
- João Otavio Moraes — RM573227
- Renata de Almeida Marinho — RM569342
- Richard Wrobel dos Santos — RM573998

## 👩‍🏫 Professores:
### Tutor(a) 
- Nicolly Candida Rodrigues de Souza
### Coordenador(a)
- André Godoi Chiovato


## 📜 Descrição

Este projeto corresponde à **Fase 3 — Capítulo 1** da trilha PBL do curso de Inteligência Artificial da FIAP, dando continuidade ao trabalho da FarmTech Solutions, startup acadêmica fictícia voltada para soluções de IA, IoT e Ciência de Dados no agronegócio. O trabalho está dividido em duas partes complementares.

A **entrega obrigatória** consiste em estruturar em um banco de dados relacional Oracle os dados produzidos na Fase 2 Cap 1 — quando desenvolvemos um sistema IoT de irrigação inteligente para a cultura do milho usando ESP32, sensor DHT22, sensor LDR e três botões representando os nutrientes N, P e K. As leituras geradas pela simulação no Wokwi foram exportadas como CSV e agora importadas via Assistente de Importação do Oracle SQL Developer para a tabela `FARMSENSORES_AGRICOLAS`, com definição apropriada dos tipos de dados de cada coluna. Sobre esses dados foram executadas seis consultas SQL exploratórias que filtram registros por temperatura, umidade, pH, presença de chuva e estado da bomba de irrigação, demonstrando a capacidade do banco em responder perguntas relevantes para o monitoramento da lavoura.

A entrega **Ir Além Opção 2 — Machine Learning no Agronegócio** aplica cinco algoritmos de classificação supervisionada sobre a base `produtos_agricolas.csv` (2200 amostras, 22 culturas) para construir um recomendador de culturas a partir de variáveis de solo e clima (N, P, K, temperatura, umidade, pH, chuva). O trabalho inclui análise exploratória com cinco gráficos, identificação do perfil ideal de solo e clima para três culturas escolhidas (arroz, milho e café) e avaliação comparativa entre KNN, Decision Tree, Random Forest, SVM e Logistic Regression, identificando o modelo de melhor desempenho.

Esta fase pavimenta o caminho para a Fase 4, na qual os dados estruturados no banco e os modelos preditivos desenvolvidos serão consumidos por um dashboard com Data Science.


## 📁 Estrutura de pastas

Dentre os arquivos e pastas presentes na raiz do projeto, definem-se:

- <b>assets</b>: aqui estão os arquivos relacionados a elementos não-estruturados deste repositório, como a logo da FIAP e os prints das telas do Oracle SQL Developer utilizados como evidência da entrega obrigatória.

- <b>document</b>: aqui estão os artefatos centrais do projeto: o arquivo `sensores_agricolas.csv` (dados gerados pela simulação Wokwi na Fase 2 e importados no Oracle), o notebook `ml_agronegocio.ipynb` (entrega Ir Além) e o dataset `Atividade_Cap10_produtos_agricolas.csv` (base de treinamento dos modelos de Machine Learning).

- <b>src</b>: contém o código-fonte `irrigacao.ino`, escrito em C++ para o ESP32, que gerou as leituras de sensores utilizadas na entrega obrigatória.

- <b>README.md</b>: arquivo que serve como guia e explicação geral sobre o projeto (o mesmo que você está lendo agora).


## 🔧 Como executar o código

### Pré-requisitos

- [Oracle SQL Developer](https://www.oracle.com/database/sqldeveloper/technologies/download/) — para a entrega obrigatória
- Python 3.10+ com Jupyter Notebook — para o Ir Além
- Bibliotecas Python: `pandas`, `numpy`, `matplotlib`, `seaborn`, `scikit-learn`
- Acesso ao banco Oracle FIAP (RM + senha de aluno)
- Conta no [Wokwi](https://wokwi.com/) para reproduzir a simulação do ESP32 (opcional)

### Parte 1 — Entrega Obrigatória (Banco Oracle)

1. Instale o Oracle SQL Developer.
2. Crie uma nova conexão com os seguintes parâmetros:

| Campo | Valor |
|---|---|
| Nome | FIAP |
| Nome do Usuário | seu RM (ex.: RM570350) |
| Senha | data de nascimento (DDMMYY) |
| Nome do Host | `oracle.fiap.com.br` |
| Porta | `1521` |
| SID | `ORCL` |

3. Após conectar, clique com o botão direito em **Tabelas (Filtrado)** → **Importar Dados** e carregue o arquivo `document/sensores_agricolas.csv`.
4. Nomeie a tabela como `farmsensores_agricolas` e defina os tipos das colunas:
   - `N`, `P`, `K` como `NUMBER(1)`
   - `temperatura`, `umidade`, `ph`, `chuva` como `NUMBER(5,2)`
   - `label` (renomear para `cultura`) e `irrigacao` como `VARCHAR2(30)`
5. Após a importação, execute as consultas SQL documentadas mais abaixo.

### Parte 2 — Ir Além (Machine Learning)

1. Abra o arquivo `document/ml_agronegocio.ipynb` no Jupyter Notebook, VSCode ou Google Colab.
2. Certifique-se de que o arquivo `document/Atividade_Cap10_produtos_agricolas.csv` está no mesmo diretório do notebook (ou ajuste o caminho no `pd.read_csv`).
3. Execute as células em ordem. O notebook está organizado em seis seções: importação de bibliotecas, análise exploratória, limpeza, perfil ideal das três culturas, modelagem preditiva com cinco algoritmos e conclusão comparativa.

---

## 🗄️ Detalhamento da Entrega Obrigatória (Oracle)

### Modelo de Dados

A tabela `FARMSENSORES_AGRICOLAS` armazena as leituras dos sensores agrícolas simulados no Wokwi:

| Coluna | Tipo | Descrição |
|---|---|---|
| `N` | NUMBER(1) | Presença de Nitrogênio (1=pressionado, 0=não) |
| `P` | NUMBER(1) | Presença de Fósforo (1=pressionado, 0=não) |
| `K` | NUMBER(1) | Presença de Potássio (1=pressionado, 0=não) |
| `TEMPERATURA` | NUMBER(5,2) | Temperatura do ambiente em °C (DHT22) |
| `UMIDADE` | NUMBER(5,2) | Umidade do solo em % (DHT22) |
| `PH` | NUMBER(5,2) | pH do solo (calculado via LDR + influência NPK) |
| `CHUVA` | NUMBER(5,2) | Chuva prevista em mm (OpenWeather API) |
| `CULTURA` | VARCHAR2(30) | Cultura monitorada (milho) |
| `IRRIGACAO` | VARCHAR2(20) | Estado da bomba de irrigação (LIGADA/DESLIGADA) |

### Passo a passo da importação

**Etapa 1 — Visualização de Dados:** carregamos o `sensores_agricolas.csv` configurando UTF-8 e delimitador correto.

![Etapa 1 - Visualização](assets/print01.jpg)

**Etapa 2 — Método de Importação:** método **Inserir**, tabela `farmsensores_agricolas`.

![Etapa 2 - Método](assets/print2.jpg)

**Etapa 4 — Definição de Colunas:** tipos numéricos para sensores e `VARCHAR2` para categóricas. A coluna `label` do CSV foi renomeada para `cultura`.

![Etapa 4 - Coluna numérica](assets/print3.jpg)

![Etapa 4 - Coluna categórica](assets/print4.jpg)

### Consultas SQL realizadas

**1. Listagem completa** — retorna os 10 registros.
```sql
SELECT * FROM farmsensores_agricolas;
```
![SELECT *](assets/print5.jpg)

**2. Temperatura elevada** — 6 registros acima de 30°C.
```sql
SELECT * FROM farmsensores_agricolas WHERE temperatura > 30;
```
![Temperatura > 30](assets/print6.jpg)

**3. Baixa umidade** — 6 registros abaixo de 40%.
```sql
SELECT * FROM farmsensores_agricolas WHERE umidade < 40;
```
![Umidade < 40](assets/print7.jpg)

**4. pH ideal para milho** — 8 registros entre 5.5 e 7.0.
```sql
SELECT * FROM farmsensores_agricolas WHERE ph BETWEEN 5.5 AND 7.0;
```
![pH ideal](assets/print8.jpg)

**5. Chuva prevista** — 2 registros com previsão > 0mm.
```sql
SELECT * FROM farmsensores_agricolas WHERE chuva > 0;
```
![Chuva > 0](assets/print9.jpg)

**6. Bomba ligada** — 5 registros em que o sistema acionou a irrigação.
```sql
SELECT * FROM farmsensores_agricolas WHERE irrigacao = 'LIGADA';
```
![Irrigação ligada](assets/print10.jpg)

---

## 🤖 Detalhamento do Ir Além (ML no Agronegócio)

Notebook: [`document/ml_agronegocio.ipynb`](document/ml_agronegocio.ipynb)

### Análise Exploratória (5 gráficos)

1. Distribuição das culturas (`countplot`)
2. Temperatura por cultura (`boxplot`)
3. Umidade × Temperatura (`scatterplot`)
4. Mapa de correlação das variáveis (`heatmap`)
5. Distribuição do pH (`histplot` com KDE)

### Perfil ideal — 3 culturas

Foram selecionadas **arroz (rice)**, **milho (maize)** e **café (coffee)**. A análise comparou as médias de N, P, K, temperatura, umidade, pH e chuva entre essas culturas, evidenciando preferências distintas (ex.: café com maior demanda de Potássio; arroz com alta umidade e precipitação).

### Modelos preditivos (5 algoritmos)

| # | Algoritmo | Categoria |
|---|---|---|
| 1 | K-Nearest Neighbors (k=9) | Baseado em distância |
| 2 | Decision Tree | Baseado em árvores |
| 3 | Random Forest | Ensemble de árvores |
| 4 | SVM (kernel linear) | Margem máxima |
| 5 | Logistic Regression (max_iter=500) | Linear probabilístico |

### Avaliação comparativa

As acurácias foram consolidadas em um DataFrame e plotadas em `barplot` ordenado. O **Random Forest apresentou a maior acurácia**, demonstrando maior capacidade de identificar corretamente as culturas com base nas variáveis de solo e clima.

---

## 🎥 Vídeos demonstrativos

- **Entrega Obrigatória (Banco Oracle):** 🔗 [Assista no YouTube](https://www.youtube.com/watch?v=ucNDfMzeHB4)
- **Ir Além — Machine Learning:** 🔗 [Assista no YouTube](https://www.youtube.com/watch?v=gklpQlGFrI0)


## 🗃 Histórico de lançamentos

* 1.0.0 - 19/05/2026
    * Entrega obrigatória da Fase 3 Cap 1: importação dos dados gerados na Fase 2 Cap 1 no Oracle FIAP, criação e definição da tabela `farmsensores_agricolas` e execução de 6 consultas SQL exploratórias documentadas com prints.
    * Ir Além Opção 2: notebook de Machine Learning com 5 gráficos exploratórios, perfil ideal de 3 culturas e comparação de 5 modelos de classificação supervisionada sobre a base `produtos_agricolas.csv`.


## 📋 Licença

<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"><p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/agodoi/template">MODELO GIT FIAP</a> por <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://fiap.com.br">Fiap</a> está licenciado sobre <a href="http://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">Attribution 4.0 International</a>.</p>
