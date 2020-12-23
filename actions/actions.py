# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/
#
# This is a simple example for a custom action which utters "Hello World!"
from typing import Any, Text, Dict, List, Union
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction
from rasa_sdk import Action, Tracker
from rasa_sdk.events import (
    SlotSet, UserUtteranceReverted, ConversationPaused, EventType, FollowupAction)
import joblib
import pandas as pd
import numpy as np
from .classifier_check import Classifier_check
# from rasa_sdk.events import SlotSet


class ActionSizeForm(FormAction):
    def name(self) -> Text:

        return "size_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Dict[Text, Any]]:
        return ["chest", "height", "weight"]

    def slot_mappings(self) -> [Dict[Text, Any]]:
        return{
            "chest": self.from_entity(entity="chest", intent="chest_entry"),
            "height": self.from_entity(entity="height", intent="height_entry"),
            "weight": self.from_entity(entity="weight", intent="weight_entry"),
        }

    def submit(self, dispatcher: CollectingDispatcher,
               tracker: Tracker,
               domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        c = tracker.get_slot("chest")
        h = tracker.get_slot("height")
        w = tracker.get_slot("weight")

        chest = int(c[0])
        height = int(h[0])
        weight = int(w[0])

        # read in model
        model = joblib.load("actions\model_joblib.joblib")

        age = 28
        bustSize1 = chest
        bust1 = chest
        size = 14
        heightCM = height
        weightLbs = weight

        recommended_size = Classifier_check().recommend_size(chest)

        xnew = [[age, bustSize1, bust1, size, heightCM, weightLbs]]
        bodytypenumber = model.predict(xnew)
        bodytypearray = ["NaN", "hourglass", "straight & narrow",
                         "pear", "athletic", "full bust", "petite", "apple"]
        bodytype = np.asanyarray(bodytypearray)[bodytypenumber]
        dispatcher.utter_message(template="utter_done", chest=str(
            bodytype), height=str(recommended_size))

        return []


class ActionTagTypes1(Action):
    """Tag a conversation in Rasa X as positive or negative feedback """

    def name(self):
        return "action_tag_types1"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:

        clothtype_value = tracker.get_slot("clothtype_value")
        patterns_value = tracker.get_slot("patterns_value")
        fittings_value = tracker.get_slot("fittings_value")

        if clothtype_value == "formal":
            if patterns_value == "floral":
                if fittings_value == "loose":
                    dispatcher.utter_message(template="utter_image1")
        if clothtype_value == "formal":
            if patterns_value == "plain":
                if fittings_value == "loose":
                    dispatcher.utter_message(template="utter_image2")
        if clothtype_value == "formal":
            if patterns_value == "floral":
                if fittings_value == "slim":
                    dispatcher.utter_message(template="utter_image3")
        if clothtype_value == "formal":
            if patterns_value == "plain":
                if fittings_value == "slim":
                    dispatcher.utter_message(template="utter_image4")
        if clothtype_value == "casual":
            if patterns_value == "floral":
                if fittings_value == "loose":
                    dispatcher.utter_message(template="utter_image5")
        if clothtype_value == "casual":
            if patterns_value == "plain":
                if fittings_value == "loose":
                    dispatcher.utter_message(template="utter_image6")
        if clothtype_value == "casual":
            if patterns_value == "floral":
                if fittings_value == "slim":
                    dispatcher.utter_message(template="utter_image7")
        if clothtype_value == "casual":
            if patterns_value == "plain":
                if fittings_value == "slim":
                    dispatcher.utter_message(template="utter_image8")
        else:
            return []

        return[]
