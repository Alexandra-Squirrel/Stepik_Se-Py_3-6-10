import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


class Test_lesson_3_6_10():
    # pytest.mark.parametrize = method without cmd "--language"
    # @pytest.mark.parametrize('language', ["ru", "es", "fr", "zh-hans", "ko", "en-gb"])
    def test_browser_locale(self, browser):
        # link for pytest.mark.parametrize
        # link = f"http://selenium1py.pythonanywhere.com/{language}/catalogue/coders-at-work_207"
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"

        # start browser
        browser.get(link)
        time.sleep(10)

        # assert
        add_2_cart_bttn = browser.find_elements(By.CLASS_NAME, "btn-add-to-basket")
        assert len(add_2_cart_bttn) > 0, "Кнопка не найдена!"

