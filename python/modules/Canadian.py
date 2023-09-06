def Monit_Canadian():

    import requests

    id_locais = []
    nome_cliente = []
    energia_dia = []
    dados = []

    url = "https://monitoring.csisolar.com/maintain-s/operating/station/search"

    querystring = {"page":"1","size":"20","order.direction":"ASC","order.property":"name"}

    payload = {
        "region": {
            "nationId": None,
            "level1": None,
            "level2": None,
            "level3": None,
            "level4": None,
            "level5": None
        },
        "externalRelationship": {},
        "powerTypeList": ["PV"]
    }
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "pt-PT,pt;q=0.9,en-US;q=0.8,en;q=0.7",
        "Authorization": "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX25hbWUiOiI5MDFfY29udGF0b0BhenRlY2VuZXJnaWEuY29tLmJyXzIiLCJzY29wZSI6WyJhbGwiXSwiZGV0YWlsIjp7Im9yZ2FuaXphdGlvbklkIjo5MDEsInRvcEdyb3VwSWQiOjkwNywiZ3JvdXBJZCI6OTA3LCJyb2xlSWQiOjEsInVzZXJJZCI6NDI3NCwidmVyc2lvbiI6MTAwMCwiaWRlbnRpZmllciI6ImNvbnRhdG9AYXp0ZWNlbmVyZ2lhLmNvbS5iciIsImlkZW50aXR5VHlwZSI6MiwibWRjIjoiQ0hJTkEiLCJhcHBJZCI6bnVsbH0sImV4cCI6MTY5NTk5MTc3MCwibWRjIjoiQ0hJTkEiLCJhdXRob3JpdGllcyI6WyJhbGwiXSwianRpIjoiZGFhZDc5M2ItYzlhMi00NWVjLTgzMGYtZmNlNjc1NmJhYWNkIiwiY2xpZW50X2lkIjoidGVzdCJ9.QS1p58-OLU4q1KqlG6Cmm7yuAnyLW4iKvGO2KKDgctjAWNgaCKLg_FOyhJYBFBpxa2lPcq0hx53GRyMtbe5WA8P0EQqwPAN_phaBz4Mff5IT-gYaTh0ma_iM8uLmWoEdv3hsmsGzUjsemMPg9uyaOUT6msOg0pRhXqh0Sln_zrmkIpYzK1VrA-B6YWGmeuh-2rT_eIP6BI0qhl4Hh5I9afy-gV_QuJTg5JmcaBDXwGGoEcm3Er28_4kQvpjs10WaD_E5YXk9xEJhY64LXDu1arxqJNCGi6Osimk2eNrfKW89kJ2UHHN0loeIgO-nt8nRXFXRLbEzXCFDWhd9gQRl4w",
        "Connection": "keep-alive",
        "Content-Type": "application/json;charset=UTF-8",
        "Cookie": "language=pt; acw_tc=a3b5429c16908074476792608ea5404465164643fb4e22d609f8f14a46; Hm_lvt_c326fd3753cda4380e25b0d74b36592e=1690807449; firstPrivacy=true; accountFirstUse=eMail; tokenKey=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX25hbWUiOiI5MDFfY29udGF0b0BhenRlY2VuZXJnaWEuY29tLmJyXzIiLCJzY29wZSI6WyJhbGwiXSwiZGV0YWlsIjp7Im9yZ2FuaXphdGlvbklkIjo5MDEsInRvcEdyb3VwSWQiOjkwNywiZ3JvdXBJZCI6OTA3LCJyb2xlSWQiOjEsInVzZXJJZCI6NDI3NCwidmVyc2lvbiI6MTAwMCwiaWRlbnRpZmllciI6ImNvbnRhdG9AYXp0ZWNlbmVyZ2lhLmNvbS5iciIsImlkZW50aXR5VHlwZSI6MiwibWRjIjoiQ0hJTkEiLCJhcHBJZCI6bnVsbH0sImV4cCI6MTY5NTk5MTc3MCwibWRjIjoiQ0hJTkEiLCJhdXRob3JpdGllcyI6WyJhbGwiXSwianRpIjoiZGFhZDc5M2ItYzlhMi00NWVjLTgzMGYtZmNlNjc1NmJhYWNkIiwiY2xpZW50X2lkIjoidGVzdCJ9.QS1p58-OLU4q1KqlG6Cmm7yuAnyLW4iKvGO2KKDgctjAWNgaCKLg_FOyhJYBFBpxa2lPcq0hx53GRyMtbe5WA8P0EQqwPAN_phaBz4Mff5IT-gYaTh0ma_iM8uLmWoEdv3hsmsGzUjsemMPg9uyaOUT6msOg0pRhXqh0Sln_zrmkIpYzK1VrA-B6YWGmeuh-2rT_eIP6BI0qhl4Hh5I9afy-gV_QuJTg5JmcaBDXwGGoEcm3Er28_4kQvpjs10WaD_E5YXk9xEJhY64LXDu1arxqJNCGi6Osimk2eNrfKW89kJ2UHHN0loeIgO-nt8nRXFXRLbEzXCFDWhd9gQRl4w; refreshTokenKey=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX25hbWUiOiI5MDFfY29udGF0b0BhenRlY2VuZXJnaWEuY29tLmJyXzIiLCJzY29wZSI6WyJhbGwiXSwiYXRpIjoiZGFhZDc5M2ItYzlhMi00NWVjLTgzMGYtZmNlNjc1NmJhYWNkIiwiZGV0YWlsIjp7Im9yZ2FuaXphdGlvbklkIjo5MDEsInRvcEdyb3VwSWQiOjkwNywiZ3JvdXBJZCI6OTA3LCJyb2xlSWQiOjEsInVzZXJJZCI6NDI3NCwidmVyc2lvbiI6MTAwMCwiaWRlbnRpZmllciI6ImNvbnRhdG9AYXp0ZWNlbmVyZ2lhLmNvbS5iciIsImlkZW50aXR5VHlwZSI6MiwibWRjIjoiQ0hJTkEiLCJhcHBJZCI6bnVsbH0sImV4cCI6MTY5NTk5MTc3MCwibWRjIjoiQ0hJTkEiLCJhdXRob3JpdGllcyI6WyJhbGwiXSwianRpIjoiNGIxMzkzNDQtYTk0NS00NjkwLTgxY2ItOTQyZGYyMTZmNDc5IiwiY2xpZW50X2lkIjoidGVzdCJ9.NHxw55amWAp5K_WmziJiqaH49C4e4sSNFlMTXpnzLZY-9hLkksyMF4YGboqpo1b4tVpEfzDaAmB6eyVsT71Q-3b02GjNq9M4u1hOTHMQvpXmrYYmw6O8zgbhgWD6aJZFbcDHBkB-oOIe9Z5CTV2GnOHGnHozb2SkrtthxKql5DJztiokkkTMieul_meyhnYa6OuBP6Q3zZr78_eNa9PpVMCmsKFnWIKp19PhjAC8gzgFER2ClEyibaecoau81_gwV-BaQZtu1bC38styoUzYxt8xUSQ6id_1s2vs4NvWXiFwwD_WdzWmwlP77YbYeRJP3chhy7gtnPNMir8k8_-UQw; Hm_lpvt_c326fd3753cda4380e25b0d74b36592e=1690809145",
        "Origin": "https://monitoring.csisolar.com",
        "Referer": "https://monitoring.csisolar.com/maintain/plant",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
        "sec-ch-ua": "^\^Not/A",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "^\^Windows^^"
    }

    response = requests.request("POST", url, json=payload, headers=headers, params=querystring)
    r = response.json()

    num = r['data']
    num = len(num)

    for i in range(0,num):

        locais = r['data'][i]['id']
        id_locais.append(locais)

        clientes = r['data'][i]['name']
        nome_cliente.append(clientes)

        energia = r['data'][i]['generationValue']
        energia_dia.append(energia)

        dados.append([id_locais[i], nome_cliente[i], energia_dia[i]])

    return dados

Monit_Canadian()
