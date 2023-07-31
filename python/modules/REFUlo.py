import datetime
import requests
data_agora = datetime.datetime.now()


def Monit_REFUsol():
    mes = data_agora.month
    hoje = data_agora.day

    id_locais = []
    nome_cliente = []
    energia_dia = []
    dados = []

    url = "https://refu-log.com/Ajax/RenderMapScript.aspx/GetGoogleMapMarkers"

    payload = {
        "publicMap": False,
        "accountId": 2673,
        "isMapAdmin": False,
        "selectedIconsType": 0
    }

    headers = {
        "authority": "refu-log.com",
        "accept": "application/json, text/javascript, */*; q=0.01",
        "accept-language": "pt-PT,pt;q=0.9,en-US;q=0.8,en;q=0.7",
        "content-type": "application/json; charset=UTF-8",
        "cookie": ".ASPXANONYMOUS=f2qJQkj62QEkAAAAMzg2MjQwNWYtZjkyZC00MjEzLWFkNjMtNjZhZmY3MDUyZWEzdpsuVggutLTMp4LcmcZh51LAemqR9XRKOnYJJ2HPFKw1; ASP.NET_SessionId=rkf0fopkdql4lf0g00igbvi1; TZD2=180; _gid=GA1.2.1462010285.1690811626; _gat_gtag_UA_75619506_2=1; PL=pt-PT; .ASPXAUTH62503=FBE3096409F5CAF246C9565CF51E9F8817C5C59C6A9F4C4AA73AB4651C6E22A6C04EF95A10A2A33BCCED696A38E6963C5FC9314DD08AE72D6F80BA63B0EC53D0976363BEF8BA4A5732F3166E95A86F0235A11FEFDC8DEC6C9AAFB70A45E917B6A8F5E2820D586090F0844B73F2D9AA7A095345D97D0DCA930227CE08499AC4A737DD7A88DD83604C3A5461D0ACDF95F00C5A805D7A7AEB6EE89692D04B7AE722F7420E5CAB86482716A53D210D285431; gvPlantsCompact_Conf=version6.90.04^%^7csort1^%^7ca1^%^7cconditions12^%^7c0^%^7c3^%^7c1^%^7c3^%^7c2^%^7c3^%^7c3^%^7c3^%^7c4^%^7c3^%^7c5^%^7c3^%^7c6^%^7c3^%^7c7^%^7c3^%^7c8^%^7c3^%^7c9^%^7c3^%^7c10^%^7c5^%^7c11^%^7c5^%^7cvisible12^%^7cf0^%^7ct1^%^7ct2^%^7ct3^%^7ct4^%^7ct5^%^7ct6^%^7ct7^%^7ct8^%^7cf9^%^7cf10^%^7ct11; .ASPROLES=_mTKQx9g232j3m3rqlzH6n_4Ff1H31pn8k4zI9rNPseLIqzSsC3p0N5I8kOuVaWXjbUlCHUlq6_puKSKBka6Mgtb3bvTyMtTUBkz6hzAawPWEBSdluRi3dHL_tTrxuncm-FvHWBczUui3WIQdhEQYmW4iYZdHR3GJI8BBbATCxlrl9WNd56ayEBCGkkNBF-VgvReg6ymQDrZcFmbrlzDKYyou9AQTqB9K2F-xOAd8Gtjdvus7fGUYUHRMOsnZkFbdbSva90iJswg8UYmmDOONGFVJji_3Qz3bsBUiDfP1ut1iT6gwC1xqfWDZgZGwjZwhHDhTxGQJoe7Z7OXpGicNoF9kIVLZTzr1IzDlo_CmLvg-W5KjQt-0ath8vu5knNba5zXSycfEKgwoxiw9pIMA0yRNc2nsLWsurRzy-T9RgJJ6IBM2ABlO6dTztGEyZW79HCHlZ8d9zFosGezhwK_ldQ8BkBfwdPo_pKLwrfZ9romsOltleRSRbOSYpbshMeEPaBnDXgaEeP2ZTWwaB8kuOoROn6p7mPw-xf4hHsltjE2Ln5ghRAaFrh5X_mhBJbT0; _ga=GA1.2.1976250177.1690811626; _ga_79BVEB39LD=GS1.1.1690811625.1.1.1690811656.0.0.0",
        "origin": "https://refu-log.com",
        "referer": "https://refu-log.com/Dashboard.aspx",
        "sec-ch-ua": "^\^Not/A",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "^\^Windows^^",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
        "x-requested-with": "XMLHttpRequest"
    }

    response = requests.request("POST", url, json=payload, headers=headers)
    r = response.json()

    num = r['d']
    num = len(num)

    for i in range(0, num):
        locais = r['d'][i]['PlantID']
        id_locais.append(locais)

        clientes = r['d'][i]['PlantName']
        nome_cliente.append(clientes)

        energia = busca_geracao(locais, clientes, mes, hoje)
        energia_dia.append(energia)

        dados.append([id_locais[i], nome_cliente[i], energia_dia[i]])

    return dados


def busca_geracao(locais,clientes,mes,hoje):
    url = "https://refu-log.com/Ajax/StatisticsWebService.aspx/GetDataForChannels"

    payload = {
        "channels": [
            {
                "ChannelId": 1,
                "ChartData": [],
                "ChartInterval": 0,
                "Color": "DE2922",
                "ConfigurationId": 0,
                "DataType": 4,
                "DataTypeName": "Potência CA",
                "IsPlantDataAccessibleBasedOnLicense": True,
                "MeasureUnit": 0,
                "MeasureUnitCode": "W",
                "ParentSolarObjects": None,
                "SolarObject": {
                    "Firmware": None,
                    "Id": None,
                    "Name": None,
                    "Type": 0
                },
                "Visible": True
            }
        ],
        "year": 2023,
        "month": None,
        "day": None
    }

    payload['channels'][0]['SolarObject']['Id'] = locais
    payload['channels'][0]['SolarObject']['Name'] = clientes
    payload['month'] = mes
    payload['day'] = hoje

    headers = {
        f"authority": "refu-log.com",
        "accept": "application/json, text/javascript, */*; q=0.01",
        "accept-language": "pt-PT,pt;q=0.9,en-US;q=0.8,en;q=0.7",
        "content-type": "application/json; charset=UTF-8",
        "cookie": ".ASPXANONYMOUS=f2qJQkj62QEkAAAAMzg2MjQwNWYtZjkyZC00MjEzLWFkNjMtNjZhZmY3MDUyZWEzdpsuVggutLTMp4LcmcZh51LAemqR9XRKOnYJJ2HPFKw1; ASP.NET_SessionId=rkf0fopkdql4lf0g00igbvi1; TZD2=180; _gid=GA1.2.1462010285.1690811626; PL=pt-PT; .ASPXAUTH62503=FBE3096409F5CAF246C9565CF51E9F8817C5C59C6A9F4C4AA73AB4651C6E22A6C04EF95A10A2A33BCCED696A38E6963C5FC9314DD08AE72D6F80BA63B0EC53D0976363BEF8BA4A5732F3166E95A86F0235A11FEFDC8DEC6C9AAFB70A45E917B6A8F5E2820D586090F0844B73F2D9AA7A095345D97D0DCA930227CE08499AC4A737DD7A88DD83604C3A5461D0ACDF95F00C5A805D7A7AEB6EE89692D04B7AE722F7420E5CAB86482716A53D210D285431; gvPlantsCompact_Conf=version6.90.04%7csort1%7ca1%7cconditions12%7c0%7c3%7c1%7c3%7c2%7c3%7c3%7c3%7c4%7c3%7c5%7c3%7c6%7c3%7c7%7c3%7c8%7c3%7c9%7c3%7c10%7c5%7c11%7c5%7cvisible12%7cf0%7ct1%7ct2%7ct3%7ct4%7ct5%7ct6%7ct7%7ct8%7cf9%7cf10%7ct11; gvErrors_Conf=version6.90.04%7csort1%7cd0%7cvisible11%7ct0%7cf2%7ct1%7ct3%7cf4%7ct5%7cf6%7ct9%7ct20%7cf-1%7cf-1; jstree_open=%23node0_87543; jstree_load=; .ASPROLES=5v4gLgj1irbD9wCjgyI0D5EZFvjOVXh1MpWelGXXPotFj81SIdhciMvAQYbNv3TxPD140_Zu4mjbn2Nb16MDm96NikDdpMG_Ku3ry6FxxHYO0ji7TKzwwFmBQVXY4xpC6KdSJIRVu-D78oBu6M8pNXy1hve8tK_h4Z6XjnLJEuFhc0cyuG8vy2dg9EBZ8EImxOuSQQ8rgu_aCbANYixMvJDMgBVlckg_aEzVeGmzcxwL8_hzW9cs37N554XX70IF6FesjDVzqN_MEEcFivqszA5lXHR4aQyaLw11mrfEYd7Ylv8Dw9ULfXzZi0z2gSbwYij3KBvVLgcshOUZQZsTTBonrMSlC6g_I9MYwh0Xgb20kWIc3cCu_bECFWvUuuLHQiAh2gJe7Mp4PgBXRc-VMfL-d9jmgmPlBFZFrp9RA4R3w7iBh3xVgNnefrEuHiwRYeaazcUGodjEtwH5_K56ZOJ-t795CB7wMw3Tbgw75C_i8nJytak_SFTH3yWsekXYspX1LxrHHA4dxzOzb8mEcNDQRiVfomvWpHIaV8FOxdg1; _ga_79BVEB39LD=GS1.1.1690811625.1.1.1690814185.0.0.0; _ga=GA1.2.1976250177.1690811626; _gat_gtag_UA_75619506_2=1",
        "origin": "https://refu-log.com",
        "referer": f"https://refu-log.com/PlantDetails.aspx?id={locais}",
        "sec-ch-ua": '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "Windows",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
        "x-requested-with": "XMLHttpRequest"
    }

    response = requests.request("POST", url, json=payload, headers=headers)
    r = response.json()

    tam = r['d'][0]['ChartData']
    tam = len(tam)
    if not r['d'][0]['ChartData']:
        return 0
    else:
        tam = tam - 1
        return r['d'][0]['ChartData'][tam]['Value']['Value1']

