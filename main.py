import modulo_Person

def main():
    Janusz = modulo_Person.Person('Janusz', 'Cebula','Radom')
    Janusz.garage.set_adres('ul.Chytrej baby nr 5')
    print(Janusz)
    for i in range(3):
        Janusz.nowy_samochod()
    print("***\tJanusz poszedł na zakupy kupił 3 samochody\t***\n")

    Janusz.garage.cars[0].set_marka('Volvo')
    Janusz.garage.cars[0].set_model('V3 Sport')
    Janusz.garage.cars[0].set_ilosc_drzwi(3)
    Janusz.garage.cars[0].set_pojemnosc_silnika(4.2)
    Janusz.garage.cars[0].set_nr_rejestracyjny('KWA 2991 RJ')
    Janusz.garage.info[0] = 'KWA 2991 RJ'
    Janusz.garage.cars[0].set_sr_spalanie(5.2)
    print(Janusz)

    historia = """*** Wycieczka Janusza ***
    W niedziele nie handlową, Janusz postanowił wybrać się do najbliższej biedronki
    Długośc trasy: 40 km Cena paliwa w najtańszej stacji benzynowej wynosi 4.5 zl/l
    Średnie zużycie paliwa w czasie podróży wynosi {},
    więc Janusz na paliwo powinien poświęcić {}zl
    Januszowi się nie opłaca, więc pójdzie na nogach.
    Niestety w tym czasie Grażyna postanowiła się przejechać...
    !!!Grażyna rozbiła Januszowi samochod!!!\n""".format(Janusz.garage.cars[0].oblicz_sr_spalanie(0.4), Janusz.garage.cars[0].cena_paliwa(0.4, 4.5))
    print(historia)
    Janusz.usun_z_kolekcji(Janusz.garage.info[0])
    print(Janusz)

    print("***\tZłodzieje okradaja Janusza\t***\n")
    Janusz.usun_z_kolekcji(Janusz.garage.info[0])
    Janusz.usun_z_kolekcji(Janusz.garage.info[0])
    print(Janusz)   

main()
