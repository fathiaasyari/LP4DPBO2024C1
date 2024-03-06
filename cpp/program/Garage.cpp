
#include <bits/stdc++.h>
#include "Vehicle.h"

using namespace std;

class Garage {
private:
    int kapasitas;
    int jumlah_kendaraan;
    vector<Vehicle*> daftar_kendaraan;

public:
    Garage(int kapasitas, vector<Vehicle*> daftarKendaraan)
    : kapasitas(kapasitas), daftar_kendaraan(daftarKendaraan) {
        jumlah_kendaraan = daftar_kendaraan.size();
    }

    void tambahKendaraan(Vehicle* kendaraan) {
        if (jumlah_kendaraan < kapasitas) {
            daftar_kendaraan.push_back(kendaraan);
            jumlah_kendaraan++;
        } else {
            cout << "Garasi penuh, tidak bisa menambahkan kendaraan lagi." << endl;
        }
    }

    int getKapasitas() const {
        return kapasitas;
    }

    int getJumlahKendaraan() const {
        return jumlah_kendaraan;
    }

    const vector<Vehicle*>& getDaftarKendaraan() const {
        return daftar_kendaraan;
    }

    ~Garage() {
        for (auto kendaraan : daftar_kendaraan) {
            delete kendaraan;
        }
    }
};
