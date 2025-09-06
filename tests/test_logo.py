import allure
from conftest import driver
from pages.main_page import MainPage

class TestLogo:
    @allure.title('Проверка перехода на главную страницу сайти при клике на лого "Самокат" в шапке')
    def test_logo_scooter(self, driver):
        main_page = MainPage(driver)
        main_page.wait_visibility_of_order_button_in_header()
        main_page.click_on_order_button_in_header()
        main_page.wait_visibility_of_header_logo_scooter()
        main_page.click_on_header_logo_scooter()
        main_page.wait_visibility_of_main_header()
        assert main_page.check_displaying_of_main_header()


    @allure.title('Проверка перехода на сайь "Дзен" при клике на лого "Яндекс"')
    def test_logo_yandex(self, driver):
        main_page = MainPage(driver)
        main_page.wait_visibility_of_header_logo_yandex()
        main_page.click_on_header_logo_yandex()
        main_page.switch_to_next_tab()
        assert main_page.get_page_title() == 'Дзен'


