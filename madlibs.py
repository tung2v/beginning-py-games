#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

'''
MadLibs
by Vivian
ask user for words, then input the choices into the correct places in the correct places in the story.
'''
'''
STORY = "one [season] day, [name] woke up feeling [adjective1]. 'I need to go to the store. I need [noun1].' So they got dressed and headed out, playing a [adjective2] summer bop [song name].
'[store name]! There it is. Finally I shall have what my weary heart desires.'
'Not so fast' came a voice around the [noun2].
'Oh no! [enemy]! You're not getting between me and my precious [noun1]'
'Haha [name], well watch me!' [enemy] pulls out a [noun3], waving it around [adverb].
"I don't want to fight you, but if I must," [name] says. [name] throws 10 [dessert] at [enemy] in rapid succession.
"[swear word]soup! This is NOT how this ends!"
Covered in [dessert], [enemy] summons a [adjective3] spell. "[color1] [animal1] hear my [noun4]. Bring [noun5] from the [place] and let [noun6] [verb1]"
The spell works, kind of. [noun6] are everywhere, but they all seem to be avoiding [name].
"Well," [name] [verb2]. "I'm [mental illness], so this can wait for another day." They press their watch and land in [year] with [noun1].
'''


print ("Let's play MadLibs. I'm going to ask you for words now")

name = input("Enter a name: ")
adjectives = input("Enter 3 adjectives, separated by a comma: ").split(', ')
verbs = input("Enter 2 verbs, separated by a comma: ").split(', ')
nouns = input("I'm gonna need 6 nouns, separated by commas: ").split(', ')
adverb = input("Pick an adverb: ")
                  
song = input("Pick a song: ")
store = input("What's your favorite store?: ")
enemy = input("Pick a nemesis: ")
animal = input("What's your favorite animal?: ").capitalize()
swear = input("What's your favorite swear?: ").upper()

color = input("Almost done. Pick a color: ").capitalize()
dessert = input("Enter your favorite dessert: ")
year = input("Enter a year: ")
ment = input("Last one. Pick a mental illness: ")


STORY = "One summer day, %s woke up feeling %s. 'I need to go to the store. I need %s.' So they got dressed and headed out, playing a %s summer bop, %s. \n '%s! There it is. Finally I shall have what my weary heart desires.' \n 'Not so fast' came a voice around the %s. \n 'Oh no! My nemesis %s! You're not getting between me and my precious %s' \n 'Haha %s, well watch me!' %s pulls out a %s, waving it around %s. \n 'I don't want to fight you, but if I must,' %s says. %s throws 10 %ss at %s in rapid succession. \n '%ssoup! This is NOT how this ends!' \n Covered in %s, the enemy summons a %s spell. '%s %s, hear my %s. Bring %ss from the sky and let %ss %s!' \n The spell works, kind of. %ss are everywhere, but they all seem to be avoiding %s. \n 'Well,' %s %ss. 'I have %s, so this can wait for another day.' They press their watch and land in %s with their %s."

print (STORY % (name, adjectives[0], nouns[0], adjectives[1], song, store, nouns[1], enemy, nouns[0], name, enemy, nouns[2], adverb, name, name, dessert, enemy, swear, dessert, adjectives[2], color, animal, nouns[3], nouns[4], nouns[5], verbs[0], nouns[5], name, name, verbs[1], ment, year, nouns[0]))

