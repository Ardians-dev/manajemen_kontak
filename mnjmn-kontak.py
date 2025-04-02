file_data = 'data.txt'
import ast
import json

def program_utama():
  while True:
    print(22*"=")
    print("== MANAJEMEN KONTAK ==")
    print(22*"=" + "\n")

    print("#Daftar Permintaan#")
    print('''
    1. input data
    2. cari data
    3. tampilkan semua kontak
    4. hapus kontak\n''')
    pertanyaan_program = int(input("apa yang ingin anda lakukan? [1/2/3/4]: "))

    if pertanyaan_program == 1:
      def program1():
        input_nama = str(input("\nmasukan nama: "))
        input_nomor_telepon = int(input("masukan nomor telepon: "))
        input_email = str(input("masukan email: "))
        input_data = str(input("\nketik 'input' untuk menginput!: "))
      
        data_nama = input_nama
        data_nomor_telepon = input_nomor_telepon
        data_email = input_email

        data_pengguna = {
        "nama":"",
        "nomor telepon":"",
        "email":""
        }

        data_pengguna.update({'nama':f'{data_nama}'})
        data_pengguna.update({'nomor telepon':f'{data_nomor_telepon}'})
        data_pengguna.update({'email':f'{data_email}'})
        
        if data_pengguna:
            print("\n" +(len(data_pengguna["email"])*'''='''))
            for x,y in data_pengguna.items():
              print(x + ' : ' + y)   
            print(len(data_pengguna["email"])*'''=''' + "\n")
            
            with open(file_data, "a") as file:
                file.write(str(data_pengguna) + "\n")
                print("data telah disimpan!")     
                
            pertanyaan_program2 = str(input("ingin input lagi? [y/n] (ketik 'exit' jika ingin keluar dari program): "))
            while pertanyaan_program2 == "y":
                program1()
            if pertanyaan_program2 == "n":
                 pertanyaan_program2 = str(input("ketik exit untuk keliar: "))
                 if pertanyaan_program2 == "exit":
                   print("terima kasih telah menggunakan program ini!")
                   exit()
            else:
              print("input anda tdak ada dipilihan. terima kasih telah menggunakan program kami!")
              exit()
      program1()
    elif pertanyaan_program == 2:
      def program2():
        output_data = str(input("masukkan nama yang ingin dicari: "))   
        cari_data = False
        with open(file_data, "r") as file:
          for line in file:
            data_dict = eval(line.strip())
            if data_dict['nama'] == output_data:
              print("\ndata ditemukan:")
              print(30*'''=''')
              print(f"nama : {data_dict['nama']}")
              print(f"nomor telepon : {data_dict['nomor telepon']}")
              print(f"email : {data_dict['email']}")
              print(30*'''=''' + "\n")
              cari_data = True
              pilihan = str(input("ingin melihat data lainnya? [y/n]: "))
              if pilihan == "y":
                program2()
              else:
                program_utama()
          if cari_data == False:
            print("\ndata tidak ditemukan")
            pilihan = str(input("ingin mencari data lainnya? [y/n] ketik exit untuk keluar dri program: "))
            if pilihan == "y":
              program2()
            elif pilihan == "n":
              program_utama()
            else:
              print("terima kasih telah menggunakan program kami")
              exit()
      program2()
    elif pertanyaan_program == 3:
       with open(file_data, "r") as file:
          data_dict = file.read()
          print("\n berikut semua data yang tersimpan:")
          print(85*'''=''' + "\n")
          print(data_dict)   
          print(85*'''=''' + "\n")
       program_utama()
    elif pertanyaan_program == 4:
      def data_dibaca(file_data):
        try:
          with open(file_data, "r") as file:
            return json.load(file)
        except (FileNotFoundError , json.JSONDecodeError):
          return []
        
      def data_ditulis(file_data, data):
        with open(file_data, "w") as file:
          json.dump(data, file, indent=4)
          
      def data_dihapus(file_data, nama):
        data = data_dibaca(file_data)
        data_baru = [item for item in data if item.get("nama") != nama]
        if len(data) == len(data_baru):
          print("data tidak ditemukan")
        else:
          data_ditulis(file_data, data_baru)
          print("data berhasil dihapus")   
      input_data = str(input("masukan nama yang ingin dihapus: "))
      data_dihapus(file_data, input_data)
    else:
      print("anda salah memasukan pilihan")
      program_utama()
program_utama()