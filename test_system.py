
import sys
from io import StringIO
import unittest
from unittest.mock import patch

# Import functions from the main file
# We need to wrap this because 'community management.py' has spaces and executes main() on import if not careful
# Actually, I'll rename the file to community_management.py for easier importing and better naming standards
import importlib.util
spec = importlib.util.spec_from_file_location("community_management", "community management.py")
cm = importlib.util.module_from_spec(spec)
spec.loader.exec_module(cm)

class TestCommunitySystem(unittest.TestCase):
    def setUp(self):
        cm.community_members = [] # Reset before each test

    def test_add_member(self):
        with patch('builtins.input', side_effect=['M001', 'Alice', '30', 'alice@example.com']):
            cm.add_member()
        self.assertEqual(len(cm.community_members), 1)
        self.assertEqual(cm.community_members[0]['name'], 'Alice')

    def test_add_duplicate_id(self):
        cm.community_members = [{'id': 'M001', 'name': 'Alice', 'age': '30', 'email': 'alice@example.com'}]
        with patch('builtins.input', side_effect=['M001']):
            cm.add_member()
        self.assertEqual(len(cm.community_members), 1) # Should not add

    def test_delete_member(self):
        cm.community_members = [{'id': 'M001', 'name': 'Alice', 'age': '30', 'email': 'alice@example.com'}]
        with patch('builtins.input', side_effect=['M001']):
            cm.delete_member()
        self.assertEqual(len(cm.community_members), 0)

    def test_search_member(self):
        cm.community_members = [
            {'id': 'M001', 'name': 'Alice', 'age': '30', 'email': 'alice@example.com'},
            {'id': 'M002', 'name': 'Bob', 'age': '25', 'email': 'bob@example.com'}
        ]
        with patch('sys.stdout', new=StringIO()) as fake_out:
            with patch('builtins.input', side_effect=['Alice']):
                cm.search_member()
            self.assertIn('Alice', fake_out.getvalue())
            self.assertNotIn('Bob', fake_out.getvalue())

if __name__ == '__main__':
    unittest.main()
