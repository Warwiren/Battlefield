Projet python test (premier essai)

Owner : CDA2_student

status : fail

installation :

utiliser les fichiers main.py / state.py / stateMachine.py -> dans replit.com

error:

Traceback (most recent call last):
File "main.py", line 3, in <module>
agent = SpecialAgent("Killian")
File "/home/runner/terre-du-milieu/stateMachine.py", line 34, in **init**
self.**fsm.setState(ScanState(self.**fsm, self.**agent))
File "/home/runner/terre-du-milieu/state.py", line 23, in setState
print("Changing state from", self.**state,"to", newState)
AttributeError: 'StateMachine' object has no attribute '\_StateMachine**state'. Did you mean: '\_StateMachine**actualState'?

#Diagramme de classe

![diagramme classe](./svg/classe.png)

#Diagramme de séquence

![diagramme séquence](./svg/sequence.png)
