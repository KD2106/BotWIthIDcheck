import sqlite3
from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker, FormValidationAction
from rasa_sdk.executor import CollectingDispatcher

conn = sqlite3.connect('student.db')


class ValidateIdForm(FormValidationAction):

     def name(self) -> Text:
         return "validate_id_form"

     def validate_idno(self, slot_value: Any, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> Dict[Text, Any]:
        '''
        if len(slot_value) != 5:
            dispatcher.utter_message(text="Invalid id!")
            return {"idno": None}

        elif len(slot_value) == 5:
            dispatcher.utter_message(text="Valid id!")
            return {"idno": slot_value}
        '''
        c = conn.cursor()
        c.execute("SELECT * FROM students WHERE idno = :idno", {"idno": slot_value})
        a = c.fetchall()
        
        if a == []:
            dispatcher.utter_message(text="Invalid id!")
            return {"idno": None}
        else:
            dispatcher.utter_message(text="Valid id!")
            return {"idno": slot_value}

