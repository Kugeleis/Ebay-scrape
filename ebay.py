# -*- coding: utf-8 -*-
"""

"""

from selenium import webdriver
from time import sleep
import matplotlib.pyplot as plt
import csv

# Change these values accordingly
ebaySite = "https://www.ebay.de/"
excludeTerms = ['Netzteil', 'Wandhalterung', 'Leerkarton']
searchTerms = ["Fritz Box 7490",
               "Fritz Box 7530", ]
pageAmounts = 20  # usually 50 entries per page
currencySign = "EUR"
wait = .5
#Limits (exclusive)
minPrice = 15.0
maxPrice = 1000.0
sold = True

# XPath setup
priceX = ".//span[@class = 's-item__price']/span[@class = 'POSITIVE']" if sold else ".//span[@class = 's-item__price']"
titleX = ".//h3[contains(concat(' ', @class, ' '), ' s-item__title ')]"

# Round a float number up


def roundUp(number):
    return int((number * 100) + 0.5) / float(100)

# Calculate mean value


def mean(numbers):
    return float(sum(numbers)) / max(len(numbers), 1)

# Calculate the median


def median(lst):
    sortedLst = sorted(lst)
    lstLen = len(lst)
    index = (lstLen - 1) // 2

    if (lstLen % 2):
        return sortedLst[index]
    else:
        return (sortedLst[index] + sortedLst[index + 1])/2.0


# Summary of all search terms
meansArray = []
mediansArray = []
sumArray = []
arrayNum = []
num = 1
excludeTerm = ' -' + ' -'.join(excludeTerms)

# Go to Ebay
driver = webdriver.Firefox(executable_path="./geckodriver")
driver.get(ebaySite)

# Click cookie warning away

# add if contains results matching fewer words exclude from results
# //*[@id="srp-river-results"]/ul/div[1]/section #[1= did you mean]
# driver.find_elements_by_xpath('.//*[@id="srp-river-results"]/ul/div[2]/section')
# //*[@id="srp-river-results"]/ul/div[2]/section #[2= results matching fewer words]

sleep(10*wait)
driver.find_element_by_id("gdpr-banner-accept").click()
sleep(wait)

# Perform searches for all search terms
for searchTerm in searchTerms:
    # Fill out and click search form
    search_input = driver.find_element_by_class_name(
        "gh-tb.ui-autocomplete-input")
    search_input.clear()
    search_input.send_keys(searchTerm + excludeTerm)
    driver.find_element_by_class_name("btn.btn-prim.gh-spr").click()
    sleep(wait)

    if (sold):  # filter for sold items
        driver.get(driver.current_url + '&LH_Sold=1&LH_Complete=1')
        sleep(wait*2)

    if(pageAmounts < 1):
        print("pageAmounts should be at least 1!")
        break
    # debug
    print("Seiten:", pageAmounts)

    sumPrices = 0.0
    prices = []
    entries = []
    entryNo = 1

    excludedPrices = 0

    currURL = ""
    prevURL = ""
    # start search
    for i in range(pageAmounts):

        currURL = driver.current_url.replace("#", "")

        listingElems = driver.find_elements_by_class_name("s-item")
        print("Amount: " + str(len(listingElems)))
        sleep(0.1)

        for a in range(len(listingElems)):
            # print(listingElems[a].text)
            # find price, ignore sponsored listing
            try:
                titleElem = listingElems[a].find_element_by_xpath(titleX).text
                priceText = listingElems[a].find_element_by_xpath(priceX).text
                print('Preis: ', priceText)

                if(priceText.startswith(currencySign) == True):
                    price = float(priceText.replace(
                        ",", ".").split(currencySign)[1])
                    if(minPrice < price and price < maxPrice):
                        sumPrices += price
                        prices.append(price)
                        entries.append(entryNo)
                        entryNo += 1
                    else:
                        excludedPrices += 1
            except:
                pass  # print("Sponsored listing detected")

        # Go to next page
        try:
            if(currURL != prevURL):
                prevURL = currURL.replace("#", "")
                driver.find_elements_by_class_name(
                    "x-pagination__control")[1].click()
            else:
                break
        except:
            print("No next page found!")
        sleep(0.1)

    # Prepare results
    meanPrice = roundUp(mean(prices))
    medianPrice = roundUp(median(prices))
    sumPrices = roundUp(sumPrices)
    amountStr = str(len(prices))
    test = driver.find_elements_by_xpath(
        './/*[@id="srp-river-results"]/ul/div[1]/section')
    if not test:
        testres = 'not ok'
    else:
        testres = 'ok'

    # Update summary arrays
    meansArray.append(meanPrice)
    mediansArray.append(medianPrice)
    sumArray.append(sumPrices)
    arrayNum.append(num)
    num += 1

    # Output results

    print("\n\nProduct: " + searchTerm)
    print("result match:     " + testres)
    print("Amount:    " + amountStr)
    print("Sum:       " + currencySign + str(sumPrices))
    print("Mean:      " + currencySign + str(meanPrice))
    print("Median:      " + currencySign + str(medianPrice))
    print("Excluded : " + str(excludedPrices))

    with open('ebayproducts.csv', 'a', encoding="utf-8", newline='') as file:
        writer = csv.writer(file)
        writer.writerow([searchTerm, testres, amountStr,
                        sumPrices, meanPrice, excludedPrices])
    # Draw a plot
    x = entries
    y = prices
    plt.plot(x, y)
    plt.xlabel('entry number')
    plt.ylabel('price (in ' + currencySign + ', on ' + ebaySite + ')')
    plt.title(searchTerm)
    plt.show()
driver.close()

# Show info about different means values in a bar chart
left = arrayNum
height = meansArray
tick_label = searchTerms
plt.bar(left, height, tick_label=tick_label,
        width=0.8, color=['red', 'blue'])
plt.xlabel('products')
plt.ylabel('mean price')
plt.title('Overview (source: ebay.com)')
plt.xticks(rotation='vertical')
plt.show()

# amounts in a pie chart
activities = searchTerms
slices = sumArray
colors = ['r', 'y', 'g', 'b', 'yellowgreen',
          'gold', 'lightskyblue', 'lightcoral']
plt.pie(slices, labels=activities, colors=colors,
        startangle=90, shadow=True,
        radius=1.2, autopct='%1.1f%%')
plt.title('Sum of Prices (source: '+ebaySite+')')
# plt.legend()
plt.show()
