from selenium import webdriver

driver = webdriver.Edge()
driver.get("http://www.nexushd.org/signin.php")
driver.find_element_by_xpath(
    '//*[@id="nav_block"]/form[2]/table/tbody/tr[1]/td[2]/input').send_keys("UserName")  # 将UserName改为你的用户名
driver.find_element_by_xpath(
    '//*[@id="nav_block"]/form[2]/table/tbody/tr[2]/td[2]/input').send_keys("Password")  # 将Password改为你的密码
driver.find_element_by_xpath(
    '//*[@id="nav_block"]/form[2]/table/tbody/tr[7]/td/button[1]').click()  # 点击登录后自动跳转至签到页面
driver.find_element_by_xpath(
    '//*[@id="sign-in-form"]/textarea').send_keys("希望大家今天能开心")  # 双引号内为任意签到内容，不能为空
driver.find_element_by_xpath('//*[@id="qr"]').click()  # 点击签到
driver.quit()  # 关闭浏览器
'''
#!/usr/bin/env python3
# -*- coding: UTF-8 -*-


import time
import requests
from selenium import webdriver


class NexusHD:
    def __init__(self, username, passowrd):
        self.username = username
        self.password = passowrd

        self.urlRoot = 'http://www.nexushd.org/'
        self.loginPath = 'takelogin.php'
        self.driverPath = 'path/to/phantomjs.exe'

        self.cookies = None

    def update_cookies(self):
        s = requests.post(self.urlRoot + self.loginPath, data={'username': self.username, 'password': self.password})
        self.cookies = s.history[0].cookies.get_dict()

    def sign_in(self):
        assert self.cookies is not None, 'should update cookies first'

        driver = webdriver.PhantomJS(executable_path=self.driverPath)
        for name, value in self.cookies.items():
            cookie = {
                'domain': '.nexushd.org',  # Note: If 'domain' part is missed or with value 'www.nexushd.org',
                                           # PhantomJS will print the following words:
                                           # "errorMessage":"Can only set Cookies for the current domain"
                                           # But actually the script still works.
                                           # Chrome driver does not have this bug.
                'name': name,
                'value': value,
                'path': '/'
            }
            try:
                driver.add_cookie(cookie)
            except Exception as e:
                print(name, 'wrong', '\n', e)

        driver.get('http://www.nexushd.org/signin.php')
        try:
            driver.find_element_by_tag_name('textarea').send_keys(' [em4] ')
            driver.find_element_by_id('qr').click()
        except:
            print('今日已签到：%s' % time.strftime('%Y-%m-%d',time.localtime(time.time())))
        driver.save_screenshot('result.png')

        driver.quit()


if __name__ == '__main__':
    nhd = NexusHD('your username', 'your password')
    nhd.update_cookies()
    nhd.sign_in()
'''
