import subprocess
import json

def run_command(command: str, parseAsJson: bool = True):
    result = subprocess.run(command.split(" "), stdout=subprocess.PIPE)
    if parseAsJson:
        try:
            return json.loads(result.stdout)
        except:
            return None
    return result