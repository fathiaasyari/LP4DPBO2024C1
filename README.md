# Janji
Saya Syaila Fathia Azzahra dengan NIM 2206272 mengerjakan LP4DPBO2024C1 dalam Praktikum mata kuliah DPBO untuk keberkahan-Nya maka saya tidak melakukan kecurangan seperti yang telah dispesifikasikan. Aamin.


# Desain dan Alur Program
![Screenshot 2024-03-06 224239.png](https://github.com/fathiaasyari/LP4DPBO2024C1/blob/ad7442b99e069264754d6a998c04ab4b4ade66a8/Screenshot%202024-03-06%20224239.png)

## Penjelasan Desain

### 1. Vehicle:
Atributnya adalah:
- Plat nomor
- Merk
- Tahun produksi
- Warna
digunakan untuk membuat entitas dasar kendaraan dengan atribut yang umum bagi semua jenis kendaraan. 

### 2. Car:
Atribunya adalah:
- Jumlah kursi
- Jumlah pintu

Alasan penggunaan inheritance di sini karena mobil adalah jenis kendaraan yang memiliki atribut , seperti jumlah kursi dan pintu.

### 3. Motorcycle:
Atributnya adalah:
- Jenis motor
- Kapasitas tangki
Sama seperti Car, alasan penggunaan inheritance di sini adalah karena sepeda motor memiliki atribut tambahan yang lebih spesifik.

### 4. Garage: (composite)
Atributnya adalah:
- Nama garasi
- Luas garasi
- Daftar kendaraan (list)
Class Garage memiliki class Vehicle, karena garasi digunakan untuk menyimpan kendaraan.

### 5. ParkingLot: (composite)
Atributnya adalah:
- Kapasitas (maksimum jumlah kendaraan yang dapat ditampung)
- Jumlah kendaraan saat ini (yang sedang diparkir)
- Daftar kendaraan (list)

Class ParkingLot memiliki class Vehicle, karena garasi digunakan untuk memarkir kendaraan.

Alasan mengapa parkinglot dan garage tidak memiliki entitas dikarenakan asumsi saya di dunia nyata, parkinglot dan garage merupakan area yang berbeda
dan peruntukan yang berbeda pula.

## Alur Program
- Objek kendaraan diimplementasikan dalam hardcode yang terdapat di file main.cpp
- Terdapat 6 objek yakni 3 motor dan 3 mobil.
- List kendaraan yang terdapat di garasi yakni 1 mobil dan 1 motor.
- List kendaraan yang terdapat di area parkir yakni 2 mobil dan 2 motor.
- Data kendaraan ditampilkan dalam bentuk list(cpp) dan tabel (pyhton) sesuai dengan areanya (garasi/parkinglot)

# Screenshoot Program (Python)
### Cara run
g++ main.cpp Vehicle.cpp Car.cpp Motorcycle.cpp Garage.cpp ParkingLot.cpp -o test
![Screenshot 2024-02-28 232243.png](https://github.com/fathiaasyari/LP4DPBO2024C1/blob/75ac44b24f30567d046f88ba87b7f07c1a760a76/python/screenshoot/Screenshot%202024-02-28%20232243.png)


