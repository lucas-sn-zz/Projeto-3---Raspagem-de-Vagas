from selenium import webdriver
import pandas as pd
import time
from datetime import date

inputs = pd.read_excel("inputGERAL.xlsx",sheetname = "SHEET1")
driver = webdriver.Chrome(executable_path=r"C:\Users\Lucas Neris\Documents\GitHub\Projeto-3---Raspagem-de-Vagas\chromedriver.exe")
nome_arquivo = str('dados'+'-'+ str(date.today().day) +'-' + str(date.today().month) + '-' + str(date.today().year) +'.csv')



try:
    tabela = pd.read_csv(nome_arquivo, sep = ',',index_col = 0)
except:
    tabela= pd.DataFrame()
    tabela['vaga'] = pd.Series([])
    tabela['empresa'] = pd.Series([])
    tabela['cidade'] = pd.Series([])
    tabela['link'] = pd.Series([])
    tabela.to_csv(nome_arquivo)
    
def indeed_links():
    for x in range(len(inputs)):
        assuntos = inputs.ix[x].Assunto
        assuntos = assuntos.replace(" ","+")
        cidades = inputs.ix[x].Cidade
        cidades = cidades.replace(" ","+")
        time.sleep(5)
        driver.get("https://www.indeed.com.br/empregos?q=" + assuntos + "&l=" + cidades)
        links = []

        for z in driver.find_elements_by_xpath("//div[@class='jobsearch-SerpJobCard row result clickcard']/a"):
            links.append(z.get_attribute('href'))
        for z in driver.find_elements_by_xpath("//div[@class='jobsearch-SerpJobCard row sjlast result clickcard']/a"):
            links.append(z.get_attribute('href'))
        try:
            for z in driver.find_elements_by_xpath("//div[@class='jobsearch-SerpJobCard row result clickcard']//h2[@class ='jobtitle']/a"):
                links.append(z.get_attribute('href'))
        except:
            pass
        
        print(len(links))
        for x in links:
            time.sleep(2)
            driver.get(x)
            informacao = [indeed_titulo_vaga(),indeed_empresa_e_cidade()[0],   indeed_empresa_e_cidade()[1] if len(indeed_empresa_e_cidade()) is 2 else ""
,indeed_link_original()]
            print(informacao)
            tabela.loc[-1] = informacao
            tabela.index = tabela.index + 1
        tabela.to_csv("site_dados.csv")
        tabela.to_excel("site_dados.xlsx")
    
    



    
    
    
    
    #pegar os links da paginas

                
            
            
            
            
        
    
def indeed_titulo_vaga():
    return(driver.find_element_by_xpath("//h3[@class='icl-u-xs-mb--xs icl-u-xs-mt--none jobsearch-JobInfoHeader-title']").text)

    #Link original
def indeed_link_original():
    try: 
        return(driver.find_element_by_xpath("//span[@id='originalJobLinkContainer' and @class = 'icl-u-lg-inline icl-us-xs-hide' ]/a").get_attribute('href'))

    except:
        return(driver.current_url)
            
    

def indeed_empresa_e_cidade():
    # Empresa; Cidade; Estado
    
    return(driver.find_element_by_xpath("//div[@class='jobsearch-InlineCompanyRating icl-u-xs-mt--xs  jobsearch-DesktopStickyContainer-companyrating']").text.split("\n-\n"))




indeed_links()


