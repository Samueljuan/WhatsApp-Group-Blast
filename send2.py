from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from tkinter import messagebox
from config import chrome_path
import pyperclip 
import time
import csv


def Send(file,poster, modal):
    options = webdriver.ChromeOptions()
    options.add_argument(chrome_path) #you can directly write the path in this file
    options.add_experimental_option("detach",True)
    browser = webdriver.Chrome(options=options)

    browser.maximize_window()
    browser.get('https://web.whatsapp.com/')


    with open (f'{file}', encoding='utf-8-sig') as f:
        groups = csv.reader (f,delimiter=';')
        for group in groups:
            search_xpath = '//*[@id="side"]/div[1]/div/div[2]/div[2]/div/div'

            search_box = WebDriverWait(browser, 500000).until(
                EC.presence_of_element_located((By.XPATH, search_xpath))
            )
            search_box.clear()
            time.sleep(5)

            pyperclip.copy(group[0])
            search_box.send_keys(Keys.SHIFT, Keys.INSERT)
            time.sleep(2)

            try:
                group_xpath = f'//span[@title="{group[0]}"]'
                group_title = browser.find_element(By.XPATH, group_xpath)
                
                group_title.click()
                time.sleep(2)
                
                input_xpath = '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]'
                input_box = browser.find_element(By.XPATH,input_xpath)

                pyperclip.copy(group[1])
                input_box.send_keys(Keys.SHIFT, Keys.INSERT)

                time.sleep(3)

                attachment_box = browser.find_element(By.XPATH,'//div[@title="Attach"]')
                attachment_box.click()
                time.sleep(3)

                image_box = browser.find_element(By.XPATH,
                    '//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]'
                    )
                image_box.send_keys(poster)
                time.sleep(3)

                send_btn = browser.find_element(By.XPATH,
                    '//span[@data-icon="send"]'
                    )
                send_btn.click()
                time.sleep(3)
            except NoSuchElementException:
                clear = messagebox.askyesno("ERROR", f'Error: Tidak Ditemukan Group dengan Nama "{group[0]}" \n \nMau melanjutkan Blast?', icon = 'error')
                if clear:
                    modal.update()
                    clear_search_xpath='//*[@id="side"]/div[1]/div/div[2]/button'
                    clear_search=browser.find_element(By.XPATH,clear_search_xpath)
                    clear_search.click()
                else:
                    browser.close()
        end=messagebox.showinfo(title="PROSES", message="Pesan telah terkirim semua!")
        if end:
            browser.close()