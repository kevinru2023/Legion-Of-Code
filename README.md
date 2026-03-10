# Legion-Of-Code
The Legion Of Code CS361 group repository.

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
  data/       # JSON data files
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
