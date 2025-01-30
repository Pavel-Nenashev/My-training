import unittest
from tests_12_3 import RunnerTest, TournamentTest

# Создаем объект TestSuite и добавляем к нему тесты из RunnerTest и TournamentTest
suite = unittest.TestSuite()
suite.addTest(unittest.TestLoader().loadTestsFromTestCase(RunnerTest))
suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TournamentTest))

# Создаем объект TextTestRunner с verbosity=2
runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite)