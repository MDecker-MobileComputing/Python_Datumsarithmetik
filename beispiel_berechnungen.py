"""
Beispielprogramm für die Verwendung der Datumsberechnungen-Klasse.
Demonstriert verschiedene Funktionen der Klasse.
"""

from datumsberechnungen import Datumsberechnungen


calc = Datumsberechnungen.get_singleton_instanz()

print()  # Empty line at the beginning

# welcher tag ist heute in 10 tagen
datum_in_10_tagen = calc.heute_plus_tage(10)
print(f"Das Datum in 10 Tagen ist: {datum_in_10_tagen}")

datum_in_100_tagen = calc.heute_plus_tage(100)
print(f"Das Datum in 100 Tagen ist: {datum_in_100_tagen}")

print()  # Empty line at the end
