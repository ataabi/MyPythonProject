from selenium import webdriver
from time import sleep


# Iniciando o Navegador.
driver = webdriver.Chrome('C:/Users/Jhony/Downloads/Animes/chromedriver.exe')
pagina = 'https://www.meuanime.com/baixar?file=1857'
count = 0
status = "notok"
open('anime.txt', 'a')
while count != 3:
    # Procurando o link para download.
    driver.get(pagina)

    episodio = driver.find_element_by_xpath('/html/body/div[5]/div/div[1]/p')
    episodio = episodio.text
    episodio = episodio.replace('Voçê esta baixando - ','')
    print(episodio)

    download = driver.find_element_by_xpath('//*[@id="conteudo404"]/div/a')
    download = download.get_attribute('href')
    print(download)

    proximo = driver.find_element_by_xpath('//*[@id="postados404"]/div[16]/a[1]')
    proximo = proximo.get_attribute('href')
    print(proximo)

    with open('anime.txt', 'a') as texte :
        print(f'{episodio} adicionado com sucesso')
        print(episodio, '\n',
              download, '\n', file=texte)


    pagina = proximo
    count += 1
    print()
    sleep(1)

driver.close()