nama = str(input("Nama: "))
NIM = int(input("NIM: "))
jkel = str(input("Jenis Kelamin: "))
tin = input("Tanggal Input Nilai: ")
matkul = input("Mata Kuliah: ")
absensi = input("Absensi: ")
tugas = float(input("nilai tugas: "))
uts = float(input("nilai UTS: "))
uas = float(input("nilai UAS: "))
na = (tugas*0.3) + (uts*0.35) + (uas*0.35)

print ("Nama: ", nama)
print("NIM", NIM)
print("Jenis Kelamin: ", jkel)
print("Tanggal input Nilai: ", tin)
print("Nama Mata Kuliah: ", matkul)
print("Absensi: ", absensi)
print("Nilai Tugas: ", tugas)
print("Nilai UTS: ",uts)
print("Nilai UAS: ", uas)
print("Nilai Akhir: ", na)

if na >= 0 and na < 50:
    print ("Grade E")
elif na >= 50 and na < 59:
    print ("Grade D")
elif na >= 60 and na < 64:
    print ("Grade C")
elif na >= 64 and na < 68:
    print ("Grade C+")
elif na >= 68 and na < 71:
    print ("Grade B-")
elif na >= 71 and na < 74:
    print ("Grade B")
elif na >= 74 and na < 77:
    print ("Grade B+")
elif na >= 77 and na < 80:
    print ("Grade A-")
elif na >= 80 and na < 100:
    print ("Grade A")

if na >= 71:
    print ("Keterangan Nilai: Lulus")
else:
    print ("Keterangan Nilai: Tidak Lulus")
