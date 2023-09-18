import threading
import os

def run_script(script_name):
    os.system(f'python3 {script_name}')

scripts = []

scripts.append('5795394157.py')#2023-09-18 12:54:20.983000

scripts.append('5825563253.py')#2023-09-18 09:27:40.628661

scripts.append('5825563253.py')#2023-09-18 08:55:34.187988

scripts.append('5825563253.py')#2023-09-18 01:01:18.871063

scripts.append('5795394157.py')#2023-09-17 23:47:32.536222

scripts.append('5795394157.py')#2023-09-17 23:47:32.536222

scripts.append('5825563253.py')#2023-09-17 23:03:31.486578

scripts.append('5795394157.py')#2023-09-17 21:44:57.272320

scripts.append('5825563253.py')#2023-09-17 21:44:57.272320

scripts.append('5825563253.py')#2023-09-17 21:44:57.272320

threads = []
for script in scripts:
    thread = threading.Thread(target=run_script, args=(script,))
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

