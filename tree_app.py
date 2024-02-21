def generate_tree(levels):
    tree = ''
    max_width = 1 + 2 * (levels - 1) * 2
    tree += ' ' * (max_width // 2) + 'W' + '\n'
    tree += ' ' * (max_width // 2) + '*' + '\n'

    for level in range(1, levels):
        padding = ' ' * ((max_width - (1 + level * 2)) // 2)
        if level % 2 == 0:
            branches = '*' * (1 + level * 2) + '@'
        else:
            branches = '@' + '*' * (level * 2)
        tree += padding + branches + '\n'

    base_padding = ' ' * ((max_width - 5) // 2)
    for _ in range(2):
        tree += base_padding + 'TTTTT' + '\n'

    return tree

def validate_levels(input_value):
    try:
        levels = int(input_value)
        if 3 <= levels <= 1000:
            return levels
        raise ValueError("Number of levels must be between 3 and 1000.")
    except ValueError:
        raise ValueError("Invalid input. Please enter a valid number between 3 and 1000.")

def main():

    while True:
        try:
            levels = validate_levels(input("Enter the number of levels for the Christmas tree (3-1000): "))
            break
        except ValueError as e:
            print(e)

    while True:
        filepath = input("Enter the path to the output file (e.g., /path/to/your/file.txt): ")
        try:
            with open(filepath, 'w') as file:
                tree = generate_tree(levels)
                file.write(tree)
            print(f"Tree with {levels} levels created and saved to {filepath}")
            break

        except Exception as e:
            print(f"An error occurred while trying to write to the file: {e}")
            print("Please make sure the path is correct.")
            print(r"Example of a valid file path: C:\\Users\\YourName\\Desktop\\file_name.txt (Windows) or /home/yourname/file_name.txt (Linux/Mac)")

if __name__ == '__main__':
    main()
