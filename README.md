# Kylogger

Ce code est un keylogger basique écrit en Python. Il utilise la bibliothèque pynput pour surveiller les frappes sur le clavier.
Lorsqu'une touche est pressée, la fonction on_press est déclenchée. Cette fonction enregistre la touche pressée dans une liste et incrémente un compteur. Lorsque le compteur atteint un certain seuil (dans ce cas, 10), il envoie un e-mail contenant les touches enregistrées sous forme de message, ainsi qu'une capture d'écran du moment où ces touches ont été enregistrées.



La fonction email(keys) rassemble les touches enregistrées dans un format lisible et lance l'envoi de l'e-mail avec cette information ainsi que la capture d'écran.



Le programme continue à enregistrer les frappes jusqu'à ce que la touche "Esc" soit pressée, moment où il se termine.

