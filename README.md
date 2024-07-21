
<div align="center"> <h1> Project Structure Generator </h1> </div>

<br />
<div align="center">
  <a href="https://github.com/LinuxSolutionz/ProjMake">
    <img src="https://github.com/user-attachments/assets/83eb9829-a156-4c07-b3f8-5aa51726305a" alt="Logo" width="100" height="100">
  </a>

  <h3 align="center">ProjMake</h3>

  <p align="center">
    Build projects with speed and ease
    <br />
    <a href="https://github.com/LinuxSolutionz/ProjMake"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/LinuxSolutionz/ProjMake#usage">View Demo</a>
    ·
    <a href="https://github.com/LinuxSolutionz/ProjMake/issues">Report Bug</a>
    ·
    <a href="https://github.com/LinuxSolutionz/ProjMake/issues">Request Feature</a>
  </p>
</div>

<a href="https://asciinema.org/a/HrFp2H9L1FRRurxslIzFYerl5" target="_blank"><img src="https://asciinema.org/a/HrFp2H9L1FRRurxslIzFYerl5.svg" /></a>

Welcome to the Project Structure Generator! This tool helps automate the creation of project structures for various programming languages using predefined templates. Whether you're starting a new project or setting up a consistent structure, this tool simplifies the process.

## Table of Contents

- [Documentation](#documentation)
- [How It Works](#how-it-works)
- [Templates Location](#templates-location)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Documentation

The Project Structure Generator provides a flexible way to create project structures based on the programming language and template of your choice. 

### Classes and Methods

- **`Variables`**: Manages global variables like start time and logger time.
- **`Colors`**: Defines color codes for enhancing console output readability.
- **`Logger`**: Handles status logging with formatted messages.
- **`ProjectStructure`**: An abstract base class for creating project structures. You can subclass this to implement language-specific project structures.

For more details, refer to the [source code](path/to/your/source/code).

## How It Works

1. **Initialization**: The `ProjectStructure` class is initialized with the desired programming language, target directory, and template name.
2. **Template Loading**: The tool loads the project structure template from the user's home directory.
3. **Structure Creation**: It creates directories and copies files from the template to the target directory, logging the process with helpful messages.

## Templates Location

Templates are stored in the following directory on your machine:

```
~/.config/projmake/templates/
```

Here, you can find a subdirectory for each supported programming language, and within those directories, you will find the available templates. For example, to create a Python project structure using the "default" template, the tool will look for:

```
~/.config/projmake/templates/python/default/
```

Make sure to place your custom templates in this directory to use them with the tool.

## Installation

To install the Project Structure Generator, follow these steps:

1. **Clone the Repository**:

    ```bash
    git clone https://github.com/LinuxSolutionz/ProjMake.git
    ```

2. **Navigate to the Project Directory**:

    ```bash
    cd ProjMake
    ```

3. **Install the Module**:

    Install the module in editable mode using pip:

    ```bash
    pip install -e .
    ```

    This will install the module and allow you to make changes to the code while the package remains updated.

## Usage

To generate a project structure, use the command line interface. Here are the basic usage instructions:

```bash
projmake -l <language> -t <template> [target_directory]
```

- `-l` or `--lang`: The programming language for which to create the project structure (e.g., `python`, `go`, `csharp`).
- `-t` or `--template`: The custom template directory within the specified language (default is `default`).
- `target_directory`: The directory where the project structure will be created (default is the current directory).

**Example**:

To create a Python project structure using the default template in the current directory:

```bash
projmake -l python
```

To create a Go project structure using a custom template named "mytemplate" in the `~/projects/mygoapp` directory:

```bash
projmake -l go -t mytemplate ~/projects/mygoapp
```

## Contributing

We welcome contributions to improve the Project Structure Generator! To contribute:

1. **Fork the Repository**.
2. **Create a Feature Branch**.
3. **Commit Your Changes**.
4. **Push to the Branch**.
5. **Open a Pull Request**.

Please ensure your code adheres to the project's coding standards and includes appropriate tests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
