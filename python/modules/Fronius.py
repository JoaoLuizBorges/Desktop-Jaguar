def Monit_Fronius():

    import requests
    from bs4 import BeautifulSoup
    from fake_useragent import UserAgent

    id_locais = []
    nome_cliente = []
    energia_dia = []

    url = "https://www.solarweb.com/PvSystems/Widgets"

    ua = UserAgent()
    user_agent = ua.random

    payload = ""


    #response = requests.request("GET", url, data=payload, headers=headers)

    session = requests.Session()
    response = session.get(url)
    cookies = (session.cookies.get_dict())
    print(cookies.items)

    cookiesclone = list(cookies)
    headers = {
        "cookie": "lbc=!ve2M76ovFhonkDaZp5E8pnbpsb0kb6W1ODiIuJi8U4ulH9umftjhza9o7IGbX3ibiREbT5Hf%2FPw4e2D4MzpVYcIJyS%2BW5u%2F57BgreWgHfDg%3D",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Accept-Language": "pt-PT,pt;q=0.9,en-US;q=0.8,en;q=0.7",
        "Cache-Control": "max-age=0",
        "Connection": "keep-alive",
        "Cookie": f"lbc=^{cookies['lbc']}; Culture={cookies['Culture']}; {cookiesclone[2]} = {cookies[{cookiesclone[2]}]}",
        #"Cookie": "lbc=^!OiOdMqZJiuuRhQGZp5E8pnbpsb0kb30jzAYDvaSM6J0YmOFwCxIcZpgmS+PIRjG6FOXqIko7QlBeo1Q0JXLTSVmb37Y/SDxfBL23nDWwfag=; __RequestVerificationToken=mOs4KV9NIQA21IZVtT4zx7SPlRH0A3vYKhNntI_6_bYC4BnzVCi_B1O60Edm7CCuH02yyuhOxKtJG6gZbxkxZUwetjw1; CookieConsent=^{stamp:^%^27pBz40THSBAoHAK2jxLT8UFyP9jUenKzZaHm5t0xV7i2vbufAsHZDFg==^%^27^%^2Cnecessary:true^%^2Cpreferences:false^%^2Cstatistics:false^%^2Cmarketing:false^%^2Cmethod:^%^27explicit^%^27^%^2Cver:1^%^2Cutc:1691754991458^%^2Cregion:^%^27br^%^27^}; rxVisitor=1691754986609RPQTFCHMPU4EKQDU9VVVMIPPP1U14299; TimeFormat=HH:mm; Culture=pt; DateFormat=DD/MM/YYYY; dtCookie=v_4_srv_-2D30_sn_T0PJF828SPLUHLSCV77QJGPTEOFV1C6P; dtSa=-; .AspNet.Auth=DGZXmwjLQ9Y4I37KR-45b4qrZ2MW57uJO4VpDJJdi5infnDQ_qWB17XXVzKnt7m9DXVke0iEgntWNA8y1aozN5PeZwqVW9n3SLvmWAzPMA4r2f3vP64gW3s3B2jsJg_zCcFECzQ_Yp0xS-FPDk0bBkLoVg-jlyo1HgHEtCO-lsipPeojLand-Mqb_UWCrrg42_xQnlISMoVn8LcxZashP6AW2dyj-30U0QQ4cTEtlIiGYxFxdB_Kqc5D50ABHNU3JXiAnj210zo7vrgL3Q13uRISrYZue539NtfQ5wgEMEd3CNp9UIA6PWT6YUleMmHAQjSbXGVpz1-kT4Bd-W67Mze8FpRZ-Q_GXKAki3ciGNk3xL6bDfrSdlZxi4ufu_FxFkJMTVsXEMo6Chdc9Rm3pJmfWtQf1Q9UQIe9eSF2MIXxPrXXLzpJ83AmrE7R3iQgqK7k0BHFUnaRyZKSEgUQOZ4AOZmx_EOTPa91LnWG_KU3qJGxJsvw02b72xDOn7ArwkoBvg; rxvt=1691779832831^|1691778031816; dtPC=-30^-vAKKVHULUCMLJEOUPRMCAWTLLQDHGEOAR-0e0",
        "Referer": "https://www.google.com/",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "cross-site",
        "Sec-Fetch-User": "?1",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": f"{user_agent}",
        "sec-ch-ua": "^\^Not/A",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "^\^Windows^^"
    }

    soup = BeautifulSoup(str(response),'html.parser')

    clientes = soup.findAll('div', attrs={"class": "pvsystem-widget-title hidden-xs"})
    clientes = list(clientes)
   
    for i in range(0, len(clientes)):

        clientes_str = str(clientes[i])
        clientes_str.replace('<div class="pvsystem-widget-title hidden-xs">','')
        clientes_str.replace('</div>','')
        nome_cliente.append(clientes_str)

    #print(nome_cliente)

    if not clientes:
        Monit_Fronius()


Monit_Fronius()
