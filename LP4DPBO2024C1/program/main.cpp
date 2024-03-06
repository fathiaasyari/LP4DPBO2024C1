#include <bits/stdc++.h>
#include "Motorcycle.cpp"
#include "Vehicle.h"
#include "Car.cpp"
#include "Garage.cpp"
#include "ParkingLot.cpp"

using namespace std;

int main() {
    Car car1("SA21CS", "Honda", 2021, "Hitam", 7, 4);
    Car car2("AB12CD", "Toyota", 2019, "Silver", 5, 4);
    Car car3("XY34ZA", "Mitsubishi", 2018, "Red", 5, 4);

    Motorcycle motor1("DJ23DD", "Yamaha", 2004, "Pink","Vespa", 1000);
    Motorcycle motor2("KJ45LK", "Suzuki", 2007, "Blue", "Scrambler", 800);
    Motorcycle motor3("OP67PO", "Honda", 2015, "Yellow", "Sport", 1200);

    vector<Vehicle*> list_kendaraan {&car1, &car2, &motor1, &motor2};
    vector<Vehicle*> daftar_kendaraan {&car3, &motor3};

    ParkingLot parkinglot1("Basement", 1000, list_kendaraan);
    Garage garage1(5, daftar_kendaraan);

    cout << "Parking Lot:" << endl;
    cout << "Nama: " << parkinglot1.getNama() << endl;
    cout << "Luas: " << parkinglot1.getLuas() << " m" << endl;
    cout << "Daftar Kendaraan:" << endl;
    for (auto kendaraan : parkinglot1.getListKendaraan()) {
        cout << "- Plat Nomor: " << kendaraan->getPlat() << endl;
        cout << "  Merk: " << kendaraan->getMerk() << endl;
        cout << "  Tahun Produksi: " << kendaraan->getTahun() << endl;
        cout << "  Warna: " << kendaraan->getWarna() << endl;
        if (dynamic_cast<Car*>(kendaraan)) {
            cout << "  Jumlah Kursi: " << dynamic_cast<Car*>(kendaraan)->getJumlahKursi() << endl;
            cout << "  Jumlah Pintu: " << dynamic_cast<Car*>(kendaraan)->getJumlahPintu() << endl;
        } else if (dynamic_cast<Motorcycle*>(kendaraan)) {
            cout << "  Jenis Motor: " << dynamic_cast<Motorcycle*>(kendaraan)->getJenisMotor() << endl;
            cout << "  Kapasitas Tangki: " << dynamic_cast<Motorcycle*>(kendaraan)->getKapasitasTangki() << endl;
        }
        cout << endl;
    }

    cout << "Garage:" << endl;
    cout << "Kapasitas: " << garage1.getKapasitas() << endl;
    cout << "Jumlah Kendaraan: " << garage1.getJumlahKendaraan() << endl;
    cout << "Daftar Kendaraan:" << endl;
    for (auto kendaraan : garage1.getDaftarKendaraan()) {
        cout << "- Plat Nomor: " << kendaraan->getPlat() << endl;
        cout << "  Merk: " << kendaraan->getMerk() << endl;
        cout << "  Tahun Produksi: " << kendaraan->getTahun() << endl;
        cout << "  Warna: " << kendaraan->getWarna() << endl;
        if (dynamic_cast<Car*>(kendaraan)) {
            cout << "  Jumlah Kursi: " << dynamic_cast<Car*>(kendaraan)->getJumlahKursi() << endl;
            cout << "  Jumlah Pintu: " << dynamic_cast<Car*>(kendaraan)->getJumlahPintu() << endl;
        } else if (dynamic_cast<Motorcycle*>(kendaraan)) {
            cout << "  Jenis Motor: " << dynamic_cast<Motorcycle*>(kendaraan)->getJenisMotor() << endl;
            cout << "  Kapasitas Tangki: " << dynamic_cast<Motorcycle*>(kendaraan)->getKapasitasTangki() << endl;
        }
        cout << endl;
    }

    return 0;
}
