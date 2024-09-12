import pytest
from playwright.sync_api import Page, expect
from constants.constants import base_url
from locators.filter_locators import FilterCategoryLocators

def test_filter_changed(page: Page):
    page.goto(base_url)
    expect(page.get_by_title(FilterCategoryLocators.NOT_CHOSEN_CATEGORY).nth(1)).to_contain_text(FilterCategoryLocators.NOT_CHOSEN_CATEGORY) 
    page.get_by_title(FilterCategoryLocators.NOT_CHOSEN_CATEGORY).nth(1).click()
    page.get_by_title(FilterCategoryLocators.MMORPG_CATEGORY).click()
    expect(page.get_by_title(FilterCategoryLocators.MMORPG_CATEGORY).first).to_contain_text(FilterCategoryLocators.MMORPG_CATEGORY)

@pytest.mark.skip(reason='При выборе категории mmorpg присутствуют игры других жанров')
def test_choose_mmorpg(page: Page):
    page.goto(base_url)
    page.get_by_title(FilterCategoryLocators.NOT_CHOSEN_CATEGORY).nth(1).click()
    expect(page.get_by_title(FilterCategoryLocators.MMORPG_CATEGORY)).to_be_visible()
    page.get_by_title(FilterCategoryLocators.MMORPG_CATEGORY).click()
    expect(page.locator(FilterCategoryLocators.MMORPG_GENRE)).to_have_count(FilterCategoryLocators.DEFAULT_PAGE_COUNT)

def test_choose_shooter(page: Page):
    page.goto(base_url)
    page.get_by_title(FilterCategoryLocators.NOT_CHOSEN_CATEGORY).nth(1).click()
    expect(page.get_by_title(FilterCategoryLocators.SHOOTER_CATEGORY)).to_be_visible()
    page.get_by_title(FilterCategoryLocators.SHOOTER_CATEGORY).click()
    expect(page.locator(FilterCategoryLocators.SHOOTER_GENRE)).to_have_count(FilterCategoryLocators.DEFAULT_PAGE_COUNT)

@pytest.mark.skip(reason='При выборе категории strategy присутствуют игры других жанров')
def test_choose_strategy(page: Page):
    page.goto(base_url)
    page.get_by_title(FilterCategoryLocators.NOT_CHOSEN_CATEGORY).nth(1).click()
    expect(page.get_by_title(FilterCategoryLocators.STRATEGY_CATEGORY)).to_be_visible()
    page.get_by_title(FilterCategoryLocators.STRATEGY_CATEGORY).click()
    expect(page.locator(FilterCategoryLocators.STRATEGY_GENRE)).to_have_count(FilterCategoryLocators.DEFAULT_PAGE_COUNT)

@pytest.mark.skip(reason='При выборе категории moba присутствуют игры других жанров')
def test_choose_moba(page: Page):
    page.goto(base_url)
    page.get_by_title(FilterCategoryLocators.NOT_CHOSEN_CATEGORY).nth(1).click()
    expect(page.get_by_title(FilterCategoryLocators.MOBA_CATEGORY)).to_be_visible()
    page.get_by_title(FilterCategoryLocators.MOBA_CATEGORY).click()
    expect(page.locator(FilterCategoryLocators.MOBA_GENRE)).to_have_count(FilterCategoryLocators.DEFAULT_PAGE_COUNT)

@pytest.mark.skip(reason='При выборе категории racin присутствуют игры других жанров')
def test_choose_racing(page: Page):
    page.goto(base_url)
    page.get_by_title(FilterCategoryLocators.NOT_CHOSEN_CATEGORY).nth(1).click()
    expect(page.get_by_title(FilterCategoryLocators.RACING_CATEGORY)).to_be_visible()
    page.get_by_title(FilterCategoryLocators.RACING_CATEGORY).click()
    expect(page.locator(FilterCategoryLocators.RACING_GENRE)).to_have_count(FilterCategoryLocators.DEFAULT_PAGE_COUNT)

@pytest.mark.skip(reason='При выборе категории sports присутствуют игры других жанров')
def test_choose_sports(page: Page):
    page.goto(base_url)
    page.get_by_title(FilterCategoryLocators.NOT_CHOSEN_CATEGORY).nth(1).click()
    expect(page.get_by_title(FilterCategoryLocators.SPORTS_CATEGORY)).to_be_visible()
    page.get_by_title(FilterCategoryLocators.SPORTS_CATEGORY).click()
    expect(page.locator(FilterCategoryLocators.SPORTS_GENRE)).to_have_count(FilterCategoryLocators.DEFAULT_PAGE_COUNT)

@pytest.mark.skip(reason='При выборе категории social присутствуют игры других жанров')
def test_choose_social(page: Page):
    page.goto(base_url)
    page.get_by_title(FilterCategoryLocators.NOT_CHOSEN_CATEGORY).nth(1).click()
    expect(page.get_by_title(FilterCategoryLocators.SOCIAL_CATEGORY)).to_be_visible()
    page.get_by_title(FilterCategoryLocators.SOCIAL_CATEGORY).click()
    expect(page.locator(FilterCategoryLocators.SOCIAL_GENRE)).to_have_count(FilterCategoryLocators.DEFAULT_PAGE_COUNT)
