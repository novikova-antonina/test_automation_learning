import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By


LANGUAGES_DATA = [
    {"lang": "ar",      "expected": "العربيّة"},
    {"lang": "ca",      "expected": "català"},
    {"lang": "cs",      "expected": "čeština"},
    {"lang": "da",      "expected": "dansk"},
    {"lang": "de",      "expected": "Deutsch"},
    {"lang": "en-gb",   "expected": "British English"},
    {"lang": "el",      "expected": "Ελληνικά"},
    {"lang": "es",      "expected": "español"},
    {"lang": "fi",      "expected": "suomi"},
    {"lang": "fr",      "expected": "français"},
    {"lang": "it",      "expected": "italiano"},
    {"lang": "ko",      "expected": "한국어"},
    {"lang": "nl",      "expected": "Nederlands"},
    {"lang": "pl",      "expected": "polski"},
    {"lang": "pt",      "expected": "Português"},
    {"lang": "pt-br",   "expected": "Português Brasileiro"},
    {"lang": "ro",      "expected": "Română"},
    {"lang": "ru",      "expected": "Русский"},
    {"lang": "sk",      "expected": "Slovensky"},
    {"lang": "uk",      "expected": "Українська"},
]


def main():
    browser = webdriver.Chrome()
    for data in LANGUAGES_DATA:
        language = data["lang"]
        link = f"http://selenium1py.pythonanywhere.com/{language}/"
        browser.get(link)
        print(f"[{language}] Открыт URL: {link}")
        browser.find_element(By.CSS_SELECTOR, "#login_link")
        print(f"[{language}] Элемент 'login_link' найден")

    browser.quit()


@pytest.fixture(scope="function")
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


test_languages = [data["lang"] for data in LANGUAGES_DATA]


@pytest.mark.parametrize("language", test_languages)
def test_guest_should_see_login_link(browser, language):
    link = f"http://selenium1py.pythonanywhere.com/{language}/"
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, "#login_link")


if __name__ == "__main__":
    main()
