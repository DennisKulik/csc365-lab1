
def main():
    file = "students_a.txt"
    by_st_last = {}
    by_t_last = {}
    by_bus = {}
    by_grade = {}

    main_data = parse_file(file, by_st_last, by_t_last, by_bus, by_grade)

    print("main_data:")
    for value in main_data:
        print(value)

    print('')
    print("st_last_data:")
    for key in by_st_last.keys():
        print(key, by_st_last[key])

    print('')
    print("t_last_data:")
    for key in by_t_last.keys():
        print(key, by_t_last[key])

    print('')
    print("bus_data:")
    for key in by_bus.keys():
        print(key, by_bus[key])

    print('')
    print("grade_data:")
    for key in by_grade.keys():
        print(key, by_grade[key])

    bus_52_students = [main_data[i] for i in by_bus[52]]
    for student in bus_52_students:
        print(student)


def parse_file(file_name, by_st_last, by_t_last, by_bus, by_grade):
    main_data = []
    md_idx = 0

    with open(file_name, 'r') as file:
        for line in file:
            split_list = line.split(",")
            add_data(main_data, md_idx, split_list, by_st_last, by_t_last, by_bus, by_grade)
            md_idx += 1
    return main_data


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

    # populates main_data and idx-dicts with student info
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
            main_data[md_idx]["Classroom"] = data

        if i == 4:
            main_data[md_idx]["Bus"] = int(data)
            if int(data) in by_bus:
                by_bus[int(data)].append(md_idx)
            else:
                by_bus[int(data)] = [md_idx]

        if i == 5:
            main_data[md_idx]["GPA"] = float(data)

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


