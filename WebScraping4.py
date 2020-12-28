# some websites require log in and we need to use external source of library

from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://automatetheboringstuff.com')

elem = browser.find_element_by_css_selector('.entry-content > ol:nth-child(15) > li:nth-child(1) > a:nth-child(1)')
elem.click()

elems = browser.find_elements_by_css_selector('p')
print(len(elems))

searchElem = browser.find_element_by_css_selector('.search-field')
searchElem.send_keys('zophie')  # insert text into the specific field
searchElem.submit()

# try these!
browser.back()
browser.forward()
browser.refresh()
browser.quit()

browser = webdriver.Chrome()
browser.get('https://automatetheboringstuff.com')

elem = browser.find_element_by_css_selector('.entry-content > p:nth-child(4)')
print(elem.text)

elem = browser.find_element_by_css_selector('html')     # this will get all the content from the whole website

