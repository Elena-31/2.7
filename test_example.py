class TestExample: #Test Suite
    def test_example_1(self, set_up_browser):  #Test Case
        driver = set_up_browser
        driver.get("https://skillbox.ru")
        assert 'Skillbox - образовательная платформа с онлайн-курсами' == driver.title

    def test_example_2(self, set_up_browser):  # Test Case
            driver = set_up_browser
            driver.get("https://skillbox.ru")
            assert 'Skillbox - образовательная платформа с онлайн-курсами' == driver.title

    def test_example_3(self, set_up_browser):  #Test Case
        driver = set_up_browser
        driver.get("https://skillbox.ru")
        assert 'Skillbox - образовательная платформа с онлайн-курсами' == driver.title

    def test_example_4(self, set_up_browser):  #Test Case
        driver = set_up_browser
        driver.get("https://skillbox.ru")
        assert 'Skillbox - образовательная платформа с онлайн-курсами' == driver.title