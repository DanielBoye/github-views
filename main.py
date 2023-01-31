from selenium import webdriver
from selenium.webdriver.common.by import By

username = input("Write your username: ")
github = "https://github.com/" 

# username = "DanielBoye"
    
with webdriver.Chrome() as driver: 
    print(f"\nGetting {username}\n")
    
    driver.get(github + username)
    driver.implicitly_wait(3)
    
    for i in range(20):
        driver.refresh()
        i+1
    print("Exiting program")
