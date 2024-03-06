

#include <bits/stdc++.h>
#include "Vehicle.h"

using namespace std;

class ParkingLot {
private:
    string nama;
    int luas;
    vector<Vehicle*> list_kendaraan;

public:
    ParkingLot(string nama, int luas, vector<Vehicle*> listKendaraan) 
    : nama(nama), luas(luas), list_kendaraan(listKendaraan) {
        
    }

    ParkingLot() {

    }

    ParkingLot(string nama, int luas) : nama(nama), luas(luas) {

    }

    void tambahKendaraan(Vehicle* kendaraan) {
        list_kendaraan.push_back(kendaraan);
    }

    string getNama() const {
        return nama;
    }

    int getLuas() const {
        return luas;
    }

    const vector<Vehicle*>& getListKendaraan() const {
        return list_kendaraan;
    }

    ~ParkingLot() {
        for (auto kendaraan : list_kendaraan) {
            delete kendaraan;
        }
    }
};
