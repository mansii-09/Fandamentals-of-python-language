def formal_follower_count(number):
    if number >= 1000000:
        return f"{number / 1000000 :.1f}M"
    elif number >= 1000:
        return f"{number / 1000:.1f}K"
    else:
        return str(number)

print(formal_follower_count(1500))
print(formal_follower_count(1200000))
print(formal_follower_count(500))