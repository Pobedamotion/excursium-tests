from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

FILTER_URL = "https://excursium.com/ekskursii-dlya-shkolnikov/list"

class TestFilter:

    def test_filters_open_by_default(self, driver):
        """EX-014: Все фильтры открыты по умолчанию"""
        driver.get(FILTER_URL)
        wait = WebDriverWait(driver, 10)

        filter_form = wait.until(EC.presence_of_element_located(
            (By.ID, "filter")))

        assert filter_form.is_displayed()

    def test_filter_shows_correct_results(self, driver):
        """EX-017: Фильтр показывает корректные результаты"""
        driver.get(FILTER_URL)
        wait = WebDriverWait(driver, 10)

        wait.until(EC.presence_of_element_located((By.ID, "filter")))
        time.sleep(2)

        # Кликаем через JavaScript на скрытый label
        label = driver.find_element(By.CLASS_NAME, "form-check-label")
        driver.execute_script("arguments[0].click();", label)

        time.sleep(2)

        results = driver.find_elements(
            By.XPATH, "//div[contains(@class,'card')]")
        assert len(results) > 0