# Análise de Dados de Seguro de Saúde

Este projeto realiza uma análise abrangente dos dados de seguro de saúde com o objetivo de extrair insights significativos para entender melhor os clientes e otimizar a estratégia de preços. 

## Objetivos

1. **Análise Exploratória de Dados (EDA)**
   - Visualizar a distribuição das variáveis no conjunto de dados.
   - Identificar correlações entre as variáveis.
   - Explorar características como idade, sexo, IMC, número de filhos, fumante e região, e como elas afetam os encargos do seguro.

2. **Teste de Hipótese Estatística**
   - Testar se há diferenças significativas nos encargos do seguro entre fumantes e não fumantes.
   - Verificar se há uma diferença significativa nos encargos do seguro entre homens e mulheres.

3. **Modelagem Estatística**
   - Desenvolver um modelo de regressão linear para prever os encargos do seguro com base nos atributos dos segurados.
   - Avaliar a qualidade do modelo e sua capacidade de generalização.

## Estrutura do Repositório

- `src/`: Código fonte para processamento de dados, análise exploratória, testes de hipótese e modelagem.
- `dataset/`: Conjunto de dados utilizado no projeto.
- `results/`: Resultados da análise, incluindo visualizações, testes estatísticos e avaliação do modelo.
- `notebooks/`: Notebooks Jupyter com a análise completa.

## Requisitos

Instale as dependências necessárias com o comando:

```bash
pip install -r requirements.txt
