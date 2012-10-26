#!/usr/bin/env python
"""
To use this script you need to install selenium:
 * pip install selenium
 
And put the chromedriver on your PATH:
  http://code.google.com/p/selenium/wiki/ChromeDriver
  
Extension: 
    Make sure to update the path to the webscript extension.
    It needs to be packaged extension.
"""
from selenium import webdriver

PATH_TO_EXT = '/Users/king/proj/webscript.crx'


def main(url, webscript_ext):

    co = webdriver.ChromeOptions()
    co.add_extension(webscript_ext)
    driver = webdriver.Chrome(chrome_options=co)

    # Grab replay window
    driver.switch_to_window(driver.window_handles[1])

    # Grab useful buttons
    start = driver.find_element_by_id('start')
    stop = driver.find_element_by_id('stop')
    replay = driver.find_element_by_id('replay')

    # Start recording
    start.click()

    # Grab the newly created window
    driver.switch_to_window(driver.window_handles[2])
    driver.set_window_size(800, 600)

    # Switch to main window
    driver.switch_to_window(driver.window_handles[0])

    ###########################################
    # Script to driving navigation of webpage
    driver.get(url)

    search = driver.find_element_by_name("q")
    search.send_keys("This is a test of selenium")
    search.submit()

    ###########################################
    # Stop Recording
    driver.switch_to_window(driver.window_handles[1])
    stop.click()

if __name__ == '__main__':
    main('http://www.google.com/', PATH_TO_EXT)
