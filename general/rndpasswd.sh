#!/bin/bash

# Just alphanumeric characters
charSet="[:alnum:]"

cat /dev/urandom | tr -cd "$charSet" | head -c $1