#Memasukkan library socket
import socket

#Inisiasi objek socket
cln_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Permintaan koneksi ke server
cln_sock.connect(('127.0.0.1', 8080))

#Perulangan untuk menmabah data
while True:
        #Input data
        input_suhu = input("Masukkan Suhu: ")
        input_lembab = input("Masukkan tingkat kelembaban (Tinggi, Sedangm, Rendah): ")
        input_oksigen = input("Masukkan Tekanan Oksigen (Tinggi, Sedang, Rendah): ")

        #Split pada data input
        suhu = input_suhu.split(' ')
        lembab = input_lembab.split(' ')
        oksigen = input_oksigen.split(' ')

        #Perulangan dengan data sebanyak 3 jenis yaitu suhu, kelembaban, dan tekanan oksigen
        for i in range(0, 3):

            #Memasukkan data input kedalam list variabel data
            data = ['Suhu:'+suhu[0]+'derajat', 'Kelembaban:' + lembab[0], 'Oksigen:' + oksigen[0]]

            #Inisialisasi varibael hasil dengan variabel list data
            hasil = data[i]

            #Encode data Menggunakan ascii
            cln_sock.send(hasil.encode('ascii'))

            #Menerima data dari client
            data = cln_sock.recv(100)

            #Decode data dari client dengan ascii
            data = data.decode('ascii')

            #Cetak data
            print(data)

        #Melakukan penambahan data atau berhenti
        lagi = input("Tambah data lagi? (y/t) : ")
        if lagi == 't':
            break



