---
mode: agent
model: Grok Code Fast 1
---
# Git Commit Message Guidelines (Silverlit Odoo 17)

## Overview
All contributors **must** follow these commit message rules for the Silverlit Odoo 17 project. This ensures clarity, traceability, and professional project history.

## Commit Message Structure

```
[TAG] module: short description

Long description (why, rationale, technical decisions).

[References: task-123, Fixes #123, Closes #123, opw-123]
```

## Required Components

### 1. Tags
Use one of these tags at the start of your commit message:

- **[FIX]** – Bug fixes
- **[REF]** – Refactoring
- **[ADD]** – Adding new modules/features
- **[REM]** – Removing resources or dead code
- **[REV]** – Reverting commits
- **[MOV]** – Moving files or code
- **[REL]** – Release commits
- **[IMP]** – Incremental improvements
- **[MERGE]** – Merge commits
- **[CLA]** – Contributor License Agreement
- **[I18N]** – Translation changes
- **[PERF]** – Performance patches

### 2. Module Name
- Use the **technical name** of the module(s) affected
- If multiple modules: list them or use `various` for cross-module changes
- Examples: `novus_sap_connector`, `novus_silverlit_report`, `novus_loading_plan`

### 3. Short Description
- Limit to ~50 characters
- Should make sense as: "If applied, this commit will <short description>"
- Be specific and actionable

### 4. Long Description
- Explain **WHY** the change was made, not just what was changed
- Include rationale, technical decisions, and context
- Reference related tasks, issues, or tickets

### 5. References
- Use `task-123`, `Fixes #123`, `Closes #123`, `opw-123` as appropriate
- If the change has no task reference (e.g., ad-hoc changes), omit the References line entirely

## Best Practices

- **Always commit all changes**: When following these guidelines, stage and commit ALL current changes using `git add . && git commit` - do not leave any changes unstaged
- **One module per commit** when possible (though all current changes should still be committed together)
- **Be verbose**: Good commit messages are an investment in your future self and team
- **Avoid**: "bugfix", "improvements", or other vague messages
- **Configure your git**:
  ```bash
  git config --global user.name "Your Name"
  git config --global user.email "your@email.com"
  ```

## Example Commit Messages

### Bug Fix
```
[FIX] novus_loading_plan: correct ZLPC filter logic

Fixed a bug where rejected items were not properly excluded from the
loading plan in shipping mode. Now, only non-rejected items are shown
when accessed from the ZLPC menu.

Closes #101
```

### New Feature
```
[ADD] novus_silverlit_report: add new sales order report type

Introduced ZSOHK report with multi-language Excel template support.
Includes new filters and improved image handling for product packaging.

task-202
```

### Refactoring
```
[REF] novus_sap_connector: unify cron job architecture

Refactored cron job logic to use the unified API profile system for all
SAP model synchronizations. Removed all individual model cron jobs and
centralized control through the API profile system.

Closes #88
```

### Improvement
```
[IMP] novus_base: enhance error logging for SAP operations

Improved error logging to provide more context in API profile logs.
This helps with debugging failed syncs and improves support response time.

task-156
```

### Performance
```
[PERF] novus_silverlit_report: optimize Excel template processing

Optimized Excel template processing by implementing batch operations
and reducing memory usage for large reports. Improves performance by 40%.

task-203
```

## Common Module Names for This Project

- `novus_base` - Foundation module
- `novus_sap_connector` - SAP S/4HANA integration
- `novus_silverlit_report` - Advanced reporting system
- `novus_loading_plan` - Loading plan management
- `various` - Cross-module changes

## Reference
Based on [Odoo 17 Git Guidelines](https://www.odoo.com/documentation/17.0/contributing/development/git_guidelines.html)

---

**Remember**: You spend hours, days, or weeks working on meaningful features. Take time to write clear and understandable commit messages that explain WHY you made the changes.

**Important**: After understanding these instructions, proceed immediately with staging all current changes using `git add .`.