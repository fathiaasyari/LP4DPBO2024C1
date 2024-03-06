#include "Vehicle.h"

Vehicle::Vehicle() : plat(""), merk(""), tahun(0), warna("") {}

Vehicle::Vehicle(string plat, string merk, int tahun, string warna) 
    : plat(plat), merk(merk), tahun(tahun), warna(warna) {}

void Vehicle::setPlat(string plat) {
    this->plat = plat;
}

string Vehicle::getPlat() const {
    return plat;
}

void Vehicle::setMerk(string merk) {
    this->merk = merk;
}

string Vehicle::getMerk() const {
    return merk;
}

void Vehicle::setTahun(int tahun) {
    this->tahun = tahun;
}

int Vehicle::getTahun() const {
    return tahun;
}

void Vehicle::setWarna(string warna) {
    this->warna = warna;
}

string Vehicle::getWarna() const {
    return warna;
}
