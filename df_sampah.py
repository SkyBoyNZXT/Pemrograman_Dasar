import pandas as pd

# Untuk soal no 1
data_sampah = r"C:\my coding\python\disperkim-od_16985_jumlah_produksi_sampah_berdasarkan_kabupatenkota_v3_metadata.xlsx"
df_sampah = pd.read_excel(data_sampah)
pd.set_option('display.max_rows', None)
filter = df_sampah.loc[:, ["nama_provinsi", "nama_kabupaten_kota", "jumlah_produksi_sampah", "satuan", "tahun"]]
print(filter)

# Untuk soal no 2
tahun_tertentu = 2015
total_produksi = 0
for index, row in filter.iterrows():
    if row['tahun'] == tahun_tertentu:
        total_produksi += row["jumlah_produksi_sampah"]
print(f"\nTotal produksi sampah di seluruh kabupaten/kota di jawa barat")
print(f"Tahun {tahun_tertentu} : {total_produksi:.2f} ton")

# Untuk soal no 3
jumlah_produksi_pertahun = {}
for index, row in filter.iterrows():
    tahun = row["tahun"]
    if tahun not in jumlah_produksi_pertahun:
        jumlah_produksi_pertahun[tahun] = 0
    jumlah_produksi_pertahun[tahun] += row["jumlah_produksi_sampah"]
print("\nTotal produksi sampah per tahun di seluruh kabupaten/kota di jawa barat:")
for tahun in sorted(jumlah_produksi_pertahun.keys()):
    print(f"Tahun {tahun} : {jumlah_produksi_pertahun[tahun]:.2f} ton")

# Untuk soal no 4
jumlah_perkabupaten_kota = {}
for index, row in filter.iterrows():
    kabupaten_kota = row["nama_kabupaten_kota"]
    jumlah_produksi = row["jumlah_produksi_sampah"]
    if kabupaten_kota not in jumlah_perkabupaten_kota:
        jumlah_perkabupaten_kota[kabupaten_kota] = 0
    jumlah_perkabupaten_kota[kabupaten_kota] += jumlah_produksi
print("\nTotal produksi sampah per kabupaten/kota di jawa barat:")
for kabupaten_kota, total in sorted(jumlah_perkabupaten_kota.items()):
    print(f"{kabupaten_kota} : {total:.2f} ton")

# Untuk export menjadi csv dan excel
filter.to_csv('data sampah jabar.csv', index=False)
filter.to_excel('data sampah jabar.xlsx', index=False)