import os
import time
import datetime
from cutepy import HEX
from abc import ABC, abstractmethod

class Variables:
    """Manages global variables used across the application."""
    start_time = time.time()
    logger_time = datetime.datetime.now().strftime("%H:%M:%S")


class Colors:
    """Defines color codes for console output to enhance readability."""
    green = HEX.print("fed0af")
    unic = HEX.print("cccccc")
    time = HEX.print("ff7e88")
    red = HEX.print("c5e2c4")
    reversed = HEX.print("ba033c")
    foreground = HEX.print("cccccc")
    reset = HEX.reset


class Logger:
    """Logs status messages to the console with specific formatting."""
    
    @staticmethod
    def __client_logger__(status: str) -> None:
        """
        Log a status message with formatting.
        
        Args:
            status (str): The status message to be logged.
        """
        log_message = (
            f"{Colors.time}{Variables.logger_time}{Colors.reset} "
            f"{Colors.green}__{Logger.__client_logger__}__{Colors.reset}"
            f"{Colors.foreground} | {status} {Colors.reset}"
        )
        print(log_message)


class ProjectStructure(ABC):
    """Abstract base class for creating a project structure for any programming language."""
    
    def __init__(self, language: str, target_directory: str, template: str = 'default') -> None:
        """
        Initialize the ProjectStructure with the specified language, target directory, and template.
        
        Args:
            language (str): The programming language for which to create the project structure.
            target_directory (str): The directory where the project structure will be created.
            template (str): The name of the template directory within the specified language (default is 'default').
        """
        self.target_directory = target_directory
        self.template = template
        self.language = language

    @abstractmethod
    def create_structure(self) -> None:
        """
        Create the project structure based on the specific implementation.
        This method must be overridden in a subclass.
        """
        pass

    def _is_binary_file(self, file_path: str) -> bool:
        """
        Check if the file is binary based on its extension.
        
        Args:
            file_path (str): The path to the file to check.
        
        Returns:
            bool: True if the file is binary, False otherwise.
        """
        binary_extensions = {'.pyc', '.exe', '.dll', '.so', '.dat'}
        _, ext = os.path.splitext(file_path)
        return ext in binary_extensions

    def _copy_file(self, src_path: str, dest_path: str) -> None:
        """
        Copy a file from the source path to the destination path.
        
        Args:
            src_path (str): The path to the source file.
            dest_path (str): The path where the file will be copied to.
        
        Raises:
            UnicodeDecodeError: If there is an error reading a non-binary file.
        """
        try:
            if self._is_binary_file(src_path):
                with open(src_path, 'rb') as src:
                    content = src.read()
                with open(dest_path, 'wb') as dst:
                    dst.write(content)
            else:
                with open(src_path, 'r', encoding='utf-8') as src:
                    content = src.read()
                with open(dest_path, 'w', encoding='utf-8') as dst:
                    dst.write(content)

            _, filename = os.path.split(src_path)
            dest_dir = os.path.dirname(dest_path)
            Logger.__client_logger__(f"{Colors.unic}╰─ {Colors.reset}{Colors.foreground}Copied file: {filename} to {Colors.red}{dest_dir}{Colors.reset}")
        except UnicodeDecodeError as e:
            Logger.__client_logger__(f"Error reading file: {os.path.basename(src_path)} - {e}")

    def _create_from_template(self, language: str) -> None:
        """
        Create the project structure from a template.
        
        Args:
            language (str): The programming language for which to use the template.
        
        Raises:
            FileNotFoundError: If the template directory does not exist.
        """
        home_dir = os.path.expanduser("~")
        template_base_path = os.path.join(home_dir, ".config", "projmake", "templates", language)
        template_path = os.path.join(template_base_path, self.template)

        if not os.path.exists(template_path):
            raise FileNotFoundError(f"Template directory '{template_path}' does not exist.")
        Logger.__client_logger__(f"{Colors.red}Using template from: {template_path}{Colors.reset}")

        for root, dirs, files in os.walk(template_path):
            relative_path = os.path.relpath(root, template_path)
            dest_dir = os.path.join(self.target_directory, relative_path)

            if not os.path.exists(dest_dir):
                os.makedirs(dest_dir)
                Logger.__client_logger__(f"{Colors.red}Created directory: {os.path.basename(dest_dir)}{Colors.reset}")
            for file_name in files:
                file_path = os.path.join(root, file_name)
                dest_path = os.path.join(dest_dir, file_name)
                self._copy_file(file_path, dest_path)

    def create_structure(self) -> None:
        """
        Create the project structure by checking and using the template.
        Calls _create_from_template to perform the actual creation.
        """
        self._create_from_template(self.language)
