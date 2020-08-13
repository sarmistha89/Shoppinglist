

class getamazondata():
    
    def __init__(self, driver):
        self.driver=driver
    
    def searchdata(self,product_name):
        self.driver.find_element_by_xpath("//input[@id='twotabsearchtextbox']").send_keys(product_name)
        
    def searchbutton(self):
        self.driver.find_element_by_xpath("//input[@type='submit' and @value='Go']").click()
        
    def price(self):
        return self.driver.find_elements_by_xpath("//span[@class='a-price-whole']")
    
    def getclear(self):
        self.driver.find_element_by_xpath("//input[@id='twotabsearchtextbox']").clear()
