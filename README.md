# Password Checker & Generator

A simple command-line tool built in Python to check password strength and generate secure passwords.

## Features

- **Strength checker**: scores a password from 0 to 6 based on length, uppercase/lowercase letters, numbers, and special characters.
- **Common password detection**: checks the password against a list of commonly leaked passwords.
- **Secure password generator**: creates strong random passwords using Python's `secrets` module (cryptographically secure), with customizable length.

## How it works

The strength score is calculated based on:
- Length >= 8 characters
- Length >= 12 characters
- Contains uppercase letter
- Contains lowercase letter
- Contains number
- Contains special character

## How to run

```bash
python senha.py
```

Then follow the on-screen menu to check or generate a password.

## What I learned

This was my first Python project. Building it helped me practice:
- Conditionals and loops
- Functions with parameters and return values
- File reading (`open`, `with`)
- Python's `secrets` module for secure random generation

## Tech stack

- Python 3