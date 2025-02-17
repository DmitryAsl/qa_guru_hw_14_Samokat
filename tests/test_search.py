import allure
import pytest
from helpers.pages.main_page import MainPage
from helpers.data_provider import DataProvider
from tests.conftest import browser_config


class TestsSearchProduct:
    main_page = MainPage()

    @allure.title('Тест на поиск товара')
    def test_search_product_positive(self):
        param = DataProvider.get('', 'search', 'search_positive')

        self.main_page.open()
        self.main_page.search_product(param['title'])
        self.main_page.assert_result_search(param['title'])

    @allure.title('Тест на поиск несуществующего товара')
    def test_search_product_negative(self):
        param = DataProvider.get('', 'search', 'search_negative')

        self.main_page.open()
        self.main_page.search_product(param['title'])
        self.main_page.assert_result_search(positive=False)
