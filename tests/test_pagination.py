import re
from playwright.sync_api import Page, expect
from constants.constants import base_url
from locators.pagination_locators import PaginationLocators

def test_prev_page_to_be_disabled(page: Page):
    page.goto(base_url)
    expect(page.locator(PaginationLocators.PAGINATION_ARROW_BUTTON).first).to_be_disabled()
    expect(page.locator(PaginationLocators.PAGINATION_ARROW_BUTTON).nth(2)).to_be_disabled()

def test_go_to_second_page(page: Page):
    page.goto(base_url)
    expect(page.get_by_title('1').first).to_have_class(re.compile(PaginationLocators.ACTIVE_PAGE_CLASS))
    page.get_by_title('2').first.click()
    expect(page.get_by_title('2').first).to_have_class(re.compile(PaginationLocators.ACTIVE_PAGE_CLASS))

def test_next_five_pages(page: Page):
    page.goto(base_url)
    expect(page.get_by_title('1').first).to_have_class(re.compile(PaginationLocators.ACTIVE_PAGE_CLASS))
    page.get_by_title(PaginationLocators.NEXT_FIVE_PAGES).first.click()
    expect(page.get_by_title('6').first).to_have_class(re.compile(PaginationLocators.ACTIVE_PAGE_CLASS))
    expect(page.get_by_title('6').nth(1)).to_have_class(re.compile(PaginationLocators.ACTIVE_PAGE_CLASS))

def test_back_five_pages(page: Page):
    page.goto(base_url)
    page.get_by_title(PaginationLocators.NEXT_FIVE_PAGES).nth(1).click()
    page.get_by_title(PaginationLocators.PREV_FIVE_PAGES).nth(1).click()
    expect(page.get_by_role('listitem').nth(1)).to_have_class(re.compile(PaginationLocators.ACTIVE_PAGE_CLASS))

def test_next_page_to_be_disabled(page: Page):
    page.goto(base_url)
    page.get_by_role("listitem").nth(7).click()
    expect(page.get_by_role("listitem").nth(7)).to_have_class(re.compile(PaginationLocators.ACTIVE_PAGE_CLASS))
    expect(page.get_by_role("listitem").nth(18)).to_have_class(re.compile(PaginationLocators.ACTIVE_PAGE_CLASS))
    expect(page.locator(PaginationLocators.PAGINATION_ARROW_BUTTON).nth(1)).to_be_disabled()
    expect(page.locator(PaginationLocators.PAGINATION_ARROW_BUTTON).nth(3)).to_be_disabled()
