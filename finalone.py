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

#sos.mkdir("L:/Scraping")

url = 'http://proxy.lib.iastate.edu/login?url=http://proxy.lib.iastate.edu/login?url=http://www.lexisnexis.com/us/lnacademic'
browser.get(url)
time.sleep(120)
browser.switch_to_frame('mainFrame')
#time.sleep(1)
browser.find_element_by_xpath('//*[@id="lblAdvancDwn"]').click()
time.sleep(20)
browser.find_element_by_id('txtFrmDate').clear()
browser.find_element_by_id('txtFrmDate').send_keys('01/01/2010')
#time.sleep(1)
browser.find_element_by_id('txtToDate').clear()
browser.find_element_by_id('txtToDate').send_keys('06/12/2015')
browser.find_element_by_xpath('//*[@id="lblSlctAll"]').click()
#time.sleep(1)
browser.find_element_by_xpath('//*[@id="OkButt"]').click()
time.sleep(1)



with open('L:\company.txt') as f:
    lines = f.readlines()

for f in lines:
    f = f.rstrip('\n')
    #os.mkdir("L:/Scraping/"+f)
    #os.mkdir("L:/Scraping/"+f+"/2014")
    if(f!='AB Volvo'):
        browser.switch_to_frame('mainFrame')
        browser.find_element_by_xpath('//*[@id="lblAdvancDwn"]').click()
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="selectAll"]').click()
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="OkButt"]').click()

    #time.sleep(1)
    #browser.find_element_by_xpath('//*[@id="lblAdvancDwn"]').click()
    #time.sleep(20)
    #browser.find_element_by_id('txtFrmDate').clear()
    #browser.find_element_by_id('txtFrmDate').send_keys('01/01/2014')
    #time.sleep(1)
    #browser.find_element_by_id('txtToDate').clear()
    #browser.find_element_by_id('txtToDate').send_keys('12/31/2014')
    #time.sleep(1)
    #browser.find_element_by_xpath('//*[@id="OkButt"]').click()
    #time.sleep(1)
    browser.find_element_by_id('terms')
    #time.sleep(1)
    browser.find_element_by_id('terms').clear()
    #time.sleep(1)
    browser.find_element_by_id('terms').send_keys(f)
    #time.sleep(1)
    try:
        count = 1
        print(count)
        browser.find_element_by_xpath('//*[@id="srchButt"]').click()
        time.sleep(1)
        browser.switch_to_default_content()
        browser.switch_to_frame('mainFrame')
        #time.sleep(1)

        while(count>0):
            time.sleep(1)
            browser.switch_to_default_content()
            browser.switch_to_frame('mainFrame')
            dyn_frame = browser.find_element_by_xpath('//frame[contains(@name, "fr_resultsNav")]')
            #time.sleep(1)
            framename = dyn_frame.get_attribute('name')
            #time.sleep(1)
            browser.switch_to_frame(framename)
            #time.sleep(1)
            browser.find_element_by_xpath('//*[@id="deliveryContainer"]/table/tbody/tr/td[6]/table/tbody/tr/td[1]/table/tbody/tr/td/a[3]/img').click()
            time.sleep(1)
            browser.switch_to_window(browser.window_handles[1])
            time.sleep(1)
            browser.find_element_by_xpath('//*[@id="docText"]').click()
            time.sleep(1)
            count1 = str(count) + '-' + str(count)
            browser.find_element_by_id('rangetextbox').send_keys(count1)
            #time.sleep(1)
            browser.find_element_by_id("delFmt")
            browser.find_element_by_xpath('//*[@id="delFmt"]/option[4]').click()
            time.sleep(1)
            browser.find_element_by_xpath('//*[@id="img_orig_bottom"]/a/img').click()
            time.sleep(4)


            #for file in os.listdir('C:/Users/Admin1/Downloads'):
            #    if file.endswith(".TXT"):
            #        file1 = "IBM-CIO-2014-" + str(count) + '.txt'
            #        shutil.move('C:/Users/Admin1/Downloads/'+file, "L:/Scraping/"+f+"/2014/"+file1)






            try:
                browser.find_element_by_xpath('//*[@id="center"]/center/p/a').click()
                time.sleep(4)
                filehandling.file(f,'2014',count)
                #time.sleep(1)
                browser.close()
                count = count+1
                browser.switch_to_window(browser.window_handles[0])

            except:

                count = 0
                browser.close()
                time.sleep(1)
                browser.switch_to_window(browser.window_handles[0])
                time.sleep(1)
                browser.find_element_by_xpath('//*[@id="restoreButtons"]/a[2]').click()

    except:
        time.sleep(1)
        print(count)
        browser.switch_to_window(browser.window_handles[0])
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="restoreButtons"]/a[2]').click()






