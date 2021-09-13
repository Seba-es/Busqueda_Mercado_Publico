from selenium import webdriver
import time
import pandas as pd

# Variables del navegador
ruta_driver = 'A:\chromedriverfor_selenium\chromedriver_win32\chromedriver.exe'
driver = webdriver.Chrome(ruta_driver)
driver.maximize_window() # For maximizing window
driver.implicitly_wait(120) # gives an implicit wait for 20 seconds
web = 'https://www.mercadopublico.cl/TiendaHome/'

# Variables tipos de Convenios Marco
ferreteria = '//*[@id="home-row-no-rs"]/section/div/div[2]/div/a[1]/div'
emergencia = '//*[@id="home-row-no-rs"]/section/div/div[2]/div/a[3]/div'
combustibles = '//*[@id="home-row-no-rs"]/section/div/div[2]/div/a[5]/div'
articulos_escritorio = '//*[@id="home-row-no-rs"]/section/div/div[2]/div/a[7]/div'
alimentos = '//*[@id="home-row-no-rs"]/section/div/div[2]/div/a[9]/div'
otros_convenios = '//*[@id="home-row-no-rs"]/section/div/div[2]/div/a[11]/div' # no puedo buscar aca
aseo = '//*[@id="home-row-no-rs"]/section/div/div[2]/div/a[2]/div'
sofware = '//*[@id="home-row-no-rs"]/section/div/div[2]/div/a[4]/div'
mobiliario = '//*[@id="home-row-no-rs"]/section/div/div[2]/div/a[6]/div'
laptop = '//*[@id="home-row-no-rs"]/section/div/div[2]/div/a[8]/div'
administracion = '//*[@id="home-row-no-rs"]/section/div/div[2]/div/a[10]/div'

#Pandas 
import pandas as pd
df = pd.read_excel('A:\Programación\Python\Pruebas_WebScraping\Búsqueda Mercado Público/Requerimiento_Productos.xlsx')

for filas, datos in df.iterrows():
    index = datos['ID']
    unidad = datos['Unidad']
    nombre_producto = datos['Nombre Producto']
    despacho = datos['Dirección de despacho'] 
    receptor = datos['Receptor del Producto ']       
    licitacion = datos['Convenio Marco ']
    pagina_web = datos['Link']
    
    # Búsqueda de productos
    if licitacion == 'Articulos de Escritorio':
        driver.get(web)
        tipo_convenio_marco = driver.find_element_by_xpath(articulos_escritorio).click()
        producto = driver.find_element_by_xpath('//*[@id="search"]')
        producto.send_keys(nombre_producto)
        boton_buscar = driver.find_element_by_xpath('//*[@id="search_mini_form"]/div[2]/button').click()
    
    elif licitacion == 'Ferreteria':
        cambiar_seccion = driver.find_element_by_xpath('//*[@id="store"]').click()
        selecionar = driver.find_element_by_xpath('//*[@id="store"]/option[1]').click()
        producto = driver.find_element_by_xpath('//*[@id="search"]')
        producto.clear()    
        producto.send_keys(nombre_producto)
        boton_buscar = driver.find_element_by_xpath('//*[@id="search_mini_form"]/div[2]/button').click()
        
    elif licitacion == 'Emergencias':
        cambiar_seccion = driver.find_element_by_xpath('//*[@id="store"]').click()
        selecionar = driver.find_element_by_xpath('//*[@id="store"]/option[3]').click()
        producto = driver.find_element_by_xpath('//*[@id="search"]')
        producto.clear()    
        producto.send_keys(nombre_producto)
        boton_buscar = driver.find_element_by_xpath('//*[@id="search_mini_form"]/div[2]/button').click()
        
    elif licitacion == 'Combustibles':
        cambiar_seccion = driver.find_element_by_xpath('//*[@id="store"]').click()
        selecionar = driver.find_element_by_xpath('//*[@id="store"]/option[4]').click()
        producto = driver.find_element_by_xpath('//*[@id="search"]')
        producto.clear()    
        producto.send_keys(nombre_producto)
        boton_buscar = driver.find_element_by_xpath('//*[@id="search_mini_form"]/div[2]/button').click()
         
    elif licitacion == 'Alimentos':
        cambiar_seccion = driver.find_element_by_xpath('//*[@id="store"]').click()
        selecionar = driver.find_element_by_xpath('//*[@id="store"]/option[9]').click()
        producto = driver.find_element_by_xpath('//*[@id="search"]')
        producto.clear()    
        producto.send_keys(nombre_producto)
        boton_buscar = driver.find_element_by_xpath('//*[@id="search_mini_form"]/div[2]/button').click()
        
    elif licitacion == ' Software':
        cambiar_seccion = driver.find_element_by_xpath('//*[@id="store"]').click()
        selecionar = driver.find_element_by_xpath('//*[@id="store"]/option[5]').click()
        producto = driver.find_element_by_xpath('//*[@id="search"]')
        producto.clear()    
        producto.send_keys(nombre_producto)
        boton_buscar = driver.find_element_by_xpath('//*[@id="search_mini_form"]/div[2]/button').click()

    elif licitacion == ' Mobiliario':
        cambiar_seccion = driver.find_element_by_xpath('//*[@id="store"]').click()
        selecionar = driver.find_element_by_xpath('//*[@id="store"]/option[6]').click()
        producto = driver.find_element_by_xpath('//*[@id="search"]')
        producto.clear()    
        producto.send_keys(nombre_producto)
        boton_buscar = driver.find_element_by_xpath('//*[@id="search_mini_form"]/div[2]/button').click()

    elif licitacion == 'Computadores':
        cambiar_seccion = driver.find_element_by_xpath('//*[@id="store"]').click()
        selecionar = driver.find_element_by_xpath('//*[@id="store"]/option[8]').click()
        producto = driver.find_element_by_xpath('//*[@id="search"]')
        producto.clear()    
        producto.send_keys(nombre_producto)
        boton_buscar = driver.find_element_by_xpath('//*[@id="search_mini_form"]/div[2]/button').click()

    elif licitacion == 'Aseo':
        cambiar_seccion = driver.find_element_by_xpath('//*[@id="store"]').click()
        selecionar = driver.find_element_by_xpath('//*[@id="store"]/option[2]').click()
        producto = driver.find_element_by_xpath('//*[@id="search"]')
        producto.clear()    
        producto.send_keys(nombre_producto)
        boton_buscar = driver.find_element_by_xpath('//*[@id="search_mini_form"]/div[2]/button').click()

    else:
        print(f'La categoria del producto "{producto}" no se encuentra disponible')
 
driver.close()