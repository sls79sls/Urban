import Runners
import unittest

class TournamentTest(unittest.TestCase):
    is_frozen = True
    print("Start")
    @classmethod
    def setUpClass(cls):
        cls.all_results =[]
        print("НАЧАЛО ТЕСТА")
        return cls.all_results

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def setUp(self):
        super(TournamentTest,self).setUp()
        print("НАЧАЛО ОЧЕРЕДНОГО ЗАБЕГА")

        self.human1 = Runners.Runner('Усэйн', speed = 10)
        self.human2 = Runners.Runner('Андрей', speed = 9)
        self.human3 = Runners.Runner('Ник', speed=3)
        #self.participants = (self.human1, self.human2, self.human3)

    print("Тест-1")

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_Tour0(self):
        T0 = Runners.Tournament(90, self.human1, self.human3)
        s=T0.start()
        print(f' s = {s}')
        print(f'Тест-1 : Begin - T0-all_results = {self.all_results}')
        self.all_results.append(s)
        print(f'Тест-1 : Middle - T0-all_results = {self.all_results}')
        #print(f'self.all_results[0][min(s))] = {self.all_results[0][min(s)]}')
        self.assertTrue(self.all_results[0][max(s)] == 'Ник')
        print(f'Тест-1 : Last - T0-all_results = {self.all_results}')

    print("Тест-2")

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_Tour1(self):
        T1 = Runners.Tournament(90, self.human2, self.human3)
        s = T1.start()
        print(f' s = {s}')
        print(f'Тест-2 : Begin - T1-all_results = {self.all_results}')
        self.all_results.append(s)
        print(f'Тест-2 : Middle - T1-all_results = {self.all_results}')
        self.assertTrue(self.all_results[1][max(s)] == 'Ник')
        print(f'Тест-2 : Last - T1-all_results = {self.all_results}')

    print("Тест-3")

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_Tour2(self):
        T2 = Runners.Tournament(90, self.human1, self.human2, self.human3)
        s = T2.start()
        print(f' s = {s}')
        print(f'Тест-3 : Begin - T2-all_results = {self.all_results}')
        self.all_results.append(s)
        print(f'Тест-3 : Middle - T2-all_results = {self.all_results}')
        #self.assertTrue(self.all_results[2][max(s)] == 'Ник')
        print(f'Тест-3 : Last - T2-all_results = {self.all_results}')

    @classmethod
    def tearDownClass(cls):
        for i in cls.all_results:
            print('{',end="")
            for j in i.keys():
                print ( j , ' : ', i[j], end="")
            print ('}\n')

if __name__ == '__main__':
    unittest.main()
