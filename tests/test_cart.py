import pytest
from helpers.pages.main_page import MainPage
from helpers.data_provider import DataProvider


@pytest.mark.usefixtures('browser_with_selected_address')
class TestCart:

    def test_add_single_item_to_cart(self):
        main_page = MainPage()
        param = DataProvider.get('', 'cart', 'add_single_product')

        try:
            main_page.search_product(param['product_name'])
            main_page.add_product_to_cart(param['product_name'])
            main_page.assert_result_addition_product_to_cart(param['product_name'])

            main_page.should_have_count_product_in_cart(param['quantity'])
        finally:
            main_page.clear_cart()

    def test_remove_item_from_cart(self):
        main_page = MainPage()

        param = DataProvider.get('', 'cart', 'remove_product')
        try:
            main_page.search_product(param['search_phrace'])
            main_page.add_product_to_cart(param['product_name'])
            main_page.should_have_count_product_in_cart(param['quantity'])
            main_page.remove_product_from_cart(param['product_name'])

            main_page.assert_empty_cart()
        finally:
            main_page.clear_cart()

    def test_total_price_by_cart(self):
        main_page = MainPage()
        param = DataProvider.get('', 'cart', 'check_total_price')
        try:
            main_page.search_product(param['search_phrace'])
            main_page.add_product_to_cart(param['product_name_1'])
            main_page.add_product_to_cart(param['product_name_2'])
            main_page.add_product_to_cart(param['product_name_3'])

            main_page.should_have_count_product_in_cart(param['quantity'])
            main_page.assert_total_cost_by_cart()
        finally:
            main_page.clear_cart()
