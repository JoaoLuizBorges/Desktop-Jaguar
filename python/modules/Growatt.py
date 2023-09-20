def Monit_Growatt():

    import requests
    import json

    id_locais = []
    nome_cliente = []
    energia_dia = []
    dados = []

    url = "https://oss.growatt.com/common/bigScreen/getShowPage_plantList"

    payload = "name=BAFLD001&pwd=143b59b81bbf504d68c2981be1bfc590&page=1&date=2023-09-20&plantType=0%2C1"
    headers = {
        'authority': 'oss.growatt.com',
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'pt-PT,pt;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'cookie': '_ga=GA1.1.558478574.1693220055; _ga_XJ71771Q0R=GS1.1.1693220054.1.1.1693220274.17.0.0; JSESSIONID=c5f62472-70e7-4c07-ba6d-7b127f7f96f8; lang=en; assToken=deca87dfeaae53976fc4d09dc120fa2a; adPic=null; bigName=BAFLD001; bigPwd=143b59b81bbf504d68c2981be1bfc590; SERVERID=1ea79574e391be8474f6c80563d620a3|1695209204|1695207576; SERVERID=1ea79574e391be8474f6c80563d620a3|1695209480|1695207576',
        'origin': 'https://oss.growatt.com',
        'referer': 'https://oss.growatt.com/deviceManage/bigScreenPage/plant',
        'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    r = response.text
    resp = json.loads(r)
    SIZE = len(resp['obj']['datas'][0])

    for i in range(0, SIZE):

        id_locais.append(resp['obj']['datas'][i]['plant_id'])

        nome_cliente.append(resp['obj']['datas'][i]['plantName'])

        energia_dia.append(resp['obj']['datas'][i]['etoday'])

        dados.append([id_locais[i], nome_cliente[i], energia_dia[i]])

    return dados

