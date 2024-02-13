from state import State, StateMachine, ScanState
import j2l.pytactx.agent as pytactx
from getpass import getpass
# from attackState import AttackState
"""Classes pour un Agent, évité les répétitions"""


class IAgent():

  def fire(self, enable):
    ...


class AgentState(State):

  def __init__(self, parentFSN):
    ...


""" *********************************** """


#Agent add
class SpecialAgent:

  def __init__(self, playerID=""):
    self.__agent = pytactx.Agent(playerID,
                                 arena="LaTerreDuMilieu",
                                 username="demo",
                                 password=getpass("🔑 password: "),
                                 server="mqtt.jusdeliens.com",
                                 verbosity=2)
    self.__fsm = StateMachine(None)
    self.__fsm.setState(ScanState(self.__fsm, self.__agent))

  def update(self):
    self.__agent.update()
    self.__fsm.doAction()
