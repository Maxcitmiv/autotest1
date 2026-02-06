import pytest
from selene import browser

@pytest.fixture
def data_user():
    return {
        'fname': 'Maxim',
        'lname':'Makak',
        'email': 'sobaka@mail.ru',
        'phone': '1234567890',
        'year': 2002,
        'month':'February',
        'day': 8,
        'subjects': 'Бибизяна',
        'address': 'LasVegas, Советская, 25',
        'sstate': 'NCR',
        'ccity': 'Delhi',
    }

@pytest.fixture(autouse=True)
def browser_function():
    browser.config.window_width = 1920
    browser.config.window_height = 1080