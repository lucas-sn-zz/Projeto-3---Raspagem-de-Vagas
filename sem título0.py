# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 13:41:54 2018

@author: Lucas Neris
"""
from selenium import webdriver
import pandas as pd
import time
from datetime import date
driver = webdriver.Chrome(executable_path=r"C:\Users\Lucas Neris\Documents\GitHub\Projeto-3---Raspagem-de-Vagas\chromedriver.exe")

driver.get('https://www.vagas.com.br/vagas-de-banco-rio-de-janeiro?')
inputs = pd.read_excel('teste.xlsx', sheetname = 'SHEET1')
links = []
for z in driver.find_elements_by_xpath("//li[@class='vaga odd ']"):
    print(z.find_element_by_tag_name('a').get_attribute('title'))
    print(z.find_element_by_tag_name('a').get_attribute('href'))
    print(z.find_element_by_xpath("*//span[@class = 'emprVaga']").text)
    print(z.find_element_by_xpath("//footer/span[@class = 'vaga-local']").text)
    
for z in driver.find_elements_by_xpath("//li[@class='vaga even ']"):
    print(z.find_element_by_tag_name('a').get_attribute('title'))
    print(z.find_element_by_tag_name('a').get_attribute('href'))
    print(z.find_element_by_xpath("*//span[@class = 'emprVaga']").text)
    print(z.find_element_by_xpath("//footer/span[@class = 'vaga-local']").text)    
    


driver.find_element_by_xpath("*//a[@class='btMaisVagas btn']").click()


