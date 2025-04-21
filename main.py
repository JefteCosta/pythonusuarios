import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# Lê uma planilha Excel (pode ser criada com openpyxl)
df = pd.read_excel('planilha.xlsx')
print("Dados lidos:", df.head())

# Inicia o navegador com WebDriver Manager
options = webdriver.ChromeOptions()
options.add_argument('--headless')  # remove se quiser ver o navegador

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Exemplo: abrir o Google e buscar algo
driver.get("https://www.google.com")
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("Python Selenium")
search_box.submit()

# Espera o carregamento e extrai algo
driver.implicitly_wait(5)
print("Título da página:", driver.title)

driver.quit()
