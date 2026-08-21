user_bio = "Music lover | Foodie | Traveller"

count = 0

for char in user_bio:
    if char != " ":
        count +=1

print("Number of characters:", count)