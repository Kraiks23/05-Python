def count_letter(letter, string):
    count = 0
    for char in string:
        if char == letter:
            count += 1
    return count


fruit = "banana"    
print(count_letter("a", fruit))

game = "League of Legends"
print(count_letter("e", game))

