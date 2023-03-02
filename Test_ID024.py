import unittest
import pymysql
import os

"""
INSERT INTO TDD.employee (Emp_id, Emp_firstname, Emp_lastname, Emp_Address, Emp_country, Emp_dateofbirth, Emp_work_policy, Employee_join_date, Employee_end_date, Employee_new_role_date)
VALUES 

('E021', 'Sarah', 'Jones', '10 Main St.', 'USA', '1990-05-10', 'Remote', '2020-01-01', '2023-06-30', NULL),
('E022', 'David', 'Nguyen', '15 Elm St.', 'Canada', '1993-08-15', 'Onsite', '2019-03-12', '2022-12-31', NULL),
('E023', 'Megan', 'Lee', '20 Oak St.', 'USA', '1987-02-28', 'Onsite', '2018-05-01', '2021-12-31', '2021-09-15'),
('E024', 'Ahmed', 'Khan', '25 Pine St.', 'Pakistan', '1995-01-12', 'Remote', '2021-01-15', '2022-06-30', NULL),
('E025', 'Emily', 'Garcia', '30 Maple St.', 'Mexico', '1992-12-01', 'Remote', '2020-07-01', '2021-12-31', '2021-10-01'),
('E026', 'Trevor', 'Wang', '35 Cedar St.', 'China', '1988-09-20', 'Onsite', '2017-02-15', '2022-06-30', '2022-01-01'),
('E027', 'Julia', 'Kim', '40 Walnut St.', 'South Korea', '1994-06-05', 'Onsite', '2019-05-01', '2023-12-31', NULL),
('E028', 'Ali', 'Hassan', '45 Birch St.', 'Lebanon', '1991-03-25', 'Remote', '2020-01-01', '2022-12-31', '2022-08-01'),
('E029', 'Daniel', 'Raj', '50 Hickory St.', 'India', '1993-11-08', 'Remote', '2018-06-01', '2021-12-31', NULL),
('E030', 'Lila', 'Singh', '55 Spruce St.', 'India', '1996-04-18', 'Onsite', '2020-10-01', '2023-09-30', NULL),
('E031', 'Jasmine', 'Liu', '60 Oakwood St.', 'China', '1995-07-20', 'Onsite', '2021-03-01', '2022-12-31', NULL),
('E032', 'Hector', 'Gomez', '65 Cedar St.', 'Mexico', '1991-01-05', 'Remote', '2019-01-01', '2023-12-31', '2022-06-01'),
('E033', 'Ava', 'Baker', '70 Maple St.', 'USA', '1994-04-30', 'Onsite', '2018-06-01', '2021-12-31', NULL),
('E034', 'Mohammed', 'Ali', '75 Pine St.', 'Egypt', '1990-11-15', 'Remote', '2020-03-01', '2021-12-31', '2021-10-15'),
('E035', 'Emma', 'Chen', '80 Walnut St.', 'China', '1993-12-10', 'Onsite', '2019-07-01', '2023-06-30', NULL),
('E036', 'Mateo', 'Garcia', '85 Hickory St.', 'Spain', '1996-02-22', 'Onsite', '2020-01-01', '2023-12-31', '2023-03-01'),
('E037', 'Aria', 'Park', '90 Spruce St.', 'South Korea', '1992-09-01', 'Remote', '2018-01-01', '2021-12-31', NULL),
('E038', 'Ankit', 'Patel', '95 Birch St.', 'India', '1995-06-18', 'Onsite', '2021-01-15', '2022-12-31', NULL),
('E039', 'Lily', 'Zhao', '100 Oak St.', 'China', '1989-08-28', 'Onsite', '2017-11-01', '2022-06-30', '2021-12-01'),
('E040', 'Miguel', 'Hernandez', '105 Elm St.', 'Mexico', '1994-03-10', 'Remote', '2020-06-01', '2021-12-31', NULL);

"""

class TestAddDataEmployeeTable(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.db = pymysql.connect(
            host=os.getenv("mysql_host"),
            user=os.getenv("mysql_user"),
            password=os.getenv("mysql_pwd"),
            database=os.getenv("mysql_db")
        )
        cls.cursor = cls.db.cursor()
    
    def test_add_data(self):
        self.cursor.execute("SELECT * FROM TDD.employee")
        result = self.cursor.fetchall()
        self.assertEqual(len(result), 44, "Data not added to employee table")

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)