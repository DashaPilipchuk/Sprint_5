from locators import Locators


class TestSectionConstructor:

    def test_go_to_section_sauces(self, driver):
        sauces = driver.find_element(*Locators.SAUCES)
        driver.execute_script("arguments[0].scrollIntoView();", sauces)
        assert "Соусы" in sauces.text

    def test_go_to_section_fillings(self, driver):
        fillings = driver.find_element(*Locators.FILLINGS)
        driver.execute_script("arguments[0].scrollIntoView();", fillings)
        assert "Начинки" in fillings.text

    def test_go_to_section_rolls(self, driver):
        fillings = driver.find_element(*Locators.FILLINGS)
        driver.execute_script("arguments[0].scrollIntoView();", fillings)
        rolls = driver.find_element(*Locators.ROLLS)
        driver.execute_script("arguments[0].scrollIntoView();", rolls)
        assert "Булки" in rolls.text


