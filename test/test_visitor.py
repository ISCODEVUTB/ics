import unittest
from logic.crs.person import Person
from logic.crs.authorized_personnel import AuthorizedPersonnel
from logic.crs.event import Event
from logic.crs.visitor import Visitor
from logic.crs.place import Place


class TestVisitor(unittest.TestCase):
    def setUp(self):
        self.person = Person(name='John Doe',
                             email='johndoe@example.com',
                             telephone='123-456-7890',
                             id=1234)

        self.authorized_personnel = AuthorizedPersonnel(name='Jane Doe',
                                                        email='janedoe@example.com',
                                                        telephone='123-456-7890',
                                                        id=5678)

        self.location = Place(name='Test Event',
                              type_place='Edifice',
                              ubication='Test Location')

        self.event = Event(location=self.location,
                           id=120,
                           timeIn=19,
                           timeOut=20,
                           date='2023-06-01')

        self.visitor_1 = Visitor(responsible=self.authorized_personnel,
                                 event=self.event,
                                 name='Bob Smith',
                                 email='bobsmith@example.com',
                                 telephone='555-555-5555',
                                 id=4321)

        self.visitor_2 = Visitor(responsible=self.authorized_personnel,
                                 event=self.event,
                                 name='Bob Smith',
                                 email='bobsmith@example.com',
                                 telephone='555-555-5555',
                                 id=4321)

        self.visitor_3 = Visitor(responsible=self.authorized_personnel,
                                 event=self.event,
                                 name='False name',
                                 email='FalseEmail@example.com',
                                 telephone='FAL-SEN-UMBER',
                                 id=4321)

    def test_visitor_attributes(self):
        visitor = Visitor(responsible=self.authorized_personnel,
                          event=self.event,
                          name='Bob Smith',
                          email='bobsmith@example.com',
                          telephone='555-555-5555',
                          id=4321)

        self.assertEqual(visitor.name, 'Bob Smith')
        self.assertEqual(visitor.email, 'bobsmith@example.com')
        self.assertEqual(visitor.telephone, '555-555-5555')
        self.assertEqual(visitor.id, 4321)
        self.assertEqual(visitor.responsible, self.authorized_personnel)
        self.assertEqual(visitor.event, self.event)

    def test_str_method(self):
        visitor = Visitor(responsible=self.authorized_personnel,
                          event=self.event,
                          name='Bob Smith',
                          email='bobsmith@example.com',
                          telephone='555-555-5555',
                          id=4321)

        expected_string = ("Informacion del visitante\n"
                           "\nInformacion del trabajador\n"
                           "\n* Nombre: Jane Doe"
                           "\n* Email: janedoe@example.com"
                           "\n* Telefono: 123-456-7890"
                           "\n* Id del trabajador: 5678"
                           "\n* Nombre del cargo: rolname"
                           "\n* Tipo de cargo: roltype"
                           "\n* Codigo del cargo: 0\n"
                           "\nInformacion del evento\n"
                           "\n* Nombre del lugar: Test Event"
                           "\n* Ubicacion del lugar: Test Location"
                           "\n* Tipo de lugar: Edifice"
                           "\n* Id del evento: 120"
                           "\n* Hora de entrada: 19"
                           "\n* Hora de salida: 20"
                           "\n* Fecha: 2023-06-01\n"
                           "\nInformacion personal del visitante\n"
                           "\n* Nombre: Bob Smith"
                           "\n* Email: bobsmith@example.com"
                           "\n* Telefono: 555-555-5555"
                           "\n* Id: 4321")
        self.assertEqual(str(visitor), expected_string)

    def test_equals_method(self):
        self.assertTrue(self.visitor_1.equals(self.visitor_2))
        self.assertFalse(self.visitor_2.equals(self.visitor_3))


if __name__ == '__main__':
    unittest.main()
