import pytest
from helpers.pages.main_page import MainPage
from helpers.data_provider import DataProvider


@pytest.mark.usefixtures('browser_with_selected_address')
class TestsSearchProduct:
    def test_search_product_positive(self):
        main_page = MainPage()
        param = DataProvider.get('', 'search', 'search_positive')

        main_page.search_product(param['title'])
        main_page.assert_result_search(param['title'])

    def test_search_product_negative(self):
        main_page = MainPage()
        param = DataProvider.get('', 'search', 'search_negative')

        main_page.search_product(param['title'])
        main_page.assert_result_search(positive=False)
