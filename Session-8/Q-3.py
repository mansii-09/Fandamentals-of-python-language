def reverse_message(message):
    result = ""

    for i in range(len(message) -1, -1, -1):
        result += message[i]

    return result

print(reverse_message("Hello World"))