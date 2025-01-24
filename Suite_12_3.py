import unittest
import RunnerTest
import test_12_2

RunnerTST = unittest.TestSuite()
RunnerTST.addTest(unittest.TestLoader().loadTestsFromTestCase(RunnerTest.RunerTest))
RunnerTST.addTest(unittest.TestLoader().loadTestsFromTestCase(test_12_2.TournamentTest))

Go = unittest.TextTestRunner(verbosity=2)
Go.run(RunnerTST)
