# Set up path
# import os
# import sys
# from pathlib import Path
# sys.path.insert(0, str(Path(os.getcwd()) / "src"))
# print(f"Updated path: {sys.path[:5]}...")

import unittest
from unittest import TestCase
# import src.packer.Dillon
from src.packer.Dillon import Dillon

class test_Handoff(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print("Set up test_Handoff class.")

    @classmethod
    def tearDownClass(cls) -> None:
        print("Tore down test_Handoff class.")

    def test_Handoff_left(self):
        Dillon.Handoff(left=True)
        print("Tested Handoff Left")

    def test_Handoff_righ5(self):
        Dillon.Handoff(left=False)
        print("Tested Handoff Right")
