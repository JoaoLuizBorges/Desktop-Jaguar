def Monit_Hoymilles():

    import requests

    id_locais = []
    nome_cliente = []
    energia_dia = []
    dados = []

    url = "https://global.hoymiles.com/platform/api/gateway/pvm/station_select_by_page"

    payload = {
        "body": {
            "name": "",
            "page": 1,
            "page_size": 10,
            "real_data": 1
        },
        "WAITING_PROMISE": True
    }

    headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "pt-PT,pt;q=0.9,en-US;q=0.8,en;q=0.7",
        "Connection": "keep-alive",
        "Content-Type": "application/json;charset=UTF-8",
        "Cookie": "hm_token_language=en_us; _ga=GA1.1.1669309742.1690803129; hm_token=1.1mxXlzZTnFnEwqyBHuAC0SLTD5a5KMYUBqsE3rj6dd1BGmTfIkIh5tVIlnTEbW2HqsjzHIbxyJBac2oUmGWTbMY8Ol8R; _ga_JRG1385S8G=GS1.1.1690803128.1.1.1690803346.0.0.0",
        "Origin": "https://global.hoymiles.com",
        "Referer": "https://global.hoymiles.com/platform/station/view",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
        "sec-ch-ua": "^\^Not/A",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "^\^Windows^^"
    }

    response = requests.request("POST", url, json=payload, headers=headers)
    r = response.json()

    num = r['data']['list']
    num = len(num)

    for i in range(0,num):

        locais = r['data']['list'][i]['id']
        id_locais.append(locais)

        clientes = r['data']['list'][i]['name']
        nome_cliente.append(clientes)

        energia = r['data']['list'][i]['real_data']['today_eq']
        energia_dia.append(energia)

        dados.append([id_locais[i], nome_cliente[i], energia_dia[i]])

    return dados

