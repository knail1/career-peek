prompts I fed to

o1:
We are going to create an application for finding out someone's career history on LinkedIn by pulling the LinkedIn API and collecting that information and storing it in a stateful database in the backend. We are going to need this to understand the career progression of the individual, their history, their jobs, what they've done in the past in each job if available and the ancillary information on LinkedIn activities to get a general idea of the proclivity of the person.

Ask me one question at a time so we can develop a thorough, step-by-step spec for this idea. Each question should build on my previous answers, and our end goal is to have a detailed specification that I can hand off to a developer. Let's do this iteratively and dig into every relevant detail. Remember, only one question at a time. I prefer yes-no answers, but I'm okay with long-form answers as well.

output: spec.md


fed this to o3:
at the end of this prompt is spec.md

Using that, Draft a detailed, step-by-step blueprint for building this project. Then, once you have a solid plan, break it down into small, iterative chunks that build on each other. Look at these chunks and then go another round to break it into small steps. Review the results and make sure that the steps are small enough to be implemented safely with strong testing, but big enough to move the project forward. Iterate until you feel that the steps are right sized for this project.

From here you should have the foundation to provide a series of prompts for a code-generation LLM that will implement each step in a test-driven manner. Prioritize best practices, incremental progress, and early testing, ensuring no big jumps in complexity at any stage. Make sure that each prompt builds on the previous prompts, and ends with wiring things together. There should be no hanging or orphaned code that isn't integrated into a previous step.

Make sure and separate each prompt section. Use markdown. Each prompt should be tagged as text using code tags. The goal is to output prompts, but context, etc is important as well.

---spec.md---

output: prompt_plan_gpt_o3.md


-- did the same with claude opus


from the spec.md attached, draft a detailed, step-by-step blueprint for building this project. Then, once you have a solid plan, break it down into small, iterative chunks that build on each other. Look at these chunks and then go another round to break it into small steps. Review the results and make sure that the steps are small enough to be implemented safely with strong testing, but big enough to move the project forward. Iterate until you feel that the steps are right sized for this project.  From here you should have the foundation to provide a series of prompts for a code-generation LLM that will implement each step in a test-driven manner. Prioritize best practices, incremental progress, and early testing, ensuring no big jumps in complexity at any stage. Make sure that each prompt builds on the previous prompts, and ends with wiring things together. There should be no hanging or orphaned code that isn't integrated into a previous step.  Make sure and separate each prompt section. Use markdown. Each prompt should be tagged as text using code tags. The goal is to output prompts, but context, etc is important as well. put this in prompt_plan_claude_opus.md for me to download


output file: (as listed in repo)

---


finally created: the todo file.

Can you make a `todo.md` that I can use as a checklist? Make sure it structurally maps with the prompt plan, since you'll start working through the todo list items and would refer to the corresponding prompts to implmemet the tasks. Be thorough.


-- after this I'm ready to code..


<the code prompt>