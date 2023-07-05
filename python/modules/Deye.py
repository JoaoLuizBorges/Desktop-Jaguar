def Monit_Deye():

    import time
    from bs4 import BeautifulSoup as sp
    from selenium import webdriver
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support import expected_conditions as EC

    usuario = "AZTEC"
    senha = "@Zt3cenergia"

    global web

    from fake_useragent import UserAgent
    ua = UserAgent()
    user_agent = ua.random

    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    options.add_experimental_option("excludeSwitches",["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)

    options.add_argument(f'user-agent={user_agent}')
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--remote-debugging-port-9222")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-extensions")
    options.add_argument("--proxy-server='direct://'")
    options.add_argument("--proxy-bypass-list=*")
    options.add_argument("--start-maximized")
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--no-sandbox')
    options.add_argument('--ignore-certificate-errors')

    web = webdriver.Chrome(options=options)

    web.get("https://pro.solarmanpv.com/login")

    WebDriverWait(web,10).until(EC.element_to_be_clickable((By.XPATH,'//button[text()="Continue a usar o navegador atual"]'))).click()
    time.sleep(1)

    WebDriverWait(web,10).until(EC.element_to_be_clickable((By. XPATH, '//*[@id="app"]/div[3]/div[2]/div/div[3]/button[1]'))).click()

    time.sleep(3.5)

    elemento = web.find_element(By.XPATH, '//*[@id="areaList"]/div[1]/button[6]')
    web.execute_script('return arguments[0].scrollIntoView();', elemento)
    web.execute_script('arguments[0].click();', elemento)

    if web.find_element(By. CSS_SELECTOR, '#app > div.frame-login > div.loginHead.pl6x.pr6x.fsLv2.cb.vaM_E > div > div > div:nth-child(1) > div > div > div.toolBar.taR.bdSplitLine-top.vaM_E > button') == True:
        WebDriverWait(web,50).until(EC.element_to_be_clickable((By. CSS_SELECTOR, '#app > div.frame-login > div.loginHead.pl6x.pr6x.fsLv2.cb.vaM_E > div > div > div:nth-child(1) > div > div > div.toolBar.taR.bdSplitLine-top.vaM_E > button'))).click()

    time.sleep(6)

    WebDriverWait(web,50).until(EC.element_to_be_clickable((By. XPATH, '//*[@id="app"]/div[3]/div[5]/div/div/div[1]/div/div/div[3]/button'))).click()
    time.sleep(2.5)

    WebDriverWait(web,50).until(EC.element_to_be_clickable((By. XPATH, '//*[@id="app"]/div[3]/div[6]/section/div[2]/div[2]/div[1]/div/div[3]/span'))).click()
    print("Login")
    time.sleep(3)

    WebDriverWait(web,50).until(EC.element_to_be_clickable((By. XPATH, '//*[@id="app"]/div[3]/div[6]/section/div[2]/div[2]/div[2]/div/input'))).send_keys(usuario)
    WebDriverWait(web,50).until(EC.element_to_be_clickable((By. XPATH, '//*[@id="app"]/div[3]/div[6]/section/div[2]/div[2]/div[3]/input'))).send_keys(senha)
    time.sleep(4)

    WebDriverWait(web,50).until(EC.element_to_be_clickable((By. XPATH, '//*[@id="app"]/div[3]/div[6]/section/div[2]/div[2]/button'))).click()
    time.sleep(12)

    print("No monitoramento")

    pageSource = web.page_source

    pg_html = sp(pageSource,'html.parser')
    print(pg_html.text)

    count = 0
    i = 0
    dadosMonit = []
    nome_cliente = []

    for dados in pg_html.find_all("div",attrs={"class": "textCut"}):
        dadosMonit.append(dados['title'])

    for i in dadosMonit:
        if count % 2 == 0:
            nome_cliente.append(i)
        count += 1

    print(nome_cliente)

    with open("pg_html.txt","w", encoding='utf-8') as g:
        g.write(pageSource)

Monit_Deye()

