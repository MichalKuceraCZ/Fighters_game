# Hra:
# Predstavte si, ze jsem vas zakaznik a chci od Vas vytvorit v Pythonu hru simulaci areny s
# bojovniky. Kreativite se meze nekladou, ale zakladni koncept je, ze mezi sebou budou
# souperit dva bojovnici na zivot a na smrt.
# Poznamka!!!: Zacnete programovat u zakladu - prvne vytvorte jednoduchy fungujici zaklad a
# pote az rozsirujte o specialni funkcionality
# Programujte postupne reseni podle obtiznost:
# 1. Dva bojovnici mezi sebou bojuji na zivot a na smrt
# 2. Zapojte prvky nahody (nahodne bonusove poskozeni, ..)
# 3. Bojovnici budou bojovat v arene (Vytvorte arenu jako objekt) - naformatujte vystup
# 4. Vytvorte vice druhu bojovniku s ruznymi vlastnostmi (sermir, lukostrelec, mag, .. -
# pres deditelnost samozrejme), ktery si budou moci uzivatele zvolit
# 5. Zamerte se na bezpecnosti detaily objektu - napr. pocet zivotu bojovnika, jeho
# poskozeni atd. by nemel byt upravitelny jinym bojovnikem jen tak - implementovat
# privatni atributy a predelat logiku utoku
# 6. Udelejte moznost bojovych skupin - vice bojovniku na kazde strane, ktery se stridaji
# kdyz ten pred nemi zemre
# 7. Muzete rozsirit hru na PVE (player vs environment - hrac proti pocitaci), kdy si napr.
# hrac muze vybrat 5 bojovniku, kteri budou bojovat proti bosovi (drak, ..)
# 8. Gratuluji! Vytvorili jste vlastni pocitacovou hru a zjistili jste, ze jste schopni
# programatori! Az se naucite pracovat s Gitem, urcite si hru ulozte na svuj Git jako
# ukazku Vasich schopnosti a sdilejte ji se skupinou i se mnou! :)
# Dale zapojte kreativitu a vylepsite si hru podle libosti, tesim se na Vase vysledky! :)
import random


class Zbran:
    def __init__(self, typ, sila):
        self.typ = typ
        self.sila = sila


class Bojovnik:
    def __init__(self, jmeno, zdravi, sila, zbran, ma_stit, bonusove_poskozeni, pocet_let_bojovych_zkusenosti,
                 pocet_zivotu):
        self.jmeno = jmeno
        self.zdravi = zdravi
        self.sila = sila
        self.zbran = zbran
        self.ma_stit = ma_stit
        self.bonusove_poskozeni = bonusove_poskozeni
        self.pocet_let_bojovych_zkusenosti = pocet_let_bojovych_zkusenosti
        self.pocet_zivotu = pocet_zivotu

    def __str__(self):
        return f"Jmeno: {self.jmeno}, Zdravi: {self.zdravi}, Sila: {self.sila}, " \
               f"Zbran: {self.zbran}, Ma stit: {self.ma_stit}, Bonusove poskozeni: {self.bonusove_poskozeni}, " \
               f"Pocet let bojovych zkusenosti: {self.pocet_let_bojovych_zkusenosti}, " \
               f"Pocet zivotu: {self.pocet_zivotu}"


class Sermir(Bojovnik):
    def __init__(self, jmeno, zdravi, sila, zbran, ma_stit, bonusove_poskozeni, pocet_let_bojovych_zkusenosti,
                 pocet_zivotu):
        super().__init__(jmeno, zdravi, sila, zbran, ma_stit, bonusove_poskozeni, pocet_let_bojovych_zkusenosti,
                         pocet_zivotu)


class Lukostrelec(Bojovnik):
    def __init__(self, jmeno, zdravi, sila, zbran, ma_stit, bonusove_poskozeni, pocet_let_bojovych_zkusenosti,
                 pocet_zivotu):
        super().__init__(jmeno, zdravi, sila, zbran, ma_stit, bonusove_poskozeni, pocet_let_bojovych_zkusenosti,
                         pocet_zivotu)


class Mag(Bojovnik):
    def __init__(self, jmeno, zdravi, sila, zbran, ma_stit, bonusove_poskozeni, pocet_let_bojovych_zkusenosti,
                 pocet_zivotu):
        super().__init__(jmeno, zdravi, sila, zbran, ma_stit, bonusove_poskozeni, pocet_let_bojovych_zkusenosti,
                         pocet_zivotu)


def stret_bojovniku(utocnik: Bojovnik, obrance: Bojovnik):
    # TODO tady si muzes pohrat se stretem, prvky randomizace apod.
    print("utocnik", utocnik.jmeno, utocnik.zbran.sila * utocnik.sila,
          "obrance", obrance.jmeno, int(obrance.ma_stit) * 100 * obrance.sila)

    if (utocnik.zbran.sila * utocnik.sila) > (int(obrance.ma_stit) * obrance.sila):
        obrance.pocet_zivotu -= 1
        print(f"vyhra utocnika")
    else:
        print(f"vyhra obrance")


class Arena:
    def __init__(self, bojovnik1: Bojovnik, bojovnik2: Bojovnik):
        self.bojovnik1 = bojovnik1
        self.bojovnik2 = bojovnik2

    def rozhodni_utocnik_obrance(self):
        if random.choice([self.bojovnik1, self.bojovnik2]) == self.bojovnik1:
            return self.bojovnik1, self.bojovnik2
        else:
            return self.bojovnik2, self.bojovnik1

    def boj(self):
        while self.bojovnik1.pocet_zivotu > 0 and self.bojovnik2.pocet_zivotu > 0:
            utocici_bojovnik, branici_bojovnik = self.rozhodni_utocnik_obrance()
            # print(f"utoci bojovnik: {utocici_bojovnik} , branici bojovnik: {branici_bojovnik}")
            stret_bojovniku(utocici_bojovnik, branici_bojovnik)

        if self.bojovnik1.pocet_zivotu > self.bojovnik2.pocet_zivotu:
            print(f"Vítězem souboje je {self.bojovnik1.jmeno}.")
        elif self.bojovnik1.pocet_zivotu < self.bojovnik2.pocet_zivotu:
            print(f"Vítězem souboje je {self.bojovnik2.jmeno}.")
        else:
            print("Oba bojovníci utrpěli stejné poškození. Boj skončil remízou.")


z1 = Zbran(typ="mec", sila=50)
z2 = Zbran(typ="luk", sila=60)

b1 = Sermir(
    jmeno="Pan Sermir", zdravi=100, sila=40, zbran=z1, ma_stit=False,
    bonusove_poskozeni=20, pocet_let_bojovych_zkusenosti=2, pocet_zivotu=4
)
b2 = Lukostrelec(
    jmeno="Pan Lukous", zdravi=100, sila=20, zbran=z2, ma_stit=True,
    bonusove_poskozeni=50, pocet_let_bojovych_zkusenosti=3, pocet_zivotu=3
)

print(b1)  # vysledek metody __str__()
print(b2)  # vysledek metody __str__()

hra = Arena(bojovnik1=b1, bojovnik2=b2)
hra.boj()
