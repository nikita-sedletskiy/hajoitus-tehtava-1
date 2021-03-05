# hajoitus-tehtava-1
Harjoitustehtävä 1, Kurssisuoritukset

Olemassa olevassa tietokannassa on tietoa opiskelijoista, opettajista, kursseista ja suorituksista. Tietokannan SQL-skeema on seuraava:

```sql
CREATE TABLE Opiskelijat (
    id INTEGER PRIMARY KEY,
    nimi TEXT
);

CREATE TABLE Opettajat (
    id INTEGER PRIMARY KEY,
    nimi TEXT
);

CREATE TABLE Kurssit (
    id INTEGER PRIMARY KEY,
    nimi TEXT,
    laajuus INTEGER,
    opettaja_id INTEGER REFERENCES Opettajat
);

CREATE TABLE Suoritukset (
    id INTEGER PRIMARY KEY,
    opiskelija_id INTEGER REFERENCES Opiskelijat,
    kurssi_id INTEGER REFERENCES Kurssit,
    arvosana INTEGER,
    paivays DATE
);
```

Saat ladattua tietokannan itsellesi SQLite-tiedostona tästä. Voit tutkia tietokantaa SQLite-tulkissa, jotta saat paremman kuvan sen sisällöstä. Tietokannan sisältö on luotu satunnaisesti tätä tehtävää varten.

Tehtäväsi on laatia tietokantaa käyttävä ohjelma, jossa on seuraavat toiminnot:

    Laske annettuna vuonna saatujen opintopisteiden yhteismäärä.
    Tulosta annetun opiskelijan kaikki suoritukset aikajärjestyksessä.
    Tulosta annetun kurssin suoritusten arvosanojen jakauma.
    Tulosta top x eniten opintopisteitä antaneet opettajat.
    Sulje ohjelma. 

Voit toteuttaa ohjelman haluamallasi ohjelmointikielellä.

Seuraavassa on esimerkki, jota voit käyttää apuna ohjelman toteuttamisessa. Varmista, että oma ohjelmasi saa haettua samat tulokset tietokannasta kuin esimerkissä.
```
Valitse toiminto: 1
Anna vuosi: 2014
Opintopisteiden määrä: 278816
Valitse toiminto: 2
Anna opiskelijan nimi: Anna Leppänen
kurssi         op   päiväys        arvosana
TKT2722        1    2000-01-23     3   
TKT4351        5    2000-03-13     5   
TKT7097        2    2000-04-06     4   
TKT9089        2    2000-04-29     4   
TKT2379        5    2000-11-10     2   
... (rivejä välissä)
TKT5409        5    2018-10-26     2   
TKT0844        3    2019-01-16     2   
TKT1076        6    2019-03-17     3   
TKT0151        9    2019-07-23     4   
TKT4629        6    2019-10-14     5   
Valitse toiminto: 3
Anna kurssin nimi: TKT1424
Arvosana 1: 193 kpl
Arvosana 2: 222 kpl
Arvosana 3: 206 kpl
Arvosana 4: 195 kpl
Arvosana 5: 213 kpl
Valitse toiminto: 4
Anna opettajien määrä: 10
opettaja             op  
Pentti Tiainen       106721
Otto Kuusela         106434
Joel Aalto           99067
Sirpa Hänninen       94917
Tommi Ojala          92107
Risto Nousiainen     91001
Niina Ojala          90092
Suvi Määttä          88284
Otto Peltola         87388
Risto Hyttinen       86336
Valitse toiminto: 5
```
Ohjelman vaatimukset:

    Ohjelman kaikki toiminnot hakevat oikeat tiedot tietokannasta.
    Jokaisessa toiminnossa tulokset haetaan yksittäisellä kyselyllä.
    Kyselyissä ei käytetä alikyselyjä.
    Käyttäjän antamat tiedot annetaan kyselyille parametreina. 
