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

@when('Aplasta el botón agregar')
def aplastar_boton_agregar(context):
    try:
        agregar_button = context.driver.find_element(By.XPATH, '/html/body/div[1]/div/button')
        agregar_button.click()
        take_screenshot(context, '2. Clickar el boton agregar')
    except Exception as e:
        mark_step_as_failed(context, 'aplastar_boton_agregar', e)

@when('Rellenar el campo Nombre {nombre}')
def rellenar_nombre(context, nombre):
    try:
        nombre_field = context.driver.find_element(By.XPATH, '//*[@id="firstName"]')
        nombre_field.send_keys(nombre)
        take_screenshot(context, '3. Rellenar el campo Nombre')
    except Exception as e:
        mark_step_as_failed(context, 'rellenar_nombre', e)

@when('Rellenar el campo Apellido {apellido}')
def rellenar_apellido(context, apellido):
    try:
        apellido_field = context.driver.find_element(By.XPATH, '//*[@id="lastName"]')
        apellido_field.send_keys(apellido)
        take_screenshot(context, '4. Rellenar el campo Apellido')
    except Exception as e:
        mark_step_as_failed(context, 'rellenar_apellido', e)

@when('Rellenar el campo Número de Telefono {telefono}')
def rellenar_telefono(context, telefono):
    try:
        telefono_field = context.driver.find_element(By.XPATH, '//*[@id="phoneNumber"]')
        telefono_field.send_keys(telefono)
        take_screenshot(context, '5. Rellenar el campo Número de Telefono')
    except Exception as e:
        mark_step_as_failed(context, 'rellenar_telefono', e)

@when('Seleccionar el sexo {sexo}')
def seleccionar_sexo(context, sexo):
    try:
        sexo_dropdown = Select(context.driver.find_element(By.XPATH, '//*[@id="gender"]'))
        sexo_dropdown.select_by_visible_text(sexo)
        take_screenshot(context, '6. Seleccionar el sexo')
    except Exception as e:
        mark_step_as_failed(context, 'seleccionar_sexo', e)

@when('Rellenar el campo Cédula {cedula}')
def rellenar_cedula(context, cedula):
    try:
        cedula_field = context.driver.find_element(By.XPATH, '//*[@id="idCard"]')
        cedula_field.send_keys(cedula)
        take_screenshot(context, '7. Rellenar el campo Cédula')
    except Exception as e:
        mark_step_as_failed(context, 'rellenar_cedula', e)

@when('Seleccionar el tipo de licencia {licencia}')
def seleccionar_licencia(context, licencia):
    try:
        licencia_dropdown = Select(context.driver.find_element(By.XPATH, '//*[@id="licenseType"]'))
        licencia_dropdown.select_by_visible_text(licencia)
        take_screenshot(context, '8. Seleccionar el tipo de licencia')
    except Exception as e:
        mark_step_as_failed(context, 'seleccionar_licencia', e)

@when('Seleccionar el tipo de sangre {sangre}')
def seleccionar_sangre(context, sangre):
    try:
        sangre_dropdown = Select(context.driver.find_element(By.XPATH, '//*[@id="bloodType"]'))
        sangre_dropdown.select_by_visible_text(sangre)
        take_screenshot(context, '9. Seleccionar el tipo de sangre')
    except Exception as e:
        mark_step_as_failed(context, 'seleccionar_sangre', e)

@when('Seleccionar la foto del chofer {foto_path}')
def seleccionar_foto_chofer(context, foto_path):
    try:
        foto_input = context.driver.find_element(By.XPATH, '//*[@id="photo"]')
        foto_input.send_keys(foto_path)
        take_screenshot(context, '10. Seleccionar la foto del chofer')
    except Exception as e:
        mark_step_as_failed(context, 'seleccionar_foto_chofer', e)

@then('Aplastar el boton para guardar el chofer')
def aplastar_guardar_chofer(context):
    try:
        guardar_button = context.driver.find_element(By.XPATH, '//*[@id="addDriverForm"]/button')
        guardar_button.click()
        take_screenshot(context, '11. Aplastar el boton para guardar el chofer')
        print("Driver saved")
    except Exception as e:
        mark_step_as_failed(context, 'aplastar_guardar_chofer', e)

@then('Visualizar el chofer guardado')
def visualizar_chofer_guardado(context):
    try:
        WebDriverWait(context.driver, 5).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="choferes"]/div[4]'))
        )
        chofer_guardado = context.driver.find_element(By.XPATH, '//*[@id="choferes"]/div[4]')
        if chofer_guardado.is_displayed():
            take_screenshot(context, '12. Visualizar el chofer guardado')
            mark_step_as_passed(context, 'visualizar_chofer_guardado')
        else:
            raise Exception("El chofer guardado no es visible")
    except Exception as e:
        mark_step_as_failed(context, 'visualizar_chofer_guardado', e)
