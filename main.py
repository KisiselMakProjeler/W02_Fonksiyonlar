from basit_hesap_makinesi.toplama import toplama
from basit_hesap_makinesi.cikarma import cikarma

birinci_sayi =int(input("Birinci sayıyı giriniz: "))
ikinci_sayi = int(input("Ikinci sayıyı giriniz: "))

toplama_sonuc=toplama(birinci_sayi, ikinci_sayi)

ucuncu_sayi = int(input("Üçüncü sayıyı giriniz: "))

cikarma_sonuc=cikarma(toplama_sonuc, ucuncu_sayi)
print(f'Çıkarma işleminin sonucu:{cikarma_sonuc}')