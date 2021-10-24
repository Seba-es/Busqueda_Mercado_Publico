from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import pandas as pd

# Variables del navegador
ruta_driver = "A:\chromedriverfor_selenium\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(ruta_driver)
driver.maximize_window()  # Para trabajar en Pantalla Completa
driver.implicitly_wait(120)  # Espera 20 despúes de cada acción
web = "https://www.mercadopublico.cl/TiendaHome/"
action = ActionChains(driver)

# Variables tipos de Convenios Marco
ferreteria = '//*[@id="home-row-no-rs"]/section/div/div[2]/div/a[1]/div'
emergencia = '//*[@id="home-row-no-rs"]/section/div/div[2]/div/a[3]/div'
combustibles = '//*[@id="home-row-no-rs"]/section/div/div[2]/div/a[5]/div'
articulos_escritorio = '//*[@id="home-row-no-rs"]/section/div/div[2]/div/a[7]/div'
alimentos = '//*[@id="home-row-no-rs"]/section/div/div[2]/div/a[9]/div'
otros_convenios = (
    '//*[@id="home-row-no-rs"]/section/div/div[2]/div/a[11]/div'  # no puedo buscar aca
)
aseo = '//*[@id="home-row-no-rs"]/section/div/div[2]/div/a[2]/div'
sofware = '//*[@id="home-row-no-rs"]/section/div/div[2]/div/a[4]/div'
mobiliario = '//*[@id="home-row-no-rs"]/section/div/div[2]/div/a[6]/div'
laptop = '//*[@id="home-row-no-rs"]/section/div/div[2]/div/a[8]/div'
administracion = '//*[@id="home-row-no-rs"]/section/div/div[2]/div/a[10]/div'

# Pandas
df = pd.read_excel(
    "A:\Programación\Python\Pruebas_WebScraping\Búsqueda Mercado Público/Requerimiento_Productos.xlsx"
)
lista_productos = []
lista_licitaciones = []
driver.get(web)

for filas, datos in df.iterrows():
    index = datos["ID"]
    unidad = datos["Unidad"]
    nombre_producto = datos["Nombre Producto"]
    despacho = datos["Dirección de despacho"]
    receptor = datos["Receptor del Producto "]
    licitacion = datos["Convenio Marco "]
    pagina_web = datos["Link"]

    lista_productos.append(nombre_producto)
    lista_licitaciones.append(licitacion)

    # Búsqueda de productos
    if lista_licitaciones[0] == "Articulos de Escritorio":
        if licitacion == "Articulos de Escritorio":
            tipo_convenio_marco = driver.find_element_by_xpath(
                articulos_escritorio
            ).click()
            producto = driver.find_element_by_xpath('//*[@id="search"]')
            producto.send_keys(nombre_producto)
            boton_buscar = driver.find_element_by_xpath(
                '//*[@id="search_mini_form"]/div[2]/button'
            ).click()

        elif licitacion == "Ferreteria":
            cambiar_seccion = driver.find_element_by_xpath('//*[@id="store"]').click()
            selecionar = driver.find_element_by_xpath(
                '//*[@id="store"]/option[1]'
            ).click()
            producto = driver.find_element_by_xpath('//*[@id="search"]')
            producto.clear()
            producto.send_keys(nombre_producto)
            boton_buscar = driver.find_element_by_xpath(
                '//*[@id="search_mini_form"]/div[2]/button'
            ).click()

        elif licitacion == "Emergencias":
            cambiar_seccion = driver.find_element_by_xpath('//*[@id="store"]').click()
            selecionar = driver.find_element_by_xpath(
                '//*[@id="store"]/option[3]'
            ).click()
            producto = driver.find_element_by_xpath('//*[@id="search"]')
            producto.clear()
            producto.send_keys(nombre_producto)
            boton_buscar = driver.find_element_by_xpath(
                '//*[@id="search_mini_form"]/div[2]/button'
            ).click()

        elif licitacion == "Combustibles":
            cambiar_seccion = driver.find_element_by_xpath('//*[@id="store"]').click()
            selecionar = driver.find_element_by_xpath(
                '//*[@id="store"]/option[4]'
            ).click()
            producto = driver.find_element_by_xpath('//*[@id="search"]')
            producto.clear()
            producto.send_keys(nombre_producto)
            boton_buscar = driver.find_element_by_xpath(
                '//*[@id="search_mini_form"]/div[2]/button'
            ).click()

        elif licitacion == "Alimentos":
            cambiar_seccion = driver.find_element_by_xpath('//*[@id="store"]').click()
            selecionar = driver.find_element_by_xpath(
                '//*[@id="store"]/option[9]'
            ).click()
            producto = driver.find_element_by_xpath('//*[@id="search"]')
            producto.clear()
            producto.send_keys(nombre_producto)
            boton_buscar = driver.find_element_by_xpath(
                '//*[@id="search_mini_form"]/div[2]/button'
            ).click()

        elif licitacion == " Software":
            cambiar_seccion = driver.find_element_by_xpath('//*[@id="store"]').click()
            selecionar = driver.find_element_by_xpath(
                '//*[@id="store"]/option[5]'
            ).click()
            producto = driver.find_element_by_xpath('//*[@id="search"]')
            producto.clear()
            producto.send_keys(nombre_producto)
            boton_buscar = driver.find_element_by_xpath(
                '//*[@id="search_mini_form"]/div[2]/button'
            ).click()

        elif licitacion == " Mobiliario":
            cambiar_seccion = driver.find_element_by_xpath('//*[@id="store"]').click()
            selecionar = driver.find_element_by_xpath(
                '//*[@id="store"]/option[6]'
            ).click()
            producto = driver.find_element_by_xpath('//*[@id="search"]')
            producto.clear()
            producto.send_keys(nombre_producto)
            boton_buscar = driver.find_element_by_xpath(
                '//*[@id="search_mini_form"]/div[2]/button'
            ).click()

        elif licitacion == "Computadores":
            cambiar_seccion = driver.find_element_by_xpath('//*[@id="store"]').click()
            selecionar = driver.find_element_by_xpath(
                '//*[@id="store"]/option[8]'
            ).click()
            producto = driver.find_element_by_xpath('//*[@id="search"]')
            producto.clear()
            producto.send_keys(nombre_producto)
            boton_buscar = driver.find_element_by_xpath(
                '//*[@id="search_mini_form"]/div[2]/button'
            ).click()

        elif licitacion == "Aseo":
            cambiar_seccion = driver.find_element_by_xpath('//*[@id="store"]').click()
            selecionar = driver.find_element_by_xpath(
                '//*[@id="store"]/option[2]'
            ).click()
            producto = driver.find_element_by_xpath('//*[@id="search"]')
            producto.clear()
            producto.send_keys(nombre_producto)
            boton_buscar = driver.find_element_by_xpath(
                '//*[@id="search_mini_form"]/div[2]/button'
            ).click()

        else:
            print(f'La categoria del producto "{producto}" no se encuentra disponible')

    if not lista_licitaciones[0] == "Articulos de Escritorio":
        if licitacion == "Ferreteria":
            ActionChains(driver).key_down(Keys.CONTROL).send_keys("t").key_up(
                Keys.CONTROL
            ).perform()
            driver.get(web)
            tipo_convenio_marco = driver.find_element_by_xpath(ferreteria).click()
            producto = driver.find_element_by_xpath('//*[@id="search"]')
            producto.send_keys(nombre_producto)
            boton_buscar = driver.find_element_by_xpath(
                '//*[@id="search_mini_form"]/div[2]/button'
            ).click()
        elif licitacion == "Articulos de Escritorio":
            ActionChains(driver).key_down(Keys.CONTROL).send_keys("t").key_up(
                Keys.CONTROL
            ).perform()
            driver.get(web)
            tipo_convenio_marco = driver.find_element_by_xpath(
                articulos_escritorio
            ).click()
            producto = driver.find_element_by_xpath('//*[@id="search"]')
            producto.send_keys(nombre_producto)
            boton_buscar = driver.find_element_by_xpath(
                '//*[@id="search_mini_form"]/div[2]/button'
            ).click()

        elif licitacion == "Emergencias":
            ActionChains(driver).key_down(Keys.CONTROL).send_keys("t").key_up(
                Keys.CONTROL
            ).perform()
            driver.get(web)
            tipo_convenio_marco = driver.find_element_by_xpath(emergencia).click()
            producto = driver.find_element_by_xpath('//*[@id="search"]')
            producto.send_keys(nombre_producto)
            boton_buscar = driver.find_element_by_xpath(
                '//*[@id="search_mini_form"]/div[2]/button'
            ).click()

        elif licitacion == "Combustibles":
            ActionChains(driver).key_down(Keys.CONTROL).send_keys("t").key_up(
                Keys.CONTROL
            ).perform()
            driver.get(web)
            tipo_convenio_marco = driver.find_element_by_xpath(combustibles).click()
            producto = driver.find_element_by_xpath('//*[@id="search"]')
            producto.send_keys(nombre_producto)
            boton_buscar = driver.find_element_by_xpath(
                '//*[@id="search_mini_form"]/div[2]/button'
            ).click()

        elif licitacion == "Alimentos":
            ActionChains(driver).key_down(Keys.CONTROL).send_keys("t").key_up(
                Keys.CONTROL
            ).perform()
            driver.get(web)
            tipo_convenio_marco = driver.find_element_by_xpath(alimentos).click()
            producto = driver.find_element_by_xpath('//*[@id="search"]')
            producto.send_keys(nombre_producto)
            boton_buscar = driver.find_element_by_xpath(
                '//*[@id="search_mini_form"]/div[2]/button'
            ).click()

        elif licitacion == " Software":
            ActionChains(driver).key_down(Keys.CONTROL).send_keys("t").key_up(
                Keys.CONTROL
            ).perform()
            driver.get(web)
            tipo_convenio_marco = driver.find_element_by_xpath(sofware).click()
            producto = driver.find_element_by_xpath('//*[@id="search"]')
            producto.send_keys(nombre_producto)
            boton_buscar = driver.find_element_by_xpath(
                '//*[@id="search_mini_form"]/div[2]/button'
            ).click()

        elif licitacion == " Mobiliario":
            ActionChains(driver).key_down(Keys.CONTROL).send_keys("t").key_up(
                Keys.CONTROL
            ).perform()
            driver.get(web)
            tipo_convenio_marco = driver.find_element_by_xpath(mobiliario).click()
            producto = driver.find_element_by_xpath('//*[@id="search"]')
            producto.send_keys(nombre_producto)
            boton_buscar = driver.find_element_by_xpath(
                '//*[@id="search_mini_form"]/div[2]/button'
            ).click()

        elif licitacion == "Computadores":
            ActionChains(driver).key_down(Keys.CONTROL).send_keys("t").key_up(
                Keys.CONTROL
            ).perform()
            driver.get(web)
            tipo_convenio_marco = driver.find_element_by_xpath(laptop).click()
            producto = driver.find_element_by_xpath('//*[@id="search"]')
            producto.send_keys(nombre_producto)
            boton_buscar = driver.find_element_by_xpath(
                '//*[@id="search_mini_form"]/div[2]/button'
            ).click()

        elif licitacion == "Aseo":
            ActionChains(driver).key_down(Keys.CONTROL).send_keys("t").key_up(
                Keys.CONTROL
            ).perform()
            driver.get(web)
            tipo_convenio_marco = driver.find_element_by_xpath(aseo).click()
            producto = driver.find_element_by_xpath('//*[@id="search"]')
            producto.send_keys(nombre_producto)
            boton_buscar = driver.find_element_by_xpath(
                '//*[@id="search_mini_form"]/div[2]/button'
            ).click()

driver.close()

print(lista_licitaciones)
print(f"Los productos encontrados en Mercado Público son {lista_productos}")
print(f"Articulos buscados {len(lista_productos)}")
