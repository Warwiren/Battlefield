class Agent:
    def __init__(self, x:int, y:int) -> None:
        # instancier =>
        self.__x = x
        # Convention pour 'privatisé' (bonne pratique) -> seulement accessible depuis la classe sauf si on utilise un Getter
        self.__y = y
    def onUpdate(self):
        # A surcharger dans la classe fille pour des extensions de update
        ...
    def beforeUpdate(self):
        ...
    def afterUpdate(self):
        ...
    def update(self):
        self.beforeUpdate()
        print("j'exécute le update de mon Agent")
        self.afterUpdate()
        ...

class DroneAgent(Agent):
    def __init__(self, x:int, y:int) -> None:
        super().__init__(x,y)
    def update(self):
        return super().update()
        print("j'ai overriden ma methode update de Agent")

class RobotAgent(Agent):
    def __init__(self, x:int, y:int) -> None:
        pass
    def update(self):
        pass

class Battlefield:
    def __init__(self, agents:list[Agent]) -> None:
        self.__agents = agents
    def update(self):
        for agent in self.__agents:
            agent.update()

monBattlefield = Battlefield([DroneAgent(0,0), RobotAgent(10,10)])
monBattlefield.update()

monAgent = DroneAgent(10,10)
monAgent.update()