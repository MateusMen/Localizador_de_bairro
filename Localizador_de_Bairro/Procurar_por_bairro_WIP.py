#carregamento de dados
import pandas as pd
#carregamento de Driver web
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()

df = pd.read_csv(r"dadosabertos_sinistros_2020.csv",sep=";")

line = df.loc[0]

rua_raw = str(line.get("LOG1"))
rua = rua_raw.replace(" ","+")
numero_int = int(line.get("NUMERO"))
numero = str(numero_int)

query = "https://www.google.com/maps/search/Brasil+Fortaleza+CE+" + rua + "+" + numero

driver.get(query)

results =[]

elems = driver.find_elements(By.XPATH, "//div[@role='article']")

for elem in elems:
    title = elem.find_element(By.CSS_SELECTOR, "div.fontHeadlineSmall")
    description = elem.find_element(By.CSS_SELECTOR, "div.fontBodyMedium")
    results.append(str(title.text)+';'+str(description.text))

driver.close()
print(elems)