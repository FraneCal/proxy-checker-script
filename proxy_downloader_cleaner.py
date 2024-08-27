import requests
import threading
import queue

# URL of the file
url = "https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/socks5.txt"
filename = "proxy_list.txt"
valid_proxies_filename = "valid_proxies.txt"

def download_proxy_list():
    '''
    Function to download the proxy list file from a GitHub repository that is frequently updated.
    '''
    response = requests.get(url)
    if response.status_code == 200:
        with open(filename, "wb") as file:
            file.write(response.content)
        print(f"File downloaded and updated as {filename}")
    else:
        print(f"Failed to download the file. Status code: {response.status_code}")

def clear_valid_proxies_file():
    '''
    Function to clear the content of the valid proxies file
    '''
    with open(valid_proxies_filename, "w") as file:
        file.write("")  # Truncate the file to zero length

def clean_file(filename):
    '''
    Function to read the file that contains validated proxies and to remove the lines that have < 5 characters.
    '''
    with open(filename, "r") as file:
        lines = file.readlines()

    with open(filename, "w") as file:
        for line in lines:
            stripped_line = line.strip()
            if len(stripped_line) >= 5: 
                file.write(line)

def check_proxies():
    '''
    Function to check the validity of proxies.
    '''
    global proxy_queue
    while not proxy_queue.empty():
        proxy = proxy_queue.get()
        try:
            res = requests.get("https://httpbin.org/ip", proxies={"http:":proxy, "https:": proxy})
        except:
            continue
        if res.status_code == 200:
            #print(proxy)
            with threading.Lock():
                with open("valid_proxies.txt", "a") as file:
                    file.write(proxy + "\n")

# Download and update the file; Clear the file valid_proxies.txt data
download_proxy_list()
clear_valid_proxies_file()

proxy_queue = queue.Queue()
valid_proxies = []

# Read the proxy list that is updated from the GitHub repository.
with open("proxy_list.txt", "r") as file:
    proxies = file.read().split("\n")
    for proxy in proxies:
        proxy_queue.put(proxy)

# Create and start threads
threads = []
for _ in range(50):
    thread = threading.Thread(target=check_proxies)
    thread.start()
    threads.append(thread)

# Wait for all threads to finish
for thread in threads:
    thread.join()

# Clean the valid proxies file after all threads have completed
clean_file(valid_proxies_filename)

print("Proxy validation complete and file cleaned.")