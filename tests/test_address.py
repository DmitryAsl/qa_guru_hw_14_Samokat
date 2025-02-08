import allure
import pytest
from helpers.pages.main_page import MainPage
from helpers.data_provider import DataProvider


@pytest.mark.usefixtures('browser_config')
class TestAddress:
    @allure.title('Тест на проверку выбора адресса')
    def test_selection_address(self):
        main_page = MainPage()
        param = DataProvider.get('', 'address', 'selection_existing_address')

        main_page.open()
        main_page.address_selection_with_default_city(city=param['city'], address=param['address'])
        main_page.assert_selected_address(param['address'])
