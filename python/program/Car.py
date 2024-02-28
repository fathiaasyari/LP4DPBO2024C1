from Vehicle import Vehicle

class Car(Vehicle):
    def __init__(self, plat, merk, tahun, warna, j_kursi, j_pintu):
        super().__init__(plat, merk, tahun, warna)
        self.__j_kursi = j_kursi
        self.__j_pintu = j_pintu

    def get_j_kursi(self):
        return self.__j_kursi

    def set_j_kursi(self, j_kursi):
        self.__j_kursi = j_kursi

    def get_j_pintu(self):
        return self.__j_pintu

    def set_j_pintu(self, j_pintu):
        self.__j_pintu = j_pintu
