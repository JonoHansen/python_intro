#Madlibs
# 1. Create a few variables that get certain bits of info from teh user
# 2. Print out a string with a short story, using the info gathered
name = raw_input("What is your name >>")
item = raw_input("Name a completly random item >>")
adjective = raw_input("Pick an Adjective >>")
living = raw_input("Name a living item >>")
adjective2 = raw_input("Pick another adjective >>")
phrase = raw_input("Pick a 'Doing Phrase'(eat some food)(make sure it doesnt have ing ")

story = "A long time ago, this dude named %s saw a floating %s. %s thought it was very %s because it reminded him of his best friends %s who used to %s." % (name, item, name, adjective, living, phrase)

print story
