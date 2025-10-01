Feature: Datumsberechnung

  Scenario: Morgiges Datum im selben Monat
    Given die API unter Test ist initialisiert
     When das heutige Datum der 2025-10-15 ist
     Then ist in 1 Tagen der 2025-10-16
