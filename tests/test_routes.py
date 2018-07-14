from service import routes
from service.models import Site
from tests import db, mock, RequestContext, TestCase


class GetModelRouteTestCase(TestCase):
    @RequestContext()
    def test_get_model_route(self):
        with mock.patch.object(routes, 'handle_get', return_value=(200, '{"id": 1}')) as mock_handle:
            response = routes.get_model('site', 1)

        self.assertEqual(response, '{"id": 1}')
        mock_handle.assert_called_once_with(Site, 1, db)

    @RequestContext(method='PATCH', json={'test': 1})
    def test_patch_model_route(self):
        with mock.patch.object(routes, 'handle_patch', return_value=(200, '{"test": 1}')) as mock_handle:
            response = routes.patch_model('site', 1)

        self.assertEqual(response, '{"test": 1}')
        mock_handle.assert_called_once_with(Site, 1, {'test': 1}, db)

    @RequestContext(method='POST', content_type='application/x-www-form-urlencoded', data={'test': '1'})
    def test_post_new_model_route(self):
        with mock.patch.object(routes, 'handle_put', return_value=(201, '{"test": "1"}')) as mock_handle:
            response = routes.post_new_model('site')

        self.assertEqual(response, '{"test": "1"}')
        mock_handle.assert_called_once_with(Site, {'test': '1'}, db)

    @RequestContext(method='POST', content_type='application/x-www-form-urlencoded', data={'test': '1'})
    def test_post_update_model_route(self):
        with mock.patch.object(routes, 'handle_patch', return_value=(200, '{"test": "1"}')) as mock_handle:
            response = routes.post_update_model('site', 1)

        self.assertEqual(response, '{"test": "1"}')
        mock_handle.assert_called_once_with(Site, 1, {'test': '1'}, db)

    @RequestContext(method='PUT', json={'test': 1})
    def test_put_model_route(self):
        with mock.patch.object(routes, 'handle_put', return_value=(201, '{"test": 1}')) as mock_handle:
            response = routes.put_model('site')

        self.assertEqual(response, '{"test": 1}')
        mock_handle.assert_called_once_with(Site, {'test': 1}, db)
