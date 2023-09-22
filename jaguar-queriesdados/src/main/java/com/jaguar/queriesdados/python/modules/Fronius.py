import time
def exec_bot():

    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.chrome.service import Service
    from webdriver_manager.chrome import ChromeDriverManager
    from fake_useragent import UserAgent
    from bs4 import BeautifulSoup
    import requests

    #Configurações do Chrome
    chrome_options = webdriver.ChromeOptions()
    ua = UserAgent()
    user_agent = ua.random

    chrome_options.add_argument('--headless')
    chrome_options.add_argument(f'--user-agent={user_agent}')
    chrome_driver = ChromeDriverManager().install()
    driver = webdriver.Chrome(options=chrome_options, service=Service(chrome_driver))
    driver.maximize_window()

    #Acesso Fronius
    print('Acesso')
    driver.get('https://www.solarweb.com/')
    email = 'contato@aztecenergia.com.br'
    senha = '@Zt3cenergia'
    time.sleep(2)
    print('Aceito Cookies')
    driver.find_element(By.XPATH, '//*[@id="CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll"]').click()
    time.sleep(3)
    print('Clica Login')
    driver.find_element(By.XPATH, '//*[@id="navigation"]/ul[2]/li[1]/a/span').click()
    time.sleep(1.3)
    print('Usuário')
    driver.find_element(By.XPATH, '//*[@id="username"]').send_keys(email)
    time.sleep(2)
    print('Senha')
    driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(senha)
    time.sleep(3)
    print('Clica Login')
    driver.find_element(By.XPATH, '//*[@id="submitButton"]').click() #OLÁ JOÃO
    time.sleep(3)

    response = requests.get(driver.current_url)
    r = response.text

    soup = BeautifulSoup(r,'html.parser')
    print(soup)

exec_bot()