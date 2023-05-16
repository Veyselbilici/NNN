#Magza sınıfı oluşturuyorum
class Magaza:
    def __init__(self, magaza_adi, satici_adi, satici_cinsi):
        self.__magaza_adi = magaza_adi
        self.__satici_adi = satici_adi
        self.__satici_cinsi = satici_cinsi

    # Accessor/Mutator metotları kullandık
    def get_magaza_adi(self):
        return self.__magaza_adi

    def set_magaza_adi(self, magaza_adi):
        self.__magaza_adi = magaza_adi

    def get_satici_adi(self):
        return self.__satici_adi

    def set_satici_adi(self, satici_adi):
        self.__satici_adi = satici_adi

    def get_satici_cinsi(self):
        return self.__satici_cinsi

    def set_satici_cinsi(self, satici_cinsi):
        self.__satici_cinsi = satici_cinsi

    # Satış tutarlarını dictionary'de saklayacak metod
def magaza_satis_tutar(magaza_dict, magaza_adi=None, satici_adi=None, satici_cinsi=None):
    toplam_magaza_satis = 0
    toplam_satici_satis = {}
    for key, value in magaza_dict.items():
        magaza = value['magaza']
        satici_adi = value['satici_adi']
        satici_cinsi = value['satici_cinsi']
        satis_tutari = value['satis_tutari']

        if magaza_adi is not None and magaza != magaza_adi:
            continue

        if satici_adi is not None and satici_adi != satici_adi:
            continue

        if satici_cinsi is not None and satici_cinsi != satici_cinsi:
            continue
        # Toplam satış tutarlarını hesaplama bölümu

        toplam_magaza_satis += satis_tutari
        if satici_adi in toplam_satici_satis:
            toplam_satici_satis[satici_adi] += satis_tutari
        else:
            toplam_satici_satis[satici_adi] = satis_tutari

    return toplam_magaza_satis, toplam_satici_satis


magaza_dict = {}
while True:
    magaza_adi = input("Mağaza adını girin: ")
    satici_adi = input("Satıcı adını girin: ")
    satici_cinsi = input("Satıcının cinsini girin (tv, bilgisayar, beyaz eşya, diğer): ")
    satis_tutari = float(input("Satış tutarını girin: "))

    # Mağaza sınıfından instance oluşturuluyor ve satış tutarı dictionary'de saklanıyor

    magaza = Magaza(magaza_adi, satici_adi, satici_cinsi)
    magaza_dict[len(magaza_dict) + 1] = {'magaza': magaza, 'satici_adi': satici_adi, 'satici_cinsi': satici_cinsi,
                                         'satis_tutari': satis_tutari}

    devam_et = input("Başka satış var mı? (E/H)").lower()
    if devam_et == "h":
        break

toplam_magaza_satis, toplam_satici_satis = magaza_satis_tutar(magaza_dict)

# Mağaza ve satıcıların toplam satış tutarları yazdırılıyor

print("Mağaza toplam :",toplam_magaza_satis)
print("satıcı toplam:",toplam_satici_satis)









