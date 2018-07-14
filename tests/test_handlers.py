import json

from tests import GHTestCase, db
from service.handlers import (
    handle_get,
    handle_patch,
    handle_put,
)
from service.models import Site


class HandleGetTestCase(GHTestCase):
    def test_handle_get(self):
        site = Site(chapter_id='1234', title='Test Site 1')
        db.session.add(site)
        db.session.commit()

        status_code, message = handle_get(Site, site.id, db)

        self.assertEqual(200, status_code)
        self.assertDictEqual(
            json.loads(message),
            {'id': 1, 'latitude': None, 'chapter_id': 1234, 'longitude': None, 'title': 'Test Site 1'}
        )


class HandlePatchTestCase(GHTestCase):
    def test_handle_patch(self):
        site = Site(chapter_id='1234', title='Test Site 1')
        db.session.add(site)
        db.session.commit()
        site_payload = {'title': 'Test Site 2'}

        status_code, message = handle_patch(Site, site.id, site_payload, db)

        self.assertEqual(200, status_code)
        self.assertDictEqual(
            json.loads(message),
            {'id': 1, 'title': 'Test Site 2'}
        )


class HandlePutTestCase(GHTestCase):
    def test_handle_put(self):
        site_payload = {'chapter_id': '1234', 'title': 'Test Site 1'}

        status_code, message = handle_put(Site, site_payload, db)

        self.assertEqual(201, status_code)
        self.assertDictEqual(
            json.loads(message),
            {'model_id': 1},
        )
