```markdown
# Contributing

Thank you for your interest in contributing to RMA-Kernel!

Guidelines
- Fork the repository and create a branch named like feature/description or fix/issue-number.
- Keep changes small and focused — one logical change per pull request.
- Run local checks before opening a PR:
  - Format: `black .`
  - Sort imports: `isort --profile black .`
  - Lint: `flake8`
  - Type checks: `mypy src`
  - Tests: `pytest`

Pull Requests
- Base branch: `main`.
- Provide a clear description of what and why.
- Link related issues.
- Add or update tests for new behavior or bug fixes.

Code style
- Follow PEP 8.
- Use type hints where appropriate.
- Add docstrings for public functions/classes.

Large changes
- Open an issue first to discuss design for large or breaking changes.
```
