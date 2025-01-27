import unittest
from runner_and_tournament import Runner, Tournament

class TournamentTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner_1 = Runner(name="Усэйн", speed=10)
        self.runner_2 = Runner(name="Андрей", speed=9)
        self.runner_3 = Runner(name="Ник", speed=3)

    @classmethod
    def tearDownClass(cls):
        for test_name, result in cls.all_results.items():
            named_result = {place: runner.name for place, runner in result.items()}
            print(named_result)

    def test_usain_vs_nick(self):
        tournament = Tournament(90, self.runner_1, self.runner_3)
        results = tournament.start()
        TournamentTest.all_results['usain_vs_nick'] = results
        self.assertTrue(results[max(results.keys())] == self.runner_3)

    def test_andrei_vs_nick(self):
        tournament = Tournament(90, self.runner_2, self.runner_3)
        results = tournament.start()
        TournamentTest.all_results['andrei_vs_nick'] = results
        self.assertTrue(results[max(results.keys())] == self.runner_3)

    def test_usain_andrei_nick(self):
        tournament = Tournament(90, self.runner_1, self.runner_2, self.runner_3)
        results = tournament.start()
        TournamentTest.all_results['usain_vs_andrei_vs_nick'] = results
        self.assertTrue(results[max(results.keys())] == self.runner_3)

if __name__ == "__main__":
    unittest.main()