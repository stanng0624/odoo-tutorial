---
mode: agent
---

## User Input

```text
$ARGUMENTS
```

You **MUST** consider the user input before proceeding (if not empty).

## Instructions

If the user input is empty, respond with "No task provided."

If the user input is not empty, use PLAN mode (Based on ${workspaceFolder}/custom_modes/plan_instructions.md) to create a detailed plan for the task described by user input. Break down the task into clear, manageable steps, and outline the approach you will take to complete each step. Consider any potential challenges and how you might address them. Your plan should be thorough and well-structured, providing a clear roadmap for executing the task effectively.

You **MUST** create docummentation for the plan and the task according to the task organization rules in tasks.md.

## Expected Output
Output the plan in markdown format, including a summary of the task, the steps involved, and any relevant details or considerations. Ensure that the plan is easy to understand and follow, providing a comprehensive guide for executing the task successfully.

