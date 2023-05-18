import unittest
from logic.crs.person import Person
from logic.crs.place import Place
from logic.crs.register import Register


class TestPlace(unittest.TestCase):
    def setUp(self):
        self.person = Person(name='John Doe',
                             email='johndoe@example.com',
                             telephone='555-1234',
                             id=1)

        self.place = Place(name='Computer room',
                           ubication='A1',
                           type_place='Building')
        self.place_2 = Place(name='Computer room',
                             ubication='A1',
                             type_place='Building')

        self.register_1 = Register(subject=self.person,
                                   zone=self.place)

        self.register_2 = Register(subject=self.person,
                                   zone=self.place)

        self.register_3 = Register(subject=self.person,
                                   zone=self.place_2)

    def test_person_attributes(self):
        register = Register(subject=self.person,
                            zone=self.place)

        self.assertEqual(register.subject, self.person)
        self.assertEqual(register.zone, self.place)

    def test_str_method(self):
        expected_output = ("\nInformacion de la persona\n"
                           "\n* Nombre: John Doe"
                           "\n* Email: johndoe@example.com"
                           "\n* Telefono: 555-1234"
                           "\n* Id: 1\n"
                           "\nInformacion del lugar\n"
                           "\n* Nombre: Computer room"
                           "\n* Ubicacion del lugar: A1"
                           "\n* Tipo de lugar: Building")
        self.assertEqual(str(self.register_1), expected_output)

    def test_equals_method(self):
        self.assertTrue(self.register_1.equals(self.register_2))
        self.assertFalse(self.register_2.equals(self.register_3))


if __name__ == '__main__':
    unittest.main()
