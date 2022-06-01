from selenium import webdriver


# Iniciando o Navegador.
driver = webdriver.Chrome('C:/Users/Jhony/Downloads/Animes/chromedriver.exe')
# Pagina do anime a ser baixado/Link Capturado
pagina = 'https://www.meuanime.com/baixar?file=55941'
# Arquivo onde os link seram salvos
open('one piece.txt', 'a')
# Inicia loop de captura
for eps in range(0,3):
    # inicia com estatus 'fora' para informar que o link ainda nao foi salvo
    status = "out"
    # Procurando o link para download. do site MeuAnime.com
    driver.get(pagina)
    # Procura o Episodio Atual
    episodio = driver.find_element_by_xpath('/html/body/div[5]/div/div[1]/p')
    episodio = episodio.text
    episodio = episodio.replace('Voçê esta baixando - ','')
    print(f"\033[33m{episodio}\033[m")

    # Procura o link de download
    download = driver.find_element_by_xpath('//*[@id="conteudo404"]/div/a')
    download = download.get_attribute('href')
    #print(download)
    # Procura o link para o proximo episodio
    proximo = driver.find_element_by_xpath('//*[@id="postados404"]/div[16]/a[1]')
    proximo = proximo.get_attribute('href')
    #print(proximo)
    # verifica se ja contem o episodio na lista
    with open('one piece.txt') as lista:
        for linha in lista:
            if episodio in linha:
                print('ja existe')
                status = 'in'
    # Adiciona as informações do episodio a lista.
    if status == 'out':
        with open('one piece.txt', 'a') as texte :
            print(f'{episodio} adicionado com sucesso')
            print(f'{episodio}\n'
                  f'{pagina}\n'
                  f'{download}\n',
                  file=texte)


    # Troca a pagina do episodio
    pagina = proximo
    print()

driver.close()
