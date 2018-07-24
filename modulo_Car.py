class Car:
    ilosc_obiektow = 0
    
    def __init__(self ,marka = 'unknow', model = 'unknow', ilosc_drzwi = 0, pojemnosc_silnika = 0, nr_rejestracyjny = 'unknow', sr_spalanie = 0):
        self.marka = marka
        self.model = model
        self.ilosc_drzwi = ilosc_drzwi
        self.pojemnosc_silnika = pojemnosc_silnika
        self.nr_rejestracyjny = nr_rejestracyjny
        self.sr_spalanie = sr_spalanie
        Car.ilosc_obiektow += 1

    def set_marka(self, marka):
        self.marka = marka

    def set_model(self, model):
        self.model = model

    def set_ilosc_drzwi(self, ilosc_drzwi):
        if ilosc_drzwi > 0:
            self.ilosc_drzwi = ilosc_drzwi
        else:
            print("Samochód nie może mieć ujemnej ilości drzwi")

    def set_pojemnosc_silnika(self, pojemnosc_silnika):
        if pojemnosc_silnika > 0:
            self.pojemnosc_silnika = pojemnosc_silnika
        else:
            print("pojemność silnika nie może być ujemna")

    def set_nr_rejestracyjny(self, nr_rejestracyjny):
        self.nr_rejestracyjny = nr_rejestracyjny

    def set_sr_spalanie(self, sr_spalanie):
        if sr_spalanie > 0:
            self.sr_spalanie = sr_spalanie
        else:
            print("Średnie spalanie na 100km nie może być liczbą ujemną")

    def get_marka(self):
        return self.marka

    def get_model(self):
        return self.model

    def get_ilosc_drzwi(self):
        return self.ilosc_drzwi

    def get_pojemnosc_silnika(self):
        return self.pojemnosc_silnika

    def get_nr_rejestracyjny(self):
        return self.nr_rejestracyjny

    def get_sr_spalanie(self):
        return self.sr_spalnie

    def oblicz_sr_spalanie(self, trasa):
        if trasa > 0:
            spalanie_na_tr = self.sr_spalanie * trasa # prawdopodobnie zjebane rownanie
            return spalanie_na_tr
        else:
            print("trasa musi byc wartością dodatnią")
            
    def cena_paliwa(self, trasa, cena):
        if trasa > 0 and cena > 0:
            cena_paliwa = (self.sr_spalanie * trasa) * cena # nie wiem czy dobrze zastanow sie
            return cena_paliwa
        else:
            print("cena i trasa muszą być liczbą dodatnią")

    def __str__(self):
        return "Samochód {}\n\tModel:{}\n\tilość drzwi: {}\n\tpojemność silnika: {}\n\tnr rejestracyjny: {}\n\tśrednie spalanie: {}".format(self.marka, self.model, self.ilosc_drzwi, self.pojemnosc_silnika, self.nr_rejestracyjny, self.sr_spalanie)
    
    def ile_samochodow(Car):
        return "ilosc obiektow: {}".format(Car.ilosc_obiektow)

def main_car():
    a = Car()
    print (a)
    a.set_pojemnosc_silnika(5)
    a.set_sr_spalanie(7)
    print(a)
    print("samochod spali srednio {} podczas 300 km".format(a.oblicz_sr_spalanie(300)))
    print("podczas wyjazdu na majowke 300 km cena paliwa to: {}".format(a.cena_paliwa(300,2)))
       
    

    
