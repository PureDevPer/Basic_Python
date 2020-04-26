money = 200
watch = 1
if money >= 300 or watch:
    print("Take a bus")
else:
    print("Walk!")

# Take a bus

if money >= 300 and watch:
    print("Take a bus")
else:
    print("Walk!")

# Walk!

if not watch:
    print("Take a bus")
else:
    print("Walk!")

# Walk!

pocket = ["paper", "headphone", "money"]
if "money" in pocket:
    print("Take a bus")
else:
    print("Walk")

# Take a bus


pocket = ["paper", "headphone"]
watch = 1
if "money" in pocket:
    print("Take a bus")
elif watch:
    print("Take a taxi")
else:
    print("Walk")

# Take a taxi
