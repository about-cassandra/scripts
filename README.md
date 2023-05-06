# System Information Script

This Python script retrieves various system information and prints it to the console. The following information is gathered:

- RAM usage
- Number of CPUs
- Block device report
- Disk readahead setting for each non-loop disk device
- Swap status
- Installed Java versions
- OS version
- Load average

## Requirements

- Python 3.x
- Linux-based operating system

## Usage

1. Clone the repository or download the script.
2. Open a terminal window and navigate to the directory containing the script.
3. Run the script using the following command:

`python system_info.py`

The script will then retrieve and display the requested system information.

## Example output


```yaml
RAM: 16.00 GB
CPUs:
8
blockdev report:
RO    RA   SSZ   BSZ   StartSec            Size   Device
rw   256   512  4096          0    8589934592   /dev/sda
rw   256   512  4096          0    8589934592   /dev/sdb
Disk readahead setting for /dev/sda 256
Disk readahead setting for /dev/sdb 256
Swap status: 7.98 GB
Java version:
openjdk version "11.0.12" 2021-07-20
OpenJDK Runtime Environment 18.9 (build 11.0.12+7)
OpenJDK 64-Bit Server VM 18.9 (build 11.0.12+7, mixed mode)
OS version:
No LSB modules are available.
Distributor ID: Ubuntu
Description:    Ubuntu 20.04.2 LTS
Release:        20.04
Codename:       focal
Load average:
 09:57:32 up  6:54,  1 user,  load average: 0.00, 0.02, 0.00
```