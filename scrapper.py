from csv import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located

#This example requires Selenium WebDriver 3.13 or newer
with webdriver.Firefox() as driver:
# open file in read mode
with open('temp.csv', 'r') as read_obj:
    with open('output.csv', 'w') as write_obj:
        # create a csv reader object
        csv_reader = reader(read_obj)
        # create a csv writer object
        csv_writer = writer(write_obj)
        # write header
        csv_writer.writerow(next(csv_reader))
        # write all rows
        for row in csv_reader:
            if row[5] == '#N/A':

                break;
            csv_writer.writerow(row)