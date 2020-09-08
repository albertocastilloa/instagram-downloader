#Call dependencies
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time
import urllib.request
import string
import random

#Start browser
#Headless mode ON
options = Options()
options.headless = True
driver = webdriver.Firefox(options = options, executable_path='/usr/local/bin/geckodriver')

def get_random_name():
    return ''.join(random.choice(string.ascii_letters) for x in range(random.randint(5,15)))

#Posts metadata
def get_content(link):
    """
    Get post image, description and links
    """
    img_directory = 'static/downloads/images/'
    video_directory = 'static/downloads/videos/'

    filename = get_random_name()

    time.sleep(5)
 
    #Navigate URL
    driver.get(link)
    try:
        #Find metadata
        media_type = driver.find_element_by_xpath("//meta[@property='og:type']").get_attribute("content")
        #media_description = driver.find_element_by_xpath("//meta[@property='og:description']").get_attribute("content")

        if media_type == "video":
            media_link = driver.find_element_by_xpath("//meta[@property='og:video']").get_attribute("content")
            urllib.request.urlretrieve(media_link, "{}.mp4".format(video_directory + filename))
        else:
            media_link = driver.find_element_by_xpath("//meta[@property='og:image']").get_attribute("content")
            urllib.request.urlretrieve(media_link, "{}.jpg".format(img_directory + filename))

        return True

    except:
        return False
