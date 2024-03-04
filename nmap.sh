#!/bin/bash


while true;  do
  read -p "Enter ip address: " ip
  if [[ $ip =~ ^([1-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.([1-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.([1-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.([1-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$ ]] ; then
    break
  else
    echo "Invalid ip address."
  fi
done


port_args=""
read -p "Enter port or ports range: " ports
if [[ $ports =~ ^[0-9]+$ ]]; then
  # port
  port_args="-p $ports"
elif [[ $ports =~ ^[0-9]+-[0-9]+$ ]]; then
  # port range
  port_args="-p $ports"
else
  echo "Invalid port"
  exit 1
fi

# nmap scan
echo "start scaning ports..."
nmap -sV $port_args $ip &> nmapresults.txt 
cat nmapresults.txt 
if [[ $? -eq 0 ]]; then
  echo "Scanning completed successfully. Results saved in nmapresults.txt"
else 
  #statements
  echo "Scan Error."
fi