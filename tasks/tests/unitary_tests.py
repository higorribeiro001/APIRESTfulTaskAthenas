from django.test import TestCase, Client

class UnitaryTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = '/person/api/v1/'

    def create_person(self):
        response = self.client.post(
            self.url,
            {
                "name": "UserTest",
                "date_birth": "2000-09-09",
                "cpf": "12345678900",
                "sex": "M",
                "height": 1.60,
                "weight": 50
            }
        )
        return response 

    def test_list_persons(self):
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 200)

    def test_return_person(self):
        person_data = self.create_person()
        response = self.client.get(f"{self.url}{person_data.json()['id']}/")

        self.assertEqual(response.status_code, 200)
        self.client.delete(f"{self.url}{person_data.json()['id']}/")

    def test_create_person(self):
        person_data = self.create_person()

        self.assertEqual(person_data.status_code, 201)  
        self.client.delete(f"{self.url}{person_data.json()['id']}/")

    def test_update_person(self):
        person_data = self.create_person()
        response = self.client.put(
            f"{self.url}{person_data.json()['id']}/",
            {
                'name': 'UserTest Updated',
                'date_birth': '2000-09-09',
                'cpf': '12345678900',
                'sex': 'M',
                'height': 1.68,
                'weight': 56,
            },
            content_type='application/json'
        )

        self.assertEqual(response.status_code, 200)
        self.client.delete(f"{self.url}{person_data.json()['id']}/")

    def test_delete_person(self):
        person_data = self.create_person()
        response = self.client.delete(f"{self.url}{person_data.json()['id']}/")
        self.assertEqual(response.status_code, 204)
