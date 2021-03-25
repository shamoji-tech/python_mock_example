import unittest
from unittest.mock import MagicMock, patch, PropertyMock
from src.some_code import code1, code2
from src.dao.some_dao import DAO
class TestSomeCode(unittest.TestCase):
    
    @patch.object(DAO, 'insert', return_value=print("Hello! python"))
    def test_code1_1(self,_):
        """How to patch to the dao
        
        You can use the patch.object decorator to patch your internally used classes.
        patch.object can be applied to anything and transformed into anything.
        try `python -m unittest discover -s test/` in repository-root folder.
        """
        code1()
    
    @patch('src.dao.some_dao.DAO.insert', return_value=print("Hello! python"))
    def test_code1_2(self, _):
        """
        another version.
        """
        code1()
        
    @patch('src.dao.some_dao.DAO.insert')
    def test_code1_3(self, mock_accessor):
        """
        another version.
        """
        mock_accessor = print("Hello! python")
        code1()