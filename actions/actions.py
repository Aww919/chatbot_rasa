# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet


"""class ActionNombre(Action):

    def name(self) -> Text:
        return "action_nombre"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        #nombre_usuario=tracker.get_slot("nombre")
        nombre_usuario=next(tracker.get_latest_entity_values("nombre"),None)

        if (any(chr.isdigit() for chr in nombre_usuario)):
            mensaje="El nombre introducido no es correcto. Compruébelo."
            dispatcher.utter_message(text=mensaje)
            return[]
        else:
            mensaje="Tu nombre es {nombre_usuario}"
            dispatcher.utter_message(text=mensaje)

        return [SlotSet("nombre",nombre_usuario)]
"""
class ActionExplicarTierra(Action):

    def name(self) -> Text:
        return "action_tierra"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        
        if tracker.get_intent_of_latest_message()=="aprender_tierra":
            f=open('tierra.txt','r')
        elif tracker.get_intent_of_latest_message()=="aprender_sistemasolar":
            f=open('sistemasolar.txt','r')
        
        mensaje=f.read()
        f.close()

        dispatcher.utter_message(text=mensaje)

        return []
