# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"
import random
import linecache

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker, FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet, EventType
from rasa_sdk.types import DomainDict

ALLOWED_TEMAS=[
    "sistema solar",
    "tierra",
    "luna"
]

ALLOWED_NIVELES=[ "principiante", "medio", "avanzado" ]

class ActionTemaElegido(Action):

    def name(self) -> Text:
        return "action_tema_elegido"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        for entidades in tracker.latest_message['entities']:
            if entidades['entity'] == 'tema':
                tema_elegido=entidades['value'].lower()
                if tema_elegido in ALLOWED_TEMAS:
                    dispatcher.utter_message(text=f"Has elegido el tema {tema_elegido}")
                    return[SlotSet("tema",tema_elegido)]
                else:
                    dispatcher.utter_message(text=f"Todavía no tenemos información de {tema_elegido}, por favor elija otro.")
                    return[SlotSet("tema",None)]


class ActionPregPrincipiante(Action):

    def name(self) -> Text:
        return "action_preguntas_principiante"

    '''def num_preg_seleccionada(self):
        with open('./preg_principiante.txt') as myfile:
                total_lineas = sum(1 for line in myfile)
        total_preguntas=total_lineas/5
        n_aleatorio=random.randint(1,total_preguntas)
        n_preg=(n_aleatorio-1)*5+1
        return(n_preg)
'''
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
            with open('./preg_principiante.txt') as myfile:
                total_lineas = sum(1 for line in myfile)
            total_preguntas=total_lineas/5
            n_aleatorio=random.randint(1,total_preguntas)
            n_preg_seleccionada=(n_aleatorio-1)*5+1
            '''n_preg_seleccionada = self.num_preg_seleccionada()'''
            preg_seleccionada=linecache.getline('preg_principiante.txt',n_preg_seleccionada)
            resp1=linecache.getline('preg_principiante.txt',1+n_preg_seleccionada)
            resp2=linecache.getline('preg_principiante.txt',2+n_preg_seleccionada)
            resp3=linecache.getline('preg_principiante.txt',3+n_preg_seleccionada)
            solucion=linecache.getline('preg_principiante.txt',4+n_preg_seleccionada)
            dispatcher.utter_message(text=preg_seleccionada, buttons = [
                            {"payload":resp1,"title":resp1},
                            {"payload":resp2,"title":resp2},
                            {"payload":resp3,"title":resp3},
                        ])
            n_preguntas_seguidas=tracker.get_slot("preguntas_seguidas")
            n_preguntas_seguidas=n_preguntas_seguidas+1

            return[SlotSet("n_pregunta",n_aleatorio),SlotSet("preguntas_seguidas",n_preguntas_seguidas)]

class ActionComprobarRespuesta(Action):

    def name(self) -> Text:
        return "action_comprobar_respuesta"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
            n_preg_seleccionada=tracker.get_slot("n_pregunta")
            numero_correctos=tracker.get_slot("n_correctos")
            resp_correcta=linecache.getline('resp_principiante.txt',n_preg_seleccionada)

            user_respuesta=str(tracker.latest_message['text'])
            n_linea_solucion=((n_preg_seleccionada-1)*5+1)+4
            if user_respuesta.lower() in resp_correcta.lower():
                numero_correctos=numero_correctos+1
                dispatcher.utter_message(text="Enhorabuena, has elegido la respuesta correcta.")
            else:
                solucion=linecache.getline('preg_principiante.txt',n_linea_solucion)
                dispatcher.utter_message(text="Oh no, esa no era la respuesta correcta. ")
                dispatcher.utter_message(text=solucion)
            '''dispatcher.utter_message(text=user_respuesta)
                dispatcher.utter_message(text=resp_correcta)'''
            return[SlotSet("n_correctos",numero_correctos)] 

class ActionNota(Action):

    def name(self) -> Text:
        return "action_nota"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
            n_total_preg=tracker.get_slot("preguntas_seguidas")
            n_resp_correctas=tracker.get_slot("n_correctos")

            nota=n_resp_correctas/n_total_preg
            dispatcher.utter_message(text=f"Has obtenido {n_resp_correctas} aciertos de {n_total_preg}.")
            if nota == 1:
                dispatcher.utter_message(text="Enhorabuena, ¡estás en racha de aciertos! ")
            elif nota >= 0.5:
                dispatcher.utter_message(text=f"Muy bien, has superado la prueba, ¡pero practica más para obtener un 100% de aciertos! ")
            else:
                dispatcher.utter_message(text="¡Oh no...no has superado la prueba, deberías de estudiar más. ")

            return[SlotSet("n_pregunta",0),SlotSet("preguntas_seguidas",0),SlotSet("n_correctos",0)]






'''    
        if tracker.get_intent_of_latest_message()=="elegir_tema":
            f=open('tierra.txt','r')
        elif tracker.get_intent_of_latest_message()=="aprender_sistemasolar":
            f=open('sistemasolar.txt','r')
        
        mensaje=f.read()
        f.close()'''


'''
        tema_elegido=tracker.get_slot("tema")
        if tema_elegido.lower() in ALLOWED_TEMAS:
            message:"Has elegido el tema {tema_elegido}."
            dispatcher.utter_message(text=mensaje)
            return[]
        elif tema_elegido.lower() not in ALLOWED_TEMAS:
            message="No tenemos información de {tema_elegido} todavía, elija otro tema."
            dispatcher.utter_message(text=mensaje)
            return []'''

        

'''class ActionValidateTema(FormValidationAction):

    def name(self) -> Text:
        return "validate_tema_form"

    def validate_tema(
        self, 
        slot_value: Any, 
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]: 

        if slot_value.lower() not in ALLOWED_TEMAS:
            dispatcher.utter_message(text="No tenemos información de {slot_value} todavía, elija otro tema.")
            return {"tema":None}
        dispatcher.utter_message(text="Ok, has elegido el tema de {slot_value}.")
        return {"tema": slot_value}'''
        
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
'''class ActionExplicarTierra(Action):

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

        return []'''
