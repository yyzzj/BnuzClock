from selenium import webdriver
from time import sleep

STUDENT_ID = ''  # 学号
PASSWORD = ''  # 密码
BODY_TEMPERATURE = '36.5'  # 体温
INFO_STATUS = '0'  # 下拉框的状态：0否 1是

browser = webdriver.Chrome()
browser.get('http://xgfx.bnuz.edu.cn/xsdtfw/sys/xsyqxxsjapp/*default/index.do?EMAP_LANG=zh#/mrbpa')

# 登录
sleep(1)
browser.find_elements_by_tag_name("button")[1].click()

# 输入账号密码
sleep(1)
browser.find_elements_by_tag_name("input")[0].send_keys(STUDENT_ID)
browser.find_elements_by_tag_name("input")[1].send_keys(PASSWORD)
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

# browser.close()
