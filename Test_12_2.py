import Runners
import unittest

class TournamentTest(unittest.TestCase):
    print("Start")
    @classmethod
    def setUpClass(cls):
        all_results = {}
        print("НАЧАЛО ТЕСТА")
        return all_results

    def setUp(self):
        super(TournamentTest,self).setUp()
        print("НАЧАЛО ОЧЕРЕДНОГО ЗАБЕГА")

        self.human1 = Runners.Runner('Усэйн', speed = 10)
        self.human2 = Runners.Runner('Андрей', speed = 9)
        self.human3 = Runners.Runner('Ник', speed=3)
        #self.participants = (self.human1, self.human2, self.human3)

    print("Тест-1")
    def test_Tour0(self):
        self.T0 = Runners.Tournament(self, (self.human1, self.human3), 90)
        result = self.T0.start()
        print(f'result 1-stfunction = {result}')
        #self.assertTrue((list(result.values())[-1]), self.human3.name, 'НЕ совпадает')
        print(f'all_results = {result}')

    print("Тест-2")
    def Tour1(self):
        self.T1 = Runners.Tournament(self, (self.human2, self.human3), 90)
        self.assertTrue((list(self.T1.start().values())[-1]), self.human3.name, 'НЕ совпадает')
        print(f'all_results = {self.all_results}')

    print("Тест-3")
    def Tour2(self):
        self.T2 = Runners.Tournament(self, (self.human1, self.human2, self.human3), 90)
        self.assertTrue(list(self.T2.start().values())[-1], 'НЕ совпадает')
        print(f'all_results = {self.all_results}')

    @classmethod
    def tearDownClass(cls):

        print (f'#all_results = {None}')


if __name__ == '__main__':
    unittest.main()
