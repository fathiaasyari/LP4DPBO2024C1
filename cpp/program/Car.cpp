

#include <bits/stdc++.h>
#include "Vehicle.h"

using namespace std;

class Car : public Vehicle
{
private:
    int j_kursi;
    int j_pintu;

public:
    Car()
    {

    }

    Car(string plat, string merk, int tahun, string warna, int j_kursi, int j_pintu)
        : Vehicle(plat, merk, tahun, warna), j_kursi(j_kursi), j_pintu(j_pintu)
    {

    }

    void setJumlahKursi(int j_kursi)
    {
        this->j_kursi = j_kursi;
    }

    int getJumlahKursi() const
    {
        return j_kursi;
    }

    void setJumlahPintu(int j_pintu)
    {
        this->j_pintu = j_pintu;
    }

    int getJumlahPintu() const
    {
        return j_pintu;
    }

    ~Car()
    {

    }
};
