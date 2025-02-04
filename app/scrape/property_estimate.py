from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait 
import selenium.webdriver.support.expected_conditions as EC

"""
driver = webdriver.Firefox()

driver.get("https://www.eppraisal.com")
# iframe = WebDriverWait(driver, 100).until(lambda x: driver.find_element(By.CSS_SELECTOR, "iframe[data-dojo-attach-point='iframeBannerContainer']"))
# driver.switch_to.frame(iframe)

# Click to close modal popup when home page loads
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.mc-closeModal[data-action='close-mc-modal']"))).click()

addr1 = driver.find_element(By.NAME, "address1")
addr1.clear()
addr1.send_keys("12931 Quinnel Ct")

addr2 = driver.find_element(By.NAME, "address2")
addr2.clear()
addr2.send_keys("92130")

elem = driver.find_element(By.XPATH, "//form[@action='/property/']/div/div/button")

elem.click()

assert "No results found." not in driver.page_source


WebDriverWait(driver, 100).until(EC.title_contains('12931'))
abc = driver.find_element(By.CLASS_NAME, "post")
#print(abc)
#print('text: ', abc.text)

title = driver.find_element(By.CSS_SELECTOR, 'h1.title')
estimate = driver.find_element(By.CSS_SELECTOR, "h2[epp_field='avm']")
low_estimate = driver.find_element(By.CSS_SELECTOR, "span.range[epp_field='avm_low']")
high_estimate = driver.find_element(By.CSS_SELECTOR, "span.range[epp_field='avm_high']")

print('title: ', title.text)
print('estimate: ', estimate.text)
print('low estimate: ', low_estimate.text)
print('high estimate: ', high_estimate.text)

driver.close()
"""

#TODO: Click 'Street View' link and get photo!!
def get_property_estimate(address: str, zipcode: str):
    """
    Use Selenium to scrape website to get property estimate (in dollars).
    Need to manually solve reCAPTCHA image puzzle
    """

    try:
        driver = webdriver.Firefox()

        # Change spaces to '+' for url query parameter
        addr1 = "+".join(address.split(' '))
        addr_nums = address.split(' ')[0]
        print('addr_nums: ', addr_nums)

        url = f'https://www.eppraisal.com/property/?address1={addr1}&address2={zipcode}&source=header'

        driver.get(url)

        # Wait at least 20 secs to see address in webpage title before exiting driver
        # Purpose: Screen does not exit right away, so can complete reCAPTCHA
        try:
            WebDriverWait(driver, 20).until(EC.title_contains(addr_nums))
        except:
            # If property DNE/not a house, title will be 'Property Not Found'
            # return title & delete row from dataframe
            WebDriverWait(driver, 10).until(EC.title_contains('Property Not Found'))
            title = driver.find_element(By.CSS_SELECTOR, 'h1.title')
            print('title: ', title.text)
            return title.text


        title = driver.find_element(By.CSS_SELECTOR, 'h1.title')
        estimate = driver.find_element(By.CSS_SELECTOR, "h2[epp_field='avm']")
        low_estimate = driver.find_element(By.CSS_SELECTOR, "span.range[epp_field='avm_low']")
        high_estimate = driver.find_element(By.CSS_SELECTOR, "span.range[epp_field='avm_high']")
        
        # Close Modal popup
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.mc-closeModal[data-action='close-mc-modal']"))).click()
        
        # Click on Street View link to get property photo/to change src for 'mstreetview'
        driver.find_element(By.XPATH, "//table[@class='prop_details']/tbody/tr/td[2]/span/a[2]").click()
        
        # Get image src
        img_el = driver.find_element(By.ID, "mstreetview")
        img_src = img_el.get_attribute("src")

        print('title: ', title.text)
        print('estimate: ', estimate.text)
        print('low estimate: ', low_estimate.text)
        print('high estimate: ', high_estimate.text)
        print('img: ', img_src)

        return estimate.text


    except Exception as error:
        print('property_estimate.py ERROR! ', error)

    finally:
        print('finally running...')
        driver.close()

    """
    return {
        'estimate': estimate.text,
        'low_estimate': low_estimate,
        'high_estimate': high_estimate,
        'img_src': img_src
    }
    """

get_property_estimate('1300 33RD ST', '93301')