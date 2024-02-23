import pytest
from src.JSONSaver import JSONSaver
import os
from config import ROOT

file = os.path.join(ROOT, 'data', 'hh.json')


def test_get_vacancy():
    assert JSONSaver.get_vacancy(file) == {}