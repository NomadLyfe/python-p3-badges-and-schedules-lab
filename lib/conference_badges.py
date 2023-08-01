def badge_maker(name):
    return f'Hello, my name is {name}.'

def batch_badge_creator(names):
    badge_batch = [f'Hello, my name is {name}.' for name in names]
    return badge_batch

def assign_rooms(names):
    room_batch = [f"Hello, {name}! You'll be assigned to room {index}!" for index, name in enumerate(names, 1)]
    return room_batch

def printer(names):
    for text in batch_badge_creator(names):
        print(text)
    for text in assign_rooms(names):
        print(text)
    return None
