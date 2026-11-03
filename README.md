# DBC Converter

**Conversor de arquivos DBC do DATASUS para CSV.**

Uma ferramenta simples e portátil desenvolvida em Python para facilitar a conversão de arquivos `.DBC` utilizados nas bases de dados do DATASUS para o formato `.CSV`.

O objetivo é tornar esse processo mais rápido e acessível, permitindo converter múltiplos arquivos simultaneamente, sem a necessidade de utilizar ferramentas complexas ou realizar procedimentos manuais.

## Funcionalidades

- Conversão de arquivos DBC para CSV.
- Processamento de múltiplos arquivos em lote.
- Identificação automática dos arquivos na pasta de entrada.
- Preservação dos nomes originais dos arquivos.
- Exportação compatível com Microsoft Excel.
- Tratamento individual de erros, sem interromper todo o processamento.
- Execução portátil no Windows, sem necessidade de instalar Python (versão executável).

## Como utilizar

### Opção 1 — Executável Windows

1. Acesse a seção [Releases](../../releases) deste repositório.
2. Baixe o arquivo `converter.exe`.
3. Coloque o executável em uma pasta de sua preferência.
4. Crie uma pasta chamada `entrada`.
5. Insira os arquivos `.DBC` que deseja converter.
6. Execute `converter.exe`.

Os arquivos convertidos serão disponibilizados automaticamente na pasta `saida`.

### Estrutura de diretórios

```text
DBC-Converter/
│
├── converter.exe
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

As pastas `entrada` e `saida` são criadas automaticamente caso não existam.

### Opção 2 — Executar pelo Python

Para executar o projeto pelo código-fonte, é necessário ter Python instalado.

Clone o repositório:

```bash
git clone https://github.com/AlanSPa/conversordbcDataSus.git
```

Entre na pasta:

```bash
cd conversordbcDataSus
```

Instale as dependências:

```bash
pip install pyreaddbc dbfread pandas
```

Execute:

```bash
python converter.py
```

Coloque os arquivos DBC na pasta `entrada` antes de iniciar a conversão.

## Formato de exportação

Os arquivos são exportados com as seguintes configurações:

| Propriedade | Configuração |
|---|---|
| Formato | CSV |
| Delimitador | Ponto e vírgula (`;`) |
| Codificação | UTF-8 com BOM |
| Índice | Não exportado |
| Nome do arquivo | Preservado |

O formato UTF-8 com BOM facilita a abertura dos arquivos no Microsoft Excel.

## Tecnologias utilizadas

- [Python](https://www.python.org/)
- [Pandas](https://pandas.pydata.org/)
- [pyreaddbc](https://github.com/AlertaDengue/pyreaddbc)
- [dbfread](https://github.com/olemb/dbfread)
- [PyInstaller](https://pyinstaller.org/)

## Objetivo do projeto

O DBC Converter nasceu da necessidade de simplificar a conversão de arquivos utilizados nas bases públicas de dados do DATASUS.

A proposta é oferecer uma alternativa leve, prática e acessível para profissionais, pesquisadores e estudantes que trabalham com dados de saúde pública.
