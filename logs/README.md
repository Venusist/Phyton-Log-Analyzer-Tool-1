Kodun anlatımı

1. Araç Çantasını Getirmek (import re)
Öncelikle Python'a diyoruz ki: "Bana birazdan metinlerin içinde dedektiflik yapıp belirli şablonları (rakam nokta rakam vs.) bulmamı sağlayacak bir araç lazım."
İşte bu hazır araçların bulunduğu koda Modül (veya Kütüphane) diyoruz. re kelimesi "Regular Expressions" (Düzenli İfadeler) kelimelerinin kısaltmasıdır.
import re diyerek, bu modülü projemizin içine dahil ediyoruz (import ediyoruz) ki kodumuzun ilerleyen satırlarında bu araçları kullanabilelim.

2. Fabrikayı Kurmak (def count_ips(path):)
Şimdi kendimize özel bir iş yapan bir sistem kuruyoruz. Belirli bir işi yapmak için gruplandırılmış bu kod bloklarına Fonksiyon (Function) diyoruz. def kelimesi (define - tanımla) ile Python'a "Ben şimdi bir fonksiyon tanımlıyorum" diyoruz ve adını count_ips koyuyoruz.
Peki o parantez içindeki (path) nedir? Buna Parametre (Parameter) diyoruz. Fonksiyonumuza diyoruz ki: "Sen bir fabrika gibisin, sana dışarıdan bir hammadde gelecek. O hammadde bir dosya konumu olacak. Ben şimdilik o konuma path adını veriyorum." Parametre, dışarıdan gelecek gerçek bilgi için ayırdığımız boş bir koltuktur, ismini tamamen biz belirleriz.

3. Çetele Tablosunu Asmak (ip_counter = {})
Şimdi IP'leri sayacağız ama bunları nerede tutacağız? Bize anahtar-kilit uyumuyla çalışan bir tablo lazım. Örneğin "192.168.1.1" -> 5 kere geçti gibi.
İşte süslü parantezlerle {} oluşturduğumuz bu yapıya Sözlük (Dictionary) diyoruz. Sözlükler Anahtar (Key) ve Değer (Value) ikilileriyle çalışır. Yani IP adresi anahtarımız, onun kaç kere geçtiği sayısı ise değerimiz olacak. Başlangıçta bu sözlüğü tertemiz, bomboş bir şekilde oluşturup ip_counter adında bir Değişkene (Variable) atıyoruz.

4. Dosyayı Güvenlice Açmak (with open(path, "r") as file:)
Şimdi elimizdeki path (dosya konumu) bilgisini kullanarak dosyayı açma vakti. Ancak dosyaları öylece açıp bırakmak tehlikelidir, işimiz bitince kapatmamız gerekir.
İşte with open(...) yapısı bizim için bu açma ve iş bitince güvenle kapatma işlemini otomatik yapar. İçerideki "r" harfi Okuma Modu (Read Mode) anlamına gelir. Dosyaya "Sadece içindekileri okuyacağım, sana zarar vermeyeceğim veya seni değiştirmeyeceğim" diyoruz. Açtığımız bu koca dosyayı da hafızada tutabilmek için file adında bir Dosya Nesnesi (File Object) olarak isimlendiriyoruz.

5. Satır Satır Okumak (for line in file:)
Koca bir log dosyasını tek seferde okumak bilgisayarın hafızasını (RAM) şişirebilir. Bunun yerine bir Döngü (Loop) kuruyoruz.
for line in file: diyerek şunu diyoruz: "Bu file dosyasının içine gir ve içindeki metni satır satır eline al. O an elinde tuttuğun satıra da line diyelim." Böylece her seferinde sadece tek bir satıra odaklanarak aşağı doğru iniyoruz.

6. Dedektiflik Zamanı (ips = re.findall(r"\d+\.\d+\.\d+\.\d+", line))
İşte en can alıcı yer! Elimizde bir line (satır) var. re modülümüzün içindeki findall (tümünü bul) fonksiyonunu çağırıyoruz.
Ona bir Düzenli İfade (Regex Şablonu) veriyoruz: r"\d+\.\d+\.\d+\.\d+". Bu şifreli metin özetle "rakamlar+nokta+rakamlar+nokta..." yani tam bir IP formatı demek.
findall bu satırı tarıyor. Bulduğu TÜM IP adreslerini bir kutunun içine koyuyor. Python'da birden fazla elemanı içinde tutabilen bu sıralı kutulara Liste (List) diyoruz. İçinde birden fazla IP olabileceği için bu listeyi ips (çoğul) adında bir değişkene atıyoruz. (Eğer o satırda hiç IP yoksa bize boş bir liste [] verir).

7. Kutunun İçindekileri Çıkarmak (for ip in ips:)
Şimdi elimizde ips adında bir liste var. Bu listenin içindeki IP'leri tek tek saymak için listeyi açmamız lazım.
Bunun için bir İç Döngü (Nested Loop) daha kuruyoruz. for ip in ips: diyerek diyoruz ki: "Bu ips listesinin içine gir, oradaki IP adreslerini sırayla eline al. O an eline aldığın tekil adrese de ip diyelim." Hatırlarsan önceki açıklamamda burası kafanı karıştırmıştı; aslında isim değiştirmiyoruz, sadece kutunun (ips) içinden tek bir eşyayı (ip) çekip alıyoruz.

8. Sözlüğü Güncellemek (if ip in ip_counter: ...)
Artık elimizde tek bir ip var. Hemen duvara astığımız çetele tablomuza yani sözlüğümüze (dictionary) dönüyoruz.
Burada bir Koşul (Condition) yani if/else (eğer/değilse) bloğu kullanıyoruz:

if ip in ip_counter: -> "Eğer bu IP, sözlüğümüzün anahtarları (keys) arasında zaten varsa..."

ip_counter[ip] += 1 -> "...git o IP'nin karşısındaki değeri (value) bul ve sayıyı 1 artır."

else: -> "Eğer bu IP sözlükte yoksa (yani bu adamla ilk kez karşılaşıyorsak)..."

ip_counter[ip] = 1 -> "...sözlüğe bu IP'yi yeni bir kayıt olarak ekle ve karşısına değer olarak 1 yaz."

9. Sonucu Teslim Etmek (return ip_counter)
Tüm dosyayı satır satır gezdik, tüm IP'leri bulduk, sözlüğe yazdık. Döngülerimiz bitti. Artık count_ips fonksiyonumuzun işi tamam.
return (döndür) anahtar kelimesiyle fonksiyonumuza diyoruz ki: "İşin bitti, hazırladığın bu ip_counter sözlüğünü, bu fonksiyonu kim çalıştırdıysa ona geri fırlat (teslim et)."

10. Motoru Çalıştırmak (if __name__ == "__main__": kısmı)
Üstteki her şey fabrikanın kurulumuydu. Şimdi şalteri indirip fabrikayı çalıştırıyoruz.
count_ips(r"C:\Users...sample.log") diyerek fonksiyonumuzu çağırıyoruz (calling the function).
İşte burası çok önemli: Fonksiyonu kurarken kullandığımız o (path) boş koltuğuna, şimdi gerçek bir veri oturtuyoruz. O parantez içine yazdığımız gerçek dosya yoluna artık parametre değil, Argüman (Argument) diyoruz. Fonksiyon gidiyor, çalışıyor ve bize o sözlüğü return ile geri fırlatıyor. Biz de gelen bu sözlüğü result adında bir değişkene kaydediyoruz.

Son olarak for ip, count in result.items(): ile sözlüğümüzün içindeki anahtar ve değerleri ikili ikili (ip ve count olarak) çekip alıyoruz ve print(f"{ip} -> {count}") sayesinde aralarına şık bir ok işareti koyarak ekrana yazdırıyoruz.
