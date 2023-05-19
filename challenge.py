#Importa o módulo RPA, que fornece funcionalidades de automação.
import rpa as r
import pandas as pd

#Importa o módulo pandas, que é usado para ler o arquivo Excel e manipular os dados.
df= pd.read_excel('challenge.xlsx')

#Lê o arquivo Excel 
r.init()


r.url('http://www.rpachallenge.com/')
#Aguarda 5 segundos para garantir que a página esteja totalmente carregada.
r.wait(5)

r.click('//button[text()="Start"]')

#a seguir utilizei um loop for para iterar sobre as linhas do DataFrame df e realizar as operações de entrada de dados no formulário da web
for index,row in df.iterrows():
    r.type('//input[@ng-reflect-name="labelFirstName"]',row['First Name'])
    r.type('//input[@ng-reflect-name="labelLastName"]',row['Last Name '])
    r.type('//input[@ng-reflect-name="labelCompanyName"]',row['Company Name'])
    r.type('//input[@ng-reflect-name="labelRole"]',row['Role in Company'])
    r.type('//input[@ng-reflect-name="labelAddress"]',row['Address'])
    r.type('//input[@ng-reflect-name="labelEmail"]',row['Email'])
    r.type('//input[@ng-reflect-name="labelPhone"]',str(row['Phone Number']))
    r.click('//input[@value="Submit"]')



r.snap('/html/body/app-root/div[2]','results.png')

#Encerra o processo do RPA
r.close()



    
