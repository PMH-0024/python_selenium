import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
def get_all_information_to_excel(output_file = "Ma_so_thue_doanh_nghiep.xlsx"):
    try:
        all_information_page_dict = {}
        driver.get("https://thuvienphapluat.vn/ma-so-thue/tra-cuu-ma-so-thue-doanh-nghiep")
        for page in range(1, 5):
            print(f"Đang lấy thông tin trang {page}")
            rows_value = "#dvResultSearch > table > tbody > tr"
            elements_rows = driver.find_elements(By.CSS_SELECTOR, rows_value)
            information_page_array = []
            for row in elements_rows:
                try:
                    Ma_so_thue_doanh_nghiep_value = "td:nth-child(2) > a"
                    element_Ma_so_thue_doanh_nghiep = row.find_element(By.CSS_SELECTOR, Ma_so_thue_doanh_nghiep_value)
                    ten_doanh_nghiep_value = "td:nth-child(3) > div > a"
                    element_ten_doanh_nghiep = row.find_element(By.CSS_SELECTOR, ten_doanh_nghiep_value)
                    ngay_cap_value ="td:nth-child(4)"
                    element_ngay_cap = row.find_element(By.CSS_SELECTOR, ngay_cap_value)
                    information_page_array.append({
                        "Mã số thuế": element_Ma_so_thue_doanh_nghiep.text,
                        "Tên doanh nghiệp": element_ten_doanh_nghiep.text,
                        "Ngày cấp": element_ngay_cap.text
                    })
                except Exception as error:
                    print(error)
            all_information_page_dict[f"Trang_{page}"] = pd.DataFrame(information_page_array)
            if page < 4:
                try:
                    btn_value = "#dvResultSearch > div.d-flex.justify-content-end > nav > ul > li.page-item.active"
                    element_btn=driver.find_element(By.CSS_SELECTOR, btn_value)
                    element_btn.click()
                except Exception as error:
                    print(error)
                    break
            with pd.ExcelWriter(output_file, engine="openpyxl") as writer:
                for sheet_name, df_information in all_information_page_dict.items():
                    df_information.to_excel(writer, sheet_name=sheet_name, index=False)
            print(f"Đã lưu vào: {output_file}")
        print("Lưu thành công")
    finally:
        driver.quit()
if __name__ == "__main__":
    get_all_information_to_excel("Ma_so_thue_doanh_nghiep.xlsx")