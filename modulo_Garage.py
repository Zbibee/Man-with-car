import modulo_Car

class Garage:
    
    def __init__(self, adres = 'unknow', pojemnosc = 0, ile_samochodow = 0, info = [], cars = []):
        self.adres = adres
        self.pojemnosc = pojemnosc
        self.ile_samochodow = ile_samochodow
        self.info = info
        self.cars = cars

    def set_adres(self, adres):
        self.adres = adres

    def set_pojemnosc(self, pojemnosc):
        if pojemnosc > 0:
            self.pojemnosc = pojemnosc
        else:
            print("maksymalna liczba samochodów którą pomieści garaż musi być liczbą dodatnią")

    def set_ile_samochodow(self, ile_samochodow):
        if  ile_samochodow > 0 and self.ile_samochodow + ile_samochodow <= self.pojemnosc:
            self.ile_samochodow = ile_samochodow
        else:
            print("Obacna ilość samochodów w garażu nie może być liczbą ujemną lub większą od maksymalnej pojemnosci w garazu")

    def set_info(self, info):
        self.info.append(info)

    def get_adres(self):
        return format(self.adres)

    def get_pojemnosc(self):
        return self.pojemnosc

    def get_ile_samochodow(self):
        return self.ile_samochodow          

    def get_info(self):
        return self.info
            
    def dodaj_samochod(self): # co zrobic gdy podane argumnety sie nie zgadzaja
        if self.ile_samochodow < self.pojemnosc:
            self.ile_samochodow += 1
            samochod = modulo_Car.Car()
            self.cars.append(samochod)
            self.set_info(samochod.nr_rejestracyjny)
        else:
            return "Za mało miejsca w garażu na nowy samochód"
    
    def usun_samochod(self, rejestracja):
        if self.ile_samochodow > 0:
            for car in self.cars:
                if car.nr_rejestracyjny == rejestracja:
                    self.cars.remove(car)
                    self.info.remove(car.nr_rejestracyjny)
                    self.ile_samochodow -= 1
        else:
            print("Garaż jest już pusty!!!")

    def __str__(self):
        ciag = "Garaż: {}\nMaksymalna ilość pojazdów mieszczących się w garażu: {}\nIlość aktualnie znajdujących się pojazdów w garażu: {}\n---------------------------------------------------".format(self.adres, self.pojemnosc, self.ile_samochodow)
        if self.cars != []:
            for car in self.cars:
                ciag += "\n" + str(car)
        else:
            ciag += "\nGaraż jest pusty"

        return ciag
        
def main_garage():
    a = Garage()
    print(a)
    a.set_pojemnosc(3)
    a.dodaj_samochod()
    a.dodaj_samochod()
    print(a)
    print(a.get_info())
    #a.get_info()
    
    a.usun_samochod('unknow')
    a.usun_samochod('unknow')
    print(a)
    print(a.get_info())

#main_garage()

