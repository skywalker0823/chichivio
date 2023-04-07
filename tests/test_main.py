import unittest
from app import create_app


class FlaskTest(unittest.TestCase):

    def setUp(self):
        self.app = create_app().test_client()

    def tearDown(self):
        pass

    def test_index_page(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_about_page(self):
        response = self.app.get('/about')
        self.assertEqual(response.status_code, 200)

    # def test_contact_page(self):
    #     response = self.app.get('/contact')
    #     self.assertEqual(response.status_code, 200)

    def test_member_page_without_login(self):
        response = self.app.get('/member')
        self.assertEqual(response.status_code, 401)

    def test_board_page_without_login(self):
        response = self.app.get('/board')
        self.assertEqual(response.status_code, 401)


if __name__ == '__main__':
    unittest.main()

# command: python3 -m unittest tests/test_main.py