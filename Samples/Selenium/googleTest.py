from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import unittest
import HtmlTestRunner

class GoogleSearch(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Chrome(ChromeDriverManager().install())
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
        
    def test_selenium(self):
        self.driver.get("https://www.google.com")
        self.driver.find_element("name","q").send_keys("Selenium")
        self.driver.find_element("name","btnK").click()

    def test_shiv(self):
        self.driver.get("https://www.google.com")
        self.driver.find_element("name","q").send_keys("Shiv Nadar")
        self.driver.find_element("name","btnK").click()
        
    @classmethod
    def tearDown(cls):   
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Users/KIIT/Documents/Github/Selenium/reports'))
