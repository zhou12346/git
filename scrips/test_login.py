import os
import sys

import allure

sys.path.append(os.getcwd())
class TestLogin:
    @allure.step("新增地址方法执行")
    def test01(self):
        allure.attach("新增地址按钮","")
        allure.attach("新增地址按钮", "")
        allure.attach("新增联系人", "")
        allure.attach("新增手机号码", "")
        allure.attach("新增收货地址", "")
        print("texto1")

    @allure.step("更新地址")
    def test02(self):

        print("texto3")