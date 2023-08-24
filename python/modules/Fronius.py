import json
import time

def Monit_Fronius():

    import requests
    from fake_useragent import UserAgent
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.by import By
    from time import sleep
    from bs4 import BeautifulSoup as bs

    id_locais = []
    nome_cliente = []
    energia_dia = []

    USUARIO = 'contato@aztecenergia.com.br'
    SENHA = '@Zt3cenergia'

    url = "https://www.solarweb.com/PvSystems/Widgets"
    option = Options()
    option.add_argument('headless')
    driver = webdriver.Chrome(options=option)
    driver.get(url)

    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="username"]'))).send_keys(USUARIO)
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="password"]'))).send_keys(SENHA)
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="submitButton"]'))).click()

    source = driver.page_source

    soup = bs(source,'html.parser')
    clientes = soup.findAll('div', attrs={"class": "pvsystem-widget-title hidden-xs"})
    clientes = list(clientes)

    for i in range(0, len(clientes)):

        clientes_str = str(clientes[i])
        clientes_str = clientes_str.replace('<div class="pvsystem-widget-title hidden-xs">',"")
        clientes_str = clientes_str.replace('</div>',"")
        nome_cliente.append(clientes_str)

    nome_cliente = nome_cliente[0:-1]

    idclientes = soup.findAll('div', attrs={"class": "u-text-disabled"})
    idclientes = list(idclientes)

    for i in range(0, len(idclientes)):

        indexid = str(idclientes[i]).find("id")
        idclientes[i] = str(idclientes[i])[indexid:]
        indexquote = [
            index for index in range(len(idclientes[i]))
            if idclientes[i].startswith('"', index)
        ]
        idclientes[i] = str(idclientes[i])[:(indexquote[1]+1)]

        idclientes_str = str(idclientes[i])
        idclientes_str = idclientes_str.replace('id="',"")
        idclientes_str = idclientes_str.replace('"',"")

        id_locais.append(idclientes_str)

    if len(id_locais) <= 4:

        print("Redirecionado!")
        Monit_Fronius()

    id_locais = id_locais[0:-2]

    session = requests.Session()
    cookies_bot = driver.get_cookies()
    url_rq = "https://www.solarweb.com/ActualData/GetActualValues?withOnlineState=False&_=1692729298132"
    response = session.get(url_rq)
    cookies_rq = session.cookies.get_dict()


    f"""
    url = "https://www.solarweb.com/ActualData/GetActualValues?withOnlineState=False&_=1692729298132"

    payload = {}
    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'pt-PT,pt;q=0.9,en-US;q=0.8,en;q=0.7',
        'Connection': 'keep-alive',
        'Cookie': f'CookieConsent={'stamp':%27pBz40THSBAoHAK2jxLT8UFyP9jUenKzZaHm5t0xV7i2vbufAsHZDFg==%27%2Cnecessary:true%2Cpreferences:false%2Cstatistics:false%2Cmarketing:false%2Cmethod:%27explicit%27%2Cver:1%2Cutc:1691754991458%2Cregion:%27br%27}; 
                    {cookies_rq[]}OpenIdConnect.nonce.yY4Dpx3q1JSQx6BMmdRyZ%2FKHN3wQyktZGW%2FclsNEZh0%3D=eGprd3BnRnF6NjdqMUgwOEFObWZ2dllPS1dXemluTmJ5dTlUOGNIMXQ3cExCd0o0TF9JN3BFNHFSWG9DbEt0Z1pfemxpbzdRZmVNS2VHRWZYcldYRFJhUjg5bTdyOXo3ODFBVjFxTGgyQjFqUk11UWlQMEZGRVNXeHI3NnVaeGtQTnJmTEhSUTZGTmtsLTlLYXhXTFJjZllUUENmWmt6Z2N1azhqMThEWThMYXJPTXpTNGZ6ajQtazhvV0tkcXpKSWxRQ0xDRFhhU0UtREZmTDNRdXlmTU1SU2NF; 
                    .AspNet.Auth={cookies_bot[9]['.AspNet.Auth']}; 
                    TimeFormat=HH:mm; 
                    Culture=pt; 
                    lbc={cookies_bot[10]['lbc']}; 
                    DateFormat=DD/MM/YYYY; 
                    __RequestVerificationToken={cookies_bot[5]['__RequestVerificationToken']}; 
                    dtCookie={cookies_bot[3]['dtCookie']}; 
                    rxVisitor={cookies_bot[2]['rxVisitor']}; 
                    dtSa=-; 
                    rxvt={cookies_bot[4]['rxvt']}; 
                    dtPC={cookies_bot[0]['dtPC']}; 
                    lbc={cookies_rq[0]},

        'Referer': 'https://www.solarweb.com/PvSystems/Widgets',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    print(response)

    r = response.json()

    for i in range(0, len(r)):
        energia_dia.append(r[i]['TotalPower'])
        if r[i]['TotalPower'] == None:
            energia_dia.append('0.0')

    print(energia_dia)
    """

Monit_Fronius()
