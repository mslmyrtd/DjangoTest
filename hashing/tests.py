from django.test import TestCase
from selenium import webdriver

class UnitTestCase(TestCase):
    pass

class functionalTestCase(TestCase):
    def setUp(self):
        self.browser=webdriver.Firefox()
    def tearDown(self):
        self.browser.quit()
    def test_ther_is_homepage(self):
        self.browser.get("http://localhost:8000")
        self.assertIn("Enter hash here",self.browser.page_source)



