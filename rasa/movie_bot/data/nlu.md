## intent:greet
- hey
- hello
- hi
- good morning
- good evening
- hey there

## intent:goodbye
- bye
- goodbye
- see you around
- see you later

## intent:affirm
- yes
- indeed
- of course
- that sounds good
- correct

## intent:deny
- no
- never
- I don't think so
- don't like that
- no way
- not really

## intent:mood_great
- perfect
- very good
- great
- amazing
- wonderful
- I am feeling very good
- I am great
- I'm good

## intent:mood_unhappy
- sad
- very sad
- unhappy
- bad
- very bad
- awful
- terrible
- not very good
- extremely sad
- so sad

## intent:bot_challenge
- are you a bot?
- are you a human?
- am I talking to a bot?
- am I talking to a human?

## intent:query_knowledge_base
- what [movies](object_type:movie) can you recommend?
- list some [movies](object_type:movie)
- can you name some [movies](object_type:movie) please?
- can you show me some [movie](object_type:movie) options
- list [thriller](genre) [movies](object_type:movie)
- do you have any [thriller](genre) [movies](object_type:movie)?
- do you know the [imdb link](attribute:imdb-link) of [that one](mention)?
- what [genre](attribute:genre) is [it](mention)?
- do you know what [genre](attribute:genre) the [last one](mention:LAST) has?
- What about any [adventure](genre) [movies](object_type:movie)?
- Do you also know some [horror](genre) [movies](object_type:movie)?
- can you tell me the [release year](attribute:release-year) of [that movie](mention)?
- what [genre](attribute:genre) do [they](mention) have?
- please list some [movies](object_type:movie) in [adventure](genre) for me
- show me some [movies](object_type:movie)
- what are [movies](object_type:movie) in [adventure](genre)
- what is the [ratings](attribute:star-rating) of the [second](mention:2) movie?
- what is the [star rating](attribute:star-rating) of [Shawshank Redemption](movie)?
- what is the [genre](attribute:genre) of [Toy Story](movie)?

## lookup:movie
dataset/movies.txt

## lookup:genre
dataset/genres.txt

## regex:release-year
[0-9]{4}

## synonym:star-rating
- star rating
- ratings

## synonym:genre
- genre
- genres