# -*- coding: utf-8 -*- 

from selenium import webdriver 
from selenium.webdriver.common.keys import Keys 

import time 
import unittest

class TestWebdriver(unittest.TestCase):
    
    def setUp(self):
        #self.browser = webdriver.Firefox() 
        #self.browser = webdriver.Ie() 
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(3)
    def tearDown(self):
        self.browser.close()
    def test_open_a_browser_search_danbo(self):  
        self.browser.get('http://www.google.com.au/') 

        elem = self.browser.find_element_by_xpath("//input[@id='gbqfq']") 
        elem.send_keys(u'danbo' + Keys.RETURN) 
        
        links = self.browser.find_elements_by_xpath("//h3[@class='r']/a/em") 
        
        self.assertIn('danbo', self.browser.title)
        self.assertEqual(links[0].text, u'Danbo', 'not match') 
        
if __name__ == '__main__':
    unittest.main(warnings='ignore')
