import unittest
import test_12_3

test_subjectsTS = unittest.TestSuite()
test_subjectsTS.addTest(unittest.TestLoader().loadTestsFromTestCase(test_12_3.RunnerTest))
test_subjectsTS.addTest(unittest.TestLoader().loadTestsFromTestCase(test_12_3.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(test_subjectsTS)
