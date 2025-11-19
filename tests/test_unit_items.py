import os
import sys

# Ajout du dossier parent (là où se trouve app.py) au PYTHONPATH
CURRENT_DIR = os.path.dirname(__file__)
PARENT_DIR = os.path.dirname(CURRENT_DIR)
sys.path.append(PARENT_DIR)

from app import is_valid_item

def test_is_valid_item_accepts_normal_string():
    assert is_valid_item("Milk")
    assert is_valid_item("Buy eggs")


def test_is_valid_item_rejects_empty_or_whitespace():
    assert not is_valid_item("")
    assert not is_valid_item("   ")


def test_is_valid_item_rejects_none():
    assert not is_valid_item(None)
