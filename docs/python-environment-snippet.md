# Python environment & pip

Recommended workflow to avoid mixing Python installations and pip packages.

## Use a per-project virtual environment (recommended)

Keep project dependencies isolated and reproducible.

Example:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Prefer the interpreter's pip

This avoids ambiguity between multiple Python installs:

```bash
python -m pip install <package>
```

## Convenience aliases (interactive shells only)

If you want `python` to mean `python3` in interactive shells, add to your shell rc:

```bash
alias python=python3
alias pip=pip3
```

Notes:

- Aliases affect interactive shells only and won't apply to scripts, CI jobs, or non-interactive shells.
- If you later install a Python version manager (pyenv, conda), consider removing aliases or symlinks to avoid conflicts.

## Check which Python/pip you're using

```bash
which python; python --version
which pip; pip --version
```

## Why this matters for this repo

The analysis scripts live in `analysis/`. Create and activate a venv before running the scripts to keep your global environment clean and avoid accidentally installing packages into the wrong Python installation.
