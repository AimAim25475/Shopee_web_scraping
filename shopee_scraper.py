#!/usr/bin/env python
# coding: utf-8

# In[97]:


from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def prepare_shopee():
    driver = webdriver.Chrome(executable_path=r'C:\Users\User\Desktop\bootcamp 24\bootcamp 24 class 6\chromedriver.exe')
    driver.get('https://shopee.co.th/')
    thai_button = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[1]/div/div[3]/div[1]/button')
    thai_button.click()
    close_popup = driver.execute_script('return document.querySelector("shopee-banner-popup-stateful").shadowRoot.querySelector("div.shopee-popup__close-btn")')
    close_popup.click()
    return driver


def prepare_data(driver):
    search_bar = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div[1]/div[1]/div/form/input')
    search_bar.click()
    search_bar.send_keys('เก้าอี้ ergonomic')
    search_bar.send_keys(Keys.ENTER)
    driver.execute_script('document.body.style.zoom="10%"')
    return driver


# In[ ]:





# In[98]:


driver = prepare_shopee()
driver = prepare_data(driver)


# In[113]:


import pandas as pd
import bs4
import time

time.sleep(2)
html_string = driver.page_source

soup = bs4.BeautifulSoup(html_string)
all_listing = soup.find_all('div',{'data-sqe':'item'})

name_list = []
price_list = []
for listing in all_listing:

    name = listing.find('div',{'class':'ie3A+n bM+7UW Cve6sh'}).text
    price = listing.find('div',{'class':'hpDKMN'}).text

    name_list.append(name)
    price_list.append(price)


pd.DataFrame([name_list,price_list]).transpose()


# In[119]:


from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def prepare_shopee(chromedriver_path):
    driver = webdriver.Chrome(executable_path=chromedriver_path)
    driver.get('https://shopee.co.th/')
    thai_button = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[1]/div/div[3]/div[1]/button')
    thai_button.click()
    close_popup = driver.execute_script('return document.querySelector("shopee-banner-popup-stateful").shadowRoot.querySelector("div.shopee-popup__close-btn")')
    close_popup.click()
    return driver

def prepare_data(driver,keyword):
    search_bar = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div[1]/div[1]/div/form/input')
    search_bar.click()
    search_bar.send_keys(keyword)
    search_bar.send_keys(Keys.ENTER)
    driver.execute_script('document.body.style.zoom="10%"')
    return driver


# In[120]:


import pyautogui


# In[121]:


keyword = pyautogui.prompt(text='ใส่ keyword ที่ต้องการค้นหา',title='shopee_scraper')
keyword


# In[122]:


chromedriver_path = pyautogui.prompt(text='ใส่ที่อยู่ของไฟล์ chromedriver.exe',title='shopee_scraper')
chromedriver_path


# In[123]:


driver = prepare_shopee(chromedriver_path)
driver = prepare_data(driver,keyword)


# ### checkpont 4

# In[63]:


import pandas as pd
import bs4
import time

time.sleep(2)
html_string = driver.page_source

soup = bs4.BeautifulSoup(html_string)
all_listing = soup.find_all('div',{'data-sqe':'item'})

name_list = []
price_list = []
for listing in all_listing:

    name = listing.find('div',{'class':'ie3A+n bM+7UW Cve6sh'}).text
    price = listing.find('div',{'class':'hpDKMN'}).text

    name_list.append(name)
    price_list.append(price)


pd.DataFrame([name_list,price_list]).transpose()


# ### checkpoint 5

# In[41]:


import pandas as pd
import bs4
import time

def get_shopee_df(driver):
    time.sleep(2)
    html_string = driver.page_source
    soup = bs4.BeautifulSoup(html_string)
    all_listing = soup.find_all('div',{'data-sqe':'item'})

    name_list = []
    price_list = []
    for listing in all_listing:

        name = listing.find('div',{'class':'ie3A+n bM+7UW Cve6sh'}).text
        price = listing.find('div',{'class':'hpDKMN'}).text
        name_list.append(name)
        price_list.append(price)

    shopee_df = pd.DataFrame([name_list,price_list]).transpose()
    return shopee_df
    


# In[42]:


shopee_df = get_shopee_df(driver)
shopee_df


# ### checkpoint 6

# In[64]:


import pandas as pd
import bs4
import time

def get_shopee_df(driver):
    time.sleep(2)
    html_string = driver.page_source
    soup = bs4.BeautifulSoup(html_string)
    all_listing = soup.find_all('div',{'data-sqe':'item'})

    name_list = []
    price_list = []
    sales_list = []
    for listing in all_listing:

        name = listing.find('div',{'class':'ie3A+n bM+7UW Cve6sh'}).text
        price = listing.find('div',{'class':'hpDKMN'}).text
        sales = listing.find('div',{'class':'r6HknA'}).text
        
        name_list.append(name)
        price_list.append(price)

    shopee_df = pd.DataFrame([name_list,price_list,sales_list]).transpose()
    return shopee_df


# In[66]:


shopee_df = get_shopee_df(driver)
shopee_df


# ### checkpoint 7 ตั้งชื่อ column
# 

# In[67]:


shopee_df.columns = ['product','price','sales']
shopee_df


# ### checkpoint 8 ตั้ง product เป็น index

# In[68]:


shopee_df = shopee_df.set_index('product')
shopee_df


# ### checkpoint 9 รวมคำสั่งไว้ใน cell เดียวกัน

# In[138]:


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd
import bs4
import time

def prepare_shopee(chromedriver_path):
    driver = webdriver.Chrome(executable_path=chromedriver_path)
    driver.get('https://shopee.co.th/')
    thai_button = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[1]/div/div[3]/div[1]/button')
    thai_button.click()
    close_popup = driver.execute_script('return document.querySelector("shopee-banner-popup-stateful").shadowRoot.querySelector("div.shopee-popup__close-btn")')
    close_popup.click()
    return driver

def prepare_data(driver,keyword):
    search_bar = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div[1]/div[1]/div/form/input')
    search_bar.click()
    search_bar.send_keys(keyword)
    search_bar.send_keys(Keys.ENTER)
    driver.execute_script('document.body.style.zoom="10%"')
    return driver

def get_shopee_df(driver):
    time.sleep(2)
    html_string = driver.page_source
    soup = bs4.BeautifulSoup(html_string)
    all_listing = soup.find_all('div',{'data-sqe':'item'})

    name_list = []
    price_list = []
    sales_list = []
    for listing in all_listing:

        name = listing.find('div',{'class':'ie3A+n bM+7UW Cve6sh'}).text
        price = listing.find('div',{'class':'hpDKMN'}).text
        sales = listing.find('div',{'class':'r6HknA'}).text
        
        name_list.append(name)
        price_list.append(price)
        sales_list.append(sales)

    shopee_df = pd.DataFrame([name_list,price_list,sales_list]).transpose()
    return shopee_df


# ### checkpoint 10 การใช้งานคำสั่งต่างๆ และบันทึกตารางเป็นไฟล์ excel

# In[125]:


import pyautogui

keyword = pyautogui.prompt(text='ใส่ keyword ที่ต้องการค้นหา',title='shopee_scraper')
chromedriver_path = pyautogui.prompt(text='ใส่ที่อยู่ของไฟล์ chromedriver.exe',title='shopee_scraper')

driver = prepare_shopee(chromedriver_path)
driver = prepare_data(driver,keyword)

shopee_df = get_shopee_df(driver)

shopee_df.columns = ['product','price','sales']
shopee_df = shopee_df.set_index('product')
shopee_df.to_excel(keyword+' shopee.xlsx')


# ### checkpoint 11 การสร้าง main คำสั่งเรียกใช้ฟังก์ชัน

# In[100]:


def main():
    keyword = pyautogui.prompt(text='ใส่ keyword ที่ต้องการค้นหา',title='shopee_scraper')
    chromedriver_path = pyautogui.prompt(text='ใส่ที่อยู่ของไฟล์ chromedriver.exe',title='shopee_scraper')
    
    
    driver = prepare_shopee(chromedriver_path)
    driver = prepare_data(driver,keyword)
    
    shopee_df = get_shopee_df(driver)

    shopee_df.columns = ['product','price','sales']
    shopee_df = shopee_df.set_index('product')
    shopee_df.to_excel(keyword+' shopee.xlsx')


# In[126]:


main()


# In[142]:


#!/usr/bin/env python
# coding: utf-8

# checkpoint 1 

#In[32]:

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def prepare_shopee(chromedriver_path):
    driver = webdriver.Chrome(executable_path=chromedriver_path)
    driver.get('https://shopee.co.th/')
    thai_button = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[1]/div/div[3]/div[1]/button')
    thai_button.click()
    close_popup = driver.execute_script('return document.querySelector("shopee-banner-popup-stateful").shadowRoot.querySelector("div.shopee-popup__close-btn")')
    close_popup.click()
    return driver

def prepare_data(driver,keyword):
    search_bar = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div[1]/div[1]/div/form/input')
    search_bar.click()
    search_bar.send_keys('เก้าอี้ ergonomic')
    search_bar.send_keys(Keys.ENTER)
    driver.execute_script('document.body.style.zoom="10%"')
    return driver

def get_shopee_df(driver):
    time.sleep(2)
    html_string = driver.page_source
    soup = bs4.BeautifulSoup(html_string)
    all_listing = soup.find_all('div',{'data-sqe':'item'})

    name_list = []
    price_list = []
    sales_list = []
    for listing in all_listing:

        name = listing.find('div',{'class':'ie3A+n bM+7UW Cve6sh'}).text
        price = listing.find('div',{'class':'hpDKMN'}).text
        sales = listing.find('div',{'class':'r6HknA'}).text
        
        name_list.append(name)
        price_list.append(price)
        sales_list.append(sales)

    shopee_df = pd.DataFrame([name_list,price_list,sales_list]).transpose()
    return shopee_df

def main():
    keyword = pyautogui.prompt(text='ใส่ keyword ที่ต้องการค้นหา',title='shopee_scraper')
    chromedriver_path = pyautogui.prompt(text='ใส่ที่อยู่ของไฟล์ chromedriver.exe',title='shopee_scraper')
    
    
    driver = prepare_shopee(chromedriver_path)
    driver = prepare_data(driver,keyword)
    
    shopee_df = get_shopee_df(driver)

    shopee_df.columns = ['product','price','sales']
    shopee_df = shopee_df.set_index('product')
    shopee_df.to_excel(keyword+' shopee.xlsx')

if __name__ == "__main__":
    main()


# In[ ]:





# In[ ]:





# In[ ]:




