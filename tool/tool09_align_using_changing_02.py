import re


def process_file(input_file, output_file):
    special_char_pattern = r"(-->|<--)"
    target_pattern = r"\b[\w_]+\b"
    type_pattern = r"\bTYPE\b"

    using_changing_count = 0
    type_count = 0
    parameter_found_in_comment = {}
    actual_parameter_used = set()
    temp_flag = False
    temp = []

    result = []

    def check_and_output_todo():
        nonlocal type_count, using_changing_count, parameter_found_in_comment, actual_parameter_used
        if using_changing_count != type_count:
            temp.append("'TODO: The count of parameters and comments do not match\n")

        sorted_actual_parameter_used = sorted(actual_parameter_used)
        sorted_parameter_found_in_comment = sorted(parameter_found_in_comment.keys())

        actually_used_but_not_in_the_comment = set(sorted_actual_parameter_used) - set(sorted_parameter_found_in_comment)
        in_the_comment_but_not_used = set(sorted_parameter_found_in_comment) - set(sorted_actual_parameter_used)

        for expected in in_the_comment_but_not_used:
            temp.append(
                f"'TODO: Found comment but not parameter       ## {expected} ## \n"
            )

        for target in actually_used_but_not_in_the_comment:
            temp.append(
                f"'TODO: There is no comment for this parameter__ {target} __ \n"
            )

        result.extend(temp)
        temp.clear()
        using_changing_count = 0
        type_count = 0
        parameter_found_in_comment.clear()
        actual_parameter_used.clear()
        actually_used_but_not_in_the_comment.clear()
        in_the_comment_but_not_used.clear()
        sorted_actual_parameter_used.clear()
        sorted_parameter_found_in_comment.clear()

    with open(input_file, "r", encoding="utf-8") as f:
        lines = f.readlines()

    for line in lines:
        special_match = re.search(special_char_pattern, line)

        if special_match:
            using_changing_count += 1
            temp_flag = True
            remaining_part = line[special_match.end():].strip()
            if line[special_match.end()] != " ":
                match = re.match(target_pattern, remaining_part)
                if match:
                    parameter_found_in_comment[match.group(0)] = False
            else:
                remaining_part_split = remaining_part.split()
                if remaining_part_split:
                    parameter_found_in_comment[remaining_part_split[0]] = False

        if temp_flag:
            temp.append(line)
            if re.search(type_pattern, line):
                type_count += 1
                # Find non-empty strings in front of TYPE
                parts = line.split()
                for i in range(1, len(parts)):
                    if parts[i] == "TYPE":
                        actual_parameter_used.add(parts[i - 1])
                        break
            if "." in line:
                temp_flag = False
                check_and_output_todo()
        else:
            result.append(line)

    # Process any remaining lines in temp
    if temp:
        check_and_output_todo()

    with open(output_file, "w", encoding="utf-8") as f:
        f.writelines(result)


input_file = "D:\\2024-01-29-0008_sort_by_creation_date\\2024-07-04-2230_Python_03_source_code_0002\\1000_test.txt"
output_file = "D:\\2024-01-29-0008_sort_by_creation_date\\2024-07-04-2230_Python_03_source_code_0002\\2000_test.txt"
process_file(input_file, output_file)

print("----ok----")
