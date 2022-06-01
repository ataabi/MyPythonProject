from selenium import webdriver

# Captura o nome do episodio em uma string
def episodio(driver) :

    episodio = driver.find_element_by_xpath('/html/body/div[5]/div/div[1]/p')
    episodio = episodio.text
    episodio = episodio.replace('Voçê esta baixando - ', '')
    return episodio

# Captura o link de download do episodio
def downloadlink(driver) :
    # Procura o link de download
    download = driver.find_element_by_xpath('//*[@id="conteudo404"]/div/a')
    download = download.get_attribute('href')
    return download

# Pega o nome do e deixa somente o numero do ep
def clearstr(episodio):
    epnum = episodio[episodio.rfind(' ') :]
    for letra in epnum.split():
        for l in letra:
            if l in '0123456789':
                pass
            else:
                epnum = epnum.replace(l,'')
    return int(epnum)


def proximoep(driver,episodio) :
    for c in range(20,0,-1):
        try:
            proximo = driver.find_element_by_xpath(f'//*[@id="postados404"]/div[{c}]/a[2]')
        except:
            proximo = driver.find_element_by_xpath(f'//*[@id="postados404"]/div[2]')

        proximo_capitulo = proximo.get_attribute('title')
        proximo_link = proximo.get_attribute('href')
        atual = clearstr(episodio)
        if 'Episódio' in proximo_capitulo:
            proximo_capitulo = clearstr(proximo_capitulo)
            if atual+1 == proximo_capitulo:
                return proximo_link
                break
            elif atual+2 == proximo_capitulo:
                return proximo_link
                break


def escreverarquivo(episodio,pagina,downloadlink):
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
            with open(f'{arquivo}.txt', 'a') as texte :
                print(f'{episodio} adicionado com sucesso')
                print(f'{episodio}\n'
                      f'{pagina}\n'
                      f'{downloadlink}\n'
                      f'',
                      file=texte)


pagina = "https://www.meuanime.com/baixar?file="+\
         input('Digite os ultimos numeros do link de download:\n')

eps = int(input('Numeros de episodios.\n:'))
driver = webdriver.Chrome('C:/Users/Jhony/Downloads/Animes/chromedriver.exe')
driver.get(pagina)

for ep in range(1,eps+1):
    try:
        driver.get(pagina)
    except :
        print("Esse foi o ultimo.")
        break
    finally:
        chapter = episodio(driver)
        link = downloadlink(driver)
        escreverarquivo(chapter,pagina,link)
        pagina = proximoep(driver,chapter)


# Pagina do anime a ser baixado/Link Capturado
