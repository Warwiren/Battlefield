class State:
    def __init__(self, stateMachine: 'StateMachine') -> None:
        self.__stateMachine = stateMachine
    def doAction(self):
        """to be overriden"""
        ...
    def onLeave(self):
        ...
    def onEnter(self):
        ...

class StateMachine:
    def __init__(self) -> None:
        #On instancie l'ordre en cours ici (par défaut 'patrol')
        # + privatisation
        self.__actualState = None
    def doAction(self):
        # on veut pouvoir changer entre patrol et attack ici
        if self.__actualState != None:
            self.__actualState.doAction()
    def setState(self, newState: State):
        print("Changing state from", self.__state,"to", newState)
        self.__actualState = newState

class ScanState:
    # setState
     def doAction(self):
        ...

class AttackState:
     def doAction(self):
        ...