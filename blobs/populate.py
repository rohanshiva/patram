import os
import random
import string

def get_random_string(length):
    # With combination of lower and upper case
    result_str = ''.join(random.choice(string.ascii_letters) for i in range(length))

    return result_str.lower()


content = '''# Gitgame Server

This backend application, built on Python and FastApi, powers the actual Gitgame. Follow the below steps if you want to set it up on your own computer.


## Setup

Ensure you navigate into the server folder
```
cd ./server
```

Ensure you have virtualenv installed
```
pip install virtualenv
```

Create a new virtualenv and install the packages listed in requirements.txt
```
virtualenv venv
pip install -r requirements.txt
```

Before running the tests, we have to locally install the package gitgame (./server/gitgame) into our virtualenv. This is the package which contains the
source code of the application.
```
pip install -e .
```

Run the tests to ensure the files compile by simply running `pytest`
```
pytest
```

The FastApi application can be started by running ./server/main.py.
```
python main.py
```
'''

for i in range(50):
    name = os.path.join(f"{i}.md")
    f = open(name, "w")
    parent = i//10
    front_matter = f"---\nposition: {i}\nname: {get_random_string(4)}\nparent: {parent}\n---\n"
    f.write(front_matter + content + f"this is the {i} doc")
    f.close()