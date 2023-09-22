def Monit_Deye():

    import requests

    url = "https://pro.solarmanpv.com/mdc-eu/maintain-s/operating/station/v2/search"

    querystring = {"page": "1", "size": "165", "order.direction": "ASC", "order.property": "name"}

    payload = {
        "station": {
            "powerTypeList": ["PV"]
        }
    }

    headers = {
        "accept": "application/json, text/plain, */*",
        "accept-language": "pt-PT,pt;q=0.9,en-US;q=0.8,en;q=0.7",
        "authorization": "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX25hbWUiOiI0NTAxNF9BWlRFQ18zIiwic2NvcGUiOlsiYWxsIl0sImRldGFpbCI6eyJvcmdhbml6YXRpb25JZCI6NDUwMTQsInRvcEdyb3VwSWQiOjM0MTEyLCJncm91cElkIjozNDExMiwicm9sZUlkIjoxLCJ1c2VySWQiOjQzNjM2NywidmVyc2lvbiI6MTAwMCwiaWRlbnRpZmllciI6IkFaVEVDIiwiaWRlbnRpdHlUeXBlIjozLCJtZGMiOiJGT1JFSUdOXzEiLCJhcHBJZCI6bnVsbH0sImV4cCI6MTY5NTcyNTMwNCwibWRjIjoiRk9SRUlHTl8xIiwiYXV0aG9yaXRpZXMiOlsiYWxsIl0sImp0aSI6IjJkMmY3NWZjLWJhYzQtNDUzNy05NzFmLTc3ZjQ5MjdjNGZmOCIsImNsaWVudF9pZCI6InRlc3QifQ.Ey1-VEs0elluXqoqcj_P97eMC9cr90H-X9dDJTjA9iAl0_m3vZhQ9-PGf-pTau7RWw5Hct8jXfMJBzrd4lbTa9K_gjxzpdKrov0PuCKHf49RHvLk_3ddf2MnvlQMPI-8qM0LOljEOcxCQoDpJR3NU9H2VBPbsmFu75YTq6nqprFW7G0JqaDULP0jJSiTCz4s_Ksrinw2rlDGLEeb95rb_Tg5q-QWprDWrukFwvJN8YD1S-XUF3E7rfunmRKS_k4qvrCnp4CJH-4hLFT7RprjNRwORqufHTdcH9ssrGLXkWhFg49nwWGPq7iOEFS4_ElTJ9sq7srMd4i9kz7jD8ulrQ",
        "cookie": "language=pt; firstPrivacy=true; affixPath=/business/maintain/plant; accountFirstUse=username; guide_nav=1; guide_headBtn=1;",
        "origin": "https://pro.solarmanpv.com",
        "referer": "https://pro.solarmanpv.com/business/maintain/plant",
        "sec-ch-ua": '"Not A;Brand";v="99", "Chromium";v="115"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
    }

    response = requests.post(url, json=payload, headers=headers, params=querystring)
    r = response.json()

    id_locais = []
    nome_cliente = []
    energia_dia = []
    dados = []

    for i in range(0, 161):

        locais = r['data'][i]['station']['id']
        id_locais.append(locais)

        clientes = r['data'][i]['station']['name']
        nome_cliente.append(clientes)

        energia = r['data'][i]['station']['generationPower']
        energia_dia.append(energia)

        dados.append([id_locais[i], nome_cliente[i], energia_dia[i]])

    return dados
