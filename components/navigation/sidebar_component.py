import re

from playwright.sync_api import Page

from components.base_component import BaseComponent
from components.navigation.sidebar_list_item_component import SidebarListItemComponent


class SidebarComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.dashboard = SidebarListItemComponent(page, "dashboard")
        self.courses = SidebarListItemComponent(page, "courses")
        self.logout = SidebarListItemComponent(page, "logout")

    def check_visible(self):
        self.dashboard.check_visible("Dashboard")
        self.courses.check_visible("Courses")
        self.logout.check_visible("Logout")

    def click_courses(self):
        self.dashboard.navigate(re.compile(r".*/#/dashboard"))

    def click_dashboard(self):
        self.dashboard.navigate(re.compile(r".*/#/courses"))

    def click_logout(self):
        self.dashboard.navigate(re.compile(r".*/#/auth/login"))
