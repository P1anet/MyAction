from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Edge()
driver.get("https://www.cc98.org/logOn")
WebDriverWait(driver, 5, 0.1).until(EC.presence_of_element_located(
    (By.ID, "loginName")))  # 98页面加载比nexushd稍慢，需要等待，否则找不到element会报错无法进行下一步
driver.find_element_by_id("loginName").send_keys(
    "UserName")  # 将UserName改为你的用户名
driver.find_element_by_id("loginPassword").send_keys(
    "Password")  # 将Password改为你的密码
driver.find_element_by_xpath(
    '//*[@id="root"]/div/div[2]/div/div/form/button').click()  # 点击登录
WebDriverWait(driver, 5, 0.1).until(
    EC.presence_of_element_located((By.CLASS_NAME, "errorIcon")))
driver.get("https://www.cc98.org/signin")  # 在同一个标签页内访问加载页面
WebDriverWait(driver, 5, 0.1).until(
    EC.presence_of_element_located((By.ID, "post-topic-button")))
# 双引号内为签到内容，好像就算写了，签到楼内也只会显示“签到回复”
driver.find_element_by_xpath(
    '//*[@id="root"]/div/div[2]/div[4]/div[2]/div[1]/textarea').send_keys("希望大家今天能开心")
driver.find_element_by_xpath('//*[@id="post-topic-button"]').click()  # 完成签到
driver.quit()  # 关闭浏览器
