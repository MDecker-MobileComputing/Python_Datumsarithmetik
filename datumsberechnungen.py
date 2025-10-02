from datetime import datetime, timedelta
import locale
from typing import Optional


class Datumsberechnungen:
    """
    Diese Klasse enthält Methoden für Datumsarithmetik mit dem aktuellen Datum als Startdatum.
    """

    # Singleton-Instanz der Klasse, wird bei Bedarf in statischer Methode get_singleton_instanz() erzeugt.
    _singleton_instanz: Optional['Datumsberechnungen'] = None

    def __init__(self):
        """
        Privater Dummy-Konstruktor um zu verhindern, dass ein Objekt
        dieser Klasse von einer anderen Klasse erzeugt wird.
        """
        # Heutiges Datum; kann mit Methode set_heute_datum_for_testing(datetime) geändert werden.
        self._heute_datetime = datetime.now()

        # Locale auf Deutsch setzen (falls verfügbar)
        try:
            locale.setlocale(locale.LC_TIME, 'de_DE.UTF-8')
        except locale.Error:
            try:
                locale.setlocale(locale.LC_TIME, 'German_Germany.1252')
            except locale.Error:
                # Fallback: Englisch verwenden
                pass

    @classmethod
    def get_singleton_instanz(cls) -> 'Datumsberechnungen':
        """
        Methode liefert Singleton-Instanz der Klasse zurück;
        Singleton-Objekt wird ggf. erzeugt.

        Returns:
            Singleton-Instanz
        """
        if cls._singleton_instanz is None:
            cls._singleton_instanz = cls()

        return cls._singleton_instanz

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

    def set_heute_datum_for_testing(self, heute_datetime: datetime) -> None:
        """
        Mit dieser Methode kann das Datum für den heutigen Tag
        für Testzwecke kontrolliert (geändert) werden.

        Args:
            heute_datetime: Neues Datum für "Heute"
        """
        self._heute_datetime = heute_datetime