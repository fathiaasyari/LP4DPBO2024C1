

#include <bits/stdc++.h>
#include "Vehicle.h"

using namespace std;

class Motorcycle : public Vehicle
{
private:
    string jenis_motor;
    int kapasitas_tangki;

public:
    Motorcycle()
    {

    }

    Motorcycle(string plat, string merk, int tahun, string warna, string jenis_motor, int kapasitas_tangki)
        : Vehicle(plat, merk, tahun, warna), jenis_motor(jenis_motor), kapasitas_tangki(kapasitas_tangki)
    {

    }

    void setJenisMotor(string jenis_motor)
    {
        this->jenis_motor = jenis_motor;
    }

    string getJenisMotor() const
    {
        return jenis_motor;
    }

    void setKapasitasTangki(int kapasitas_tangki)
    {
        this->kapasitas_tangki = kapasitas_tangki;
    }

    int getKapasitasTangki() const
    {
        return kapasitas_tangki;
    }

    ~Motorcycle()
    {

    }
};
