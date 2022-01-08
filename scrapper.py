from csv import *
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located

i = 0

# profile = webdriver.FirefoxProfile()
# profile.add_extension('amazon_ad_blocker-0.4-an+fx.xpi')
# option = webdriver.FirefoxOptions()
# option.add_extension('amazon_ad_blocker-0.4-an+fx.xpi')

with open('Eng2.csv', 'r', newline='', encoding='ISO-8859-1') as read_obj:
    with open('frombeg.csv', 'w') as write_obj:
        csv_reader = reader(read_obj)
        csv_writer = writer(write_obj)
        csv_writer.writerow(next(csv_reader))
        for row in csv_reader:
            # i += 1
            # if i < 2234:
            #     continue
            if row[7] == '#N/A':
                copy = row.copy()
                try:
                    with webdriver.Firefox() as firefox:
                        # try:
                        # firefox.install_addon('/home/reshyurem/Web-Scraping/adblocker_ultimate-3.7.15-an+fx.xpi')
                        firefox.install_addon('/home/reshyurem/Web-Scraping/ublock_origin-1.39.2-an+fx.xpi')
                        # except Exception as e:
                        #     print(e)

                        # i += 1
                        # if i > 5:
                        #     break
                        firefox.get("https://www.amazon.in/")
                        # time.sleep(2000)
                        assert "Amazon" in firefox.title
                        searchbox = firefox.find_element(
                            by="id", value="twotabsearchtextbox")
                        searchbox.clear()
                        searchbox.send_keys(row[1] + " by " + row[2])
                        searchbox.submit()
                        time.sleep(4)
                        # time.sleep(2000)
                        i = 1
                        while (i < 6):
                            try:
                                link = firefox.find_element(by="xpath", value="/html/body/div[1]/div[2]/div[1]/div[1]/div/span[3]/div[2]/div[" + str(i) + "]/div/span/div/div/div[2]/div[2]/div/div/div[1]/h2/a")
                                break
                            except:
                                i += 1
                        # try:
                        #     link = firefox.find_element(by="xpath", value="/html/body/div[1]/div[2]/div[1]/div[1]/div/span[3]/div[2]/div[1]/div/span/div/div/div[2]/div[2]/div/div/div[1]/h2/a")
                        # except:
                        #     link = firefox.find_element(by="xpath", value="/html/body/div[1]/div[2]/div[1]/div[1]/div/span[3]/div[2]/div[2]/div/span/div/div/div[2]/div[2]/div/div/div[1]/h2/a")
                        link.click()
                        firefox.switch_to.window(firefox.window_handles[1])
                        time.sleep(4)
                        try:
                            ISBN = firefox.find_element(by="xpath", value="//*[contains(text(), 'ISBN-13')]/following-sibling::*[1]")
                            row[7] = ISBN.text
                        except Exception as e:
                            print(copy[1])
                            print(e)
                            row[7] = copy[7]
                        # time.sleep(2000)
                        # try:
                        #     Page = firefox.find_element(by="xpath", value="//*[contains(text(), 'pages')]")
                        #     row[9] = Page.text
                        # except Exception as e:
                        #     print(copy[1])
                        #     print(e)
                        #     row[9] = copy[9]
                        # try:
                        #     Pub = firefox.find_element(by="xpath", value="//*[contains(text(), 'Publisher')]/following-sibling:span[1]")
                        #     row[8] = Pub.text
                        # except Exception as e:
                        #     print(copy[1])
                        #     print(e)
                        #     row[8] = copy[8]
                        # try:
                        #     Price = firefox.find_element(by="xpath", value="//span[contains(text(), '₹')]")
                        #     row[7] = Price.text
                        # except Exception as e:
                        #     print(copy[1])
                        #     print(e)
                        #     row[7] = copy[7]
                            # try:
                            #     ISBN = firefox.find_element(by="xpath", value="/html/body/div[2]/div[2]/div[3]/div[20]/div/div[1]/ul/li[5]/span/span[2]")
                            #     row[5] = ISBN.text
                            # except:
                            #     row[5] = copy[5]
                            # try:
                            #     Page = firefox.find_element(by="xpath", value="/html/body/div[2]/div[2]/div[3]/div[20]/div/div[1]/ul/li[3]/span/span[2]")
                            #     row[9] = Page.text
                            # except:
                            #     row[9] = copy[9]
                            # try:
                            #     Pub = firefox.find_element(by="xpath", value="/html/body/div[2]/div[2]/div[3]/div[1]/div[5]/div[29]/div/div/div/div/div[2]/div/ol/li[4]/div/div[3]/span")
                            #     row[8] = Pub.text
                            # except:
                            #     row[8] = copy[8]
                            # try:
                            #     Price = firefox.find_element(by="xpath", value="/html/body/div[2]/div[2]/div[3]/div[1]/div[3]/div[2]/div/form/div[1]/div/div/div/div[1]/div/div/span")
                            #     row[7] = Price.text
                            # except:
                            #     row[7] = copy[7]
                except:
                    row = copy.copy()
            csv_writer.writerow(row)