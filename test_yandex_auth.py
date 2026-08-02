import os
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait


class TestYandexAuth(unittest.TestCase):
    def setUp(self):
        """Инициализация веб-драйвера перед каждым тестом."""
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])

        self.driver = webdriver.Chrome(options=options)
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 10)

    def test_authorization(self):
        """Тестирование процесса авторизации на Яндексе."""
        self.driver.get("https://passport.yandex.ru/auth/")

        login = os.getenv("YANDEX_LOGIN", "твой_логин")
        password = os.getenv("YANDEX_PASSWORD", "твой_пароль")

        # 1. Ожидание поля логина и ввод
        login_input = self.wait.until(
            ec.presence_of_element_located((By.XPATH, "//*[@id='passp-field-login']"))
        )
        login_input.send_keys(login)

        # 2. Клик по кнопке входа
        sign_in_button = self.wait.until(
            ec.element_to_be_clickable((By.XPATH, "//*[@id='passp:sign-in']"))
        )
        sign_in_button.click()

        # 3. Ожидание поля пароля и ввод
        password_input = self.wait.until(
            ec.presence_of_element_located((By.XPATH, "//*[@id='passp-field-passwd']"))
        )
        password_input.send_keys(password)

        # 4. Клик по кнопке входа для пароля
        sign_in_button_pwd = self.wait.until(
            ec.element_to_be_clickable((By.XPATH, "//*[@id='passp:sign-in']"))
        )
        sign_in_button_pwd.click()

        # 5. Проверка успешного редиректа
        self.wait.until(ec.url_contains("id.yandex.ru"))
        self.assertNotIn("auth", self.driver.current_url)

    def tearDown(self):
        """Закрытие браузера."""
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
