---
name: brainstorm-feature
description: Feature brainstorm template - new feature design and requirements discovery
type: template
---

# AXEL Template: Brainstorm Feature

```xml
<document type="brainstorm">

  <enforcement>
    - MUST identify all affected components before planning
    - MUST list integration points with existing code
    - NEVER assume feature scope without user confirmation
  </enforcement>

  <objective>
    Add user authentication feature with JWT tokens.
    Support login, logout, and token refresh endpoints.
  </objective>

  <!-- Documents: Load relevant project references and existing code -->
  <documents name="core" load="always" mode="context">
    <read src=".claude/BOOTSTRAP.md"/>
    <read src="references/api/REST-Standards.md" ask="[api, rest]"/>
    <read src="src/Services/BaseService.cs"/>
    <understanding>
      - READ project configuration and standards first
      - IDENTIFY existing patterns to follow
      - CHECK for similar features as reference
    </understanding>
  </documents>

  <user_request>
    Add JWT-based authentication to the API.
    Need login/logout endpoints and token refresh.
  </user_request>

  <interpretation>
    User wants to implement JWT-based stateless authentication:
    - Login endpoint: Validate credentials, return access + refresh tokens
    - Logout endpoint: Invalidate refresh token
    - Token refresh: Exchange refresh token for new access token
    - Middleware: Validate JWT on protected endpoints
  </interpretation>

  <scope>
    Include:
    - Authentication endpoints (login, logout, refresh)
    - JWT token generation and validation
    - Authentication middleware
    - User credential validation

    Exclude:
    - User registration (separate feature)
    - Password reset flow (separate feature)
    - OAuth/social login (future phase)
    - Authorization/permissions (separate feature)
  </scope>

  <context_findings>
    Project Documents:
    - REST-Standards.md defines endpoint conventions
    - BaseService.cs shows dependency injection pattern

    Codebase:
    - UserService.cs exists, can extend for auth
    - No existing authentication middleware
    - appsettings.json used for configuration

    External:
    - .NET 8 supports Microsoft.AspNetCore.Authentication.JwtBearer
    - Industry standard: Access token 15min, Refresh token 7 days
  </context_findings>

  <questions_to_answer>
    Functional:
    - What are the exact user flows for this feature?
    - What edge cases need to be handled?
    - What are the validation rules?

    Technical:
    - Which existing components can be reused?
    - What new dependencies are needed?
    - How will this integrate with existing code?

    Design:
    - What API contract should be exposed?
    - What data models are needed?
    - What error handling approach fits best?
  </questions_to_answer>

  <affected_components>
    New Components:
    - AuthService (token generation, validation)
    - AuthController (endpoints)
    - JwtMiddleware (request validation)

    Modified Components:
    - UserService (add credential validation)
    - appsettings.json (JWT configuration)
    - Program.cs (middleware registration)

    Integration Points:
    - UserService.ValidateCredentials() - existing user lookup
    - ILogger - existing logging infrastructure
    - IConfiguration - existing config system
  </affected_components>

  <suggested_documents>
    Reference Files:
    - references/api/REST-Standards.md
    - references/security/Authentication-Guidelines.md

    Codebase Files:
    - src/Services/UserService.cs
    - src/Services/BaseService.cs
    - src/Models/UserEntity.cs
    - appsettings.json
  </suggested_documents>

  <open_questions>
    - What token expiration times are preferred? (default: 15min access, 7 days refresh)
    - Should tokens be stored in HttpOnly cookies or returned in response body?
    - Is there an existing password hashing convention to follow?
    - Are there specific security requirements (rate limiting, account lockout)?
  </open_questions>

  <assumptions>
    - User passwords are already hashed in database (BCrypt assumed)
    - HTTPS is enforced in production
    - Single-tenant application (no multi-tenancy)
  </assumptions>

  <next_steps>
    1. Resolve open questions with user
    2. Create AXEL Todo (type: coding) with specific implementation details
    3. Implement in order: AuthService -> JwtMiddleware -> AuthController
    4. Write integration tests
  </next_steps>

  <understanding/>

</document>
```
