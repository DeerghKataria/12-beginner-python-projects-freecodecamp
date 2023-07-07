# Matllib works on the basis of String concatenation
# For example, we are going to create a string that says: "Subscribe to ____"

# youtuber = "Deergh Kataria" # This is some string variable

# There are 3 ways of doing it
# print("subscribe to " + youtuber)
# print("subscribe to {}".format(youtuber))
# print(f"subscribe to {youtuber}")

# The third way of doing it using fstring seems like a better option
# since it is the cleanest way of doing string concatenation.

adj = input("Adjective: ")
verb1 = input("Verb1: ")
verb2 = input("Verb2: ")
famous_person = input("Famous Person: ")

madlib = f"\nComputer programming is so {adj}! iT makes me so excited all the time because \
    I love to {verb1}. Stay hydrated and {verb2} like you are {famous_person}"

print(madlib)

