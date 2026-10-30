# ISM2411 — Python for Business

**Name:** Isabella Martinez

**Semester:** Fall 2026

## About This Repo

This repository contains my Python lab assignments for ISM2411. The assignments focus on solving business problems, including calculating taxes, applying customer discounts, and analyzing sales.

## Modules

- `week07/` — Functions, discount and tax calculations, and debugging.
- Module 8 — Git and GitHub setup, version control, and repository documentation.

## How to Run

With Python installed, open a terminal in the repository and run:

```bash
python week07/functions.py
```

The script prints examples of tax calculations, customer discounts, final prices, sales totals, and variable scope.

## AI Assistance

ChatGPT helped organize the repository, add files through GitHub, and draft the documentation and reflection. The Module 7 script retains its original AI assistance disclosure.

## Reflection

### 1. Commit history and work habits

The following is the output of `git log --oneline` from a clone of this repository, captured before adding this reflection:

```text
bacf812 add README with module listing and run instructions
1ef28f9 add module 7 functions: calculate_tax, apply_discount, final_price
49fba87 add .gitignore for Python and OS files
b6dbfbe Initial commit
```

The separate commits make it clear what changed at each step. If I were hiring someone, specific messages like these would help me see that their work is organized and easy to review. Since ChatGPT helped make these commits through GitHub, this history shows how the repository was organized rather than proving that I completed the local Git workflow independently.

### 2. Making edits to a working script

Using Git should help me make smaller changes and save a working version before trying something new. I should test each change and commit it with a clear message, so if something breaks, I can compare versions and find the mistake more easily.

### 3. Another file to ignore

One exclusion I would add is `.venv/`, which is a folder I could use for a local Python virtual environment. It contains installed packages and files tied to the local setup, so it should be recreated on each computer instead of being stored in the repository. This exclusion is included in my .gitignore.
