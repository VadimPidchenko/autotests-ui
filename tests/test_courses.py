import pytest
from playwright.sync_api import expect, Page


@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list(chromium_page_with_state: Page):
    chromium_page_with_state.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

    course_title = chromium_page_with_state.get_by_test_id("courses-list-toolbar-title-text")
    expect(course_title).to_be_visible()
    expect(course_title).to_have_text("Courses")

    course_icon = chromium_page_with_state.get_by_test_id("courses-list-empty-view-icon")
    expect(course_icon).to_be_visible()

    course_title_results = chromium_page_with_state.get_by_test_id("courses-list-empty-view-title-text")
    expect(course_title_results).to_be_visible()
    expect(course_title_results).to_have_text("There is no results")

    course_description_text = chromium_page_with_state.get_by_test_id("courses-list-empty-view-description-text")
    expect(course_description_text).to_be_visible()
    expect(course_description_text).to_have_text("Results from the load test pipeline will be displayed here")
