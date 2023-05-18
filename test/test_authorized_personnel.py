import unittest
from logic.crs.authorized_personnel import AuthorizedPersonnel


class TestAuthorizedPersonnel(unittest.TestCase):
    def setUp(self):
        self.authorized_personnel_1 = AuthorizedPersonnel(name='John Doe',
                                                          email='johndoe@example.com',
                                                          telephone='555-1234',
                                                          id=1,
                                                          rolname='Manager',
                                                          roltype='Full-time',
                                                          rolcode=101)

        self.authorized_personnel_2 = AuthorizedPersonnel(name='Jane Smith',
                                                          email='janesmith@example.com',
                                                          telephone='555-5678',
                                                          id=2,
                                                          rolname='Assistant Manager',
                                                          roltype='Part-time',
                                                          rolcode=102)

        self.authorized_personnel_3 = AuthorizedPersonnel(name='John Doe',
                                                          email='johndoe@example.com',
                                                          telephone='555-1234',
                                                          id=1,
                                                          rolname='Manager',
                                                          roltype='Full-time',
                                                          rolcode=101)

    def test_visitor_attributes(self):
        authorized_personnel = AuthorizedPersonnel(name='John Doe',
                                                   email='johndoe@example.com',
                                                   telephone='555-1234',
                                                   id=1,
                                                   rolname='Manager',
                                                   roltype='Full-time',
                                                   rolcode=101)

        self.assertEqual(authorized_personnel.name, 'John Doe')
        self.assertEqual(authorized_personnel.email, 'johndoe@example.com')
        self.assertEqual(authorized_personnel.telephone, '555-1234')
        self.assertEqual(authorized_personnel.id, 1)
        self.assertEqual(authorized_personnel.rolname, 'Manager')
        self.assertEqual(authorized_personnel.roltype, 'Full-time')
        self.assertEqual(authorized_personnel.rolcode, 101)

    def test_str_method(self):
        authorized_personnel = AuthorizedPersonnel(name='John Doe',
                                                   email='johndoe@example.com',
                                                   telephone='555-1234',
                                                   id=1,
                                                   rolname='Manager',
                                                   roltype='Full-time',
                                                   rolcode=101)
        expected_output = ("Informacion del trabajador\n"
                           "\n* Nombre: John Doe"
                           "\n* Email: johndoe@example.com"
                           "\n* Telefono: 555-1234"
                           "\n* Id del trabajador: 1"
                           "\n* Nombre del cargo: Manager"
                           "\n* Tipo de cargo: Full-time"
                           "\n* Codigo del cargo: 101")
        self.assertEqual(str(authorized_personnel), expected_output)

    def test_equals_method(self):
        self.assertTrue(self.authorized_personnel_1.equals(self.authorized_personnel_3))
        self.assertFalse(self.authorized_personnel_1.equals(self.authorized_personnel_2))


if __name__ == '__main__':
    unittest.main()
