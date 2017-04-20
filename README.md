# PWGEN

## Overview

This script will generate a high quality (cryptographic) random password.

## Usage
    -h, --help            show this help message and exit
    -l LENGTH, --length LENGTH
                        Password length
    -q QUANTITY, --quantity QUANTITY
                        The number of passwords you want to be generated
    -c COMPLEXITY, --complexity COMPLEXITY
                        Defines if you want special characters in your
                        password

## Example

Generates a 15 character password:

    pwgen.py
    F58D53hz3c@J@8%

Generates 3 times a 20 character password:

    pwgen.py -q 3 -l 20
    3XClLh#kx@cXqzx5pq9V
    @n!5Po%Ka6BcQ*GV(27G
    DT1tH)fmAJj0cqhiPOc8
    
Generates a less complex password without special characters

    pwgen.py -l 10 -q 1 -c 0
    Ym8Qz9vwWC

## Contact

You can contact me via mail: [mail@sysadmin-log.de](mail@sysadmin-log.de)
