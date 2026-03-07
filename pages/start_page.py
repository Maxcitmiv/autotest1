from pathlib import Path

from selene import browser, by, be, have, command, query


class StartPage:
    def __init__(self):
        self.firstName = browser.element('#firstName')
        self.lastName = browser.element('[placeholder="Last Name"]')
        self.userEmail = browser.element('#userEmail')
        self.radiobuttonMale = browser.element('label[for="gender-radio-1"]')
        self.userNumber = browser.element('#userNumber')
        self.dateOfBirthInput = browser.element('#dateOfBirthInput')
        self.yearselect = browser.element('.react-datepicker__year-select')
        self.mounthselect = browser.element('.react-datepicker__month-select')
        self.subjectsInput = browser.element('#subjectsInput')
        self.hobbies_checkbox_1 = browser.element('label[for="hobbies-checkbox-1"]')
        self.uploadPicture = browser.element('#uploadPicture')
        self.currentAddress = browser.element('#currentAddress')
        self.state = browser.element('#state')
        self.city = browser.element('#city')
        self.cityintput = browser.element('#react-select-4-input')
        self.submit = browser.element('#submit')
        self.modalka = browser.element(by.text('Thanks for submitting the form'))
        self.modal_rows = browser.all('.modal-body tbody tr')
        self.button_close_modal = browser.element('#closeLargeModal')
        self.url = '/automation-practice-form'

    def open_page(self):
        browser.open(self.url)

    def firstname_fill(self, name):
        self.firstName.click().type(name)

    def lastname_fill(self, lastname):
        self.lastName.click().type(lastname)
    def fill_email(self, email):
        self.userEmail.click().type(email)

    def fill_gender(self):
        self.radiobuttonMale.click()

    def fill_phone(self, phone):
        self.userNumber.should(be.visible).type(phone).should(have.value(phone))

    def fill_dateofbirth(self, year, month, day):
        self.dateOfBirthInput.should(be.visible).click()
        self.yearselect.click()
        browser.element(f'[value="{year}"]').click()
        self.mounthselect.click()
        browser.element(by.text(month)).click()
        browser.element(f'[aria-label*="{month} {day}th, {year}"]').click()
        self.dateOfBirthInput.should(have.value(f'{day:02d} {month[:3]} {year}'))

    def fill_subjects(self, subject):
        self.subjectsInput.type(subject).press_enter()

    def fill_hobbies(self):
        self.hobbies_checkbox_1.click()

    def uploadpicture(self):
        base_dir = Path(__file__).resolve().parent.parent
        testfile = base_dir / 'test_data' / 'image' / 'testimage.png'
        self.uploadPicture.send_keys(str(testfile))
        return self

    def fill_address(self, address):
        (self.currentAddress.perform(command.js.scroll_into_view).type(address)
         .should(have.value(address)))
        return self

    def fill_city_and_state(self, cccity, ssstate):
        self.cityintput.should(have.attribute('disabled'))

        self.state.click()
        browser.element(by.text(ssstate)).click()
        self.state.should(have.text(ssstate))

        self.city.click()
        browser.element(by.text(cccity)).click()
        self.city.should(have.text(cccity))
        return self

    def pess_submit(self):
        self.submit.click()

    def get_rows(self):
        rows = {}
        for row in self.modal_rows:
            cells = row.all('td')
            label = cells[0].get(query.text)
            value = cells[1].get(query.text)
            rows[label] = value

        return rows

    def should_user_data(self, firstname, lastname, email, phone, day, month, year, subject, address, state, city):
        self.modalka.should(be.visible)

        modal_data = {
            'Student Name': f'{firstname} {lastname}',
            'Student Email': email,
            'Gender': 'Male',
            'Mobile': phone,
            'Date of Birth': f'{day:02d} {month},{year}',
            'Subjects': subject,
            'Hobbies': 'Sports',
            'Picture': f'testimage.png',
            'Address': f'{address}',
            'State and City': f'{state} {city}',
        }
        actual_data = self.get_rows()
        assert modal_data == actual_data

        return self

    def close_modal(self):
        self.button_close_modal.perform(command.js.scroll_into_view).perform(command.js.click)
        self.modalka.should(be.visible)
