# Chatbot for movie database(Rasa)

This repository is for developing chatbot using Rasa framework.

This project includes the action code and the variations of utterances/story for user conversations.
- `actions.py` - The action file containing the actions that are executed.
- `nlu.md` - This file contains the variations of user utterance.
- `stories.md` - A sample list of user conversations.
- `movies.txt` - List of movies recognized.
- `genres.txt` - List of genres supported.
- `knowledge_data.json` - Complete knowledge database of the movies and its respective attributes.

## Steps to create the sample chatbot
The sample movie chatbot can be run using rasa commands.
- `rasa init` - Creates a skeleton
- `rasa train` - Trains a model using the nlu/stories provided.
- `rasa run actions` - Run the actions on the configured endpoints.
- `rasa shell` - Run an interactive shell to see the chatbot output.

## Sample conversations:
 * [User] : Hi
 * [Bot] : Hey! How are you?
 * [User] : Can you recommend some movies?
 * [Bot] : Found the following objects of type 'movie':
          1: King of Kong, The (Visit http://www.imdb.com/title/tt0923752) for more details. 
          2: Shag (Visit http://www.imdb.com/title/tt0098300) for more details. 
          3: Mrs. Parker and the Vicious Circle (Visit http://www.imdb.com/title/tt0110558) for more details. 
          4: Lone Ranger, The (Visit http://www.imdb.com/title/tt1210819) for more details. 
          5: Cold in July (Visit http://www.imdb.com/title/tt1179031) for more details. 
 * [User] : What is the genre of the last one?
 * [Bot] : Cold in July (Visit http://www.imdb.com/title/tt1179031) for more details is ['drama', 'thriller']
 