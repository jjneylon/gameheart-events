from unittest import mock, TestCase

from service import db


class GHTestCase(TestCase):

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()


class RequestContext:
    def __init__(self, path='/', method='GET', content_type='application/json', json=None, data=None):
        self.path = path
        self.method = method
        self.content_type = content_type
        self.json = json
        self.data = data

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            context_kwargs = {'path': self.path, 'method': self.method, 'content_type': self.content_type}
            if self.json is not None:
                context_kwargs.update(json=self.json)
            if self.data is not None:
                context_kwargs.update(data=self.data)
            with db.app.test_request_context(**context_kwargs):
                func(*args, **kwargs)
        return wrapper


def request_context(url='', json=None):
    def decorator(func):
        def wrapper(*args, **kwargs):
            with db.app.test_request_context(url, json=json):
                func(*args, **kwargs)
        return wrapper
    return decorator
