class Product:
    def __init__(self, name : str, weight : float, category : str):
        self.name = name
        self.weight = weight
        self.category = category
    def __str__(self):
        return (f'Название: {self.name}, Вес: {self.weight}, Категория: {self.category}')


class Shop:
    __filename = 'products.txt'
    def get_products(self):
        file = open (self.__filename,"r")
        a = file.read()
        file.close()
        return a
    def add(self, *products):
        file =  open (self.__filename, 'r+')
        lines = file.readlines()
        flag = False
        try:
            for j in range(len(products)):
                for i in range(len(lines)):
                    if str(products[j].name) == str(lines[i].split(sep=None, maxsplit=-1)[1][0:-1]):
                        flag = True
                        break
                if flag:
                    print(f'Продукт {products[j]},  уже есть в магазине')
                    flag = False
                else:
                    file.write(f'{products[j]}\n')
        except IndexError:
            if lines == []:
                for k in range(len(products)):
                    file.write(f'{products[k]}\n')


if __name__ == '__main__':
    s1 = Shop()
    p1 = Product('Potato', 50.5, 'Vegetables')
    p2 = Product('Spaghetti', 3.4, 'Groceries')
    p3 = Product('Potato', 5.5, 'Vegetables')
    print(p2)  # __str__

    s1.add(p1, p2, p3)
    print(s1.get_products())

