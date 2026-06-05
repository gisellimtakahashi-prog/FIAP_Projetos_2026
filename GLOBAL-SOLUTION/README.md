<h1 align="center">FIAP - Faculdade de Informática e Administração Paulista</h1>

<p align="center">
    <img src="https://github.com/agodoi/templateFiapVfinal/raw/main/assets/logo-fiap.png" alt="FIAP" width="300">
</p>

# Lunar Resource & Solar Weather Integrated Monitor 

Sistema integrado de monitoramento do clima espacial e modelagem mineralógica lunar com foco na detecção de Ilmenita ($\text{FeTiO}_3$) e estimativa preditiva de Hélio-3 ($^3\text{He}$) via aprendizado de máquina.

### 👨‍🎓 Integrantes (FIAP - Global Solution)
* **David Lacerda** (RM570350)
* **Giselli Mayumi Takahashi Yokoyama** (RM572690)
* **João Otávio Moraes** (RM573227)
* **Renata de Almeida Marinho** (RM569342)

### 👩‍🏫 Corpo Docente e Orientação
* **Tutor(a):** Nicolly Candida Rodrigues de Souza
* **Coordenador(a):** André Godoi Chiovato

---

## 📌 Visão Geral do Projeto

Este sistema foi desenvolvido como uma ferramenta acadêmica de suporte à prospecção espacial e engenharia de recursos extraplanetários. A plataforma monitora dados dinâmicos do vento solar interplanetário e os correlaciona com dados mineralógicos históricos obtidos por missões lunares, aplicando um modelo preditivo para mapear os locais com maior potencial de concentração de Hélio-3 no regolito lunar.

O ecossistema é dividido em quatro módulos principais:
1. **Módulo de Clima Espacial:** Processamento cinético do plasma solar e do Campo Magnético Interplanetário (IMF).
2. **Módulo Geoquímico e IA:** Calibração por Regressão Linear com base em amostras físicas coletadas pelas missões Apollo.
3. **Dashboard Visual:** Interface analítica unificada e balanceada para visualização científica de dados.
4. **Pipeline de Exportação:** Persistência de dados em arquivos estruturados (`.csv`, `.json` e `.png`).

---

## 🔬 Fundamentação Científica

Devido à ausência de uma atmosfera densa e de um campo magnético global protetor, a superfície da Lua é continuamente bombardeada pelo vento solar. O Hélio-3 ($^3\text{He}$), um isótopo leve promissor para reatores de fusão nuclear limpa, é implantado diretamente nos grãos do regolito.

Estudos geoquímicos (e.g., Cameron, 1992) confirmam que a eficiência de aprisionamento do Hélio-3 está correlacionada com a abundância de Dióxido de Titânio ($\text{TiO}_2$) presente na **Ilmenita** ($\text{FeTiO}_3$). A malha cristalina deste mineral atua como uma armadilha molecular estável para os íons incidentes.

O sistema fornece estimativas espaciais e validações numéricas baseando-se no modelo empírico parametrizado:
$$[^3\text{He}] \approx (2.4 \times \text{TiO}_2\% + 0.5) \times \text{fator\_fluxo\_solar}$$

---

## 🛠️ Tecnologias e Dependências

O projeto foi codificado seguindo rigorosamente as diretrizes de estilo da **PEP 8**. As seguintes bibliotecas do ecossistema científico do Python são necessárias:

* **NumPy & Pandas:** Manipulação matricial e estruturação de séries temporais de dados espaciais.
* **Matplotlib:** Renderização cartográfica e plotagem multigráfica via `GridSpec`.
* **Scikit-Learn:** Treinamento do estimador de Inteligência Artificial (`LinearRegression`).

### Instalação das Dependências
Instale os pacotes requeridos através do gerenciador de pacotes:
```bash
pip install numpy pandas matplotlib scikit-learn requests
```

---

## 📡 Fontes de Dados Utilizadas


| Módulo | Satélite / Missão | API | Auth |
| :--- | :--- | :--- | :--- |
| Vento solar (plasma) | NOAA DSCOVR | `services.swpc.noaa.gov` | Nenhuma |
| Campo magnético (IMF) | NOAA DSCOVR | `services.swpc.noaa.gov` | Nenhuma |
| CME / Flares / Tempestades | ACE, WIND, DSCOVR | `api.nasa.gov/DONKI` | NASA API Key |
| Ilmenita / $\text{TiO}_2$ | Chandrayaan-1 M3 | `cmr.earthdata.nasa.gov` | Earthdata Token |
| Ti, Fe, He-3 | JAXA SELENE/Kaguya | `darts.isas.jaxa.jp` | Nenhuma |
| Datasets gerais | LRO, Lunar Prospector | `pds.nasa.gov/api` | Nenhuma |

---

## 🔑 Credenciais Necessárias

Antes de executar o monitor, é obrigatório configurar o ambiente com as chaves de autenticação de duas APIs científicas da NASA. Siga os procedimentos abaixo:

#### 1. NASA API Key
* **Finalidade:** Fornece acesso ao inventário de clima espacial do DONKI (CMEs, Flares e Tempestades).
* **Como Obter:** 
  1. Acesse o portal oficial [NASA Open APIs](https://nasa.gov).
  2. Preencha o formulário de cadastro com seu nome e e-mail.
  3. Clique em **Generate API Key**. A chave token será enviada instantaneamente para a sua caixa de entrada.

#### 2. NASA Earthdata Token
* **Finalidade:** Permite realizar consultas aos metadados espectrais das sondas Chandrayaan-1 (M3) e LRO via repositório CMR.
* **Como Obter:**
  1. Acesse o portal de gerenciamento de perfil [Earthdata Login](https://nasa.gov).
  2. Crie uma conta gratuita clicando em **Register for a Profile**.
  3. Após efetuar o login, navegue até a guia **Profile** e selecione **Generate Token**. Copie a hash gerada.

### ⚙️ Configuração do Arquivo de Ambiente (`.env`)

Crie um arquivo de texto genérico nomeado exatamente como `.env` na mesma pasta que o seu script e cole o conteúdo abaixo substituindo com suas chaves:

```env
NASA_API_KEY=SUA_CHAVE_NASA_AQUI
EARTHDATA_TOKEN=SEU_TOKEN_EARTHDATA_AQUI
OUTPUT_DIR=./outputs
DATA_WINDOW_DAYS=7
```

---

## 🚀 Como Executar o Sistema

Para inicializar o pipeline de coleta, modelagem de IA, validação de acurácia no terminal e exibição do dashboard visual, execute o script central:

```bash
python lunar_monitor.py
```

---

## 📁 Estrutura de Arquivos de Saída (Módulo 4)

Ao final de cada execução bem-sucedida, o sistema cria um diretório `./outputs/` contendo os seguintes artefatos estruturados para auditoria científica:

* `solar_wind_plasma.csv`: Dados temporais de velocidade ($km/s$), densidade e temperatura do plasma interplanetário.
* `solar_wind_mag.csv`: Vetores magnéticos interplanetários com foco no componente de inclinação $B_z$ ($nT$).
* `cme_events.json` & `flare_events.json`: Inventário estruturado de alertas de atividade solar severa.
* `lunar_ilmenite_regions.csv`: Tabela das regiões selenográficas de maior viabilidade econômica ranqueadas por teor mineral.
* `he3_map_sample.csv`: Matriz amostral georreferenciada do potencial global de Hélio-3.
* `m3_granules.json`: Metadados simulados de indexação de arquivos espectrais do *Moon Mineralogy Mapper* (M3 - Chandrayaan-1).
* `dashboard_YYYYMMDD_HHMMSS.png`: Cópia estática renderizada em alta definição ($140\text{ DPI}$) do painel visual analítico.

---

## 📊 Arquitetura do Dashboard Analítico

O painel visual unificado exibe cinco quadrantes integrados estrategicamente para evitar sobreposição ou truncamento de rótulos:

1. **Velocidade do Vento Solar:** Gráfico temporal (7 dias) que atua como indicador do fluxo cinético incidente.
2. **Componente IMF $B_z$:** Gráfico de linhas dinâmico codificado por cor (Azul: orientação Norte, Laranja: orientação Sul, indicativo de perturbação magnética).
3. **Modelo Preditivo IA:** Gráfico de dispersão cruzando as amostras de laboratório das missões Apollo com a linha de tendência matemática gerada pelo Scikit-Learn.
4. **Mapa Global Potencial:** Projeção bidimensional em escala de contorno contínuo (`viridis`) mapeando os mares lunares basálticos mais ricos em voláteis energéticos.
5. **Top Alvos de Mineração:** Tabela de engenharia integrada que sintetiza as quatro melhores coordenadas geográficas lunares para futuras missões de pouso e prospecção de recursos in situ (*ISRU*).

---

## 📝 Licença e Finalidade Acadêmica

Este projeto possui finalidade puramente acadêmica e de pesquisa científica. Os dados utilizados e gerados nas simulações baseiam-se em coeficientes teóricos e padrões reais estabelecidos por agências aeroespaciais (NASA, NOAA, JAXA e USGS).

---

## 📚 Referências Bibliográficas e Documentais

* **Cameron, E. N. (1992):** *Helium Resources of Mare Tranquillitatis*. Wisconsin Center for Space Automation and Robotics, Technical Report WCSAR-TR-AR3-9207-1.
* **Wittenberg, L. J., Cameron, E. N., et al. (1992):** *A Review of Helium-3 Resources and Acquisition for Use as Fusion Fuel*. Fusion Technology, v. 21, pp. 2230-2253.
* **Fa, W., & Jin, Y. Q. (2007):** *Quantitative Estimation of Helium-3 Distribution in Lunar Regolith Using Solar Wind Implantation Models*. Progress in Electromagnetics Research, v. 7, pp. 465-472.
* **Pieters et al. (2009):** *Characterization of the Moon Mineralogy Mapper (M3) aboard Chandrayaan-1*. Current Science, v. 96, n. 4.
* **Ogawa et al. (2011):** *Elemental Composition Maps from SELENE/Kaguya Gamma-Ray Spectrometer (GRS)*. JAXA DARTS Planetology Database.
* **NASA DONKI Portal:** [CCMC Space Weather Inventory](https://nasa.gov).
* **NOAA SWPC Operations:** [Space Weather Prediction Center Data Access](https://noaa.gov).
* **NASA CMR Program:** [Common Metadata Repository Gateway](https://nasa.gov).
* **JAXA DARTS System:** [Data Archives and Transmission System for Space Science](https://jaxa.jp).

