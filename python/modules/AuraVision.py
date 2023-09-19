def Monit_AuraVision():

    id_locais = []
    nome_cliente = []
    energia_dia = []

    import requests

    url = "https://www.auroravision.net/asset/v1/portfolios/27246128/plants"

    querystring = {"includePerformanceProfiles":"true"}

    payload = ""
    headers = {
        "cookie": "token.auroravision.net=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6IkdKUHpPdUJxUm9MTXdLTm5UWmxaeXcifQ.eyJzdWIiOiJhenRlY2VuZXJnaWEiLCJpc3MiOiJhdXJvcmF2aXNpb24iLCJhdWQiOlsiYXYiXSwiZXhwIjoxNjkxNTEwMzU2LCJpYXQiOjE2OTE0NjcxNTYsImp0aSI6ImF2LTdjYjUwOWM0LWUyZGMtNDEyZi1hOTNjLTQ2ZGUzM2NkYjQ0YyIsImJybCI6WyJwYXJ0bmVyIiwidXNlcmFkbWluIiwicG9ydGFsYWRtaW4iLCJwZXJtYWRtaW4iLCJwYXJzZXJhZG1pbiIsImVkaXRpb25hZG1pbiIsImRhc2hib2FyZCIsImN1c3RvbWVyX2dyb3VwX2FkbWluIiwiY3VzdG9tZXItZ3JvdXAtYWRtaW4iLCJjdXN0b21lci1hZG1pbiJdLCJwcmwiOnsicG9ydGZvbGlvcyI6eyIyNzI0NjEyOCI6ImFkbWluaXN0cmF0b3IifX0sInBpZCI6WyIyNzI0NjEyOCJdLCJkcGciOiIyNzI0NjEyOCIsInNjaCI6ImF2LnYxIn0.VN9V3WZYFA7AzJFe0yyv4qfX0thxcC-INd7r5HA6vKCG_V_M28UHwOVQPesF6juyLwcUaAK4Y4Ms_gaaj-z6vnRazsLAUbotise3jpYQpMTjsgER-rHFk2xYyAvpX4ArH7ep-BWjOuke0daI6cwHYsYg4J0An5aEfh-cEC7Xw4EhZRclfWKA3ICqbQEWbUzHSdGojRxa2HW4uKaAl66KOhqocWM2tWH48-2qptb2SBDarIZW10sOl-MfATSwVxNyVztAmXBe_Q_k1BK-y-UCfpX7dVZig4N8vpSUuMiy8OhXevWor5Cb8PlZ4h8XOEW3gTwf9WsqpairymF2WuvbWA; _ga=GA1.1.631013839.1691467158; _ga_H3LHNEQX48=GS1.1.1691467158.1.0.1691467158.0.0.0; JSESSIONID=3C8F45D319D527B04CEA1FB2252D5C57",
        "authority": "www.auroravision.net",
        "accept": "application/json",
        "accept-language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7",
        "referer": "https://www.auroravision.net/home/",
        "sec-ch-ua": "^\^Not/A",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "^\^Windows^^",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
    }

    response = requests.request("GET", url, data=payload, headers=headers, params=querystring)
    r = response.json()

    num = len(r)

    for i in range(len(num)):

        locais = r[i]['entityID']
        id_locais.append(locais)

        clientes = r[i]['name']
        nome_cliente.append(clientes)

Monit_AuraVision()