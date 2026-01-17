---
name: brainstorm-migration
description: Migration brainstorm template - upgrade, conversion, and transition planning
type: template
---

# AXEL Template: Brainstorm Migration

```xml
<document type="brainstorm">

  <enforcement>
    - MUST document current state accurately
    - MUST define target state clearly
    - MUST identify breaking changes and risks
    - NEVER proceed without rollback plan consideration
  </enforcement>

  <objective>
    Migrate from .NET 6 to .NET 8.
    Maintain backward compatibility during transition.
  </objective>

  <documents name="core" load="always" mode="context">
    <read src=".claude/BOOTSTRAP.md"/>
    <read src="*.csproj" pattern="true" optional="true"/>
    <understanding>
      - DOCUMENT current state from project files
      - IDENTIFY breaking changes in target version
      - CHECK dependency compatibility
    </understanding>
  </documents>

  <user_request>
    We need to upgrade from .NET 6 to .NET 8.
    Want to do it with minimal disruption.
  </user_request>

  <interpretation>
    User wants to perform a framework upgrade:
    - Current: .NET 6 (LTS)
    - Target: .NET 8 (LTS)
    - Constraint: Minimal disruption
    - Approach: Incremental migration with testing at each step
  </interpretation>

  <current_state>
    Framework:
    - .NET 6.0.x
    - ASP.NET Core 6.0
    - Entity Framework Core 6.0

    Dependencies:
    - Newtonsoft.Json 13.x
    - Serilog 2.x
    - AutoMapper 12.x

    Configuration:
    - Target framework in .csproj files
    - Docker base images (mcr.microsoft.com/dotnet/aspnet:6.0)
    - CI/CD pipeline references
  </current_state>

  <target_state>
    Framework:
    - .NET 8.0.x
    - ASP.NET Core 8.0
    - Entity Framework Core 8.0

    Dependencies (updated):
    - System.Text.Json (replace Newtonsoft where possible)
    - Serilog 3.x
    - AutoMapper 13.x

    Configuration:
    - Updated target framework
    - Updated Docker base images
    - Updated CI/CD pipeline
  </target_state>

  <scope>
    Include:
    - Framework version upgrade
    - NuGet package updates
    - Breaking change fixes
    - Docker image updates
    - Basic testing verification

    Exclude:
    - New .NET 8 feature adoption (future phase)
    - Performance optimization (separate task)
    - Architecture changes
  </scope>

  <context_findings>
    Breaking Changes (.NET 6 to 8):
    - Minimal API changes (if used)
    - EF Core query changes
    - Some deprecated APIs

    Dependency Compatibility:
    - Most packages have .NET 8 support
    - Some may require major version updates

    Risk Areas:
    - Database migrations (EF Core changes)
    - Third-party library compatibility
    - Runtime behavior changes
  </context_findings>

  <suggested_documents>
    Microsoft Docs:
    - .NET 6 to 8 migration guide
    - ASP.NET Core breaking changes
    - EF Core 8 migration guide

    Codebase:
    - @*.csproj (all project files)
    - @Directory.Build.props
    - @Dockerfile
    - @docker-compose.yml
  </suggested_documents>

  <open_questions>
    - Is there a staging environment for testing?
    - What is the rollback strategy if issues arise?
    - Are there any third-party integrations that need coordination?
    - What is the acceptable downtime window?
  </open_questions>

  <assumptions>
    - All unit tests pass on current version
    - CI/CD pipeline can be updated
    - Team can dedicate time for migration testing
  </assumptions>

  <next_steps>
    1. Resolve open questions with user
    2. Create AXEL Todo (type: migration) with phased approach
    3. Update in development environment first
    4. Run full test suite
    5. Deploy to staging for validation
  </next_steps>

  <understanding/>

</document>
```
