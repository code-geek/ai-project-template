# Claude Code Agents

This directory contains specialized Claude Code agents designed to enhance development workflow. Each agent is an expert in a specific domain and can be automatically invoked based on context.

## Available Agents

### 🔍 **code-reviewer**

Expert code reviewer for quality, security, best practices, and architectural consistency.

- Reviews code for security vulnerabilities
- Checks performance patterns
- Ensures coding standards
- Validates accessibility

### 🧪 **test-writer**

Comprehensive testing specialist for Django pytest backend and Next.js frontend testing.

- Writes pytest tests for Django
- Creates React Testing Library tests
- Implements E2E tests with Playwright
- Maintains high code coverage

### 🏗️ **backend-architect**

Django REST API architect specializing in Django Ninja, database design, and scalable backend architecture.

- Designs RESTful APIs with Django Ninja
- Optimizes database queries
- Implements authentication patterns
- Ensures API best practices

### 🎨 **frontend-engineer**

Next.js and React specialist focusing on modern UI development and performance.

- Creates responsive components
- Implements state management
- Optimizes performance
- Ensures accessibility

### 🐛 **debugger**

Expert debugging specialist for identifying and resolving errors in Django backend and Next.js frontend.

- Quickly identifies root causes
- Provides systematic debugging approach
- Offers specific solutions
- Implements error prevention

### ⚡ **performance-optimizer**

Performance optimization specialist focusing on speed, scalability, and resource efficiency.

- Optimizes database queries
- Reduces bundle sizes
- Implements caching strategies
- Monitors performance metrics

### 🚀 **deployment-engineer**

Deployment and DevOps specialist for Docker, CI/CD, and cloud infrastructure.

- Configures Docker environments
- Sets up CI/CD pipelines
- Manages cloud deployments
- Implements monitoring

### 📝 **api-designer**

API design specialist focusing on RESTful principles and Django Ninja implementation.

- Designs consistent API endpoints
- Creates comprehensive schemas
- Implements proper error handling
- Documents API specifications

## How Agents Work

Claude Code automatically detects and uses these agents based on the task context. You can also explicitly request a specific agent by mentioning the type of task:

- "Review this code" → triggers `code-reviewer`
- "Write tests for this feature" → triggers `test-writer`
- "Debug this error" → triggers `debugger`
- "Optimize the page load time" → triggers `performance-optimizer`
- "Design the API for user management" → triggers `api-designer`

## Agent Coordination

Agents can work together on complex tasks:

1. **Sequential**: `backend-architect` → `test-writer` → `code-reviewer`
2. **Parallel**: Multiple agents analyzing different aspects simultaneously
3. **Hierarchical**: Primary agent delegates subtasks to specialists

## Best Practices

1. **Let Claude Choose**: Usually Claude will automatically select the right agent
2. **Be Specific**: Clear task descriptions help Claude pick the best agent
3. **Chain Agents**: For complex features, multiple agents work better together
4. **Trust the Experts**: Each agent is specialized in their domain

## Adding New Agents

To add a new agent:

1. Create a new `.md` file in this directory
2. Add YAML frontmatter with name, description, and tools
3. Write the agent's system prompt
4. Focus on specific expertise area

Example structure:

```yaml
---
name: your-agent-name
description: Brief description of when this agent should be used
tools: Read, Write, Edit, Bash
---

You are a specialized agent for...
```

## Performance Tips

- Agents have separate context windows
- Use agents for complex, focused tasks
- Avoid using agents for simple operations
- Leverage parallel execution for independent tasks
