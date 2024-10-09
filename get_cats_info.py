def get_cats_info(path) -> list:
    """
    Reads a file containing cat information and returns a list of dictionaries with the cat details.
    Args:
        path (Path): The path to the file containing cat information. Each line in the file should be in the format "id,name,age".
    Returns:
        list: A list of dictionaries, each containing the keys 'id', 'name', and 'age'. If the file is not found or an error occurs, an empty list is returned.
    """

    try:
        with open(path, "r", encoding="utf-8") as file:
            records = [line.strip() for line in file.readlines()]
            cats_info = []

            for record in records:
                cats_info_splitted = record.split(",")

                if (
                    len(cats_info_splitted) < 3
                ):  # if the info is not in the correct format
                    continue
                try:
                    id = cats_info_splitted[0]
                    name = cats_info_splitted[1]
                    age = int(cats_info_splitted[2])
                    print(id, name, age)
                    cats_info.append({"id": id, "name": name, "age": age})

                except ValueError:  # if the age is not a number
                    continue

            return cats_info

    except FileNotFoundError:
        # Return special value to indicate that the file was not found
        print(f"Error: File not found: {path}")
        return []

    except Exception as e:
        # Catch all other potential errors and return empty list
        print(f"An unexpected error occurred: {e}")
        return []


print(get_cats_info(Path("cats.txt")))
