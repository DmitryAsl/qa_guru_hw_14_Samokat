import allure
import pytest
from helpers.pages.main_page import MainPage
from helpers.data_provider import DataProvider
from tests.conftest import browser_config


@pytest.mark.usefixtures('browser_config')
class TestsSearchProduct:
    @allure.title('Тест на поиск товара')
    def test_search_product_positive(self):
        main_page = MainPage()
        param = DataProvider.get('', 'search', 'search_positive')

        main_page.open()
        main_page.search_product(param['title'])
        main_page.assert_result_search(param['title'])

    @allure.title('Тест на поиск несуществующего товара')
    def test_search_product_negative(self):
        main_page = MainPage()
        param = DataProvider.get('', 'search', 'search_negative')

        main_page.open()
        main_page.search_product(param['title'])
        main_page.assert_result_search(positive=False)
