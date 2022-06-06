import subprocess
import shlex
import argparse
import sys
import os

REMOTE_HOST = os.getenv("REMOTE_HOST", "docker.whatislove118.xyz")

class ContainersName:
    CRM_BACKEND = f"{REMOTE_HOST}/crm.backend"
    CRM_FRONTEND = f"{REMOTE_HOST}/crm.frontend"
    SPRING_SERVER = f"{REMOTE_HOST}/spring-server"

class Settings:
    Verbose = False

def Run(cmd):
    if Settings.Verbose:
        process = subprocess.Popen(
            shlex.split(cmd),
            stdout=subprocess.PIPE, 
            stderr=subprocess.STDOUT
        )
        while True:
            line = process.stdout.readline().decode('UTF-8', 'replace')
            if line:
                sys.stdout.write(line)
            elif process.poll() is not None:
                break
    else:
        process = subprocess.Popen(shlex.split(cmd), stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        process.wait()

    if process.returncode != 0:
        raise RuntimeError(f"Failed to run '{cmd}'")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Build tool", allow_abbrev=False)
    parser.add_argument('-v', '--verbose', help="Verbose output", action='store_true')
    args = parser.parse_args()

    Settings.Verbose = args.verbose
    
    cmd = f'docker build -t {ContainersName.CRM_BACKEND} remzona47-crm --file remzona47-crm/Dockerfile'
    Run(cmd)
    #cmd = f'docker build -t {ContainersName.SPRING_SERVER} SpringServer --file SpringServer/Dockerfile'
    #Run(cmd)
    
    
    cmd = f'docker push {ContainersName.CRM_BACKEND}'
    Run(cmd)
    #cmd = f'docker push {ContainersName.SPRING_SERVER}'
    #Run(cmd)
    
