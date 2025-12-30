import subprocess

commands = [
    ["docker-compose", "down"],
    ["docker-compose", "up", "-d"]
]

for cmd in commands:
    try:
        subprocess.run(cmd, check=True)
        print("Executed:", " ".join(cmd))
    except subprocess.CalledProcessError:
        print("Failed:", " ".join(cmd))
        exit(1)
