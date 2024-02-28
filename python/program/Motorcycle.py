from Vehicle import Vehicle

class Motorcycle(Vehicle):
    def __init__(self, plat, merk, tahun, warna, jenis_motor, tangki):
        super().__init__(plat, merk, tahun, warna)
        self.__jenis_motor = jenis_motor
        self.__tangki = tangki

    def get_jenis_motor(self):
        return self.__jenis_motor

    def set_jenis_motor(self, jenis_motor):
        self.__jenis_motor = jenis_motor

    def get_tangki(self):
        return self.__tangki

    def set_tangki(self, tangki):
        self.__tangki = tangki
