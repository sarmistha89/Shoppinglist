class getBigbasket():
    
    def __init__(self, driver):
        self.driver=driver
    
    def searchdata(self,product_name):
        self.driver.find_element_by_xpath("//input[@id='input']").send_keys(product_name)
        
    def searchbutton(self):
        self.driver.find_element_by_xpath("//button[@type='submit']").click()
        
    def price(self):
        return self.driver.find_elements_by_xpath("//span[@class='discnt-price']//span[@class='ng-binding']")
   
    def getclear(self):
        self.driver.find_element_by_xpath("//input[@id='input']").clear()