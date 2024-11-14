import unittest
from runner_and_tournament import Runner, Tournament

class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}
        
    def setUp(self):
        self.runner_1 = Runner("Усэйн", 10)
        self.runner_2 = Runner("Андрей", 9)
        self.runner_3 = Runner("Ник", 3)
    
    @classmethod    
    def tearDownClass(cls):
        for test_key, test_value in cls.all_results.items():
            print(test_key)
            for key, value in test_value.items():
                print(f'\t{key}:{value}')
    
    def test_turn1(self):
        turn_1 = Tournament(90, self.runner_1, self.runner_3)
        result = turn_1.start()
        self.assertTrue(result[list(result.keys())[-1]] == 'Ник')
        self.all_results['Первый забег'] = result
        
    def test_turn2(self):
        turn_2 = Tournament(90, self.runner_1, self.runner_2)
        result = turn_2.start()
        self.assertTrue(result[list(result.keys())[-1]])
        self.all_results['Второй забег'] = result
        
    def test_turn3(self):
        turn_3 = Tournament(90, self.runner_1, self.runner_2, self.runner_3)
        result = turn_3.start()
        self.assertTrue(result[list(result.keys())[-1]] == 'Ник')
        self.all_results['Третий забег'] = result
    
        
        
        
        
if __name__ == "__main__":
    unittest.main()