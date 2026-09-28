import json

with open ("clientes.txt","r", encoding="utf-8") as arquivo:
    cli = {}

    for linha in arquivo:
        dados = linha.split(",")

        codigo = dados[0]
        nome = dados[1]
        compras = [float(dados[2]), float(dados[3])]

        cli[codigo] = {
            "nome": nome,
            "compras": compras
        }

    x = json.dumps(cli, indent=4)
    print(x)