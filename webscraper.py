from selenium import webdriver 

url = 'https://www.youtube.com/@shetheseriesdmv'
browser = webdriver.Chrome()
browser.get(url)

browser.find_element_by_xpath('//*[@id="thumbnail"]').click()
