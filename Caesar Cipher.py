alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


# TODO-1: Create a function called 'encrypt()' that takes 'original_text' and 'shift_amount' as 2 inputs.

# TODO-2: Inside the 'encrypt()' function, shift each letter of the 'original_text' forwards in the alphabet
#  by the shift amount and print the encrypted text.

for letter in text:
    if direction == "encode":
        ind = alphabet.index(letter)
        if ind + shift <= 25:
            print(alphabet[ind+shift],end="")
        else:
            print(alphabet[ind + shift-26], end="")

    elif direction == "decode":
        ind = alphabet.index(letter)
        if ind - shift >= 0:
            print(alphabet[ind - shift], end="")
        else:
            print(alphabet[26-abs(ind - shift)%25], end="")
    else:
        print("wrong ")

# TODO-4: What happens if you try to shift z forwards by 9? Can you fix the code?

# TODO-3: Call the 'encrypt()' function and pass in the user inputs. You should be able to test the code and encrypt a
#  message.

