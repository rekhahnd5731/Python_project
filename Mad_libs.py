# Mad-lab project

print("Welcome to the Python Mad Libs Game! ")

#take input from user about the blanks in the Story
a = input("Enter the Adjective: ")
b = input("Enter the name: ")
c = input("Object: ")
d = input("place: ")
e = input("animal: ")
f = input("verb ending in -ing: ")
g = input("body of water: ")
h = input("color: ")
i = input("noun: ")
j = input("magical_object: ")
k = input("emotion: ")

# creating the story which contain blanks (the mysterious Adventure)
mad_lib = f"""
            It was a {a} day when {b} decided to go on an adventure. With their trusty {c} in hand, they set off towards the {d}. The journey was long and {a}, but {b} was determined.

              After walking for hours, they stumbled upon a {a} {e} that appeared to be {f} by the {g}. Surprised by this encounter, {b} stopped and said, “I’ve never seen a {e} act like that!”

            Suddenly, the sky turned {h}, and the {i} in the distance started to glow. A voice from behind them said, “Only the bravest souls can complete the quest for the {j}. Do you accept?”

            Without hesitation, {b} nodded. They grabbed their {c} and hurried toward the glowing {i}. But before they could reach it, they had to cross a {a} bridge made of (material).

            Finally, after facing many challenges, {b} reached the {j}. They felt {k}, knowing their adventure was only just beginning.
            """

#display the completed story
print("\n Here the mad lab story")
print(mad_lib)