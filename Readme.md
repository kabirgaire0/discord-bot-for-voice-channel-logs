Discord bot for voice channel logs.

## HOW TO RUN

On linux :
```
source ./run.sh
```
or on windows (run with git bash) :
```
./run.sh
```

Details:

Steps:
Create a virtual environment in your project directory:
```
python3 -m venv venv
```
This will create a directory named venv where the virtual environment will be stored.

Activate the virtual environment:

On Linux/Mac:
```
source venv/bin/activate
```

On Windows:
```
venv\Scripts\activate
```

Install the required packages using pip inside the virtual environment:
```
pip install .
```

Since you are now in an isolated environment, the externally-managed-environment error won't occur.

When you are done working, deactivate the virtual environment:
```
deactivate
```
