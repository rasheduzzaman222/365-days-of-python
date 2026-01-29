def analyze_log(file_path):
    error_count = 0
    warning_count = 0

    with open(file_path, "r") as file:
        for line in file:
            if "ERROR" in line:
                error_count += 1
            elif "WARNING" in line:
                warning_count += 1

    return {
        "errors": error_count,
        "warnings": warning_count
    }


if __name__ == "__main__":
    result = analyze_log("sample.log")
    print(result)
