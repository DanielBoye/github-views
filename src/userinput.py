from selenium import webdriver
from selenium.webdriver.common.by import By

username = input("Write your username: ")
github = "https://github.com/" 

times = int(input("How many times do you want it to refresh?: "))
    
with webdriver.Chrome() as driver: 
    print(f"\nGetting {username}\n")
    
    driver.get(github + username)
    driver.implicitly_wait(3)
    
    for i in range(times):
        driver.refresh()
        i+1
    print("Exiting program")