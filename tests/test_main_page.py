import allure
import pytest
from data import TestData
from pages.main_page import MainPage
from conftest import driver


class TestMainPageFAQ:
    @allure.title('Проверка текста раздела "Вопросы о важном" на главной странице')
    @pytest.mark.parametrize('question_number, expected_answer', TestData.test_question)
    def test_text_in_faq(self, driver, question_number, expected_answer):
        main_page = MainPage(driver)
        main_page.scroll_to_faq()
        main_page.wait_visibility_of_faq(question_number)
        main_page.click_on_faq(question_number)
        main_page.wait_visibility_of_faq_answer(question_number)
        assert main_page.get_displayed_text_from_faq(question_number) == expected_answer