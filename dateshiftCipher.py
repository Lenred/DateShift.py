### meant to do date shift cipher automatically

# Create the alphabet lookup table
alphabet_lookup = {letter: index + 1 for index, letter in enumerate("abcdefghijklmnopqrstuvwxyz")}

def shift_letter(letter, shift):
    if letter.lower() in alphabet_lookup:
        shifted_index = (alphabet_lookup[letter.lower()] + shift) % 26
        if shifted_index == 0:
            shifted_index = 26
        for key, value in alphabet_lookup.items():
            if value == shifted_index:
                return key.upper() if letter.isupper() else key
    else:
        return letter

def main():
    # Get date and text from user
    date_input = input("date: ")
    text_input = input("text: ")

    # Process the date input
    date_list = [int(digit) for digit in date_input if digit.isdigit()]

    # Create a list from the input text
    text_list = list(text_input)

    # Initialize final list to store the result
    final_list = []

    # Loop through the text to apply the cipher
    for i in range(len(text_list)):
        shift_value = date_list[i % len(date_list)]
        shifted_letter = shift_letter(text_list[i], shift_value)
        final_list.append(shifted_letter)

    # Assemble and print the final text
    final_text = "".join(final_list)
    print(f"Scrambled text: {final_text}")

if __name__ == "__main__":
    main()
