import allure
import pytest
from helpers.pages.main_page import MainPage
from helpers.data_provider import DataProvider


class TestCart:
    main_page = MainPage()

    @allure.title('Тест на добавление товара в корзину')
    def test_add_single_item_to_cart(self, browser_with_selected_address):
        param = DataProvider.get('', 'cart', 'add_single_product')

        try:
            self.main_page.search_product(param['product_name'])
            self.main_page.add_product_to_cart(param['product_name'])
            self.main_page.assert_result_addition_product_to_cart(param['product_name'])

            self.main_page.should_have_count_product_in_cart(param['quantity'])
        finally:
            self.main_page.clear_cart()

    @allure.title('Тест на удаление товара из корзины')
    def test_remove_item_from_cart(self, browser_with_selected_address):
        param = DataProvider.get('', 'cart', 'remove_product')

        try:
            self.main_page.search_product(param['search_phrace'])
            self.main_page.add_product_to_cart(param['product_name'])
            self.main_page.should_have_count_product_in_cart(param['quantity'])
            self.main_page.remove_product_from_cart(param['product_name'])

            self.main_page.assert_empty_cart()
        finally:
            self.main_page.clear_cart()

    @allure.title('Тест на проверку корректности расчета стоимости корзины')
    def test_total_price_by_cart(self, browser_with_selected_address):
        param = DataProvider.get('', 'cart', 'check_total_price')

        try:
            self.main_page.search_product(param['search_phrace'])
            self.main_page.add_product_to_cart(param['product_name_1'])
            self.main_page.add_product_to_cart(param['product_name_2'])
            self.main_page.add_product_to_cart(param['product_name_3'])

            self.main_page.should_have_count_product_in_cart(param['quantity'])
            self.main_page.assert_total_cost_by_cart()
        finally:
            self.main_page.clear_cart()
