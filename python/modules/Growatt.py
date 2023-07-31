def Monit_Growatt():

    import requests

    url = "https://oss.growatt.com/deviceManage/plantManage/list"

    dados = []

    for x in range(1,5):

        id_locais = []
        nome_cliente = []
        energia_dia = []

        payload = f"page={x}&=iCode%3D&=uOrP%3D&=city%3D&=designPower%3D&=totalPowerstar%3D&=totalPowerend%3D&=createPlantstatrime%3D&=createPlantendTime%3D&=deviceSN%3D&=status%3D&groupId=-1&plantType=-1&order=9"

        headers = {
            "authority": "oss.growatt.com",
            "accept": "application/json, text/javascript, */*; q=0.01",
            "accept-language": "pt-PT,pt;q=0.9,en-US;q=0.8,en;q=0.7",
            "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
            "cookie": "lang=en; adPic=true; JSESSIONID=7e75377a-8dcf-40cf-a256-5abc6a1cc1c9; assToken=9924f987dd6abffc2c55d3bcbfc98b40; uns=BAFLD001; pds=49cc005b1c024f819d216671ae07f2fe",
            "origin": "https://oss.growatt.com",
            "referer": "https://oss.growatt.com/index",
            "sec-ch-ua": "^\^Not/A",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "^\^Windows^^",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
            "x-requested-with": "XMLHttpRequest"
        }

        response = requests.request("POST", url, data=payload, headers=headers)
        r = response.json()

        num = r['obj']['pagers'][0]['datas']
        num = len(num)

        for i in range(0,num):

            locais = r['obj']['pagers'][0]['datas'][i]['uId']
            id_locais.append(locais)

            clientes = r['obj']['pagers'][0]['datas'][i]['plantNameEncryption']
            nome_cliente.append(clientes)

            energia = r['obj']['pagers'][0]['datas'][i]['eToday']
            energia_dia.append(energia)

            dados.append([id_locais[i], nome_cliente[i], energia_dia[i]])

    return dados
