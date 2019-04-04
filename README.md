# 1password-python
A basic wrapper module for the official 1Password command-line tool

## Introduction

This of course, requires that you have the 1Password CLI installed.

* [Installation Instructions](https://support.1password.com/command-line-getting-started/)

* [Download Page](https://app-updates.agilebits.com/product_history/CLI)

Follow the official instructions for installing and setting up the 1Password CLI with your account.

Once that is done, you are ready to rock and roll.

## Usage

1. Using this module is very simple, start by importing it.

```Python
from onepass import OnePass
```

2. Create a `OnePass` object.

```Python
onepass = OnePass()
```

*Note*: This will prompt you for your 1Password CLI Session Token.

This token can be obtained by running `op signin domain --output=raw`.

Alternatively, you can export this session token as an enviroment variable,
and pass it to the constructor of the OnePass object. Whatever you prefer.

*Note*: These tokens expire after 30 minutes of inactivity.

3. Call the desired functions

```Python
onepass.get_credentials("GitHub")
```

See the `test.py` file in this repo for more examples.
