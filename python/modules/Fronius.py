import json
import time


def oauth_sign_in():

    import requests
    from fake_useragent import UserAgent
    from bs4 import BeautifulSoup

    ua = UserAgent()

    urlreqper = """https://login.fronius.com/authenticationendpoint/login.do
                 ?response_type=code+id_token
                 &client_id=mf_o9iTAyKemNLQTa6Sp6HYonCIa
                 &redirect_uri=https://www.solarweb.com/Account/ExternalLoginCallback
                 &scope=openid+profile+solarweb+solweb_browserid_93c65d8e866a6421e43a4e3d7b75f200
                 &state=OpenIdConnect.AuthenticationProperties%3DSPSH41wrDFDgyxgKCi4uNrJKW6rEysC2Y95dwaVLU79CyNs6_3TVAyWQDqAU3mHCxlEiJ7_M8PoXSe-v5FSgUGCblK6spEz0ZKn0HZSrHImyWK2a6YQFfhuopr-Gq6ZC1j8Ouh5zmr5BCcV27GCQ-btfUs2BuMFOQNaFldAfUlC9Ayc8UHDuNmB2y84PJzNr3cISBO9q9m7TWQ-MIeJwLgQ9QhI_ndGUeN0oBjZ3IFioUx8pkztVaWWe-R8gMClvgQvO1AEze-TqqC7uFnS3FhewfU0
                """
    session = requests.Session()
    session.headers.update({'User-Agent': f'{ua}'})

    response = session.get(urlreqper)
    resposta = response.content.decode()
    r = json.dumps(resposta)
    soup = BeautifulSoup(r,'html.parser')
    print(soup.prettify())

def Monit_Fronius():
    import requests
    auth = 'mf_o9iTAyKemNLQTa6Sp6HYonCIa'

    payload = {
        'redirect_uri': 'https://www.solarweb.com/Account/ExternalLoginCallback'
    }
    URL = 'https://login.fronius.com/authenticationendpoint/login.do?client_id=mf_o9iTAyKemNLQTa6Sp6HYonCIa&commonAuthCallerPath=%2Foauth2%2Fauthorize&forceAuth=false&nonce=638285913968124533.ZGQxM2UyYzgtYTY0Yi00MjcwLTk2NTQtMzEwMjExNmE3NmNmOWNhMzFhNWMtOTMzZC00NGIyLThjOWMtMDI5NzY5YjdlYWEx&passiveAuth=false&redirect_uri=https%3A%2F%2Fwww.solarweb.com%2FAccount%2FExternalLoginCallback&response_mode=form_post&response_type=code+id_token&scope=openid+profile+solarweb+solweb_browserid_93c65d8e866a6421e43a4e3d7b75f200&state=OpenIdConnect.AuthenticationProperties%3DSPSH41wrDFDgyxgKCi4uNrJKW6rEysC2Y95dwaVLU79CyNs6_3TVAyWQDqAU3mHCxlEiJ7_M8PoXSe-v5FSgUGCblK6spEz0ZKn0HZSrHImyWK2a6YQFfhuopr-Gq6ZC1j8Ouh5zmr5BCcV27GCQ-btfUs2BuMFOQNaFldAfUlC9Ayc8UHDuNmB2y84PJzNr3cISBO9q9m7TWQ-MIeJwLgQ9QhI_ndGUeN0oBjZ3IFioUx8pkztVaWWe-R8gMClvgQvO1AEze-TqqC7uFnS3FhewfU0&tenantDomain=carbon.super&x-client-SKU=ID_NET461&x-client-ver=6.9.0.0&sessionDataKey=b39d6f44-98de-472c-a5e3-27d10b83b611&relyingParty=mf_o9iTAyKemNLQTa6Sp6HYonCIa&type=oidc&sp=Solar.web+-+Portals&isSaaSApp=false&authenticators=SAMLSSOAuthenticator:Fronius%20Login;CustomAuthenticatorLocalMain:LOCAL:LOCAL'

    response_post = requests.post(URL, data=payload, auth=auth)
    resposta = response_post.json()
    print(resposta)


oauth_sign_in()
