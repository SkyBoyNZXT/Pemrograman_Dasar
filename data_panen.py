data_panen = {
    'lokasi1': {
        'nama_lokasi': 'Kebun A',
        'hasil_panen': {
            'padi': 1200,
            'jagung': 800,
            'kedelai': 500
        }
    },
    'lokasi2': {
        'nama_lokasi': 'Kebun B',
        'hasil_panen': {
            'padi': 1500,
            'jagung': 900,
            'kedelai': 450
        }
    },
    'lokasi3': {
        'nama_lokasi': 'Kebun C',
        'hasil_panen': {
            'padi': 1300,
            'jagung': 750,
            'kedelai': 600
        }
    },
    'lokasi4': {
        'nama_lokasi': 'Kebun D',
        'hasil_panen': {
            'padi': 1300,
            'jagung': 850,
            'kedelai': 550
        }
    },
    'lokasi5': {
        'nama_lokasi': 'Kebun E',
        'hasil_panen': {
            'padi': 1400,
            'jagung': 950,
            'kedelai': 480
        }
    }
}

print("Seluruh Data Panen :")
for lokasi, data in data_panen.items():
    print(f"Nama Lokasi : {data['nama_lokasi']}")
    for tanaman, jumlah in data['hasil_panen'].items():
        print(f"  {tanaman} : {jumlah} kg")
    print()

jumlah_jagung_lokasi2 = data_panen['lokasi2']['hasil_panen']['jagung']
print(f"Jumlah hasil panen jagung di lokasi2 : {jumlah_jagung_lokasi2} kg\n")

nama_lokasi3 = data_panen['lokasi3']['nama_lokasi']
print(f"Nama lokasi dari lokasi3 : {nama_lokasi3}\n")

hasil_panen_padi = {lokasi: data['hasil_panen']['padi'] for lokasi, data in data_panen.items()}
hasil_panen_kedelai = {lokasi: data['hasil_panen']['kedelai'] for lokasi, data in data_panen.items()}
print("Jumlah hasil panen padi setiap lokasi :", hasil_panen_padi)
print("Jumlah hasil panen kedelai setiap lokasi :", hasil_panen_kedelai, "\n")

padi_total = sum(hasil_panen_padi.values())
kedelai_total = sum(hasil_panen_kedelai.values())
print(f"Total hasil panen padi : {padi_total} kg")
print(f"Total hasil panen kedelai : {kedelai_total} kg\n")

print("Evaluasi Lokasi :")
for lokasi, data in data_panen.items():
    nama_lokasi = data['nama_lokasi']
    padi = data['hasil_panen']['padi']
    jagung = data['hasil_panen']['jagung']
    if padi > 1300 or jagung > 800:
        print(f"{nama_lokasi} : Memerlukan perhatian khusus (Padi : {padi}, Jagung : {jagung})")
    else:
        print(f"{nama_lokasi} : Kondisi baik (Padi : {padi}, Jagung : {jagung})")
