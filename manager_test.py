# -*- coding: utf-8 -*-
import unittest
import manager
from BeautifulSoup import BeautifulSoup

class ManagerTestCase(unittest.TestCase):


    def setUp(self):
        manager.app.config['TESTING'] = True
        self.app = manager.app.test_client()

    def test_index_returns_html(self):
        response = self.app.get('/')
        soup = BeautifulSoup(response.data)
        self.assertTrue(soup.findAll('html'), 'index page does not return html')

if __name__ == '__main__':
    unittest.main()
