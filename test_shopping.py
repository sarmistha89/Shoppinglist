import pytest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from utility.Baseclass import BaseClass
from POM.amazon import getamazondata
from POM.Bigbasket import getBigbasket
from BaseClass import BaseClass
#print("enter the product name")
#n=input("enter your product")

class Testeasyshopping(BaseClass):
    
    def test_shopping(self):
        
        #with open('/home/pi/Documents/Framework1/list.txt') as f:
        lines = open('/home/pi/Documents/Framework1/list.txt', 'r', encoding='utf-8-sig').read().split('\n')
        print(lines)
        for l in lines:
            amazoncart=getamazondata(self.driver)
            amazoncart.searchdata(l)
            
            amazoncart.searchbutton()
#comparing price
            price_tags=amazoncart.price()
            if price_tags == []:
                print("Sorry! No item matched")
            else:
                price=[]
                for item in price_tags:
                    price.append(item.text)
                    price = [sub.replace(',', '') for sub in price]
#converting str to int
                self.conversion(price)
  
                n1=len(price)
                self.sortingtext(price,n1)
                amazonprice=[i for i in price if i != 0]
                print("the lowest price of",l," in Amazon is:", amazonprice[0])
                amazoncart.getclear()
#for big basket
        for l in lines: 
            self.driver.get("https://www.bigbasket.com/")
            BBcart=getBigbasket(self.driver)
            BBcart.searchdata(l)
            BBcart.searchbutton()         
            
            bbprice=BBcart.price()
            if bbprice == []:
                print("Sorry! No item matched")
            else:
                price=[]
                for amt in bbprice:
                    price.append(amt.text)
#print(price_bb)

                self.conversion(price)
#print(price_bb)
                n3=len(price)
                self.sortingtext(price,n3)
                print("the lowest price of",l, "in BigBasket is:", price[0])
                BBcart.getclear()