print("------------------------------------------------")
print("--- LaFarge's CrackMe v0.2 Keygen by TalhaSa ---")
print("------------------------------------------------\n\n")

start_string = "_r <()<1-Z2[l5,^"
username = input("Username: ")

start_string_len = len(start_string)
username_len = len(username)

longer_index = start_string_len if start_string_len > username_len else username_len

def change_char(s, index, new_char):
    if index < 0:
        raise IndexError("Index is outside available index")
    if index >= len(s):
        index = index % len(s)
    return s[:index] + new_char + s[index + 1:]

def insert_every(s, chunk_size, insert_char):
    parts = [s[i:i+chunk_size] for i in range(0, len(s), chunk_size)]
    return insert_char.join(parts)


for i in range(longer_index):
    start_str_divide_remainder = i % start_string_len      # edx
    start_str_char = start_string[start_str_divide_remainder]

    username_divide_remainder = i % username_len
    username_char = username[username_divide_remainder]

    xor_result = chr(ord(username_char) ^ ord(start_str_char))

    xor_divide_remainder = ord(xor_result) % 25
    result_char = chr((xor_divide_remainder + 65) & 0xFF)

    start_string = change_char(start_string, i, result_char)


start_string = insert_every(start_string, 4, "-")

print("\nReg. code is: '%s'" % start_string)
