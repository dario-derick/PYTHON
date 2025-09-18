# File Read & Write Challenge 🖋️
# Error Handling Lab 🧪

# Ask the user for the filename
filename = input("Enter the name of the file to read: ")

try:
    

    file = open(filename, "r", encoding="utf-8")
    content = file.read()
    file.close()
except FileNotFoundError:
    print(f"❌ Error: The file '{filename}' was not found.")
    exit()
except PermissionError:
    print(f"❌ Error: You don’t have permission to read '{filename}'.")
    exit()
except Exception as e:
    print(f"❌ Unexpected error: {e}")
    exit()

# Modify the content (convert to uppercase)

modified_content = content.upper()

# New filename

new_filename = "modified_" + filename

try:
    # Write the modified content

    new_file = open(new_filename, "w", encoding="utf-8")
    new_file.write(modified_content)
    new_file.close()

    print(f"✅ Modified file saved as '{new_filename}'")
except Exception as e:
    print(f"❌ Could not write to file: {e}")
