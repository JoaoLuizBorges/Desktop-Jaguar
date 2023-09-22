def Monit_Hoymilles():

    import requests
    import json

    id_locais = []
    nome_cliente = []
    energia_dia = []
    dados = []

    url = "https://global.hoymiles.com/platform/api/gateway/pvm/station_select_by_page"

    payload = "{\"body\":{\"name\":\"\",\"page\":1,\"page_size\":10,\"real_data\":1},\"WAITING_PROMISE\":true}"
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'pt-PT,pt;q=0.9,en-US;q=0.8,en;q=0.7',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json;charset=UTF-8',
        'Cookie': 'hm_token_language=en_us; _ga=GA1.1.1137844556.1695133645; hm_token=1.1Dr9nSxM4YSjClNZ5dazvPqm5w22AWAvwJiTc5UfzFX1TkkMPv6HxkpAN0HG7JfkCpamBDlTQXwWpbjbN9Ge9bO0jJmu; _ga_JRG1385S8G=GS1.1.1695133645.1.1.1695133903.0.0.0',
        'Origin': 'https://global.hoymiles.com',
        'Referer': 'https://global.hoymiles.com/platform/station/view',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    r = response.text
    resp = json.loads(r)
    SIZE = resp['data']['total']

    for i in range(0, SIZE):
        id_locais.append(resp['data']['list'][i]['id'])

        nome_cliente.append(resp['data']['list'][i]['name'])

        ger = (resp['data']['list'][i]['real_data']['real_power'])
        ger = format(float(ger), ".2f")
        energia_dia.append(str(ger))

        dados.append([id_locais[i], nome_cliente[i], energia_dia[i]])

    return dados




