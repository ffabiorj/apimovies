from json import loads
from unittest import TestCase
from app.initializer import init_app


class BaseTests(TestCase):
    def setUp(self):
        self.app = init_app()
        self.app.testing = True
        self.app_context = self.app.test_request_context()
        self.app_context.push()
        self.client = self.app.test_client()
        self.app.db.create_all()

    def tearDown(self):
        self.app.db.drop_all()