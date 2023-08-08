def Monit_Ecosolys():

    import requests

    url = "https://portal.ecosolys.com.br:8843/api-v1/planta"
    headers = {"Host": "portal.ecosolys.com.br"}

    # Desativa a verificação do certificado SSL (NÃO RECOMENDADO em produção)
    response = requests.get(url, headers=headers, verify=False)

    print("Status Code:", response.status_code)
    print("Response Content:", response.text)

Monit_Ecosolys()