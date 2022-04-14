
1. Clone this repo, switch to dev branch, pull changes.
2. Create the .env file in the root with that content:
```
BOT_TOKEN=
DATABASE=mysql+pymysql://username:password@host/db_name
```
3. Create a virtual environment. To do that run the command:

```
python -m venv .venv   # windows
python3 -m venv .venv  # linux or macos
```

:exclamation: If you got the error like "virtualenv : command not found" - that means you don't have the virtualenv package installed. Install it with the command `pip install virtualenv` and go to the start of this step.

Then activate your venv:

(:exclamation: Important! If you're doing it in the VSCode terminal, select the cmd one)

```
.venv\Scripts\activate.bat  # windows
source .venv/bin/activate   # linux or macos
```

:exclamation: Make sure that there's a "(.venv)" title at the start of a terminal path line - that means you've succeeded at venv-activation.

4. Install dependencies:

```
pip install -r requirements.txt
```

5. Enter a bot token in the .env file for the particular key.

6. Run the project with the `python polling.py` command.

Have fun!
