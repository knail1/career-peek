# Career Peek

<div align="center">

![Career Peek Logo](https://via.placeholder.com/200x200?text=Career+Peek)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.11-blue.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.3.3-lightgrey.svg)](https://flask.palletsprojects.com/)
[![Docker](https://img.shields.io/badge/Docker-Ready-blue.svg)](https://www.docker.com/)
[![LinkedIn API](https://img.shields.io/badge/LinkedIn-API-0077B5.svg)](https://developer.linkedin.com/)

**Gain valuable insights into career histories through LinkedIn data**

[Features](#-features) • 
[Installation](#-installation) • 
[Usage](#-usage) • 
[Architecture](#-architecture) • 
[Development](#-development) • 
[Contributing](#-contributing) • 
[License](#-license)

</div>

## 📋 Overview

Career Peek is an application designed for managers and HR professionals to analyze an employee's career history on LinkedIn. By leveraging the LinkedIn API, it collects and stores information in a stateful database to provide insights into an individual's career progression, job history, responsibilities, and LinkedIn activities. This tool helps managers better understand their team members' professional backgrounds, skills, and tendencies, enabling more informed decisions about team composition, professional development, and role assignments.

## ✨ Features

- **Career Timeline Visualization**: View a chronological representation of an individual's professional journey
- **Skill Analysis**: Identify and categorize skills based on job descriptions and endorsements
- **Job Responsibility Extraction**: Extract and analyze key responsibilities from past roles
- **Activity Insights**: Understand engagement patterns through LinkedIn activity data
- **Comparative Analysis**: Compare career trajectories across team members or candidates
- **Data Export**: Export insights in various formats for reporting and presentation

## 🚀 Installation

### Prerequisites

- Docker and Docker Compose
- Git
- LinkedIn API credentials (OAuth 2.0)

### Using Docker (Recommended)

1. Clone the repository:
   ```bash
   git clone https://github.com/knail1/career-peek.git
   cd career-peek
   ```

2. Configure environment variables:
   ```bash
   cp .env.example .env
   # Edit .env with your LinkedIn API credentials and other settings
   ```

3. Start the application:
   ```bash
   docker-compose up -d
   ```

4. Access the application at http://localhost:3000

### Manual Installation

For detailed instructions on manual installation, please refer to the [SETUP.md](SETUP.md) file.

## 🔍 Usage

**Note**: The application is currently under development. Usage examples will be provided as features are implemented.

## 🏗 Architecture

Career Peek follows a modern web application architecture:

- **Frontend**: React-based single-page application
- **Backend**: Flask RESTful API
- **Database**: PostgreSQL for data persistence
- **Authentication**: OAuth 2.0 for LinkedIn API access
- **Containerization**: Docker for consistent development and deployment

## 🛠️ Development

### Project Structure

```
career-peek/
├── backend/           # Flask API server
│   ├── app.py         # Application entry point
│   ├── config.py      # Configuration settings
│   ├── requirements.txt # Python dependencies
│   └── tests/         # Backend tests
├── database/          # Database migrations and seeds
├── docs/              # Project documentation
│   ├── meta_file_for_readme.txt  # Original prompts used
│   ├── prompt_plan_claude_opus.md # Implementation plan from Claude
│   ├── prompt_plan_gpt_o3.md    # Implementation plan from GPT-4
│   ├── spec.md                  # Project specifications
│   └── todo_claude_opus.md      # Implementation checklist
├── docker-compose.yml # Docker configuration
├── frontend/          # React frontend (to be implemented)
├── .env.example       # Example environment variables
├── LICENSE            # MIT License
├── README.md          # This file
└── SETUP.md           # Detailed setup instructions
```

### Development Workflow

1. Start the development environment:
   ```bash
   docker-compose up -d
   ```

2. Make changes to the code

3. Run tests:
   ```bash
   docker-compose exec api pytest
   ```

4. Rebuild containers if necessary:
   ```bash
   docker-compose build
   ```

For more detailed development instructions, please refer to the [SETUP.md](SETUP.md) file.

## 📝 Meta-work: How I Built the Planning Docs

The development of Career Peek followed a structured approach using AI assistance to create comprehensive planning documentation. This section outlines the process used to develop the project blueprint.

### AI-Assisted Planning Process

#### 1. Initial Concept Development with OpenAI

The project began with a clear vision that was refined through an iterative Q&A process with OpenAI. This approach helped transform a high-level concept into a detailed specification:

```
We are going to create an application for finding out someone's career history on LinkedIn by pulling the LinkedIn API and collecting that information and storing it in a stateful database in the backend. We are going to need this to understand the career progression of the individual, their history, their jobs, what they've done in the past in each job if available and the ancillary information on LinkedIn activities to get a general idea of the proclivity of the person.

Ask me one question at a time so we can develop a thorough, step-by-step spec for this idea.
```

This dialogue-based approach allowed for:
- Clarification of ambiguous requirements
- Identification of potential challenges
- Refinement of feature scope
- Documentation of technical constraints

The result was a comprehensive `docs/spec.md` document that served as the foundation for all subsequent planning.

#### 2. Blueprint Development with Multiple AI Models

To ensure a robust implementation plan, the specification was processed through two different AI models:

**GPT-4 Implementation Plan:**
```
Using that, Draft a detailed, step-by-step blueprint for building this project. Then, once you have a solid plan, break it down into small, iterative chunks that build on each other.
```

**Claude Opus Alternative Perspective:**
```
From the spec.md attached, draft a detailed, step-by-step blueprint for building this project. Then, once you have a solid plan, break it down into small, iterative chunks that build on each other.
```

This dual-model approach provided:
- Diverse implementation strategies
- Identification of potential blind spots
- Complementary technical perspectives
- More comprehensive risk assessment

The resulting documents (`docs/prompt_plan_gpt_o3.md` and `docs/prompt_plan_claude_opus.md`) offered alternative implementation paths, allowing for a more informed development strategy.

#### 3. Structured Task Management

The final planning step involved creating a detailed task list that mapped directly to the implementation plans:

```
Can you make a `todo.md` that I can use as a checklist? Make sure it structurally maps with the prompt plan, since you'll start working through the todo list items and would refer to the corresponding prompts to implement the tasks.
```

This produced a comprehensive checklist in `docs/todo_claude_opus.md` that:
- Breaks down the project into manageable tasks
- Establishes clear dependencies between components
- Provides a roadmap for incremental development
- Enables progress tracking throughout implementation

### Benefits of This Approach

This AI-assisted planning methodology offers several advantages:
- **Comprehensive Documentation**: Detailed plans before writing any code
- **Reduced Ambiguity**: Clear specifications minimize misunderstandings
- **Incremental Development**: Well-defined steps for gradual implementation
- **Test-Driven Focus**: Testing considerations built into the planning process
- **Multiple Perspectives**: Diverse viewpoints from different AI models

By leveraging AI for the planning phase, the project benefits from a more thorough and well-considered foundation, potentially reducing rework and ensuring a more cohesive final product.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📬 Contact

Project Link: [https://github.com/knail1/career-peek](https://github.com/knail1/career-peek)

---

⭐️ From [knail1](https://github.com/knail1)