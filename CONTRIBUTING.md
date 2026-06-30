# Contributing to Prodev SLAM Jazzy

Thank you for your interest in contributing to this project!

## How to Contribute

1. Fork the repository and clone it to your local machine.
2. Create a new branch for your feature or bug fix:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. Make your changes and test them locally using Docker:
   ```bash
   bash scripts/docker_run.sh --build --gui
   ```
4. Ensure your code follows the existing style and conventions.
5. Update `CHANGELOG.md` and `CHANGELOG_CN.md` if your change is user-facing.
6. Commit your changes with clear and descriptive messages.
7. Push to your fork and open a Pull Request against the `main` branch.

## Development Workflow

- Use `feature/*` branches for new features.
- Use `fix/*` branches for bug fixes.
- Keep commits focused and atomic.
- Write commit messages in English or Chinese, but be concise and descriptive.

## Code Style

- Python: follow PEP 8.
- C++: follow the ROS 2 style guide.
- Launch files: keep parameters explicit and add comments for non-trivial logic.

## Reporting Issues

If you find a bug or have a feature request, please open an issue using the provided templates.

## License

By contributing, you agree that your contributions will be licensed under the same license as the project.
