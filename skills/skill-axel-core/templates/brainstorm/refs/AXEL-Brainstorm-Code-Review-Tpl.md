---
name: brainstorm-code-review
description: Code review brainstorm template - review preparation and criteria definition
type: template
---

# AXEL Template: Brainstorm Code Review

```xml
<document type="brainstorm">

  <enforcement>
    - MUST define specific review criteria
    - MUST list all files to be reviewed
    - NEVER skip security-related checks
  </enforcement>

  <objective>
    Review UserService for security vulnerabilities and performance.
    Focus on authentication flow and database queries.
  </objective>

  <documents name="core" load="always" mode="context">
    <read src="references/quality/Security-Standards.md" optional="true"/>
    <read src="references/quality/Performance-Guidelines.md" optional="true"/>
    <understanding>
      - LOAD quality standards if available
      - CHECK existing review criteria
      - IDENTIFY patterns to look for
    </understanding>
  </documents>

  <user_request>
    Please review the UserService code.
    Concerned about security and performance.
  </user_request>

  <interpretation>
    User wants a focused code review:
    - Primary concern: Security vulnerabilities
    - Secondary concern: Performance issues
    - Scope: UserService and related components
    - Output: Categorized findings with fix suggestions
  </interpretation>

  <scope>
    Include:
    - UserService.cs
    - UserRepository.cs
    - UserController.cs
    - Related DTOs and models

    Exclude:
    - Unit tests (separate review)
    - Frontend code
    - Unrelated services
  </scope>

  <context_findings>
    Codebase:
    - UserService handles authentication and profile management
    - Uses Entity Framework for database access
    - Follows repository pattern

    Potential Risk Areas:
    - Password handling methods
    - SQL query construction
    - Input validation
    - Error message content
  </context_findings>

  <review_criteria>
    Security:
    - SQL injection vulnerabilities (parameterized queries?)
    - Password storage (proper hashing?)
    - Authentication bypass possibilities
    - Sensitive data exposure in logs/errors
    - Input validation and sanitization

    Performance:
    - N+1 query problems
    - Missing database indexes (query patterns)
    - Unnecessary data loading (eager/lazy)
    - Connection management

    Code Quality:
    - SOLID principles adherence
    - Error handling patterns
    - Naming conventions
    - Code duplication
  </review_criteria>

  <affected_components>
    Files to Review:
    - src/Services/UserService.cs
    - src/Repositories/UserRepository.cs
    - src/Controllers/UserController.cs
    - src/Models/UserEntity.cs
    - src/DTOs/UserDto.cs

    Related Files (reference):
    - src/Services/BaseService.cs (pattern reference)
    - appsettings.json (configuration)
  </affected_components>

  <suggested_documents>
    Standards:
    - references/quality/Security-Standards.md
    - references/quality/Performance-Guidelines.md
    - references/coding/Naming-Conventions.md

    Codebase:
    - @src/Services/UserService.cs
    - @src/Repositories/UserRepository.cs
    - @src/Controllers/UserController.cs
  </suggested_documents>

  <open_questions>
    - Are there specific security requirements or compliance needs?
    - What is the expected load on UserService endpoints?
    - Has there been a security audit before?
  </open_questions>

  <assumptions>
    - Current code is in production (no breaking changes preferred)
    - Team follows standard .NET conventions
    - Entity Framework Core is used
  </assumptions>

  <next_steps>
    1. Resolve open questions if any
    2. Create AXEL Todo (type: analysis) with detailed review criteria
    3. Perform review and document findings
    4. Categorize by severity (Critical/Major/Minor)
  </next_steps>

  <understanding/>

</document>
```
