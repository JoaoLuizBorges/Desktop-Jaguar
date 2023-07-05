def main():
    from modules import Solaredge
    import json

    DadosClienteSolaredge = (Solaredge.Monit_SE())

    InfoCliente = {
        "Id": [],
        "Nome_Cliente": [],
        "Energia_Dia": []
    }

    for i in range(len(DadosClienteSolaredge)):
        InfoCliente["Id"].append(DadosClienteSolaredge[i][0])
        InfoCliente["Nome_Cliente"].append(DadosClienteSolaredge[i][1])
        InfoCliente["Energia_Dia"].append(DadosClienteSolaredge[i][2])

    DadosGeracao = json.dumps(InfoCliente)

    with open("InfoCliente.json", "w", encoding='utf8') as outfile:
        json.dump(DadosGeracao, outfile, ensure_ascii=False, indent=4)


if __name__ == '__main__':
    main()
