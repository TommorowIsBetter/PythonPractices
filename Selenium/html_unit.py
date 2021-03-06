#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:Wang Yan
@ide:PyCharm
@time:2019/4/23 14:17
"""

import unittest

from selenium import webdriver
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class Logout(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Remote(desired_capabilities=DesiredCapabilities.PHANTOMJS)
        self.driver.implicitly_wait(30)
        self.base_url = "http://192.168.1.166"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_logout(self):
        driver = self.driver
        driver.get(self.base_url + "/jenkins-2.0/login?from=%2Fjenkins-2.0%2F")
        driver.find_element_by_id("j_username").clear()
        driver.find_element_by_id("j_username").send_keys("admin")
        driver.find_element_by_name("j_password").clear()
        driver.find_element_by_name("j_password").send_keys("admin")
        driver.find_element_by_id("yui-gen1-button").click()
        driver.find_element_by_xpath("//div[@id='header']/div[2]/span/a[2]/b").click()

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()

