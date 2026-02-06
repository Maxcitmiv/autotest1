from selene import browser, be, by, have
from selene.core.exceptions import TimeoutException


def test_browser():
    browser.open('https://www.ya.ru')
    browser.element('#text').type('hdbcsdcbsjkcdnsjdcnskjbdcjshdcbkjsdc').press_enter()
    browser.should(have.url_containing('https://ya.ru/search?text=hdbcsdcbsjkcdnsjdcnskjbdcjshdcbkjsdc'))
    try:
        browser.element('[aria-label="Нет, спасибо"]').should(be.visible).click()
    except TimeoutException:
        pass
    browser.element('.EmptySearchResults-Title').should(have.text('Ничего не нашли'))
    browser.element('.EmptySearchResults-Subtitle').should(have.text('Переформулируйте запрос или поищите что-нибудь ещё'))