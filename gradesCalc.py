
def final_grade(input_path: str, output_path: str) -> int:
    pass

def is_digit(char):
    return char in [str(a) for a in list(range(10))]

def isLegalId(strToCheck):
    return type(strToCheck) == str and len(strToCheck) == 8 and strToCheck[0] != '0' and len([a for a in strToCheck if is_digit(a)]) == len(strToCheck)