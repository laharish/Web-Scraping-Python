from selenium import webdriver
import socketserver
from selenium.common.exceptions import NoSuchElementException
import os
import time
import os
import shutil
import filehandling


path_to_chromedriver = 'L:\Python\chromedriver_win32\chromedriver.exe' # change path as needed
browser = webdriver.Chrome(executable_path = path_to_chromedriver)
    #Chrome(executable_path = path_to_chromedriver)


url = 'http://proxy.lib.iastate.edu/login?url=http://proxy.lib.iastate.edu/login?url=http://www.lexisnexis.com/us/lnacademic'
browser.get(url)
time.sleep(2)


time.sleep(2)

with open('L:\company.txt') as f:
    lines = f.readlines()

for f in lines:
    f = f.rstrip('\n')
    text_file = open("L:/Count.txt",'a')
    text_file.write(f+'\t')

    for x in range(2010,2015):
        y = '01/01/'+str(x)
        z = '12/31/'+str(x)
        time.sleep(2)
        browser.switch_to_frame('mainFrame')
        browser.find_element_by_xpath('//*[@id="lblAdvancDwn"]').click()
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="selectAll"]').click()
        time.sleep(2)
        if(f=='Accordant Health' and x==2010):
            time.sleep(20)
        browser.find_element_by_id('txtFrmDate').clear()
        browser.find_element_by_id('txtFrmDate').send_keys(y)
        browser.find_element_by_id('txtToDate').clear()
        browser.find_element_by_id('txtToDate').send_keys(z)
        browser.find_element_by_xpath('//*[@id="OkButt"]').click()
        browser.find_element_by_id('terms')
        browser.find_element_by_id('terms').clear()
        browser.find_element_by_id('terms').send_keys(f)

        try:

            browser.find_element_by_xpath('//*[@id="srchButt"]').click()
            time.sleep(2)
            browser.switch_to_default_content()
            browser.switch_to_frame('mainFrame')
            dyn_frame = browser.find_element_by_xpath('//frame[contains(@name, "fr_resultsNav")]')
            time.sleep(2)
            framename = dyn_frame.get_attribute('name')
            browser.switch_to_frame(framename)
            browser.find_element_by_xpath('//*[@id="deliveryContainer"]/table/tbody/tr/td[6]/table/tbody/tr/td[1]/table/tbody/tr/td/a[3]/img').click()
            time.sleep(2)
            browser.switch_to_window(browser.window_handles[1])
            time.sleep(2)
            x=browser.find_element_by_xpath('//*[@id="docText"]').text
            text_file.write(x[19:len(x)-1]+"\t")
            browser.find_element_by_xpath('//*[@id="docText"]').click()
            time.sleep(2)
            count1 = str(count) + '-' + str(count)
            count = count+1
            browser.find_element_by_id('rangetextbox').send_keys(count1)
            browser.close()
            time.sleep(2)
            browser.switch_to_window(browser.window_handles[0])
            time.sleep(2)
            browser.find_element_by_xpath('//*[@id="restoreButtons"]/a[2]').click()


        except:
            time.sleep(2)
            text_file.write("0"+'\t')
            browser.switch_to_window(browser.window_handles[0])
            time.sleep(2)
            browser.find_element_by_xpath('//*[@id="restoreButtons"]/a[2]').click()

    text_file.write('\n')
    text_file.close()





