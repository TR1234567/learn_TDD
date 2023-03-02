import unittest
import pymysql
import os
class TestCreateEmployeeTable(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.connection =pymysql.connect(
            host=os.getenv("mysql_host"),
            user=os.getenv("mysql_user"),
            password=os.getenv("mysql_pwd"),
            database=os.getenv("mysql_db")
        )
        cls.cursor = cls.connection.cursor()
        
    @classmethod
    def test_table_exist(self):
        self.cursor.execute("SHOW TABLES LIKE 'employee'")
        result = self.cursor.fetchone()
        self.assertIsNotNone(result, "Table 'employee' does not exist")
    
    def test_column_names(self):
        self.cursor.execute("DESCRIBE employee")
        result = self.cursor.fetchall()
        column_names = [row[0] for row in result]
        expected_column_names = ['Emp_id', 'Emp_firstname', 'Emp_lastname', 'Emp_Address', 'Emp_country', 'Emp_dateofbirth','Emp_work_policy','Employee_join_date','Employee_end_date','Employee_new_role_date']
        self.assertEqual(column_names, expected_column_names, "Column names do not match")

    def test_column_types(self):
        self.cursor.execute("DESCRIBE employee")
        result = self.cursor.fetchall()
        column_types = [row[1] for row in result]
        expected_column_types = ['varchar(20)', 'varchar(45)', 'varchar(45)', 'varchar(90)', 'varchar(45)', 'date','varchar(45)','date','date','date']
        self.assertEqual(column_types, expected_column_types, "Column types do not match")
        
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
