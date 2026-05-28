# FIAP - Faculdade de Informática e Administração Paulista

<p align="center">
<a href= "https://www.fiap.com.br/"><img src="assets/logo-fiap.png" alt="FIAP - Faculdade de Informática e Admnistração Paulista" border="0" width=40% height=40%></a>
</p>

<br>

# FarmTech Solutions — Fase 2: Sistema de Irrigação Inteligente

## FarmTech Solutions — Grupo 7

## 👨‍🎓 Integrantes: 
- David Ribeiro Prado de Lacerda (RM570350)
- Giselli Mayumi Takahashi Yokoyama (RM572690)
- Renata de Almeida Marinho (RM569342)
- Richard Wrobel dos Santos (RM573998)

## 👩‍🏫 Professores:
### Tutor(a) 
- Nicolly Candida Rodrigues de Souza
### Coordenador(a)
- André Godoi Chiovato


## 📜 Descrição

A **FarmTech Solutions** continua sua jornada na Agricultura Digital. Nesta Fase 2, avançamos no sistema de gestão agrícola desenvolvendo um dispositivo embarcado capaz de **monitorar o solo em tempo real** e **controlar automaticamente a irrigação** de uma lavoura de **milho (*Zea mays*)**, tomando como região de referência **Sorriso/MT**, maior produtor nacional da cultura segundo o IBGE.

O sistema foi projetado no simulador **Wokwi.com**, usando um **ESP32 DevKit v4** programado em **C/C++**, e integra cinco fontes de dados para decidir quando acionar a bomba d'água (representada por um relé):

- **3 botões verdes** simulam os sensores de **Nitrogênio (N)**, **Fósforo (P)** e **Potássio (K)**. Cada botão pressionado influencia o pH do solo, reproduzindo didaticamente o efeito químico real dos fertilizantes: N acidifica (−2.0), P alcaliniza moderadamente (+1.5) e K alcaliniza levemente (+0.5).
- **1 sensor LDR** (fotorresistor) simula o **pH do solo**, mapeando a leitura analógica de 0–4095 para a escala real de pH 0.0–14.0, onde 7 representa o pH neutro.
- **1 sensor DHT22** simula a **umidade do solo** (adotado didaticamente no lugar de sensor agrícola específico, conforme orientação do enunciado).
- **1 módulo relé** representa a **bomba d'água** da lavoura.

A decisão de irrigação segue uma **árvore hierárquica de 5 níveis de prioridade**: (1) previsão de chuva ≥ 5mm nas próximas 6 horas suspende a irrigação; (2) se o solo já está úmido (≥50%), não irriga; (3) se o pH está fora da faixa ideal (5.5–7.0), não irriga; (4) se não há nutrientes presentes, não irriga; (5) caso todas as condições sejam adequadas e o solo esteja seco, a bomba é acionada com motivo "irrigando". As faixas operacionais foram definidas com base em recomendações da **Embrapa Milho e Sorgo**.

Como **Ir Além 1**, implementamos integração com a **API pública OpenWeather**: um script Python consulta a previsão de chuva para Sorriso/MT nas próximas 6 horas, converte os horários de UTC para GMT-3 (horário de Brasília) e exibe o volume total previsto em milímetros. Esse valor é copiado pelo usuário e colado no Monitor Serial do Wokwi, onde o ESP32 o captura via `Serial.available()` e `Serial.readStringUntil()`, ajustando automaticamente a lógica de irrigação para suspender o acionamento da bomba quando há previsão de chuva suficiente — economizando recursos hídricos e evitando encharcamento do solo.


## 🔌 Circuito no Wokwi

A imagem abaixo mostra o circuito completo montado na plataforma Wokwi, com todas as conexões entre o ESP32 e os sensores/atuadores:

<p align="center">
  <img src="assets/circuito_wokwi.png" alt="Circuito FarmTech no Wokwi" width="80%">
</p>

**Mapeamento de pinos:**

| Componente | Pino ESP32 | Função |
|---|---|---|
| DHT22 (SDA) | GPIO 32 | Sensor de umidade do solo |
| LDR (AO) | GPIO 15 | Sensor simulando pH do solo |
| Módulo Relé (IN) | GPIO 14 | Aciona a bomba d'água |
| Botão N (Nitrogênio) | GPIO 16 | Sensor de nutriente |
| Botão P (Fósforo) | GPIO 22 | Sensor de nutriente |
| Botão K (Potássio) | GPIO 25 | Sensor de nutriente |

**Alimentação:** todos os componentes são alimentados em 3.3V do ESP32, com GND compartilhado. Os botões utilizam `INPUT_PULLUP` interno, dispensando resistores externos.


## 🎥 Vídeo Demonstrativo

Assista à demonstração completa do projeto no YouTube (vídeo não listado):

🎬 **https://www.youtube.com/watch?v=v0hlTEeaBzs**


## 📁 Estrutura de pastas

Dentre os arquivos e pastas presentes na raiz do projeto, definem-se:

- <b>assets</b>: aqui estão os arquivos relacionados a elementos não-estruturados deste repositório, como imagens — incluindo a captura do circuito montado no Wokwi (`circuito_wokwi.png`) e o logo da FIAP.

- <b>src</b>: Todo o código fonte do projeto. Contém:
  - `farmtech_fase2.ino` — código C/C++ do ESP32 com a lógica completa de monitoramento e decisão de irrigação.
  - `diagram.json` — descrição do circuito montado no Wokwi (importável diretamente na plataforma).
  - `libraries.txt` — lista das bibliotecas Arduino utilizadas (DHT sensor library).
  - `wokwi-project.txt` — link direto para o projeto no Wokwi.
  - `openweather_chuva.py` — script Python que consulta a API OpenWeather e retorna a previsão de chuva para Sorriso/MT (parte do **Ir Além 1**).

- <b>README.md</b>: arquivo que serve como guia e explicação geral sobre o projeto (o mesmo que você está lendo agora).


## 🔧 Como executar o código

### Pré-requisitos

| Recurso | Versão | Finalidade |
|---|---|---|
| Conta no [Wokwi.com](https://wokwi.com) | — | Simulação do ESP32 |
| Biblioteca **DHT sensor library** (Adafruit) | 1.4.x+ | Leitura do DHT22 |
| Python | 3.8+ | Script da API OpenWeather |
| Biblioteca `requests` | qualquer | Requisições HTTP em Python |
| Chave da [OpenWeather API](https://openweathermap.org/api) | Gratuita | Previsão meteorológica |

### Passo 1 — Clonar o repositório

```bash
git clone https://github.com/dokitodavid/farmtech-solutions-fase2-cap1.git
cd farmtech-solutions-fase2-cap1
```

### Passo 2 — Executar a simulação no Wokwi

1. Acesse [wokwi.com](https://wokwi.com) e crie um novo projeto **ESP32**.
2. Cole o conteúdo de `src/diagram.json` na aba **diagram.json** do Wokwi.
3. Cole o conteúdo de `src/farmtech_fase2.ino` na aba **sketch.ino**.
4. No menu de bibliotecas do Wokwi, adicione **DHT sensor library** (Adafruit).
5. Clique em ▶ **Start Simulation**.
6. O Serial Monitor exibirá o cabeçalho com a cultura (milho), a região (Sorriso/MT) e as faixas operacionais.

### Passo 3 — Interagir com a simulação

| Ação | Como fazer |
|---|---|
| Ativar nutriente N, P ou K | Clicar e **segurar** o botão verde correspondente |
| Variar umidade do solo | Clicar no DHT22 e ajustar o slider de **humidity** |
| Variar pH | Clicar no LDR e ajustar o slider de **lux** |
| Simular chuva prevista | Digitar um valor no campo do Serial Monitor e pressionar Enter |

### Passo 4 — Executar o script Python (Ir Além 1)

```bash
cd src
pip install requests
```

Abra o arquivo `openweather_chuva.py` e substitua `sua_api_key_aqui` pela sua chave da OpenWeather API (obtenha gratuitamente em https://home.openweathermap.org/api_keys — a ativação leva até 2 horas após a criação).

Execute o script:

```bash
python openweather_chuva.py
```

Saída esperada:

```
FarmTech - Previsao de Chuva (Milho - Sorriso/MT)
Horarios em GMT-3 (Brasilia)
--------------------------------------------------
  17/04 00:00 | nublado              | chuva: 0.0mm
  17/04 03:00 | nublado              | chuva: 0.0mm
--------------------------------------------------
Chuva total prevista (6h): 0.0 mm
>>> Cole no Serial Monitor do Wokwi: 0.0
>>> ESP32 decide com base nos sensores
```

Copie o valor exibido (ex: `0.0`, `4.3`, `8.5`) e cole no campo do Serial Monitor do Wokwi, pressionando Enter. O ESP32 confirma a atualização e ajusta a lógica de irrigação em tempo real.

### Passo 5 — Validação da lógica de irrigação

Cenários sugeridos para teste:

| Umidade | pH Final | NPK | Chuva | Bomba | Motivo |
|---|---|---|---|---|---|
| 65% | 6.5 | [---] | 0mm | DESLIGADA | umidade ok |
| 30% | 3.0 | [---] | 0mm | DESLIGADA | pH fora da faixa |
| 30% | 6.5 | [---] | 0mm | DESLIGADA | sem nutrientes |
| 30% | 6.5 | [K--] | 0mm | **LIGADA** | irrigando |
| 30% | 6.5 | [K--] | 8.0mm | DESLIGADA | chuva prevista |


## 🗃 Histórico de lançamentos

* 1.0.0 - 20/04/2026
    * Entrega final da Fase 2: sistema de irrigação inteligente com ESP32, integração OpenWeather via Python, documentação completa e vídeo demonstrativo.

## 📋 Licença

<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"><p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/agodoi/template">MODELO GIT FIAP</a> por <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://fiap.com.br">Fiap</a> está licenciado sobre <a href="http://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">Attribution 4.0 International</a>.</p>
