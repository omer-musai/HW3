ID_LENGTH = 8
ID_INDEX = 0
NAME_INDEX = 1
SEMESTER_INDEX = 2
GRADE_INDEX = 3
LOWEST_AVERAGE_GRADE = 50
HIGHEST_AVERAGE_GRADE = 100


def final_grade(input_path: str, output_path: str):
    if type(input_path) != str or type(output_path) != str:
        raise TypeError('File paths must be strings.')

    data = {}
    input_file = open(input_path, 'r')

    for line in input_file:
        if not is_legal_line(line):
            continue

        current_data = parse_line(line)
        data[current_data[0]] = current_data[1:]

    input_file.close()

    output_file = open(output_path, 'w')

    sorted_keys = list(data.keys())
    sorted_keys.sort()
    for key in sorted_keys:
        homework_avg, grade = data[key]
        output_file.write(', '.join((key, str(homework_avg), str(grade))) + '\n')

    output_file.close()


def calculate_final_grade(id_number: str, homework_avg: int):
    # TODO: Ask in Piazza if we need to make these poor 2s into constants.
    return int((int(id_number[-2:]) + homework_avg) / 2)


# Returns a tuple of the form (ID: str, homework_avg: int, final_grade: int)
def parse_line(line: str):
    line = line.split(',')

    id_number = line[ID_INDEX]
    homework_avg = line[GRADE_INDEX]
    grade = calculate_final_grade(id_number, int(homework_avg))

    return id_number, homework_avg, grade


def is_legal_line(line: str):
    line = line.split(',')

    legal_id = is_legal_id(line[ID_INDEX])
    legal_name = is_legal_name(line[NAME_INDEX])
    legal_semester = int(line[SEMESTER_INDEX]) >= 1
    legal_average_grade = LOWEST_AVERAGE_GRADE < int(line[GRADE_INDEX]) <= HIGHEST_AVERAGE_GRADE

    return legal_id and legal_name and legal_semester and legal_average_grade


def is_legal_id(id_to_check: str):
    if type(id_to_check) != str:
        return len(id_to_check) == ID_LENGTH and id_to_check[0] != '0' and id_to_check.isdigit()

    return False


def is_legal_name(name: str):
    name = [word for word in name.split(' ') if len(word) > 0]
    return len([word for word in name if not word.isalpha()]) == 0
