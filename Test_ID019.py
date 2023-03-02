import unittest
import pymysql
import os


class TestAddNewColumn(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.db = pymysql.connect(
            host=os.getenv("mysql_host"),
            user=os.getenv("mysql_user"),
            password=os.getenv("mysql_pwd"),
            database=os.getenv("mysql_db")
        )
        cls.cursor = cls.db.cursor()
# Check new table Employee_join_date, Employee_end_date, Employee_new_role_date name is exist and type is date
    def test_Employee_join_date_Exist(self):
        self.cursor.execute("""
        SELECT COLUMN_NAME, DATA_TYPE FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = 'employee' AND COLUMN_NAME = 'Employee_join_date';
        """)
        result = self.cursor.fetchall()
        self.assertIsNotNone(result, "Employee_join_date is not exist")
        self.assertEqual(result[0][1], "date", "Type is not date")

    def test_Employee_end_date_Exist(self):
        self.cursor.execute("""
        SELECT COLUMN_NAME, DATA_TYPE FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = 'employee' AND COLUMN_NAME = 'Employee_end_date';
        """)
        result = self.cursor.fetchall()
        self.assertIsNotNone(result, "Employee_end_date is not exist")
        self.assertEqual(result[0][1], "date", "Type is not date")

    def test_Employee_new_role_date_Exist(self):
        self.cursor.execute("""
        SELECT COLUMN_NAME, DATA_TYPE FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = 'employee' AND COLUMN_NAME = 'Employee_new_role_date';
        """)
        result = self.cursor.fetchall()
        self.assertIsNotNone(result, "Employee_new_role_date is not exist")
        self.assertEqual(result[0][1], "date", "Type is not date")
    


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)


