import unittest
from stu import student

class test_emp(unittest.TestCase):
    def test_full_name(self):
        student1 = student('ashutosh', 'mishra', 150)
        student2 = student('abcd', 'xyz', 999)

        self.assertEqual(student1.email_id(), 'ashutosh.mishra@gmail.com')

        self.assertEqual(student1.full_name(), 'ashutosh mishra')
        self.assertEqual(student2.full_name(), 'abcd xyz')

        student1.name = 'ash'
        student2.name = 'jklmnop'

        self.assertEqual(student1.full_name(), 'ash mishra')
        self.assertEqual(student2.full_name(), 'jklmnop xyz')

if __name__ == "__main__":
    unittest.main()
