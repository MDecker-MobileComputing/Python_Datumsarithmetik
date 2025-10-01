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

