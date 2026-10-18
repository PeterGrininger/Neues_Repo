<<<<<<< HEAD
# Python Testing Course

Dieses Repository ist eine praxisorientierte Lernumgebung für das Schreiben von Tests mit Python, pytest und Test-Driven Development (TDD). Es wurde als Übungsprojekt aufgebaut, um die wichtigsten Konzepte der Softwarequalität, des Testens und der sauberen Code-Entwicklung in einer leicht verständlichen, aber professionellen Form zu vermitteln.

Das Ziel ist nicht nur, dass Tests funktionieren, sondern dass sie als Werkzeug zur Sicherung von Codequalität, Lesbarkeit und wartbarer Architektur dienen. Die Aufgaben im Projekt sind bewusst so gestaltet, dass sie typische Entwicklungsszenarien widerspiegeln: kleine Domänenmodelle, Regeln, Spiellogik, Randfälle und Verhaltensänderungen, die durch gezielte Tests abgesichert werden.

---

## Warum dieses Projekt?

Softwareentwicklung ist heute nicht nur ein Thema der Funktionalität, sondern auch der Stabilität und Zuverlässigkeit. Ein gutes Test-Setup hilft dabei, Fehler frühzeitig zu erkennen, Änderungen sicherer zu machen und langfristig die Wartung von Projekten zu vereinfachen.

In diesem Projekt lernen Sie:

- wie man mit pytest Tests für Python-Code schreibt
- wie man Tests für reale Anforderungen formt
- wie man mit TDD arbeitet, also zuerst Tests schreibt und dann die Implementierung entwickelt
- wie man Fehlerfälle, Grenzwerte und untypische Situationen absichert
- wie man mit Mocks, Fakes und einfachen Testdaten arbeitet
- wie man Logik sauber in kleine, testbare Einheiten aufteilt
- wie man Qualität auf nachhaltige Weise überprüft, statt nur „funktioniert auf meinem Rechner“ zu behaupten

Diese Kompetenzen sind für jeden Python-Entwickler relevant, egal ob man an kleinen Projekten, Backend-APIs oder größeren Systemen arbeitet.

---

## Lernziele

Das Projekt verfolgt mehrere Lernziele:

1. Verstehen der grundlegenden Testprinzipien in Python.
2. Schreiben von aussagekräftigen, lesbaren und verlässlichen Tests.
3. Erkennen, wie Anforderungen in Testfälle übersetzt werden.
4. Einsatz von pytest als Standard-Tool für Unit-Tests.
5. Anwendung von TDD: Red → Green → Refactor.
6. Sicherung von Randfällen und Fehlerbedingungen.
7. Gewinnen eines praktischen Verständnisses für saubere Softwarearchitektur.

---

## Aufbau des Repositories

Das Repository ist bewusst in kleine, gut getrennte Übungsbereiche aufgeteilt. Jede Einheit fokussiert sich auf ein bestimmtes Thema oder einen konkreten Testfall.

```text
PythonTesting/
├── src/
│   └── testing_course/
│       ├── exploration/
│       ├── bowling/
│       └── connect_four/
├── tests/
│   ├── exploration/
│   ├── bowling/
│   └── connect_four/
├── pyproject.toml
├── README.md
└── .venv/
```

Die wichtigsten Bereiche sind:

### 1. Exploration
Dieser Teil dient dazu, die Grundlagen von Test- und Entwicklungspraktiken zu üben. Typische Themen sind:

- einfache Funktionen testen
- Logik in kleine Einheiten zerlegen
- Fehlerfälle bewusst modellieren
- Mocks und Fakes einsetzen
- Testdaten klar und konsistent gestalten

Die Übungen sind bewusst zugänglich und bilden die Grundlage für die späteren, komplexeren Aufgaben.

### 2. Bowling-Kata
Bei dieser Übung geht es um die klassische Bowling-Logik. Das Ziel ist, die Regeln eines Spiels in Programmlogik zu übersetzen und mit Tests abzusichern.

Typische Anforderungen sind:

- Strikes und Spares korrekt berechnen
- Mehrere Frames verarbeiten
- Sonderregeln im letzten Frame berücksichtigen
- Grenzfälle sauber abdecken

Dieses Beispiel ist besonders geeignet, um zu sehen, wie komplexe Regeln in kleine, überprüfbare Testfälle zerlegt werden können.

### 3. Connect Four
Die Connect-Four-Übung erweitert das Projekt um eine interaktive Spiel- und Spielregellogik. Diese Domäne ist ideal, um folgendes zu üben:

- Zustände des Spielboards verwalten
- Spielzüge validieren
- Gewinnerprüfung und Gewinnbedingungen abdecken
- Turn-Logik und Regeln modellieren
- Nutzerinteraktionen und Spielabläufe testen

Hier zeigt sich besonders, wie wichtig saubere Trennung von Logik und Benutzeroberfläche ist.

---

## Test-Driven Development im Projekt

Das zentrale Prinzip dieses Projekts ist TDD.

Der typische Ablauf sieht so aus:

1. Eine Anforderung wird formuliert.
2. Ein Test wird geschrieben, der das gewünschte Verhalten beschreibt.
3. Der Test schlägt fehl, weil die Funktion noch nicht implementiert ist.
4. Die minimale Implementierung wird ergänzt.
5. Die Tests werden erneut ausgeführt.
6. Der Code wird refaktoriert, sofern nötig.
7. Der Zyklus wiederholt sich für die nächste Anforderung.

Dieser Ablauf ist nicht nur theoretisch interessant, sondern praktisch extrem wertvoll. Er erzwingt eine klare Definition von Anforderungen und verhindert, dass Code „irgendwie“ funktioniert, ohne wirklich das gewünschte Verhalten zu validieren.

---

## Praktische Einrichtung

Bevor Sie mit den Übungen beginnen, müssen Sie die Python-Umgebung korrekt einrichten.

### Voraussetzungen

- Python 3.13 oder höher
- uv als Paketmanager

### Installation und Setup

Im Projektverzeichnis ausführen:

```bash
uv sync
```

Damit werden die Abhängigkeiten und das Projekt-Environment eingerichtet.

### Tests ausführen

```bash
uv run pytest
```

Wenn Sie nur bestimmte Übungen ausführen möchten:

```bash
uv run pytest tests/bowling
uv run pytest tests/exploration
uv run pytest tests/connect_four
```

Mit Filtern lassen sich einzelne Tests gezielt ausführen:

```bash
uv run pytest -k spare
```

Für mehr Details und Coverage-Reports:

```bash
uv run pytest --cov
```

---

## Nützliche Befehle

```bash
uv run pytest tests/bowling      # Bowling-Übung
uv run pytest -k spare           # Tests mit Namen, die „spare“ enthalten
uv run pytest --cov              # Coverage-Bericht
uv run ruff check                # Linting
uv run ruff format               # Code formatieren
uv run ty check                  # Typprüfung
uv run connect-four               # Das Connect-Four-Spiel starten
```

Diese Befehle helfen dabei, den Entwicklungsprozess professionell und reproduzierbar zu gestalten. Sie zeigen auch, dass gutes Testen nicht nur aus dem Schreiben von Assertions besteht, sondern auch aus dem regelmäßigen Validieren der Qualität des Codes.

---

## Warum Tests wichtig sind

Ein Test ist nicht nur ein Nachweis, dass etwas funktioniert. Er ist vor allem ein Sicherheitsnetz für zukünftige Änderungen.

Ohne Tests kann eine kleine Änderung leicht unbeabsichtigt andere Verhaltensweisen beeinflussen. Gerade bei Regeln, Berechnungen und Logiksystemen führt dies schnell zu versteckten Fehlern, die erst im Einsatz auffallen. Tests helfen dabei, diese Risiken zu minimieren.

Gute Tests zeichnen sich durch folgende Eigenschaften aus:

- verständlich und klar formuliert
- möglichst klein und fokussiert
- unabhängig von anderen Tests
- robust gegen spätere Refactorings
- auf das tatsächliche Verhalten gerichtet
- nicht nur auf Implementierungsdetails

---

## Typischer Arbeitsablauf

Für die einzelnen Übungen empfiehlt sich dieser Ablauf:

1. Die Anforderung lesen und verstehen.
2. Die erwarteten Ergebnisse definieren.
3. Tests schreiben, die das gewünschte Verhalten dokumentieren.
4. Den Code ausführen und die Fehler analysieren.
5. Die Funktionalität implementieren.
6. Die Tests erneut ausführen.
7. Refactoring durchführen, wenn der Code noch unklar oder redundant ist.
8. Sicherstellen, dass die gesamte relevante Test-Suite weiterhin grün ist.

Dieser Zyklus bildet die Grundlage für sauberes und verantwortungsvolles Coden.

---

## Ziel der Übung

Das Projekt ist als Einstieg in die Welt des testen Lernens gedacht. Es vermittelt die Grundlagen, aber es geht auch darüber hinaus: Es zeigt, dass gute Softwareentwicklung nicht nur aus dem Schreiben von funktionierendem Code besteht, sondern aus dem systematischen Denken über Anforderungen, Randbedingungen, Qualität und langfristige Wartbarkeit.

Die Übungen sind bewusst einfach genug, um die Konzepte zu verstehen, aber realistisch genug, um typische Herausforderungen moderner Softwareentwicklung abzubilden.

Wer dieses Projekt durchläuft, gewinnt nicht nur ein besseres Verständnis für pytest, sondern auch für den professionellen Umgang mit Code, Tests und Änderungen im Verlauf eines Projekts.

---

## Fazit

Dieses Repository dient als praktischer Übungsraum für Python-Entwickler, die ihre Testfähigkeiten verbessern möchten. Es verbindet Theorie und Praxis, indem reale, verständliche Probleme mit klaren Testfällen und sauberem TDD-Workflow kombiniert werden.

Wenn Sie die Grundlagen verstanden haben und regelmäßig mit den Übungen arbeiten, werden Sie schnell merken, dass gut geschriebene Tests nicht nur eine technische Hilfe sind, sondern ein wesentlicher Bestandteil hochwertiger Softwareentwicklung.

---

## Hinweis

Dieses Projekt ist als Lernprojekt konzipiert und eignet sich besonders für Selbststudium, Workshops, Code-Reviews oder den Einstieg in Test-Driven Development mit Python.
=======
# Testing and TDD with Python

Exercises for learning unit testing and test-driven development with [pytest](https://docs.pytest.org).

## Setup

Install [uv](https://docs.astral.sh/uv/), then:

```bash
uv sync
uv run pytest
```

## Layout

| Exercise | Code | Tests |
|---|---|---|
| Exploration (pytest, mocks, fakes) | `src/testing_course/exploration/` | `tests/exploration/` |
| Bowling kata | `src/testing_course/bowling/` | `tests/bowling/` |
| Connect Four (TDD) | `src/testing_course/connect_four/` | `tests/connect_four/` |

## Useful commands

```bash
uv run pytest tests/bowling      # one exercise
uv run pytest -k spare           # tests matching a name
uv run pytest --cov              # coverage
uv run ruff check                # lint
uv run ruff format               # format
uv run ty check                  # type check
uv run connect-four              # play Connect Four
```
>>>>>>> PythonTesting/Vorlesung
