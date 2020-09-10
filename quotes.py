from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
import time
import sys
import os

path = os.getcwd()
chrome_driver_path = '{path}/chromedriver'.format(path=path)

url = 'https://www.brainyquote.com/'

chrome_options = Options()
chrome_options.add_argument('--headless')

webdriver = webdriver.Chrome(
    executable_path=chrome_driver_path, options=chrome_options
)

category = """ -- Pilih kategori --
[*] Motivational
[*] Positive
[*] Attitude
[*] Life
[*] Love
[*] Beauty
[*] Smile
[*] Funny
[*] Wisdom """

print(category)


# default search query
input_user = input("[*] Masukan pilihan (Life) : ")
search_query = input_user

print()

if (len(sys.argv) >= 2):
    search_query = sys.argv[1]
    print(search_query)


with webdriver as driver:
    # Set timeout time
    wait = WebDriverWait(driver, 10)

    # retrive url in headless browser
    driver.get(url)

    # find search box
    search = driver.find_element_by_id("hmSearch")
    search.send_keys(search_query + Keys.RETURN)

    wait.until(presence_of_element_located((By.ID, "quotesList")))
    # time.sleep(3)
    results = driver.find_elements_by_class_name('m-brick')
    # store quotes
    store_quotes = []

    for quote in results:
        quoteArr = quote.text.split('\n')

        store_quotes.append(quoteArr)

        print(quoteArr)

        print()

    # must close the driver after task finished
    driver.close()

# write to text
for i, item in enumerate(store_quotes):
    with open("quotes.txt", 'a') as f:
        f.write("{}\n".format(str(store_quotes[i])[1:-1]))
