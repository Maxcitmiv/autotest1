import os.path
import pytest
from selene import browser, have, be, by, command, query

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

#локаторы
firstName=browser.element('#firstName')
lastName=browser.element('[placeholder="Last Name"]')
userEmail=browser.element('#userEmail')
radiobuttonMale=browser.element('label[for="gender-radio-1"]')
userNumber=browser.element('#userNumber')
dateOfBirthInput=browser.element('#dateOfBirthInput')
yearselect=browser.element('.react-datepicker__year-select')
mounthselect=browser.element('.react-datepicker__month-select')
subjectsInput=browser.element('#subjectsInput')
hobbies_checkbox_1=browser.element('label[for="hobbies-checkbox-1"]')
uploadPicture=browser.element('#uploadPicture')
currentAddress=browser.element('#currentAddress')
state=browser.element('#state')
city=browser.element('#city')
cityintput=browser.element('#react-select-4-input')
submit=browser.element('#submit')
modalka=browser.element(by.text('Thanks for submitting the form'))
modal_rows=browser.all('.modal-body tbody tr')
button_close_modal=browser.element('#closeLargeModal')

def test_firstname(data_user):
    browser.open('https://demoqa.com/automation-practice-form')
    firstName.click()
    firstName.type(data_user['fname'])

def test_lastname(data_user):
    lastName.click()
    lastName.type(data_user['lname'])

    userEmail.click()
    userEmail.type(data_user['email'])

    radiobuttonMale.click()

    userNumber.should(be.visible).type(data_user['phone']).should(have.value(data_user['phone']))

def test_date(data_user):
    year=data_user['year']
    month=data_user['month']
    day=data_user['day']
    dateOfBirthInput.perform(command.js.scroll_into_view)
    dateOfBirthInput.should(be.visible).click()
    yearselect.click()
    browser.element(f'[value="{year}"]').click()
    mounthselect.click()
    browser.element(by.text(month)).click()
    browser.element(f'[aria-label*="{month} {day}th, {year}"]').click()
    dateOfBirthInput.should(have.value(f'{day:02d} {month[:3]} {year}'))

def test_subject(data_user):
    subjectsInput.type(data_user['subjects']).should(have.value(data_user['subjects']))
    hobbies_checkbox_1.click()

def test_file():
    testfile = os.path.abspath('test_data/image/testimage.png')
    uploadPicture.send_keys(testfile)

def test_address(data_user):
    (currentAddress.type(data_user['address'])
     .should(have.value(data_user['address'])))

    cityintput.should(have.attribute('disabled'))

    state.click()
    browser.element(by.text(data_user['sstate'])).click()
    state.should(have.text(data_user['sstate']))

    city.click()
    browser.element(by.text(data_user['ccity']))
    city.should(have.text(data_user['ccity']))

    submit.click()

def get_rows():
    rows={}
    for row in modal_rows:
        cells=row.all('td')
        label=cells[0].get(query.text)
        value=cells[1].get(query.text)
        rows[label]=value

    return rows

def test_modalwindow(data_user):

    modalka.should(be.visible)

    modal_data= {
        'Student Name': f'{data_user["fname"]} {data_user["lname"]}',
        'Student Email': data_user['email'],
        'Gender': 'Male',
        'Mobile': data_user['phone'],
        'Date of Birth': f'{data_user["day"]:02d} {data_user["month"]},{data_user["year"]}',
        'Subjects': '',
        'Hobbies': 'Sports',
        'Picture': f'testimage.png',
        'Address': f'{data_user["address"]}',
        'State and City': '',
    }
    actual_data=get_rows()
    assert modal_data==actual_data

def test_closemodal():
    button_close_modal.perform(command.js.scroll_into_view).click()
    modalka.should(be.not_.visible)

def test_conflict():
    print('Макаки нападают')