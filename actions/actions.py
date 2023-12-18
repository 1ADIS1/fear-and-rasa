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


class ActionCharacterChoice(Action):

    def name(self) -> Text:
        return "action_character_chosen"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        character_name = tracker.get_slot("character_name")

        if character_name == "mercenary":
            dispatcher.utter_message(
                text="""You were born with the soul of the endless that makes you yearn for freedom 
                        and forces you to push your creativity to its limits.""")
            dispatcher.utter_message(
                text="""You had to choose at a very young age who you will become:
                        Pickpocket
                        Burglar
                        Lead an honest life
                        """)

            # TODO: become a pickpocket
            # TODO: burglar
            # TODO: lead a honest life
        elif character_name == "knight":
            dispatcher.utter_message(
                text="""knight!""")
        elif character_name == "dark priest":
            dispatcher.utter_message(
                text="""dark priest""")
        elif character_name == "outlander":
            dispatcher.utter_message(
                text="""outlander""")
        else:
            dispatcher.utter_message(
                text="Unknown character. Enter the character again.")

        return []


class ActionCharacterOrigin(Action):

    def name(self) -> Text:
        return "action_character_origin"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        character_origin = tracker.get_slot("character_origin")

        ability = []
        if character_origin == "Pickpocket":
            ability = [SlotSet(key="ability", value="Steal")]

            dispatcher.utter_message(
                text="You learned Steal!")
        elif character_origin == "Burglar":
            ability = [SlotSet(key="ability", value="Lockpicking")]

            dispatcher.utter_message(
                text="You learned Lockpicking!")
        elif character_origin == "Honest life":
            # TODO: give 30 silver coins
            pass

        if ability != []:
            dispatcher.utter_message(
                text="""You're now in front of the dungeons of Fear and Hunger... There are 2 entrances:
                Main - gigantic opened gates leading to the castle in front of you.
                Side - small wooden door to the left of the gates, nothing interesting.
                """)

        return ability


class ActionCrawMaulerChoice(Action):

    def name(self) -> Text:
        return "action_craw_mauler_choice"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        character_origin = tracker.get_slot("character_origin")

        return []
