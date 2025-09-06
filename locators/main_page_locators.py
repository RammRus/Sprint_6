from selenium.webdriver.common.by import By


class MainPageLocators:
    main_header = (By.XPATH, "//div[contains(@class, 'Home_Header__iJKdX')]")
    faq = (By.XPATH, "//div[contains(@class, 'Home_FAQ')]")
    faq_questions = {
        1: [By.XPATH, "//div[@id='accordion__heading-0']/parent::div"],
        2: [By.XPATH, "//div[@id='accordion__heading-1']/parent::div"],
        3: [By.XPATH, "//div[@id='accordion__heading-2']/parent::div"],
        4: [By.XPATH, "//div[@id='accordion__heading-3']/parent::div"],
        5: [By.XPATH, "//div[@id='accordion__heading-4']/parent::div"],
        6: [By.XPATH, "//div[@id='accordion__heading-5']/parent::div"],
        7: [By.XPATH, "//div[@id='accordion__heading-6']/parent::div"],
        8: [By.XPATH, "//div[@id='accordion__heading-7']/parent::div"]
    }

    faq_answers = {
        1: [By.XPATH, "//div[@id='according__panel-0']"],
        2: [By.XPATH, "//div[@id='according__panel-1']"],
        3: [By.XPATH, "//div[@id='according__panel-2']"],
        4: [By.XPATH, "//div[@id='according__panel-3']"],
        5: [By.XPATH, "//div[@id='according__panel-4']"],
        6: [By.XPATH, "//div[@id='according__panel-5']"],
        7: [By.XPATH, "//div[@id='according__panel-6']"],
        8: [By.XPATH, "//div[@id='according__panel-7']"]
    }

    order_button_main = (By.XPATH, "//div[contains(@class, 'Home_FinishButton')]/button")
    order_button_header = (By.XPATH, "//div[contains(@class, 'Header_Nav__AGCXC')]/button[text()='Заказать']")
    header_logo_scooter = (By.XPATH, "//div/a[@class='Header_LogoScooter__31sAR']")
    header_logo_yandex = (By.XPATH, "//div/a[@class='Header_LogoYandex__3TSOI']")
    