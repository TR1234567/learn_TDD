import unittest
import pymysql
import os

#Validate top 10 employee by salary along with their department name and technology name
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

    def test_top_10(self):
        self.cursor.execute("""
        SELECT f.emp_salary ,d.Dept_name ,t.Tech_name
        FROM TDD.employee e 
        INNER JOIN TDD.finance f 
        ON f.Emp_id = e.Emp_id 
        INNER JOIN TDD.department d 
        ON d.Dept_id = f.Dept_id 
        INNER JOIN TDD.technology t 
        ON t.Tech_id = f.Tech_id
        ORDER BY f.emp_salary DESC LIMIT 10;
        """)
        result = self.cursor.fetchall()
        self.assertIsNotNone(result, "No result found")

    def test_count_top_10(self):
        self.cursor.execute("""
        SELECT f.emp_salary ,d.Dept_name ,t.Tech_name
        FROM TDD.employee e
        INNER JOIN TDD.finance f
        ON f.Emp_id = e.Emp_id
        INNER JOIN TDD.department d
        ON d.Dept_id = f.Dept_id
        INNER JOIN TDD.technology t
        ON t.Tech_id = f.Tech_id
        ORDER BY f.emp_salary DESC LIMIT 10;
        """)
        result = self.cursor.fetchall()
        self.assertEqual(len(result), 10, "Number of records is not 10")

    def test_top_10_salary(self):
        self.cursor.execute("""
        SELECT f.emp_salary ,d.Dept_name ,t.Tech_name
        FROM TDD.employee e
        INNER JOIN TDD.finance f
        ON f.Emp_id = e.Emp_id
        INNER JOIN TDD.department d
        ON d.Dept_id = f.Dept_id
        INNER JOIN TDD.technology t
        ON t.Tech_id = f.Tech_id
        ORDER BY f.emp_salary DESC LIMIT 10;
        """)
        result = self.cursor.fetchall()
        self.assertEqual(result[0][0], 155000, "Top salary is not 155000")
        self.assertEqual(result[1][0], 150000, "Second salary is not 150000")
        self.assertEqual(result[2][0], 145000, "Third salary is not 145000")
        self.assertEqual(result[3][0], 140000, "Fourth salary is not 140000")
        self.assertEqual(result[4][0], 135000, "Fifth salary is not 135000")
        self.assertEqual(result[5][0], 130000, "Sixth salary is not 130000")
        self.assertEqual(result[6][0], 125000, "Seventh salary is not 125000")
        self.assertEqual(result[7][0], 120000, "Eighth salary is not 120000")
        self.assertEqual(result[8][0], 115000, "Ninth salary is not 115000")
        self.assertEqual(result[9][0], 110000, "Tenth salary is not 110000")

    
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)

