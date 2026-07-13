name= input("Enter a name: ")
adjective = input("Enter an adjective: ")
verb = input("Enter a verb: ")
activity = input("Enter an activity: ")
helping_activity = input("Enter a helping activity: ")
activity2 = input("Enter another activity: ")
adjective2 = input("Enter another adjective: ")
object = input("Enter an object: ")
adverb = input("Enter an adverb: ")

story = f"""
There was once an individual named {name}, who lived in a small village. 
{name} was known for their {adjective} nature and their ability to {verb}.
They spent their days {activity} and helping others in the community by {helping_activity}.
One day, {name} was caught in a sudden storm while {activity}. 
Despite the harsh weather, {name} remained {adjective} and continued to {verb}.
Unfortunately, {name} got hit by a flying {object} and was injured.
In the end, {name} was unable to fully recover and lived the rest of their life {adverb}.
"""
print(story)
