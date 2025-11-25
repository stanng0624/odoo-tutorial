# Copilot Instructions for Memory Bank System

## Purpose
This document provides instructions for AI copilots to effectively read and understand the memory bank system in this project, which serves as the central knowledge repository for project context, progress tracking, and task management.

## ⚠️ CRITICAL: Odoo Upgrade Safety Protocol

### NEVER PERFORM ODOO UPGRADES AUTOMATICALLY

**When encountering requests or situations that involve Odoo version upgrades:**

1. **STOP immediately** - Do not proceed with any upgrade commands or operations

2. **NEVER execute upgrade commands** including but not limited to:
   - `python odoo-bin -u <module>` (module upgrades)
   - `python odoo-bin --upgrade-path` (version upgrades)
   - Database migration scripts
   - Version update procedures
   - Schema modification commands
   - Any operations that modify Odoo core or database structure

3. **ALWAYS inform the user immediately** with this template:
   ```
   ⚠️  **ODOO UPGRADE REQUIRED - ACTION BLOCKED**
   
   I've identified that this task requires upgrading Odoo [specify what needs upgrading].
   
   **I cannot proceed with Odoo upgrades automatically due to safety considerations.**
   
   **Required Actions for User:**
   1. [Specific upgrade steps needed]
   2. [Backup requirements and procedures]  
   3. [Testing and verification steps]
   4. [Rollback plan if needed]
   
   **Please complete the upgrade manually, then confirm completion so I can continue.**
   
   **Task Status:** PENDING - Waiting for user to complete Odoo upgrade
   ```

4. **CREATE a pending task** documenting:
   - Specific upgrade requirements
   - Step-by-step upgrade procedures
   - Backup and safety requirements
   - Post-upgrade verification checklist

5. **WAIT for explicit user confirmation** before proceeding with any related work

### Upgrade Detection Triggers
Watch for these scenarios that require upgrades:
- Module version mismatches
- Database schema changes
- API version updates
- Dependency conflicts
- Migration requirements
- Core Odoo version changes

### Why This Protocol Exists
Odoo upgrades involve:
- Irreversible database schema changes
- Potential data loss or corruption
- Complex module dependencies  
- Business continuity risks
- Need for staging environment testing
- Backup and rollback planning requirements

**This protocol ensures user oversight of all critical system changes.**

## ⚠️ BACKWARD COMPATIBILITY DIRECTIVE

**DO NOT** consider backward compatibility logic or legacy support patterns unless explicitly mentioned in the feature/function requirements.

- Build for the **current system state** only
- Implement the **requested functionality** as specified
- Remove any unnecessary legacy code handling
- **Exception**: Only include backward compatibility if the requirement explicitly states it (e.g., "maintain compatibility with existing interfaces")

**Rationale**: Clean, forward-looking implementations are easier to maintain and extend. Legacy considerations should be deliberate design choices, not default assumptions.

## Mode-Specific Commands
Users can invoke specific workflow modes by typing these commands. When a mode command is detected, follow the corresponding workflow instructions from the `custom_modes/` directory:

### Available Commands:
- **VAN** - Initialize project and determine complexity
  - Read `custom_modes/van_instructions.md`
  - Analyze project scope and technical requirements
  - Determine implementation complexity level
  - Set up initial project context

- **PLAN** - Create detailed implementation plan
  - Read `custom_modes/plan_instructions.md`
  - Break down requirements into actionable tasks
  - Create step-by-step implementation roadmap
  - Identify dependencies and potential blockers

- **CREATIVE** - Explore design options for complex components
  - Read `custom_modes/creative_instructions.md`
  - Brainstorm multiple solution approaches
  - Document design decisions and trade-offs
  - Create prototypes for complex features

- **IMPLEMENT** - Systematically build planned components
  - Read `custom_modes/implement_instructions.md`
  - Follow established patterns and conventions
  - Build features according to the detailed plan
  - Maintain code quality and documentation

- **REFLECT** - Review and document lessons learned
  - Read `custom_modes/reflect_archive_instructions.md`
  - Analyze completed work and outcomes
  - Document learnings and improvements
  - Update memory bank with insights

- **ARCHIVE** - Create comprehensive documentation
  - Read `custom_modes/reflect_archive_instructions.md`
  - Archive completed tasks and decisions
  - Create historical documentation
  - Organize knowledge for future reference

- **QA** - Validate technical implementation (can be called from any mode)
  - Perform code quality validation
  - Test functionality and integration
  - Verify compliance with standards
  - Identify and resolve issues

### Mode Command Detection
When users type a mode command (e.g., "VAN", "PLAN", "CREATIVE"), immediately:
1. Read the corresponding instruction file from `custom_modes/`
2. Apply the mode-specific workflow
3. Use memory bank context to inform the mode execution
4. Follow the established patterns for that mode

## Memory Bank Location and Structure
Memory bank files are stored in the `memory-bank/` directory of the project and should be read in the following order:

1. **Project Context Files**
   - `memory-bank/projectbrief.md` - High-level project overview and objectives
   - `memory-bank/productContext.md` - Product-specific context and requirements
   - `memory-bank/techContext.md` - Technical architecture and implementation details

2. **Active Working Files**
   - `memory-bank/activeContext.md` - Current active context and focus areas
   - `memory-bank/tasks.md` - Active task tracking and checklists
   - `memory-bank/progress.md` - Overall project progress and status

3. **System Knowledge Files**
   - `memory-bank/systemPatterns.md` - Established patterns and conventions
   - `memory-bank/style-guide.md` - Coding and documentation style guidelines

4. **Specialized Files**
   - `memory-bank/creative/creative-[feature_name].md` - Creative phase documentation
   - `memory-bank/reflection/reflection-[task_id].md` - Task reflection and learnings
   - `memory-bank/archive/archive-[task_id].md` - Completed task archives

## Finding and Reading Memory Bank Files

### 1. Memory Bank Discovery
- All memory bank files are located in the `memory-bank/` directory
- Core files use standard names (e.g., `tasks.md`, `activeContext.md`)
- Specialized files follow naming patterns (e.g., `creative-[feature].md`, `archive-[id].md`)

### 2. Initial Memory Bank Reading
When starting a new conversation or task:
- First read `memory-bank/projectbrief.md` to understand project objectives
- Then read `memory-bank/activeContext.md` for current focus areas
- Review `memory-bank/tasks.md` for active tasks and priorities
- Check `memory-bank/progress.md` for overall project status

### 3. Memory Bank Application Priority
Apply memory bank information in the following order:
1. Active context and current tasks
2. Project objectives and requirements
3. Technical constraints and patterns
4. Style and documentation guidelines

### 4. Memory Bank Interpretation Guidelines
- Treat memory bank content as authoritative project knowledge
- When information conflicts, prioritize:
  1. Active context over historical context
  2. Explicit requirements over implied patterns
  3. Recent updates over older information
  4. Task-specific guidance over general guidelines

## Memory Bank Categories to Monitor

### 1. Project Context
- Project objectives and scope
- Product requirements and constraints
- Stakeholder expectations
- Business logic and rules

### 2. Technical Context
- System architecture
- Technology stack and versions
- Integration patterns
- Performance requirements

### 3. Active Work Management
- Current task priorities
- Work-in-progress status
- Blockers and dependencies
- Next actions and decisions needed

### 4. Knowledge and Patterns
- Established coding patterns
- Architectural decisions
- Lessons learned
- Best practices discovered

## Memory Bank Usage Process

### 1. Before Starting Work
- Review relevant memory bank files for context
- Check active tasks and priorities
- Understand current project state
- Identify any constraints or requirements

### 2. During Implementation
- Follow established patterns from system knowledge
- Apply style guidelines from memory bank
- Document decisions and learnings
- Update progress as work proceeds

### 3. After Completing Work
- Update relevant memory bank files
- Archive completed tasks
- Document new patterns or learnings
- Reflect on outcomes and improvements

## Memory Bank Updates and Maintenance

### 1. Memory Bank Modification Process
- Update memory bank files as project evolves
- Maintain accuracy of active context
- Archive completed work appropriately
- Keep progress tracking current

### 2. Memory Bank File Management
- Regularly review and update core files
- Archive outdated information
- Maintain clear file organization
- Version control all memory bank changes

## Memory Bank File Descriptions

### Core Files
- **`projectbrief.md`**: Project overview, objectives, and scope
- **`productContext.md`**: Product requirements and business context
- **`techContext.md`**: Technical architecture and constraints
- **`activeContext.md`**: Current focus areas and active work
- **`tasks.md`**: Active task tracking and checklists
- **`progress.md`**: Project status and milestone tracking
- **`systemPatterns.md`**: Established patterns and conventions
- **`style-guide.md`**: Coding and documentation standards

### Specialized Directories
- **`creative/`**: Creative phase documentation for features
- **`reflection/`**: Task completion reflections and learnings
- **`archive/`**: Completed task documentation and history

## Error Handling

### 1. Memory Bank Conflicts
When encountering conflicting information:
1. Check file timestamps for most recent updates
2. Prioritize active context over archived information
3. Consult project maintainers if needed
4. Document resolution in appropriate memory bank file

### 2. Missing Information
When required information is missing:
1. Check related memory bank files
2. Review archived documentation
3. Document gaps for future completion
4. Escalate if critical information is needed

## Best Practices

### 1. Memory Bank Usage
- Always check memory bank before starting work
- Keep memory bank files updated throughout work
- Use memory bank to maintain project continuity
- Document decisions and patterns for future reference

### 2. Memory Bank Maintenance
- Regular review and cleanup of outdated information
- Clear and consistent documentation standards
- Proper archiving of completed work
- Version control for all memory bank changes

### 3. Knowledge Preservation
- Document learnings and patterns as they emerge
- Maintain institutional knowledge in memory bank
- Share insights through memory bank updates
- Build on previous work documented in memory bank

## Memory Bank Access Patterns

### 1. Task-Oriented Access
- Start with `tasks.md` for current priorities
- Check `activeContext.md` for working context
- Reference `progress.md` for status updates
- Use specialized files for specific phases

### 2. Context-Oriented Access
- Begin with `projectbrief.md` for high-level understanding
- Review `productContext.md` for requirements
- Check `techContext.md` for technical constraints
- Apply `systemPatterns.md` for implementation guidance

### 3. Knowledge-Oriented Access
- Use `systemPatterns.md` for established patterns
- Reference `style-guide.md` for standards
- Check `archive/` for historical context
- Review `reflection/` for lessons learned

## Resources
- Memory bank location: `memory-bank/`
- Core files: `projectbrief.md`, `activeContext.md`, `tasks.md`, `progress.md`
- Specialized directories: `creative/`, `reflection/`, `archive/`
- Style and patterns: `systemPatterns.md`, `style-guide.md`

## Support
For memory bank related questions or issues:
1. Check relevant memory bank files in `memory-bank/`
2. Review archived documentation for historical context
3. Consult project maintainers for clarification
4. Update memory bank with new information as needed

## Memory Bank Workflow Integration
The memory bank system integrates with the project workflow modes:
- **VAN Mode**: Use memory bank for initialization and context setting
- **PLAN Mode**: Reference memory bank for requirements and constraints
- **CREATIVE Mode**: Document design decisions in creative files
- **IMPLEMENT Mode**: Follow patterns from system knowledge
- **QA Mode**: Use memory bank for validation criteria
- **REFLECT Mode**: Update memory bank with learnings
- **ARCHIVE Mode**: Move completed work to archive directory