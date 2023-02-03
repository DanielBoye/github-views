from selenium import webdriver
from selenium.webdriver.common.by import By

github = "https://github.com/" 

# Edit these two variables 
username = "DanielBoye" # your username
times = 20 # how many times it should refesh 
    
with webdriver.Chrome() as driver: 
    print(f"\nGetting {username}\n")
    
    driver.get(github + username)
    driver.implicitly_wait(3)
    
    for i in range(times):
        driver.refresh()
        i+1
    print("Exiting program")
