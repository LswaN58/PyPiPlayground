"""Simple test module for importing from another file within a package
"""
from packer.players.Dillon import Dillon
from packer.players.historical.Green import Green

class Love:
    @staticmethod
    def Give(player:str):
        if player.upper() == "DILLON":
            Dillon.Handoff(left=True)
        elif player.upper() == "GREEN":
            Green.Handoff(left=False)
