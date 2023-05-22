# KILLIX - Malicious Code Scanner

KILLIX is a Python program designed to scan Python scripts for potentially malicious code patterns and packages. It provides a simple yet effective way to identify and analyze suspicious code within your Python projects.

## Features

- Scans individual Python files or entire folders for malicious code patterns.
- Detects potentially harmful URLs, keywords, webhooks, invites, pastebin links, suspicious one-liners, and imported packages.
- Optional scan for potentially malicious imported packages/modules.
- Generates informative scan reports for each scanned file.

## Getting Started

1. Clone the repository:

   ```shell
   git clone https://github.com/lopekinz/killix-scanner.git
   ```

2. Install the required dependencies:

   ```shell
   pip install -r requirements.txt
   ```

3. Run the KILLIX scanner:

   ```shell
   python killix.py
   ```

## Usage

1. Enter the file or folder you want to scan when prompted:

   ```shell
   File/Folder: /path/to/your/script.py
   ```

   or

   ```shell
   File/Folder: /path/to/your/folder
   ```

2. Choose whether you want to scan for potentially malicious imported packages/modules:

   ```shell
   Scan modules? (y/n): y
   ```

   The scanner will analyze the specified file or folder for potentially malicious code patterns.

## Scan Results

The KILLIX scanner will provide detailed information about the potentially malicious code patterns found within the scanned file(s).

- URLs: Suspicious URLs detected in the code.
- Keywords: Suspicious keywords identified in the code.
- Webhooks: Suspicious webhooks found in the code.
- Invites: Suspicious invitation links detected in the code.
- Pastebin: Suspicious pastebin links identified in the code.
- Suslines: Suspicious one-liners detected in the code.
- Rats: Potentially harmful code patterns found within one-liners.

If the option to scan for potentially malicious imported packages/modules is enabled, the scanner will also display the imported packages and perform additional scans on them.

## Contributing

Contributions are welcome! If you encounter any issues or have suggestions for improvements, please create a new issue in the [GitHub repository](https://github.com/lopekinz/KILLIX-Scanner).

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

## Credits

KILLIX was created by [Lopekinz](https://github.com/lopekinz).
