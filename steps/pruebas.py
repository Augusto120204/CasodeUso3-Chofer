import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
import os

# Configuración del navegador
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument('--disable-extensions')
options.add_argument('--no-sandbox')
options.add_argument('--disable-infobars')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--disable-browser-side-navigation')
options.add_argument('--disable-gpu')

def take_screenshot(context, step_name):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    screenshot_dir = "screenshots"
    if not os.path.exists(screenshot_dir):
        os.makedirs(screenshot_dir)
    screenshot_name = os.path.join(screenshot_dir, f"{step_name}_{timestamp}.png")
    context.driver.save_screenshot(screenshot_name)
    context.pdf.add_screenshot(screenshot_name, step_name)
    print(f"Screenshot taken: {screenshot_name}")
    return screenshot_name

def mark_step_as_failed(context, step_name, exception):
    print(f"Error in '{step_name}': {exception}")
    raise Exception(f"Step failed: {step_name}. Error: {exception}")

def mark_step_as_passed(context, step_name):
    print(f"Step passed: {step_name}")

@given('Se inicia el navegador')
def iniciarNavegador(context):
    context.driver = webdriver.Chrome(options=options)
    context.failed_steps = []
    print("Browser started")

@when('Entra a la seccion chofer')
def entrar_seccion_chofer(context):
    try:
        context.driver.maximize_window()
        context.driver.get("C:\\Users\\cesar\\OneDrive\\Desktop\\req\\Chofer\\Chofer.html")
        take_screenshot(context, '1. Entra a la seccion chofer')
        print("Entered 'Chofer' section")
    except Exception as e:
        mark_step_as_failed(context, 'entra_seccion_chofer', e)

@when('Escribir el nombre a buscar {nombre}')
def buscar_nombre(context, nombre):
    try:
        nombre_field = context.driver.find_element(By.XPATH, '//*[@id="nombre"]')
        nombre_field.send_keys(nombre)
        take_screenshot(context, '2. Escribir el nombre a buscar')
    except Exception as e:
        mark_step_as_failed(context, 'buscar_nombre', e)

@then('Visualizar el chofer buscado')
def visualizar_chofer_buscado(context):
    try:
        WebDriverWait(context.driver, 5).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="choferes"]/div[1]'))
        )
        chofer_buscado = context.driver.find_element(By.XPATH, '//*[@id="choferes"]/div[1]')
        if chofer_buscado.is_displayed():
            take_screenshot(context, '3. Visualizar el chofer buscado')
            mark_step_as_passed(context, 'visualizar_chofer_buscado')
        else:
            raise Exception("El chofer buscado no existe")
    except Exception as e:
        mark_step_as_failed(context, 'visualizar_chofer_buscado', e)
