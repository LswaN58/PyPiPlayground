# Set up path
# import os
# import sys
# from pathlib import Path
# sys.path.insert(0, str(Path(os.getcwd()) / "src"))
# print(f"Updated path: {sys.path[:5]}...")

import unittest
from unittest import TestCase
from src.packer.players.Love import Love

class test_Give(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print("Set up test_Give class.")

    @classmethod
    def tearDownClass(cls) -> None:
        print("Tore down test_Give class.")

    def test_give_left(self):
        print("   Testing Give...")
        Love.Give()
        print("   Done.")