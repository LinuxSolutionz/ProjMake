import os
import argparse
from projmake.project_structure import ProjectStructure

def create_project_structure(language: str, target_directory: str, template: str) -> None:
    """
    Create the project structure based on the provided language and template.

    Args:
        language (str): The programming language for which to create the project structure.
        target_directory (str): The directory where the project structure should be created.
        template (str): The name of the custom template directory within the specified language.

    Raises:
        ValueError: If the provided language or template is invalid.
        FileNotFoundError: If the target directory cannot be found or accessed.
    """
    try:
        structure = ProjectStructure(language, target_directory, template)
        structure.create_structure()
    except ValueError as e:
        print(f"Error: {e}")
    except FileNotFoundError as e:
        print(f"Error: {e}")

def check_directory() -> None:
    """
    Check and create necessary directories for storing project templates.

    Ensures that the following directories exist:
        - ~/.config/projmake
        - ~/.config/projmake/templates
    """
    home_dir = os.path.expanduser("~")
    config_dir = os.path.join(home_dir, ".config")
    projmake_dir = os.path.join(config_dir, "projmake")
    templates_dir = os.path.join(projmake_dir, "templates")
    
    if not os.path.exists(projmake_dir):
        os.makedirs(projmake_dir)
    
    if not os.path.exists(templates_dir):
        os.makedirs(templates_dir)

def main() -> None:
    """
    Main function to parse command-line arguments and initiate the project structure creation.
    
    Parses the following command-line arguments:
        - -l/--lang: The programming language for which to create the project structure (required).
        - -t/--template: The name of a custom template directory within the specified language (optional, default is 'default').
        - target_directory: The directory where the project structure should be created (optional, default is the current directory).

    Calls check_directory to ensure necessary directories exist and then calls create_project_structure.
    """
    parser = argparse.ArgumentParser(description="Project Structure Generator")

    parser.add_argument(
        '-l', '--lang',
        required=True,
        help='Language for which to create the project structure (e.g., python, go, csharp)'
    )
    parser.add_argument(
        '-t', '--template',
        default='default',
        help='Specify a custom template directory within the project language'
    )
    parser.add_argument(
        'target_directory',
        nargs='?',
        default='.',
        help='The directory where the project structure should be created (default: current directory)'
    )

    args = parser.parse_args()
    
    check_directory()
    create_project_structure(args.lang, args.target_directory, args.template)

if __name__ == '__main__':
    main()
