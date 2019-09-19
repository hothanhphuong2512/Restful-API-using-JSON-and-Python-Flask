import json
from model import Model
from actor import Actor
import os.path
import datetime

class TalentAgency:
    '''Maintains details about talent agency'''
    def __init__(self,_filepath):
        """Constructor of TalentAgency"""

        self._talents = []

        self._validate_string_input("File path",_filepath)
        self._filepath = _filepath
        self._read_entities_from_file()

    def _read_entities_from_file(self):
        """Read talents from file"""
        if os.path.exists(self._filepath):
            with open(self._filepath,'r') as object_file:
                string = object_file.read()
                # print(string)

                if not string:
                    return

                else:
                    data = json.loads(string)
                    # print (data)

                    for talent in data:
                        if talent['type'] == 'model':

                            model = Model(talent['first_name'], talent['last_name'], talent['talent_num'], talent['date_debut'],
                                          talent['model_type'])
                            self.add_talent(model)


                        elif talent['type'] == 'actor':

                            actor =  Actor(talent['first_name'], talent['last_name'], talent['talent_num'], talent['date_debut'], talent['award_num'])

                            for movie in talent['movie_list']:
                               actor.get_movie_list().append(movie)

                            self.add_talent(actor)


    def _write_entities_from_file(self):
        """Write talent to file"""
        with open(self._filepath,'w+') as object_file:
            new_talent = []
            for talent_object in self._talents:
                # print(talent_object.to_dict())
                new_talent.append(talent_object.to_dict())
            # print(new_talent)
            object_file.write(json.dumps(new_talent, indent=4))


    def add_talent(self,talent_object):
        '''Return talent_id, adds new talent to the list of talents.'''

        self._validate_string_input("Talent object", talent_object)

        if len(self._talents) == 0:
            talent_id = 1
        else:
            talent_id = self._talents[-1].get_id() + 1

        talent_object.set_id(talent_id)

        if len(self._talents) == 0:
            self._talents.append(talent_object)
            self._write_entities_from_file()
        else:
            for talent in self._talents:
                exist = False
                if talent.get_id() == talent_object.get_id():
                    exist = True
                if exist == False:
                    self._talents.append(talent_object)
                    self._write_entities_from_file()
                    break

        return talent_id

    def get_talent(self, talent_id: int):
        '''Gets talent object based on talent_id'''

        self._validate_integer_input("Talent ID", talent_id)

        for talent in self._talents:
            if talent.get_id() == talent_id:
                return talent
        else:
            raise ValueError("Talent ID does not exist")

    def get_all(self) -> list:
        '''Returns list of all the talents.'''
        return self._talents

    def get_all_by_type(self, type: str) -> list:
        '''Returns talent list based on type provided'''

        self._validate_string_input("Type", type)

        list_all = []
        for talent in self._talents:
            if talent.get_type() == type:
                list_all.append(talent)
        return list_all

    def update(self, talent_object):
        '''Updates talent list based on talent_id provided'''

        self._validate_string_input("Talent object", talent_object)

        for index, talent in enumerate(self._talents):

            if talent_object.get_id() == talent.get_id():
                self._talents[index] = talent_object
                self._write_entities_from_file()
                return

        raise ValueError("Talent ID does not exist")

    def delete(self, talent_id: int):
        '''Deletes talent from list based on talent_id provided'''

        self._validate_integer_input("Talent ID", talent_id)
        for talent in self._talents:

            if talent.get_id() == talent_id:
                self._talents.remove(talent)
                self._write_entities_from_file()
                return

        raise ValueError("Talent ID does not exist")



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

