import unittest
from logic.crs.person import Person


class TestPerson(unittest.TestCase):
    def setUp(self):
        self.person_1 = Person(name='John Doe',
                               email='johndoe@example.com',
                               telephone='555-1234',
                               id=1)

        self.person_2 = Person(name='John Doe',
                               email='johndoe@example.com',
                               telephone='555-1234',
                               id=1)

        self.person_3 = Person(name='False name',
                               email='False email',
                               telephone='False-number',
                               id=1)

    def test_person_attributes(self):
        person = Person(name='John Doe',
                        email='johndoe@example.com',
                        telephone='555-1234',
                        id=1)

        self.assertEqual(person.name, 'John Doe')
        self.assertEqual(person.email, 'johndoe@example.com')
        self.assertEqual(person.telephone, '555-1234')
        self.assertEqual(person.id, 1)

    def test_str_method(self):
        expected_output = ("\nInformacion de la persona\n"
                           "\n* Nombre: John Doe"
                           "\n* Email: johndoe@example.com"
                           "\n* Telefono: 555-1234"
                           "\n* Id: 1")
        self.assertEqual(str(self.person_1), expected_output)

    def test_equals_method(self):
        self.assertTrue(self.person_1.equals(self.person_2))
        self.assertFalse(self.person_2.equals(self.person_3))


if __name__ == '__main__':
    unittest.main()
