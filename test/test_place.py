import unittest
from logic.crs.place import Place


class TestPlace(unittest.TestCase):
    def setUp(self):
        self.place_1 = Place(name='Computer room',
                             ubication='A1',
                             type_place='Building')

        self.place_2 = Place(name='Computer room',
                             ubication='A1',
                             type_place='Building')

        self.place_3 = Place(name='False name',
                             ubication='False ubication',
                             type_place='False type place')

    def test_person_attributes(self):
        place = Place(name='Computer room',
                      ubication='A1',
                      type_place='Building')

        self.assertEqual(place.name, 'Computer room')
        self.assertEqual(place.ubication, 'A1')
        self.assertEqual(place.type_place, 'Building')

    def test_str_method(self):
        expected_output = ("\nInformacion del lugar\n"
                           "\n* Nombre: Computer room"
                           "\n* Ubicacion del lugar: A1"
                           "\n* Tipo de lugar: Building")
        self.assertEqual(str(self.place_1), expected_output)

    def test_equals_method(self):
        self.assertTrue(self.place_1.equals(self.place_2))
        self.assertFalse(self.place_2.equals(self.place_3))


if __name__ == '__main__':
    unittest.main()
