
import pyreaddbc
import pandas as pd

from dbfread import DBF
from pathlib import Path

# Diretório do projeto
BASE_DIR = Path(__file__).resolve().parent

# Pastas de entrada e saída
PASTA_ENTRADA = BASE_DIR / "entrada"
PASTA_SAIDA = BASE_DIR / "saida"


# Localiza arquivos DBC, inclusive em subpastas
arquivos_dbc = list(PASTA_ENTRADA.rglob("*.dbc"))

if not arquivos_dbc:
    print("Nenhum arquivo DBC encontrado.")
else:
    print(f"\nEncontrados {len(arquivos_dbc)} arquivo(s).\n")

    sucessos = 0
    erros = 0

    for arquivo in arquivos_dbc:

        print(f"Processando: {arquivo.name}")

        try:
            # Mantém a estrutura das subpastas na saída
            pasta_relativa = arquivo.parent.relative_to(PASTA_ENTRADA)
            pasta_destino = PASTA_SAIDA / pasta_relativa
            pasta_destino.mkdir(parents=True, exist_ok=True)

            # Arquivos temporários e finais
            arquivo_dbf = pasta_destino / f"{arquivo.stem}.dbf"
            arquivo_csv = pasta_destino / f"{arquivo.stem}.csv"

            # Etapa 1: Descompacta DBC para DBF
            pyreaddbc.dbc2dbf(
                str(arquivo),
                str(arquivo_dbf)
            )

            if not arquivo_dbf.exists():
                raise RuntimeError("Não foi possível gerar o arquivo DBF.")

            # Etapa 2: Lê o DBF
            tabela = DBF(
                str(arquivo_dbf),
                encoding="iso-8859-1"
            )

            df = pd.DataFrame(iter(tabela))

            # Etapa 3: Exporta para CSV
            df.to_csv(
                arquivo_csv,
                sep=";",
                index=False,
                encoding="utf-8-sig"
            )

            # Remove o DBF temporário
            arquivo_dbf.unlink()

            print(f"  CONCLUÍDO: {arquivo_csv.name}")
            print(f"  Registros: {len(df)}")
            print(f"  Colunas: {len(df.columns)}\n")

            sucessos += 1

        except Exception as e:
            print(f"  ERRO: {e}\n")
            erros += 1

    print("=" * 45)
    print("PROCESSAMENTO FINALIZADO")
    print("=" * 45)
    print(f"Convertidos: {sucessos}")
    print(f"Com erro: {erros}")
    print(f"Total: {len(arquivos_dbc)}")
    print(f"Saída: {PASTA_SAIDA}")
