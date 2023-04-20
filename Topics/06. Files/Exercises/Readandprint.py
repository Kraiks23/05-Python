def add_line_number(input_file, output_file):
    with open(input_file, "r") as input_f, open(output_file, "w")as output_f:
        line_number = 1
        for line in input_f:
            line = line.strip()
            line_number_str = "{:04}".format(line_number)
            output_line = f"{line_number_str} {line}\n"
            output_f.write(output_line)
            line_number += 1


input_file = "C:/Users/Kraiks/Desktop/CLOUD COMPUTING/Python/05-Python/Topics/06. Files/Exercises/text.txt"
output_file = "C:/Users/Kraiks/Desktop/CLOUD COMPUTING/Python/05-Python/Topics/06. Files/Exercises/new_text.txt"

add_line_number(input_file, output_file)
