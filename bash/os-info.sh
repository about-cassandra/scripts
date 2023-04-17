#!/bin/bash

# Check RAM usage
mem_total=$(cat /proc/meminfo | grep "MemTotal" | awk '{print $2}')
ram=$(echo "scale=2; $mem_total/1024/1024" | bc)
echo "RAM: $ram GB"

# Check number of CPUs
cpus=$(nproc)
echo "CPUs: $cpus"

# Check block device report
sudo blockdev --report | grep -v loop

# Check disk readahead setting for each non-loop disk device
disk_list=$(lsblk -ln -o NAME | grep -v loop)
for disk_name in $disk_list; do
    echo "$disk_name:   $(sudo blockdev --getra /dev/$disk_name)"
done

# Check swap status
swap_total=$(cat /proc/meminfo | grep "SwapTotal" | awk '{print $2}')
swap=$(echo "scale=2; $swap_total/1024/1024" | bc)
echo "Swap status: $swap GB"

# Check installed Java versions
java -version

# Check OS version
lsb_release -a

# Check load average
uptime
