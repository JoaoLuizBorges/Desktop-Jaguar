def main():

    from modules import Solaredge
    from modules import Deye
    from modules import Growatt
    from modules import Hoymilles
    from modules import Canadian

    import json

    DadosClienteSolaredge = (Solaredge.Monit_SE())
    DadosClienteSolarman = (Deye.Monit_Deye())
    DadosClientesGrowatt = (Growatt.Monit_Growatt())
    DadosClientesCanadian = (Canadian.Monit_Canadian())

    InfoCliente = {
        "Id": [],
        "Nome_Cliente": [],
        "Energia_Dia": []
    }

    for i in range(len(DadosClientesGrowatt)):
        InfoCliente["Id"].append(DadosClientesGrowatt[i][0])
        InfoCliente["Nome_Cliente"].append(DadosClientesGrowatt[i][1])
        InfoCliente["Energia_Dia"].append(DadosClientesGrowatt[i][2])

    for i in range(len(DadosClienteSolaredge)):
        InfoCliente["Id"].append(DadosClienteSolaredge[i][0])
        InfoCliente["Nome_Cliente"].append(DadosClienteSolaredge[i][1])
        InfoCliente["Energia_Dia"].append(DadosClienteSolaredge[i][2])

    for i in range(len(DadosClienteSolarman)):
        InfoCliente["Id"].append(DadosClienteSolarman[i][0])
        InfoCliente["Nome_Cliente"].append(DadosClienteSolarman[i][1])
        InfoCliente["Energia_Dia"].append(DadosClienteSolarman[i][2])

    for i in range(len(DadosClientesCanadian)):
        InfoCliente["Id"].append(DadosClientesCanadian[i][0])
        InfoCliente["Nome_Cliente"].append(DadosClientesCanadian[i][1])
        InfoCliente["Energia_Dia"].append(DadosClientesCanadian[i][2])

    DadosGeracao = json.dumps(InfoCliente)

    with open("InfoCliente.json", "w", encoding='utf8') as outfile:
        json.dump(DadosGeracao, outfile, ensure_ascii=False, indent=4)


if __name__ == '__main__':
    main()
