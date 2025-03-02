#!/usr/bin/env python3

import unittest
from command_describer import describe_command

class TestCommandDescriber(unittest.TestCase):
    def test_file_operations(self):
        self.assertEqual(describe_command("cat file.txt"), "Reading file.txt")
        self.assertEqual(describe_command("cp source.txt dest.txt"), "Copying source.txt to dest.txt")
        self.assertEqual(describe_command("rm -rf directory"), "Forcefully removing directory directory and its contents")

    def test_directory_operations(self):
        self.assertEqual(describe_command("ls -la"), "Listing directory contents in detailed format")
        self.assertEqual(describe_command("cd /home"), "Changing directory to /home")
        self.assertEqual(describe_command("mkdir test"), "Creating directory: test")

    def test_package_management(self):
        self.assertEqual(describe_command("apt-get install python3"), "Installing package(s): python3")
        self.assertEqual(describe_command("apt update"), "Updating package list")

    def test_sudo_commands(self):
        self.assertEqual(
            describe_command("sudo apt-get install nginx"),
            "Running with administrative privileges: apt-get install nginx"
        )

    def test_ssh_commands(self):
        self.assertEqual(
            describe_command("ssh user@example.com"),
            "Connecting to remote host: user@example.com"
        )

    def test_fallback(self):
        long_command = "some_unknown_command " + "x" * 100
        self.assertTrue(len(describe_command(long_command)) <= 100)
        self.assertTrue(describe_command(long_command).startswith("Executing:"))

if __name__ == '__main__':
    unittest.main()
