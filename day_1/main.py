# replace words with digit in the name, but ensure the last character of the word is preseved to keep overlaps present and thus overlaps are counted
numbers_map = {"one": "o1ne", "two": "t2wo", "three": "t3hree", "four": "f4our", "five": "f5ive", "six": "s6ix", "seven": "s7even", "eight": "e8ight", "nine": "n9ine"}

def main():
    with open("input.txt", "r") as f:
        input_data = f.read().splitlines()

    Part 1
    calibration_numbers = []
    for row in input_data:
        number = []
        # Search from start and break at first digit
        for char in row:
            if char.isdigit():
                number.append(char)
                break
        # Repeat from end to get last digit
        for char in row[-1::-1]:
            if char.isdigit():
                number.append(char)
                break
        # Join the 2 numbers and convert to int
        result = int("".join(number))
        # Add the final result for that row to the list
        calibration_numbers.append(result)
    print(sum(calibration_numbers))

    # Part 2
    calibration_numbers = []
    for row in input_data:
        # Replace the numbers with their strings
        for key, value in numbers_map.items():
            row = row.replace(key, str(value))
        print(row)
        # Repeat the same process as in part 1
        number = []
        for char in row:
            if char.isdigit():
                number.append(char)
                break
        for char in row[-1::-1]:
            if char.isdigit():
                number.append(char)
                break
        result = int("".join(number))
        calibration_numbers.append(result)
    print(sum(calibration_numbers))

if __name__ == "__main__":
    main()
