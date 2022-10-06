# Hra:
# Predstavte si, ze jsem vas zakaznik a chci od Vas vytvorit v Pythonu hru simulaci areny s bojovniky. Kreativite se meze nekladou, ale zakladni koncept je, ze mezi sebou budou souperit dva bojovnici na zivot a na smrt.
#
# Poznamka!!!: Zacnete programovat u zakladu - prvne vytvorte jednoduchy fungujici zaklad a pote az rozsirujte o specialni funkcionality
#
# Programujte postupne reseni podle obtiznost:
# Dva bojovnici mezi sebou bojuji na zivot a na smrt
# Zapojte prvky nahody (nahodne bonusove poskozeni, ..)
# Bojovnici budou bojovat v arene (Vytvorte arenu jako objekt) - naformatujte vystup
# Vytvorte vice druhu bojovniku s ruznymi vlastnostmi (sermir, lukostrelec, mag, .. - pres deditelnost samozrejme), ktery si budou moci uzivatele zvolit
# Zamerte se na bezpecnosti detaily objektu - napr. pocet zivotu bojovnika, jeho poskozeni atd. by nemel byt upravitelny jinym bojovnikem jen tak - implementovat privatni atributy a predelat logiku utoku
# Udelejte moznost bojovych skupin - vice bojovniku na kazde strane, ktery se stridaji kdyz ten pred nemi zemre
# Muzete rozsirit hru na PVE (player vs environment - hrac proti pocitaci), kdy si napr. hrac muze vybrat 5 bojovniku, kteri budou bojovat proti bosovi (drak, ..)
# Gratuluji! Vytvorili jste vlastni pocitacovou hru a zjistili jste, ze jste schopni programatori! Az se naucite pracovat s Gitem, urcite si hru ulozte na svuj Git jako ukazku Vasich schopnosti a sdilejte ji se skupinou i se mnou! :)
# Dale zapojte kreativitu a vylepsite si hru podle libosti, tesim se na Vase vysledky! :)



import random


class Bojovnik:

    def __init__(self, jmeno, zbran, pocet_zivotu, stit: bool, bojove_zkusenosti):
        self.jmeno = jmeno
        self.zbran = zbran
        self.pocet_zivotu = pocet_zivotu
        self.stit = stit
        self.bojove_zkusenosti = bojove_zkusenosti
        self.sila_zbrane = self.ucinnost_zbrane()

        self.zbrane = {"mec": 75, "dyka": 50, "kopi": 80, "palcat": 45, "maceta": 70}

    def ucinnost_zbrane(self):
        if self.zbran == "mec":
            ef_zbr = random.randrange(50, 76)
        elif self.zbran == "dyka":
            ef_zbr = random.randrange(15, 36)
        elif self.zbran == "kopi":
            ef_zbr = random.randrange(40, 96)
        elif self.zbran == "palcat":
            ef_zbr = random.randrange(15, 45)
        elif self.zbran == "maceta":
            ef_zbr = random.randrange(40, 76)
        else:
            ef_zbr = random.randrange(1, 11)

        return ef_zbr

    def jmeno(self):
        return self.jmeno

    def utok(self):
        return (random.randint(0, 100) + self.zbrane.get(self.zbran) + self.bojove_zkusenosti) / 3

    def obrana(self):
        return (random.randint(0, 100) + self.bojove_zkusenosti + (100 * self.stit)) / 3 * self.pocet_zivotu / 100

    def uder(self, protivnik):
        protivnik.pocet_zivotu -= self.sila_zbrane*random.random()
        if protivnik.pocet_zivotu <= 0:
            protivnik.pocet_zivotu = 0


Robin_bojovnik = Bojovnik("Robin", "mec", 100, True, 80)
Jan_bojovnik = Bojovnik("Jan", "mec", 100, False, 80)

while Jan_bojovnik.pocet_zivotu > 0 or Robin_bojovnik.pocet_zivotu > 0:

    if Robin_bojovnik.pocet_zivotu != 0:
        Robin_bojovnik.uder(Jan_bojovnik)
        print(f"životy Jana {Jan_bojovnik.pocet_zivotu: .0f}")
        if Jan_bojovnik.pocet_zivotu != 0:
            Jan_bojovnik.uder(Robin_bojovnik)
            print(f"životy Robina {Robin_bojovnik.pocet_zivotu: .0f}")
        else:
            break
    else:
        break

    if Robin_bojovnik.pocet_zivotu > Jan_bojovnik.pocet_zivotu:
        print("Vítězem souboje je Robin.")
    elif Robin_bojovnik.pocet_zivotu < Jan_bojovnik.pocet_zivotu:
        print("Vítězem souboje je Jan.")
    else:
        print("Oba bojovníci utrpěli stejné poškození. Boj skončil remízou.")
