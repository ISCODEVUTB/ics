import unittest
from logic.crs.package import Package
from logic.crs.person import Person
from logic.crs.authorized_personnel import AuthorizedPersonnel
from logic.crs.event import Event
from logic.crs.visitor import Visitor
from logic.crs.place import Place


class TestPackage(unittest.TestCase):
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
                              type_place='Test type',
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

        self.package_1 = Package(subject=self.visitor_1,
                                 name='Toy',
                                 description='Juguete rojo',
                                 code=1)

        self.package_2 = Package(subject=self.visitor_1,
                                 name='Toy',
                                 description='Juguete rojo',
                                 code=1)

        self.package_3 = Package(subject=self.visitor_1,
                                 name='False name',
                                 description='False description',
                                 code=1)

    def test_package_attributes(self):
        package = Package(subject=self.visitor_1,
                          name='Toy',
                          description='Juguete rojo',
                          code=1)

        self.assertEqual(package.subject, self.visitor_1)
        self.assertEqual(package.name, 'Toy')
        self.assertEqual(package.description, 'Juguete rojo')
        self.assertEqual(package.code, 1)

    def test_str_method(self):
        package = Package(subject=self.visitor_1,
                          name='Toy',
                          description='Juguete rojo',
                          code=1)

        expected_string = ("\nInformacion del objeto\n"
                           "\nInformacion del visitante\n"
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
                           "\n* Tipo de lugar: Test type"
                           "\n* Id del evento: 120"
                           "\n* Hora de entrada: 19"
                           "\n* Hora de salida: 20"
                           "\n* Fecha: 2023-06-01\n"
                           "\nInformacion personal del visitante\n"
                           "\n* Nombre: Bob Smith"
                           "\n* Email: bobsmith@example.com"
                           "\n* Telefono: 555-555-5555"
                           "\n* Id: 4321"
                           "\n* Nombre: Toy"
                           "\n* Descripcion: Juguete rojo"
                           "\n* Codigo: 1")
        self.assertEqual(str(package), expected_string)

    def test_equals_method(self):
        self.assertTrue(self.package_1.equals(self.package_2))
        self.assertFalse(self.package_2.equals(self.package_3))


if __name__ == '__main__':
    unittest.main()
