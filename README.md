# Mixed Content Detector

A simple Python script to detect mixed content in URLs using `requests` and `BeautifulSoup`.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Example](#example)
- [Contributing](#contributing)
- [License](#license)

## Introduction

Mixed content occurs when an HTTPS website references insecure (HTTP) resources. Browsers prevent an HTTPS website from loading most insecure resources to maintain the security of the page. This script helps identify and fix or replace mixed content, ensuring your website remains secure.

## Features

- Efficiently detects mixed content in given URLs.
- Uses the power of `requests` and `BeautifulSoup` for web scraping.
- Easy to use and integrate into existing workflows.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/assafv/isMixedContent.git
    cd isMixedContent
    ```

2. Create a virtual environment (optional but recommended):
    ```sh
    python3 -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

3. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Create a text file named `urls.txt` and populate it with the URLs you want to check, each on a new line.

2. Run the script:
    ```sh
    python detect_mixed_content.py
    ```

## Example

Here's an example of how to use the script:

1. Add URLs to `urls.txt`:
    ```
    https://example.com
    https://anotherexample.com
    ```

2. Run the script:
    ```sh
    python detect_mixed_content.py
    ```

3. The script will output any mixed content found in the URLs provided.

## Contributing

Contributions are welcome! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add new feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Open a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
