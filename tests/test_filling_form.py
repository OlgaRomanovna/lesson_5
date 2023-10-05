import os

from selene import browser, have


def test_filling_form():
    browser.open("/automation-practice-form")
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
    browser.element("table > tbody > tr:nth-child(1) > td:nth-child(2)").should(
        have.text("Olga N")
    )
    browser.element("table > tbody > tr:nth-child(2) > td:nth-child(2)").should(
        have.text("olgaN@mail.ru")
    )
    browser.element("table > tbody > tr:nth-child(3) > td:nth-child(2)").should(
        have.text("Female")
    )
    browser.element("table > tbody > tr:nth-child(4) > td:nth-child(2)").should(
        have.text("9999999999")
    )
    browser.element("table > tbody > tr:nth-child(5) > td:nth-child(2)").should(
        have.text("09 April,1995")
    )
    browser.element("table > tbody > tr:nth-child(6) > td:nth-child(2)").should(
        have.text("Biology")
    )
    browser.element("table > tbody > tr:nth-child(7) > td:nth-child(2)").should(
        have.text("Reading")
    )
    browser.element("table > tbody > tr:nth-child(8) > td:nth-child(2)").should(
        have.text("cat.jpeg")
    )
    browser.element("table > tbody > tr:nth-child(9) > td:nth-child(2)").should(
        have.text("Krasnodar")
    )
    browser.element("table > tbody > tr:nth-child(10) > td:nth-child(2)").should(
        have.text("Haryana Karnal")
    )
