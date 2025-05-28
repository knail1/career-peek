# Career Peek

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 📋 Overview

Career Peek is an application designed for managers and HR professionals to analyze an employee's career history on LinkedIn. By leveraging the LinkedIn API, it collects and stores information in a stateful database to provide insights into an individual's career progression, job history, responsibilities, and LinkedIn activities. This tool helps managers better understand their team members' professional backgrounds, skills, and tendencies, enabling more informed decisions about team composition, professional development, and role assignments.

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)
- LinkedIn API credentials (OAuth 2.0)

### Installation

**TBD**: Installation instructions will be provided as the project is implemented.

## 🔍 Usage

**TBD**: Usage examples will be provided as the project is implemented.

## 🛠️ Development

### Project Structure

```
career-peek/
├── LICENSE
├── README.md
├── meta_file_for_readme.txt
├── prompt_plan_claude_opus.md
├── prompt_plan_gpt_o3.md
├── spec.md
└── todo_claude_opus.md
```

### Running Tests

**TBD**: Test instructions will be provided as the project is implemented.

## 📝 Meta-work: How I Built the Planning Docs

The development of Career Peek followed a structured approach using AI assistance to create comprehensive planning documentation. Here's the exact process I used:

### Initial Concept Development with OpenAI

I started by feeding this prompt to OpenAI to develop the initial concept:

```
We are going to create an application for finding out someone's career history on LinkedIn by pulling the LinkedIn API and collecting that information and storing it in a stateful database in the backend. We are going to need this to understand the career progression of the individual, their history, their jobs, what they've done in the past in each job if available and the ancillary information on LinkedIn activities to get a general idea of the proclivity of the person.

Ask me one question at a time so we can develop a thorough, step-by-step spec for this idea. Each question should build on my previous answers, and our end goal is to have a detailed specification that I can hand off to a developer. Let's do this iteratively and dig into every relevant detail. Remember, only one question at a time. I prefer yes-no answers, but I'm okay with long-form answers as well.
```

This iterative Q&A process resulted in the creation of a detailed specification document called `spec.md`.

### Blueprint Development with GPT-4

I then used the specification to create an implementation plan by feeding this prompt to GPT-4:

```
Using that, Draft a detailed, step-by-step blueprint for building this project. Then, once you have a solid plan, break it down into small, iterative chunks that build on each other. Look at these chunks and then go another round to break it into small steps. Review the results and make sure that the steps are small enough to be implemented safely with strong testing, but big enough to move the project forward. Iterate until you feel that the steps are right sized for this project.

From here you should have the foundation to provide a series of prompts for a code-generation LLM that will implement each step in a test-driven manner. Prioritize best practices, incremental progress, and early testing, ensuring no big jumps in complexity at any stage. Make sure that each prompt builds on the previous prompts, and ends with wiring things together. There should be no hanging or orphaned code that isn't integrated into a previous step.

Make sure and separate each prompt section. Use markdown. Each prompt should be tagged as text using code tags. The goal is to output prompts, but context, etc is important as well.
```

This generated a detailed implementation plan in `prompt_plan_gpt_o3.md`.

### Alternative Blueprint with Claude Opus

I repeated a similar process with Claude Opus to get an alternative perspective:

```
From the spec.md attached, draft a detailed, step-by-step blueprint for building this project. Then, once you have a solid plan, break it down into small, iterative chunks that build on each other. Look at these chunks and then go another round to break it into small steps. Review the results and make sure that the steps are small enough to be implemented safely with strong testing, but big enough to move the project forward. Iterate until you feel that the steps are right sized for this project. From here you should have the foundation to provide a series of prompts for a code-generation LLM that will implement each step in a test-driven manner. Prioritize best practices, incremental progress, and early testing, ensuring no big jumps in complexity at any stage. Make sure that each prompt builds on the previous prompts, and ends with wiring things together. There should be no hanging or orphaned code that isn't integrated into a previous step. Make sure and separate each prompt section. Use markdown. Each prompt should be tagged as text using code tags. The goal is to output prompts, but context, etc is important as well.
```

This created an alternative implementation plan in `prompt_plan_claude_opus.md`.

### Task Management with Todo List

Finally, I created a structured to-do list to track implementation progress:

```
Can you make a `todo.md` that I can use as a checklist? Make sure it structurally maps with the prompt plan, since you'll start working through the todo list items and would refer to the corresponding prompts to implement the tasks. Be thorough.
```

This generated a comprehensive checklist in `todo_claude_opus.md` that aligns with the implementation plans, providing a roadmap for development.

With these planning documents in place, I was ready to begin the actual coding process, using the prompts to guide the implementation of each component in a structured, test-driven manner.

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