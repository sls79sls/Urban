import Runer
import unittest

class RunerTest(unittest.TestCase):
    def test_walk(self):
        human = Runer.Runner('LSS')
        for i in range(10):
            human.walk()
        self.assertEqual(human.distance,50, 'Walk : Ошибка')

    def test_run(self):
        human = Runer.Runner('SLS')
        for i in range(10):
            human.run()
        self.assertEqual(human.distance, 100, 'Run : Ошибка')

    def test_challenge(self):
        human1 = Runer.Runner('Fed')
        human2 = Runer.Runner('Ded')
        for i in range(10):
            human1.run()
            human2.walk()
        self.assertNotEqual(human1.distance, human2.distance, 'Run&Walk NotEqual : Ошибка')

if __name__ == '__main__':
    unittest.main()
