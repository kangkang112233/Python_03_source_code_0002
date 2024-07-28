import re


def process_file(input_file, output_file):
    with open(input_file, "r", encoding="utf-8") as f:
        lines = f.readlines()

    temp = []
    max_length = 0
    result = []

    def extract_parts(line):
        parts = line.split()
        first_part = parts[0]
        second_part = parts[1]
        third_part = " ".join(parts[2:]).strip()
        return first_part, second_part, third_part

    def process_temp(temp, max_length):
        for line in temp:
            first_part, second_part, third_part = extract_parts(line)
            spaces_needed = max_length - len(second_part)
            formatted_line = (
                f"{first_part}    {second_part}{' ' * spaces_needed}    {third_part}"
            )
            result.append(formatted_line + "\n")

    for line in lines:
        if "-->" in line or "<--" in line:
            special_match = re.search(r"(-->|<--)", line)
            special_pos = special_match.end()

            if line[special_pos] != " ":
                temp.append(line)
            else:
                remaining_part = line[special_pos:].strip()
                match = re.search(r"\b[\w_]+\b", remaining_part)
                if match:
                    first_non_empty = match.group(0)
                    rest_of_line = line.split(first_non_empty, 1)[1].strip()
                    new_line = f"{line[:special_pos]}{first_non_empty} {rest_of_line}"
                    temp.append(new_line)
                else:
                    temp.append(line)

            _, second_part, _ = extract_parts(temp[-1])
            max_length = max(max_length, len(second_part))
        else:
            if temp:
                process_temp(temp, max_length)
                temp = []
                max_length = 0
            result.append(line)

    if temp:
        process_temp(temp, max_length)

    with open(output_file, "w", encoding="utf-8") as f:
        f.writelines(result)


input_file = "D:\\2024-01-29-0008_sort_by_creation_date\\2024-07-04-2230_Python_03_source_code_0002\\1000_test.txt"
output_file = "D:\\2024-01-29-0008_sort_by_creation_date\\2024-07-04-2230_Python_03_source_code_0002\\2000_test.txt"
process_file(input_file, output_file)
print("----ok----")
