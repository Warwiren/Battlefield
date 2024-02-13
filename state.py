class State:
  def __init__(self, stateMachine: 'StateMachine') -> None:
      self._parent = stateMachine
  def doAction(self):
      """to be overriden"""
      ...
  def onLeave(self):
      ...
  def onEnter(self):
      ...

class StateMachine:
  def __init__(self, state: "State") -> None:
      #On instancie l'ordre en cours ici (par défaut 'patrol')
      # + privatisation
      self.__actualState = state
  def doAction(self):
      # on veut pouvoir changer entre patrol et attack ici
      if self.__actualState != None:
          self.__actualState.doAction()
        
  def setState(self, newState: State):
      print("Changing state from", self.__state,"to", newState)
      self.__actualState = newState

class AttackState(State):
  def __init__(self, parentFSN: StateMachine, agent):
    super().__init__(parentFSN)
    self.__agent = agent
    self.__xEnemy = 0
    self.__yEnemy = 0
  def __str__(self):
    return "AttackState"

  def doAction(self):
    # if self.__agent.distance == 0:
    if len(self.__agent.range) != 0:
      for enemyName, enemyAttributes in self.__agent.range.items():
        self.__xEnemy,self.__yEnemy = enemyAttributes['x'], enemyAttributes['y']
        break
    if self._agent.x == self.__xEnemy and self._agent.y == self.__yEnemy:
      self._parent.setState(ScanState(self._parent, self.__agent))
      return
    self.__agent.fire(True)
    self.__agent.move(0,0)
    self.__agent.setColor(255, 0, 0)

class ScanState(State):
  def __init__(self, parentFSN: StateMachine, agent):
      super().__init__(parentFSN)
      self.__agent = agent
      self.__cp = [(4, 4), (4, 14), (14, 14), (14, 4)]
      self.__icp = 0

  def __str__(self):
      return "ScanState"

  def doAction(self):
    if self.__agent.distance != 0:
      self._parent.setState(
        self._parent.setState(AttackState(self._parent, self.__agent))
      )
      return
    self.__agent.setColor(0,255,128)
    self.__agent.fire(False)
    cpx,cpy = self.__cp[self.__icp]
    if self.__agent.x == cpx and self.__agent.y == cpy:
      self.__icp = (self._icp+1)%len(self.__cp)
    self.__agent.moveTowards(cpx,cpy)
