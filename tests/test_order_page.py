import allure
import pytest
from conftest import driver
from data import *
from pages.order_page import OrderPage
from locators import main_page_locators



class TestOrderPage:

    @allure.title('Проверка позитивных сценариев оформления заказа')
    @pytest.mark.parametrize('button, test_data', [(main_page_locators.order_button_header, TestData.test_user_1),
                                                   (main_page_locators.order_button_main, TestData.test_user_2)])
    def test_order(self, driver, button, test_data):
        order_page = OrderPage(driver)
        order_page.scroll_to_element(button)
        order_page.wait_visibility_of_element(button)
        order_page.click_on_element(button)
        order_page.data_entry_first_form(test_data)
        order_page.data_entry_second_form(test_data)
        assert order_page.check_displaying_of_button_check_status_of_order()