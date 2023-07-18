import os
import shutil
import tempfile
import unittest
from pathlib import Path

class TestDownloadOrganizer(unittest.TestCase):
    def setUp(self):
        # Create a temporary directory for testing
        self.test_dir = tempfile.mkdtemp()
        # Create some test files with different extensions
        self.test_files = [
            "document1.pdf",
            "document2.docx",
            "image1.jpg",
            "image2.png",
            "video1.mp4",
            "video2.avi",
            "music1.mp3",
            "music2.wav",
            "archive1.zip",
            "archive2.rar",
            "executable1.exe",
            "executable2.msi",
            "other1.xyz",
            "other2"
        ]
        for filename in self.test_files:
            file_path = os.path.join(self.test_dir, filename)
            with open(file_path, "w") as f:
                f.write("test")
    
    def tearDown(self):
        # Remove the temporary directory and its contents
        shutil.rmtree(self.test_dir)
    
    def test_download_organizer(self):
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
        downloads_dir = self.test_dir
        
        # Create the destination directories if they don't exist
        destination_dir = os.path.join(downloads_dir, "Organized Downloads")
        for category in categories:
            category_dir = os.path.join(destination_dir, category)
            if not os.path.exists(category_dir):
                os.makedirs(category_dir)
        
        # Organize the test files
        for filename in self.test_files:
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
        
        # Check that the files are organized correctly
        for category, extensions in categories.items():
            category_dir = os.path.join(destination_dir, category)
            for filename in os.listdir(category_dir):
                file_extension = os.path.splitext(filename)[1].lower()
                self.assertIn(file_extension, extensions)
            for filename in os.listdir(downloads_dir):
                file_extension = os.path.splitext(filename)[1].lower()
                if file_extension not in extensions and file_extension != "":
                    self.assertEqual(category, "Other")
    
if __name__ == "__main__":
    unittest.main()
