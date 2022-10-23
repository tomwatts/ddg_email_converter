#!/usr/bin/python3

import sys


if len(sys.argv) < 2:
    print("Not enough arguments")

elif len(sys.argv) == 3:  # Converting to a duck email
    (duck_email, other_email) = sys.argv[1:3]

    converted_email = other_email.replace('@', '_at_') + '_' + duck_email

    print(converted_email)

else:  # Converting from a duck email
    email_address = sys.argv[1]
    chomp_from = email_address.find('@duck.com') - 9  # Address is 8 chars before '@' plus '_' separator

    # TODO: this could be a problem if '_at_' appears in the original address; fix it
    converted_email = email_address[0:chomp_from].replace('_at_', '@')

    print(converted_email)
