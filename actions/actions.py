# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet, SessionStarted, ActionExecuted, EventType,  FollowupAction


class ActionRestart(Action):
    """
    Handling game over.
    """

    def name(self) -> Text:
        return "action_restart"

    async def run(
        self, dispatcher, tracker: Tracker, domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(
            text="\n~~~~~~~\nYou died.\n~~~~~~~\nType 'play'")

        return []


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
                text="""You had to choose at a very young age who you will become: (Choose 1 option)
                        Pickpocket
                        Burglar
                        """)
        elif character_name == "knight":
            dispatcher.utter_message(
                text="""You were born with the soul of domination that makes people around you bend to your will. 
                You are a natural leader, but you might often end up blind to self-esteem. 
                If your birth sign wasn't enough to warrant a future of greatness, you were also born into a wealthy noble family. 
                At an early age you were sent into training to become a holy knight of the Kingdom of Rondon. 
                Training to become a squire was a harsh school that spared no one. No matter if you were from a noble origin or not. 
                A practice sparring match between you and a well-seasoned squire took place at the central training grounds. 
                It is said that a fighter shows their true colors in their first fight. This applied to you too. 
                When you saw the sword coming your way, you... (Choose 1 option)\n

                dodge - Quickly stepped aside and dodged it\n
                block - Raised your buckler in defence
                """)
        elif character_name == "dark priest":
            dispatcher.utter_message(
                text="""
You were born with the soul of the enlightened. You are always seeking restlessly for new knowledge and secrets hidden from the common folk. 
This trait started to show itself at a very young age as you were chosen to become a dark priest upon the birth of you and your twin sister. 
Typical to such occult rites, you were pitted against your sibling with ritual daggers and challenged to fight each other to the very last breath. 
Unfortunately for you, you were born with a fragile body and your sister easily overpowered you and had her dagger on your neck waiting for the final blow. 
She however showed mercy and withdrew her dagger. She stepped away from you as your high priest masters glared gleefully at the event unfolding before their very eyes. 
What will you do? (Choose 1 option)\n

kill - Strike your dagger to her spine while she walks away
defeat - Accept your defeat
""")
        elif character_name == "outlander":
            dispatcher.utter_message(
                text="""
You were born with the soul of the tormented. 
You are destined to struggle in every step you take in life. 
Ultimately this makes you stronger physically and tempers your iron will that rivals the will of the gods themselves.\n

Winters grew colder and summers shorter, which resulted in a great hunger in the north. 
The fine men of the Oldegård set sails to the unknown west in a desperate attempt to find food and riches to feed the people.\n

You had grown into your manhood and boarded the ship. 
After months of sailing, the sea saw no end and the crew was struggling. 
Some laid weak under the deck while some embraced the cold dark sea.\n

As the weak met their fate, the rest indulged in the greatest sin... (Choose 1 option)\n

devour - Devour your fallen comrades
not - Don't give in
""")
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
        if character_origin == "pickpocket":
            ability = [SlotSet(key="ability", value="steal")]

            dispatcher.utter_message(
                text="\nYou learned Steal!\n")
        elif character_origin == "burglar":
            ability = [SlotSet(key="ability", value="lockpicking")]

            dispatcher.utter_message(
                text="\nYou learned Lockpicking!\n")
        elif character_origin == "dodge":
            ability = [SlotSet(key="ability", value="fast attack")]

            dispatcher.utter_message(
                text="\nYou learned Fast attack!\n")
        elif character_origin == "block":
            ability = [SlotSet(key="ability", value="defence stance")]

            dispatcher.utter_message(
                text="\nYou learned Defence stance!\n")
        elif character_origin == "kill":
            dispatcher.utter_message(text="""
You stroke your dagger to the spin of your sister and she collapsed to the ground. 
The high priests seemed especially pleased with this and prepared you for your ascension ceremony. 
In the ascension ceremony you were to resurrect your deceased sister with necromancy and use her as a ghoul. 
You did this and the cold corpse of your sister brought a smile to your otherwise emotionless face.""")

            ability = [SlotSet(key="ability", value="necromancy")]

            dispatcher.utter_message(
                text="\nYou learned Necromancy!\n")
        elif character_origin == "defeat":
            ability = [SlotSet(key="ability", value="mastery over insects")]

            dispatcher.utter_message(
                text="\nYou learned Mastery over insects!\n")
        elif character_origin == "devour":
            ability = [SlotSet(key="ability", value="devour")]

            dispatcher.utter_message(
                text="\nYou learned Devour!\n")
        elif character_origin == "not":
            dispatcher.utter_message(text="""
Eventually you lost your mind to the hunger. 
While the others feasted on the fallen, you cried the night on the deck like a raging wolf.""")

            ability = [SlotSet(key="ability", value="bloodlust")]

            dispatcher.utter_message(
                text="\nYou learned Bloodlust!\n")

        if ability != []:
            dispatcher.utter_message(
                text="""You're now in front of the dungeons of Fear and Hunger... There are 2 entrances:
                Main - gigantic opened gates leading to the castle in front of you.
                Side - small wooden door to the left of the gates, nothing interesting.
                """)
        else:
            dispatcher.utter_message(
                text="""
                You didn't pick the origin! Try again.
                """)

        return ability


class ActionCrowMaulerChoice(Action):

    def name(self) -> Text:
        return "action_crow_mauler_choice"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        name = tracker.get_slot("character_name")
        origin = tracker.get_slot("character_origin")
        ability = tracker.get_slot("ability")
        crow_mauler_choice = tracker.get_slot("crow_mauler_choice")

        events = []
        if crow_mauler_choice == "fight":
            if ability == "fast attack":
                dispatcher.utter_message(
                    text="""
                    You're trembling from fear, but somehow you pull yourself together. Using your fast movements, you strike crow mauler in the eye, 
                    blinding it forever. Creature in pain, it is screaming, but with each blow, it weakens. Finally, the lifeless body falls down at your feet.\n

                    You find a key with an emblem of crow!\n

                    You can return to the side entrance (type 'side').
                    """)

                events = [SlotSet(key="crow_key", value=True)]
            elif ability == "defence stance":
                dispatcher.utter_message(
                    text="""
                    You're trembling from fear, but somehow you pull yourself together. You are preparing the defence stance and waiting for a creature's turn...
                    
                    Crow mauler swings its mace and hits your shield, but you parry the blow and puts the sword in the crow mauler's heart. Creature is dead!\n

                    You find a key with an emblem of crow!\n

                    You can return to the side entrance (type 'side').
                    """)

                events = [SlotSet(key="crow_key", value=True)]
            elif ability == "necromancy":
                dispatcher.utter_message(
                    text="""
The crow mauler is just a tiny brick in a greater scheme of things - you're the one who is going to be a king of this world!\n

You are using your blood magic to summon the the dead... The ghoul appears from the blood portal and rushes towards crow mauler!\n

Ghoul rips off crow's skin, while you're using blood magic against it.\n

Finally, the crow mauler is dead.\n

You find a key with an emblem of crow!\n

You can return to the side entrance (type 'side').\n\n
                    """)

                events = [SlotSet(key="crow_key", value=True)]
            elif ability == "mastery over insects":
                dispatcher.utter_message(
                    text="""
The crow mauler is just a tiny brick in a greater scheme of things - you're the one who is going to be a king of this world!

You are chanting and ordering all maggots, spiders, and other insects to swarm crow mauler and eat it alive.

After a great feast, the only things that are left are bones and a key...

You find a key with an emblem of crow!\n

You can return to the side entrance (type 'side').\n\n
                    """)

                events = [SlotSet(key="crow_key", value=True)]
            elif ability == "devour":
                dispatcher.utter_message(
                    text="""
As the crow mauler approaches, you feel a terrible sense of hunger, which cannot be held on any longer.
You leap towards the crow mauler and start devouring it alive... It was horrible, your mind was blank in the process.
You didn't even understand whether you were alive or not.\n

Right now you're standing in the bloodbath, and under your legs you see a shiny object.\n

You find a key with an emblem of a crow!\n

You can return to the side entrance (type 'side').\n\n
                    """)

                events = [SlotSet(key="crow_key", value=True)]
            elif ability == "bloodlust":
                dispatcher.utter_message(
                    text="""
As crow mauler approaches, you feel terrible sense of killing, but it's not coming from crow mauler...\n

It is coming from you.\n

You swing your axe flawlessly, until you turn the crow mauler face and body into mincemeat.\n

On the body of crow there is something shiny...\n

You find a key with an emblem of crow!\n

You can return to the side entrance (type 'side').\n\n
                    """)

                events = [SlotSet(key="crow_key", value=True)]
            else:
                dispatcher.utter_message(
                    text="""
                    You're trembling from fear, but somehow you pull yourself together. You are striking crow mauler with your weapon, 
                    but crow mauler does not react to it even slightly. It raises its peak above you and chops off your head instantly...\n\n
                    """)

                events = [FollowupAction("action_restart")]
        elif crow_mauler_choice == "run":
            if ability == "steal":
                dispatcher.utter_message(
                    text="""
                        Of course, what you - mere human can do against ancient terror? The best thing is to run as fast as you can. The harsh world of thieves taught you
                        agility. \n\n
                        
                        You outrun crow mauler and even manage to steal something from his left pocket... It is a key with an emblem of crow!\n\n
                        
                        You can return to the side entrance (type 'side').
                        """)
                events = [SlotSet(key="crow_key", value=True)]
            else:
                dispatcher.utter_message(
                    text="""
                    Of course, what you, mere human, can do against ancient terror? The best thing is to run as fast as you can. However, when you turn your back to the crow mauler,
                    it chops your legs off and beats you to death. Finally, it raises its peak above you and chops off your head...\n\n
                    """)
                events = [FollowupAction("action_restart")]

        return events


class ActionSideDoorChoice(Action):

    def name(self) -> Text:
        return "action_side_door_choice"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        ability = tracker.get_slot("ability")
        crow_key = tracker.get_slot("crow_key")
        side_door_choice = tracker.get_slot("side_door_choice")

        events = []
        if side_door_choice == "mushrooms":
            dispatcher.utter_message(
                text="""
You're gathering some mushrooms from the dry wall. They are squishy and some of them have a distinctive smell.
Despite that, you still try to taste one. As you chew it, you seem to start feeling uncomfortable tension in the belly. You puke with blood, but you cannot stop
until you fall on the ground unconsciously. It was a mistake to eat these mushrooms... \n\n
                    """)
            events = [FollowupAction("action_restart")]
        elif side_door_choice == "down":
            if crow_key:
                dispatcher.utter_message(
                    text="""
You see a wooden door, and hear strange noises coming from it. You cannot distinguish whether it is a scream or just your imagination...
The door is locked, but you're inserting the key with a symbol of a crow. You hear the unlocking sound. The door is opened.\n

You feel the breeze coming from the door, and see a bright light. It feels like a home, with each step you want to go to sleep.\n

When you reach the light, you lay down near it and fall asleep. This nightmare is over, finally...\n

Ending B: the end?\n\n
                        """)
                events = [FollowupAction("action_restart")]
            elif ability == "lockpicking":
                dispatcher.utter_message(
                    text="""
You see a wooden door, and hear strange noises coming from it. You cannot distinguish whether it is scream or just your imagination...
The door is locked, but you use your lockpicking skill to open it. Success! You open the door...\n

You feel the breeze coming from the entrance, and see a bright light. It feels like a home, with each step you want to go to sleep.\n

When you reach the light, you lay down near it and fall asleep. This nightmare is over, finally...\n

Ending B: the end?\n\n
                        """)
                events = [FollowupAction("action_restart")]
            else:
                dispatcher.utter_message(
                    text="""
You see a wooden door, and hear strange noises coming from it. You cannot distinguish whether it is scream or just your imagination...\n
The door is locked, you need a key with a symbol of crow to go through it.\n\n

You can return to the main entrance (type 'main').
                        """)
        else:
            dispatcher.utter_message(
                text="Incorrect choice. Please try again.")

        return events
