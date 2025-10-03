"""
Beispielprogramm für die Verwendung der Datumsberechnungen-Klasse.
Demonstriert verschiedene Funktionen der Klasse.
"""

from datumsberechnungen import Datumsberechnungen


# Erstelle eine Instanz mit dem aktuellen Datum (kein Parameter übergeben)
calc = Datumsberechnungen()

print()

# welcher tag ist heute in 10 tagen
datum_in_10_tagen = calc.heute_plus_tage(10)
print(f"Das Datum in 10 Tagen ist: {datum_in_10_tagen}")

datum_in_100_tagen = calc.heute_plus_tage(100)
print(f"Das Datum in 100 Tagen ist: {datum_in_100_tagen}")

print()

datum_vor_10_tagen = calc.heute_minus_tage(10)
print(f"Das Datum vor 10 Tagen war: {datum_vor_10_tagen}")

datum_vor_100_tagen = calc.heute_minus_tage(100)
print(f"Das Datum vor 100 Tagen war: {datum_vor_100_tagen}")

print()

# Beispiel mit einem spezifischen Referenzdatum
print("Beispiel mit Referenzdatum 2024-01-15:")
calc_mit_datum = Datumsberechnungen("2024-01-15")

datum_in_7_tagen = calc_mit_datum.heute_plus_tage(7)
print(f"7 Tage nach dem 15.01.2024 ist: {datum_in_7_tagen}")

datum_vor_30_tagen = calc_mit_datum.heute_minus_tage(30)
print(f"30 Tage vor dem 15.01.2024 war: {datum_vor_30_tagen}")

print()
