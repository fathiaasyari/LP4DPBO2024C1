class Vehicle:
    def __init__(self, plat, merk, tahun, warna):
        self.__plat = plat
        self.__merk = merk
        self.__tahun = tahun
        self.__warna = warna

    def get_plat(self):
        return self.__plat

    def set_plat(self, plat):
        self.__plat = plat

    def get_merk(self):
        return self.__merk

    def set_merk(self, merk):
        self.__merk = merk

    def get_tahun(self):
        return self.__tahun

    def set_tahun(self, tahun):
        self.__tahun = tahun

    def get_warna(self):
        return self.__warna

    def set_warna(self, warna):
        self.__warna = warna
