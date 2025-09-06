from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.main_page_locators import MainPageLocators


class MainPage:
   class MainPage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def is_main_header_visible(self):
        return self.wait.until(EC.visibility_of_element_located(MainPageLocators.main_header))

    def click_order_button_main(self):
        order_btn = self.wait.until(EC.element_to_be_clickable(MainPageLocators.order_button_main))
        order_btn.click()

    def click_order_button_header(self):
        order_btn = self.wait.until(EC.element_to_be_clickable(MainPageLocators.order_button_header))
        order_btn.click()

    def click_faq_question(self, question_number):
        locator = MainPageLocators.faq_questions.get(question_number)
        if locator:
            element = self.wait.until(EC.element_to_be_clickable(tuple(locator)))
            element.click()
        else:
            raise ValueError(f"Вопрос с номером {question_number} не найден в локаторах.")

    def get_faq_answer_text(self, question_number):
        locator = MainPageLocators.faq_answers.get(question_number)
        if locator:
            element = self.wait.until(EC.visibility_of_element_located(tuple(locator)))
            return element.text
        else:
            raise ValueError(f"Ответ с номером {question_number} не найден в локаторах.")

    def is_faq_visible(self):
        return self.wait.until(EC.visibility_of_element_located(MainPageLocators.faq))

    def click_header_logo_scooter(self):
        logo = self.wait.until(EC.element_to_be_clickable(MainPageLocators.header_logo_scooter))
        logo.click()

    def click_header_logo_yandex(self):
        logo = self.wait.until(EC.element_to_be_clickable(MainPageLocators.header_logo_yandex))
        logo.click()
