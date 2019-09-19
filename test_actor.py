import unittest
from unittest import TestCase
import inspect
from actor import Actor
import datetime

class TestActor(TestCase):
    '''Unit tests for the TestActor Class.'''
    def setUp(self):
        """ Creates a test fixture before each test method is run """
        self.actor1 = Actor("Sub","Hossan","A01050900","2012-12-25 00:00:00",3)
        self.actor1.set_id(1)
        self.actor2 = Actor("Ewan","Watt","A01020509","1995-04-08 00:00:00",0)
        self.actor2.set_id(2)
        self.actor3 = Actor("Tom", "Cruise", "A01021122", "1999-04-28 00:00:00", 0)
        self.actor3.set_id(3)
        self.actor4 = Actor("Anna", "Bell", "A01030900", "2018-04-28 00:00:00", 1)
        self.actor4.set_id(4)

        self.logPoint()


    def tearDown(self):
        """ Prints a log point when test is finished """
        self.logPoint()

    def logPoint(self):
        """ Utility function used for module functions and class methods """
        current_test = self.id().split('.')[-1]
        calling_function = inspect.stack()[1][3]
        print('in %s - %s()' % (current_test, calling_function))



    def test_valid_constructor(self):
        '''Test with valid constructor'''
        self.assertIsNotNone(self.actor1,"Actor must be defined.")

    def test_constructor_empty(self):
        '''Test with empty  parameter of constructor'''
        self.assertRaisesRegex(ValueError,"First Name cannot be empty.",Actor,"","Hossan","A01050900","2012-12-25",3)
        self.assertRaisesRegex(ValueError, "Last Name cannot be empty.", Actor, "Sub", "", "A01050900", "2012-12-25",3)
        self.assertRaisesRegex(ValueError, "Talent Number cannot be empty.", Actor, "Sub", "Hossan", "", "2012-12-25", 3)
        self.assertRaisesRegex(ValueError, "Date Debut cannot be empty.", Actor, "Sub", "Hossan", "A01050900", "", 3)
        self.assertRaisesRegex(ValueError, "Award Number has to be an integer.", Actor, "Sub", "Hossan", "A01050900", "2012-12-25", "")

    def test_constructor_none(self):
        '''Test with none  parameter of constructor'''
        self.assertRaisesRegex(ValueError,"First Name cannot be undefined.",Actor,None,"Hossan","A01050900","2012-12-25",3)
        self.assertRaisesRegex(ValueError, "Last Name cannot be undefined.", Actor, "Sub",None, "A01050900", "2012-12-25",3)
        self.assertRaisesRegex(ValueError, "Talent Number cannot be undefined.", Actor, "Sub", "Hossan",None, "2012-12-25", 3)
        self.assertRaisesRegex(ValueError, "Date Debut cannot be undefined.", Actor, "Sub", "Hossan", "A01050900",None, 3)
        self.assertRaisesRegex(ValueError, "Award Number has to be an integer.", Actor, "Sub", "Hossan", "A01050900", "2012-12-25",None)

    def test_add_movie(self):
        "Test with valid new movie"
        self.actor1._movie_list = []
        self.actor1.add_movie('Gone with the wind')
        self.assertEqual(self.actor1.get_movie_list(),['Gone with the wind'])

        self.actor1._movie_list = ['Gone with the wind']
        self.actor1.add_movie('Harry Porter')
        self.assertEqual(self.actor1.get_movie_list(), ['Gone with the wind', 'Harry Porter'])

    def test_add_movie_exist(self):
        "Test with existing new movie"
        self.actor1._movie_list = ['Gone with the wind']
        self.actor1.add_movie('Gone with the wind')
        self.assertEqual(self.actor1.get_movie_list(),['Gone with the wind'])

    def test_get_movie_summary(self):
        '''Test with valid movie summary'''
        self.actor1._movie_list = ['Gone with the wind', 'Harry Porter']
        self.assertEqual(self.actor1.get_movie_summary(),"Sub, Hossan is an actor in the Gone with the wind, Harry Porter")

    def test_get_num_movie(self):
        '''Test with valid number of movie'''
        self.actor1._movie_list = ['Gone with the wind', 'Harry Porter']
        self.assertEqual(self.actor1.get_num_movie(),2)

    def test_get_num_award(self):
        '''Test with valid number of awards'''
        self.assertEqual(self.actor1.get_num_award(),3)

    def test_get_details(self):
        '''Test with valid details'''
        self.assertEqual(self.actor1.get_details(), "Sub, Hossan id 1 talent number A01050900 year debuted 2012 has 3 awards")
        self.assertEqual(self.actor2.get_details(), "Ewan, Watt id 2 talent number A01020509 year debuted 1995 has no award")
        self.assertEqual(self.actor3.get_details(), "Tom, Cruise id 3 talent number A01021122 year debuted 1999 has no award")
        self.assertEqual(self.actor4.get_details(), "Anna, Bell id 4 talent number A01030900 year debuted 2018 has 1 awards")

    def test_get_type(self):
        '''Test with valid type'''
        self.assertEqual(self.actor1.get_type(),"actor")
        self.assertEqual(self.actor2.get_type(), "actor")
        self.assertEqual(self.actor3.get_type(), "actor")
        self.assertEqual(self.actor4.get_type(), "actor")

    def test_get_id(self):
        '''Test with valid id'''
        self.assertEqual(self.actor1.get_id(),1)

    def test_set_id(self):
        '''Test with valid id'''

        self.actor1.set_id(2)
        self.assertEqual(self.actor1.get_id(),2)

    def test_get_first_name(self):
        "Test with valid first name"
        self.assertEqual(self.actor1.get_first_name(),"Sub" )


    def test_get_last_name(self):
        "Test with valid last name"
        self.assertEqual(self.actor1.get_last_name(),"Hossan" )


    def test_get_full_name(self):
        "Test with valid full name"
        self.assertEqual(self.actor1.get_full_name(),"Sub, Hossan" )

    def test_get_talent_num(self):
        "Test with valid talent num"
        self.assertEqual(self.actor1.get_talent_num(),"A01050900" )

    def test_get_year_debut(self):
        "Test with valid year debut"
        self.assertEqual(self.actor1.get_year_debut(),2012)

    def test_get_date_debut(self):
        "Test with valid date debut"
        self.assertEqual(self.actor1.get_date_debut(),datetime.datetime(2012, 12, 25, 0, 0))

    def test_get_years_debut(self):
        "Test with valid num of years debut"
        self.assertEqual(self.actor1.get_years_debut(),7)

    def test_to_dict(self):
        """Test with valid return of a dictionary represenation of an actor"""

        self.assertEqual(self.actor1.to_dict(),
                         {'award_num': 3,
                         'date_debut': '2012-12-25 00:00:00',
                         'first_name': 'Sub',
                         'id': 1,
                         'last_name': 'Hossan',
                         'movie_list': [],
                         'talent_num': 'A01050900',
                         'type': 'actor'})

