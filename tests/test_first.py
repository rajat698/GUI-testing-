from playwright.sync_api import Page, expect
import re

website = 'http://34.171.206.146:3200'
url = website[7:]

#Test to check if the website is responsive
def test_response(page: Page):

    response = page.request.get(website)
    expect(response).to_be_ok()

#Test case to check the CONTENT of the index page title
def test_title_home(page: Page):

    page.goto(website)
    expect(page).to_have_title("CSE565 Assignment 5")

#Test case to check the CONTENT of heading of More Info page
def test_title_infoPage(page: Page):

    page.goto(website)
    page.get_by_role("button", name="More Info").click()
    assert page.inner_text('h3') == "This is a website for CSE565 assignment"

#Test case to check the EXISTENCE of the radio button on sign ip page
def test_radioButton_signUp(page: Page):

    page.goto(website)
    page.get_by_role("button", name="Sign Up").click()
    page.get_by_label("Glad that you are still grading my assignment").check()

#Test to check the EXISTENCE of Sign In button on the home page
def test_SignIn_button(page: Page):

    page.goto(website)
    page.get_by_role("button", name="Sign In").click()

#Test to check the EXISTENCE of the logo on the home page
def test_logo_exists(page: Page):

    page.goto(website)
    page.get_by_role("img").click()

#Test to check the SIZE of the logo on the home page
def test_logo_size(page: Page):
    page.goto(website)
    logo = page.get_by_role("img")
    size_details = logo.bounding_box()

    #Height and width calculated using the bounding_box method
    assert size_details['height'] == 231.5625
    assert size_details['width'] == 300

#Test to check the SIZE of the Go Back button on the Sign Up page
def test_GoBackButton_size(page: Page):
    page.goto(website)
    page.get_by_role("button", name="Sign Up").click()
    button = page.get_by_role("button", name="Go Back")
    size_details = button.bounding_box()

    #Height and width calculated using the bounding_box method
    assert size_details['height'] == 48
    assert size_details['width'] == 300

#Test to check the SIZE of the text box on the More Info page
def test_textBox_size(page):
    page.goto(website)
    page.get_by_role("button", name="More Info").click()
    text_box = page.get_by_placeholder("Say Something Random")
    size_details = text_box.bounding_box()

    #Height and width calculated using the bounding_box method
    assert size_details['height'] == 50
    assert size_details['width'] == 205.5

#Test to check the LOCATION of the radio button on the home page
def test_radioButton_location(page: Page):
    page.goto(website)
    checkBox = page.get_by_label("Hello and welcome to grading my assignment")
    location_details = checkBox.bounding_box()
    
    #Location calculated using bounding_box method
    assert location_details['x'] == 545
    assert location_details['y'] == 521.0625

#Test to check the LOCATION of the main image on the sign in page
def test_image_location(page: Page):
    page.goto(website)
    page.get_by_role("button", name="Sign In").click()
    image = page.get_by_role("img")
    location_details = image.bounding_box()

    #Location calculated using bounding_box method
    assert location_details['x'] == 490
    assert location_details['y'] == 116

#Test to check the LOCATION of the 'Last Name' text field on the sign up page
def test_textBox_location(page:Page):
    page.goto(website)
    page.get_by_role("button", name="Sign Up").click()
    text_field = page.get_by_placeholder("Last Name")
    location_details = text_field.bounding_box()

    #Location calculated using bounding_box method
    assert location_details['x'] == 641.7578125
    assert location_details['y'] == 212

# Test to check the FLOW of pages main -> Sign In
def test_flow_to_sign_in(page: Page):
    page.goto(website)
    page.get_by_role("button", name="Sign In").click()
    expect(page).to_have_url(re.compile(f"{url}/signin"))

#Test to check the FLOW of pages main -> Sign Up
def test_flow_to_sign_up(page: Page):
    page.goto(website)
    page.get_by_role("button", name="Sign Up").click()
    expect(page).to_have_url(re.compile(f"{url}/signup"))

#Test to check the FLOW of pages main -> More Info - > Go Back
def test_flow_to_more_info(page: Page):
    page.goto(website)
    page.get_by_role("button", name="More Info").click()
    page.get_by_role("button", name="Go Back").click()
    expect(page).to_have_url(re.compile(f"{url}"))