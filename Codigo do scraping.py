from selenium import webdriver
import pandas as pd
import time
driver = webdriver.Firefox()
from datetime import date
nome_arquivo = str('dados'+'-'+ str(date.today().day) +'-' + str(date.today().month) + '-' + str(date.today().year) +'.csv')
try:
    tabela = pd.read_csv(nome_arquivo, sep = ',',index_col = 0)
except:
    tabela= pd.to_csv(nome_arquivo)
def informacoes_pag():
    #aqui serão armazenados os links encontrados a fim de entrar em cada página
    #vamos fazer um for em cada link para pegar as informações
    nome_empresas = 'BTG'
    região = 'Rio de Janeiro'
        driver.get('https://www.truckpad.com.br/fretes?page='+ str(y))
        if y == 10 or 20 or 30 or 40 or 50 or 60 or 70 or 80 or 90:
            tabela.to_csv('dados.csv', sep=',')
        time.sleep(1)
        print(y)
        links = []
        for z in driver.find_elements_by_xpath("//div[@class='container-freight media border-top position-relative']/a"):
            links.append(z.get_attribute('href'))
        print(links)
        for x in  range(len(links)):
            print(x)
            driver.get(links[x])
        ##  print(links[x])
            time.sleep(0.9)
       ##     print('aqui foi')
                ### print(x.get_attribute('href'))
            infom = [links[x],cidade_origem(),cidade_destino(),data_coleta(),data_entrega(),distancia(),peso(),caminhoes(),(x +1)]
            tabela.loc[-1] = infom
            tabela.index = tabela.index + 1 
            
            
def cidade_origem():
    return(driver.find_elements_by_xpath("//div[@class='origin_destiny config_line_infos row col-12 col-sm-6 col-lg-6 margin-0px']//div[@class='col-7 p-0']/p[@class='description']")[0].text)

    
def cidade_destino():
    return(driver.find_elements_by_xpath("//div[@class='origin_destiny config_line_infos row col-12 col-sm-6 col-lg-6 margin-0px']//div[@class='col-5 reset-padding-mobile']/p[@class='description']")[0].text)

    
def data_coleta():
    return(driver.find_elements_by_xpath("//div[@class='principal_information config_line_infos row col-12 col-sm-6 col-lg-6 margin-0px']//div[@class='col-7 p-0']/p[@class='description']")[1].text)

def data_entrega():
    return(driver.find_elements_by_xpath("//div[@class='principal_information config_line_infos row col-12 col-sm-6 col-lg-6 margin-0px']//div[@class='col-5 reset-padding-mobile']/p[@class='description']")[1].text)
    
def distancia():
    return(driver.find_elements_by_xpath("//div[@class='origin_destiny config_line_infos row col-12 col-sm-6 col-lg-6 margin-0px']//div[@class='col-5 reset-padding-mobile']/p[@class='description']")[1].text)
      
def peso():
    return(driver.find_elements_by_xpath("//div[@class='principal_information config_line_infos row col-12 col-sm-6 col-lg-6 margin-0px']//div[@class='col-5 reset-padding-mobile']/p[@class='description']")[0].text)


def  caminhoes():
    caminhoes = []
    for x in driver.find_elements_by_xpath("//div[@class='vehicle_infos config_line_infos col-12']//p[@class='description float-left']/span"):
        caminhoes.append(x.text)
    return(caminhoes)