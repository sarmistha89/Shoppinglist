#import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

print("enter the product name")
n=input("enter your product")
        
driver=webdriver.Chrome()

driver.get("https://www.amazon.in/")
searchamazon=driver.find_element_by_xpath("//input[@id='twotabsearchtextbox']")
searchamazon.send_keys(n)
searchbutton=driver.find_element_by_xpath("//input[@type='submit' and @value='Go']")
searchbutton.click()

#comparing price
price_tags = driver.find_elements_by_xpath("//span[@class='a-price-whole']")
#print(price_tags)
if price_tags == []:
    print("No item matched")
else:
    price=[]
    for item in price_tags:
        price.append(item.text)
        newprice = [sub.replace(',', '') for sub in price] 
#print(newprice)

#converting str to int
    for i in range(0, len(newprice)): 
        newprice[i] = int(newprice[i]) 
  
    n1=len(newprice)

    for i in range(n1):
        for j in range(0, n1-i-1):
            if newprice[j] > newprice[j+1]:
                newprice[j], newprice[j+1] = newprice[j+1], newprice[j] 
#print(newprice)
    amazonprice=[i for i in newprice if i != 0]
    print("the lowest price in Amazon is:", amazonprice[0])

    


'''
#for groofers

driver.get("https://grofers.com/")
#driver.maximize_window()
locationalert=driver.find_element_by_xpath("//div[@class='location-body center-aligned location__tooltip']")
changelocation=driver.find_element_by_xpath("//button[@class='btn btn--inverted']").click()
city=driver.find_element_by_xpath("//img[@alt='Bengaluru']")
city.is_displayed()
driver.implicitly_wait(10)
ActionChains(driver).move_to_element(city).click(city).perform()

driver.find_element_by_xpath("//input[@class='react-autosuggest__input']").send_keys(n)
driver.find_element_by_xpath("//button[@class='btn search__btn']").click()
amounts=driver.find_elements_by_xpath("//div[@class='plp-product__price']/div/div/span")
price_grofer=[]
for amount in amounts:
    price_grofer.append(amount.text)
    #price_grofer = [sub.replace('₹', '') for sub in price_grofer]
print(price_grofer)
for i in range(0, len(price_grofer)): 
    price_grofer[i] = int(price_grofer[i]) 
#print(price_grofer)
n2=len(price_grofer)
for i in range(n2):
    for j in range(0,n2-i-1):
        if price_grofer[j] > price_grofer[j+1]:
            price_grofer[j],price_grofer[j+1]=price_grofer[j+1],price_grofer[j]
#print(price_grofer)
print("the lowest price in grofer is:", price_grofer[0])
'''
#for Big basket

driver.get("https://www.bigbasket.com/")
driver.find_element_by_xpath("//input[@id='input']").send_keys(n)
driver.find_element_by_xpath("//button[@type='submit']").click()
bbprice=driver.find_elements_by_xpath("//span[@class='discnt-price']//span[@class='ng-binding']")
price_bb=[]
for amt in bbprice:
    price_bb.append(amt.text)
#print(price_bb)

for i in range(0, len(price_bb)):
    price_bb[i] = int(float(price_bb[i]))
#print(price_bb)
n3=len(price_bb)

for i in range(n3):
    for j in range(0,n3-i-1):
        if price_bb[j] > price_bb[j+1]:
            price_bb[j],price_bb[j+1] = price_bb[j+1],price_bb[j]
#print(price_bb)
print("the lowest price in BigBasket is:", price_bb[0])
    