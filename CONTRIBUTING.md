# CONTRIBUTING

Thank you for your interest in contributing to the project!

### Core Contribution Steps:
1.  **Fork** the repository and create a branch: `feature/your-feature` or `fix/issue-number`.
2.  **Verify** that your branch passes all tests and static analysis locally:
    *   `black .`
    *   `isort --profile black .`
    *   `flake8`
    *   `mypy`
    *   `pytest`
3.  **Describe** your changes in the PR: what was changed, why, and provide a brief usage example if applicable.
4.  **Add tests** for any new features or regression fixes.
5.  **Sign the CLA** (if required by the organization).

### Code Standards:
*   Follow **PEP8**.
*   Use **type hints** wherever possible.
*   Write compact commits with meaningful messages.

### Review Process:
*   PRs should generally contain **one logical task** or fix.
*   For major changes, please **open an issue** first to discuss the design before implementation.
