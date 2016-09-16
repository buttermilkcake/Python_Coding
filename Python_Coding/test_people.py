import unittest
from raise_people import People

class TestPeople(unittest.TestCase):
    """Tests for the class People."""

    def test_raise(self):
        """Test that the individual gets a raise."""
        monies = "What is the new raise amount?"
        my_rich_people = People(monies)
        my_rich_people.increment_raise(5000)

        self.assertIn(5000, my_rich_people.give_raise)

unittest.main()        
        
        
