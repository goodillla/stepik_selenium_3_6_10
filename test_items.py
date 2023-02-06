import time

from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_guest_should_see_add_to_cart_button(browser):
    browser.get(link)
    add_to_basket_button = browser.find_elements(By.CSS_SELECTOR, "button.btn-add-to-basket")
    #print(len(add_to_basket_button))    #для отладки
    #add_to_basket_button = []           #для проверки ассерта
    assert len(add_to_basket_button) == 1, 'Кнопка "Добавить в корзину" не найдена!'
    time.sleep(10)