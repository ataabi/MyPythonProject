from selenium import webdriver

def animes(pagina):
    driverpath = input('Diretorio do WebDriver.')
    eps = input('Número de episodios a serem baixados.')
    driver = webdriver.Chrome(driverpath)
    driver.get(pagina)
    def episodio(driver) :
        episodio = driver.find_element_by_xpath('/html/body/div[5]/div/div[1]/p')
        episodio = episodio.text
        episodio = episodio.replace('Voçê esta baixando - ', '')
        return episodio


    def downloadlink(driver) :
        # Procura o link de download
        download = driver.find_element_by_xpath('//*[@id="conteudo404"]/div/a')
        download = download.get_attribute('href')
        return download


    def proximoep(driver,episodio) :
        cap_atual = int(episodio[episodio.rfind(' ') :].replace('!', ''))
        for c in range(1,21):
            proximo = driver.find_element_by_xpath(f'//*[@id="postados404"]/div[{c}]/a[2]')
            proximo_capitulo = proximo.get_attribute('title')
            proximo_capitulo = int(proximo_capitulo[proximo_capitulo.rfind(' ') :].replace('!', ''))
            proximo_link = proximo.get_attribute('href')
            if cap_atual+1 == proximo_capitulo:
                return proximo_link


    def escreverarquivo(episodio,pagina,downloadlink) :
        arquivo = episodio.replace(episodio[episodio.find('episodio') :], '')
        try :
            open(f'{arquivo}.txt', 'a')
        finally :
            status = 'out'
            # verifica se ja contem o episodio na lista
            with open(f'{arquivo}.txt') as lista :
                for linha in lista :
                    if episodio in linha :
                        print('ja existe')
                        status = 'in'
            # Adiciona as informações do episodio a lista.
            if status == 'out' :
                with open('one piece.txt', 'a') as texte :
                    print(f'{episodio} adicionado com sucesso')
                    print(f'{episodio}\n'
                          f'{pagina}\n'
                          f'{downloadlink}\n'
                          f'',
                          file=texte)


    for c in range(0,eps+1):
        driver.get(pagina)
        salvarEP = episodio(driver)
        salvarLI = downloadlink(driver)
        escreverarquivo(salvarEP,pagina,salvarLI)
        pagina = proximoep(driver,salvarEP)



# Pagina do anime a ser baixado/Link Capturado
pagina = 'https://www.meuanime.com/baixar?file=9285254'
# Iniciando o plugin do webdriver no chrome.
driver = 'C:/Users/Jhony/Downloads/Animes/chromedriver.exe'

animes(input('link de download'))

