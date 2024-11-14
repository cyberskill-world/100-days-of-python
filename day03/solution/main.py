import sys

print("~~~~~~~~~~you know fireworks, it is the most beautiful flower in the night.~~~~~~~~~~")
print("~~~~~~~~~~Chemistry will tell us how to make fireworks.~~~~~~~~~~")
print("----------~~~~~~~~~~let's get started~~~~~~~~~~---------------")
print('''Fireworks are produced by oxidation-reduction reactions\n
      For example:\nOxidant: Potassium nitrate (KNO₃) or ammonium nitrate (NH₄NO₃).\n
      Reducing agent: Carbon (C) or other forms of chemical energy.\nSo the overall reaction can be described as follows\n
      oxidizing agent + reducing agent -> gaseous products + heat + ....''')

first = input("Choose one of the following two answers: light / water. Choose:").lower()

if first == "water":
    print("wrong, start over")
    sys.exit()
elif first == "light":
    print("oxidizing agent + reducing agent -> gaseous products + heat + light")
    print("Nice, you made it to the next level!")

second = input('''How to create colors in fireworks: To create different colors in fireworks, people often add metal salts to the mixture.
            So what do you need to add to create red color?
            Choose(Enter Formula Only): Strontium carbonate (SrCO₃) / Cupric chloride (CuCl₂) / Sodium nitrate (NaNO₃)''').lower()

if second =="strontium carbonate":
    print("Nice, you made it to the next level, you're pretty good at this!")
    print ("Red: Strontium carbonate (SrCO₃) or Strontium nitrate (Sr(NO₃)₂)")
elif second =="cupric chloride":
    print("wrong, start over")
elif second == "sodium nitrate":
    print("wrong, start over")



