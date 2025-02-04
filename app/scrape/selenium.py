from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait 
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

# Start a Selenium WebDriver session (assuming you have Chrome WebDriver installed)
#service = Service('app/scrape/chromedriver-mac-x64/chromedriver')
#service.start()
#driver = webdriver.Remote(service.service_url)
driver = webdriver.Firefox()

addr1 = "12931 Quinnel Ct"
addr1 = "+".join(addr1.split(' '))
zipcode = '92130'

# Define the URL
url = f"https://www.eppraisal.com/property/?address1={addr1}&address2={zipcode}&source=header"
print(url)

captcha_sitekey = '6LdysN4cAAAAAKDU_Zokqf23RDTgui2PM8T8w7qA'

# Open the URL in the browser
driver.get(url)
# Wait for the page to load
# You may need to adjust the waiting time depending on the page load time
#driver.implicitly_wait(100)
iframe = WebDriverWait(driver, 100).until(lambda x: driver.find_element(By.XPATH, "//iframe[@title='reCAPTCHA']"))
driver.switch_to.frame(iframe)
#driver.switch_to(iframe)
#iframe.send_keys(Keys.PAUSE)

WebDriverWait(driver, 200).until(lambda x: driver.find_element(By.CSS_SELECTOR, 'div.rc-anchor')).click()
#wait.until(lambda x: driver.find_element(By.CLASS_NAME, "rc-anchor").click())

driver.switch_to.default_content()
#driver.find_element(By.XPATH, "//button[@type='submit']").click()

"""
driver.find_element(By.CLASS_NAME, "rc-anchor").click()
driver.switch_to.default_content()
iframe.send_keys(Keys.PAUSE)
driver.find_element(By.XPATH, "//button[@type='submit']").click()
"""

#token_input = wait.until(lambda x:driver.find_element(By.ID, "recaptcha-token").send_keys('03AFcWeA5ZZvyJrFjwV1s6pQQAvHJRx2wNdYbBzvxJGfKVCLK-lQ9ue0roQbKxfTDcTReumGklF3tK4hZz82LUN21e0asjjPSz5tWysIy-FeF5qb0e0qkzD6tRWDJS3zmZDX11eLMI1RBMmlkECQvdhmsz0OhkdW8uHedxyMSG2UuXWDMyRiQqcP4izKDZe3zaQtJxNPEpWfKr13Br1J8jD1s4lTwpHLXAAAfOtOpy9Pk0MVqzjw2DNndY2eSmLYvUIrZA26Z4nWk3s3Ej-oiLD52agjCFjxdbFpRu3wyi3TtkgsEMBynw5qrzdw3Hmour1BlGqpPr646Ygeiop2Vb6G4ku-qLpyWwkguQjOzWXAYGeaLlyNkEZBO28OB3sZ8y-fu8dFn3dewz1u53SxEhoHv1FL3-ioNdOmhvXR1zpCxJKIG1Fm7NjMmKGLzcZ3QDNZkCztmIuydlGouqfOMZILBL9_fEP4SxKuDpw96jyEWCrGr8VnUE857miHjRiRTeut5XcDu_KnNnL-7_JIKh_LK4h9H0tkADI_Sd51H_HvUTLCs9uS8pa-Af9-Y7NBvNMmSBviJ3rF3plEKtiPK9wCEhZuROwH5CTgas4iVWfoI8HzJqTGzuGDYdI2hT6XqRglt_FZ6Y8rgFC5iiN5vSMCr0rJzPLxCAqGrHB9Ne1EWKq1B1ArDIzGFC0bY1FiQPQwMvYwBsZ62kb9FBgVL-q4zyaBaLX0BDFQvFsYbSO7RwewiSh7LurtYvdNcNSrHHaR-yadBVpdz4x8z3bG-pOLu_-4kvA-uCIBhbdjaGcoIeP6ZZMWKN5RqQvKh6r1_yZm5pjDN8d7gOfs6F8fVOyoDBw3im0YOH_Q40Mqt6fXEW1hSLcrBmsNKc8kqbCnhOP5Hu-7MFKYV4dFzjU7iuSmUB12eHsN1O_0ZckUwUaQSz0mkCOEHw7qY0KZa1K-6z-r6DzwRtPqgwiNdqxS5tmJcb_fmWXx50R4L79HmGY5NlUW8s7Sa6R1v8IJozyAc8C6e_Q_iIwPPX8oqlxllxL88NyynCsz86beG5MMCEaTdZSfFCpW6i0mFMhu4q-qJALSSghhMbXQ0xfA0Fe5HPWmo2C_IXKOIkecEhHpWg590PSo6n0_JdjocFE97zPkkAV5LbWH4egMUhfsLs9oH6Wcws1Qg-PpCySKfMr6Mb4m8cvT0nItMOpqGHLllGzehZ6EOO1cI1sdUEGLVWM-L00SpGu7T5V9UOBMpezrmMuw_peIsW-anmic9Su92DLMEgTfFtx1Jn7QcrNAso1k5TT6IjmYRoQRccAIm_JmFFrhFwNVa1E_lmnQdnWX2E2qdvZaIu3vZPdS9oslPRU9hgnLUytLC5Fu1_h0GM7IuUM3HXClu92j0-ciWj10EmjDLM_ITDHBRwnzkWjKr79rRetmAo7adCXSTJlzq33MRPUL8A9Vqve4GJwdt8xT-nIwA8wXR5ugEZ7gGPxBHGqOUSG06qeICJvMM62iZg_HYPtatYmUgIaB4jqhsYrtAgkdNrFEZgQMYnupmih3YPMD4h1L7XsHa-UMBmm579JyLS6czTUu46t53bPHJSNCRfJVrVpxMnawYpUuB5mos2WH9pRGcOm9nlPlDDFCkgL7iWFTjCFN224D8lVUyG7Uc09spJMjNalXGdWaf0TrutdqmmdMky0CkoupckFw'))
#print('token_input', token_input, token_input.text)

# token_input.send_keys('03AFcWeA5ZZvyJrFjwV1s6pQQAvHJRx2wNdYbBzvxJGfKVCLK-lQ9ue0roQbKxfTDcTReumGklF3tK4hZz82LUN21e0asjjPSz5tWysIy-FeF5qb0e0qkzD6tRWDJS3zmZDX11eLMI1RBMmlkECQvdhmsz0OhkdW8uHedxyMSG2UuXWDMyRiQqcP4izKDZe3zaQtJxNPEpWfKr13Br1J8jD1s4lTwpHLXAAAfOtOpy9Pk0MVqzjw2DNndY2eSmLYvUIrZA26Z4nWk3s3Ej-oiLD52agjCFjxdbFpRu3wyi3TtkgsEMBynw5qrzdw3Hmour1BlGqpPr646Ygeiop2Vb6G4ku-qLpyWwkguQjOzWXAYGeaLlyNkEZBO28OB3sZ8y-fu8dFn3dewz1u53SxEhoHv1FL3-ioNdOmhvXR1zpCxJKIG1Fm7NjMmKGLzcZ3QDNZkCztmIuydlGouqfOMZILBL9_fEP4SxKuDpw96jyEWCrGr8VnUE857miHjRiRTeut5XcDu_KnNnL-7_JIKh_LK4h9H0tkADI_Sd51H_HvUTLCs9uS8pa-Af9-Y7NBvNMmSBviJ3rF3plEKtiPK9wCEhZuROwH5CTgas4iVWfoI8HzJqTGzuGDYdI2hT6XqRglt_FZ6Y8rgFC5iiN5vSMCr0rJzPLxCAqGrHB9Ne1EWKq1B1ArDIzGFC0bY1FiQPQwMvYwBsZ62kb9FBgVL-q4zyaBaLX0BDFQvFsYbSO7RwewiSh7LurtYvdNcNSrHHaR-yadBVpdz4x8z3bG-pOLu_-4kvA-uCIBhbdjaGcoIeP6ZZMWKN5RqQvKh6r1_yZm5pjDN8d7gOfs6F8fVOyoDBw3im0YOH_Q40Mqt6fXEW1hSLcrBmsNKc8kqbCnhOP5Hu-7MFKYV4dFzjU7iuSmUB12eHsN1O_0ZckUwUaQSz0mkCOEHw7qY0KZa1K-6z-r6DzwRtPqgwiNdqxS5tmJcb_fmWXx50R4L79HmGY5NlUW8s7Sa6R1v8IJozyAc8C6e_Q_iIwPPX8oqlxllxL88NyynCsz86beG5MMCEaTdZSfFCpW6i0mFMhu4q-qJALSSghhMbXQ0xfA0Fe5HPWmo2C_IXKOIkecEhHpWg590PSo6n0_JdjocFE97zPkkAV5LbWH4egMUhfsLs9oH6Wcws1Qg-PpCySKfMr6Mb4m8cvT0nItMOpqGHLllGzehZ6EOO1cI1sdUEGLVWM-L00SpGu7T5V9UOBMpezrmMuw_peIsW-anmic9Su92DLMEgTfFtx1Jn7QcrNAso1k5TT6IjmYRoQRccAIm_JmFFrhFwNVa1E_lmnQdnWX2E2qdvZaIu3vZPdS9oslPRU9hgnLUytLC5Fu1_h0GM7IuUM3HXClu92j0-ciWj10EmjDLM_ITDHBRwnzkWjKr79rRetmAo7adCXSTJlzq33MRPUL8A9Vqve4GJwdt8xT-nIwA8wXR5ugEZ7gGPxBHGqOUSG06qeICJvMM62iZg_HYPtatYmUgIaB4jqhsYrtAgkdNrFEZgQMYnupmih3YPMD4h1L7XsHa-UMBmm579JyLS6czTUu46t53bPHJSNCRfJVrVpxMnawYpUuB5mos2WH9pRGcOm9nlPlDDFCkgL7iWFTjCFN224D8lVUyG7Uc09spJMjNalXGdWaf0TrutdqmmdMky0CkoupckFw')

# Capture the generated JavaScript on the second loaded page
#generated_js = driver.execute_script("return document.documentElement.outerHTML")

# Now you can process the generated JavaScript as needed
#print(generated_js)

abc = driver.find_element(By.CLASS_NAME, "post")
print('abc.text', abc.text)

# Quit the driver
driver.quit()


"""

# Open the URL in the browser
driver.get(url)

# Find the search form elements
address1_input = driver.find_element_by_css_selector("input[name='address1']")
address2_input = driver.find_element_by_css_selector("input[name='address2']")
search_button = driver.find_element_by_css_selector("button[type='submit']")

# Fill in the search form
address1_input.send_keys("12931 Quinnel Ct")
address2_input.send_keys("92130")

# Submit the form
#search_button.click()

# Wait for the page to load
# You may need to adjust the waiting time depending on the page load time
driver.implicitly_wait(10)  

# Capture the generated JavaScript on the second loaded page
generated_js = driver.execute_script("return document.documentElement.outerHTML")

# Now you can process the generated JavaScript as needed
print(generated_js)

# Quit the driver
driver.quit()
"""