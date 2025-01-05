import Runners
import unittest

class TournamentTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        all_results = {}
        print("НАЧАЛО ТЕСТА")
        return all_results

    def setUp(self):
        self.human1 = Runners.Runner('Усэйн', speed = 10)
        self.human2 = Runners.Runner('Андрей', speed = 9)
        self.human3 = Runners.Runner('Ник', speed=3)
        self.participants = (self.human1, self.human2, self.human3)
        self.T = Runners.Tournament(self, (self.human1, self.human3), 90)
        self.all_results = self.T.start
        self.assertTrue((list(self.T.start().values())[-1]), self.human3.name, 'НЕ совпадает')
        print(f'all_results = {self.all_results}')

    @classmethod
    def tearDownClass(cls):
        print (f'all_results = {None}')


if __name__ == '__main__':
    unittest.main()
