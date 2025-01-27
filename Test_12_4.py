import Module_12_4
import unittest
import logging

class RunerTest(unittest.TestCase):

    def test_walk(self):
        logging.info ('Это сообщение активирует ваш логгер', exc_info = True) # ИНформация в лог-файл
        print(f"test_walk запущен в работу")
        try:
            human = Module_12_4.Runner('LSS',5)
            print(f"human = {human}")
            for i in range(10):
                human.walk()
            self.assertEqual(human.distance,50, 'Walk : Ошибка')
            logging.info(f'"test_walk" выполнен успешно', exc_info = True) # ИНформация в лог-файл
        except ValueError as err:
            logging.warning("Неверная скорость для Runner", exc_info = True) # ИНформация в лог-файл

    def test_run(self):
        human = Module_12_4.Runner('SLS')
        for i in range(10):
            human.run()
        self.assertEqual(human.distance, 100, 'Run : Ошибка')

    def test_challenge(self):
        human1 = Module_12_4.Runner('Fed')
        human2 = Module_12_4.Runner('Ded')
        for i in range(10):
            human1.run()
            human2.walk()
        self.assertNotEqual(human1.distance, human2.distance, 'Run&Walk NotEqual : Ошибка')

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_tests.log', encoding='utf-8',
                        format="%(asctime)s | %(levelname)s | %(message)s") # Конфигурация записи в лог файл.
    logging.info(f'Конфигурация лог файла задана успешно', exc_info = True) # ИНформация в лог-файл
    unittest.main()
