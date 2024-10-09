def total_salary(path) -> tuple:
    """
    Calculate the total and average salary from a file.
    Args:
        path (Path): The file path to read the salary data from. The file should contain lines
                    with comma-separated values, where the second value is the salary.
    Returns:
        tuple: A tuple containing the total salary (int) and the average salary (int), or (None, None)
               if the file is not found or an error occurs.
    """
    try:
        with open(path, "r") as file:
            records = [line.strip() for line in file.readlines()]
            total_salary = 0
            valid_records = 0  # Counter for valid records

            for record in records:
                salary_splitted = record.split(",")

                if (
                    len(salary_splitted) < 2
                ):  # if the salary is not in the correct format
                    continue
                try:
                    total_salary += int(salary_splitted[1])
                    valid_records += 1
                except ValueError:  # if the salary is not a number
                    continue

            # Avoid division by zero
            if valid_records == 0:
                average_salary = 0
            else:
                average_salary = total_salary // valid_records

        return total_salary, average_salary

    except FileNotFoundError:
        # Return special value to indicate that the file was not found
        print(f"Error: File not found: {path}")
        return None, None

    except Exception as e:
        # Catch all other potential errors and return None
        print(f"An unexpected error occurred: {e}")
        return None, None
