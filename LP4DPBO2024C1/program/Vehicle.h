#ifndef VEHICLE_H
#define VEHICLE_H

#include <string>
#include <iostream>
using namespace std;

class Vehicle {
private:
    string plat;
    string merk;
    int tahun;
    string warna;

public:
    Vehicle();
    Vehicle(string plat, string merk, int tahun, string warna);
    virtual ~Vehicle() {}

    void setPlat(string plat);
    string getPlat() const;

    void setMerk(string merk);
    string getMerk() const;

    void setTahun(int tahun);
    int getTahun() const;

    void setWarna(string warna);
    string getWarna() const;
};

#endif