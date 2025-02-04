import mechanicalsoup

browser = mechanicalsoup.StatefulBrowser()

url = "https://www.eppraisal.com/"
#page = browser.get(url)

#print(page) # returns HTTP code

# print(page.soup)

# Extract the form with class 'prop-search-container'
#form_container = page.soup.find("div", class_="prop-search-container")
#form = form_container.contents[1]
#form = page.soup.select(".prop-search-container form")[0]
#print(form)

try:
    browser.open(url)
    browser.select_form('form[action="/property/"]')
    print(browser.form.print_summary())

    browser['address1'] = '12931 Quinnel Ct'
    browser['address2'] = '92130'
    response = browser.submit_selected()
    print(response.text)

except Exception as error:
    print(f'Error using mechanicalsoup: {error}')

# If the form is found, proceed with the search

##if form:
    # Extract the form inputs
    #address1_input = form.find("input", {"name": "address1"})
    #address2_input = form.find("input", {"name": "address2"})

    # Set the search query
    #address1_input["value"] = "12931 Quinnel Ct"
    #address2_input["value"] = "92130"

    #print(address1_input["value"], address2_input["value"])

    #form.select("input")[0]["value"] = "12931 Quinnel Ct"
    #form.select("input")[1]["value"] = "92130"

    # Submit the form
    #response = browser.submit(form, page.url)

    # Print the response content or do further processing
    #print(response.text)
    #browser.select_form('form[action="/property/"]')
    #print(browser.form.print_summary())
#else:
#    print("Form not found.")
    