import json

from tests import GHTestCase, db
from service.handlers import (
    handle_get,
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
