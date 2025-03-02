# Linux Command Describer

A Python utility that converts Linux commands into human-readable descriptions. This tool helps users understand what Linux commands do by providing clear, concise descriptions in plain English.

## Features

- Converts common Linux commands into human-readable descriptions
- Supports a wide range of command types:
  - File operations (cat, cp, mv, rm)
  - Directory operations (cd, ls, mkdir, pwd)
  - Package management (apt, apt-get)
  - SSH commands
  - User management
  - And more...
- Handles sudo commands
- Provides fallback descriptions for unknown commands
- Easy to extend and customize

## Installation

```bash
git clone https://github.com/nonbios-1/linux-command-describer.git
cd linux-command-describer
```

## Usage

```python
from command_describer import describe_command

# Example usage
print(describe_command("cat file.txt"))  # Output: Reading file.txt
print(describe_command("ls -la"))        # Output: Listing directory contents in detailed format
print(describe_command("mkdir test"))     # Output: Creating directory: test
```

## Examples

```python
# File operations
describe_command("cat file.txt")          # Reading file.txt
describe_command("cp source.txt dest.txt") # Copying source.txt to dest.txt
describe_command("rm -rf directory")       # Forcefully removing directory directory and its contents

# Package management
describe_command("sudo apt-get install python3")  # Running with administrative privileges: apt-get install python3
describe_command("apt update")                    # Updating package list

# SSH
describe_command("ssh user@example.com")  # Connecting to remote host: user@example.com

# User management
describe_command("useradd john")          # Creating new user: john
describe_command("passwd mary")           # Changing password for user: mary
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Author

nonbios-1 (nonbios-1@nonbios.ai)
