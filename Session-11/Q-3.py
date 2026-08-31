def display_friends(friends):
    for username, followers in friends.items():
        print(f"{username} : {str(followers) }K followers")

friends = {
    "mansi" : 2.3,
    "riya" : 4.5,
    "neha" : 1.8
}

display_friends(friends)