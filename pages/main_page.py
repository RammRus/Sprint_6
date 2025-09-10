from selenium.webdriver.support.wait import WebDriverWait
from locators.main_page_locators import MainPageLocators
import allure


class MainPage:

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    @allure.step('Ожидание прогрузки главной страницы')
    def is_main_header_visible(self):
        return self.wait_visibility_of_element(MainPageLocators.main_header)

    @allure.step('Клик по кнопке "Заказать" на главной странице')
    def click_order_button_main(self):
        order_btn = self.wait.until(EC.element_to_be_clickable(MainPageLocators.order_button_main))
        order_btn.click()

    @allure.step('Клик по кнопке "Заказать" в шапке страницы')
    def click_order_button_header(self):
        order_btn = self.wait_clickable_of_element(MainPageLocators.order_button_header)
        order_btn.click()

    @allure.step('Клик по вопросу в разделе "Вопросы о важном"')
    def click_faq_question(self, question_number):
        locator = MainPageLocators.faq_questions.get(question_number)
        if locator:
            element = self.wait_clickable_of_element(tuple(locator))
            element.click()
        else:
            raise ValueError(f"Вопрос с номером {question_number} не найден в локаторах.")

    @allure.step('Получить текст ответа на вопрос в разделе "Вопросы о важном"')
    def get_faq_answer_text(self, question_number):
        locator = MainPageLocators.faq_answers.get(question_number)
        if locator:
            element = self.wait_visibility_of_element(tuple(locator))
            return element.text
        else:
            raise ValueError(f"Ответ с номером {question_number} не найден в локаторах.")

    @allure.step('Дождаться прогрузки раздела "Вопросы о важном"')
    def is_faq_visible(self):
        return self.wait_visibility_of_element(MainPageLocators.faq)

    @allure.step('Клик по логотипу "Самокат" в шапке главной страницы')
    def click_header_logo_scooter(self):
        logo = self.wait_clickable_of_element(MainPageLocators.header_logo_scooter)
        logo.click()

    @allure.step('Клик по логотипу "Яндекс" в шапке главной страницы')
    def click_header_logo_yandex(self):
        logo = self.wait_clickable_of_element(MainPageLocators.header_logo_yandex)
        logo.click()
