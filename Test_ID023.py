import unittest
import pymysql
import os
"""
INSERT INTO TDD.project (Id, Prj_id,emp_id,Dept_id,Prj_name,Prj_team_size,Prj_budget,Budget_currency ,Prj_client)
VALUES 
  (24, 'P040', 'E037', 'D019', 'Miami 2', 10, 2000000, 'USD', 'Royal Caribbean Group'),
  (25, 'P041', 'E038', 'D020', 'Boston 2', 8, 1700000, 'USD', 'State Street Corporation'),
  (26, 'P042', 'E039', 'D021', 'Seattle 2', 11, 2400000, 'USD', 'Microsoft'),
  (27, 'P043', 'E040', 'D022', 'Houston 2', 7, 1400000, 'USD', 'Chevron Corporation'),
  (28, 'P044', 'E041', 'D023', 'Austin 2', 12, 2200000, 'USD', 'Whole Foods Market'),
  (29, 'P045', 'E042', 'D013', 'JP 3', 9, 1900000, 'USD', 'Toyota'),
  (30, 'P046', 'E043', 'D014', 'NY 3', 13, 2600000, 'USD', 'Morgan Stanley'),
  (31, 'P047', 'E044', 'D015', 'SF 3', 8, 1500000, 'USD', 'Uber'),
  (32, 'P048', 'E045', 'D016', 'LA 3', 10, 1800000, 'USD', 'Warner Bros. Pictures'),
  (33, 'P049', 'E046', 'D017', 'Chicago 3', 6, 1200000, 'USD', 'United Continental Holdings'),
  (34, 'P050', 'E047', 'D018', 'Dallas 3', 11, 2400000, 'USD', 'Southwest Airlines'),
  (35, 'P051', 'E048', 'D019', 'Miami 3', 9, 1900000, 'USD', 'Carnival Cruise Line'),
  (36, 'P052', 'E049', 'D020', 'Boston 3', 12, 2200000, 'USD', 'Boston Scientific'),
  (37, 'P053', 'E050', 'D021', 'Seattle 3', 8, 1700000, 'USD', 'Nordstrom'),
  (38, 'P054', 'E051', 'D022', 'Houston 3', 10, 1800000, 'USD', 'Phillips 66'),
  (39, 'P055', 'E052', 'D023', 'Austin 3', 7, 1400000, 'USD', 'National Instruments'),
  (40, 'P056', 'E053', 'D013', 'JP 4', 11, 2400000, 'USD', 'SoftBank Group'),
  (41, 'P057', 'E054', 'D014', 'NY 4', 8, 1500000, 'USD', 'American Express'),
  (42, 'P058', 'E055', 'D015', 'SF 4', 12, 2200000, 'USD', 'Airbnb'),
  (43, 'P059', 'E056', 'D016', 'LA 4', 7, 1400000, 'USD', '20th Century Studios'),
  (44, 'P060', 'E057', 'D013', 'LA 5', 2, 123000, 'USD', 'Airbnb');
"""



class TestAddDataProjectTable(unittest.TestCase):
    
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
        self.cursor.execute("SELECT * FROM TDD.project")
        result = self.cursor.fetchall()
        self.assertEqual(len(result), 44, "Data not added to project table")

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)