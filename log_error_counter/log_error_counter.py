def count_errors(filename):
    count = 0

    with open(filename, "r") as f:
        for line in f:
            if "ERROR" in line:
                count += 1

    return count


print(count_errors("log.txt"))