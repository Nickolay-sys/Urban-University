import unittest
import logging
from rt_with_exceptions import Runner

class RunnerTest(unittest.TestCase):
    def test_walk(self):
        try:
            test_subject_1 = Runner("Nickolay", -5) 
            for i in range(10):
                test_subject_1.walk()
            self.assertEqual(test_subject_1.distance, 50)
            logging.info('"test_walk" выполнен успешно')
        except ValueError:
            logging.error("Неверная скорость для Runner", exc_info=True)
        
    def test_run(self):
        try:
            test_subject_2 = Runner(10)
            for i in range(10):
                test_subject_2.run()
            self.assertEqual(test_subject_2.distance, 100)
            logging.info('"test_run" выполнен успешно')
        except TypeError:
            logging.warning("Неверный тип данных для объекта Runner", exc_info=True)
        
        
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, filemode="w", filename="runner_tests.log",
                        encoding="utf-8", format="%(levelname)s | %(message)s")
    unittest.main()
        
    