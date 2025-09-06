from selenium.webdriver.common.by import By


class OrderPageLocators:
    title_page_personal = (By.XPATH, "//div[text()='Для кого самокат']")
    name = (By.XPATH, "//input[@placeholder='* Имя']")
    lastname = (By.XPATH, "//input[@placeholder ='* Фамилия']")
    address = (By.XPATH, "//input[@placeholder = '* Адрес: куда привезти заказ']")
    metro = (By.XPATH, "//input[@placeholder = '* Станция метро']")
    select_metro = (By.XPATH, ".//li[@class='select-search__row']")
    phone = (By.XPATH, "//input[@placeholder ='* Телефон: на него позвонит курьер']")
    button_next = (By.XPATH, "//button[text()='Далее']")
    title_page_rent = (By.XPATH, "//div[@class='Order_Header__BZX0b' and text()='Про аренду']")
    data = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    calendar = (By.XPATH, "//div[@class='react-datepicker-popper']")
    calendar_item = (By.XPATH, "//div[contains(@class, 'react-datepicker') and contains(@tabindex, '0')]")
    rental_period = (By.XPATH, ".//div[text()='* Срок аренды']")
    dropdown_rental_period = (By.XPATH, ".//div[@class='Dropdown-menu']/div[text()='сутки']")
    color_scooter = (By.XPATH, "//input[@id='grey']")
    comment = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    button_make_order = (By.XPATH, "//div[contains(@class, 'Order_Buttons')]/button[text()='Заказать']")
    button_yes = (By.XPATH, "//button[text()='Да']")
    button_check_status_order = (By.XPATH, ".//*[text()='Посмотреть статус']")