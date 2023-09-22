def Monit_REFUsol():

    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.chrome.service import Service
    from webdriver_manager.chrome import ChromeDriverManager
    from fake_useragent import UserAgent
    from bs4 import BeautifulSoup
    import requests
    import time

    #Configurações do Chrome
    chrome_options = webdriver.ChromeOptions()
    ua = UserAgent()
    user_agent = ua.random

    chrome_options.add_argument('--headless')
    chrome_options.add_argument(f'--user-agent={user_agent}')
    #chrome_options.add_experimental_option("detach",True)
    chrome_driver = ChromeDriverManager().install()
    driver = webdriver.Chrome(options=chrome_options, service=Service(chrome_driver))
    driver.maximize_window()

    #Acesso Fronius
    print('Acesso')
    driver.get('https://refu-log.com/Dashboard.aspx')
    email = 'aztecenergia'
    senha = '@Zt3cenergia'
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="ctl00_headerControl_loginControl_txtUsername"]').send_keys(email)
    time.sleep(2)
    print('Senha')
    driver.find_element(By.XPATH, '//*[@id="ctl00_headerControl_loginControl_txtPassword"]').send_keys(senha)
    time.sleep(3)
    print('Clica Login')
    driver.find_element(By.XPATH, '//*[@id="ctl00_headerControl_loginControl_btnLogin"]').click() #OLÁ JOÃO
    time.sleep(3)

    response = requests.get(driver.current_url)
    rp = response.text

    soup = BeautifulSoup(rp,'html.parser')

    with open('source.txt','w',encoding='utf-8') as src:
        src.write(str(soup))