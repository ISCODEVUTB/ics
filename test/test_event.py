import unittest
from logic.crs.place import Place
from logic.crs.event import Event


class TestEvent(unittest.TestCase):
    def setUp(self):
        self.place = Place(name='Computer room',
                           ubication='A1',
                           type_place='Building')

        self.event_1 = Event(location=self.place,
                             id=1,
                             timeIn=15,
                             timeOut=16,
                             date='2023-06-01')

        self.event_2 = Event(location=self.place,
                             id=1,
                             timeIn=15,
                             timeOut=16,
                             date='2023-06-01')

        self.event_3 = Event(location=self.place,
                             id=1,
                             timeIn=15,
                             timeOut=16,
                             date='False date')

    def test_person_attributes(self):
        event = Event(location=self.place,
                      id=1,
                      timeIn=15,
                      timeOut=16,
                      date='2023-06-01')

        self.assertEqual(event.location, self.place)
        self.assertEqual(event.id, 1)
        self.assertEqual(event.timeIn, 15)
        self.assertEqual(event.timeOut, 16)
        self.assertEqual(event.date, '2023-06-01')

    def test_str_method(self):
        expected_output = ("\nInformacion del evento\n"
                           "\n* Nombre del lugar: Computer room"
                           "\n* Ubicacion del lugar: A1"
                           "\n* Tipo de lugar: Building"
                           "\n* Id del evento: 1"
                           "\n* Hora de entrada: 15"
                           "\n* Hora de salida: 16"
                           "\n* Fecha: 2023-06-01")

        self.assertEqual(str(self.event_1), expected_output)

    def test_equals_method(self):
        self.assertTrue(self.event_1.equals(self.event_2))
        self.assertFalse(self.event_2.equals(self.event_3))

if __name__ == '__main__':
    unittest.main()
