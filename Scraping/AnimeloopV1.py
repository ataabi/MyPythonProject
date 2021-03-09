from selenium import webdriver

class Animes:
    from selenium import webdriver
    # Pagina do anime a ser baixado/Link Capturado
    pagina = 'https://www.meuanime.com/baixar?file=2055'
    # Iniciando o Navegador.
    driver = webdriver.Chrome('C:/Users/Jhony/Downloads/Animes/chromedriver.exe')

    # Inicia a Pagina no navegador
    driver.get(pagina)

    def episodio(driver):
        episodio = driver.find_element_by_xpath('/html/body/div[5]/div/div[1]/p')
        episodio = episodio.text
        episodio = episodio.replace('Voçê esta baixando - ', '')
        episodio = episodio.strip()
        print(f"\033[33m{episodio}\033[m")
        return episodio

    def linkdownload(driver):
        # Procura o link de download
        download = driver.find_element_by_xpath('//*[@id="conteudo404"]/div/a')
        download = download.get_attribute('href')
        return download

    def escreverarquivo(episodio):
        arquivo = episodio.replace(episodio[episodio.find('episodio'):],'')
        try:
            open(f'{arquivo}.txt', 'a')
        finally:
            # verifica se ja contem o episodio na lista
            with open(f'{arquivo}.txt') as lista:
                for linha in lista:
                    if episodio in linha:
                        print('ja existe')
                        status = 'in'
            # Adiciona as informações do episodio a lista.
            if status == 'out':
                with open('one piece.txt', 'a') as texte :
                    print(f'{episodio} adicionado com sucesso')
                    print(f'{episodio}\n',
                          file=texte)

    def proximoep(driver):

        proximo = driver.find_element_by_xpath('//*[@id="postados404"]/div[16]/a[1]')
        proximo = proximo.get_attribute('href')
        return proximo

    def anime(pagina, eps=1) :
        # Arquivo onde os link seram salvos
        open('one piece.txt', 'a')
        # Inicia loop de captura
        for capitulo in range(0, eps) :
            # inicia com estatus 'fora' para informar que o link ainda nao foi salvo
            status = "out"


            # print(download)
            # Procura o link para o proximo episodio

            # print(proximo)
            return driver

            # Troca a pagina do episodio
            pagina = proximo
            print()

Animes
