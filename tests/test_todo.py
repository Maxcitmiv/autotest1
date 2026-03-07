from pages.start_page import StartPage


def test_fill_form(data_user):
    start_page=StartPage()
    start_page.open_page()
    start_page.firstname_fill(data_user.fname)
    start_page.lastname_fill(data_user.lname)
    start_page.fill_email(data_user.email)
    start_page.fill_gender()
    start_page.fill_phone(data_user.phone)
    start_page.fill_dateofbirth(data_user.year,data_user.month,data_user.day)
    start_page.fill_subjects(data_user.subjects)
    start_page.fill_hobbies()
    (start_page.uploadpicture()
    .fill_address(data_user.address)
    .fill_city_and_state(data_user.ccity,data_user.sstate)
    .pess_submit())

def test_modalwindow(data_user):
    (StartPage().should_user_data(
        data_user.fname,
        data_user.lname,
        data_user.email,
        data_user.phone,
        data_user.day,
        data_user.month,
        data_user.year,
        data_user.subjects,
        data_user.address,
        data_user.sstate,
        data_user.ccity,
    )
    .close_modal())