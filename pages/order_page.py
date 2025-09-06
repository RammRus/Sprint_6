from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.order_page_locators import OrderPageLocators
from data import *

class OrderPage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def scroll_to_element(self, locator):
        element = self.wait.until(EC.presence_of_element_located(locator))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

    def wait_visibility_of_element(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def click_on_element(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    def data_entry_first_form(self, test_data):
        name, lastname, address, metro_station, phone, _ = test_data

        name_input = self.wait_visibility_of_element(OrderPageLocators.name)
        name_input.clear()
        name_input.send_keys(name)

        lastname_input = self.wait_visibility_of_element(OrderPageLocators.lastname)
        lastname_input.clear()
        lastname_input.send_keys(lastname)

        address_input = self.wait_visibility_of_element(OrderPageLocators.address)
        address_input.clear()
        address_input.send_keys(address)

        metro_input = self.wait_visibility_of_element(OrderPageLocators.metro)
        metro_input.clear()
        metro_input.send_keys(metro_station)

        # Ждём и выбираем первый вариант из списка
        self.wait_visibility_of_element(OrderPageLocators.select_metro)
        first_option = self.driver.find_element(*OrderPageLocators.select_metro)
        first_option.click()

        phone_input = self.wait_visibility_of_element(OrderPageLocators.phone)
        phone_input.clear()
        phone_input.send_keys(phone)

        self.click_on_element(OrderPageLocators.button_next)
        self.wait_visibility_of_element(OrderPageLocators.title_page_rent)

    def data_entry_second_form(self, test_data):
        _, _, _, _, _, date = test_data

        date_input = self.wait_visibility_of_element(OrderPageLocators.data)
        date_input.clear()
        date_input.send_keys(date)

        # Выбор срока аренды
        rental_period = self.wait_visibility_of_element(OrderPageLocators.rental_period)
        rental_period.click()

        # Выбираем "сутки" из выпадающего списка
        option = self.wait.until(EC.element_to_be_clickable(OrderPageLocators.dropdown_rental_period))
        option.click()

        # Выбор цвета самоката (серый)
        color_grey = self.wait_visibility_of_element(OrderPageLocators.color_scooter)
        color_grey.click()

        comment_input = self.wait_visibility_of_element(OrderPageLocators.comment)
        comment_input.clear()
        comment_input.send_keys("Пожалуйста, позвоните за 5 минут до приезда.")

        self.click_on_element(OrderPageLocators.button_make_order)
        self.click_on_element(OrderPageLocators.button_yes)

    def check_displaying_of_button_check_status_of_order(self):
        try:
            button = self.wait_visibility_of_element(OrderPageLocators.button_check_status_order)
            return button.is_displayed()
        except:
            return False