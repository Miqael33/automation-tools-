#!/bin/bash

echo "Checking for updates..."
sleep 3
sudo apt update 
sudo apt upgrade -y
sudo apt autoremove
sudo apt list --upgradable





