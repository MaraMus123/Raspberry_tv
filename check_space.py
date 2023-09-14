import shutil

# Specify the path to the directory on the SD card that you want to check
sd_card_directory = 'D:\\'

# Get disk usage statistics for the specified directory
usage = shutil.disk_usage(sd_card_directory)

# Calculate the remaining space in bytes
remaining_space_bytes = usage.free

# Convert bytes to a more human-readable format (e.g., megabytes or gigabytes)
remaining_space_megabytes = remaining_space_bytes / (1024 ** 2)  # Convert to MB

used_space_bytes = usage.used

# Convert bytes to a more human-readable format (e.g., megabytes or gigabytes)
used_space_megabytes = used_space_bytes / (1024 ** 2)  # Convert to MB

# Print the used space
print(f"Used space on SD card: {used_space_megabytes:.2f} MB")
# Print the remaining space
print(f"Remaining space on SD card: {remaining_space_megabytes:.2f} MB")

