from unittest import TestCase
from actor import Actor
from model import Model
from talent_agency import TalentAgency
import inspect
from unittest.mock import MagicMock
from unittest.mock import patch, mock_open

class TestTalentAgency(TestCase):
    '''Unit tests for the TestTalentAgency Class'''

    @patch('builtins.open', mock_open(read_data=''))
    def setUp(self):
        """ Creates a test fixture before each test method is run """
        self.actor1 = Actor("Sub","Hossan","A01050900","2012-12-25 00:00:00",3)
        self.actor2 = Actor("Ewan","Watt","A01020509","1995-04-08 00:00:00",0)

        self.model1 = Model("Ashvan", "Wal", "A01023474", "2000-01-15 00:00:00", "commercial")
        self.model2 = Model("Phuong", "Ho", "A01023444", "2011-05-23 00:00:00", "vedette")

        self.talent1 = TalentAgency("testresults.json")
        self.logPoint()

    @patch('builtins.open', mock_open(read_data=''))
    def test_valid_constructor(self):
        '''Test with valid constructor'''
        self.talent1._talents = []
        self.assertEqual(self.talent1.get_all(),[])

    @patch('builtins.open', mock_open(read_data=''))
    def test_add_talent(self):
        '''Test with valid talent'''
        self.talent1.add_talent(self.model1)
        self.talent1.add_talent(self.model2)
        self.assertEqual(self.talent1.get_all(),[self.model1, self.model2])

        self.talent1.add_talent(self.actor1)
        # print(self.talent1.get_all())
        self.talent1.add_talent(self.actor2)
        self.assertEqual(self.talent1.get_all(),[self.model1,self.model2,self.actor1,self.actor2])

    @patch('builtins.open', mock_open(read_data=''))
    def test_add_invalid_talent(self):
        '''Test with invalid talent'''
        invalid_object = ""
        self.assertRaisesRegex(ValueError,"Talent object cannot be empty.",self.talent1.add_talent,invalid_object)

        invalid_object = None
        self.assertRaisesRegex(ValueError, "Talent object cannot be undefined.", self.talent1.add_talent, invalid_object)

    @patch('builtins.open', mock_open(read_data=''))
    def test_id_talent(self):
        '''Test with valid id talent created'''
        self.talent1.add_talent(self.model1)
        self.assertEqual(self.model1.get_id(),1)

        self.talent1.add_talent(self.model2)
        self.assertEqual(self.model2.get_id(),2)

        self.talent1.add_talent(self.actor1)
        self.assertEqual(self.actor1.get_id(),3)

        self.talent1.add_talent(self.actor2)
        self.assertEqual(self.actor2.get_id(),4)

    @patch('builtins.open', mock_open(read_data=''))
    def test_get_talent(self):
        '''Test with valid talent id'''
        self.talent1.add_talent(self.model1)
        self.talent1.add_talent(self.model2)
        self.talent1.add_talent(self.actor1)
        self.talent1.add_talent(self.actor2)

        self.assertEqual(self.talent1.get_talent(1),self.model1)

    @patch('builtins.open', mock_open(read_data=''))
    def test_get_talent_not_valid_talent_id(self):
        '''Test with invalid talent id'''
        invalid_id = "acb"
        self.assertRaisesRegex(ValueError, "Talent ID has to be an integer.", self.talent1.get_talent, invalid_id)

    @patch('builtins.open', mock_open(read_data=''))
    def test_get_talent_not_exist(self):
        '''Test with not exist talent id'''
        invalid_id = 4
        self.assertRaisesRegex(ValueError,"Talent ID does not exist", self.talent1.get_talent, invalid_id)


    @patch('builtins.open', mock_open(read_data=''))
    def test_get_all(self):
        '''Test with valid talents returned'''
        self.talent1.add_talent(self.model1)
        self.talent1.add_talent(self.model2)
        self.talent1.add_talent(self.actor1)
        self.talent1.add_talent(self.actor2)

        self.assertEqual(self.talent1.get_all(),[self.model1,self.model2,self.actor1,self.actor2])

    @patch('builtins.open', mock_open(read_data=''))
    def test_get_all_by_type(self):
        '''Test with valid talents by type'''
        self.talent1.add_talent(self.model1)
        self.talent1.add_talent(self.model2)
        self.talent1.add_talent(self.actor1)
        self.talent1.add_talent(self.actor2)

        self.assertEqual(self.talent1.get_all_by_type("actor"),[self.actor1,self.actor2])
        self.assertEqual(self.talent1.get_all_by_type("model"), [self.model1,self.model2])

    @patch('builtins.open', mock_open(read_data=''))
    def test_get_all_by_type_invalid_type(self):
        '''Test with invalid type'''
        self.talent1.add_talent(self.model1)
        self.talent1.add_talent(self.model2)
        self.talent1.add_talent(self.actor1)
        self.talent1.add_talent(self.actor2)

        invalid_type_empty = ""
        self.assertRaisesRegex(ValueError, "Type cannot be empty.", self.talent1.get_all_by_type, invalid_type_empty)

        invalid_type_none = None
        self.assertRaisesRegex(ValueError, "Type cannot be undefined.", self.talent1.get_all_by_type,
                               invalid_type_none)

    @patch('builtins.open', mock_open(read_data=''))
    def test_update_model(self):
        '''Test with valid update model'''
        self.talent1.add_talent(self.model1)
        self.talent1.add_talent(self.model2)
        self.talent1.add_talent(self.actor1)
        self.talent1.add_talent(self.actor2)

        self.model3 = Model("David", "Magno", "A01023547", "2004-07-27 00:00:00", "editorial")
        self.model3.set_id(1)
        self.talent1.update(self.model3)
        object = self.talent1.get_all()
        self.assertEqual(object[0],self.model3)

    @patch('builtins.open', mock_open(read_data=''))
    def test_update_actor(self):
        '''Test with valid update actor '''
        self.talent1.add_talent(self.model1)
        self.talent1.add_talent(self.model2)
        self.talent1.add_talent(self.actor1)
        self.talent1.add_talent(self.actor2)

        self.actor3 = Actor("Tom", "Cruise", "A01021122", "1999-04-28 00:00:00", 0)
        self.actor3.set_id(3)
        self.talent1.update(self.actor3)
        object = self.talent1.get_all()
        self.assertEqual(object[2], self.actor3)

    @patch('builtins.open', mock_open(read_data=''))
    def test_update_model_not_exist(self):
        '''Test with model not exist in the list '''
        self.talent1.add_talent(self.model1)
        self.talent1.add_talent(self.model2)
        self.talent1.add_talent(self.actor1)
        self.talent1.add_talent(self.actor2)

        self.model3 = Model("David", "Magno", "A01023547", "2004-07-27 00:00:00", "editorial")
        self.model3.set_id(8)
        self.assertRaisesRegex(ValueError,"Talent ID does not exist", self.talent1.update, self.model3)

    @patch('builtins.open', mock_open(read_data=''))
    def test_update_actor_not_exist(self):
        '''Test with actor not exist in the list '''
        self.talent1.add_talent(self.model1)
        self.talent1.add_talent(self.model2)
        self.talent1.add_talent(self.actor1)
        self.talent1.add_talent(self.actor2)

        self.actor3 = Actor("Tom", "Cruise", "A01021122", "1999-04-28 00:00:00", 0)
        self.actor3.set_id(7)
        self.assertRaisesRegex(ValueError,"Talent ID does not exist", self.talent1.update, self.actor3)

    @patch('builtins.open', mock_open(read_data=''))
    def test_update_invalid_talent(self):
        '''Test with invalid talent'''
        invalid_object = ""
        self.assertRaisesRegex(ValueError, "Talent object cannot be empty.", self.talent1.update, invalid_object)

        invalid_object = None
        self.assertRaisesRegex(ValueError, "Talent object cannot be undefined.", self.talent1.update,
                               invalid_object)

    @patch('builtins.open', mock_open(read_data=''))
    def test_delete_model(self):
        '''Test with valid model deleted'''
        self.talent1.add_talent(self.model1)
        self.talent1.add_talent(self.model2)
        self.talent1.add_talent(self.actor1)
        self.talent1.add_talent(self.actor2)

        self.talent1.delete(2)
        self.assertEqual(self.talent1.get_all(),[self.model1,self.actor1,self.actor2])


    @patch('builtins.open', mock_open(read_data=''))
    def test_delete_actor(self):
        '''Test with valid actor deleted'''
        self.talent1.add_talent(self.model1)
        self.talent1.add_talent(self.model2)
        self.talent1.add_talent(self.actor1)
        self.talent1.add_talent(self.actor2)

        self.talent1.delete(3)
        self.assertEqual(self.talent1.get_all(), [self.model1, self.model2, self.actor2])

    @patch('builtins.open', mock_open(read_data=''))
    def test_delete_model_not_exist(self):
        '''Test with not exist talent deleted'''
        self.talent1.add_talent(self.model1)
        self.talent1.add_talent(self.model2)
        self.talent1.add_talent(self.actor1)
        self.talent1.add_talent(self.actor2)

        self.assertRaisesRegex(ValueError,"Talent ID does not exist",self.talent1.delete,6)


    @patch('builtins.open', mock_open(read_data=''))
    def tearDown(self):
        """ Prints a log point when test is finished """
        self.logPoint()

    @patch('builtins.open', mock_open(read_data=''))
    def logPoint(self):
        """ Utility function used for module functions and class methods """
        current_test = self.id().split('.')[-1]
        calling_function = inspect.stack()[1][3]
        print('in %s - %s()' % (current_test, calling_function))


    @patch('builtins.open', mock_open(read_data=''))
    def test_empty_constructor(self):
        '''Test with empty parameter of constructor'''
        self.assertRaisesRegex(ValueError,"File path cannot be empty",TalentAgency,"")

    @patch('builtins.open', mock_open(read_data=''))
    def test_none_constructor(self):
        '''Test with none parameter of constructor'''
        self.assertRaisesRegex(ValueError, "File path cannot be undefined", TalentAgency, None)


    @patch('builtins.open', mock_open(read_data=''))
    def test_add_talent_return_id(self):
        '''Test with valid talent'''
        self.assertEqual(self.talent1.add_talent(self.model1),1)


    @patch('builtins.open', mock_open(read_data=''))
    def test_valid_constructor_file(self):
        """Test with valid file path"""
        talent2 = TalentAgency("food.json")
        self.assertIsNotNone(talent2)
