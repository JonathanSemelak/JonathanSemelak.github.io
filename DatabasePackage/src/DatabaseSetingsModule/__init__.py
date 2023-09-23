""""
DatabaseSetingsModule
----------------------
This is a Module which has Class for Database

"""

class Database(object):
    def __init__(self, connection_string):
        """
        This is connection string or connect sql server
        :param coection_String: str
        """
        self.connection_string = connection_string

    def connect(self) -> True:
        """
        This method to connect to database
        :return: Bool
        """
        print("connected to database")
        return True
