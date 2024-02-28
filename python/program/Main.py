from Vehicle import Vehicle
from Car import Car
from Motorcycle import Motorcycle
from Garage import Garage
from Parking import Parking

mobil1 = Car("D1823AD","Mazda", 2019, "Hitam", 5, 2)
mobil2 = Car("B18923L","BMW", 2023, "Putih", 2, 2)
mobil3 = Car("E9123E","Brio", 2014, "Hitam", 4, 2)
mobil4 = Car("BN9012L","Rush", 2020, "Putih", 7, 2)
mobil5 = Car("AD2193","Mercy", 2022, "Merah", 2, 2)


motor1 = Motorcycle("BN9012", "Honda", 2020, "Pink", "Vespa", 1800)
motor2 = Motorcycle("AL9121", "Harley", 2018, "Hitam", "Sport", 5000)
motor3 = Motorcycle("D3718LA", "Yamaha", 2013, "Merah", "Bebek", 1200)
motor4 = Motorcycle("R 1", "Harley", 2022, "Hitam", "Sport", 10000)


Parking = Parking(100, 5)
Parking.add_list_kendaraan(mobil1)
Parking.add_list_kendaraan(mobil2)
Parking.add_list_kendaraan(mobil3)
Parking.add_list_kendaraan(motor1)
Parking.add_list_kendaraan(motor2)


Garage = Garage("Rumah Thia", 400)
Garage.add_daftar(mobil4)
Garage.add_daftar(mobil5)
Garage.add_daftar(motor3)
Garage.add_daftar(motor4)


print ("------------------------------------------------------------------------------------------------------------------------------------------------------------------")
print ("                                                                          PARKING AREA                                                                            ")
print ("------------------------------------------------------------------------------------------------------------------------------------------------------------------")
print ("Area Parkir")
print("Kapasitas        : ", Parking.get_kapasitas())
print("Jumlah Kendaraan : ", Parking.get_jumlah_kendaraan())
print("Berikut dibawah ini merupakan daftar kendaraan")
print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
 # Membuat list untuk menyimpan data kendaraan
vehicle_data = []

# Mengisi list dengan data kendaraan
for i, vehicle in enumerate(Parking.get_list_kendaraan(), start=1):
    if isinstance(vehicle, Car): # jika mobil
        vehicle_data.append([
            f"{i}.",
            "Mobil",
            vehicle.get_plat(),
            vehicle.get_merk(),
            vehicle.get_tahun(),
            vehicle.get_warna(),
            vehicle.get_j_kursi(),
            vehicle.get_j_pintu(),
            "-",  # Menyisipkan "-" untuk kapasitas tangki pada mobil
            "-",
        ])
    elif isinstance(vehicle, Motorcycle): # jika motor
        vehicle_data.append([
            f"{i}.",
            "Motor",
            vehicle.get_plat(),
            vehicle.get_merk(),
            vehicle.get_tahun(),
            vehicle.get_warna(),
            "-",  # Menyisipkan "-" untuk jumlah kursi pada motor
            "-",  # Menyisipkan "-" untuk jumlah pintu pada motor
            vehicle.get_jenis_motor(),
            vehicle.get_tangki(),
        ])

# Fungsi untuk mencetak tabel dari data kendaraan
def print_table(data):
    # Mencetak header tabel
    print("{:<15} {:<10} {:<15} {:<15} {:<20} {:<15} {:<15} {:<15} {:<15} {:<15}".format(
        "Kendaraan", "Tipe", "Plat Nomor", "Merk", "Tahun Produksi", "Warna", "Jumlah Kursi", "Jumlah Pintu", "Jenis","Kapasitas Tangki "))
    # Mencetak baris untuk setiap kendaraan
    for row in data:
        print("{:<15} {:<10} {:<15} {:<15} {:<20} {:<15} {:<15} {:<15} {:<15} {:<15}".format(*row))

# Memanggil fungsi untuk mencetak tabel
print_table(vehicle_data)

print ("\n")


print ("------------------------------------------------------------------------------------------------------------------------------------------------------------------")
print ("                                                                          GARAGE                                                                                  ")
print ("------------------------------------------------------------------------------------------------------------------------------------------------------------------")
print("Nama Garage      : ", Garage.get_nama_garage())
print("Luas Garage      : ", Garage.get_luas_garage())
print("Berikut dibawah ini merupakan daftar kendaraan")
print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

vehicle_data = []
# Mengisi list dengan data kendaraan
for i, vehicle in enumerate(Garage.get_daftar(), start=1):
    if isinstance(vehicle, Car): # jika mobil
        vehicle_data.append([
            f"{i}.",
            "Mobil",
            vehicle.get_plat(),
            vehicle.get_merk(),
            vehicle.get_tahun(),
            vehicle.get_warna(),
            vehicle.get_j_kursi(),
            vehicle.get_j_pintu(),
            "-",  # Menyisipkan "-" untuk kapasitas tangki pada mobil
            "-",
        ])
    elif isinstance(vehicle, Motorcycle): # jika motor
        vehicle_data.append([
            f"{i}.",
            "Motor",
            vehicle.get_plat(),
            vehicle.get_merk(),
            vehicle.get_tahun(),
            vehicle.get_warna(),
            "-",  # Menyisipkan "-" untuk jumlah kursi pada motor
            "-",  # Menyisipkan "-" untuk jumlah pintu pada motor
            vehicle.get_jenis_motor(),
            vehicle.get_tangki(),
        ])

# Fungsi untuk mencetak tabel dari data kendaraan
def print_table(data):
    # Mencetak header tabel
    print("{:<15} {:<10} {:<15} {:<15} {:<20} {:<15} {:<15} {:<15} {:<15} {:<15}".format(
        "No", "Tipe", "Plat Nomor", "Merk", "Tahun Produksi", "Warna", "Jumlah Kursi", "Jumlah Pintu", "Jenis","Kapasitas Tangki "))
    # Mencetak baris untuk setiap kendaraan
    for row in data:
        print("{:<15} {:<10} {:<15} {:<15} {:<20} {:<15} {:<15} {:<15} {:<15} {:<15}".format(*row))

print_table(vehicle_data)
