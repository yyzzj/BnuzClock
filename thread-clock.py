from selenium import webdriver
from time import sleep
from threading import Thread

# 多线程版本
INFO = {  # 学生列表
    "yzj": {  # 学生1
        "id": "",  # 学号
        "password": ""  # 密码
    },
    "tl": {  # 学生2
        "id": "",  # 学号
        "password": ""  # 密码
    }
}

BODY_TEMPERATURE = '36.5'  # 体温
INFO_STATUS = '0'  # 下拉框的状态：0否 1是


def main_method(student_info_id, student_info_password):
    # browser = webdriver.Chrome(executable_path="chromedriver.exe")
    browser = webdriver.Chrome()
    browser.get('http://xgfx.bnuz.edu.cn/xsdtfw/sys/xsyqxxsjapp/*default/index.do?EMAP_LANG=zh#/mrbpa')

    # 登录
    sleep(1)
    browser.find_elements_by_tag_name("button")[1].click()

    # 输入账号密码
    sleep(1)
    browser.find_elements_by_tag_name("input")[0].send_keys(student_info_id)
    browser.find_elements_by_tag_name("input")[1].send_keys(student_info_password)
    browser.find_element_by_tag_name("button").click()

    # # 进入编辑页面
    # sleep(6)
    # browser.find_elements_by_link_text("编辑")[0].click()

    # 填入每日情况
    # 填入体温
    sleep(6)
    temperature = browser.find_element_by_xpath("//input[@data-caption='体温']")
    temperature.clear()
    temperature.send_keys(BODY_TEMPERATURE)

    # 下拉框值的填入
    for num in range(6, 15, 2):
        a1 = browser.find_element_by_xpath("/html/body/main/article/section/div[2]/div[2]/div/div[2]/div[2]/div[" + str(
            num) + "]/div/div/div[2]/input")
        browser.execute_script("arguments[0].setAttribute(arguments[1],arguments[2])", a1, 'value', INFO_STATUS)

    # 获取保存按钮，提交保存
    sub = browser.find_element_by_xpath("/html/body/main/article/footer/a[1]")
    browser.execute_script("arguments[0].click();", sub)

    # 关闭浏览器
    browser.close()


if __name__ == '__main__':

    threads = []
    files = range(len(INFO))  # range(0,2)

    # 创建线程
    for student_info in INFO.values():
        thread = Thread(target=main_method, args=(student_info["id"], student_info["password"]))
        threads.append(thread)

    # 启动线程
    for i in files:
        threads[i].start()

    for i in files:
        threads[i].join()
