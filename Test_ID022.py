import unittest
import pymysql
import os

#create a class for the test the stored procedure
class TestStoredProcedure(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.db = pymysql.connect(
            host=os.getenv("mysql_host"),
            user=os.getenv("mysql_user"),
            password=os.getenv("mysql_pwd"),
            database=os.getenv("mysql_db")
        )
        cls.cursor = cls.db.cursor()

    def test_stored_procedure(self):
        self.cursor.execute("CALL TDD.is_active_emp()")
        self.cursor.execute("SELECT * FROM TDD.LIVE")
        result = self.cursor.fetchall()
        self.assertIsNotNone(result, "There is no data in LIVE table")
        self.cursor.execute("SELECT * FROM TDD.HISTORY")
        result = self.cursor.fetchall()
        self.assertIsNotNone(result, "There is no data in HISTORY table")

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
