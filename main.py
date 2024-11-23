
calls = 0

def count_calls():
    global calls
    calls += 1
    return calls

def string_info(string):
    x = len(string)
    y = string.upper()
    z = string.lower()
    count_calls()
    return x, y, z


def is_contains(string, list):
    count_calls()
    new_list = []
    for i in list:
        new_list.append(i.lower())
    if string.lower() in new_list:
        return True
    else:
        return False
