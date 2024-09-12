from playwright.sync_api import Page, expect
from constants.constants import base_url
from locators.main_page_locators import MainPageLocators

def test_go_back_from_game(page: Page):
    page.goto(base_url)
    page.locator(MainPageLocators.GAME_CARDS).nth(0).click()
    expect(page.locator("button[type=button]")).to_be_visible()
    page.locator("button[type=button]").click()
    expect(page.get_by_text(MainPageLocators.MAIN_PAGE_TITLE)).to_be_visible()
