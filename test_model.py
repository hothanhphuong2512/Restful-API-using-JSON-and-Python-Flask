from unittest import TestCase
from model import Model
import inspect
import datetime


class TestModel(TestCase):
    """Unit Tests for the TestModel Class"""

    def setUp(self):
        """Hook method for setting up the test fixture"""

        self.model1 = Model("Ashvan", "Wal", "A01023474", "2000-01-15 00:00:00", "commercial")
        self.model1.set_id(1)
        self.model2 = Model("Phuong", "Ho", "A01023444", "2011-05-23 00:00:00", "vedette")
        self.model2.set_id(2)
        self.model3 = Model("David", "Magno", "A01023547", "2004-07-27 00:00:00", "editorial")
        self.model3.set_id(3)
        self.model4 = Model("Ewan", "Watt", "A01025673", "2018-01-9 00:00:00", "vedette")
        self.model4.set_id(4)

    def tearDown(self):
        """Hook method for deconstructing the test fixture"""
        self.logPoint()

    def logPoint(self):
        currentTest = self.id().split('.')[-1]
        callingFunction = inspect.stack()[1][3]
        print('in %s - %s()' % (currentTest, callingFunction))

    def test_valid_constructor(self):
        '''Test with valid constructor'''
        self.assertIsNotNone(self.model1,"Model must be defined.")

    def test_empty_parms(self):
        """Tests for empty parameters"""

        self.assertRaisesRegex(ValueError, "cannot be empty", Model, "", "Wal", "A01023474", "2000-01-15", "commercial")
        self.assertRaisesRegex(ValueError, "cannot be empty", Model, "Ashvan", "", "A01023474", "2000-01-15", "commercial")
        self.assertRaisesRegex(ValueError, "cannot be empty", Model, "Ashvan", "Wal", "", "2000-01-15", "commercial")
        self.assertRaisesRegex(ValueError, "cannot be empty", Model, "Ashvan", "Wal", "", "2000-01-15", "commercial")
        self.assertRaisesRegex(ValueError, "cannot be empty", Model, "Ashvan", "Wal", "A01023474", "", "commercial")
        self.assertRaisesRegex(ValueError, "cannot be empty", Model, "Ashvan", "Wal", "A01023474", "2000-01-15", "")


    def test_undefined_param(self):
        """Tests for undefined parameters"""
        self.assertRaisesRegex(ValueError, "cannot be undefined", Model, None, "Wal", "A01023474", "2000-01-15", "commercial")
        self.assertRaisesRegex(ValueError, "cannot be undefined", Model, "Ashvan", None, "A01023474", "2000-01-15","commercial")
        self.assertRaisesRegex(ValueError, "cannot be undefined", Model, "Ashvan", "Wal", None, "2000-01-15", "commercial")
        self.assertRaisesRegex(ValueError, "cannot be undefined", Model, "Ashvan", "Wal", "A01023474", None, "commercial")
        self.assertRaisesRegex(ValueError, "cannot be undefined", Model, "Ashvan", "Wal", "A01023474", "2000-01-15", None)


    def test_get_model_type(self):
        """Get model type."""

        self.assertEqual(self.model1.get_model_type(), "commercial")
        self.assertEqual(self.model2.get_model_type(), "vedette")
        self.assertEqual(self.model3.get_model_type(), "editorial")

    def test_is_vedette(self):
        """Tests to see if model is vedette. if vedette returns true, else returns false."""
        self.assertEqual(self.model2.is_vedette(), True)
        self.assertEqual(self.model1.is_vedette(), False)
        self.assertEqual(self.model4.is_vedette(), True)


    def test_get_details(self):
        """Tests get_details"""
        self.assertEqual(self.model1.get_details(), "Ashvan, Wal with id: 1 , talent number: A01023474, Year debut: 2000 is a commercial model" )
        self.assertEqual(self.model2.get_details(), "Phuong, Ho with id: 2 , talent number: A01023444, Year debut: 2011 is a vedette model")
        self.assertEqual(self.model3.get_details(), "David, Magno with id: 3 , talent number: A01023547, Year debut: 2004 is a editorial model")
        self.assertEqual(self.model4.get_details(), "Ewan, Watt with id: 4 , talent number: A01025673, Year debut: 2018 is a vedette model")

    def test_get_type(self):
        """Tests get_type to see if type is returned."""
        self.assertEqual(self.model1.get_type(), "model")
        self.assertEqual(self.model4.get_type(), "model")

    def test_get_id(self):
        '''Test with valid id'''
        self.assertEqual(self.model1.get_id(), 1)

    def test_set_id(self):
        '''Test with valid id'''

        self.model1.set_id(2)
        self.assertEqual(self.model1.get_id(), 2)

    def test_get_first_name(self):
        "Test with valid first name"
        self.assertEqual(self.model1.get_first_name(), "Ashvan")

    def test_get_last_name(self):
        "Test with valid last name"
        self.assertEqual(self.model1.get_last_name(), "Wal")

    def test_get_full_name(self):
        "Test with valid full name"
        self.assertEqual(self.model1.get_full_name(), "Ashvan, Wal")

    def test_get_talent_num(self):
        "Test with valid talent num"
        self.assertEqual(self.model1.get_talent_num(), "A01023474")

    def test_get_year_debut(self):
        "Test with valid year debut"
        self.assertEqual(self.model1.get_year_debut(), 2000)

    def test_get_date_debut(self):
        "Test with valid date debut"
        self.assertEqual(self.model1.get_date_debut(), datetime.datetime(2000, 1, 15, 0, 0))

    def test_get_years_debut(self):
        "Test with valid num of years debut"
        self.assertEqual(self.model1.get_years_debut(), 19)

    def test_to_dict(self):
        """Test with valid return of a dictionary represenation of a model"""

        self.assertEqual(self.model1.to_dict(),
                         {'date_debut': '2000-01-15 00:00:00',
                          'first_name': 'Ashvan',
                          'id': 1,
                          'last_name': 'Wal',
                          'model_type': 'commercial',
                          'talent_num': 'A01023474',
                          'type': 'model'}
                       )

