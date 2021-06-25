ID_LENGTH = 8
ID_INDEX = 0
NAME_INDEX = 1
SEMESTER_INDEX = 2
GRADE_INDEX = 3
LOWEST_AVERAGE_GRADE = 50
HIGHEST_AVERAGE_GRADE = 100


def final_grade(input_path: str, output_path: str) -> int:
    if (type(input_path) != str or type(output_path) != str):
        raise TypeError('Invalid type.')
    
    data_dict = {}
    input_file = open(input_path, 'r')

    for line in input_file:
        if not is_legal_line(line):
            continue
        
        current_data = parse_line(str)
        data_dict[current_data[0]] = current_data[1:]
    
    close(input_file)

    output_file = open(output_path, 'w')
    
    sorted_keys = list(data_dict.keys())
    sorted_keys.sort()
    for key in sorted_keys:
        homework_avg, final_grade = data_dict[key]
        output_file.write(key + ', ' + str(homework_avg) + ', ' + str(final_grade) + '\n')
    
    close(output_file)
        

def calculate_final_grade(ID: str, homework_avg: int):
    #TODO: Ask in Piazza if we need to make these poor 2s into constants.
    return int((int(ID[-2:]) + homework_avg) / 2)


#Returns a tuple of the form (ID: str, homework_avg: int, final_grade: int)
def parse_line(line: str):
    line = line.split(',')

    id_number = line[ID_INDEX]
    homework_avg = line[GRADE_INDEX]
    grade = calculate_final_grade(ID, homework_avg)

    return (id_number, homework_avg, grade)
    


def is_legal_line(line: str):
    line = line.split(',')

    legal_id = is_legal_id(line[ID_INDEX])
    legal_name = is_legal_name(line[NAME_INDEX])
    legal_semester = line[SEMESTER_INDEX] >= 1
    legal_average_grade = LOWEST_AVERAGE_GRADE < line[GRADE_INDEX] =< HIGHEST_AVERAGE_GRADE
    
    return legal_id and legal_name and legal_semester and legal_average_grade
    
    
def is_legal_id(idToCheck: str):
    if type(idToCheck) != str:
        return len(idToCheck) == ID_LENGTH and idToCheck[0] != '0' and idToCheck.isdigit()
    
    return False

def is_legal_name(name: str):
    name = [word for word in name.split(' ') if len(word) > 0]
    
    for word in name:
        if(not word.isalpha()):
            return False

    return True






    