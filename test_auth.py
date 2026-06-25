from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = "https://excursium.com/Client/Login"

class TestAuth:

    def test_successful_login(self, driver):
        """EX-001: Успешная авторизация с валидными данными"""
        driver.get(BASE_URL)
        wait = WebDriverWait(driver, 10)

        login_tab = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//button[contains(text(),'Вход')]")))
        login_tab.click()

        email = wait.until(EC.presence_of_element_located(
            (By.XPATH, "//input[@placeholder='Ваша электронная почта']")))
        email.send_keys("doorgaliyo@gmail.com")

        password = driver.find_element(
            By.XPATH, "//input[@placeholder='Ваш пароль']")
        password.send_keys("sdkgjjskfghj")

        driver.find_element(By.ID, "login-btn").click()

        # Исправили URL — после входа открывается Startup или cabinet
        wait.until(EC.url_contains(("Startup" or "cabinet")))
        assert "Startup" in driver.current_url or "cabinet" in driver.current_url

    def test_wrong_password(self, driver):
        """EX-002: Авторизация с неверным паролем"""
        driver.get(BASE_URL)
        wait = WebDriverWait(driver, 10)

        login_tab = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//button[contains(text(),'Вход')]")))
        login_tab.click()

        email = wait.until(EC.presence_of_element_located(
            (By.XPATH, "//input[@placeholder='Ваша электронная почта']")))
        email.send_keys("doorgaliyo@gmail.com")

        password = driver.find_element(
            By.XPATH, "//input[@placeholder='Ваш пароль']")
        password.send_keys("неверный_пароль123")

        driver.find_element(By.ID, "login-btn").click()

        # Ищем сообщение об ошибке по тексту
        error = wait.until(EC.presence_of_element_located(
            (By.XPATH, "//*[contains(text(),'Неверная почта')]")))
        assert error.is_displayed()