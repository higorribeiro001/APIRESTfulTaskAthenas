from django.test import TestCase, Client

class UnitaryTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = '/ideal-weight/api/v1/'
        self.urlPerson = '/person/api/v1/'

    def create_person(self):
        response = self.client.post(
            self.urlPerson,
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

    def test_return_ideal_weight(self):
        person_data = self.create_person()
        response = self.client.get(f"{self.url}{person_data.json()['id']}/")

        self.assertEqual(response.status_code, 200)
        self.client.delete(f"{self.urlPerson}{person_data.json()['id']}/")
