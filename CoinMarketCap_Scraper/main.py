import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
from datetime import datetime

options = webdriver.ChromeOptions()

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

try:
    driver.get("https://coinmarketcap.com/")
    time.sleep(5)
    coins = []
    rows = driver.find_elements(By.XPATH, "//table/tbody/tr")[0:10]

    for row in rows:
        name = row.find_element(By.XPATH, ".//td[3]").text
        price = row.find_element(By.XPATH, ".//td[4]").text

        coins.append({
            "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "Name": name.split('\n')[0],
            "Price": price
        })

    df = pd.DataFrame(coins)
    df.to_csv("crypto_data.csv", mode='a', index=False, header=not pd.io.common.file_exists("crypto_data.csv"))
    print("Data saved successfully to crypto_data.csv!")

finally:
    driver.quit()
