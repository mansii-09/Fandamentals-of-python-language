score = int(input("Enter your team's score: "))

if score >= 200:
    print("High score!")
elif score >= 150:
    print("Good score")
elif score >= 100:
    print("Average")
else :
    print("Needs Improvement")