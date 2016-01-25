from selenium import webdriver

browser = webdriver.Firefox()
print (browser.firefox_profile.path)
browser.get('http://localhost:8000')

assert 'Django' in browser.title
