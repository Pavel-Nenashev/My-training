import unittest

from runner_and_tournament import Runner, Tournament

# Декоратор для проверки значения атрибута is_frozen
def skip_if_frozen(func):
    def wrapper(self, *args, **kwargs):
        if self.is_frozen:
            self.skipTest('Тесты в этом кейсе заморожены')
        else:
            return func(self, *args, **kwargs)
    return wrapper

class RunnerTest(unittest.TestCase):
    is_frozen = False

    @skip_if_frozen
    def test_walk(self):
        runner = Runner('Test Runner')
        for _ in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50)

    @skip_if_frozen
    def test_run(self):
        runner = Runner('Test Runner')
        for _ in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)

    @skip_if_frozen
    def test_challenge(self):
        runner1 = Runner('Runner 1')
        runner2 = Runner('Runner 2')
        for _ in range(10):
            runner1.run()
            runner2.walk()
        self.assertNotEqual(runner1.distance, runner2.distance)

class TournamentTest(unittest.TestCase):
    is_frozen = True  # Заморожено, тесты будут пропущены

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner_1 = Runner('Усэйн', 10)
        self.runner_2 = Runner('Андрей', 9)
        self.runner_3 = Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for test_name, result in cls.all_results.items():
            named_result = {place: runner.name for place, runner in result.items()}
            print(named_result)


    @skip_if_frozen
    def test_first_tournament(self):
        tournament = Tournament(90, self.runner_1, self.runner_3)
        results = tournament.start()
        TournamentTest.all_results['usain_vs_nick'] = results
        self.assertTrue(results[max(results.keys())] == self.runner_3)

    @skip_if_frozen
    def test_second_tournament(self):
        tournament = Tournament(90, self.runner_2, self.runner_3)
        results = tournament.start()
        TournamentTest.all_results['usain_vs_nick'] = results
        self.assertTrue(results[max(results.keys())] == self.runner_3)

    @skip_if_frozen
    def test_third_tournament(self):
        tournament = Tournament(90, self.runner_1, self.runner_2, self.runner_3)
        results = tournament.start()
        TournamentTest.all_results['usain_vs_nick'] = results
        self.assertTrue(results[max(results.keys())] == self.runner_3)



if __name__ == '__main__':
    unittest.main()