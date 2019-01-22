#coding=utf-8
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from framework.base_page import BasePage
import time
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
class CreatOrder(object):
    driver = webdriver.Chrome()
    basepage=BasePage(driver)
    def open_yongche(self):
        self.basepage.open_url("https://sso.yongche.org/")
        time.sleep(1)
    def login_yongche(self):
        username="zhaolisi"
        keys="Zls@8891"
        self.driver.find_element_by_id('J_login').send_keys(username)
        time.sleep(1)
        self.driver.find_element_by_id('J_pwd').send_keys(keys)
        time.sleep(1)
        self.driver.find_element_by_id('id_submit').click()
        time.sleep(1)
    def jump_handler(self):
        self.driver.find_element_by_link_text('首页').click()
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath("//*[contains(text(),'ERP')]").click()
        self.driver.implicitly_wait(10)
        currentwinfirstpage = self.driver.current_window_handle
        handles = self.driver.window_handles
        for handle in handles:
            if handle != currentwinfirstpage:
                self.driver.switch_to.window(handle)
    def find_user(self):
        self.driver.switch_to.frame("content")
        self.driver.find_element_by_id("cellphone").send_keys("16801015609")
        self.driver.find_element_by_id("cellphone_search").click()
    def create_order(self):
        #等待元素出现后，开始下面的代码
        locator = (By.ID, 'btn_create')
        WebDriverWait(self.driver, 10, 0.5).until(EC.presence_of_element_located(locator))
        #拖动滚动条到指定位置
        target = self.driver.find_element_by_id("btn_create")
        self.driver.execute_script("arguments[0].scrollIntoView();", target)
        target.click()
        self.driver.implicitly_wait(10)
        #判断radio是否被选中
        radioselected = self.driver.find_element_by_id("use_type_17")
        if radioselected.is_selected()==False:
            radioselected.click()
        self.driver.implicitly_wait(10)

        self.driver.find_element_by_name("start_position").click()
        self.driver.find_element_by_xpath("//*[contains(text(),'中谷酒店')]").click()
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_name("end_position").click()
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath("//*/div[@id='end_addrlist']/li/a[contains(text(),'北京西站')]").click()
        self.driver.implicitly_wait(10)
        #拖动滚动条到指定位置
        target1 = self.driver.find_element_by_xpath("//*/input[@type='submit']")
        self.driver.execute_script("arguments[0].scrollIntoView();", target1)

        self.driver.find_element_by_id("car_type").click()
        self.driver.find_element_by_xpath("//*/option[@value='37']").click()
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath("//*/select[@name='corporate_id']").click()
        self.driver.find_element_by_xpath("//*/option[@value='0']").click()
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath("//*/span[@id='self-use']").click()
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath("//*/input[@name='passenger_phone']").click()
        self.driver.implicitly_wait(10)
        #判断checkbox是否被选中
        is_auto_dispatch = self.driver.find_element_by_xpath("//*/input[@id='is_auto_0']")
        if is_auto_dispatch.is_selected() ==False:
            is_auto_dispatch.click()
        self.driver.implicitly_wait(10)

        send_message_to_passenger = self.driver.find_element_by_xpath("//*/input[@name='passenger']")
        if send_message_to_passenger.is_selected():
            send_message_to_passenger.click()
        self.driver.implicitly_wait(10)

        self.driver.find_element_by_xpath("//*/input[@type='submit']").click()
        self.driver.implicitly_wait(10)
    def send_order_to_alldrivers(self):
        target1 = self.driver.find_element_by_xpath("//*/input[@id='selectCarButton']")
        self.driver.execute_script("arguments[0].scrollIntoView();", target1)
        target1.click()
        self.driver.find_element_by_xpath("//*/a[@id='allCheck']").click()
        self.driver.find_element_by_xpath("//*/input[@id='formSub']").click()
        # 判断是否弹出Alert窗口，如果弹出就点击确定,并且返回True，不是就返回False
        result=EC.alert_is_present()(self.driver)
        if result:
            result.accept()
            print ("No driver")
            self.driver.get_screenshot_as_file("/Users/zhaolisi/PycharmProjects/ScreenShots/No_driver_found.png")
            return True
        else:
            return False
    def choose_driver(self):
        target2 = self.driver.find_element_by_xpath("//*/input[@id='driverCPhoneNumber']")
        self.driver.execute_script("arguments[0].scrollIntoView();", target2)
        target2.send_keys("16812345678")
        self.driver.find_element_by_xpath("//*/input[@id='selectCarButton']").click()
        self.driver.find_element_by_xpath("//*/input[@id='formSub']").click()
        #判断是否弹出Alert窗口，如果弹出就点击确定,并且返回True，不是就返回False
        result = EC.alert_is_present()(self.driver)
        if result:
            result.accept()
            print("The driver is not online")
            self.driver.get_screenshot_as_file("/Users/zhaolisi/PycharmProjects/ScreenShots/No_driver_found.png")
            return True
        else:
            print("The driver is online")
            return False
        '''
        #判断元素是否存在，如果存在就点击，不存在就保存图片，返回False
        if self.basepage.iselementexist("//*/input[@value='确定使用']") == True:
           self.driver.find_element_by_xpath("//*/input[@value='确定使用']").click()
           return True
        else:
            self.driver.get_screenshot_as_file("/Users/zhaolisi/PycharmProjects/ScreenShots/No_driver_found.png")
            return False
        '''
    def cancle_order(self):
        target3 = self.driver.find_element_by_xpath("//*/input[@value='取消订单']")
        self.driver.execute_script("arguments[0].scrollIntoView();", target3)
        target3.click()
        #time.sleep(1)
        locator = (By.ID, 'cancel_reason')
        WebDriverWait(self.driver, 10, 0.5).until(EC.element_to_be_clickable(locator))
        self.driver.find_element_by_xpath("//*/option[@value='12']").click()
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_id("J_cancel_submit").click()
        time.sleep(1)
        self.driver.switch_to.alert.accept()
        time.sleep(1)
    def quit_browser(self):
        self.basepage.quit_browser()