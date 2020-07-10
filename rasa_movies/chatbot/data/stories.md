## happy path 1
* greet
  - utter_greet
* mood_great
  - utter_happy

## sad path 1
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* affirm
  - utter_happy

## sad path 2
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* deny
  - utter_goodbye

## Hello
* greet
- utter_greet

## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot

## happy path 2
* greet
  - utter_greet
* query_knowledge_base
  - action_query_knowledge_base
* goodbye
  - utter_goodbye

## happy path 3
* greet
  - utter_greet
* query_knowledge_base
  - action_query_knowledge_base
* query_knowledge_base
  - action_query_knowledge_base
* goodbye
  - utter_goodbye

## Query Knowledge Base
* query_knowledge_base
- action_query_knowledge_base

