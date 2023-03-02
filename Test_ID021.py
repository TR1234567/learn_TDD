import unittest
import pymysql
import os
class TestActiveEmployeeTable(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.db = pymysql.connect(
            host=os.getenv("mysql_host"),
            user=os.getenv("mysql_user"),
            password=os.getenv("mysql_pwd"),
            database=os.getenv("mysql_db")
        )
        cls.cursor = cls.db.cursor()

    def test_active_employee_table(self):
        self.cursor.execute("""
        SELECT e.Emp_firstname ,e.Emp_lastname ,d.Dept_name ,t.Tech_name,p.Prj_name, e.Employee_end_date  FROM TDD.employee e 
        INNER JOIN TDD.finance f 
        ON f.Emp_id = e.Emp_id 
        INNER JOIN TDD.department d 
        ON d.Dept_id = f.Dept_id 
        INNER JOIN TDD.technology t 
        ON t.Tech_id = f.Tech_id
        INNER JOIN TDD.project p 
        ON p.emp_id = e.Emp_id 
        WHERE e.Employee_end_date IS NULL;  
        """)
        result = self.cursor.fetchall()
        self.assertIsNotNone(result, "There is no data")

    def test_count_active_employee_table(self):
        self.cursor.execute("""
        SELECT e.Emp_firstname ,e.Emp_lastname ,d.Dept_name ,t.Tech_name,p.Prj_name, e.Employee_end_date  FROM TDD.employee e 
        INNER JOIN TDD.finance f 
        ON f.Emp_id = e.Emp_id 
        INNER JOIN TDD.department d 
        ON d.Dept_id = f.Dept_id 
        INNER JOIN TDD.technology t 
        ON t.Tech_id = f.Tech_id
        INNER JOIN TDD.project p 
        ON p.emp_id = e.Emp_id 
        WHERE e.Employee_end_date IS NULL;  
        """)
        result = self.cursor.fetchall()
        self.assertEqual(len(result), 4, "Result is false")

    def test_non_active_employee_table(self):
        self.cursor.execute("""
        SELECT e.Emp_firstname ,e.Emp_lastname ,d.Dept_name ,t.Tech_name,p.Prj_name, e.Employee_end_date  FROM TDD.employee e 
        INNER JOIN TDD.finance f 
        ON f.Emp_id = e.Emp_id 
        INNER JOIN TDD.department d 
        ON d.Dept_id = f.Dept_id 
        INNER JOIN TDD.technology t 
        ON t.Tech_id = f.Tech_id
        INNER JOIN TDD.project p 
        ON p.emp_id = e.Emp_id 
        WHERE e.Employee_end_date IS NOT NULL;  
        """)
        result = self.cursor.fetchall()
        self.assertIsNotNone(result, "There is no data")
    
    def test_count_non_active_employee_table(self):
        self.cursor.execute("""
        SELECT e.Emp_firstname ,e.Emp_lastname ,d.Dept_name ,t.Tech_name,p.Prj_name, e.Employee_end_date  FROM TDD.employee e 
        INNER JOIN TDD.finance f 
        ON f.Emp_id = e.Emp_id 
        INNER JOIN TDD.department d 
        ON d.Dept_id = f.Dept_id 
        INNER JOIN TDD.technology t 
        ON t.Tech_id = f.Tech_id
        INNER JOIN TDD.project p 
        ON p.emp_id = e.Emp_id 
        WHERE e.Employee_end_date IS NOT NULL;  
        """)
        result = self.cursor.fetchall()
        self.assertEqual(len(result), 1, "Result is false")

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)