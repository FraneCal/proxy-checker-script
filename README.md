# Proxy Checker Script

This repository contains a Python script that automates the process of downloading, validating, and cleaning a list of SOCKS5 proxies. The script fetches a frequently updated proxy list from a GitHub repository, checks the validity of each proxy, and saves the valid ones to a separate file.

## Features

- **Automatic Proxy List Download:** The script automatically downloads the latest proxy list from [TheSpeedX's SOCKS-List repository](https://github.com/TheSpeedX/SOCKS-List).
- **Concurrent Proxy Validation:** Utilizes multithreading to validate proxies in parallel, ensuring faster processing.
- **Filtering and Cleaning:** Proxies that pass validation are saved to a separate file, with any invalid entries being removed.
- **Easy-to-Use:** The script requires minimal setup and can be run directly after downloading the repository.

## How It Works

1. **Download Proxy List:**
   - The script downloads a list of SOCKS5 proxies from [TheSpeedX's SOCKS-List repository](https://github.com/TheSpeedX/SOCKS-List).

2. **Validate Proxies:**
   - Each proxy is tested by making a request to `https://httpbin.org/ip`. If the proxy successfully returns a response, it is considered valid.

3. **Save Valid Proxies:**
   - Valid proxies are saved to `valid_proxies.txt`. Any invalid proxies or improperly formatted entries are discarded.

4. **Clean Up:**
   - After validation, the script cleans the `valid_proxies.txt` file by removing any entries with less than 5 characters, ensuring only valid proxies are stored.

## Usage

1. **Clone the Repository:**

   -  `git clone https://github.com/FraneCal/proxy-checker-script.git`

   -  `cd free-proxy-servers`

2. **Install Dependencies:**

   -  `pip install requests`

3. **Run the Script:**

   -  `python main.py`

4. **Check the Output:**

   -  The valid proxies will be saved in `valid_proxies.txt` in the root directory of the project.

## Customization

   -  **Proxy List Source**: You can change the source of the proxy list by modifying the url variable in the script.
     
   -  **Number of Threads**: Adjust the number of threads used for proxy checking by modifying the range in the thread creation loop.
     
## Contributing

Contributions are welcome! If you have ideas for improvements or encounter any issues, feel free to contribute.
