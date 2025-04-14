from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from datetime import datetime

class GLPIBot:
    def __init__(self, usuario, senha, url="https://chamados.idxdatacenters.com.br"):
        self.usuario = usuario
        self.senha = senha
        self.url = url
        self.driver = webdriver.Firefox()

    def login(self):
        self.driver.get(self.url)
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="login_name"]')))
        self.driver.find_element(By.XPATH, '//*[@id="login_name"]').send_keys(self.usuario)
        self.driver.find_element(By.XPATH, '//*[@id="login_password"]').send_keys(self.senha)

        login_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.NAME, "submit")))
        login_button.click()

        WebDriverWait(self.driver, 20).until(
            lambda driver: driver.execute_script("return document.readyState") == "complete"
        )
    def extrair_chamados(self):
        self.driver.get(self.url + "/front/ticket.php?is_deleted=0&as_map=0&browse=0&criteria%5B0%5D%5Blink%5D=AND&criteria%5B0%5D%5Bfield%5D=65&criteria%5B0%5D%5Bsearchtype%5D=equals&criteria%5B0%5D%5Bvalue%5D=16&criteria%5B1%5D%5Blink%5D=AND&criteria%5B1%5D%5Bfield%5D=12&criteria%5B1%5D%5Bsearchtype%5D=equals&criteria%5B1%5D%5Bvalue%5D=notold&criteria%5B2%5D%5Blink%5D=AND&criteria%5B2%5D%5Bfield%5D=18&criteria%5B2%5D%5Bsearchtype%5D=equals&_select_criteria%5B2%5D%5Bvalue%5D=TODAY&criteria%5B2%5D%5Bvalue%5D=TODAY&itemtype=Ticket&start=0&_glpi_csrf_token=85007dfad6233902c9a5bfc84bf56950c17b5d800808d563bcb5d40b0d770909&sort%5B%5D=19&order%5B%5D=DESC")

        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, "search-results")))

        try:
            chamados = WebDriverWait(self.driver, 10).until(
                EC.presence_of_all_elements_located((By.XPATH, '//table[contains(@class, "search-results")]//tbody/tr'))
            )
        except:
            print("❌ Nenhum chamado encontrado na página.")
            self.driver.quit()
            return []

        lista_chamados = []

        for chamado in chamados:
            try:
                numero = chamado.find_element(By.XPATH, './td[2]/span').text.strip().replace(" ", "")
                tempo_solucao = chamado.find_element(By.XPATH, './td[17]').text.strip()
                tecnico = chamado.find_element(By.XPATH, './td[10]').text.strip()
                categoria = chamado.find_element(By.XPATH, './td[11]').text.strip()

                if numero.isdigit() and tecnico != "" and categoria not in ["Infra", "Telefonia"]:
                    lista_chamados.append({
                        "numero": numero,
                        "tecnico": tecnico,
                        "tempo_solucao": tempo_solucao,
                        "categoria": categoria
                    })
            except Exception:
                continue  # Pula linhas que não possuem o formato esperado

        if not lista_chamados:
            print("ℹ️ Nenhum chamado válido encontrado no momento.")
            self.driver.quit()
            return []

        self.driver.quit()
        return lista_chamados
