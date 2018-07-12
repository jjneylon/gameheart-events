from unittest import TestCase

from service import db


class GHTestCase(TestCase):

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
