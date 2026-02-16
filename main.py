import keyboard

key_dict = {}

def on_key(event):
    if event.event_type == "down":
        if event.name in key_dict.keys():
            key_dict[f"{event.name}"]+= 1
        else:
            key_dict[f"{event.name}"] = 1

keyboard.hook(on_key)

keyboard.wait(hotkey='ctrl+space')

sorted_tuples = sorted(key_dict.items(), key=lambda num_key: num_key[1], reverse=True)

sorted_key = dict(sorted_tuples)

print(sorted_key)

for key, value in sorted_key.items():
    print(f"{key}: {value}")