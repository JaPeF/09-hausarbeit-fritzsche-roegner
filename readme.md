[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/T2iLlfUP)
---
title: Webprogrammierung Hausarbeit
author: Niklas Klein
date: 30.11.2025
lang: de-DE
---

# Hausarbeit als Prüfungsleistung WiSe 2025/2026

**Achtung: Dies ist eine Gruppenhausarbeit.**

Bitte lest den gesamten Text aufmerksam durch, bevor ihr mit der Aufgabe beginnt. Bei Fragen wendet euch bitte im Discord oder im Labor an mich.

## Abgabefrist

**Abgabe bis zum 05.01.2026 um 23:59:59.99999**

## Aufgabe

Entwickelt eine Buch-Datenbank-Anwendung mit Python und Django. Die Anwendung soll es Nutzern ermöglichen, Informationen über Bücher, Autor:innen und Verlage zu verwalten. Zusätzlich sollen Nutzer Bücher durchsuchen und filtern können. Schließlich soll ein eigenes, von euch erdachtes Feature implementiert werden, das die Anwendung erweitert und die Benutzererfahrung verbessert.

Die Studierenden von Gründung, Innovation, Entwicklung (GIE) können freiwillig diese Aufgabenstellung wählen. Alternativ können die Studierenden der GIE die mir bereits mitgeteilten individuellen Aufgaben umsetzen, müssen dabei aber alle Kapitel dieses Dokuments beachten, bis auf die Funktionalen Anforderungen, die aber als Orientierung dienen können.

## Bewertungskriterien

- **60 %** der Note ergeben sich aus der **Erfüllung der funktionalen Anforderungen**.
- **20 %** der Note ergeben sich aus der **Einhaltung der nicht-funktionalen Anforderungen**.
- **20 %** der Note ergeben sich aus der **Präsentation der Ergebnisse**.



## Funktionale Anforderungen (60 Punkte)

Die folgenden Funktionalen Anforderungen gelten für die Studierenden der Angewandten Informatik (AI) und die Studierenden von Gründung, Innovation, Entwicklung (GIE), sofern die Studierenden aus GIE freiwillig diese Aufgabenstellung wählen.

Alternativ können die Studierenden aus GIE die mir bereits mitgeteilten individuellen Funktionalen Anforderungen umsetzen. Alle übrigen Kapitel gelten für alle Studierendengruppen.

### 1. Kern-CRUD-Operationen (20 Punkte)

Implementiert die vollständigen CRUD-Funktionen (Erstellen, Anzeigen, Aktualisieren, Löschen) für die folgenden Modelle:

- **Buch**
  - Felder: Titel, Veröffentlichungsdatum, Genre, Beschreibung.
- **Autor**
  - Felder: Vorname, Nachname, Geburtsdatum, Biografie.
- **Verlag**
  - Felder: Name, Gründungsjahr, Sitz, Beschreibung.
- **Rezension**
  - Felder: Buch (ForeignKey), Rezensent (Pseudonym), Bewertung (z.B. 1 bis 5 Sterne), Kommentar, Datum.

**Hinweise:**

- Die CRUD-Funktionen sollen über benutzerfreundliche Webseiten zugänglich sein (nicht über das Django-Admin-Interface).
- Stellt sicher, dass Nutzer Rezensionen zu Büchern hinzufügen können.

### 2. Komplexe Beziehungen (15 Punkte)

- Modelliert die Beziehungen zwischen Büchern, Autor:innen und Verlagen korrekt:

  - **Viele-zu-Viele-Beziehung** zwischen Büchern und Autor:innen.
    - Ein Buch kann mehrere Autor:innen haben.
    - Eine Autorin / ein Autor kann mehrere Bücher geschrieben haben.
  - **Eins-zu-Viele-Beziehung** zwischen Verlagen und Büchern.
    - Ein Buch hat einen Verlag.
    - Ein Verlag kann mehrere Bücher verlegen.

- Erstellt Ansichten, die diese Beziehungen darstellen:
  - Seite, die alle Bücher einer bestimmten Autorin / eines bestimmten Autors anzeigt.
  - Seite, die alle Autor:innen zu einem bestimmten Buch anzeigt.
  - Seite, die alle Bücher eines Verlags anzeigt.
- Ermöglicht die Navigation zwischen diesen Ansichten (z.B. von der Buchseite zu den Autor:innen und zum Verlag).

### 3. Such- und Filterfunktionalität (15 Punkte)

- Implementiert eine **Suchfunktion**, mit der Nutzer nach Büchern suchen können basierend auf:
  - Titel
  - Genre
  - Autor:in
  - Verlag
- Implementiert **Filteroptionen**, um Bücher einzugrenzen:
  - Veröffentlichungsjahr (Zeitraum)
  - Durchschnittliche Bewertung
- **Kreative Erweiterung:** Ihr könnt zusätzliche Filter hinzufügen, z.B. nach Seitenzahl, Sprache, etc.

### 4. Eigenes Feature (10 Punkte)

- **Anforderung:** Implementiert mindestens ein einzigartiges Feature, das die Benutzererfahrung verbessert.
- **Beispiele:**
  - **Benutzer-Leseliste:**
    - Nutzer können Bücher zu einer persönlichen Leseliste hinzufügen.
    - Anzeigen der Leseliste auf der Profilseite des Nutzers.
  - **Empfehlungssystem:**
    - Bietet personalisierte Buchempfehlungen basierend auf bevorzugten Genres oder zuvor bewerteten Büchern an.
  - **Kommentarfunktion:**
    - Erlaubt Nutzern, Kommentare zu Autor:innen zu hinterlassen.
    - Implementiert Diskussionsforen oder Kommentar-Threads.
- **Hinweis:** Beschreibt in eurer Präsentation, welches Feature ihr implementiert habt und warum ihr euch dafür entschieden habt.



## Nicht-funktionale Anforderungen (20 Punkte)

1. **Verwendung von Python und Django** (Pflicht)
   - Die Anwendung muss mit Python und Django umgesetzt werden.
   - JavaScript kann optional für verbesserte Benutzeroberflächen verwendet werden, aber die Kernfunktionalität soll serverseitig in Django implementiert sein.

2. **Klassenbasierte Views** (2 Punkte)
   - Nutzt, wo sinnvoll, klassenbasierte Views (`Class-Based Views`).

3. **Fehlerbehandlung** (2 Punkte)
   - Bei Aufrufen von URLs mit nicht vorhandenen IDs soll eine benutzerfreundliche 404-Fehlerseite angezeigt werden.

4. **Projektstruktur** (2 Punkte)
   - Organisiert euer Projekt in einer üblichen und sinnvollen Struktur.
   - Verwendet mindestens eine eigene Django-App (`python manage.py startapp ...`).

5. **Dokumentation und Kommentare** (2 Punkte)
   - Funktionen, Klassen und Module sollen mit aussagekräftigen Kommentaren und Docstrings versehen sein.
   - Verwendet den PEP 257 Style Guide für Docstrings.

6. **Templates** (2 Punkte)
   - Verwendet ein Basis-Template und nutze Template-Blöcke (`{% block content %}{% endblock %}`) für wiederkehrende Elemente.

7. **Abhängigkeiten** (2 Punkte)
   - Verwaltet eure Abhängigkeiten mit einer `requirements.txt`-Datei oder mit `uv`.

8. **Benutzeroberfläche** (2 Punkte)
   - Die Anwendung soll optisch ansprechend sein.
   - Ihr könnt CSS-Frameworks wie Bootstrap oder Tailwind CSS verwenden.

9. **Code-Qualität** (4 Punkte)
   - Vermeidet Code-Duplikationen.
   - Verwendet sinnvolle und aussagekräftige Variablen- und Funktionsnamen.
   - Entfernt ungenutzte Importe und unnötigen Code.
   - Haltet euch an den PEP 8 Style Guide für sauberen und lesbaren Code.



## Präsentation der Ergebnisse (20 Punkte)

Stellt eure Anwendung im Labor in der ersten Januarwoche (05.01. bzw. 09.01.) vor (15-20 Minuten). **Alle Gruppenmitglieder** sollen an der Präsentation beteiligt sein. Die Präsentation kann auch über Discord erfolgen.

### Bewertungsrichtlinien:

- **Einhaltung des Zeitrahmens** (5 Punkte)
  - Die Präsentation sollte zwischen 15 und 20 Minuten dauern.
- **Demonstration der implementierten Funktionen** (5 Punkte)
  - Zeigt die Kernfunktionen eurer Anwendung.
- **Erklärung der gewählten Lösungen und Herausforderungen** (5 Punkte)
  - Diskutiert eure Herangehensweise und eventuelle Probleme, die ihr gelöst habt.
- **Vorstellung des eigenen Features** (5 Punkte)
  - Präsentiert euer einzigartiges Feature und erläutert, warum ihr euch dafür entschieden habt.



## Bildung der Note aus den Punkten

| Prozent (Punkte) | Note                 |
|------------------|----------------------|
| 100 - 94 %       | 1,0 (sehr gut)       |
| <94 - 89 %       | 1,3 (sehr gut -)     |
| <89 - 84 %       | 1,7 (gut +)          |
| <84 - 79 %       | 2,0 (gut)            |
| <79 - 73 %       | 2,3 (gut -)          |
| <73 - 68 %       | 2,7 (befriedigend +) |
| <68 - 63 %       | 3,0 (befriedigend)   |
| <63 - 57 %       | 3,3 (befriedigend -) |
| <57 - 52 %       | 3,7 (ausreichend +)  |
| <52 - 50 %       | 4,0 (ausreichend)    |
| <50 %            | 5,0 (nicht bestanden)|



## Hinweise zur Umsetzung und Bewertung

### Hinweis zu Prüfungsrecht und Hilfsmitteln

Für diese Hausarbeit gelten die Regelungen des § 19 der Prüfungsverfahrensordnung der Hochschule Flensburg (siehe: [https://hs-flensburg.de/satzung/a/PVO_Lesefassung2025.pdf](https://hs-flensburg.de/satzung/a/PVO_Lesefassung2025.pdf)). Die Hausarbeit ist von eurer Gruppe eigenständig zu erbringen.

**Nicht zugelassene Hilfsmittel sind insbesondere:**

* der Einsatz von Systemen Künstlicher Intelligenz (z.B. Chatbots, Code-Generatoren, „Agents“ usw.) zur Erstellung oder Überarbeitung von Code, Texten oder Konzepten, die unmittelbar in die Abgabe einfließen,
* die Unterstützung durch Dritte, z.B. beauftragte externe Programmierer:innen oder andere Personen, die maßgeblich an der Lösung mitwirken.

Die Nutzung von KI-Systemen als **Tutor** ist zulässig, z.B. um sich Konzepte erklären zu lassen, Verständnisfragen zu stellen oder Fehlermeldungen erläutern zu lassen. Unzulässig ist es jedoch, sich von KI-Systemen direkt den abzugebenden Code, fertige Textpassagen oder vollständige Lösungsteile erzeugen zu lassen und diese (ganz oder im Wesentlichen) in die eigene Abgabe zu übernehmen.

Sollte der abgegebene Code einer Gruppe den begründeten Verdacht nahelegen, dass er nicht (vollständig) von den Gruppenmitgliedern selbst erstellt wurde, behalte ich mir vor, mit einzelnen oder allen Gruppenmitgliedern eine zusätzliche mündliche Prüfung zur Klärung der Eigenleistung durchzuführen.


### Zusammenarbeit und individuelle Beiträge

- **Git und Versionskontrolle**
  - Nutzt Git zur Versionskontrolle eures Projekts.
  - Achtet auf aussagekräftige Commit-Nachrichten.
  - Die Git-Historie wird zur Bewertung der individuellen Beiträge herangezogen. Daher auch individuell eure kleineren Arbeitsschritte committen, nicht alles am als ein großer Commit am Ende von einem Gruppenmitglied.

- **Individuelle Leistung**
  - Sollte die Leistung innerhalb der Gruppe ungleich verteilt sein, besteht Anspruch auf eine individuelle Benotung.
  - Individuelle Beiträge können anhand von Git-Commits, Beteiligung an der Präsentation und Rückmeldungen der Teammitglieder beurteilt werden.

- **Problemlösung innerhalb der Gruppe**
  - Versucht zunächst, eventuelle Probleme innerhalb der Gruppe einvernehmlich zu lösen.
  - Wenn keine Einigung erzielt werden kann, wendet euch frühzeitig an mich (niklas.klein@hs-flensburg.de).

### Abgabe

- **Deadline einhalten**
  - Die Abgabe erfolgt bis zum 05.01.2025 um 23:59:59.99999.
  - Verspätete Abgaben können nicht berücksichtigt werden.

- **Abgabeformat**
  - Reicht die Abgabe über GitHub Classroom ein.
  - Verwendet eine `.gitignore`-Datei, um Umgebungsdateien (z.B. `.venv`) und unnötige Dateien vom Upload auszuschließen.

### Unterstützung und Ressourcen

- **Fragen und Hilfe**
  - Bei Fragen oder Problemen nutzt den Discord-Server oder sprecht mich im Labor an.
  - Zögert nicht, Hilfe zu suchen, wenn ihr nicht weiterkommt.

- **Ressourcen**
  - Offizielle Django-Dokumentation: https://docs.djangoproject.com/
  - PEP 8 Style Guide: https://www.python.org/dev/peps/pep-0008/
  - PEP 257 Docstring Conventions: https://www.python.org/dev/peps/pep-0257/



## Ich wünsche euch viel Erfolg!

Nutzt diese Aufgabe als Gelegenheit, eure Fähigkeiten in Python und Django zu vertiefen und kreativ zu sein. Ich freue mich auf eure innovativen und gut durchdachten Lösungen!
