from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com")
# user
css_user_name = "user-name"
id_input = "user-name"
# password
id_pass = "password"
# login
id_btn = "login-button"
input("login tài khoản để vào trang sản phẩm")
# //*[@id="item_4_title_link"]/div
# //*[@id="item_0_title_link"]/div
# //*[@id="item_1_title_link"]/div
# //*[@id="item_2_title_link"]/div
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "inventory_item"))
)
# Lấy dữ liệu sản phẩm
value_titles = driver.find_elements(By.CLASS_NAME, "inventory_item_name")
value_prices = driver.find_elements(By.CLASS_NAME, "inventory_item_price")
data = []
for i in range(len(value_titles)):
    title = value_titles[i].text
    price = value_prices[i].text
    data.append({"Tên sản phẩm": title, "Giá": price})
# Lưu vào Excel
df = pd.DataFrame(data)
excel_path = r"C:\Users\Admin\Downloads\luu_sanpham_gia.xlsx"
df.to_excel(excel_path, index=False)
print(f"thông báo lưu sản phẩm: {excel_path}")
input("Nhấn Enter để đóng trình duyệt...")
driver.quit()