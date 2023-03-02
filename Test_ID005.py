import unittest
import pymysql
import os
class TestCreateDepartmentTable(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.connection = pymysql.connect(
            host=os.getenv("mysql_host"),
            user=os.getenv("mysql_user"),
            password=os.getenv("mysql_pwd"),
            database=os.getenv("mysql_db")
        )
        cls.cursor = cls.connection.cursor()
        
    @classmethod

    def test_table_exist(self):
        self.cursor.execute("SHOW TABLES LIKE 'department'")
        result = self.cursor.fetchone()
        self.assertIsNotNone(result, "Table 'department' does not exist")
    
    def test_column_names(self):
        self.cursor.execute("DESCRIBE department")
        result = self.cursor.fetchall()
        column_names = [row[0] for row in result]
        expected_column_names = ['Id','Dept_id', 'Emp_id', 'Dept_name', 'Dept_code', 'Dept_count','Dept_function']
        self.assertEqual(column_names, expected_column_names, "Column names do not match")
        
    def test_column_types(self):
        self.cursor.execute("DESCRIBE department")
        result = self.cursor.fetchall()
        column_types = [row[1] for row in result]
        expected_column_types = ['int','varchar(20)', 'varchar(20)', 'varchar(45)', 'varchar(45)', 'varchar(45)', 'varchar(45)']
        self.assertEqual(column_types, expected_column_types, "Column types do not match")
        
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
