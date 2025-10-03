# Datumsarithmetik mit Python #

<br>

Dieses Repo enthält eine Python-Klasse für Datumsarithmetik, mit der die Anzahl der Tage zwischen 
dem aktuellen Datum und einem anderen Datum in der Zukunft oder Vergangenheit berechnet werden kann.
Diese Klasse soll mit [Behave](https://pypi.org/project/behave/) unter Test genommen werden; 
siehe hierzu auch [dieses Tutorial](https://pyquesthub.com/enhancing-test-automation-with-cucumber-in-python).

<br>

Siehe [hier](https://github.com/MDecker-MobileComputing/Maven_Cucumber_Datumsarithmetik) für die Java-Variante
dieses Beispiels.

<br>

----

## Tests mit Behave ausführen ##

<br>

Installation von *Behave*:
```cmd
py -m pip install behave
```

<br>

Tests ausführen:

```cmd
behave
```

<br>

Wenn *Behave* so nicht gefunden wird (weil *Python User Scripty Directory* nicht in Umgebungsvariable `$PATH` enthalten ist), dann kann man es mit folgendem Befehl 
ausführen:
```cmd
py -m behave
``` 

<br>

----

## API-Doku erzeugen ##

<br>

Programm [pydoc](https://pdoc.dev/) installieren:
``` 
py -m pip install pdoc
```

<br>

API-Doku für Klasse `Datumsberechnungen` erzeugen und in Unterordner `docs` schreiben:

```
py -m pdoc datumsberechnungen.py --output-dir docs
```

<br>

Die so erzeugte API-Doku wird mit *GitHub Pages* unter [dieser URL](https://mdecker-mobilecomputing.github.io/Python_Datumsarithmetik/datumsberechnungen.html)
Bereitgestellt.

<br>
