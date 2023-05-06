#!/usr/bin/env python3

import subprocess

# Define output file name
output_file = "system_info_output.txt"

# Check RAM usage
ram_output = subprocess.run(['cat', '/proc/meminfo'], stdout=subprocess.PIPE)
if ram_output.returncode == 0:
    output_string = ram_output.stdout.decode('utf-8')
    mem_total = float(output_string.split('\n')[0].split()[1]) / 1024 / 1024
    print(f"RAM: {mem_total:.2f} GB")
else:
    with open(output_file, "a") as f:
        f.write("Command 'cat' not found.\n")

# Check number of CPUs
cpu_output = subprocess.run(['nproc'], stdout=subprocess.PIPE)
if cpu_output.returncode == 0:
    print(f"CPUs:\n{cpu_output.stdout.decode('utf-8')}")
else:
    with open(output_file, "a") as f:
        f.write("Command 'nproc' not found.\n")

# Check block device report
blockdev_output = subprocess.run(
    ['sudo', 'blockdev', '--report'], stdout=subprocess.PIPE)
if blockdev_output.returncode == 0:
    print(f"blockdev report:\n{blockdev_output.stdout.decode('utf-8')}")
else:
    with open(output_file, "a") as f:
        f.write("Command 'blockdev' not found or permission denied.\n")

disk_readahead_output = subprocess.run(
    ['lsblk', '-ln', '-o', 'NAME,RA'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
if disk_readahead_output.returncode == 0:
    device_names = disk_readahead_output.stdout.decode('utf-8').split('\n')
    for device_name in device_names:
        if 'loop' not in device_name:
            if device_name.strip() != '':
                disk_readahead_output = subprocess.run(
                    ['sudo', 'blockdev', '--getra', device_name.split()[0], 'RA'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                if disk_readahead_output.returncode == 0:
                    print(
                        f"Disk readahead setting for {device_name.split()[0]} {disk_readahead_output.stdout.decode('utf-8')}")
                else:
                    with open(output_file, "a") as f:
                        f.write(
                            f"Command 'blockdev' not found or permission denied for device: {device_name.split()[0]}\n")
else:
    with open(output_file, "a") as f:
        f.write("Command 'lsblk' not found.\n")

# Check swap status
swap_output = subprocess.run(['cat', '/proc/meminfo'], stdout=subprocess.PIPE)
if swap_output.returncode == 0:
    output_string = swap_output.stdout.decode('utf-8')
    swap_total = float(output_string.split('\n')[15].split()[1]) / 1024 / 1024
    print(f"Swap status: {swap_total:.2f} GB")
else:
    with open(output_file, "a") as f:
        f.write("Command 'cat' not found.\n")

# Check installed Java versions
java_output = subprocess.run(['java', '-version'], stderr=subprocess.PIPE)
if java_output.returncode == 0:
    print(f"Java version:\n{java_output.stderr.decode('utf-8')}")
else:
    with open(output_file, "a") as f:
        f.write("Java not found.\n")

# Check OS version
os_version_output = subprocess.run(['lsb_release', '-a'], stdout=subprocess.PIPE)

if os_version_output.returncode == 0:
    print(f"OS version:\n{os_version_output.stdout.decode('utf-8')}")
else:
    with open(output_file, "a") as f:
        f.write("Command 'lsb_release' not found.\n")

# Check load average
load_average_output = subprocess.run(['uptime'], stdout=subprocess.PIPE)

if load_average_output.returncode == 0:
    print(f"Load average:\n{load_average_output.stdout.decode('utf-8')}")
else:
    with open(output_file, "a") as f:
        f.write("Command 'uptime' not found.\n")

# License
# This script is licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at

# http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.