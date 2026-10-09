import time

jumlah_data = int(input("Masukkan jumlah total data : "))

data_mahasiswa = [
  
]

for i in range (jumlah_data) :
    print(f"Data mahasiswa ke - {i+1}")
    nama = input("Masukkan Nama mahasiswa : ")
    nim = input("Masukkan NIM mahasiswa : ")
    data_mahasiswa.append({"nama":nama, "nim":nim})
    print("\n")

target_nim = input("Masukkan NIM target : ")

def linear_search(data, target):
    for mhs in data:
        if mhs["nim"] == target:
            return mhs["nama"]
    return None

def binary_search(data, target):
    low, high = 0, len(data) - 1
    
    while low <= high:
        mid = (low + high) // 2
        if data[mid]["nim"] == target:
            return data[mid]["nama"]
        elif data[mid]["nim"] < target:
            low = mid + 1
        else:
            high = mid - 1
            
    return None

start = time.perf_counter()
hasil_linear = linear_search(data_mahasiswa, target_nim)
waktu_linear = (time.perf_counter() - start) * 1000

def ambil_nim(x):
    return x["nim"]

data_terurut = sorted(data_mahasiswa, key=ambil_nim)

start = time.perf_counter()
hasil_binary = binary_search(data_terurut, target_nim)
waktu_binary = (time.perf_counter() - start) * 1000

print(f"NIM yang dicari: {target_nim}")
print(f"[Linear Search] Nama: {hasil_linear} | Waktu: {waktu_linear:.6f} ms")
print(f"[Binary Search] Nama: {hasil_binary} | Waktu: {waktu_binary:.6f} ms")