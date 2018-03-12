#Import library socket, threading dan time
import socket
import threading
import time


# Definisi fungsi dengan nama thread
def thread(conn):

    #Perulangan untuk menampilkan data
   while True:

       #Exception Handler apabila koneksi masih berjalan dan terputus
       try:

           #Menerima data dengan delay 1 second serta mengirimkan pesan balasan ke server
           data = conn.recv(100)
           data = data.decode('ascii')
           print(data)
           time.sleep(1)
           data = "OK " + data
           conn.send(data.encode('ascii'))

        #Exception apabila koneksi telah terputus
       except (socket.error):
           conn.close()
           print("Koneksi diputus oleh client....")
           break


#Inisiasi objek socket
srv_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Binding ke alamat client
srv_sock.bind(('0.0.0.0', 8080))

#Listen dengan permintaan sebanyak 100 kali
srv_sock.listen(100)

#Perulangan untuk melakukan threading
while True:
    conn, cln_sock = srv_sock.accept()
    tr = threading.Thread(target=thread, args=(conn,))
    tr.start()

