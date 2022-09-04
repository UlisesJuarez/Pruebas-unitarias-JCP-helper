from cgitb import text
from selenium import webdriver
from selenium.webdriver.common.by import By



texto=input("Ingrese el programa a compilar: ")

driver = webdriver.Chrome("C:/wdm/chromedriver.exe")

driver.get("https://www.programiz.com/python-programming/online-compiler/")



consola = driver.find_element(by=By.CLASS_NAME, value="ace_content")
boton= driver.find_element(by=By.CLASS_NAME, value="desktop-run-button")
consola.send_keys(texto)

boton.click()