# CobaPy program cek ganjil genap
# video panduan di https://youtu.be/mIKqOA-dCPc
while True:
	print("Tekan tombol x jika ingin keluar")
	angka = input("Masukan angka yang ingin anda periksa: ")

	if angka == "x":
		exit()
	sisa = int(angka)%2
	if sisa == 0:
		print("Bilangan yang anda masukan adalah bilangan Genap\n")
	else :
		print ("Bilangan yang anda masukan adalah bilangan Ganjil\n")
