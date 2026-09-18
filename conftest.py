import pytest
from selenium import webdriver

NAVEGADOR="Chrome"

@pytest.fixture()
def navegador():
    if NAVEGADOR=="Chrome":
       driver=webdriver.Chrome()
    elif NAVEGADOR=="Firefox": 
         driver=webdriver.Firefox()
    elif NAVEGADOR=="Edge":
         driver=webdriver.Edge()
    else:
        raise Exception(f"Navegador {NAVEGADOR} no soportado")
    driver.maximize_window()
    driver.get("https://the-internet.herokuapp.com/login")
    yield driver
    driver.quit()