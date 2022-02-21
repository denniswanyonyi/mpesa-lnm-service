from django.test import TestCase, Client

from .views import index, details, c2b_validation, c2b_confirmation


class ViewsTestCase(TestCase):

    # Create your tests here.
    def test_home_page_status_code_success(self):

        client = Client()

        request = client.get('/')

        assert request.status_code == 200



    def test_details_not_found_status_code(self):

        client = Client()

        request = client.get('/c2b/details/NONEXISTENT')

        print(request.status_code)

        assert request.status_code == 200