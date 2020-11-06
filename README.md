# Tugas_Pertemuan_7- Praktikum_labspy02

Repository ini dibuat untuk memenuhi tugas Bahasa Pemrograman Pertemuan ke-7 pada Modul Praktikum 2.

***Nama : Miftahu Rizkiyah***

***NIM : 312010014***

***Kelas : TI.20.B.1***

=====================

## Tugas Praktikum_labspy02
 
Membuat program sederhana dengan menginput 3 buah bilangan, dari ketiga bilangan tersebut tampilkan bilangan terbesarnya, dengan menggunakan *statement if*

## Menentukan Bilangan Terbesar dari 3 nilai yang diinputkan

Pada pertemuan ke-7 ini saya membuat tugas yang diberikan oleh dosen Bahasa Pemrograman - Teknik Informatika.
Untuk membuat aplikasi yang menentukan bilangan terbesar dari 3 bilangan yang user inputkan menggunakan bahasa program python.
<br>

Pada repository ini saya akan menjelaskan alur didalam **Flowchart** yang telah saya buat. Untuk file **flowchat** bisa dilihat pada link berikut : 
:[Tugas_Pertemuan_7_Tugas_Pertemuan_7](Flowchart_part7.pdf)
<br>

berikut source code yang saya buat :

``` python
print("Masukan Bilangan ke-1 : ")
bilangan1=int(input())
print("Masukan Bilangan Ke-2 : ")
bilangan2=int(input())
print("Masukan Bilangan Ke-3 : ")
bilangan3=int(input())
```
berikut contoh (bilangan 1>bilangan2) and (bilangan 1>bilangan3) :<br>
Dengan source code : 

``` python
if ( bilangan1 > bilangan2 ) and ( bilangan1 > bilangan3 ) :
    print("Bilangan 1 lebih Besar dari Bilangan 2 dan 3")
```
Dari source code tersebut akan menghasilkan output :

![Bilangan1>bilangan2&3](pict/Bilangan1_lebih_besar_dari_bilangan2_dan_bilangan3.PNG)
<br>
dan jika (bilangan 2>bilangan 1) and (bilangan 2>bilangan 3) :
dengan source code :

```python
elif ( bilangan2 > bilangan1) and ( bilangan2 > bilangan3 ) :
    print ("Bilangan 2 lebih Besar dari Bilangan 1 dan 3")
```
Dari source code tersebut akan menghasilkan output : 
![(Bilangan2>Bilangan1),(Bilangan2>Bilangan3)](pict/Bil2_lebih_besar_dari_bil1_dan_bil3.PNG)

 


