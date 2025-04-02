def num_of_string(text):
    return len(text.split())

def character_frequency(text):
    freq_dict = {}
    text_arr = text.split()
    text_arr = "".join(text_arr)
    for char in text_arr:
        char = char.lower()
        if char not in freq_dict.keys() and char.isalpha():
            freq_dict[char] = 1
        elif char in freq_dict.keys() and char.isalpha(): 
            freq_dict[char] += 1
        else:
            continue

    return freq_dict

def print_report(char_dict):
    char_dict = dict(sorted(char_dict.items()))
    for key, value in char_dict.items():
        print(f"{key}: {value}")
    







        
