"""
- Tämä on harjoitus tehtävä 1 (Kurssisuoritukset), Tietokantojen perusteet kevät 2021
"""

import sqlite3

class DB:
    """
    Tietokannan luokka
    """

    def __init__(self, route:str,lvl:bool):
        self.db = sqlite3.connect(route)
        self.db.isolation_level = lvl
        self.Main()
    
    def Main(self):
        while True:
            command = int(input('Valitse toiminto: '))
            if command == 1:
                return self.count_summary()
            if command == 2:
                return self.student_courses()
                break
            if command == 3:
                return self.course_deg()
                break
            if command == 4:
                return self.top_points()
                break
            if command == 5:
                break
    def top_points(self):
        while True:
            limit = int(input("Anna opettajien määrä: "))
            result = self.db.execute('SELECT OP.nimi, SUM(S.arvosana) FROM Suoritukset S, Kurssit K, Opettajat OP WHERE S.kurssi_id = K.id AND K.opettaja_id = OP.id GROUP BY OP.id ORDER BY SUM(S.arvosana) DESC LIMIT ?', [limit]).fetchall()
            print("{:<30} {:<10}".format('opettaja','op'))
            for ope in result:
                print("{:<30} {:<10}".format(ope[0],ope[1]))
            break
        self.Main()

    def course_deg(self):
        while True:
            nimi = input("Anna kurssin nimi: ")
            result = self.db.execute('SELECT S.arvosana, COUNT(S.arvosana) FROM Suoritukset S, Opiskelijat O, Kurssit K WHERE S.opiskelija_id = O.id AND K.nimi = ? AND S.kurssi_id = K.id GROUP BY S.arvosana', [nimi]).fetchall()
            for arvosana in result:
                print(f'Arvosana {arvosana[0]}: {arvosana[1]} kpl')
            break
        self.Main()

    def student_courses(self):
        while True:
            nimi = input("Anna opiskelijan nimi: ")
            result = self.db.execute('SELECT K.nimi, K.laajuus, S.paivays, S.arvosana FROM Suoritukset S, Opiskelijat O, Kurssit K WHERE S.opiskelija_id = O.id AND O.nimi = ? AND S.kurssi_id = K.id ORDER BY S.paivays', [nimi]).fetchall()
            print("{:<10} {:<10} {:<15} {:<15}".format('kurssi', 'op', 'päiväys', 'arvosana'))
            for kurssi in result:
                print("{:<10} {:<10} {:<15} {:<15}".format(kurssi[0], kurssi[1], kurssi[2], kurssi[3]))
            break
        self.Main()


    def count_summary(self):
        while True:
            year = input("Anna vuosi: ")
            result = self.db.execute('SELECT COUNT(s.arvosana) FROM Suoritukset s WHERE s.paivays like ? ', [year+'%']).fetchall()
            print(f'Opintopisteiden määrä: {result[0][0]}')
            break
        self.Main()


db = DB('kurssit.db',None)
