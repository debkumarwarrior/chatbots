# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

from rasa_sdk.knowledge_base.storage import InMemoryKnowledgeBase
from rasa_sdk.knowledge_base.actions import ActionQueryKnowledgeBase
from rasa_sdk.executor import CollectingDispatcher
from typing import Text, Dict, List, Any
import random


class InMemoryKnowledgeBase_v2(InMemoryKnowledgeBase):
    def __init__(self, file):
        super(InMemoryKnowledgeBase_v2, self).__init__(data_file=file)

    @staticmethod
    def match(content, value):
        if isinstance(content, list) and content.index(value) != -1:
            return True
        else:
            if content == value:
                return True
            else:
                return False

    async def get_objects(
        self, object_type: Text, attributes: List[Dict[Text, Text]], limit: int = 5
    ) -> List[Dict[Text, Any]]:
        if object_type not in self.data:
            return []

        objects = self.data[object_type]

        # filter objects by attributes
        if attributes:
            objects = list(
                filter(
                    lambda obj: [
                        InMemoryKnowledgeBase_v2.match(obj[a["name"]],a["value"]) for a in attributes
                    ].count(False)
                    == 0,
                    objects,
                )
            )

        random.shuffle(objects)

        return objects[:limit]



class ActionMyKB(ActionQueryKnowledgeBase):
    def __init__(self):
        # load knowledge base with data from the given file
        knowledge_base = InMemoryKnowledgeBase("dataset/knowledge_data.json")

        # overwrite the representation function of the hotel object
        # by default the representation function is just the name of the object
        knowledge_base.set_representation_function_of_object(
            "movie", lambda obj: '%s (Visit https://www.imdb.com/title/tt{%07d}) for more details.' %
                                 (obj["name"], obj['imdb'])
        )
        super(ActionMyKB, self).__init__(knowledge_base)

    def utter_attribute_value(
        self,
        dispatcher: CollectingDispatcher,
        object_name: Text,
        attribute_name: Text,
        attribute_value: Text,
    ) -> None:
        """
        Utters a response that informs the user about the attribute value of the
        attribute of interest.

        Args:
            dispatcher: the dispatcher
            object_name: the name of the object
            attribute_name: the name of the attribute
            attribute_value: the value of the attribute
        """
        if attribute_value:
            if attribute_name == 'year':
                dispatcher.utter_message(text='Movie {} was released in the year {}'.format(object_name,
                                                                                             attribute_value))
            elif attribute_name == 'rating':
                dispatcher.utter_message(text='Movie {} was rated {}'.format(object_name, attribute_value))
            elif attribute_name == 'genre':
                    dispatcher.utter_message(text='Genre of {} is {}'.format(object_name, attribute_value))
            else:
                dispatcher.utter_message(
                    text=f"'{object_name}' has the value '{attribute_value}' for attribute '{attribute_name}'."
                )
        else:
            dispatcher.utter_message(
                text='Sorry, could not find movies with {} for {}.'.format(attribute_name, attribute_value)
            )