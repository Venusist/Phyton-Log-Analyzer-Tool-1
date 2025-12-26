import re

def count_ips(path):
    ip_counter = {}
#{} → boş dictionary

    with open(path, "r") as file:
        for line in file:
            ips = re.findall(r"\d+\.\d+\.\d+\.\d+",line)
            for ip in ips:
                if ip in ip_counter:
                    #Bu IP’yi daha önce saymış mıydım evetse artar
                    ip_counter[ip] += 1
                else:
                    ip_counter[ip] = 1

    return ip_counter

if __name__ == "__main__":
    result = count_ips(r"C:\Users\ipekm\Desktop\logs\sample.log")
#Dönen dictionary’yi result içine koyuyoruz
    print("IP Count results:")
    for ip, count in result.items():
        print(f"{ip} -> {count}")


"""
kodun bi önceki hali sadece dosyayı okurken
def read_log_file(path):
    with open(path, "r") as file:
        for line in file:
            print(line.strip())

if __name__ == "__main__":
    read_log_file(r"C:\ipekm\Desktop\logs\sample.log")

def: Python'a "Ben yeni bir işlem (fonksiyon) tanımlıyorum" dersiniz.
read_log_file adını ve path adını da biz verdik
with: En önemli kısımdır. with bloğu, işimiz bittiğinde dosyanın otomatik olarak kapatılmasını sağlar. Eğer with kullanmazsanız ve dosyayı kapatmayı unutursanız, dosya hafızada asılı kalabilir veya bozulabilir.
open(path, "r"): path adresindeki dosyayı açar. "r" harfi "read" (oku) anlamına gelir. Yani "Sadece okuyacağım, üzerine bir şey yazmayacağım" demiş olursunuz.
as file: Açtığımız bu dosyaya kodun geri kalanında kısaca file (dosya) diyeceğiz diye takma isim verirsiniz.
strip() → baştaki/sondaki boşlukları siler
r (raw string) eklediğinizde, Python ters bölü işaretlerini olduğu gibi metin olarak kabul eder ve hata çıkmaz.
if __name__ == "__main__":
Eğer bu dosya direkt olarak çalıştırılıyorsa (başka bir dosya tarafından kütüphane olarak çağrılmadıysa) aşağıdaki kodları yap
Bu sayede bu dosyayı başka bir projeye import ederseniz, aşağıdaki test kodları otomatik olarak çalışmaz, sadece fonksiyonu kullanabilirsiniz

read_log_file("logs/sample.log")
Yukarıda tanımladığımız read_log_file makinesini çalıştırıyoruz.
Ona path olarak bilgiyi de veriyoru<z
"""

"""
Kalıbı (r"\d+\.\d+\.\d+\.\d+") parçalayalım:
r"...": "Raw string" anlamına gelir. Python'a "Bunun içindeki ters eğik çizgileri (\) özel karakter olarak değil, regex sembolü olarak algıla" der.
\d+: Bir veya daha fazla rakam (Örneğin: 192, 10, 5).
\.: Nokta işareti. Normalde . regex'te "her şey" demektir. Sadece noktayı kastetmek için önüne \ (kaçış karakteri) koyuyoruz.
Mantık: Rakamlar + . + Rakamlar + . + Rakamlar + . + Rakamlar
Bu kalıp şuna benzeyen her şeyi yakalar: 192.168.1.1, 10.0.0.50, 127.0.0.1."""