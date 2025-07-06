# Mixcloud Integration für Home Assistant

**Features:**
- Mixcloud-User-Statistiken als Sensoren (Follower, Uploads, letzte Veröffentlichung etc.)
- Einfache Einrichtung via Config Flow (Benutzername oder URL)
- HACS-kompatibel

## Installation

1. Repository klonen oder als ZIP herunterladen, entpacken.
2. Ordner `custom_components/mixcloud` in deinen Home Assistant `custom_components`-Ordner kopieren.
3. Home Assistant neu starten.
4. Integration im UI hinzufügen: **Einstellungen → Geräte & Dienste → Integration hinzufügen → Mixcloud**.

## Konfiguration

Einfach Benutzername oder vollständige Mixcloud-Profil-URL eingeben.

## Sensors

- **Follower**: Aktuelle Follower-Zahl
- **Uploads**: Anzahl der Uploads
- **Letzte Veröffentlichung**: Name & Details der letzten Veröffentlichung

**Weitere Sensoren einfach ergänzbar.**

---

### HACS-Setup

- Repository als benutzerdefiniertes Repository hinzufügen (`HACS → Integrationen → Benutzerdefiniertes Repository`).

---

## Lizenz

MIT