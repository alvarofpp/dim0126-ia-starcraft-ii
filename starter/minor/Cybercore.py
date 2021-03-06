from sc2.constants import PYLON, GATEWAY, CYBERNETICSCORE
from model.ModuleModel import *


class Cybercore(ModuleModel):
    def __init__(self, number):
        super().__init__()
        self.ready = 0
        self.target = number

    async def condition(self, bot):
        pass
        
    async def run(self, bot):
        if self.ready < self.target and not bot.already_pending(CYBERNETICSCORE) and bot.units(GATEWAY).ready.exists:
            pylons = bot.units(PYLON).ready
            if pylons.exists and bot.can_afford(CYBERNETICSCORE): 
                await bot.build(CYBERNETICSCORE, near=pylons.random)
                self.ready += 1
