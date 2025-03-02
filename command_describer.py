#!/usr/bin/env python3

import re
from typing import Optional

def describe_command(command: str) -> str:
    """
    Convert a Linux command into a human-readable description.
    
    Args:
        command (str): The Linux command to describe
        
    Returns:
        str: A human-readable description of the command
    """
    # Remove leading/trailing whitespace and handle empty input
    command = command.strip()
    if not command:
        return "Empty command"

    # Split command and arguments
    parts = command.split()
    base_cmd = parts[0]
    
    # Handle sudo prefix
    if base_cmd == "sudo":
        return f"Running with administrative privileges: {' '.join(parts[1:])}"
    
    # File operations
    if base_cmd == "cat":
        return f"Reading {''.join(parts[1:])}"
    elif base_cmd == "cp":
        return f"Copying {parts[1]} to {parts[2]}" if len(parts) >= 3 else "Invalid copy command"
    elif base_cmd == "mv":
        return f"Moving {parts[1]} to {parts[2]}" if len(parts) >= 3 else "Invalid move command"
    elif base_cmd == "rm":
        if "-rf" in parts:
            return f"Forcefully removing directory {parts[-1]} and its contents"
        return f"Removing {' '.join(parts[1:])}"
    
    # Directory operations
    if base_cmd == "cd":
        return f"Changing directory to {parts[1]}" if len(parts) > 1 else "Changing to home directory"
    elif base_cmd == "pwd":
        return "Showing current directory path"
    elif base_cmd == "ls":
        if "-l" in parts:
            return "Listing directory contents in detailed format"
        return "Listing directory contents"
    elif base_cmd == "mkdir":
        return f"Creating directory: {' '.join(parts[1:])}"
    
    # Package management
    if base_cmd in ["apt", "apt-get"]:
        if len(parts) > 1:
            if parts[1] == "install":
                return f"Installing package(s): {' '.join(parts[2:])}"
            elif parts[1] == "remove":
                return f"Removing package(s): {' '.join(parts[2:])}"
            elif parts[1] == "update":
                return "Updating package list"
            elif parts[1] == "upgrade":
                return "Upgrading installed packages"
    
    # SSH commands
    if base_cmd == "ssh":
        return f"Connecting to remote host: {parts[1]}" if len(parts) > 1 else "Invalid SSH command"
    
    # User management
    if base_cmd == "useradd":
        return f"Creating new user: {parts[1]}" if len(parts) > 1 else "Invalid user creation command"
    elif base_cmd == "userdel":
        return f"Deleting user: {parts[1]}" if len(parts) > 1 else "Invalid user deletion command"
    elif base_cmd == "passwd":
        return f"Changing password for user: {parts[1]}" if len(parts) > 1 else "Changing current user password"
    
    # Fallback for unknown commands
    return f"Executing: {command[:97]}..." if len(command) > 100 else f"Executing: {command}"

if __name__ == "__main__":
    # Example usage
    test_commands = [
        "cat file.txt",
        "ls -la",
        "sudo apt-get install python3",
        "rm -rf /tmp/test",
        "ssh user@example.com"
    ]
    
    for cmd in test_commands:
        print(f"Command: {cmd}")
        print(f"Description: {describe_command(cmd)}\n")
