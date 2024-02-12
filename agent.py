from state import State, StateMachine

class IAgent():
    def fire(self, enable):
        ...

class AgentState(State):
    def __init__(self, parentFSN ):
        ...

class AttackState():
    def __init__(self, parentFSN: StateMachine, agent: IAgent):
        super().__init__(parentFSN)
        self.__agent = agent
    def __str__(self):
        return "AttackState"
    def onDoAction(self):
        self.__agent.fire(True)
        #Ajouter code de déplacement ronde et transition si plus d'ennemi

class ScanState():
    def __init__(self, parentFSN: StateMachine, agent: IAgent):
        super().__init__(parentFSN, agent)
        self.__agent = agent
    def __str__(self):
        return "ScanState"
    def onDoAction(self):
        self.__agent.fire(False)
        #Ajouter code de poursuite si ennemi

class SpecialAgent(Agent):
    def __init__(self, playerID=""):
        super().__init__(playerID)
        self.__fsm = StateMachine(None)
        self.__fsm.setState(ScanState(self.__fsm, self))
    
    def onUpdate(self):
        self.__fsm.doAction()