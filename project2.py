import random

print("****************Welcome to the madlibs game *********************")

#Taking input as the verb,noun,place,name.....................
enter_name_value = input("Please enter the name for the madlibs game:")
enter_noun_value = input("Please enter the noun for the madlibs game:")
enter_verb_value = input("Please enter the verb for the madlibs game:")
enter_adjective_value = input("Please enter the adjective for the madlibs game:")
enter_place_value = input("Please enter the place for the madlibs game:")
enter_number_value = input("Please enter the number for the madlibs game:")
enter_animal_value = input("Please enter  the animal for the madlibs game:")
print("\n")
print("\t\twe have ten madlibs story")
choices_for_story = int(input("Please enter the number of story you want to enter:"))

#creating stories for the madlibs and storing it in the dictionary
madlibs_story_library= {
            'A Day in the jungle' :"Explorer {name} ventured into the jungle near {place}.There,they saw a {adjective}"
            "{animal} trying to {verb} a {noun}. They watched it for {number} hours!",
            'The Birthday Suprise':"For {name}'s birthday, they invited everyoe to {place} for a {adjective} celebration."
            "The guests brought  a big {noun}, and everyoe cheered as {name} tried to {verb} like a"
            "{animal} for {number} minutes!",
            'Mystery in the Library':" Detective {name} was called to {place} to solve a mystery. There was a {adjective}"
            "{noun} left on the floor, and they heard  a {animal} trying to {verb}. The detective spent"
            "{number} hours  searching for clues",
            'The Best Day at the Zoo':"{name} visited the zoo at {place} and saw a {adjective}{animal} that loved to {verb}"
            "The animal kept playing with a {noun} all day, drawing attention from {number} people",
            'A Space Adventure':"{name} traveled to {place} in a spaceship! They found a {adjective} {noun} floating in space." 
            "Suddenly, an alien that looked like a {animal} asked them to {verb}. They stayed"
            "there for {number} days",
            'A Magical Potion':" Wizard {name} mixed a potion in their lab at {place}. They added a {adjective} {noun}"
            "and said  a spell to make a {animal}{verb}.After {number} seconds, the potion was"
            "ready!",
            'The Haunted House':"One stormy night,{name} went to the haunted house near {place}.Inside, they found"
            "a {adjective} {noun} that started to {verb} like a {animal}.They ran out of there in"
            "{number} seconds!" ,
            'Camping by the Lake':"{name} went camping at {place}. They spotted a {adjective} {animal} that came close to"
            "their tent.It tried to {verb} their {noun}, and they  stayed awake for {number} hours to "
            "keep watch.",
            'An Unusual Pet':"{name} bought a pet {animal} from {place}. The {animal} was very {adjective} and loved"
            "to {verb} with a {noun}.{name} played with it every day for {number} hours.",
            'Treasure Hunt Adventure':"{name} was on a treasure hunt in {place}. They discovered a {adjective} map hidden in"
            "a {noun}. The map said to follow the sound of a {animal} that liked to {verb}. After"
            "{number} days, they found the treasure!" 
}

#storing the the noun,verb,name to insert to the madlibs story library keys value where they are kept inside the curlybraces
values = {
    'name':enter_name_value,
    'noun':enter_noun_value,
    'verb':enter_verb_value,
    'place':enter_place_value,
    'animal':enter_animal_value,
    'number':enter_number_value,
    'adjective':enter_adjective_value
}

#new story library with the values from the above 
filling_story_with_values = {
    key:value.format(**values) for key,value in madlibs_story_library.items()
}
#This is to have a space between the the final output and the above input taken 
print("\n")
#final output with the loop to have different story which is selected by the user
for _ in range(choices_for_story):
    output = random.choice(list(filling_story_with_values.keys()))
    print(output)
    print(f"{filling_story_with_values[output]}\n")

