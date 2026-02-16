import keyboard

key_dict = {}
word_dict = {}
word = ""
buffer = ""
command_lst = ["space", "shift", "ctrl", "alt", "backspace"]

def counter(key, dict_type):
    if key in dict_type.keys():
        dict_type[key] +=1
    else:
        dict_type[key] = 1
    
def sort_things(dict_type):
    sorted_tuples = sorted(dict_type.items(), key=lambda num_key: num_key[1], reverse=True)
    return dict(sorted_tuples)

def print_things(dict_type):
    for key, value in dict_type.items():
        print(f"{key:7}:{value:7}") # will fix later
                

def on_key(event):
    global word
    global buffer
    if event.event_type == "down":
        if event.name not in command_lst:
            word += event.name
            counter(event.name, key_dict)
        elif event.name == command_lst[0]:
            counter(word, word_dict)
            word = ""
        
 
keyboard.hook(on_key)

keyboard.wait(hotkey='ctrl+alt')

print_things(sort_things(key_dict))
print("----------------------------------------------------") # will fix later
print_things(sort_things(word_dict))