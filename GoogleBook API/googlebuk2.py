import json, urllib
import urllib.request
import sys

apikey = "&key=AIzaSyCV6kIMVmUwU-ja91j7arZo9QMBuQKlqZo"
link = ("https://www.googleapis.com/books/v1/volumes?q=")
pengarang = (sys.argv[1])+(sys.argv[2])
hasil = link + pengarang + apikey
datanya = urllib.request.urlopen(hasil).read()
baca = json.loads(datanya)
print("Judul : ")
for nilai in range(0,10) :
    print(nilai,".",baca["items"][nilai]["volumeInfo"]["title"])