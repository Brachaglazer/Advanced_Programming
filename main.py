def read_lines(filename):
    stripped_lines = []
    with open(filename, "r") as f:
        for line in f:
            line = line.strip("/n")
            stripped_lines.append(line)  # append each stripped line to a list
        return stripped_lines  # return the list of stripped lines


def normalize_line(line):
    # normalize all records by replacing the ununiformed
    line = line.replace("||", "|").replace(" |", "|").replace("| ", "|")
    line = line.replace("GRADE", "grade").replace("grade =", "grade=").replace("grade= ", "grade=")
    line = line.replace("PROF", "prof").replace("prof: ", "prof:").replace("prof :", "prof:")
    entry = line.split("|")
    entry[2] = entry[2][ : 5] + entry[2][5 : ].title()  # capitalize first letter of prof names
    line = "|".join(entry)
    print(line)
    return line


def parse_record(clean):
    record_list = clean.split("|")
    # check that age is an integer
    if record_list[1].isdigit() == False or int(record_list[1]) < 15 or int(record_list[1]) > 99:
        valid = False
    # check that grade is an integer
    elif record_list[3][6 : ].strip().isdigit() == False or int(record_list[3][6 : ]) < 0 or int(record_list[3][6 : ]) > 100:
        valid = False
    # check that the prof section starts with the word prof: and grade section starts with grade:
    elif record_list[2].startswith("prof:") == False or record_list[3].startswith("grade=") == False:
        valid = False
    else:
        valid = True
    # remove records with missing sections
    for record in record_list:
        if record.strip() == "":
            valid = False
    # only return valid records
    if valid == True:
        return tuple(record_list)
    else:
        return None


def write_clean_records(records, filename):
    # write the cleaned valid records into their own file
    with open(filename, "w") as f:
        clean_file = ""
        for line in records:
            for entry in line:
                clean_file += entry
                if entry == line[-1]:
                    clean_file += "\n"
                else:
                    clean_file += "|"
        f.write(clean_file)


def write_invalid_lines(bad_lines, filename):
    # write the invlaid records into their own file
    with open(filename, "w") as f:
        for line in bad_lines:
            f.write(line)


def average_grade(records):
    # helper to find the average grade
    total = 0
    count = 0
    for entry in records:
        record = list(entry)
        total += float(record[3][6 : ].strip())
        count += 1
    return total/count


def professor_summary(records):
    # helper to find the total amount of students and average grade per prof
    professors = []
    track = []
    for entry in records:
        record = list(entry)
        if record[2][5 : ] not in track:
            track.append(record[2][5 : ])
    for prof in track:
        count = 0
        total_grade = 0
        for entry in records:
            record = list(entry)
            if prof in record[2][5 : ]:
                count += 1
                total_grade += float(record[3][6 : ])
        professors.append((prof, count, total_grade/count))

    print(professors)
    return professors


def top_student_per_prof(records):
    # helper to find the student with the best grade per prof
    professors = []
    track = []
    for entry in records:
        record = list(entry)
        if record[2][5 : ] not in track:
            track.append(record[2][5 : ])
    for prof in track:
        best_grade = None
        best_name = None
        for entry in records:
            record = list(entry)
            if prof in record[2][5 : ]:
                if best_grade == None or int(record[3][6 : ]) > best_grade:
                    best_grade = int(record[3][6 : ])
                    best_name = record[0]
        professors.append((prof, best_name, best_grade))

    print(professors)
    return professors


def write_report(records, filename):
    # write full report into a new file
    with open("invalid_records.txt", "r") as fi:
        invalid_count = 0
        for line in fi:
            invalid_count += 1
    valid_count = 0
    for entry in records:
        valid_count += 1
    with open(filename, "w") as f:
        average = average_grade(records)
        summary = professor_summary(records)
        top_student = top_student_per_prof(records)
        f.write(f'Total valid records: {valid_count} \n')
        f.write(f'Total invalid records: {invalid_count} \n')
        f.write(f'Class average: {average:.2f} \n')
        f.write(f'\nPROFESSOR SUMMARY \n')
        for line in summary:
            collection = ""
            for detail in line:
                if detail == line[0]:
                    collection += detail + " | "
                elif detail == line[1]:
                    collection += "students: " + str(detail) + " | "
                elif detail == line[2]:
                    collection += "avg: " + str(detail)
            f.write(f'{collection} \n')
        f.write(f'\nTOP STUDENT PER PROFESSOR \n')
        for student in top_student:
            complete = ""
            for part in student:
                if part == student[-1]:
                    complete += str(part)
                else:
                    complete += part + " | "
            f.write(f'{complete} \n')


def main():
    # call all functions to run the program
    raw = read_lines("raw_records.txt")

    valid_records = []

    invalid_lines = []

    for line in raw:

        clean = normalize_line(line)
        print(clean)

        rec = parse_record(clean)

        if rec is None:

            invalid_lines.append(line)

        else:

            valid_records.append(rec)
    print(invalid_lines)
    print(valid_records)

    write_clean_records(valid_records, "clean_records.txt")

    write_invalid_lines(invalid_lines, "invalid_records.txt")

    write_report(valid_records, "report.txt")

    print("Done. Wrote clean_records.txt, invalid_records.txt, report.txt")

if __name__ == "__main__":
    main()