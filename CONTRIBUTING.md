# Contributing to AI Project Template

First off, thank you for considering contributing to AI Project Template! It's people like you that make this template better for everyone.

## How Can I Contribute?

### Reporting Bugs

Before creating bug reports, please check existing issues as you might find out that you don't need to create one. When you are creating a bug report, please include as many details as possible using the issue template.

### Suggesting Enhancements

Enhancement suggestions are tracked as GitHub issues. Create an issue and provide the following information:

- Use a clear and descriptive title
- Provide a step-by-step description of the suggested enhancement
- Provide specific examples to demonstrate the steps
- Describe the current behavior and explain which behavior you expected to see instead

### Pull Requests

1. Fork the repo and create your branch from `main`
2. If you've added code that should be tested, add tests
3. If you've changed APIs, update the documentation
4. Ensure the test suite passes
5. Make sure your code follows the existing style
6. Issue that pull request!

## Development Process

1. Clone your fork:
   ```bash
   git clone https://github.com/YOUR_USERNAME/ai-project-template.git
   cd ai-project-template
   ```

2. Create a branch:
   ```bash
   git checkout -b feature/your-feature-name
   ```

3. Make your changes and test:
   ```bash
   ./scripts/run-tests.sh
   ```

4. Commit your changes:
   ```bash
   git commit -m "Add your descriptive commit message"
   ```

5. Push to your fork:
   ```bash
   git push origin feature/your-feature-name
   ```

## Style Guidelines

### Python Code Style
- Follow PEP 8
- Use type hints
- Run `ruff` for linting

### JavaScript/TypeScript Code Style
- Use ESLint and Prettier
- Follow the existing patterns in the codebase
- Use TypeScript strictly

### Commit Messages
- Use the present tense ("Add feature" not "Added feature")
- Use the imperative mood ("Move cursor to..." not "Moves cursor to...")
- Limit the first line to 72 characters or less

## Claude Code Agents

When contributing new agents:
1. Place them in `.claude/agents/`
2. Use YAML frontmatter with name, description, and tools
3. Focus on a specific expertise area
4. Include practical examples

## Questions?

Feel free to open an issue with your question or reach out to the maintainers.

Thank you for contributing! 🎉