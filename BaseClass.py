import pytest
import inspect
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select

@pytest.mark.usefixtures("setup")
class BaseClass:
    
    
    def sortingtext(self,price, n):
        for i in range(n):
            for j in range(0, n-i-1):
                if price[j] > price[j+1]:
                    price[j], price[j+1] = price[j+1], price[j]
                    
    def conversion(self,price):
        for i in range(0, len(price)):
            price[i] = int(float(price[i]))

        
    def logging(self):
        loggerName= inspect.stack()[1][3]
        logger=logging.getLogger(loggerName)

        fileHandler=logging.FileHandler('logfile.log')
        formatter=logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
        fileHandler.setFormatter(formatter)

        logger.addHandler(fileHandler)
        logger.setLevel(logging.DEBUG)
        return logger