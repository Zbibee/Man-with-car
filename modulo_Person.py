import modulo_Garage

class Person:
    def __init__(self, imie = 'unknow', nazwisko = 'unknow', adres_zam = 'unknow', ilosc_samochodow = []):
        self.imie = imie
        self.nazwisko = nazwisko
        self.adres_zam = adres_zam
        self.garage = modulo_Garage.Garage()
        self.garage.set_pojemnosc(3)
        self.ilosc_samochodow = self.garage.info
    
    def nowy_samochod(self):
        self.garage.dodaj_samochod()
    
    def usun_z_kolekcji(self, rejestracja):
        self.garage.usun_samochod(rejestracja)
    
    def __str__(self):
        return "---{} {}------------------------------------\n{}\n{}\n".format(self.imie, self.nazwisko, self.adres_zam, self.garage)



    
