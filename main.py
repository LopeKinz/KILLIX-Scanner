from utils.scan import Scan
from utils.imports import CheckImports
from os.path import join
from os import walk

# Logo
LOGO = r"""

 _  ___  _    _    ____  _
/ |/ / \/ \  / \  / \  \//
|   /| || |  | |  | |\  / 
|   \| || |_/\ |_/\ |/  \ 
\_|\_\_/\____|____|_/__/\\


"""

class Checker:
    def __init__(self, scanmodules: bool = False) -> None:
        self.smodules = scanmodules

    def scan_file(self, file: str) -> None:
        print(f"\n[>] Scanning {file}...")

        self.code = open(file, "r", errors="ignore").read()
        self.scanned = Scan(self.code).get_info()

        self.urls = ", ".join(self.scanned["urls"])
        self.keywords = ", ".join(self.scanned["keywords"])
        self.webhooks = ", ".join(self.scanned["webhooks"])
        self.invites = ", ".join(self.scanned["invites"])
        self.pastebin = ", ".join(self.scanned["pastebin"])
        self.suslines, self.rats = ", ".join(self.scanned["oneliner"][0]), ", ".join(self.scanned["oneliner"][1])

        print(f"[!] Urls: {self.urls}") if self.urls else None
        print(f"[!] Keywords: {self.keywords}") if self.keywords else None
        print(f"[!] Webhooks: {self.webhooks}") if self.webhooks else None
        print(f"[!] Invites: {self.invites}") if self.invites else None
        print(f"[!] Pastebin: {self.pastebin}") if self.pastebin else None
        print(f"[!] Suslines: {self.suslines}") if self.suslines else None
        print(f"[!] Rats: {self.rats}") if self.rats else None

        if self.smodules:
            ci = CheckImports(self.code)
            imports = ci._gather_imports()
            print(f"[!] Imports: {', '.join(imports)}")
            for module in imports:
                result = ci.check_import(module)
                # Check if the result is a tuple that can be unpacked
                if isinstance(result, tuple):
                    s, d = result
                    if not s:
                        self.scan_folder(d)
                else:
                    # If result is just a boolean, you can handle it here if needed.
                    # For now, simply skip to the next module.
                    continue

    def scan_folder(self, folder):
        for root, _, files in walk(folder):
            for file in files:
                if file.endswith(".py"):
                    self.scan_file(join(root, file))


if __name__ == "__main__":
    print(LOGO)

    while True:
        print("============== MENU ==============")
        print("1. Scan a File")
        print("2. Scan a Folder")
        print("0. Exit")
        print("===================================")

        choice = input("Enter your choice: ")

        if choice == "1":
            f = input("File: ").strip("'").strip('"').replace("\\", "/")
            sm = input("Scan modules? (y/n): ").lower() == "y"
            checker = Checker(sm)
            checker.scan_file(f)

        elif choice == "2":
            f = input("Folder: ").strip("'").strip('"').replace("\\", "/")
            sm = input("Scan modules? (y/n): ").lower() == "y"
            checker = Checker(sm)
            checker.scan_folder(f)

        elif choice == "0":
            break

        else:
            print("Invalid choice. Please try again.\n")
