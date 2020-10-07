from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.contrib.auth.models import User
from django.conf import settings
from playwright import sync_playwright

class ExampleTests(StaticLiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.playwright = sync_playwright().start()
        cls.browser = cls.playwright.chromium.launch(headless=False)

    @classmethod
    def tearDownClass(cls):
        cls.browser.close()
        cls.playwright.stop()

    def test_login(self):
        page = self.browser.newPage()
        page.goto(self.live_server_url)
        page.click('text=Add a new Task')
        page.fill('input[name="title"]', 'title')
        page.fill('textarea[name="description"]', 'description')
        page.click('button[type="submit"]')
        result = page.evaluate('document.querySelectorAll("div.card").length')
        assert result == 1
