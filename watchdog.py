#!/bin/env python3.4

from threading import Thread
import os
import subprocess
import time


def watchdog():
    """Launch all the scripts in a folder and wait until completion."""
    scripts_processes = []
    base_dir = os.path.join(os.path.dirname(__file__), 'modules')

    # Launch scripts
    for script in os.listdir(base_dir):
        script = os.path.join(base_dir, script)
        print('** Executing {}'.format(script))
        process = subprocess.Popen(['{}'.format(script)], shell=True, stdout=subprocess.PIPE)
        scripts_processes.append(process)

    # Wait for script completion
    while scripts_processes:
        time.sleep(1)
        for process in scripts_processes:
            ret_code = process.poll()
            if ret_code is not None:
                scripts_processes.remove(process)
                print('** {} finished with code {}'.format(process, ret_code))
            else:
                print('** {} Still running'.format(process))


t = Thread(target=watchdog)
print('## Start watchdog')
t.start()

t.join()
print('## Finish watchdog')
