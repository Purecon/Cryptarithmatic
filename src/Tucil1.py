#Muhammad Furqon (13519184)
#Cryptarithmatic

import time
import os

last_hasil=0,0,0
length_max=0
remainder=0 
angka=0 
jmlh=0
valid=True
jmlh_loop=0
list_angka = [0,1,2,3,4,5,6,7,8,9]
list_huruf = []
correct =0
ada_jawaban=False

#Permutasi elemen
def permutasi(elemen, r):
    n = len(elemen)
    indeks = list(range(n))
    perm = list(range(n, n-r, -1))
    yield tuple(elemen[i] for i in indeks[:r])
    stop=False
    while(not stop):
        stop=True
        for i in reversed(range(r)):
            perm[i] -= 1
            if perm[i] == 0:
                indeks[i:] = indeks[i+1:] + indeks[i:i+1]
                perm[i] = n - i
            else:
                j = perm[i]
                indeks[i], indeks[-j] = indeks[-j], indeks[i]
                yield tuple(elemen[i] for i in indeks[:r])
                stop=False
                break
#Referensi: https://stackoverflow.com/questions/104420/how-to-generate-all-permutations-of-a-list

#Dictionary huruf unik
isMain=True
substring="+"
substring_skip="-"
list_main=[]
list_main_output=[]
list_hasil=[]
dict_huruf = {}
#List untuk setiap kata, inisialisasi dictionary
os.chdir("..")
cur_dir=os.getcwd()
os.chdir(cur_dir+"\\test")
nama_file = input("Masukkan nama file masukan: ")
cur_dir=os.getcwd()
path=cur_dir+ "\\" + nama_file
file = open(path,"r") 
Lines = file.readlines()
start = time.time()
for kata in Lines:
    skip=False
    kata=kata.strip() 
    if(substring_skip in kata):
        skip=True
    if(not skip):
        if(isMain):
            if(substring in kata):
                isMain=False
                kata=kata.replace('+','')
            list_main.append(list(kata))
            list_main_output.append(list(kata))     
        else:
            list_hasil=list(kata)
        for huruf in kata:
            dict_huruf[huruf] = dict_huruf.get(huruf,0) + 1

#Buat dict kosong, list huruf
for key in dict_huruf:
    list_huruf.append(key)
    dict_huruf[key] = -1

list_hasil_output=list(list_hasil)

#Cek dari kanan/last
for x in list_main:
    x.reverse()

list_hasil.reverse()

#Ujung kiri tidak boleh 0, angka mulai dari 1
#Length di sini adalah indeks ujung, len-1
length_main_max = len(max(list_main,key=len))-1
length_max = len(list_hasil)-1

# Permutasi
perm = permutasi(list_angka,len(dict_huruf))  
for x in list(perm):
    #Setup
    correct=0
    angka=0
    valid=True
    i=0
    #ubah nilai dictionary
    for y in x:
        dict_huruf[list_huruf[angka]]=y
        angka += 1
    while(i<=length_max and valid):
        if(i <= length_main_max):
            for sublist in list_main:
                if(i<=len(sublist)-1):
                    temp = dict_huruf[sublist[i]]
                    if(i==(len(sublist)-1)):
                        if(temp==0):
                            valid=False
                            remainder=0
                else:
                    temp=0
                jmlh += temp
            jmlh += remainder
            if jmlh>=10:
                remainder=jmlh//10
            else:
                remainder=0
            if(i!=length_max):
                jmlh=jmlh%10
            #penjumlahan elemen
        else:
            jmlh=remainder

        #cek dengan elemen dari hasil
        last_hasil = dict_huruf[list_hasil[i]]
        if(i==(len(list_hasil)-1)):
            if(last_hasil==0):
                valid=False
                remainder=0
        if(valid):
            if(jmlh==last_hasil):
                correct+=1
                if(correct==length_max+1):
                    valid=False
                    remainder=0
            else:
                valid=False
                remainder=0
        jmlh=0
        i+=1
    if(correct==length_max+1):
        #Print soal
        count=0
        print("Soal:")
        for output in list_main_output:
            selisih=length_max-len(output)+1
            print(" "*selisih,end="")
            for x in output:
                print(x, end="")
            if(count==len(list_main_output)-1):
                print("+",end="")
            print()
            count+=1
        print("-" * (length_max+1))
        for x in list_hasil_output:
            print(x, end="")
        print()
        #Print jawaban
        count=0
        print("Jawaban:")
        for output in list_main_output:
            selisih=length_max-len(output)+1
            print(" "*selisih,end="")
            for x in output:
                print(dict_huruf[x], end="")
            if(count==len(list_main_output)-1):
                print("+",end="")
            print()
            count+=1
        print("-" * (length_max+1))
        for x in list_hasil_output:
            print(dict_huruf[x], end="")
        print()
        #Print tes dan waktu
        print('Jumlah total tes: {}'.format(jmlh_loop))
        end = time.time()
        print('Waktu pengerjaan adalah {:.2f} s'.format(end-start))

        correct=0
        ada_jawaban=True
    jmlh_loop += 1

if(not ada_jawaban):
    print("Tidak ditemukan solusi")

input("Tekan enter untuk mengakhiri program")
