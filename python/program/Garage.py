from Vehicle import Vehicle
from Car import Car
from Motorcycle import Motorcycle

class Garage: 
    __nama_garage = ""
    __luas_garage = 0
    __daftar = [] 

    def __init__(self, nama_garage = "", luas_garage = 0):
        self.__nama_garage = nama_garage
        self.__luas_garage = luas_garage
        self.__daftar = []
    
    def set_nama_garage(self, nama_garage):
        self.__nama_garage = nama_garage

    def get_nama_garage(self):
        return self.__nama_garage
    
    def set_luas_garage(self, luas_garage):
        self.__luas_garage = luas_garage

    def get_luas_garage(self):
        return self.__luas_garage
    
    def add_daftar(self, daftar_kendaraan : Vehicle):
        self.__daftar.append(daftar_kendaraan)

    def get_daftar(self):
        return self.__daftar