g"""The script is created by Naman Vij"""
def count_words(filename):
    """
    Counts the number of words in a file.

    Args:
        filename (str): The path to the file to read

    Returns:
        int: The number of words in the file, or None if file doesn't exist
    """
    import os
    print(f"Looking for file: '{filename}'")
    print(f"File exists: {os.path.exists(filename)}")

    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
            words = content.split()
            return len(words)
    except FileNotFoundError:
        print("File doesn't exist")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def main():
    import os
    print(f"Current directory: {os.getcwd()}")
    print("\nFiles in current directory:")
    for file in os.listdir():
        print(f"  - {file}")

    filename = input("\nEnter the filename: ")
    word_count = count_words(filename)
    if word_count is not None:
        print(f"Word count: {word_count}")

if __name__ == "__main__":
    main()
