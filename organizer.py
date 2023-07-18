import os
import shutil
from pathlib import Path

# Define the categories and their corresponding file extensions
categories = {
    "Documents": [".pdf", ".doc", ".docx", ".txt"],
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Videos": [".mp4", ".avi", ".mov", ".wmv"],
    "Music": [".mp3", ".wav", ".flac"],
    "Archives": [".zip", ".rar", ".tar", ".gz"],
    "Executables": [".exe", ".msi"],
    "Other": []
}

# Find the downloads folder on the system
downloads_dir = str(Path.home() / "Downloads")

# Create the destination directories if they don't exist
destination_dir = os.path.join(downloads_dir, "Organized Downloads")
for category in categories:
    category_dir = os.path.join(destination_dir, category)
    if not os.path.exists(category_dir):
        os.makedirs(category_dir)

# Iterate over the files in the downloads folder
for filename in os.listdir(downloads_dir):
    file_path = os.path.join(downloads_dir, filename)
    if os.path.isfile(file_path):
        # Get the file extension
        file_extension = os.path.splitext(filename)[1].lower()
        # Find the category for the file
        category_found = False
        for category, extensions in categories.items():
            if file_extension in extensions:
                category_dir = os.path.join(destination_dir, category)
                shutil.move(file_path, category_dir)
                category_found = True
                break
        # If no category was found, move the file to the "Other" category
        if not category_found:
            category_dir = os.path.join(destination_dir, "Other")
            shutil.move(file_path, category_dir)
