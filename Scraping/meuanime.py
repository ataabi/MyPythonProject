from selenium import webdriver

# Iniciando o Navegador.
driver = webdriver.Chrome('C:/Users/Jhony/Downloads/Animes/chromedriver.exe')
driver.get('https://www.meuanime.com/baixar?file=1857')
# Procurando o link para download.
downloadlink = driver.find_element_by_xpath('//*[@id="conteudo404"]/div/a')
print(downloadlink.get_attribute('href'))
# Avançando Para o Proximo episodio.
'''episodio = driver.find_element_by_xpath('//*[@id="corpo"]/div[1]/div[1]')

for c in episodio.get_attribute('<p>'):
    print(c)'''
proximo = driver.find_element_by_xpath('//*[@id="postados404"]/div[16]/a[1]')
print(proximo.get_attribute('href'))