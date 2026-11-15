# Playwright avec Python et Pytest

Projet d'apprentissage accompagné de la playlist YouTube [Playwright with Python And Pytest](https://www.youtube.com/playlist?list=PLUDwpEzHYYLtFprdVOrMLBJcqCJ-gRDYa). Il rassemble des exemples progressifs de tests web automatisés avec Python, Playwright et Pytest.

## Contenu du projet

Les exemples locaux couvrent actuellement les deux premières sessions :

| Dossier | Notions pratiquees |
| --- | --- |
| `Setup Environment & Writing Tests (Session 1)` | Premiers tests Pytest avec Playwright : navigation vers le Demo Web Shop, vérification de l'URL et du titre de la page. |
| `Playwright Built-In Locators (Session 2)` | Localisation d'éléments avec `get_by_text()` et vérification de leur visibilité. |

La playlist sert de support de cours et va plus loin que les exemples présents dans ce dépôt. Elle aborde notamment les locators, les tests pilotés par les données, la capture de vidéos et de traces, les tests instables et la génération de rapports. Ces sujets ne sont pas tous implémentés dans le projet actuel.

Les tests utilisent le site de démonstration [demowebshop.tricentis.com](https://demowebshop.tricentis.com/).

## Prérequis

- Python installé et accessible depuis PowerShell (`python`).
- Windows PowerShell pour les commandes ci-dessous.
- Les navigateurs gérés par Playwright, installés à l'étape de configuration.

## Installation

Depuis la racine du dépôt :

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m playwright install chromium firefox
```

Le fichier `requirements.txt` fixe les versions de Playwright, Pytest et de ses plugins.

## Exécuter les tests

Lancer tous les tests en mode headless :

```powershell
python -m pytest -v
```

Exécuter un fichier de test avec un navigateur spécifique :

```powershell
python -m pytest "Setup Environment & Writing Tests (Session 1)\test_playwright.py" --browser chromium -v
python -m pytest "Playwright Built-In Locators (Session 2)\test_locators.py" --browser firefox -v
```

Ajouter `--headed` pour afficher le navigateur pendant l'exécution. Pour lister les tests collectés sans les exécuter :

```powershell
python -m pytest --collect-only -q
```

## Structure

```text
.
|-- Setup Environment & Writing Tests (Session 1)/
|   |-- notes.txt
|   `-- test_playwright.py
|-- Playwright Built-In Locators (Session 2)/
|   |-- cmd.txt
|   `-- test_locators.py
`-- requirements.txt
```

## Dependances principales

- `playwright` : automatisation du navigateur.
- `pytest` : découverte et exécution des tests.
- `pytest-playwright` : fixtures et options Pytest pour Playwright.
- `pytest-xdist` : exécution parallèle des tests avec `-n auto`.
