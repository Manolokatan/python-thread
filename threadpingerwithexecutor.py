import concurrent.futures
import os
import time


def ping_server(servername):
    response = os.system('ping -n 1 ' + servername)
    if response == 0:
        print(f'{servername} is up!')
    else:
        print(f'{servername} is Down!')

serverlist = ['google.com','youtube.com','stackoverflow.com']

t1 = time.perf_counter()

with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(ping_server, serverlist) # run map when you want to use a list on variables on the function

t2 = time.perf_counter()

print(f'Finished in {t2-t1} seconds')

