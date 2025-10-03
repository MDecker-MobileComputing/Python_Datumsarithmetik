# Diese Datei verwendet die Gherkin-Syntax, siehe auch https://cucumber.io/docs/#what-is-gherkin
Feature: Datumsberechnung

  Scenario: Morgiges Datum im selben Monat
    Given die API unter Test ist initialisiert
     When das heutige Datum der 2025-10-15 ist
     Then ist in 1 Tagen der 2025-10-16

  Scenario: Morgiges Datum im selben Monat
    Given die API unter Test ist initialisiert
     When das heutige Datum der 2025-10-25 ist
     Then ist in 1 Tagen der 2025-10-26

  Scenario: Morgiges Datum im nächsten Monat
    Given die API unter Test ist initialisiert
     When das heutige Datum der 2025-10-31 ist
     Then ist in 1 Tagen der 2025-11-01

  Scenario: Morgiges Datum im nächsten Jahr
    Given die API unter Test ist initialisiert
     When das heutige Datum der 2025-12-31 ist
     Then ist in 1 Tagen der 2026-01-01

  Scenario: Gestriges Datum im selben Monat
    Given die API unter Test ist initialisiert
     When das heutige Datum der 2025-10-25 ist
     Then ist in -1 Tagen der 2025-10-24

   Scenario: Gestriges Datum im vorherigen Monat
    Given die API unter Test ist initialisiert
     When das heutige Datum der 2025-10-01 ist
     Then ist in -1 Tagen der 2025-09-30

   Scenario: Gestriges Datum im vorherigen Jahr
    Given die API unter Test ist initialisiert
     When das heutige Datum der 2026-01-01 ist
     Then ist in -1 Tagen der 2025-12-31

   Scenario: Datum laut Delta aus Tabelle
    Given die API unter Test ist initialisiert
     When das heutige Datum der 2023-01-01 ist
     Then ergeben sich durch Addition der folgenden Deltawerte folgende Datumswerte
          | Delta  | Ergebnis   |
          |  10    | 2023-01-11 |
          |  100   | 2023-04-11 |
          | -2     | 2022-12-30 |
          | -100   | 2022-09-23 |

# Webseite zum Nachrechnen: https://de.planetcalc.com/410/
