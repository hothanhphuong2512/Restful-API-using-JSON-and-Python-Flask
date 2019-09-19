from abstract_talent import AbstractTalent
import datetime
class Actor(AbstractTalent):
    '''Maintain details of Actor class'''
    ACTOR_TYPE = "actor"


    def __init__(self, first_name, last_name, talent_num, date_debut,award_num):
        '''Constructor - Initializes the main attributes for the actor'''
        self._movie_list = []
        Actor._validate_integer_input("Award Number", award_num)
        self._award_num = award_num
        super().__init__(first_name, last_name, talent_num, date_debut)

    def add_movie(self, new_movie):
        '''Add new movie to list of movie actor plays'''
        Actor._validate_string_input("New Movie", new_movie)
        if len(self._movie_list) == 0:
            self._movie_list.append(new_movie)
        else:
            for movie in self._movie_list:
                exist = False
                if new_movie == movie:
                    exist = True
                if exist == False :
                    self._movie_list.append(new_movie)

    def get_movie_list(self) ->list:
        '''Return movie list'''
        return self._movie_list

    def get_movie_summary(self) ->str:
        '''Get movies actor plays'''
        if len(self._movie_list) > 0:
            movie_list = ', '.join(str(movie) for movie in self._movie_list)
            details = self.get_full_name() + " is an actor in the " + movie_list
            return details
        else:
            return "{} has no movie".format(self.get_full_name())

    def get_num_movie(self) ->int:
        '''Get number of movies actor plays'''
        return len(self._movie_list)

    def get_num_award(self) ->int:
        '''Get number of award actor has'''
        return self._award_num


    def get_details(self) ->str:
        '''Returns the actor's details in a printable format'''
        if self.get_num_award() < 1:
            return '{} id {} talent number {} year debuted {} has no award'.format(self.get_full_name(),
                                                                                   self.get_id(),
                                                                                   self.get_talent_num(),
                                                                                   self.get_year_debut())
        else:
            return '{} id {} talent number {} year debuted {} has {} awards'.format(self.get_full_name(),
                                                                                    self.get_id(),
                                                                                    self.get_talent_num(),
                                                                                         self.get_year_debut(),
                                                                                         self.get_num_award())

    def get_type(self) ->str:
        '''Return actor for any object in this class'''
        return Actor.ACTOR_TYPE


    def to_dict(self) -> dict:
        '''Return a dictionary representation of an actor'''
        dict = {}
        dict['id'] = self._id
        dict['first_name'] = self._first_name
        dict['last_name'] = self._last_name
        dict['talent_num'] = self._talent_num
        dict['date_debut'] = str(self._date_debut)
        dict['movie_list'] = self._movie_list
        dict['award_num'] = self._award_num
        dict['type'] = Actor.ACTOR_TYPE
        return dict

    @staticmethod
    def _validate_integer_input(display_name, int_value):
        """ Private helper to validate string values """

        if type(int_value) != type(0):
            raise ValueError(display_name + " has to be an integer.")

        if int_value < 0 :
            raise ValueError(display_name + " cannot be negative.")

        if int_value is None:
            raise ValueError(display_name + " cannot be undefined.")

        if int_value == "":
            raise ValueError(display_name + " cannot be empty.")

    @staticmethod
    def _validate_string_input(display_name, int_value):
        """ Private helper to validate string values """

        if int_value is None:
            raise ValueError(display_name + " cannot be undefined.")

        if int_value == "":
            raise ValueError(display_name + " cannot be empty.")
