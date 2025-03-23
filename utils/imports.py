from requests   import get
from os         import mkdir
from os.path    import exists
from zipfile    import ZipFile
from string     import ascii_letters, digits


class CheckImports:
    def __init__(self, code) -> None:
        self.code = code

    def getmodinfo(self, module):
        r = get(f"https://pypi.org/pypi/{module}/json")
        return False if r.status_code == 404 else r.json()["urls"][0]["url"]

    def checkmodule(self, module):
        for i in module:
            if i not in ascii_letters + digits + "_-":
                return False
        
        r = get(f"https://pypi.org/pypi/{module}/json").status_code
        return r == 200 or self.check_if_imported(module)

    def check_if_imported(self, module):
        try:
            __import__(module)
            return True
        except:
            return False


    def _gather_imports(self):
        imports = [lin for lin in self.code.splitlines() if "import" in lin and not any([True for char in ['"', "'", ";", ".", "#"] if char in lin])]
        imports =  [
            imp.replace("import ", ",")
            .replace("from ", "")
            .replace(" ", "")
            .split(",")[0]
            if "from" in imp
            else imp.replace(" ", "")
            .replace("__import__", "")
            .replace("(", "")
            .replace(")", "")
            if "__import__" in imp
            else imp.replace("import ", "").replace(" ", "").split(",")[0]
            for imp in imports
        ]  # from billythegoat356 (i improved it a bit)
        return [imp for imp in imports if  self.checkmodule(imp)]

    def check_import(self, module):
        whitelist = [
            "absl-py"
            "aggdraw"
            "aiofiles"
            "aioflask"
            "aiohttp"
            "aiosignal"
            "altgraph"
            "anyio"
            "appdirs"
            "argon2-cffi"
            "argon2-cffi-bindings"
            "asgiref"
            "asttokens"
            "astunparse"
            "async-class"
            "async-generator"
            "async-timeout"
            "attrs"
            "AuthGG"
            "auto-py-to-exe"
            "backcall"
            "beautifulsoup4"
            "black"
            "blinker"
            "boto3"
            "botocore"
            "botright"
            "bottle"
            "bottle-websocket"
            "Brotli"
            "browser-cookie3"
            "bs4"
            "cachetools"
            "captcha"
            "certifi"
            "cffi"
            "cfscrape"
            "charset-normalizer"
            "click"
            "colorama"
            "colored"
            "Colr"
            "commonmark"
            "contourpy"
            "cryptography"
            "curlify"
            "cursor"
            "cycler"
            "Cython"
            "dangcf"
            "dearpygui"
            "decompyle3"
            "decorator"
            "discord"
            "discord.py"
            "discum"
            "easyocr"
            "Eel"
            "enum34"
            "exceptiongroup"
            "executing"
            "fastapi"
            "filelock"
            "filetype"
            "fire"
            "Flask"
            "Flask-SQLAlchemy"
            "flatbuffers"
            "fonttools"
            "frida"
            "frida-tools"
            "frozenlist"
            "func-timeout"
            "future"
            "gast"
            "gevent"
            "gevent-websocket"
            "gitdb"
            "GitPython"
            "google-auth"
            "google-auth-oauthlib"
            "google-pasta"
            "greenlet"
            "greenletio"
            "grpcio"
            "h11"
            "h2"
            "h5py"
            "hcaptcha-challenger"
            "holehe"
            "hpack"
            "httpcore"
            "httpq"
            "httptools"
            "httpx"
            "huggingface-hub"
            "hyperframe"
            "hypno"
            "idna"
            "ImageHash"
            "imageio"
            "importlib-metadata"
            "imutils"
            "iniconfig"
            "ipython"
            "iso8601"
            "itsdangerous"
            "jedi"
            "Jinja2"
            "jmespath"
            "joblib"
            "Js2Py"
            "kaitaistruct"
            "keptcha"
            "keras"
            "Keras-Applications"
            "Keras-Preprocessing"
            "keyboard"
            "kiwisolver"
            "leakcheck"
            "libclang"
            "loguru"
            "lz4"
            "Markdown"
            "markdown-it-py"
            "MarkupSafe"
            "matplotlib"
            "matplotlib-inline"
            "mdurl"
            "memory-profiler"
            "mitm"
            "MouseInfo"
            "multidict"
            "mypy-extensions"
            "networkx"
            "ninja"
            "nltk"
            "Nuitka"
            "numpy"
            "oauthlib"
            "openai"
            "opencv-contrib-python"
            "opencv-python"
            "opencv-python-headless"
            "opt-einsum"
            "ordered-set"
            "outcome"
            "packaging"
            "pandas"
            "parso"
            "passlib"
            "pathspec"
            "pbr"
            "pefile"
            "pep8"
            "pickleshare"
            "PIL-Tools"
            "Pillow"
            "ping3"
            "plaidml-keras"
            "platformdirs"
            "playwright"
            "playwright-stealth"
            "pluggy"
            "prompt-toolkit"
            "protobuf"
            "psutil"
            "pure-eval"
            "pyarmor"
            "pyasn1"
            "pyasn1-modules"
            "PyAutoGUI"
            "pybboxes"
            "pyclipper"
            "pycparser"
            "pycryptodome"
            "pycryptodomex"
            "pydantic"
            "pydivert"
            "pydub"
            "pyee"
            "PyExecJS"
            "PyGetWindow"
            "Pygments"
            "pyinjector"
            "pyinstaller"
            "pyinstaller-hooks-contrib"
            "pyjsparser"
            "PyMsgBox"
            "pynput"
            "pyobf2"
            "pyOpenSSL"
            "pyparsing"
            "pyperclip"
            "pyppeteer"
            "pypresence"
            "PyQt5"
            "PyQt5-Qt5"
            "PyQt5-sip"
            "PyRect"
            "PyScreeze"
            "pyseto"
            "PySocks"
            "pystyle" # 💀
            "pytesseract"
            "pytest"
            "pytest-base-url"
            "pytest-playwright"
            "python-bidi"
            "python-dateutil"
            "python-dotenv"
            "python-slugify"
            "pytweening"
            "pytz"
            "pytz-deprecation-shim"
            "PyWavelets"
            "pywin32"
            "pywin32-ctypes"
            "PyYAML"
            "redis"
            "regex"
            "replit"
            "requests"
            "requests-oauthlib"
            "requests-toolbelt"
            "rfc3986"
            "rich"
            "rsa"
            "s3transfer"
            "sahi"
            "sanic"
            "sanic-routing"
            "scikit-image"
            "scikit-learn"
            "scipy"
            "scrape-search-engine"
            "seaborn"
            "selenium"
            "selenium-wire"
            "sentence-transformers"
            "sentencepiece"
            "shapely"
            "six"
            "skidbilly"
            "sklearn"
            "smmap"
            "sniffio"
            "soc"
            "socks"
            "sortedcontainers"
            "soupsieve"
            "spark-parser"
            "SpeechRecognition"
            "SQLAlchemy"
            "stack-data"
            "starlette"
            "stdiomask"
            "suds-py3"
            "tensorboard"
            "tensorboard-data-server"
            "tensorboard-plugin-wit"
            "tensorflow"
            "tensorflow-estimator"
            "tensorflow-intel"
            "tensorflow-io-gcs-filesystem"
            "termcolor"
            "terminaltables"
            "text-unidecode"
            "thop"
            "threadpoolctl"
            "tifffile"
            "tinyaes"
            "tls-client"
            "tokenizers"
            "tomli"
            "tomlkit"
            "toolbox"
            "torch"
            "torchvision"
            "tqdm"
            "traitlets"
            "transformers"
            "trio"
            "trio-websocket"
            "TwoCaptcha"
            "typing_extensions"
            "tzdata"
            "tzlocal"
            "ua-parser"
            "uncompyle6"
            "undetected-chromedriver"
            "Unidecode"
            "urllib3"
            "uvicorn"
            "vcrpy"
            "waitress"
            "wcwidth"
            "webdriver-manager"
            "WebOb"
            "websocket-client"
            "websockets"
            "WebTest"
            "Werkzeug"
            "whichcraft"
            "win32-setctime"
            "WMI"
            "wrapt"
            "wsproto"
            "xdis"
            "xvfbwrapper"
            "yarl"
            "yolov5"
            "zipp"
            "zope.event"
            "zope.interface"
            "zstandard"
        ]

        blacklist = ['tkcalendra', 'tkkcalendar', 'tkcalenddar', 'kcalendar', 'tkcalenar', 'tkcaledar', 'tkcaendar', 'ktcalendar', 'tkccalendar', 'tkcaalendar', 'tkcalenndar', 'tkcalednar', 'ttkcalendar', 'tcalendar', 'tkcalendaar', 'tkcaleendar', 'tkcalendr', 'tkcallendar', 'tckalendar', 'tkclaendar', 'tkalendar', 'tkcalnedar', 'tkcalendarr', 'tkclendar', 'tkcalndar', 'tkcaelndar', 'tkcalenda', 'tkaclendar', 'tkcalenadr', 'beautifulsou', 'ebautifulsoup', 'beautifullsoup', 'beautifulsup', 'beautifuulsoup', 'beautifuloup', 'beatifulsoup', 'beauutifulsoup', 'beautiflsoup', 'beautfiulsoup', 'eautifulsoup', 'beuatifulsoup', 'beatuifulsoup', 'bautifulsoup', 'beutifulsoup', 'beauifulsoup', 'beautifulosup', 'beautifusloup', 'beautifusoup', 'beautifulsopu', 'beauitfulsoup', 'beautiffulsoup', 'beautifulsoupp', 'beautiuflsoup', 'beautifulsouup', 'beaautifulsoup', 'beautiifulsoup', 'beautiflusoup', 'beeautifulsoup', 'beautifulsooup', 'beautifulsuop', 'beautifulsop', 'bbeautifulsoup', 'baeutifulsoup', 'beautifulssoup', 'beauttifulsoup', 'beautiulsoup', 'gitypthon', 'giptython', 'gitpythhon', 'gitpythno', 'gitpythonn', 'ggitpython', 'gitpythn', 'gitpyhon', 'pycodesyle', 'ppycodestyle', 'pycodesstyle', 'pycodestylle', 'pycodeestyle', 'pycodestylee', 'pyccodestyle', 'giitpython', 'gtpython', 'gitpyhton', 'pycodstyle', 'gtipython', 'itpython', 'gipython', 'pycodsetyle', 'gitpythoon', 'gitpytthon', 'igtpython', 'gitpyython', 'gitppython', 'pycoedstyle', 'pycodestye', 'gitptyhon', 'gitpyton', 'pycoodestyle', 'gitython', 'pycodetsyle', 'gittpython', 'gitpthon', 'gitpytohn', 'pycodestle', 'pcyodestyle', 'pyycodestyle', 'ycodestyle', 'pcodestyle', 'pyocdestyle', 'pycdoestyle', 'ypcodestyle', 'pycodetyle', 'pyodestyle', 'pycodesttyle', 'pycoddestyle', 'pycoestyle', 'pycodestyl', 'pycodestyyle', 'pycdestyle', 'pycodestyel', 'pycodesytle', 'pycodestlye', 'prompt-toolit', 'prompt-oolkit', 'prompt-toollkit', 'prompt-toolkti', 'propmt-toolkit', 'prompt-toolkkit', 'prompt-toolikt', 'prmopt-toolkit', 'prompt-tooolkit', 'prompt-tooklit', 'rpompt-toolkit', 'prompt-tolkit', 'proompt-toolkit', 'prompt-ttoolkit', 'prompt-tookit', 'prompt-tolokit', 'prrompt-toolkit', 'prompt-toolkitt', 'pormpt-toolkit', 'prompt-otolkit', 'rompt-toolkit', 'propt-toolkit', 'prmpt-toolkit', 'prompt-toolkiit', 'promtp-toolkit', 'pprompt-toolkit', 'prompt-toolkt', 'prompt-toolki', 'promt-toolkit', 'promppt-toolkit', 'pompt-toolkit', 'prommpt-toolkit', 'progreessbar2', 'progressbar22', 'prrogressbar2', 'prgressbar2', 'progressba2', 'progressabr2', 'progresbsar2', 'progerssbar2', 'progrressbar2', 'proggressbar2', 'rogressbar2', 'pprogressbar2', 'rpogressbar2', 'progressbra2', 'prorgessbar2', 'prgoressbar2', 'progressar2', 'progressbarr2', 'progressba2r', 'progressbbar2', 'proogressbar2', 'pogressbar2', 'progressbr2', 'progresssbar2', 'progressbaar2', 'progessbar2', 'porgressbar2', 'proressbar2', 'progresbar2', 'progrsesbar2', 'progrssbar2', 'pysoocks', 'psocks', 'pyscoks', 'pyoscks', 'ypsocks', 'psyocks', 'pysoks', 'pysokcs', 'pyysocks', 'pyssocks', 'pysocs', 'pyscks', 'ysocks', 'pysockss', 'pysocsk', 'pysockks', 'ppysocks', 'pysoccks', 'pyocks', 'psuttil', 'psutill', 'pstil', 'psuutil', 'pustil', 'ppsutil', 'pstuil', 'psuil', 'pssutil', 'discodr-py', 'discod-py', 'idscord-py', 'dscord-py', 'iscord-py', 'discord-y', 'discrod-py', 'diiscord-py', 'disord-py', 'discordd-py', 'discord-ppy', 'discord-pyy', 'disccord-py', 'dicsord-py', 'discord-yp', 'disocrd-py', 'discord-p', 'dicord-py', 'psuti', 'discord-webhhook', 'discord-wehbook', 'disccord-webhook', 'discord-webhoook', 'discord-webbhook', 'iscord-webhook', 'discord-webook', 'dsicord-webhook', 'discor-webhook', 'discord-wehook', 'discordd-webhook', 'discoord-webhook', 'discord-ebhook', 'disocrd-webhook', 'discord-webohok', 'discrd-webhook', 'disscord-py', 'idscord-webhook', 'discord-webhoko', 'ddiscord-py', 'discorrd-webhook', 'discrod-webhook', 'dsicord-py', 'discoord-py', 'discorrd-py', 'discrd-py', 'requests-tooblelt', 'requests-tolbelt', 'equests-toolbelt', 'erquests-toolbelt', 'discord-weebhook', 'disord-webhook', 'diiscord-webhook', 'discodr-webhook', 'dicsord-webhook', 'requess-toolbelt', 'reqeusts-toolbelt', 'discord-wbhook', 'requesst-toolbelt', 'requests-toolbetl', 'requets-toolbelt', 'discord-wwebhook', 'discord-webhookk', 'discord-ewbhook', 'discord-webhoo', 'requuests-toolbelt', 'rrequests-toolbelt', 'discod-webhook', 'disscord-webhook', 'discord-wbehook', 'dscord-webhook', 'discord-webhok', 'ddiscord-webhook', 'dicord-webhook', 'requests-tolobelt', 'requetss-toolbelt', 'requests-toobelt', 'requests-tooleblt', 'requests-toolbeltt', 'rqeuests-toolbelt', 'requests-tooolbelt', 'rquests-toolbelt', 'requests-oolbelt', 'requsts-toolbelt', 'reequests-toolbelt', 'requests-toolbet', 'reqests-toolbelt', 'reuqests-toolbelt', 'requests-toollbelt', 'requestts-toolbelt', 'requests-toolblet', 'reuests-toolbelt', 'requsets-toolbelt', 'requestss-toolbelt', 'requests-ttoolbelt', 'request-toolbelt', 'requests-toolbbelt', 'requests-otolbelt', 'requests-toolbel', 'reqquests-toolbelt', 'requests-toolbellt', 'requests-toolelt', 'requessts-toolbelt', 'requests-toolblt', 'requests-toolbeelt', 'requeests-toolbelt', 'simpleson', 'simplejosn', 'simpplejson', 'simpljeson', 'smiplejson', 'simpejson', 'simplejsoon', 'simplejsson', 'siplejson', 'siimplejson', 'simplesjon', 'simpeljson', 'simplejsonn', 'ismplejson', 'simpleejson', 'sipmlejson', 'simpllejson', 'simplejon', 'simplejsno', 'ssimplejson', 'simpljson', 'simplejsn', 'simlpejson', 'simlejson', 'simplejso', 'implejson', 'simmplejson', 'simplejjson', 'rllib3', 'urrllib3', 'rullib3', 'urllbi3', 'urlli3', 'urllibb3', 'urllb3', 'urlli3b', 'urlliib3', 'uurllib3', 'xlsxwrtier', 'xlsxwrite', 'lsxwriter', 'lxsxwriter', 'xxlsxwriter', 'xlsxwriiter', 'xlsxxwriter', 'xlsxwriterr', 'xlssxwriter', 'xlsxwriteer', 'xlxswriter', 'xlsxrwiter', 'xllsxwriter', 'xlxwriter', 'xlsxwrriter', 'xlsxwritre', 'xlsxriter', 'xlsxwiter', 'xlsxwrier', 'xsxwriter', 'xlswxriter', 'xlsxwwriter', 'xlsxwritr', 'xlsxwrietr', 'xlsxwrter', 'xlsxwritter', 'opeenpyxl', 'openypxl', 'oppenpyxl', 'opnepyxl', 'opennpyxl', 'oopenpyxl', 'openppyxl', 'openpyx', 'openpyyxl', 'openpyxxl', 'openpyxll', 'poenpyxl', 'oenpyxl', 'oepnpyxl', 'openyxl', 'opepyxl', 'openpylx', 'pilloww', 'pllow', 'pilloow', 'ipllow', 'pillw', 'pilllow', 'ppillow', 'pilolw', 'cclick', 'clicck', 'clickk', 'cick', 'clcik', 'clikc', 'lcick', 'cliick', 'weebsocket-client', 'websockte-client', 'websocket-cliet', 'websocket-cclient', 'websocket-cllient', 'wwebsocket-client', 'wbesocket-client', 'wbsocket-client', 'websocket-lcient', 'websoket-client', 'websoocket-client', 'websockket-client', 'ebsocket-client', 'websocket-lient', 'websocket-cient', 'ewbsocket-client', 'webscoket-client', 'wesocket-client', 'webocket-client', 'websockett-client', 'websocket-clien', 'websocket-clinet', 'websocekt-client', 'websokcet-client', 'websocet-client', 'websocket-clieent', 'websocket-clietn', 'websocke-client', 'websocket-cliennt', 'websocket-clientt', 'webbsocket-client', 'webssocket-client', 'weboscket-client', 'websockeet-client', 'wesbocket-client', 'websocket-cleint', 'websoccket-client', 'webscket-client', 'websockt-client', 'websocket-clint', 'aiohtt', 'aiohhttp', 'aiohttpp', 'aioohttp', 'aaiohttp', 'aihottp', 'aohttp', 'iaohttp', 'aiohtpt', 'aiottp', 'aiothtp', 'ypthon-binance', 'pyton-binance', 'ppython-binance', 'pytohn-binance', 'pythno-binance', 'python-binace', 'python-binannce', 'pythoon-binance', 'python-biinance', 'python-binanec', 'pyhon-binance', 'pythhon-binance', 'pytho-binance', 'pythn-binance', 'python-binnance', 'ptyhon-binance', 'python-bniance', 'python-binanc', 'python-binancee', 'pythonn-binance', 'pyhton-binance', 'python-binancce', 'python-biannce', 'pytthon-binance', 'python-bnance', 'python-binnce', 'python-binacne', 'python-binaance', 'python-binnace', 'python-biance', 'python-ibnance', 'python-binane', 'pthon-binance', 'python-inance', 'python-bbinance', 'pyython-binance', 'ython-binance', 'pyttorch', 'pyytorch', 'pytrch', 'pytoch', 'ytorch', 'pygae', 'pgame', 'pyagme', 'pygamme', 'pygaame', 'pyggame', 'pygamee', 'ppygame', 'ygame', 'pygmae', 'pyygame', 'ppytorch', 'ptorch', 'pytorh', 'ptyorch', 'pytorrch', 'pytorcch', 'pytoorch', 'pytocrh', 'pytorchh', 'pndas', 'pandaas', 'pandsa', 'panads', 'panas', 'apndas', 'pnadas', 'ppandas', 'scikit-lern', 'scikit-laern', 'scikitt-learn', 'scikkit-learn', 'scikit-lean', 'scikit-leanr', 'scikit-learrn', 'scikit-learnn', 'sciki-learn', 'scikit-leearn', 'scikit-leaarn', 'scikt-learn', 'scikit-elarn', 'csikit-learn', 'sciikit-learn', 'cikit-learn', 'sciikt-learn', 'scikit-leran', 'scikit-earn', 'scikit-larn', 'scikiit-learn', 'sckiit-learn', 'scikit-lear', 'sikit-learn', 'scikti-learn', 'sickit-learn', 'sciit-learn', 'sccikit-learn', 'sscikit-learn', 'scikit-llearn', 'tnsorflow', 'tensroflow', 'tnesorflow', 'tensorfloow', 'ensorflow', 'tensorflo', 'tenorflow', 'tensoorflow', 'tesorflow', 'tensorfflow', 'tenosrflow', 'pyinsstaller', 'pynistaller', 'ypinstaller', 'pyinstalleer', 'pyinstallerr', 'tensorlfow', 'tensorfllow', 'pyinstallre', 'pyiinstaller', 'piynstaller', 'tesnorflow', 'pyinnstaller', 'pyintaller', 'pyinstalelr', 'teensorflow', 'tensorfloww', 'tensofrlow', 'tenssorflow', 'tensorflwo', 'etnsorflow', 'tensorlow', 'tensorrflow', 'tennsorflow', 'tensorflw', 'sscrapy', 'scarpy', 'srcapy', 'csrapy', 'sccrapy', 'pyisntaller', 'scrapyy', 'scraapy', 'ppyinstaller', 'pyinstallr', 'scrrapy', 'scrpay', 'pyinstalle', 'pyinsaller', 'pyinstalller', 'pinstaller', 'pyyinstaller', 'pyintsaller', 'pyinstaaller', 'pyinsttaller', 'pyinstlaler', 'scray', 'matplotlb', 'matplotliib', 'matplotlibb', 'mtaplotlib', 'matpllotlib', 'mattplotlib', 'matpltlib', 'mtplotlib', 'atplotlib', 'matlotlib', 'mmatplotlib', 'matpplotlib', 'matlpotlib', 'matpoltlib', 'amtplotlib', 'matplolib', 'matplottlib', 'maplotlib', 'matplootlib', 'maatplotlib', 'matpltolib', 'matploltib', 'seleinum', 'seelnium', 'sselenium', 'seleenium', 'eslenium', 'seelenium', 'sellenium', 'selenum', 'seleniumm', 'selennium', 'seleium', 'selneium', 'seleniu', 'seleniium', 'seleniuum', 'selnium', 'sleenium', 'beaautifulsoup4', 'beautiflusoup4', 'beauutifulsoup4', 'beatuifulsoup4', 'beautifullsoup4', 'beautifulssoup4', 'beautifulsoup44', 'beautifulosup4', 'beautiflsoup4', 'bautifulsoup4', 'ebautifulsoup4', 'beautifusloup4', 'beautifulsooup4', 'beeautifulsoup4', 'beautiifulsoup4', 'beautifulsuop4', 'beuatifulsoup4', 'beautifulsop4', 'beautifulsoupp4', 'beautifulsouup4', 'beautifuloup4', 'beautifuulsoup4', 'beautifulsou4', 'beauttifulsoup4', 'beautiulsoup4', 'beutifulsoup4', 'beautiffulsoup4', 'coloramma', 'olorama', 'coloraa', 'colorrama', 'coloorama', 'erquests', 'coloramaa', 'coloarma', 'collorama', 'clorama', 'ccolorama', 'coloama', 'coolrama', 'coorama', 'oclorama', 'websocckets', 'ebsockets', 'wwebsockets', 'webssockets', 'websockest', 'webosckets', 'webscokets', 'websockeets', 'wesbockets', 'websockts', 'websckets', 'websocketts', 'websockes', 'websocets', 'webockets', 'weebsockets', 'webbsockets', 'wesockets', 'websocketss', 'websokcets', 'websockkets', 'websokets', 'wbesockets', 'websoockets', 'websocktes', 'yfiance', 'yyfinance', 'yfinaance', 'yfiannce', 'yfinnance', 'yfiinance', 'yfniance', 'yfinanec', 'yffinance', 'yfinancce', 'yfinnce', 'yfinnace', 'yfinannce', 'yfinancee', 'yfinacne', 'fyinance', 'yfinace', 'yfinane', 'yfnance', 'oslana', 'slana', 'soana', 'soalna', 'solna', 'solanna', 'solaan', 'solaa', 'vpyer', 'yvper', 'vyyper', 'vyperr', 'ssolana', 'vyepr', 'vypper', 'vper', 'olana', 'sollana', 'soolana', 'solanaa', 'solaana', 'solnaa', 'sloana', 'itcoinlib', 'bticoinlib', 'bitcoilnib', 'bitcoinnlib', 'bitocinlib', 'bitcinlib', 'bitcooinlib', 'bitconlib', 'vypre', 'vypeer', 'yper', 'vype', 'vyer', 'vvyper', 'bictoinlib', 'bitcoinlbi', 'bicoinlib', 'bitcoilib', 'bitcionlib', 'bitoinlib', 'btcoinlib', 'bbitcoinlib', 'biitcoinlib', 'bitcoiinlib', 'bittcoinlib', 'bitcoinliib', 'bitcoinlb', 'bitcoinli', 'bitccoinlib', 'bitcoinlibb', 'ibtcoinlib', 'bitconilib', 'crryptocompare', 'cryptocompae', 'cryptocompar', 'crptocompare', 'cryptocomppare', 'cyrptocompare', 'cryptocompre', 'cyptocompare', 'cryptocomprae', 'cryptcompare', 'crytpocompare', 'crypocompare', 'cryptocommpare', 'cryptocomparre', 'rcyptocompare', 'crypotcompare', 'cryptocomparee', 'cryptocomapre', 'cryptcoompare', 'ryptocompare', 'cryptocopare', 'cryptocmpare', 'crypptocompare', 'cryptocomare', 'cryptoocmpare', 'crpytocompare', 'cryptocompaer', 'cryptocopmare', 'cryptocoompare', 'cryptocompaare', 'crypttocompare', 'cryyptocompare', 'cryptoompare', 'cryptoocompare', 'ccryptocompare', 'cryptoccompare', 'cryptocmopare', 'crytocompare', 'ryptofeed', 'cyptofeed', 'cryptoffeed', 'cryptofede', 'cryptofed', 'cryptoofeed', 'crryptofeed', 'crytofeed', 'cyrptofeed', 'ccryptofeed', 'cryptfoeed', 'crytpofeed', 'cryptofeeed', 'crypofeed', 'crypotfeed', 'cryptoefed', 'cryptofee', 'cryptoeed', 'cryptfeed', 'cryptofeedd', 'crypptofeed', 'crpytofeed', 'crypttofeed', 'cryyptofeed', 'rcyptofeed', 'crptofeed', 'freqtraed', 'ffreqtrade', 'rfeqtrade', 'freqtarde', 'freqtrdae', 'frqetrade', 'freqqtrade', 'freqtrde', 'freqtrad', 'freqrade', 'freqtradee', 'freqtrae', 'freqttrade', 'frqtrade', 'freqtrrade', 'fretqrade', 'freqtradde', 'fretrade', 'freqrtade', 'feqtrade', 'freeqtrade', 'freqtraade', 'frreqtrade', 'reqtrade', 'ferqtrade', 'cxct', 'freqtade', 'cxt', 'ccx', 'cccxt', 'ccxtt', 'ccxxt']

        if module in whitelist or self.check_if_imported(module):
            return (True)
        if module in blacklist:
            print("[*] Checking:",module)
            download_url = self.getmodinfo(module)
            if download_url:
                pat     = f"./malicious/{module}"
                
                mkdir(pat) if not exists(pat)  else None
                whl     = get(download_url).content
                path    = f"./malicious/{module}/{module}.whl"

                open(path, "wb").write(whl)
                ZipFile(path).extractall(pat)
                print("[+] Downloaded:",module)
                return (False, pat)
        else:
            print("[*] Checking:",module)
            download_url = self.getmodinfo(module)
            if download_url:
                pat     = f"./malicious/{module}"
                
                mkdir(pat) if not exists(pat)  else None
                whl     = get(download_url).content
                path    = f"./malicious/{module}/{module}.whl"

                open(path, "wb").write(whl)
                ZipFile(path).extractall(pat)
                print("[+] Downloaded:",module)
                return (False, pat)

if __name__ == "__main__":
    file = "C:/Users/kiana/Documents/GitHub/polonium/test.py"
    code = open(file, "r", errors="ignore").read()
    ci = CheckImports(code)
    imports = ci._gather_imports()
    print(len(imports))
    ci.check_imports(imports)
