from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pandas as pd
import time

USER = "自身の学籍番号"
PASS = "自身のパスワード"

# Chromeが開く
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')  # ヘッドレスモードを使用する場合は追加

browser = webdriver.Chrome(options=chrome_options)
browser.get('https://lcam.aitech.ac.jp/portalv2/')

elem_username = browser.find_element(By.NAME, "userID")
elem_username.send_keys(USER)

elem_password = browser.find_element(By.NAME, "password")
elem_password.send_keys(PASS)

elem_login_btn = browser.find_element(By.CLASS_NAME, "btn_login")
elem_login_btn.click()
print("ログイン成功です!")

time.sleep(0.5)

# 曜日とクラスのデータを格納するリスト
days = []
classes = []

for i in range(1, 8):  # 1から7までの曜日に対して繰り返し
    day_xpath = f"/html/body[@id='home']/div[@id='container']/div[@class='clearfix'][1]/div[@id='right-box-top']/form[1]/div[@class='center-module clear mt15']/div[@class='center-module-inner']/div[@class='schedule-box']/div[@id='ttb_sheet t_timetable']/table[@class='calendar-body']/thead/tr/th[{i}]"
    class_xpath = f"/html/body[@id='home']/div[@id='container']/div[@class='clearfix'][1]/div[@id='right-box-top']/form[1]/div[@class='center-module clear mt15']/div[@class='center-module-inner']/div[@class='schedule-box']/div[@id='ttb_sheet t_timetable']/table[@class='calendar-body']/tbody/tr/td[{i}]/div[@class='div_content_reference']"

    day = browser.find_element(By.XPATH, day_xpath).text
    class_data = browser.find_element(By.XPATH, class_xpath).text

    days.append(day)
    classes.append(class_data)

# WebDriverの終了
browser.close()
browser.quit()

# CSVファイルに保存
df = pd.DataFrame({"Day": days, "Class": classes})
df.to_csv("./public/csv/class_schedule.csv", index=False)

print("CSVファイルに保存しました。")
