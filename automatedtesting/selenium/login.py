# #!/usr/bin/env python
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions

def login ( user, password):
    print ('Starting the browser...')
  #  options = ChromeOptions()
  #  options.add_argument('--no-sandbox')
  #  options.add_argument("--headless")
  #  driver = webdriver.Chrome(options=options)
    options = webdriver.ChromeOptions()
    options.add_argument("--no-sandbox")
    options.add_argument("--remote-debugging-port=9222")
    options.headless = True
    driver = webdriver.Chrome("chromedriver", options=options)
    print ('Browser started successfully. Navigating to the demo page to login.')
    url = 'https://www.saucedemo.com/'
    print('Navigating to ' + url)
    driver.get(url)
    driver.find_element_by_css_selector("input[id='user-name']").send_keys(user)
    driver.find_element_by_css_selector("input[id='password']").send_keys(password)
    driver.find_element_by_id("login-button").click()
    print('login succeded as ' + user)
    return driver

def add_to_cart (driver):
    totalNoOfItems = '6'
    itemsAdded = 0

    items = driver.find_elements_by_css_selector("div.inventory_item")

    while totalNoOfItems != str(int(itemsAdded)):
        item_button = items[itemsAdded].find_element_by_tag_name("button")
        item_button.click()
        print("Added item " + items[itemsAdded].find_element_by_css_selector(".inventory_item_name").text + " to cart")
        itemsAdded = itemsAdded + 1
    assert '6' in str(int(itemsAdded))
    print('Total items added to cart :' + str(int(itemsAdded)))
    #print('Added {} to cart'.format(item_name))

def remove_from_cart (driver):
    itemsRemoved = 0
    totalNoOfItems = '6'

    items = driver.find_elements_by_css_selector("div.inventory_item")

    while totalNoOfItems != str(int(itemsRemoved)):
        item_button = items[itemsRemoved].find_element_by_tag_name("button")
        item_button.click()
        print("removed item " + items[itemsRemoved].find_element_by_css_selector(".inventory_item_name").text + " to cart")
        itemsRemoved = itemsRemoved + 1
    assert "6" in str(int(itemsRemoved))
    print('All iteams are removed from cart')

if __name__ == "__main__":
    driver = login('standard_user', 'secret_sauce')
    print('add items to cart')
    add_to_cart(driver)
    print("remove items from cart")
    remove_from_cart(driver)
    print("complete")


#
#
# # #!/usr/bin/env python
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options as ChromeOptions
# import logging
# logging.basicConfig(
#     format='%(asctime)s %(levelname)-8s %(message)s',
#     level=logging.INFO,
#     datefmt='%Y-%m-%d %H:%M:%S')
#
# def login ( user, password):
#     logging.info ('Starting the browser...')
#     #  options = ChromeOptions()
#     #  options.add_argument('--no-sandbox')
#     #  options.add_argument("--headless")
#     #  driver = webdriver.Chrome(options=options)
#     options = webdriver.ChromeOptions()
#     #    options.add_argument("--no-sandbox")
#     #    options.add_argument("--remote-debugging-port=9222")
#     #    options.headless = True
#     driver = webdriver.Chrome("chromedriver", options=options)
#     logging.info ('Browser started successfully. Navigating to the demo page to login.')
#     url = 'https://www.saucedemo.com/'
#     logging.info('Navigating to ' + url)
#     driver.get(url)
#     driver.find_element_by_css_selector("input[id='user-name']").send_keys(user)
#     driver.find_element_by_css_selector("input[id='password']").send_keys(password)
#     driver.find_element_by_id("login-button").click()
#     logging.info('login succeded as ' + user)
#     return driver
#
# def add_to_cart (driver):
#     totalNoOfItems = '6'
#     itemsAdded = 0
#
#     items = driver.find_elements_by_css_selector("div.inventory_item")
#
#     while totalNoOfItems != str(int(itemsAdded)):
#         item_button = items[itemsAdded].find_element_by_tag_name("button")
#         item_button.click()
#         logging.info("Added item " + items[itemsAdded].find_element_by_css_selector(".inventory_item_name").text + " to cart")
#         itemsAdded = itemsAdded + 1
#     assert '6' in str(int(itemsAdded))
#     logging.info('Total items added to cart :' + str(int(itemsAdded)))
#
# def remove_from_cart (driver):
#     itemsRemoved = 0
#     totalNoOfItems = '6'
#
#     items = driver.find_elements_by_css_selector("div.inventory_item")
#
#     while totalNoOfItems != str(int(itemsRemoved)):
#         item_button = items[itemsRemoved].find_element_by_tag_name("button")
#         item_button.click()
#         logging.info("removed item " + items[itemsRemoved].find_element_by_css_selector(".inventory_item_name").text + " to cart")
#         itemsRemoved = itemsRemoved + 1
#     assert "6" in str(int(itemsRemoved))
#     logging.info('All iteams are removed from cart')
#
# if __name__ == "__main__":
#     driver = login('standard_user', 'secret_sauce')
#     logging.info('add items to cart')
#     add_to_cart(driver)
#     logging.info("remove items from cart")
#     remove_from_cart(driver)
#     logging.info("complete")

