story = """
Once upon a time, a crow was perched on a branch,
Parched and thirsty under the scorching sun.
Spotting a pitcher below, the crow flew down with hope,
Only to find the water level too low to reach.

The clever crow gathered pebbles one by one,
Dropping them carefully into the pitcher's mouth.
With each pebble, the water rose a little higher,
Until finally, the crow could quench its thirst.

The moral of the tale: persistence and wit
Can overcome the greatest of obstacles.
And so the crow learned, as we all must know,
That patience and cleverness will help us grow.
"""

# # print(story)
# print(f"The number of words in the story is: {len(story.split())} words ")
# print(f"The number of characters in the story is: {len(story)} characters ")
# print(f"The number of lines in the story is: {len(story.splitlines())} lines ")
# print(f"The number of sentences in the story is: {len(story.split('.')) - 1} sentences ")
# print(f"The position of crow in the story is: {story.find('crow')} @character position ")
# print(f"The position of crow in the story is: {story.index('crow')} @character position ")
# story = story.replace("crow", "swan")
# print(story)
# print(story.count("swan"))
# print(story.lower( ))
# print(story.upper())
num = 20
 
words = story.split()
for word in words:
    print(word)