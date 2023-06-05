
import sys
sys.path.append("C:/Users/joaob/Desktop/Desenvolvimento/AppJaguar/src/Modules")

def main():
    from Modules import Solaredge
    import json
    
    DadosCliente = (Solaredge.Monit_SE())

    print(DadosCliente)

    InfoCliente = {
        "Id":[],
        "Nome_Cliente": [],
        "Energia_Dia": []
    }

    for i in range(len(DadosCliente)):

        InfoCliente['Id'].append(DadosCliente[i][0])
        InfoCliente['Nome_Cliente'].append(DadosCliente[i][1])
        InfoCliente['Energia_Dia'].append(DadosCliente[i][2])
    
    DadosGeracao = json.dumps(InfoCliente)
    
    with open("InfoCliente.json","w") as outfile:
        json.dump(DadosGeracao, outfile)

if __name__ ==  '__main__':
    main()