from selenium import webdriver
from selenium.webdriver.common.by import By

username = input("Write your username: ")
github = "https://github.com/" 

# https://github.com/DanielBoye
    
with webdriver.Chrome() as driver: 
    print(f"\nGetting {username}\n\n")
    
    driver.get(github + username)
    driver.implicitly_wait(3)
    
    for i in range(20):
        driver.refresh()
        print("Refreshed: ", i+1)
