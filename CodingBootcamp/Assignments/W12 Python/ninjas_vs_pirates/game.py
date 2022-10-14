from classes.ninja import Ninja
from classes.pirate import Blackbeard, Pirate

michelangelo = Ninja("Michelanglo")

jack_sparrow = Pirate("Jack Sparrow")

blackbeard = Blackbeard("Blackbeard")

while michelangelo.health > 0 and jack_sparrow.health > 0:
    michelangelo.attack(jack_sparrow)
    print(f"Jack has {jack_sparrow.health} HP now")
    jack_sparrow.attack(michelangelo)
    print(f"Michel has {michelangelo.health} HP now")
    #if Michelangelo crits enough, he can win (i reduced Jack's strength by 1)

#bringing Jack to full HP before next fight
jack_sparrow.health = 100

while blackbeard.health > 0 and jack_sparrow.health > 0:
    blackbeard.attack(jack_sparrow)
    print(f"Jack has {jack_sparrow.health} HP now")
    jack_sparrow.attack(blackbeard)
    print(f"Blackbeard has {blackbeard.health} HP now")
    #Jack get's executed because he falls at 4HP, he never had a chance...
