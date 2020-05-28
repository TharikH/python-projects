from selenium.webdriver import Chrome;
from selenium.webdriver.chrome.options import Options;
from selenium.webdriver.common.keys import Keys;
import urllib;


options = Options()
# option.add_argument("--headless")
options.add_argument("--start-maximized")
options.add_argument("--disable-popup-blocking")
driver=Chrome(executable_path="/home/tharikh/web_scrape/chromedriver",chrome_options=options)
# url=raw_input("Enter url:- ")
url="https://yts.mx/movies/sonic-the-hedgehog-2020"
driver.get(url)
driver.find_element_by_class_name('torrent-modal-download').click()
lis=driver.find_elements_by_class_name('modal-torrent')
details={}
for i in lis:
    temp={}
    temp_arr=i.find_elements_by_class_name('quality-size')
    temp["Size"]=temp_arr[1].text
    temp["magnet-link"]=i.find_element_by_class_name('magnet-download').get_attribute('href')
    if i.find_element_by_tag_name('span').text is not None:
        details[i.find_element_by_tag_name('span').text + i.find_element_by_tag_name('p').text]=temp
    else:
        details[i.find_element_by_tag_name('p').text]=temp
print (details)
try:
    urllib.urlopen(url)
except IOError:
    print "Not a real URL"