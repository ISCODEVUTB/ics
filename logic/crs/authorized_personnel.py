from logic.crs.person import Person


class AuthorizedPersonnel(Person):
    """
    Represents an authorized personnel in the system.

    Attributes:
        name (str): The name of the authorized personnel.
        email (str): The email of the authorized personnel.
        telephone (str): The telephone number of the authorized personnel.
        id (int): The ID of the authorized personnel.
        rolname (str): The name of the role of the authorized personnel.
        roltype (str): The type of the role of the authorized personnel.
        rolcode (int): The code of the role of the authorized personnel.
    """

    def __init__(self, name: str = 'name', email: str = 'email', telephone: str = 'telephone', id: int = 0,
                 rolname: str = 'rolname', roltype: str = 'roltype', rolcode: int = 0):
        """
        Initializes a new instance of the AuthorizedPersonnel class.

        Args:
            name (str): The name of the authorized personnel.
            email (str): The email of the authorized personnel.
            telephone (str): The telephone number of the authorized personnel.
            id (int): The ID of the authorized personnel.
            rolname (str): The name of the role of the authorized personnel.
            roltype (str): The type of the role of the authorized personnel.
            rolcode (int): The code of the role of the authorized personnel.
        """
        super().__init__(name, email, telephone, id)
        self.rolname = rolname
        self.roltype = roltype
        self.rolcode = rolcode

    @property
    def rolname(self) -> str:
        """
        str: The name of the role of the authorized personnel.
        """
        return self._rolname

    @rolname.setter
    def rolname(self, value) -> None:
        """
        Sets the name of the role of the authorized personnel.

        Args:
            value (str): The name of the role of the authorized personnel.
        """
        self._rolname = value

    @property
    def roltype(self) -> str:
        """
        str: The type of the role of the authorized personnel.
        """
        return self._roltype

    @roltype.setter
    def roltype(self, value) -> None:
        """
        Sets the type of the role of the authorized personnel.

        Args:
            value (str): The type of the role of the authorized personnel.
        """
        self._roltype = value

    @property
    def rolcode(self) -> int:
        """
        int: The code of the role of the authorized personnel.
        """
        return self._rolcode

    @rolcode.setter
    def rolcode(self, value) -> None:
        """
        Sets the code of the role of the authorized personnel.

        Args:
            value (int): The code of the role of the authorized personnel.
        """
        self._rolcode = value

    def __str__(self) -> str:
        """
        str: Returns a string representation of the authorized personnel.
        """
        return (f"Informacion del trabajador\n"
                f"\n* Nombre: {self.name}"
                f"\n* Email: {self.email}"
                f"\n* Telefono: {self.telephone}"
                f"\n* Id del trabajador: {self.id}"
                f"\n* Nombre del cargo: {self.rolname}"
                f"\n* Tipo de cargo: {self.roltype}"
                f"\n* Codigo del cargo: {self.rolcode}")

    def equals(self, other) -> bool:
        """
    Checks if this instance of AuthorizedPersonnel is equal to another instance by comparing their attributes.

    Args:
        other: The other instance of AuthorizedPersonnel to compare to.

    Returns:
        A boolean indicating if the two instances are equal or not.
    """
        if isinstance(other, AuthorizedPersonnel):
            return (super().equals(other) and
                    self.rolname == other.rolname and
                    self.roltype == other.roltype and
                    self.rolcode == other.rolcode)
        return False


    def create_credentials(self) -> dict:
        """
        Creates credentials for the visitor.
        
        Returns:
            dict: A dictionary containing the credentials.
        """
        credentials = {
            
            'ID de rol': self.rolcode,
            'Nombre del rol': self.rolname,
            'Tipo de rol': self.roltype
        }
        return credentials
    
    def modify_credentials(self, field: str, new_value) -> None:
        """
        Modifies a field in the visitor's credentials.

        Args:
            field (str): The field to be modified.
            new_value: The new value for the field.
        """
        if field == 'ID de rol':
            self.rolcode = new_value
        elif field == 'Nombre del rol':
            self.rolname = new_value
        elif field == 'Tipo de rol':
            self.roltype = new_value
        else:
            raise ValueError("Invalid field")