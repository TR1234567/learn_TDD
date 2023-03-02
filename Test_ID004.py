import unittest
import pymysql
import os
class TestConstraintEmployeeTable(unittest.TestCase):
        
        @classmethod
        def setUpClass(cls):
            cls.db = pymysql.connect(
                host=os.getenv("mysql_host"),
                user=os.getenv("mysql_user"),
                password=os.getenv("mysql_pwd"),
                database=os.getenv("mysql_db")
            )
            cls.cursor = cls.db.cursor()
        def test_unique(self):
            self.cursor.execute("SELECT Emp_id, COUNT(*) FROM TDD.employee GROUP BY Emp_id HAVING COUNT(*) > 1")
            result = self.cursor.fetchone()
            self.assertIsNone(result, "Emp_id is not unique")
        def test_primary_key(self):
            self.cursor.execute("SHOW KEYS FROM TDD.employee WHERE Key_name = 'PRIMARY'")
            result = self.cursor.fetchone()
            self.assertIsNotNone(result, "Primary key does not exist")
            self.assertEqual(result[4], 'Emp_id', "Primary key is not 'Emp_id'")
        
        
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)