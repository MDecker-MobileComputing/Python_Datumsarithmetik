# Datumsarithmetik mit Python #

<br>

Dieses Repo enthält ein Python-Programm für Datumsarithmetik.
Es wird mit [Behave](https://pypi.org/project/behave/) unter Test genommen; siehe hierzu auch
[dieses Tutorial](https://pyquesthub.com/enhancing-test-automation-with-cucumber-in-python).

## Installation

### Option 1: Globale Installation (einfach)
```cmd
py -m pip install behave
```

### Option 2: Mit virtueller Umgebung (empfohlen)
```cmd
# Virtuelle Umgebung erstellen
py -m venv venv

# Aktivieren (Windows)
venv\Scripts\activate

# Dependencies installieren
py -m pip install -r requirements.txt
```

## Tests ausführen
```cmd
behave
```

## Programm ausführen
```cmd
py beispiel_berechnungen.py
```