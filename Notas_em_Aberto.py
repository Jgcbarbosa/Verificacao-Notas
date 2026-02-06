import pandas as pd
import pyodbc as db
from dotenv import load_dotenv
from os import getenv


#Conectando ao banco de dados
load_dotenv()
conexao = db.connect(getenv("Conexao_SQL"))


def notas_abertas():
    #Consultando notas fiscais em aberto no ERP com SQL
    Notas_Pendentes = """
    Select 
	    nf.cgcfil as FILIAL,
	    f.nomfor as FORNECEDOR,
        nf.numnfc as NOTA_FISCAL,
        f.codfor as COD_FOR,
        nf.datemi as DATA_EMISSAO
    from NotasFiscais as nf
    left join Fornecedores as f
    on nf.cgcfor = f.cgccpf
    where nf.datemi >= '2025-11-01' and nf.stanfv <> 3
    order by DATA_EMISSAO
    """

    #Retornando dados da query, transformando em Excel e transformando os dados para melhor visualização.
    dados = pd.read_sql(con=conexao, sql=Notas_Pendentes)
    dados["COD_FOR"] = dados["COD_FOR"].astype('Int64')
    pd.set_option("display.max_rows", None)

    print(f"\nQuantidade total de notas fiscais em aberto: {len(dados)}")
    EM1_ES = dados.loc[dados["FILIAL"] == 12345678000101].drop(columns=["FILIAL"])
    EM1_RJ = dados.loc[dados["FILIAL"] == 12345678000102].drop(columns=["FILIAL"])
    EM1_SP = dados.loc[dados["FILIAL"] == 12345678000103].drop(columns=["FILIAL"])
    EM1_MG = dados.loc[dados["FILIAL"] == 12345678000104].drop(columns=["FILIAL"])
    EM1_PR = dados.loc[dados["FILIAL"] == 12345678000105].drop(columns=["FILIAL"])
    EM1_RN = dados.loc[dados["FILIAL"] == 12345678000106].drop(columns=["FILIAL"])
    EM2_M = dados.loc[dados["FILIAL"] == 98765432000101].drop(columns=["FILIAL"])
    EM2_F = dados.loc[dados["FILIAL"] == 98765432000102].drop(columns=["FILIAL"])
    print(f"Tem {len(EM1_ES) + len(EM1_RJ) + len(EM1_SP) + len(EM1_MG) + len(EM1_PR) + len(EM1_RN)} nota(s) em aberto na Empresa 1 e {len(EM2_M) + len(EM2_F)} nota(s) em aberto na Empresa 2!")

    Filiais = {
        "ES": ("Empresa 1 Espírito Santo", EM1_ES),
        "RJ": ("Empresa 1 Rio de Janeiro", EM1_RJ),
        "SP": ("Empresa 1 São Paulo", EM1_SP),
        "MG": ("Empresa 1 Minas Gerais", EM1_MG),
        "PR": ("Empresa 1 Paraná", EM1_PR),
        "RN": ("Empresa 1 Rio Grande do Norte", EM1_RN),
        "MAT": ("Empresa 2 Matriz", EM2_M),
        "FIL": ("Empresa 2 Filial", EM2_F) 
    }

    while True:
        print("\n---Filiais Disponíveis---")
        for chave, (filial, lista) in Filiais.items():
            print(f"{chave} - {filial} -> {len(lista)} nota(s)")

        try:
            escolha = input("\nEscolha uma filial para verificar as notas fiscais ou digite sair:").upper()
            if escolha in Filiais:
                nome, notas = Filiais[escolha]
                print(f"\nNotas em aberto da {nome}: \n{notas}\n")
                while True:
                    continuar = input("Deseja verificar outra filial? (s/n): ").lower()
                    if continuar in ("s", "sim"):
                        break
                    elif continuar in ("n", "nao", "não"):
                        print("Saindo do sistema.")
                        exit()
                    else:
                        print("\nComando inválido. Digite sim ou não.")
            elif escolha == "SAIR":
                print("Saindo do sistema.")
                exit()
            else:
                print("\nOpção inválida, escolha uma das opções abaixo.")
        except ValueError:
            print("Por favor, digite uma opção válida.")