import time

# Function to execute the steps
def executeSteps(steps):
    for step in steps:
        print(step)
        time.sleep(2.5)


# Function to Make Tea
def makeTea():
    steps = [
        "STEPS TO MAKE TEA\n",
        "A Tea is a hot drink usually made with various ", #continue from here
        "Step 1: Go to the crockery shelf",
        "Step 2: Take a tea kettle from the shelf",
        "Step 3: Keep it on the kitchen counter",
        "Step 4: Look for a water source",
        "Step 5: Take a glass of water",
        "Step 6: Bring water glass to the kitchen counter",
        "Step 7: Move to the drawer and find tea powder and sugar",
        "Step 8: Move to the refrigerator",
        "Step 9: Take milk from the refrigerator and go back to the kitchen counter",
        "Step 10: Keep all the ingredients on the counter",
        "Step 11: Put the kettle on the stove",
        "Step 12: Pour glass of water in the kettle",
        "Step 13: Turn the stove ON",
        "Step 14: Let the water boil",
        "Step 15: Add tea powder and sugar in the boiling water",
        "Step 16: Go to the shelf and bring a tea cup",
        "Step 17: Come back to the kitchen counter",
        "Step 18: Pour two cups of milk in the kettle",
        "Step 19: Wait for the liquid to become hot again",
        "Step 20: Turn the stove OFF",
        "Step 21: Look for a strainer",
        "Step 22: Pour tea into the cup through the strainer",
        "Step 23: Wait for the tea to cool for 2 minutes",
        "Step 24: Tea is ready to drink"
    ]

    executeSteps(steps)


# Function to Brush teeth
def brushTeeth():
    steps = [
        "STEPS TO BRUSH YOUR TEETH\n",
        "Step 1: Stand in front of a sink", 
        "Step 2: Find a toothbrush",
        "Step 3: Pick up the toothbrush by its handle",
        "Step 4: Look for a toothpaste",
        "Step 5: Remove the cap of the toothpaste tube",
        "Step 6: Hold the toothbrush so the bristles point upwards",
        "Step 7: Press the toothpaste tube and place toothpaste onto the bristles",
        "Step 8: Put the cap back on the toothpaste tube",
        "Step 9: Put the toothpaste down",
        "Step 10: Open your mouth",
        "Step 11: Insert the toothbrush into your mouth",
        "Step 12: Place the bristles on your teeth",
        "Step 13: Move the toothbrush back and forth 10 times",
        "Step 14: Then place the toothbrush bristles on the other side of mouth",
        "Step 15: Gently rub the tooth back and forth",
        "Step 16: Repeat step 12-15 for all the teeth",
        "Step 17: Brush the tongue gently for 2 minutes",
        "Step 18: Remove the toothbrush from your mouth",
        "Step 19: Rinse the toothbrush with water",
        "Step 20: Place it back to its location",
        "Step 21: Spit the toothpaste foam in the sink",
        "Step 22: Fill your mouth with water",
        "Step 23: Swish the water around your mouth for 5-6 times",
        "Step 24: Spit the water into the sink",
        "Step 25: Repeat step 22-24 two times",
        "Step 26: Take a towel from the storage place",
        "Step 27: Wipe your mouth."
    ]

    executeSteps(steps)


# Function to Tie the Shoe
def tieShoe():
    steps = [
        "STEPS TO TIE YOUR SHOELACE\n",
        "Step 1: Take the shoes out of the shoe rack",
        "Step 2: Sit down",
        "Step 3: Place one shoe on your foot",
        "Step 4: Hold the laces in both of your hands",
        "Step 5: Pull the laces until the shoe feels tight but comfy enough",
        "Step 6: Cross the laces on each other",
        "Step 7: Push one lace underneath the other",
        "Step 8: Pull both lace ends tightly",
        "Step 9: Make loops of both ends",
        "Step 10: Cross the loops with each other",
        "Step 11: Push one loop through the hole created by crossing",
        "Step 12: Hold one loop with each thumb and index finger",
        "Step 13: Pull the loops away from each other",
        "Step 14: Stop pulling when the knot becomes tight",
        "Step 15: Adjust the loops in their places",
        "Step 16: The shoe is tied"
    ]

    executeSteps(steps)


# main code
print("What task you want to do?")
tasks = ["Enter 1 to Make Tea",
         "Enter 2 to Brush Teeth",
         "Enter 3 to Tie the Shoe"]
print()
for task in tasks:
    print(task)

choice = int(input("Enter your choice: "))

if choice == 1:
    makeTea()
elif choice == 2:
    brushTeeth()
elif choice == 3:
    tieShoe()
else:
    print("Invalid choice")