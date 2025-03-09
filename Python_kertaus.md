# Python ohjelmoinnin kertaus 2025

---
### practice1.py - Perusteet: muuttujat, funktiot ja merkkijonot


#### Ohjelman logiikka (Wireframe):

- Tulostetaan erilaisia arvoja, kuten merkkijonoja ja lukuja
- Luodaan muuttujia ja käytetään niitä laskutoimituksissa
- Luodaan funktioita päivien muuntamiseen sekunneiksi
- Esitellään muuttujien näkyvyysalueet

#### Kuvaus:

Tämä koodi esittelee Pythonin perusteita, kuten muuttujien käyttöä, merkkijonojen muotoilua ja funktioiden luontia.
Käytetyt ohjelmointitekniikat:

- Muuttujien käyttö: merkkijono, kokonaisluku ja liukuluku

    ```python
    print("Hello World!") # Merkkijono (String)
    print(2.5) # Liukuluku (Float)
    print(2) # Kokonaisluku (Integer)
    print(-2) # Kokonaisluku (Integer)
    ```
- Merkkijonojen yhdistäminen
    ```python
    print("20 days are " + str(50) + " minutes")  # Vanha tapa
    print(f"20 days are {50} minutes")  # Uudempi tapa (f-string)
    ```
- Funktioiden luonti ja käyttö
- Muuttujien näkyvyysalueet (scope)

#### Funktiot

```python
    def days_to_units(num_of_days):
        print(f"{num_of_days} days are {num_of_days * cal_to_sec} {name_of_unit}")
        print("Good!")
```

#### Funktiokutsut

```python
    days_to_units(20)
    days_to_units(35)
    days_to_units(50)
    days_to_units(110)
```

#### Muuttujien laajuus (Scope)

```python
    def scope_check(num_of_days):
        inside_var = "This variable only inside of function"
        print(name_of_unit)  # Globaali muuttuja
        print(num_of_days)   # Paikallinen muuttuja
        print(inside_var)
```

<hr>

### <span style="color:#01759a">practice2.py - Käyttäjän syötteen käsittely</span>
<hr>

#### Kuvaus:

    Tämä koodi esittelee käyttäjän syötteen käsittelyä ja funktioiden paluuarvojen käyttöä.
    Käytetyt ohjelmointitekniikat:

    - Käyttäjän syötteen lukeminen (input).
    - Funktioiden paluuarvot (return).

#### Ohjelman logiikka (Wireframe):

    - Käyttäjä syöttää päivämäärän.
    - days_to_units-funktio muuntaa päivät tunneiksi.
    - Tulos tallennetaan muuttujaan ja tulostetaan.

#### Käyttäjän Syöte

#### Käyttäjän syötteen lukeminen

    ```python
    user_input = input("He, enter a number of days and I will convert it to hours?\n")
    print(user_input)
    ```
    - `input()` lukee käyttäjän antaman syötteen merkkijonona.
    - `print()` tulostaa syötteen konsoliin.

#### Funktiot ja Palautusarvot

#### Muuttujien määrittely

    ```python
    cal_to_units = 24             
    name_of_unit = "seconds"
    ```
    - Määritellään muuttujat, joita käytetään laskennassa.

#### Funktion määrittely

    ```python
    def days_to_units(num_of_days):       
        return f"{num_of_days} days are {num_of_days * cal_to_units} {name_of_unit}"
    ```
    - `def` määrittää funktion.
    - `return` palauttaa arvon kutsujalle, eikä vain tulosta sitä.

#### Funktiokutsu

#### Palautetun arvon tallennus ja tulostus

    ```python
    my_var = days_to_units(20)
    print(my_var)
    ```
    - Tallennetaan funktion palauttama arvo muuttujaan.
    - Tulostetaan muuttujan arvo konsoliin.

### practice3.py - Funktioiden paluuarvot

#### Kuvaus:

    Tämä koodi esittelee funktioiden paluuarvojen käyttöä. Se muuntaa käyttäjän syöttämät päivät tunneiksi ja tulostaa tuloksen.
    Käytetyt ohjelmointitekniikat:

    - Funktioiden paluuarvot (return).
    - Syötteen muuntaminen kokonaisluvuksi (int).

#### Funktioiden Palautusarvot ja Käyttäjän Syöte

#### Muuttujien määrittely

    ```python
    cal_to_units = 24             
    name_of_unit = "hours"
    ```
    - `cal_to_units` sisältää päivien muunnoskertoimen tunneiksi.
    - `name_of_unit` määrittää yksikön tulosteelle.

#### Funktion määrittely

    ```python
    def days_to_units(num_of_days):       
        return f"\n{num_of_days} days are {num_of_days * cal_to_units} {name_of_unit}"
    ```
    - `def` määrittää funktion.
    - `return` palauttaa muokatun merkkijonon.

#### Käyttäjän syötteen käsittely

#### Syötteen lukeminen ja muuntaminen

    ```python
    user_input = input("Hey, enter a number of days and I will convert it to hours? ")
    ```
    - `input()` lukee käyttäjän antaman arvon merkkijonona.

#### Arvon muuntaminen kokonaisluvuksi ja funktion kutsuminen

    ```python
    calculate_value = days_to_units(int(user_input))
    print(calculate_value)
    ```
    - `int(user_input)` muuntaa syötteen kokonaisluvuksi.
    - `days_to_units()` laskee arvon ja tulostaa sen.

#### Vaihtoehtoinen tapa tallentaa ja käyttää syötettä

    ```python
    user_input_number = int(user_input)
    calculate_value2 = days_to_units(user_input_number)
    print(calculate_value2)
    ```
    - Syöte muunnetaan ensin kokonaisluvuksi ja tallennetaan muuttujaan.
    - Muuttujaa käytetään funktion kutsussa.


#### Ohjelman logiikka (Wireframe):

    - Käyttäjä syöttää päivämäärän.
    - days_to_units-funktio muuntaa päivät tunneiksi.
    - Tulos tallennetaan muuttujaan ja tulostetaan.

### practice4.py - Käyttäjän syötteen validointi

#### Kuvaus:

    Tämä koodi esittelee käyttäjän syötteen validointia. Se tarkistaa, onko syöte positiivinen kokonaisluku, ennen kuin se muuntaa päivät tunneiksi.
    Käytetyt ohjelmointitekniikat:

    - Syötteen validointi (isdigit).
    - Funktioiden käyttö (days_to_units).

#### Ohjelman logiikka (Wireframe):

    - Käyttäjä syöttää päivämäärän.
    - if-else-lause tarkistaa, onko syöte positiivinen kokonaisluku.
    - Jos syöte on kelvollinen, päivämäärä muunnetaan tunneiksi ja tulostetaan.
    - Jos syöte ei ole kelvollinen, tulostetaan virheilmoitus.

### practice5.py - Koodin siistiminen ja kapselointi

#### Kuvaus:

    Tämä koodi on siistitty versio practice4.py-koodista. Se kapseloi päivien muuntamisen tunneiksi funktioihin ja lisää virheenkäsittelyn.
    Käytetyt ohjelmointitekniikat:

    - Funktioiden käyttö (days_to_units, validate_and_execute).
    - Virheenkäsittely (if-else-lauseet).

#### Ohjelman logiikka (Wireframe):

    - Käyttäjä syöttää päivämäärän.
    - validate_and_execute-funktio tarkistaa, onko syöte kelvollinen.
    - Jos syöte on kelvollinen, päivämäärä muunnetaan tunneiksi ja tulostetaan.

### practice6.py - Sisäkkäiset silmukat

#### Kuvaus:

    Tämä koodi esittelee sisäkkäisten if-else-lauseiden käyttöä. Se tarkistaa, onko käyttäjän syöte positiivinen kokonaisluku, ja muuntaa päivät tunneiksi.
    Käytetyt ohjelmointitekniikat:

    - Sisäkkäiset if-else-lauseet.
    - Funktioiden käyttö (days_to_units, validate_and_execute).

#### Ohjelman logiikka (Wireframe):

    - Käyttäjä syöttää päivämäärän.
    - validate_and_execute-funktio tarkistaa, onko syöte positiivinen kokonaisluku.
    - Jos syöte on kelvollinen, päivämäärä muunnetaan tunneiksi ja tulostetaan.

### practice7.py - Virheenkäsittely (try-except)

#### Kuvaus:

    Tämä koodi esittelee try-except-rakenteen käyttöä virheiden käsittelyyn. Se varmistaa, että käyttäjän syöte on kelvollinen ennen päivien muuntamista tunneiksi.
    Käytetyt ohjelmointitekniikat:

    - Virheenkäsittely (try-except).
    - Funktioiden käyttö (days_to_units, validate_and_execute).

#### Ohjelman logiikka (Wireframe):

    - Käyttäjä syöttää päivämäärän.
    - validate_and_execute-funktio yrittää muuntaa syötteen kokonaisluvuksi.
    - Jos syöte on kelvollinen, päivämäärä muunnetaan tunneiksi ja tulostetaan.
    - Jos syöte ei ole kelvollinen, tulostetaan virheilmoitus.

### practice8.py - while-silmukka

#### Kuvaus:

    Tämä koodi esittelee while-silmukan käyttöä. Se kysyy käyttäjältä päivämäärää toistuvasti, kunnes käyttäjä syöttää "exit".
    Käytetyt ohjelmointitekniikat:

    - while-silmukka.
    - Funktioiden käyttö (days_to_units, validate_and_execute).
    - Virheenkäsittely (try-except).

#### Ohjelman logiikka (Wireframe):

    - Käyttäjä syöttää päivämäärän tai "exit"-lopettaakseen.
    - Jos syöte ei ole "exit", päivämäärä muunnetaan tunneiksi ja tulostetaan.
    - Silmukka jatkuu, kunnes käyttäjä syöttää "exit".

### practice9.py - Listan käsittely ja pilkkominen

#### Kuvaus:

    Tämä koodi esittelee listan käyttöä ja syötteen pilkkomista pilkulla erotetuksi listaksi. Se muuntaa jokaisen listan alkion tunneiksi.
    Käytetyt ohjelmointitekniikat:

    - Listan käsittely (split, strip).
    - Silmukka (for-loop) listan alkioiden läpikäyntiin.
    - Funktioiden käyttö (days_to_units, validate_and_execute).

#### Ohjelman logiikka (Wireframe):

    - Käyttäjä syöttää päivämääriä pilkulla eroteltuna.
    - Syöte jaetaan listaksi, ja jokainen alkio käsitellään erikseen.
    - Jokainen päivämäärä muunnetaan tunneiksi ja tulostetaan.

### practice10.py - Listan käsittely

#### Kuvaus:

    Tämä koodi esittelee Pythonin listan käyttöä. Se luo listan, lisää ja poistaa alkioita, tulostaa listan pituuden ja käy läpi listan alkiot silmukassa.
    Käytetyt ohjelmointitekniikat:

    - Listan luonti ja käsittely (append, remove, len).
    - Silmukka (for-loop) listan alkioiden läpikäyntiin.

#### Ohjelman logiikka (Wireframe):

    - Luodaan lista my_list kolmella alkulla.
    - Tulostetaan kolmas alkio ja koko lista.
    - Lisätään uusi alkio listaan ja tulostetaan päivitetty lista.
    - Käydään läpi listan alkiot silmukassa.
    - Poistetaan alkio listasta ja tulostetaan päivitetty lista.

### practice11.py - Päivien muuntaminen tunneiksi

#### Kuvaus:

    Tämä koodi muuntaa käyttäjän syöttämät päivät tunneiksi. Se käyttää joukkoja (set) käsittelemään päivämääriä ja varmistaa, että samat syötteet käsitellään vain kerran.
    Käytetyt ohjelmointitekniikat:

    - Funktiot (days_to_units, validate_and_execute).
    - Joukon käyttö (set) duplikaattien poistamiseen.
    - Virheenkäsittely (try-except).

#### Ohjelman logiikka (Wireframe):

    - Käyttäjä syöttää päivämääriä pilkulla eroteltuna.
    - Syötteet jaetaan joukoksi, jotta duplikaatit poistetaan.
    - Jokainen päivämäärä muunnetaan tunneiksi ja tulostetaan.
    - Ohjelma jatkaa, kunnes käyttäjä syöttää "exit".

### practice12.py - Joukon käsittely

#### Kuvaus:

    Tämä koodi esittelee Pythonin joukon (set) käyttöä. Se luo joukon, lisää ja poistaa alkioita sekä tulostaa joukon alkiot.
    Käytetyt ohjelmointitekniikat:

    - Joukon luonti ja käsittely (add, remove).
    - Silmukka (for-loop) joukon alkioiden läpikäyntiin.

#### Ohjelman logiikka (Wireframe):

    - Luodaan joukko my_set kolmella alkulla.
    - Tulostetaan joukko ja sen alkiot silmukassa.
    - Lisätään uusi alkio joukkoon ja poistetaan yksi alkio.
    - Tulostetaan päivitetty joukko.

### practice13.py - Dictionary käyttö päivien muuntamiseen

#### Kuvaus:

Tämä koodi muuntaa päivät tunneiksi tai minuuteiksi käyttäen sanakirjaa (dictionary) syötteen käsittelyyn.

Käytetyt ohjelmointitekniikat:

- Dictionary käyttö syötteen tallentamiseen.
- Funktiot (days_to_units, validate_and_execute).
- Virheenkäsittely (try-except).

#### Ohjelman logiikka (Wireframe):

- Käyttäjä syöttää päivämäärän ja muunnosyksikön (esim. "5-hours").
- Syöte jaetaan sanakirjaksi, jossa avaimet ovat "days" ja "unit".
- Päivämäärä muunnetaan tunneiksi tai minuuteiksi ja tulostetaan.

### practice14.py - Moduulien käyttö

#### Kuvaus:

Tämä koodi esittelee moduulien käyttöä Pythonissa. Se käyttää helper14-moduulia päivien muuntamiseen tunneiksi tai minuuteiksi.

Käytetyt ohjelmointitekniikat:

- Moduulien tuonti (from helper14 import).
- Funktioiden käyttö ulkoisesta moduulista.
- Silmukka (while-loop) käyttäjän syötteen käsittelyyn.

#### Ohjelman logiikka (Wireframe):

- Käyttäjä syöttää päivämäärän ja muunnosyksikön (esim. "5-hours").
- Syöte jaetaan dictionary |sanakirjaksi.
- validate_and_execute-funktio suoritetaan, ja tulos tulostetaan.

helper14.py - Apumoduuli päivien muuntamiseen (practice14.py)

#### Kuvaus:

Tämä moduuli sisältää funktiot päivien muuntamiseen tunneiksi tai minuuteiksi. Sitä käytetään practice14.py-koodissa.
Käytetyt ohjelmointitekniikat:

- Funktiot (days_to_units, validate_and_execute).
- Sanakirjan käyttö syötteen käsittelyyn.
- Virheenkäsittely (try-except).

#### Ohjelman logiikka (Wireframe):

- days_to_units-funktio muuntaa päivät tunneiksi tai minuuteiksi.
- validate_and_execute-funktio varmistaa, että syöte on kelvollinen, ja suorittaa muunnoksen.

### practice15.py - OOP

#### Kuvaus: Jatkan tästä kunhan taas kerkeää..

#### Ohjelman logiikka (Wireframe):


