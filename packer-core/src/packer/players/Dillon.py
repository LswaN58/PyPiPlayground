"""Simple module whose function can be imported in another package.
"""
from importlib.resources import files

class Dillon:

    @staticmethod
    def Handoff(left:bool):
        if left:
            print("Dillon takes the handoff to the left.")
        else:
            print("Dillon takes the handoff to the right.")

    @staticmethod
    def Stats():
        stats_text = files("packer").joinpath("DillonStats.txt").read_text()
        print(f"Stats for AJ Dillon:\n{stats_text}")