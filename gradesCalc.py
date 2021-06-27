ID_LENGTH = 8
ID_INDEX = 0
NAME_INDEX = 1
SEMESTER_INDEX = 2
GRADE_INDEX = 3
LOWEST_AVERAGE_GRADE = 50
HIGHEST_AVERAGE_GRADE = 100
NUM_OF_DIGITS = 2
NUM_OF_ELEMENTS = 2


#### PART 1 ####
# final_grade: Calculates the final grade for each student, and writes the output (while eliminating illegal
# rows from the input file) into the file in `output_path`. Returns the average of the grades.
#   input_path: Path to the file that contains the input
#   output_path: Path to the file that will contain the output
def final_grade(input_path: str, output_path: str) -> int:
    if type(input_path) != str or type(output_path) != str:
        raise TypeError('File paths must be strings.')

    data = {}
    with open(input_path, 'r') as input_file:
        for line in input_file:
            if not is_legal_line(line):
                continue

            line = line.replace('\n', '')

            current_data = parse_line(line)
            data[current_data[0]] = current_data[1:]

    
    sum_of_grades = 0

    sorted_keys = list(data.keys())
    sorted_keys.sort()
    
    with open(output_path, 'w') as output_file:
        for key in sorted_keys:
            homework_avg, grade = data[key]
            output_file.write(', '.join((key, str(homework_avg), str(grade))) + '\n')
            sum_of_grades += grade

    if len(sorted_keys) == 0:
        return 0

    return int(sum_of_grades / len(sorted_keys))


# calculate_final_grade: Receives ID number and homework average and calculates the final grade.
def calculate_final_grade(id_number: str, homework_avg: int):
    return int((int(id_number[-NUM_OF_DIGITS:]) + homework_avg) / NUM_OF_ELEMENTS)


# parse_line: Returns a tuple of the form (ID: str, homework_avg: int, final_grade: int), parsed from the line received.
# Note: the line is expected to be legal, so this should be run after is_legal_line.
def parse_line(line: str):
    line = line.split(',')
    line = [remove_trailing_whitespaces(part) for part in line]

    id_number = line[ID_INDEX]
    homework_avg = str(int(line[GRADE_INDEX]))  # Getting rid of trailing zeroes.
    grade = calculate_final_grade(id_number, int(homework_avg))

    return id_number, homework_avg, grade


def remove_trailing_whitespaces(string: str) -> str:
    while string[0] == ' ':
        string = string[1:]

    while string[-1] == ' ':
        string = string[:-1]

    return string


# is_legal_line: Receives a line from the input file as a parameter and checks if it is legal.
def is_legal_line(line: str):
    line = line.split(',')
    line = [remove_trailing_whitespaces(part) for part in line]

    legal_id = is_legal_id(line[ID_INDEX])
    legal_name = is_legal_name(line[NAME_INDEX])
    legal_semester = int(line[SEMESTER_INDEX]) >= 1
    legal_average_grade = LOWEST_AVERAGE_GRADE < int(line[GRADE_INDEX]) <= HIGHEST_AVERAGE_GRADE

    return legal_id and legal_name and legal_semester and legal_average_grade


# is_legal_id: Checks if id_to_check is made of ID_LENGTH digits.
def is_legal_id(id_to_check: str):
    if type(id_to_check) == str:
        return len(id_to_check) == ID_LENGTH and id_to_check[0] != '0' and id_to_check.isdigit()

    return False


# is_legal_name: Checks if name is composed solely of words made of English letters.
def is_legal_name(name: str):
    name = [word for word in name.split(' ') if len(word) > 0]
    return all([word.isalpha() for word in name])


#### PART 2 ####
# check_strings: Checks if `s1` can be constructed from `s2`'s characters.
#   s1: The string that we want to check if it can be constructed
#   s2: The string that we want to construct s1 from
def check_strings(s1: str, s2: str) -> bool:
    s1_histogram = make_histogram(s1)
    s2_histogram = make_histogram(s2)
    letters = [chr(letter) for letter in range(ord('a'), ord('z') + 1)]

    return all([s1_histogram[letter] <= s2_histogram[letter] for letter in letters])


# make_histogram: Creates a dictionary with lowercase English letters mapped to their appearance count in string.
#   string: String to construct a histogram out of.
def make_histogram(string: str) -> dict:
    string = string.lower()
    letters = [chr(letter) for letter in range(ord('a'), ord('z') + 1)]
    letter_count = [string.count(letter) for letter in letters]
    return dict(zip(letters, letter_count))

