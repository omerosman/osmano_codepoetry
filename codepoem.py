import random
import sys
import time

def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.03)

print_slow(("What is Life?").center(200)); print "\n"
print_slow(("by Omer Osman").center(200)); print "\n"; print "\n"

Life = ["The existence of an individual human being or animal.",
        "A principle or force that is considered to underlie the distinctive quality of animate beings.",
        "The period of existence.",
        "The quality that distinguishes a vital and functional being from a dead body.",
        "The sequence of physical and mental experiences that make up the existence of an individual."]

Process_of_Life = ["In life we win and we lose.",
                   "In life we rise and we fall.",
                   "In life we fight and we win.",
                   "In life we fight and we lose.",
                   "In life we lose and we win.",
                   "In life we are born and we die."]

And_People_Say = ["Life is what happens to you while you're busy making other plans.",
                  "Life is not about waiting for the storm to pass. It's about learning to dance in the rain.",
                  "Yesterday is history, tomorrow a mystery and today is a gift. That's why we call it the present.",
                  "Live every day like it's your last.",
                  "Dream as if you'll live forever. Live as if you'll die today."]

living = 0
while living < 10:
    print_slow(("What is Life?").center(200)); print "\n"
    print_slow(random.choice(Life).center(200)); print "\n"
    print_slow(random.choice(Process_of_Life).center(200)); print "\n"
    print_slow(random.choice(And_People_Say).center(200)); print "\n"
    living += 1
print_slow("Fin")