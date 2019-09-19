from abc import ABCMeta, abstractmethod
import datetime

class AbstractTalent:
    """ AbstractTalent - Maintains the details of a AbstractTalent """
    INITIAL_ID = 0
    def __init__(self, first_name, last_name, talent_num, date_debut):
        '''Constructors of AbstractTalent'''
        self._id = AbstractTalent.INITIAL_ID
        AbstractTalent._validate_string_input("First Name", first_name)
        self._first_name = first_name
        AbstractTalent._validate_string_input("Last Name", last_name)
        self._last_name = last_name
        AbstractTalent._validate_string_input("Talent Number", talent_num)
        self._talent_num = talent_num
        AbstractTalent._validate_string_input("Date Debut", date_debut)
        self._date_debut = datetime.datetime.strptime(date_debut, "%Y-%m-%d %H:%M:%S")

    def get_id(self) -> int:
        '''Return ID of talent'''
        return self._id

    def set_id(self,new_id: int):
        '''Set id of talent'''

        self._validate_integer_input("New ID", new_id)
        self._id = new_id

    def get_first_name(self) -> str:
        '''Return first name of talent'''
        return self._first_name

    def get_last_name(self) -> str:
        '''Return last name of talent'''
        return self._last_name

    def get_full_name(self) -> str:
        '''Return full name of talent'''
        return self._first_name + ", " + self._last_name

    def get_talent_num(self) -> str:
        '''Return talent number of talent'''
        return self._talent_num

    def get_year_debut(self):
        '''Return year debuted of talent'''
        year_debut = self._date_debut
        return year_debut.year

    def get_date_debut(self):
        '''Return date debuted of talent'''
        return self._date_debut

    def get_years_debut(self):
        '''Return year debuted of talent'''
        year_now = datetime.datetime.now()
        year_join = self.get_year_debut()
        return year_now.year - year_join

    @abstractmethod
    def to_dict(self) ->dict:
        '''Return a dictionary representation of a talent'''
        raise NotImplementedError("Must be implemented in subclass")


    @abstractmethod
    def get_details(self) -> str:
        '''Return details of talent'''
        raise NotImplementedError("Must be implemented in subclass")

    @abstractmethod
    def get_type(self) -> str:
        '''Return type of talent'''
        raise NotImplementedError("Must be implemented in subclass")

    @staticmethod
    def _validate_string_input(display_name, str_value):
        """ Private helper to validate string values """

        if str_value is None:
            raise ValueError(display_name + " cannot be undefined.")

        if str_value == "":
            raise ValueError(display_name + " cannot be empty.")

    @staticmethod
    def _validate_integer_input(display_name, int_value):
        """ Private helper to validate integer values """

        if type(int_value) != type(0):
            raise ValueError(display_name + " has to be an integer.")

        if int_value is None:
            raise ValueError(display_name + " cannot be undefined.")

        if int_value == "":
            raise ValueError(display_name + " cannot be empty.")

        if int_value < 0 :
            raise ValueError(display_name + " cannot be negative.")

