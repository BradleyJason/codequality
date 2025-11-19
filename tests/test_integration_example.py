import os
import sys

# Ajout du dossier parent (là où se trouve app.py) au PYTHONPATH
CURRENT_DIR = os.path.dirname(__file__)
PARENT_DIR = os.path.dirname(CURRENT_DIR)
sys.path.append(PARENT_DIR)


import pytest
from app import app, items  # app = instance Flask, items = liste en mémoire


@pytest.fixture
def client():
    """Client de test Flask, avec liste `items` vidée avant/après chaque test."""
    app.config["TESTING"] = True

    with app.test_client() as client:
        # Avant le test : on part d'une liste vide
        items.clear()
        yield client
        # Après le test : on nettoie (par sécurité)
        items.clear()


def test_index_returns_200(client):
    """Le endpoint GET / doit répondre 200."""
    response = client.get("/")
    assert response.status_code == 200


def test_add_item_persists_and_shows_item(client):
    """POST /add doit ajouter un item et le rendre visible sur la page d'accueil."""
    response = client.post(
        "/add",
        data={"item": "Milk"},
        follow_redirects=True,  # suit le redirect vers "/"
    )

    # La requête finale doit être OK
    assert response.status_code == 200

    # La page devrait contenir le texte "Milk" (affiché via le template index.html)
    assert b"Milk" in response.data
