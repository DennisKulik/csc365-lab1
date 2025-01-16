import sys

INPUT_MAX = 3
BUS_FLAG = 1
NO_BUS_FLAG = 0
NO_GRADE_FLAG = 0
HIGH_GPA_FLAG = 1
LOW_GPA_FLAG = 2
AVG_GPA_FLAG = 3
NUMBER_OF_GRADES = 7
ONE_ARG = 1
TWO_ARGS = 2
THREE_ARGS = 3
def main():
    file = "students.txt"
    by_st_last = {}
    by_t_last = {}
    by_bus = {}
    by_grade = {}

    main_data = parse_file(file, by_st_last, by_t_last, by_bus, by_grade)

    # Check if command-line arguments are passed
    if len(sys.argv) > ONE_ARG:
        input_list = sys.argv[1:]  # ignore sys.argv[0]
        handle_command(input_list, main_data, by_st_last, by_t_last, by_bus, by_grade)
    else:
        # Otherwise, enter interactive mode
        while True:
            user_input = input("Input Command (or type 'Q' to quit): ")
            input_list = user_input.split()

            input_length = len(input_list)

            if input_length > INPUT_MAX:
                print("Too many arguments")
                continue
            elif input_length == 0:
                continue
            if input_list[0] == "Q":
                print("Goodbye!")
                return

            handle_command(main_data, by_st_last, by_t_last, by_bus, by_grade, input_list)


def handle_command(main_data, by_st_last, by_t_last, by_bus, by_grade, input_list):
    first_arg = input_list[0]
    if first_arg == "S:":
        handle_student_lastname(main_data, by_st_last, input_list)
    elif first_arg == "T:":
        handle_teacher_lastname(main_data, by_t_last, input_list)
    elif first_arg == "B:":
        handle_bus(main_data, by_bus, input_list)
    elif first_arg == "G:":
        handle_grade(main_data, by_grade, input_list)
    elif first_arg == "A:":
        handle_average(main_data, by_grade, input_list)
    elif first_arg == "I":
        handle_info(main_data, by_grade)


def handle_info(main_data, by_grade):
    for i in range(NUMBER_OF_GRADES):
        students = search_grade(i, NO_GRADE_FLAG, by_grade, main_data)

        # Check if students is of type [[None]] (has zero students)
        if students == [[None]]:
            print(f"Grade {i}: 0")
        else:
            student_count = len(students)
            print(f"Grade {i}: {student_count}")


def handle_average(main_data, by_grade, input_list):
    input_length = len(input_list)
    if input_length == TWO_ARGS:
        grade = input_list[1]
        if grade.isdigit():
            data = search_grade(int(grade), AVG_GPA_FLAG, by_grade, main_data)
            if data != [[None]]:
                for student in data:
                    print(", ".join(str(x) for x in student))
            else:
                print("No students found for the specified grade.")
    else:
        print("Check Arguments")


def handle_grade(main_data, by_grade, input_list):
    input_length = len(input_list)
    if (input_length == 1) or (input_length > THREE_ARGS):
        print("Check Arguments")
        return
    grade = input_list[1]
    if grade.isdigit():
        data = ""
        if input_length == TWO_ARGS:
            data = search_grade(int(grade), NO_GRADE_FLAG, by_grade, main_data)
        elif input_length == THREE_ARGS:
            flag = input_list[2]
            if flag == "H":
                data = search_grade(int(grade), HIGH_GPA_FLAG, by_grade, main_data)
            elif flag == "L":
                data = search_grade(int(grade), LOW_GPA_FLAG, by_grade, main_data)
            else:
                print("Check Arguments")
                return
        if data != [[None]]:
            for student in data:
                print(", ".join(str(x) for x in student))
        else:
            print("No students found for the specified grade.")
    else:
        print("Check Grade Argument")


def handle_bus(main_data, by_bus, input_list):
    input_length = len(input_list)
    if input_length == TWO_ARGS:
        bus_route = input_list[1]
        if bus_route.isdigit():
            data = search_bus(int(bus_route), by_bus, main_data)
            if data != [[None]]:
                for student in data:
                    print(", ".join(str(x) for x in student))
            else:
                print("No students found for the specified bus route.")
        else:
            print("Check Bus Route Argument")
    else:
        print("Check Arguments")


def handle_teacher_lastname(main_data, by_t_last, input_list):
    input_length = len(input_list)
    if input_length == TWO_ARGS:
        data = search_t_last(input_list[1], by_t_last, main_data)
        if data != [[None]]:
            for student in data:
                print(", ".join(str(x) for x in student))
        else:
            print("No students found for the specified teacher last name.")
    else:
        print("Check Arguments")


def handle_student_lastname(main_data, by_st_last, input_list):
    input_length = len(input_list)
    data = ""

    if input_length == TWO_ARGS:
        data = search_st_last(input_list[1], NO_BUS_FLAG, by_st_last, main_data)
    elif input_length == THREE_ARGS:
        if input_list[2] == "B":
            data = search_st_last(input_list[1], BUS_FLAG, by_st_last, main_data)
        else:
            print("Check Arguments")
            return
    else:
        print("Check Arguments")
        return

    if data != [[None]]:
        for student in data:
            print(", ".join(str(x) for x in student))
    else:
        print("No students found for the specified last name.")

    #
    # print("main_data:")
    # for value in main_data:
    #     print(value)
    #
    # print('')
    # print("st_last_data:")
    # for key in by_st_last.keys():
    #     print(key, by_st_last[key])

    # print('')
    # print("t_last_data:")
    # for key in by_t_last.keys():
    #     print(key, by_t_last[key])
    #
    # print('')
    # print("bus_data:")
    # for key in by_bus.keys():
    #     print(key, by_bus[key])
    #
    # print('')
    # print("grade_data:")
    # for key in by_grade.keys():
    #     print(key, by_grade[key])
    #
    # test_list = search_st_last("COOKUS", 1, by_st_last, main_data)
    # print("student test", test_list)

    # test_list = search_t_last("FAFARD", by_t_last, main_data)
    # print("teacher test", test_list)

    # test_list = search_grade(6, 0, by_grade, main_data)
    # print("grade test0", test_list)
    #
    # test_list = search_grade(6, 1, by_grade, main_data)
    # print("grade test1", test_list)
    #
    # test_list = search_grade(6, 2, by_grade, main_data)
    # print("grade test2", test_list)
    #
    # test_list = search_grade(6, 3, by_grade, main_data)
    # print("grade test3", test_list)

    # test_list = search_bus(52, by_bus, main_data)
    # print("test", test_list)


# returns list of lists, if bus == 0, nested lists look like
# [StLastName, StFirstName, Grade, Classroom, TLastName, TFirstName]
# if bus == 1, nested lists look like
# [StLastName, StFirstName, Bus]
# if last name does not exist, returns [[None]]
def search_st_last(lastname, bus, by_st_last, main_data):
    if lastname in by_st_last:
        students = [main_data[i] for i in by_st_last[lastname]]
    else:
        return [[None]]

    outlist = []
    if bus:
        for student in students:
            info = [
                student["StLastName"],
                student["StFirstName"],
                student["Bus"]]
            outlist.append(info)
    else:
        for student in students:
            info = [
                student["StLastName"],
                student["StFirstName"],
                student["Grade"],
                student["Classroom"],
                student["TLastName"],
                student["TFirstName"]]
            outlist.append(info)
    return outlist


# returns list of lists, nested lists look like
# [StLastName, StFirstName]
# if last name does not exist, returns [[None]]
def search_t_last(lastname, by_t_last, main_data):
    if lastname in by_t_last:
        students = [main_data[i] for i in by_t_last[lastname]]
    else:
        return [[None]]

    outlist = []
    for student in students:
        info = [
            student["StLastName"],
            student["StFirstName"],
            # student["Grade"],
            # student["Classroom"],
            # student["TLastName"],
            # student["TFirstName"]
            ]
        outlist.append(info)
    return outlist


# returns list of lists, if modifier == 0, nested lists look like
# [StLastName, StFirstName]
# if modifier == 1 or 2, nested list looks like
# [StLastName, StFirstName, Bus, GPA, TLastName, TFirstName]
# if modifier == 3, nested list looks like
# [avg GPA as a float]
# if grade does not exist, returns [[None]]
def search_grade(grade, modifier, by_grade, main_data):
    if grade in by_grade:
        students = [main_data[i] for i in by_grade[grade]]
    else:
        return [[None]]

    outlist = []
    if modifier == 0:
        for student in students:
            info = [
                student["StLastName"],
                student["StFirstName"]]
            outlist.append(info)
    elif modifier == 1:
        highest_student = None
        highest = 0.0

        for student in students:
            gpa = float(student["GPA"])
            if gpa > highest:
                highest = gpa
                highest_student = student
        info = [
            highest_student["StLastName"],
            highest_student["StFirstName"],
            highest_student["Bus"],
            highest_student["GPA"],
            highest_student["TLastName"],
            highest_student["TFirstName"]]
        outlist.append(info)
    elif modifier == 2:
        lowest_student = None
        lowest = 32768.0

        for student in students:
            gpa = float(student["GPA"])
            if gpa < lowest:
                lowest = gpa
                lowest_student = student
        info = [
            lowest_student["StLastName"],
            lowest_student["StFirstName"],
            lowest_student["Bus"],
            lowest_student["GPA"],
            lowest_student["TLastName"],
            lowest_student["TFirstName"]]
        outlist.append(info)
    else:
        sum_nums = 0
        num_nums = 0

        for student in students:
            sum_nums += float(student["GPA"])
            num_nums += 1
        avg = sum_nums / num_nums
        avg = round(avg, 2)
        outlist.append([avg])

    return outlist


# returns list of lists, nested lists look like
# [StLastName, StFirstName, Grade, Classroom]
# if bus does not exist, returns [[None]]
def search_bus(bus, by_bus, main_data):
    if bus in by_bus:
        students = [main_data[i] for i in by_bus[bus]]
    else:
        return [[None]]

    outlist = []
    for student in students:
        info = [
            student["StLastName"],
            student["StFirstName"],
            student["Grade"],
            student["Classroom"]]
        outlist.append(info)
    return outlist


def parse_file(file_name, by_st_last, by_t_last, by_bus, by_grade):
    main_data = []
    md_idx = 0

    with open(file_name, 'r') as file:
        for line in file:
            split_list = line.split(",")
            add_data(main_data, md_idx, split_list, by_st_last, by_t_last, by_bus, by_grade)
            md_idx += 1
    return main_data


# populates main_data and idx-dicts with student info
def add_data(main_data, md_idx, student_info, by_st_last, by_t_last, by_bus, by_grade):
    student_dict = {
        "StLastName": None,
        "StFirstName": None,
        "Grade": None,
        "Classroom": None,
        "Bus": None,
        "GPA": None,
        "TLastName": None,
        "TFirstName": None}
    main_data.append(student_dict)

    for i, data in enumerate(student_info):

        # determines which field to populate using i
        if i == 0:
            main_data[md_idx]["StLastName"] = data

            # populates by_st_last dict with the last name as the key
            # by_st_last will contain a list of main_data indices with the matching student last name
            if data in by_st_last:
                by_st_last[data].append(md_idx)
            else:
                by_st_last[data] = [md_idx]

        if i == 1:
            main_data[md_idx]["StFirstName"] = data

        if i == 2:
            main_data[md_idx]["Grade"] = int(data)
            if int(data) in by_grade:
                by_grade[int(data)].append(md_idx)
            else:
                by_grade[int(data)] = [md_idx]

        if i == 3:
            main_data[md_idx]["Classroom"] = int(data)

        if i == 4:
            main_data[md_idx]["Bus"] = int(data)
            if int(data) in by_bus:
                by_bus[int(data)].append(md_idx)
            else:
                by_bus[int(data)] = [md_idx]

        if i == 5:
            main_data[md_idx]["GPA"] = data

        if i == 6:
            main_data[md_idx]["TLastName"] = data
            if data in by_t_last:
                by_t_last[data].append(md_idx)
            else:
                by_t_last[data] = [md_idx]

        if i == 7:
            data = data.strip()
            main_data[md_idx]["TFirstName"] = data


if __name__ == "__main__":
    main()
