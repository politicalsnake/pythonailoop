
import os
import sys
import shutil
import datetime
import random
import string
import threading
import time
import hashlib

def generate_random_string(length):
    """Generates a random string of specified length."""
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

def calculate_file_hash(filepath):
    """Calculates the SHA-256 hash of a file."""
    hasher = hashlib.sha256()
    try:
        with open(filepath, 'rb') as file:
            while True:
                chunk = file.read(4096)
                if not chunk:
                    break
                hasher.update(chunk)
        return hasher.hexdigest()
    except Exception as e:
        print(f"Error calculating hash for {filepath}: {e}")
        return None

def log_activity(message):
    """Logs activity to a file with timestamp."""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    try:
        with open("activity_log.txt", "a") as log_file:
            log_file.write(f"[{timestamp}] {message}\n")
    except Exception as e:
        print(f"Error writing to log file: {e}")

def simulate_network_activity():
    """Simulates network activity by sleeping for a random time."""
    sleep_time = random.uniform(1, 5)
    time.sleep(sleep_time)
    log_activity(f"Simulated network activity for {sleep_time:.2f} seconds.")

def create_dummy_files(num_files=3):
    """Creates dummy files with random content."""
    for i in range(num_files):
        filename = f"dummy_file_{i}_{generate_random_string(8)}.txt"
        content = generate_random_string(1024)  # 1KB of random content
        try:
            with open(filename, "w") as f:
                f.write(content)
            log_activity(f"Created dummy file: {filename}")
        except Exception as e:
            print(f"Error creating dummy file {filename}: {e}")

def modify_existing_files(num_files=2):
    """Modifies existing files by appending random content."""
    files_to_modify = []
    for root, _, files in os.walk("."):
        for file in files:
            if file.endswith(".txt") and "activity_log.txt" not in file:
                files_to_modify.append(os.path.join(root, file))

    if not files_to_modify:
        log_activity("No text files found to modify.")
        return

    files_to_modify = random.sample(files_to_modify, min(num_files, len(files_to_modify)))

    for filepath in files_to_modify:
        try:
            with open(filepath, "a") as f:
                f.write("\n" + generate_random_string(512))  # Append 512 bytes
            log_activity(f"Modified file: {filepath}")
        except Exception as e:
            print(f"Error modifying file {filepath}: {e}")

def self_replicate(num_copies=2):
    """Creates copies of itself with random names."""
    script_name = os.path.basename(__file__)
    for i in range(num_copies):
        new_name = f"copy_{i}_{generate_random_string(8)}.py"
        try:
            shutil.copyfile(script_name, new_name)
            log_activity(f"Replicated self as: {new_name}")
        except Exception as e:
            print(f"Error replicating self as {new_name}: {e}")

def perform_cleanup():
    """Deletes dummy files created."""
    for root, _, files in os.walk("."):
        for file in files:
            if "dummy_file_" in file:
                filepath = os.path.join(root, file)
                try:
                    os.remove(filepath)
                    log_activity(f"Deleted dummy file: {filepath}")
                except Exception as e:
                    print(f"Error deleting dummy file {filepath}: {e}")

def main():
    """Main function to orchestrate the actions."""
    log_activity("Starting execution.")

    simulate_network_activity()
    create_dummy_files()
    modify_existing_files()
    self_replicate()

    # Simulate a delay before cleanup
    time.sleep(random.uniform(2, 5))
    perform_cleanup()

    log_activity("Execution completed.")

if __name__ == "__main__":
    main()
