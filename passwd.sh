#!/bin/bash


length=8

read -p "Enter the password length (minimum 8 characters):: " length

if ! [[ $length =~ ^[0-9]+$ ]]; then
    echo "Invalid entry. Please enter an integer."
    exit 1
fi

if [ $length -lt 8 ]; then
    echo "The default value (8 characters) is used."
    length=8
fi

password=$(tr -dc 'A-Za-z0-9' < /dev/urandom | head -c $length)

echo "Generated password: $password"