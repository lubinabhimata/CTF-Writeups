#!/usr/bin/env python

import base64

encoded = '3d3d516343746d4d6d6c315669563362'

# Original Function -> bin2hex(strrev(base64_encode($secret)))

bytes_obj = bytes.fromhex(encoded) # Turn hex to bytes
ascii_string = bytes_obj.decode("ASCII") # Decode to ASCII from bytes

reversed_string = ascii_string[::-1] # Reverse the string

decoded_b64_string = base64.b64decode(reversed_string) # Decode from base64

print(decoded_b64_string.decode()) # Print the decoded string ( .decode() in the end is so that the string doesn't start with the 'b' prefix
