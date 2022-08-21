from functools import cache
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome import service as fs
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from os.path import join

root = join(__file__, "..")

# webdriverオブジェクトを作る（ブラウザが開く）
driver_path=join(root, "chromedriver.exe")

# 起動時にオプションをつける。（ポート指定により、起動済みのブラウザのドライバーを取得）
options = webdriver.ChromeOptions()
options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
chrome_service = fs.Service(executable_path=driver_path)
driver = webdriver.Chrome(service=chrome_service, options=options)

# ページのタイトルを表示する
print(driver.title)
print("========== source ========== ")

print("execute watch do yes man")
few_a_wait=True
while True:
    sleep(2)
    try:
        elm = driver.find_element(by=By.XPATH, value="//button[contains(., 'OK')]")
        if few_a_wait:
            print("few_a_wait")
            few_a_wait=False
            continue
        few_a_wait=True
        elm.click()
        print("do checking yes")
    except Exception as e:
        pass
