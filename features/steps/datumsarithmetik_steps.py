from behave import given, when, then
from datetime import datetime
import sys
import os

# Add the parent directory to the path to import our module
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
from datumsberechnungen import Datumsberechnungen


@given('die API unter Test ist initialisiert')
def step_api_initialisiert(context):
    """
    Initialisiert die Datumsberechnungen API für den Test.
    """

    # Das Kontext-Objekt wird von Behave bereitgestellt
    context.datumsberechnungen = Datumsberechnungen.get_singleton_instanz()

    # Sicherstellen, dass die API verfügbar ist
    assert context.datumsberechnungen is not None, "API konnte nicht initialisiert werden"


@when('das heutige Datum der {datum} ist')
def step_datum_setzen(context, datum):
    """
    Setzt das heutige Datum für den Test auf den angegebenen Wert.

    Args:
        context: Behave context object
        datum: Datum im Format YYYY-MM-DD, z.B. "2025-10-15"
    """
    # Parse das Datum im Format YYYY-MM-DD
    try:
        test_datum = datetime.strptime(datum, '%Y-%m-%d')
        context.datumsberechnungen.set_heute_datum_for_testing(test_datum)
        context.test_datum = datum  # Speichere für später
    except ValueError as e:
        raise ValueError(f"Ungültiges Datumsformat '{datum}'. Erwartet: YYYY-MM-DD") from e


@then('ist in {tage:d} Tagen der {erwartetes_datum}')
def step_datum_pruefen(context, tage, erwartetes_datum):
    """
    Prüft, ob das berechnete Datum nach der angegebenen Anzahl Tage korrekt ist.

    Args:
        context: Behave context object
        tage: Anzahl Tage als Integer
        erwartetes_datum: Erwartetes Datum im Format YYYY-MM-DD
    """
    # Berechne das Datum
    berechnetes_datum = context.datumsberechnungen.heute_plus_tage(tage)

    # Extrahiere nur das Datum (ohne Wochentag) aus dem Format "DD.MM.YYYY (Wochentag)"
    # Das Format der Ausgabe ist "DD.MM.YYYY (Wochentag)", wir brauchen nur das Datum
    if '(' in berechnetes_datum:
        datum_teil = berechnetes_datum.split('(')[0].strip()
    else:
        datum_teil = berechnetes_datum

    # Konvertiere DD.MM.YYYY zu YYYY-MM-DD für Vergleich
    try:
        parsed_datum = datetime.strptime(datum_teil, '%d.%m.%Y')
        berechnetes_datum_iso = parsed_datum.strftime('%Y-%m-%d')
    except ValueError:
        # Falls das Format anders ist, verwende direkt den berechneten Wert
        berechnetes_datum_iso = berechnetes_datum

    assert berechnetes_datum_iso == erwartetes_datum, \
        f"Erwartetes Datum: {erwartetes_datum}, aber berechnet wurde: {berechnetes_datum_iso}"