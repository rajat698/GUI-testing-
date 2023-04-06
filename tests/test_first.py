from playwright.sync_api import Page, expect
from flask import url_for
import pytest


def test_example(page: Page):

    page.goto("http://34.171.206.146:3200")
    assert page.title() == "CSE565 Assignment 5"
    
    page.get_by_role("button", name="Sign In").click()
    page.get_by_role("button", name="Go back").click()
    page.get_by_role("button", name="Sign Up").click()
    page.get_by_role("button", name="Go Back").click()
    page.get_by_role("button", name="More Info").click()
    page.get_by_role("button", name="Go Back").click()