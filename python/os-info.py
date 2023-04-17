import subprocess

# Check RAM usage
ram_output = subprocess.run(['cat', '/proc/meminfo'], stdout=subprocess.PIPE)
if ram_output.returncode == 0:
    output_string = ram_output.stdout.decode('utf-8')
    mem_total = float(output_string.split('\n')[0].split()[1]) / 1024 / 1024
    print(f"RAM: {mem_total:.2f} GB")
else:
    print("Command 'cat' not found.")

# Check number of CPUs
cpu_output = subprocess.run(['nproc'], stdout=subprocess.PIPE)
if cpu_output.returncode == 0:
    print(f"CPUs:\n{cpu_output.stdout.decode('utf-8')}")
else:
    print("Command 'nproc' not found.")

# Check block device report
blockdev_output = subprocess.run(['sudo', 'blockdev', '--report'], stdout=subprocess.PIPE)
if blockdev_output.returncode == 0:
    print(f"blockdev report:\n{blockdev_output.stdout.decode('utf-8')}")
else:
    print("Command 'blockdev' not found or permission denied.")

# Check disk readahead setting for each non-loop disk device
disk_readahead_output = subprocess.run(['lsblk', '-ln', '-o', 'NAME,RA'], stdout=subprocess.PIPE)
if disk_readahead_output.returncode == 0:
    device_names = disk_readahead_output.stdout.decode('utf-8').split('\n')
    for device_name in device_names:
        if 'loop' not in device_name:
            if device_name.strip() != '':
                disk_readahead_output = subprocess.run(['sudo', 'blockdev', '--getra', device_name.split()[0], 'RA'], stdout=subprocess.PIPE)
                if disk_readahead_output.returncode == 0:
                    print(f"Disk readahead setting for {device_name.split()[0]} {disk_readahead_output.stdout.decode('utf-8')}")
                else:
                    print(f"Command 'blockdev' not found or permission denied for device: {device_name.split()[0]}")
else:
    print("Command 'lsblk' not found.")

# Check swap status
swap_output = subprocess.run(['cat', '/proc/meminfo'], stdout=subprocess.PIPE)
if swap_output.returncode == 0:
    output_string = swap_output.stdout.decode('utf-8')
    swap_total = float(output_string.split('\n')[15].split()[1]) / 1024 / 1024
    print(f"Swap status: {swap_total:.2f} GB")
else:
    print("Command 'cat' not found.")

# Check installed Java versions
java_output = subprocess.run(['java', '-version'], stderr=subprocess.PIPE)
if java_output.returncode == 0:
    print(f"Java version:\n{java_output.stderr.decode('utf-8')}")
else:
    print("Java not found.")

# Check OS version
os_version_output = subprocess.run(['lsb_release', '-a'], stdout=subprocess.PIPE)
if os_version_output.returncode == 0:
    print(f"OS version:\n{os_version_output.stdout.decode('utf-8')}")
else:
    print("Command 'lsb_release' not found.")

# Check load average
load_average_output = subprocess.run(['uptime'], stdout=subprocess.PIPE)
if load_average_output.returncode == 0:
    print(f"Load average:\n{load_average_output.stdout.decode('utf-8')}")
else:
    print("Command 'uptime' not found.")

