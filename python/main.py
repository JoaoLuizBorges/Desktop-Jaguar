def main():

    from modules import Solaredge
    from modules import Deye
    from modules import Growatt
    from modules import Hoymilles
    from modules import Canadian
    from modules import REFUlo
    from modules import AuraVision

    import json

    DadosClienteSolaredge = (Solaredge.Monit_SE())
    DadosClienteSolarman = (Deye.Monit_Deye())
    DadosClientesGrowatt = (Growatt.Monit_Growatt())
    DadosClientesHoymilles = (Hoymilles.Monit_Hoymilles())
    DadosClientesCanadian = (Canadian.Monit_Canadian())
    DadosClientesREFUsol = (REFUlo.Monit_REFUsol())
    DadosClientesAuraVision = (AuraVision.Monit_AuraVision())

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

    for i in range(len(DadosClientesHoymilles)):
        InfoCliente["Id"].append(DadosClientesHoymilles[i][0])
        InfoCliente["Nome_Cliente"].append(DadosClientesHoymilles[i][1])
        InfoCliente["Energia_Dia"].append(DadosClientesHoymilles[i][2])

    for i in range(len(DadosClientesCanadian)):
        InfoCliente["Id"].append(DadosClientesCanadian[i][0])
        InfoCliente["Nome_Cliente"].append(DadosClientesCanadian[i][1])
        InfoCliente["Energia_Dia"].append(DadosClientesCanadian[i][2])

    for i in range(len(DadosClientesREFUsol)):
        InfoCliente["Id"].append(DadosClientesREFUsol[i][0])
        InfoCliente["Nome_Cliente"].append(DadosClientesREFUsol[i][1])
        InfoCliente["Energia_Dia"].append(DadosClientesREFUsol[i][2])

    for i in range(len(DadosClientesAuraVision)):
        InfoCliente["Id"].append(DadosClientesAuraVision[i][0])
        InfoCliente["Nome_Cliente"].append(DadosClientesAuraVision[i][1])

    DadosGeracao = json.dumps(InfoCliente)

    with open("InfoCliente.json", "w", encoding='utf8') as outfile:
        json.dump(DadosGeracao, outfile, ensure_ascii=False, indent=4)


if __name__ == '__main__':
    main()
