# 🦸 Análise Exploratória de Dados dos Vingadores da Marvel

## 📖 Sobre o Projeto

Este projeto tem como objetivo realizar uma Análise Exploratória de Dados (EDA - Exploratory Data Analysis) utilizando um conjunto de dados contendo informações sobre personagens dos Vingadores da Marvel.

Ao longo do projeto, foram aplicadas técnicas de limpeza, transformação, visualização e interpretação de dados para responder perguntas relevantes sobre os personagens, como:

* Qual a distribuição de gênero dos Vingadores?
* Como o número de aparições evoluiu ao longo do tempo?
* Existe relação entre gênero e mortalidade?
* Personagens com mais aparições tendem a morrer mais?
* Qual a taxa de retorno dos personagens após eventos de morte?

O projeto foi desenvolvido em Python utilizando bibliotecas amplamente utilizadas no mercado de Dados.

Fonte: https://github.com/fivethirtyeight/data/tree/master/avengers

---

## 🎯 Objetivos

Este projeto foi criado com o propósito de praticar e demonstrar competências essenciais para um Analista de Dados, incluindo:

* Limpeza e preparação de dados;
* Tratamento de valores ausentes;
* Criação de novas variáveis;
* Análise estatística descritiva;
* Visualização de dados;
* Geração de insights;
* Comunicação de resultados.

---

## 🛠️ Tecnologias Utilizadas

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Jupyter Notebook

---

## 📂 Base de Dados

O conjunto de dados contém informações sobre membros dos Vingadores da Marvel, incluindo:

* Nome do personagem
* Gênero
* Número de aparições
* Ano de entrada nos Vingadores
* Status honorário
* Registro de mortes
* Registro de retornos após morte

A base foi utilizada para explorar padrões históricos e comportamentais dos personagens ao longo do tempo.

---

## 🔍 Etapas da Análise

### 1. Importação e Conhecimento dos Dados

Inicialmente foi realizada a leitura do conjunto de dados e uma análise da estrutura das variáveis, tipos de dados e quantidade de registros.

---

### 2. Tratamento dos Dados

Durante esta etapa foram realizadas ações importantes para garantir a qualidade da análise:

* Preenchimento de valores ausentes;
* Conversão de variáveis categóricas para formato numérico;
* Remoção de colunas com elevado percentual de valores nulos;
* Validação da consistência dos dados.

---

### 3. Análise da Distribuição de Gênero

Foi realizada uma análise da representatividade de personagens masculinos e femininos na equipe dos Vingadores.

**Insight encontrado:**
A maior parte dos personagens da base pertence ao gênero masculino.

---

### 4. Análise das Aparições

Utilizando histogramas e medidas descritivas, foi investigada a distribuição do número de aparições dos personagens.

**Insight encontrado:**
A maioria dos heróis possui relativamente poucas aparições, enquanto um pequeno grupo concentra grande visibilidade.

---

### 5. Relação entre Gênero e Aparições

Foi utilizado um gráfico Boxplot para avaliar possíveis diferenças na quantidade de aparições entre os gêneros.

**Insight encontrado:**
Personagens masculinos apresentam, em média, maior número de aparições.

---

### 6. Evolução dos Vingadores ao Longo dos Anos

Foi analisada a quantidade de novos personagens incorporados à equipe ao longo das décadas.

**Insight encontrado:**
Observa-se crescimento gradual da equipe ao longo do tempo, com oscilações em determinados períodos.

---

### 7. Distribuição de Gênero por Década

A análise permitiu observar como a participação feminina evoluiu ao longo da história dos Vingadores.

**Insight encontrado:**
Embora o número de personagens femininas tenha crescido, a predominância masculina permanece evidente.

---

### 8. Personagens Honorários

Foi investigada a proporção de personagens honorários por gênero.

**Insight encontrado:**
A distribuição apresenta diferenças interessantes que podem indicar padrões de representação dentro da equipe.

---

### 9. Mortalidade e Retorno dos Personagens

Uma das análises mais interessantes do projeto foi avaliar:

* Quantos personagens morreram;
* Diferenças entre gêneros;
* Taxa de retorno após morte.

**Insights encontrados:**

* O gênero masculino apresentou maior número absoluto de mortes.
* Proporcionalmente, a taxa de mortalidade também foi superior.
* Personagens femininas apresentaram maior percentual de retorno após eventos de morte.

---

### 10. Análise por Quartis de Aparições

Foi criada uma variável baseada em quartis para segmentar os personagens conforme seu número de aparições.

**Insight encontrado:**
Personagens mais populares tendem a apresentar maior incidência de eventos de morte, possivelmente devido à sua relevância nas narrativas.

---

### 11. Cruzamento entre Aparições, Gênero e Mortalidade

Foi construída uma visualização do tipo Heatmap para analisar simultaneamente:

* Gênero;
* Ocorrência de morte;
* Média de aparições.

**Insight encontrado:**
Os personagens masculinos que sofreram eventos de morte possuem, em média, o maior número de aparições da base.

---

## 🌎 Aplicação no Mundo Real

Embora o conjunto de dados seja baseado em personagens fictícios, as técnicas utilizadas neste projeto são amplamente aplicadas em cenários corporativos reais.

### Exemplos de aplicações:

#### Marketing

Analisar quais clientes mais engajados possuem maior probabilidade de cancelar um serviço.

#### Recursos Humanos

Identificar padrões de rotatividade de colaboradores de acordo com perfil, tempo de empresa e área de atuação.

#### Varejo

Avaliar quais produtos possuem maior risco de descontinuação com base em histórico de vendas.

#### Saúde

Investigar fatores associados ao retorno de pacientes após determinado tratamento.

---

## 📊 Competências Demonstradas

Este projeto evidencia conhecimentos em:

✅ Limpeza de dados

✅ Tratamento de valores ausentes

✅ Análise exploratória de dados (EDA)

✅ Estatística descritiva

✅ Engenharia de atributos

✅ Visualização de dados

✅ Storytelling com dados

✅ Interpretação de resultados

✅ Comunicação de insights

---

## 🚀 Como Executar o Projeto

### Clone o repositório

```bash
git clone https://github.com/hccruz/Projeto_Avengres
```

### Instale as dependências

```bash
pip install pandas numpy matplotlib seaborn jupyter
```

### Execute o Notebook

```bash
jupyter notebook
```

Abra o arquivo:

```bash
main.ipynb
```

---

## 👨‍💻 Sobre Mim

Sou profissional da área de Dados com experiência em Python, SQL, Excel e automação de processos.

Este projeto demonstra minha capacidade de transformar dados brutos em informações relevantes para apoiar a tomada de decisão, aplicando boas práticas de análise exploratória, visualização e interpretação de dados.

Estou em constante evolução na área de Análise e Ciência de Dados, buscando desenvolver soluções que gerem valor para o negócio através dos dados.
