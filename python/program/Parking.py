from Vehicle import Vehicle
from Car import Car
from Motorcycle import Motorcycle

class Parking: 
    __kapasitas = 0
    __jumlah_kendaraan = 0
    __list_kendaraan = [] 
    

    def __init__(self, kapasitas = 0, jumlah_kendaraan = 0):
        self.__kapasitas = kapasitas
        self.__jumlah_kendaraan = jumlah_kendaraan
        self.__list_kendaraan = []

    def set_kapasitas(self, kapasitas):
        self.__kapasitas = kapasitas

    def get_kapasitas(self):
        return self.__kapasitas
    
    def set_jumlah_kendaraan(self, jumlah_kendaraan):
        self.__jumlah_kendaraan = jumlah_kendaraan

    def get_jumlah_kendaraan(self):
        return self.__jumlah_kendaraan
    
    def add_list_kendaraan(self, daftar_kendaraan : Vehicle):
        self.__list_kendaraan.append(daftar_kendaraan)

    def get_list_kendaraan(self):
        return self.__list_kendaraan
    