from datetime import datetime, timedelta
import locale
from typing import Optional


class Datumsberechnungen:
    """
    Diese Klasse enthält Methoden für Datumsarithmetik mit einem Referenzdatum als Startdatum.
    """

    def __init__(self, referenz_datum: Optional[str] = None):
        """
        Konstruktor für Datumsberechnungen.
        
        Args:
            referenz_datum: Referenzdatum im ISO-Format (YYYY-MM-DD). 
                          Falls None, wird das aktuelle Datum verwendet.
        """
        if referenz_datum is None:
            # Aktuelles Datum verwenden
            self._heute_datetime = datetime.now()
        else:
            # Referenzdatum aus ISO-String parsen (str: string parse time)
            try:
                self._heute_datetime = datetime.strptime(referenz_datum, '%Y-%m-%d')
            except ValueError as e:
                raise ValueError(f"Ungültiges Datumsformat '{referenz_datum}'. Erwartet: YYYY-MM-DD") from e

        # Locale auf Deutsch setzen (falls verfügbar)
        try:
            locale.setlocale(locale.LC_TIME, 'de_DE.UTF-8')
        except locale.Error:
            try:
                locale.setlocale(locale.LC_TIME, 'German_Germany.1252')
            except locale.Error:
                # Fallback: Englisch verwenden
                pass

    def _formatiere_datum_mit_wochentag(self, datum: datetime) -> str:
        """
        Formatiert ein Datum mit dem entsprechenden deutschen Wochentag.

        Args:
            datum: Das zu formatierende Datum

        Returns:
            String im Format DD.MM.YYYY (Wochentag), z.B. "15.01.2024 (Montag)"
        """
        # Deutsche Wochentage
        deutsche_wochentage = {
            0: "Montag",
            1: "Dienstag",
            2: "Mittwoch",
            3: "Donnerstag",
            4: "Freitag",
            5: "Samstag",
            6: "Sonntag"
        }

        datum_str = datum.strftime("%d.%m.%Y")
        wochentag = deutsche_wochentage[datum.weekday()]

        return f"{datum_str} ({wochentag})"

    def heute_plus_tage(self, anzahl_tage: int) -> str:
        """
        Addiert Anzahl tage auf heutiges Datum und gibt das Ergebnisdatum zurück.

        Args:
            anzahl_tage: Anzahl Tage, die auf heutiges Datum zu addieren ist;
                        kann auch negativ sein.

        Returns:
            String mit Ergebnisdatum im Format DD.MM.YYYY (Wochentag), z.B. "15.01.2024 (Montag)".
        """
        ergebnis_datum = self._heute_datetime + timedelta(days=anzahl_tage)
        return self._formatiere_datum_mit_wochentag(ergebnis_datum)

    def heute_minus_tage(self, anzahl_tage: int) -> str:
        """
        Subtrahiert Anzahl Tage vom heutigen Datum und gibt das Ergebnisdatum zurück.

        Args:
            anzahl_tage: Anzahl Tage, die vom heutigen Datum zu subtrahieren ist;
                        sollte positiv sein.

        Returns:
            String mit Ergebnisdatum im Format DD.MM.YYYY (Wochentag), z.B. "15.01.2024 (Montag)".
        """
        return self.heute_plus_tage(-anzahl_tage)