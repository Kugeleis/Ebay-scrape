# -*- coding: utf-8 -*-
"""

"""

from selenium import webdriver
from time import sleep
import matplotlib.pyplot as plt 
import csv

#Change these values accordingly
searchTerms = ["Cartridge Filter for Einhell Vacuum Cleaners",
"32mm Crevice Tool Grey for Dyson DC14 Vacuum Cleaners",
"Paper Filter Bag for Vacuum Cleaners, 5 Pack",
"Fleece Filter Bags for M Class Wet & Dry Vacuum Cleaners",
"Paper Filter Bag for Vacuum Cleaners, 5 Pack",
"Paper Filter Bags for CV 30/1 & CV 38/2 Adv Vacuum Cleaners",
"HEPA Filter for CV 30/1 & CV 38/2 Adv Vacuum Cleaners",
"Paper Cartridge Filter for NT 48/1 & NT 27/1 Wet & Dry Vacuum Cleaners",
"3.5m Extension Suction Hose for WD Range of Wet & Dry Vacuum Cleaners",
"Fleece Filter Bags for NT 40/1 L & M Class Wet & Dry Vacuum Cleaners",
"Fabric Filter for for Einhell Vacuum Cleaners",
"2.5m Suction Hose for NT Range of Wet & Dry Vacuum Cleaners",
"Universal Vacuum Cleaner Tool Accessory Kit - 32mm & 35mm",
"15L 1100W Charles Wet & Dry Cylinder Vacuum Cleaner 230V",
"15L 1060W George 3-in-1 Wet & Dry Cylinder Vacuum Cleaner 230V",
"6L 620W Hetty Compact Vacuum Cleaner, Pink 230V",
"6L 2x 36V Batteries Henry Cordless Vacuum Cleaner, Red",
"9L 620W Industrial Plug Henry Vacuum Cleaner 110V",
"6L 620W Henry Compact Vacuum Cleaner, Red 230V",
"9L 620W Vacuum Cleaner 230V",
"Replacement Vacuum Cleaner Drive Belts - Hoover Compatible, 2 Pack",
"7.5L 1000W Pro T200 Vacuum Cleaner 230V",
"15L 1250W Wet & Dry Vacuum Cleaner 230V",
"8L 620W Nuvac Vacuum Cleaner 230V",
"Reusable Filter Dust Bags for Cordless Backpack Vacuum Cleaner, 10 Pack",
"Cartridge Filter for Einhell Vacuum Cleaners",
"32mm Crevice Tool Grey for Dyson DC14 Vacuum Cleaners",
"Paper Filter Bag for Vacuum Cleaners, 5 Pack",
"Fleece Filter Bags for M Class Wet & Dry Vacuum Cleaners",
"Paper Filter Bag for Vacuum Cleaners, 5 Pack",
"Paper Filter Bags for CV 30/1 & CV 38/2 Adv Vacuum Cleaners",
"HEPA Filter for CV 30/1 & CV 38/2 Adv Vacuum Cleaners",
"Paper Cartridge Filter for NT 48/1 & NT 27/1 Wet & Dry Vacuum Cleaners",
"3.5m Extension Suction Hose for WD Range of Wet & Dry Vacuum Cleaners",
"Fleece Filter Bags for NT 40/1 L & M Class Wet & Dry Vacuum Cleaners",
"Fabric Filter for for Einhell Vacuum Cleaners",
"2.5m Suction Hose for NT Range of Wet & Dry Vacuum Cleaners",
"Universal Vacuum Cleaner Tool Accessory Kit - 32mm & 35mm",
"15L 1100W Charles Wet & Dry Cylinder Vacuum Cleaner 230V",
"15L 1060W George 3-in-1 Wet & Dry Cylinder Vacuum Cleaner 230V",
"6L 620W Hetty Compact Vacuum Cleaner, Pink 230V",
"6L 2x 36V Batteries Henry Cordless Vacuum Cleaner, Red",
"9L 620W Industrial Plug Henry Vacuum Cleaner 110V",
"6L 620W Henry Compact Vacuum Cleaner, Red 230V",
"9L 620W Vacuum Cleaner 230V",
"Replacement Vacuum Cleaner Drive Belts - Hoover Compatible, 2 Pack",
"7.5L 1000W Pro T200 Vacuum Cleaner 230V",
"15L 1250W Wet & Dry Vacuum Cleaner 230V",
"8L 620W Nuvac Vacuum Cleaner 230V",
"Reusable Filter Dust Bags for Cordless Backpack Vacuum Cleaner, 10 Pack",
"Paper Filter Bags for AdvancedVac 20 Vacuum Cleaner, 5 Pack",
"Universal Vacuum Cleaner Micro Tool Kit",
"20L 1250W Wet & Dry Vacuum Cleaner 230V",
"0.6L 22.2V Rechargeable Cordless Vacuum Cleaner",
"1.2L 22.2V AirGility Cordless Hand Held & Floor Vacuum Cleaner",
"0.65L 18V LXT Li-Ion Cordless Vacuum Cleaner - Bare Unit",
"18V LXT Li-Ion Cordless Vacuum Cleaner - Bare Unit",
"18V LXT Li-Ion Brushless Cordless Vacuum Cleaner - Bare Unit",
"15L 800W M Class Mini Vacuum Dust Extractor / Cleaner 230V",
"10L 1250W Wet & Dry Vacuum Cleaner 230V",
"Build Your Own Robotic Vacuum Cleaner",
"25L 1250W L Class Wet & Dry Vacuum Cleaner with Power Take-Off 230V",
"17L 600W AD4 Premium Ash Vacuum Cleaner 230V",
"6L 620W Henry Compact Vacuum Cleaner, Blue 230V",
"48L 1380W Professional Wet & Dry Vacuum Cleaner 230V",
"Replacement Vacuum Cleaner Drive Belts - Panasonic Compatible, 2 Pack",
"Power X-Change 20L 18V Wet & Dry Vacuum Cleaner - Bare Unit",
"Power X-Change 20L 18V 3Ah Li-Ion Cordless Wet & Dry Vacuum Cleaner",
"20L 1250W Wet & Dry Vacuum Cleaner 230V",
"30L 1500W Wet & Dry Vacuum Cleaner with Power Take-Off 230V",
"12L 1000W Wet & Dry Vacuum Cleaner 230V",
"Pre Filter for AdvancedVac 20 Vacuum Cleaner",
"Electronics Toner Vacuum Cleaner",
"15L 1100W Tool Box Wet & Dry Vacuum Cleaner 230V",
"Spare Battery for Henry Cordless Vacuum Cleaner",
"Battery Charger for Henry Cordless Vacuum Cleaner",
"20L 1200W Wet & Dry Vacuum Cleaner 230V",
"30L 1200W M Class Wet & Dry Vacuum Cleaner 110V",
"0.75L 18V LXT Li-Ion Brushless Cordless Vacuum Cleaner",
"Window Vacuum Cleaner",
"0.9L 18V 2.5Ah Li-Ion Cordless Hand Held Vacuum Cleaner",
"75L 2400W Commercial Wet & Dry Vacuum Cleaner 230V",
"15L 800W M Class Mini Vacuum Dust Extractor / Cleaner 110V",
"22L 1200W Wet & Dry Vacuum Cleaner 230V",
"Dust Bags for V-Tuf M Class Vacuum Cleaner, 5 Pack",
"Replacement Vacuum Cleaner Drive Belts - Hoover & Bush Compatible, 2 Pack",
"Filter Bags for Buddy II 18L Wet & Dry Vacuum Cleaner, 4 Pack",
"32mm Brush Attachment for Toner Vacuum Cleaner",
"32mm Vacuum Cleaner Soft Touch Dusting Brush Tool",
"32mm Vacuum Cleaner Combination Floor Nozzle Tool - 300mm",
"5L 1300W Backpack Vacuum Cleaner 230V",
"5.5L 850W CV 30/1 Upright Vacuum Cleaner 230V",
"6L 1x 36V Battery Henry Cordless Vacuum Cleaner, Red",
"6L 620W Henry Compact Vacuum Cleaner, Yellow 230V",
"Vacuum Cleaner Drive Belts - Morphy Richards, Sanyo, Argos, Samsung & Vax Compatible, 2 Pack",
"0.5L 18V 2Ah Cordless Hand Held & Floor Vacuum Cleaner",
"Paper Filter Dust Bags for 18V LXT Brushless Cordless Vacuum Cleaner, 5 Pack",
"Filter Bags for TC-VC 1820 Wet & Dry Vacuum Cleaner, 5 Pack",
"Dyson Junior Ball Vacuum Cleaner",
"Henry Junior Vacuum Cleaner",
"Type 2 Replacement Filter for Toner Vacuum Cleaner",
"20L 1050W Wet & Dry Vacuum Cleaner 230V",
"20L 1050W Stainless Steel Wet & Dry Vacuum Cleaner 230V",
"30L 1400W M Class Wet & Dry Vacuum Cleaner 230V",
"0.5L 22.2V Airpower Cordless Vacuum Cleaner",
"Revo 11.1V Rechargeable Cordless Handheld Vacuum Cleaner",
"0.35L 10.8V / 12V GAS Professional Hand Held Vacuum Cleaner - Bare Unit",
"35L 1250W Commercial Wet & Dry Vacuum Cleaner 230V",
"10L 1000W Wet & Dry Vacuum Cleaner 230V",
"3L 400W Eureka PowerTurbo Pet Extending Upright Vacuum Cleaner",
"1L 18V Li-Ion Cordless Hand Held Vacuum Cleaner - Bare Unit",
"Compatible Miele GN Type Vacuum Cleaner Dust Bags 4 Pack with 1x Micro Filter, 1x Motor Filter",
"Vacuum Cleaner Drive Belts for Dyson DC01/04/07/14, 2 Pack",
"Compatible Vacuum Cleaner Drive Belts, 2 Pack",
"Filter Bags for 17L Wet & Dry Vacuum Cleaner, 5 Pack",
"5L 36V Cordless Backpack Vacuum Cleaner",
"8L 620W James Bagged Cylinder Vacuum Cleaner, Sky Blue",
"Replacement Vacuum Cleaner Drive Belts - Electrolux Compatible, 2 Pack",
"Compatible Sebo X Series Vacuum Cleaner Dust Bags & Filters Service Box Kit 10+2 Pack",
"Compatible Vax 2000 Canister Vacuum Cleaner Dust Bags 5 Pack",
"Cartridge Filter for AdvancedVac 20 Vacuum Cleaner",
"Hetty Junior Vacuum Cleaner",
"30L 1050W Stainless Steel Wet & Dry Vacuum Cleaner 230V",
"25L 1250W L Class Wet & Dry Vacuum Cleaner with Power Take-Off 110V",
"18L 1200W Wet & Dry Vacuum Cleaner 230V",
"15L Twin 18V / 36V Li-Ion Cordless or Corded L Class Dust Extractor / Vacuum Cleaner 110V - Bare Unit",
"48mm x 2.1m Super Flexible Hose for Tool Box Wet & Dry Vacuum Cleaner",
"Dust Bags for Tool Box Wet & Dry Vacuum Cleaner, 3 Pack",
"HH110 Rechargeable Cordless Handheld Vacuum Cleaner",
"10.8V / 12V CXT 2x 1.5Ah Combi and Vacuum Cleaner Kit",
"27L 1380W Wet & Dry Vacuum Cleaner 230V",
"Vacuum Cleaner Filter",
"Twin 18V / 36V LXT Li-Ion Cordless Backpack Vacuum Cleaner - Bare Unit",
"400W Eureka PowerTurbo Upright Vacuum Cleaner",
"32mm Vacuum Cleaner Combination Floor Nozzle Tool - 270mm",
"6L 620W Henry Compact Vacuum Cleaner, Green 230V",
"Compatible Daewoo VCB300 RC300 / 400 / 700 / 3000 / 4000 Series Vacuum Cleaner Dust Bags 5 Pack",
"Compatible Miele Type GN Series Vacuum Cleaner Dust Bags 5 Pack",
"20L 1400W Wet & Dry Vacuum Cleaner 230V",
"Foam Filter for Tool Box Wet & Dry Vacuum Cleaner",
"0.5L 21.6V PowerPlush Turbo Cordless 3-in-1 Vacuum Cleaner",
"Replacement Plug In Power Supply for Voom Vacuum Cleaner, 240V",
"20L 1250W Wet & Dry Vacuum Cleaner 230V",
"Filter Bags for MAXXI II 35 Wet & Dry Vacuum Cleaner, 5 Pack",
"20L 1250W Wet & Dry Vacuum Cleaner 110V",
"Filter Bags for 750W Eco Efficiency Dry Vacuum Cleaner, 10 Pack",
"30mm-38mm Universal Vacuum Cleaner Floor Tool",
"Replacement Vacuum Cleaner Drive Belts - Hoover Compatible, 2 Pack",
"Replacement Vacuum Cleaner Drive Belts - Bissell, Vax & Electrolux Compatible, 2 Pack",
"0.6L 10.8V / 12V CXT Li-Ion Cordless Vacuum Cleaner - Bare Unit",
"40L 1380W L Class Wet & Dry Vacuum Cleaner with Power Take-Off 230V",
"0.5L 21.6V HyperClean Cordless 3-in-1 Vacuum Cleaner",
"17L 1000W Wet & Dry Vacuum Cleaner with Power Take-Off 230V",
"55L 2400W Commercial Wet & Dry Vacuum Cleaner 230V",
"Filter Bags for MV4 20L Wet & Dry Vacuum Cleaner, 4 Pack",
"32mm Universal Vacuum Cleaner Crevice Tool - 345mm",
"Fleece Filter Bags for Cordless 36V Backpack Vacuum Cleaner, 10 Pack",
"Tonavac 99 Toner Vacuum Cleaner Replacement Filter Bags - Pack of 10",
"5.5L 850W CV 38/2 Adv Upright Vacuum Cleaner 230V",
"Poly Bags for Twin 18V / 36V L Class Dust Extractor / Vacuum Cleaner, 10 Pack",
"1.7L 400W Tonavac 99 Toner Vacuum Cleaner 230V",
"15L Twin 18V / 36V Li-Ion Cordless or Corded L Class Dust Extractor / Vacuum Cleaner 230V - Bare Unit",
"Spare Floor Head & Beater Brush for Voom Vacuum Cleaner",
"22.2V Li-Ion Battery Pack for Voom Vacuum Cleaner",
"Compatible Electrolux Lite Series Vacuum Cleaner Dust Bags 5 Pack",
"Compatible Jeyes / Sebo Ensign 350 Vacuum Cleaner Dust Bags 5 Pack",
"Replacement Main Filter for Cordless 36V Backpack Vacuum Cleaner",
"Fleece Filter Bags for 1300W Backpack Vacuum Cleaner, 10 Pack",
"Replacement Vacuum Cleaner Drive Belts - Panasonic Compatible, 2 Pack",
"Compatible Electrolux Boss E66N 4105 / 4110 Vacuum Cleaner Dust Bags 5 Pack",
"Compatible Goblin Ace, Morphy Compact, Electrolux E67N Vacuum Cleaner Dust Bags 5 Pack",
"Compatible Hoover H30+ Vacuum Cleaner Dust Bags 5 Pack",
"Compatible Miele Type FJM Series Vacuum Cleaner Dust Bags 5 Pack",
"Compatible Nilfisk GS80 Series Vacuum Cleaner Dust Bags 5 Pack",
"Compatible Panasonic MC-E40 Upright Series Vacuum Cleaner Dust Bags 5 Pack",
"Compatible Morphy Richards / Blomberg Vacuum Cleaner Dust Bags 5 Pack",
"Replacement Cartridge Filter for MAXXI II 35 Wet & Dry Vacuum Cleaner",
"22L 1350W L Class Wet & Dry Vacuum Cleaner with Power Take-Off 230V",
"HEPA Filter for Twin 18V / 36V L Class Dust Extractor / Vacuum Cleaner",
"Filter for MV2 12L Wet & Dry Vacuum Cleaner",
"Wet & Dry Floor Tool for NT Vacuum Cleaner Range",
"Motor Switch Assembly for V-Tuf Voom Vacuum Cleaner",
"Pet Grooming Tool for V-Tuf Voom Vacuum Cleaner",
"Spare Charging Dock for Voom Vacuum Cleaner",
"Vacuum Cleaner Filter Bag, 5 Pack",
"Replacement Vacuum Cleaner Drive Belts - Dyson Compatible, 2 Pack",
"Compatible Hoover H20 PurePower Series Vacuum Cleaner Dust Bags 5 Pack",
"Compatible Rowenta RU11 Vacuum Cleaner Dust Bags 5 Pack",
"Filter Bags for TE-VC 1930 SA 30L Wet & Dry Vacuum Cleaner, 5 Pack",
"Filter Bag for Vacuum Cleaner, 5 Pack",
"36V Battery for BV 5/1 Bp Backpack Vacuum & T 9/1 Bp Dry Vacuum Cleaner",
"40cm 5x Extendable Hose for Voom Vacuum Cleaner",
"Floor Nozzle Tool for T 10/1 Vacuum Cleaner - 270mm",
"Compatible Hoover H18 TurboPower 2/3 Vacuum Cleaner Dust Bags 5 Pack",
"Compatible Panasonic 71/852 Cylinder Vacuum Cleaner Dust Bags 5 Pack",
"35L 1400W Wet & Dry Vacuum Cleaner 230V",
"40L 1100W M Class Wet & Dry Vacuum Cleaner with Power Take-Off 110V",
"Spare Filter Assembly for Voom Vacuum Cleaner",
"32mm Universal Vacuum Cleaner Round Brush Tool",
"Replacement Vacuum Cleaner Drive Belts - Oreck Compatible, 2 Pack",
"Compatible Nilfisk GM200 Canister Vacuum Cleaner Dust Bags 5 Pack",
"Compatible Oreck XL2000, XL8000 & XL9000 Series Docking Design Vacuum Cleaner Dust Bags 5 Pack",
"40L 1380W M Class Wet & Dry Vacuum Cleaner with Power Take-Off 230V",
"9L 36V T 9/1 Bp Cordless Vacuum Cleaner",
"Compatible Goblin W&D 1000 / Exxtra Vacuum Cleaner Dust Bags 5 Pack",
"22L 1200W L Class Wet & Dry Vacuum Cleaner with Power Take-Off 110V",
"30L 1100W H Class Wet & Dry Vacuum Cleaner with Power Take-Off 110V",
"30L 1380W H Class Wet & Dry Vacuum Cleaner with Power Take-Off 230V",
"Replacement Extension Pole for V-Tuf Voom Vacuum Cleaner",
"Spare Floor Beater Brush Spindle for Voom Vacuum Cleaner",
"Swan Neck Surface Brush for Voom Vacuum Cleaner",]
pageAmounts = 20 # usually 50 entries per page
currencySign = "£"
wait = .5
#Limits (exclusive)
minPrice = 0.0
maxPrice = 10000.0

#Round a float number up
def roundUp(number):
    return int(( number * 100 ) + 0.5) / float(100)

#Calculate mean value
def mean(numbers):
    return float(sum(numbers)) / max(len(numbers), 1)

#Summary of all search terms
meansArray = []
sumArray = []
arrayNum = []
num = 1

#Go to Ebay
driver = webdriver.Firefox()
driver.get("https://www.ebay.co.uk/")

#Click cookie warning away

##add if contains results matching fewer words exclude from results
##//*[@id="srp-river-results"]/ul/div[1]/section #[1= did you mean] 
#driver.find_elements_by_xpath('.//*[@id="srp-river-results"]/ul/div[2]/section')
##//*[@id="srp-river-results"]/ul/div[2]/section #[2= results matching fewer words]

sleep(10*wait)
driver.find_element_by_id("gdpr-banner-accept").click()
sleep(wait)

#Perform searches for all search terms
for searchTerm in searchTerms:
    
    #Fill out and click search form
    search_input = driver.find_element_by_class_name("gh-tb.ui-autocomplete-input")
    search_input.clear()
    search_input.send_keys(searchTerm)
    driver.find_element_by_class_name("btn.btn-prim.gh-spr").click()
    sleep(wait)
    
    if(pageAmounts<1):
        print("pageAmounts should be at least 1!")
        break
    
    sumPrices = 0.0
    prices = []
    entries = []
    entryNo = 1
    
    excludedPrices = 0
    
    currURL = ""
    prevURL = ""
    #start search
    for i in range(pageAmounts):
        currURL = driver.current_url.replace("#","")
        
        listingElems = driver.find_elements_by_class_name("s-item")
        #print("Amount: " + str(len(listingElems)))
        sleep(0.1)
        
        for a in range(len(listingElems)):
            #find price, ignore sponsored listing
            try:
                titleElem = listingElems[a].find_element_by_xpath(".//h3[@class='s-item__title']").text
                priceText = listingElems[a].find_element_by_xpath(".//span[@class='s-item__price']").text
                if(priceText.startswith(currencySign) == True):
                    price = float(priceText.replace("to","").split(currencySign)[1])
                    if(minPrice < price and price < maxPrice):
                        sumPrices += price
                        prices.append(price)
                        entries.append(entryNo)
                        entryNo+=1
                    else:
                        excludedPrices+=1
            except:
                pass #print("Sponsored listing detected")
                
        #Go to next page
        try:
            if(currURL != prevURL):
                prevURL = currURL.replace("#","")
                driver.find_elements_by_class_name("x-pagination__control")[1].click()
            else:
                break
        except:
            print("No next page found!")
        sleep(0.1)
        
    #Prepare results
    meanPrice = roundUp(mean(prices))
    sumPrices = roundUp(sumPrices)
    amountStr = str(len(prices))
    test = driver.find_elements_by_xpath('.//*[@id="srp-river-results"]/ul/div[1]/section')
    if not test:
        testres='not ok'
    else:
        testres='ok'

 
    #Update summary arrays
    meansArray.append(meanPrice)
    sumArray.append(sumPrices)
    arrayNum.append(num)
    num+=1
    
    #Output results

    print("\n\nProduct: " + searchTerm)
    print("result match:     " + testres)
    print("Amount:    " + amountStr)
    print("Sum:       " + currencySign + str(sumPrices))
    print("Mean:      " + currencySign + str(meanPrice))
    print("Excluded : " + str(excludedPrices))
    
    with open('ebayproducts.csv', 'a', encoding="utf-8", newline='') as file:
            writer = csv.writer(file)
            writer.writerow([searchTerm,testres, amountStr, sumPrices, meanPrice, excludedPrices])    
    #Draw a plot
    x = entries
    y = prices
    plt.plot(x, y) 
    plt.xlabel('entry number') 
    plt.ylabel('price (in ' + currencySign + ', on ebay.com)') 
    plt.title(searchTerm) 
    plt.show() 
driver.close()

#Show info about different means values in a bar chart
left = arrayNum
height = meansArray
tick_label = searchTerms
plt.bar(left, height, tick_label = tick_label, 
        width = 0.8, color = ['red', 'blue']) 
plt.xlabel('products') 
plt.ylabel('mean price') 
plt.title('Overview (source: ebay.com)') 
plt.xticks(rotation='vertical')
plt.show() 

#amounts in a pie chart
activities = searchTerms
slices = sumArray
colors = ['r', 'y', 'g', 'b', 'yellowgreen', 'gold', 'lightskyblue', 'lightcoral'] 
plt.pie(slices, labels = activities, colors=colors,  
        startangle=90, shadow = True, 
        radius = 1.2, autopct = '%1.1f%%') 
plt.title('Sum of Prices (source: ebay.com)') 
#plt.legend() 
plt.show() 