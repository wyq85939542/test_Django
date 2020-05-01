from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self) -> None:
        self.browser = webdriver.Firefox()

    def test_get_one_web_01(self):
        self.browser.get('http://localhost:8000')

        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the Test!')

    def tearDown(self):

        self.browser.close()
