
# coding: utf-8

# In[2]:


from selenium import webdriver
from selenium.webdriver.common.by import By


# In[47]:



pw = input()
browser = webdriver.Chrome()
url = 'https://sso.uvt.nl/login'
squash_url = 'https://dmsonline.uvt.nl/nl/auth/connect_uvt'
bookings_url = 'https://dmsonline.uvt.nl/nl/bookings/view/advanced'
browser.get(url)
browser.find_element_by_id('username').send_keys('u868978')
browser.find_element_by_id('password').send_keys(pw)
browser.find_element_by_name('login').click()
browser.get(squash_url)
#browser.find_element_by_xpath("//*[@class='a.result.active.access.focussed']").click()
browser.find_element_by_link_text('Tilburg University').click()
browser.get(bookings_url)



