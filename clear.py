import os

# List of file extensions to delete
extensions_to_delete = ['.exe', '.exp', '.lib']

# Get the current directory
current_directory = os.getcwd()

# Iterate through files in the current directory
for filename in os.listdir(current_directory):
    # Check if the file has an extension to delete
    if any(filename.endswith(ext) for ext in extensions_to_delete):
        file_path = os.path.join(current_directory, filename)
        try:
            os.remove(file_path)
            print(f"Deleted: {file_path}")
        except Exception as e:
            print(f"Error deleting {file_path}: {e}")
