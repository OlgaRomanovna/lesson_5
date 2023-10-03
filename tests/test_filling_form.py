import os

from selene import browser, have


def test_filling_form():
    browser.open("https://demoqa.com/automation-practice-form")
    browser.element("#firstName").type("Olga")
    browser.element("#lastName").type("N")
    browser.element("#userEmail").type("olgaN@mail.ru")
    browser.element(
        'div.col-md-9.col-sm-12 > div:nth-child(2) > [for="gender-radio-2"]'
    ).click()
    browser.element("#userNumber").type("9999999999")
    browser.element("#dateOfBirthInput").click()
    browser.element(".react-datepicker__month-select").click().all("option").element_by(
        have.exact_text("April")
    ).click()
    browser.element(".react-datepicker__year-select").click().all("option").element_by(
        have.exact_text("1995")
    ).click()
    browser.element('[aria-label="Choose Sunday, April 9th, 1995"]').click()
    browser.element("#subjectsInput").type("B").press_enter()
    browser.element(
        'div.col-md-9.col-sm-12 > div:nth-child(2) > [for="hobbies-checkbox-2"]'
    ).click()
    browser.element("#uploadPicture").send_keys(os.path.abspath("img/cat.jpeg"))
    browser.element("#currentAddress").type("Krasnodar")
    browser.execute_script("window.scrollTo(0, 500)")
    browser.element("#state").click().all('[id^="react-select-3-option"]').element_by(
        have.exact_text("Haryana")
    ).click()
    browser.element("#city").click().all('[id^="react-select-4-option"]').element_by(
        have.exact_text("Karnal")
    ).click()
    browser.element("#userNumber").press_enter()
    browser.element("#example-modal-sizes-title-lg").should(
        have.exact_text("Thanks for submitting the form")
    )

    browser.element(".modal-title").should(
        have.exact_text("Thanks for submitting the form")
    )
    browser.element(
        '//div[@class="modal-body"]//td[text()="Student Name"]/following-sibling::td'
    ).should(have.text("Olga N"))
    browser.element(
        '//div[@class="modal-body"]//td[text()="Student Email"]/following-sibling::td'
    ).should(have.text("olgaN@mail.ru"))
    browser.element(
        '//div[@class="modal-body"]//td[text()="Gender"]/following-sibling::td'
    ).should(have.text("Female"))
    browser.element(
        '//div[@class="modal-body"]//td[text()="Mobile"]/following-sibling::td'
    ).should(have.text("9999999999"))
    browser.element(
        '//div[@class="modal-body"]//td[text()="Date of Birth"]/following-sibling::td'
    ).should(have.text("09 April,1995"))
    browser.element(
        '//div[@class="modal-body"]//td[text()="Subjects"]/following-sibling::td'
    ).should(have.text("Biology"))
    browser.element(
        '//div[@class="modal-body"]//td[text()="Hobbies"]/following-sibling::td'
    ).should(have.text("Reading"))
    browser.element(
        '//div[@class="modal-body"]//td[text()="Picture"]/following-sibling::td'
    ).should(have.text("cat.jpeg"))
    browser.element(
        '//div[@class="modal-body"]//td[text()="Address"]/following-sibling::td'
    ).should(have.text("Krasnodar"))
    browser.element(
        '//div[@class="modal-body"]//td[text()="State and City"]/following-sibling::td'
    ).should(have.text("Haryana Karnal"))
