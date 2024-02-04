# scrape-bls-canada

## This command will run scrape.py and write its output to output.txt. If output.txt already exists, it will be overwritten

`python scrape.py > output.txt`

## If you want to append to the file instead of overwriting it, use >>:

`python scrape.py >> output.txt`

## Notes:

1. Make sure you are using the correct version of Python. Your command might look like `python3.9 scrape.py`.
2. Make sure you are using the correct version of `chrome_driver_binary`, such as `chromedriver_linux64` for AWS Linux or `chromedriver` for macOS.
3. Update the "APPLICANT DETAILS" section with your own details.

## Comment the following code lines to use GUI

# Maybe needed in some environments where GUI is not available

`options.add_argument('--headless')  # Run Chrome in headless mode`
`options.add_argument('--disable-gpu')  # Disable GPU acceleration`

# Other optional configurations

`options.add_argument('--no-sandbox')  # May be needed in some environments`
`options.add_argument('--disable-dev-shm-usage')  # May be needed in some environments`
