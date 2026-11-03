# DBC Converter

**Conversor de arquivos DBC do DATASUS para CSV.**

O DBC Converter é uma ferramenta desenvolvida em Python para facilitar a conversão de arquivos `.DBC`, utilizados nas bases de dados do DATASUS, para o formato `.CSV`.

A proposta é simplificar esse processo por meio de uma solução leve, automatizada e de fácil utilização, permitindo converter múltiplos arquivos simultaneamente.

## Funcionalidades

- Conversão de arquivos DBC para CSV.
- Processamento de múltiplos arquivos em lote.
- Identificação automática dos arquivos na pasta de entrada.
- Preservação dos nomes originais dos arquivos.
- Exportação compatível com Microsoft Excel.
- Tratamento individual de erros, sem interromper todo o processamento.
- Criação automática das pastas de entrada e saída.

## Estrutura do projeto

```text
conversordbcDataSus/
│
├── converter.py
│
├── entrada/
│   ├── ERPE2601.dbc
│   ├── ERPE2602.dbc
│   └── ERPE2603.dbc
│
└── saida/
    ├── ERPE2601.csv
    ├── ERPE2602.csv
    └── ERPE2603.csv
```

As pastas `entrada` e `saida` são criadas automaticamente pelo programa caso não existam.

## Requisitos

- Python 3.9 ou superior.
- Bibliotecas:
  - pyreaddbc
  - dbfread
  - pandas

## Instalação

Clone o repositório:

```bash
git clone https://github.com/AlanSPa/conversordbcDataSus.git
```

Acesse a pasta do projeto:

```bash
cd conversordbcDataSus
```

Instale todas as dependências necessárias utilizando o arquivo `requirements.txt`:

```bash
pip install -r requirements.txt
```

**Nota:** O arquivo `requirements.txt` contém a lista de bibliotecas necessárias para executar o projeto. Não é necessário instalar cada dependência individualmente.

## Como utilizar

1. Coloque os arquivos `.DBC` na pasta `entrada`.
2. Execute o script:

```bash
python converter.py
```

3. Aguarde o processamento.
4. Acesse a pasta `saida` para encontrar os arquivos CSV convertidos.

Não é necessário informar os nomes dos arquivos ou alterar o código. Todos os arquivos DBC encontrados na pasta de entrada serão processados automaticamente.

## Formato de exportação

Os arquivos CSV são gerados com as seguintes configurações:

| Propriedade | Configuração |
|---|---|
| Formato | CSV |
| Delimitador | Ponto e vírgula (`;`) |
| Codificação | UTF-8 com BOM |
| Índice | Não exportado |
| Nome do arquivo | Preservado |

A codificação UTF-8 com BOM facilita a abertura dos arquivos no Microsoft Excel.

## Tecnologias utilizadas

- [Python](https://www.python.org/)
- [Pandas](https://pandas.pydata.org/)
- [pyreaddbc](https://github.com/AlertaDengue/pyreaddbc)
- [dbfread](https://github.com/olemb/dbfread)

## Objetivo do projeto

O DBC Converter surgiu da necessidade de simplificar a conversão de arquivos utilizados nas bases públicas de dados do DATASUS.

A ferramenta busca oferecer uma alternativa simples e automatizada para profissionais, pesquisadores e estudantes que trabalham com dados de saúde pública.
