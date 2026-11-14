# Legion-Of-Code
A command-line workout and fitness planning app in Python, built by a 7-person team for **CS 361 (Software Engineering I) at Oregon State University**, Winter 2026. The project follows a full design process (use cases, UAT criteria, UML class diagrams, and activity diagrams in `design/` and `docs/`) alongside the implementation. Mirrored here from the course organization with full commit history.

**My contributions (Kevin Rubio):** set up the initial `src/` project structure, separated the classes, and added the JSON data directory. I designed and implemented the `WorkoutPlan` class and its class diagram, built much of the `Planner`, `Viewer`, `Session`, and `User` logic, and authored the activity diagram (with PlantUML sources) for the rest-day suggestion test case.

## Team Members
- Niki Pandya
- Aron Meraz
- Nolan Flores
- Kevin Rubio
- Noah Letter
- Alex Cortes
- Nolan Cutler

## Project Structure

```
src/
  classes/    # Application logic classes
  models/     # Data classes
  data/       # JSON files containing information such as different exercises and the workout videos
  prog-data/  # Read/Write Dir for data crated during program runtime 
```

## Using
First clone the repo:
```bash
git clone https://github.com/CS361-2026-Winter-Term/Legion-Of-Code
cd Legion-Of-Code
```
At the moment, there is no external dependencies besides a Python3 runtime (we tested with 3.10)

To run the program, cd into the src folder and execute the main.py script:
```
cd src
python3 main.py
```

## Development Setup

**Requirements:** Python 3.10

### 1. Clone the repo
```bash
git clone <repo-url>
cd Legion-Of-Code
```

### 2. Create and activate a virtual environment
```bash
python3.10 -m venv venv
source venv/bin/activate        # macOS/Linux
# venv\Scripts\activate         # Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Format code before committing
We use [Black](https://black.readthedocs.io/) for code formatting (line length 100).
```bash
black src/
```

## Workflow

1. Pull the latest changes from `main`
2. Create a new branch for your work
3. Write code, format with `black src/` before committing
4. If you add a new dependency: `pip freeze > requirements.txt`
5. Commit, push, and open a PR into `main`
