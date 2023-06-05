
from contextlib import nullcontext


def Monit_SE():
    
    import solaredge as se
    
    #Definição da variável 's' a qual receberá a chave API (Fazer troca anual)
    s = se.Solaredge("ZL1EDZ2CA4DQZN3KBK1JK73KTRPH9OEX")

    #Criação da variável sites, que receberá uma listagem de todos os sites
    #Os parâmetros são: tamanho de 100 (já que temos 43 sites cadastrados),
    #começo em 0 e busca por sites ativos
    sites = s.get_list(size=100, start_index=0, status='Active')
    
    #Criação da variável locais. Aqui acontece o acesso de 'diretórios' do
    #dicionário 'sites'. O qual acessa primeiro a chave 'sites, depois 'site'
    #sendo que a informação da chave sites é alocada na variável 'locais'

    locais = (sites['sites']['site'])

    DadosCliente = [[None for x in range (1)] for y in range(len(locais))]

    #Matrix = [["" for x in range(3)] for y in range(len(locais))] 
 
    #Laço de repetição que irá buscar, por todo o dicionário 'locais', pelo
    #ID do site (id_locais), nome do cliente(nome_cliente) e a energia gerada
    #no dia(energia_dia). Todas as buscas são feitas pelo mesmo método de 
    #escalonamento que ocorreu na variável 'locais'

    for i in range(len(locais)):

        id_locais = (locais[i]['id']) #Busca do ID, usando da variável i para
                                        #percorrer todo o dicionário e alocando
                                        #a informação da chave 'id' na variável
                                        #id_locais

        nome_cliente = (locais[i]['name']) #Busca do Nome do Cliente, para 
                                            #implementação de um banco de dados.
                                            #Mesmo método da variável acima

        
        energia = s.get_overview(id_locais) #Criação da variável 'energia' a qual
                                                #recebe os dados vindos da função da API
                                                #SolarEdge 'get_overview', a qual depende
                                                #da variável 'id_locais' para retornar a
                                                #visão geral, referente a geração, do ID
                                                #inserido.

        energia_dia = (energia['overview']['lastDayData']['energy']) #Há o escalonamento, buscando
                                                                        #os dados de geração de energia
                                                                        #em um dia até o momento da captura
                                                                        #de dados.
        dados = {}

        dados = id_locais, nome_cliente, energia_dia #A inserção dos dados buscados acima. Utilizando do ID
                                                        #como chave do dicionário e informações da tupla sendo
                                                        #respectivamente o nome do cliente e energia gerada até 
                                                        #o momento da captura de dados.
                                                        #Sendo armazenda do seguinte modo:
                                                        # 2555300: ('1112_Melissa Villela', 1077.0)
        for j in range(len(locais)): 

            DadosCliente[i] = dados
        
    return DadosCliente
    

