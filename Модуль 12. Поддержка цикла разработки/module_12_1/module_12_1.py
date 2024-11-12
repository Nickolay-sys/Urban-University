from runner import Runner
import unittest


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        test_subject_1 = Runner("Nickolay")
        for i in range(10):
            test_subject_1.walk()
        self.assertEqual(test_subject_1.distance, 50)
        
    def test_run(self):
        test_subject_2 = Runner("Alexandr")
        for i in range(10):
            test_subject_2.run()
        self.assertEqual(test_subject_2.distance, 100)
        
    def test_challenge(self):
        test_subject_1 = Runner("Nickolay")
        test_subject_2 = Runner("Alexandr")
        for i in range(10):
            test_subject_1.walk()
            test_subject_2.run()
        self.assertNotEqual(test_subject_1.distance, test_subject_2.distance)
        
if __name__ == "__main__":
    unittest.main()
    
