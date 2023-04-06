from playwright.sync_api import Page, expect
from flask import url_for
import pytest
import re

#Test to check if the website is responsive
def test_response(page: Page):

    response = page.request.get('http://34.171.206.146:3200')
    expect(response).to_be_ok()

#Test case to check the CONTENT of the index page title
def test_title_home(page: Page):

    page.goto("http://34.171.206.146:3200")
    expect(page).to_have_title("CSE565 Assignment 5")

#Test case to check the CONTENT of heading of More Info page
def test_title_infoPage(page: Page):
    page.goto("http://34.171.206.146:3200")
    page.get_by_role("button", name="More Info").click()
    assert page.inner_text('h3') == "This is a website for CSE565 assignment"

#Test case to check the exstence of the radio button on sign ip page
def test_radioButton_signUp(page: Page):
    page.goto("http://34.171.206.146:3200")
    page.get_by_role("button", name="Sign Up").click()
    page.get_by_label("Glad that you are still grading my assignment").check()

#Test to check the EXISTENCE of Sign In button on the home page
def test_SignIn_button(page: Page):
    page.goto("http://34.171.206.146:3200")
    page.get_by_role("button", name="Sign In").click()

def test_logo_exists(page: Page):
    page.goto("http://34.171.206.146:3200")
    page.get_by_role("img").click()


    