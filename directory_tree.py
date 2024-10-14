from pathlib import Path
import sys
from colorama import Fore, Style

file_icons = {
    ".py": "🐍",       # Python files
    ".txt": "📄",      # Text files
    ".md": "📝",       # Markdown files
    ".html": "🌐",     # HTML files
    ".css": "🎨",      # CSS files
    ".js": "📜",       # JavaScript files
    ".json": "🔧",     # JSON files
    ".xml": "🗂️",     # XML files
    ".csv": "📊",      # CSV files
    ".pdf": "📕",      # PDF files
    ".jpg": "🖼️",     # JPG images
    ".png": "🖼️",     # PNG images
    ".gif": "🎞️",     # GIF images
    ".zip": "🗜️",     # ZIP files
    ".rar": "🗜️",     # RAR files
    ".exe": "⚙️",     # Executable files
    ".bat": "📄",      # Batch files
    ".sh": "💻",       # Shell scripts
    ".mp3": "🎵",      # MP3 files
    ".mp4": "🎬",      # MP4 files
    ".wav": "🔊",      # WAV files
    ".docx": "📄",     # Word documents
    ".xlsx": "📊",     # Excel spreadsheets
    ".pptx": "📽️",    # PowerPoint presentations
    ".sql": "🗃️",     # SQL files
    ".log": "📋",      # Log files
}


def directory_tree(path, indent=0):
    """
    Recursively prints the directory tree structure starting from the given path.

    Args:
        path (str or Path): The root directory path from which to start printing the tree.
        indent (int, optional): The indentation level for nested directories. Defaults to 0.

    Prints:
        The directory tree structure with directories and files. Directories are marked with a folder icon,
        Python files with a snake icon, and other files with a document icon. Handles and prints errors
        for non-existent paths and permission issues.

    Raises:
        FileNotFoundError: If the specified path does not exist.
        PermissionError: If there is a permission issue accessing the specified path.
        Exception: For any other exceptions that occur during execution.
    """

    try:
        path = Path(path)
        for file in path.iterdir():
            if file.is_dir():
                print(f'{" " * (4 * indent)}{Fore.WHITE}└── 📁 {Fore.BLUE}{file.name}/')
                directory_tree(file, indent + 1)
            else:
                print(f'{" " * (4 * indent)}{Fore.WHITE}├── {file_icons.get(file.suffix, "📄")} {Fore.YELLOW}{file.name}')
    except FileNotFoundError:
        print(f"{Fore.RED}The specified path does not exist.")
    except PermissionError:
        print(f"{Fore.RED}Permission denied while accessing the specified path.")
    except Exception as e:
        print(f"{Fore.RED}An error occurred: {e}")

def main():
    if len(sys.argv) < 2:
        print(f"{Fore.RED}Please provide a directory path as an argument.{Style.RESET_ALL}")
    else:
        directory_tree(sys.argv[1])
        
if __name__ == "__main__":
  main()