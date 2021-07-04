def what_to_do(command):
    if command.startswith("Simon says") or command.endswith("Simon says"):
        new_string = command.replace("Simon says", "").strip()
        return "I " + new_string
    else:
        return "I won't do it!"
