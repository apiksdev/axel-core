---
name: brainstorm-project
description: Project brainstorm template - new project initialization and architecture
type: template
---

# AXEL Template: Brainstorm Project

```xml
<document type="brainstorm">

  <enforcement>
    - MUST confirm tech stack before proceeding
    - MUST identify architectural patterns to follow
    - NEVER assume project structure without user confirmation
  </enforcement>

  <objective>
    Initialize new e-commerce platform backend.
    Microservices architecture with .NET 8.
  </objective>

  <documents name="core" load="always" mode="context">
    <read src=".claude/BOOTSTRAP.md" optional="true"/>
    <understanding>
      - CHECK if project has existing configuration
      - IDENTIFY user's tech preferences
      - GATHER best practices for selected stack
    </understanding>
  </documents>

  <user_request>
    Create a new e-commerce backend with microservices.
    Should support product catalog, orders, and user management.
  </user_request>

  <interpretation>
    User wants to build a microservices-based e-commerce platform:
    - Product Catalog Service: Product CRUD, categories, search
    - Order Service: Order management, cart, checkout
    - User Service: Authentication, profiles, preferences
    - Shared infrastructure: API Gateway, message broker
  </interpretation>

  <tech_stack>
    Language: C# (.NET 8)
    Framework: ASP.NET Core Web API
    Database: PostgreSQL (per-service databases)
    Message Broker: RabbitMQ
    API Gateway: YARP
    Containerization: Docker
    Orchestration: Kubernetes (future)

    Patterns:
    - Clean Architecture per service
    - CQRS for complex services
    - Event-driven communication
  </tech_stack>

  <scope>
    Include:
    - Solution structure and project scaffolding
    - Shared libraries (common, contracts)
    - Docker configuration
    - Basic API Gateway setup
    - Development environment configuration

    Exclude:
    - Production deployment configuration
    - CI/CD pipeline (separate task)
    - Kubernetes manifests (future phase)
    - Frontend application
  </scope>

  <context_findings>
    External Research:
    - .NET 8 performance improvements for microservices
    - YARP reverse proxy recommended for .NET API Gateway
    - MassTransit for RabbitMQ integration

    Best Practices:
    - Database per service (data isolation)
    - Shared contracts library (DTOs, events)
    - Health checks for each service
  </context_findings>

  <suggested_documents>
    Templates:
    - AXEL-Claude-Tpl.md (for CLAUDE.md generation)
    - Clean Architecture template references

    References to Create:
    - Architecture-Overview.md
    - Microservices-Guidelines.md
    - Naming-Conventions.md
  </suggested_documents>

  <open_questions>
    - Which cloud provider is targeted? (affects infrastructure choices)
    - Is there an existing database or starting fresh?
    - What authentication method? (JWT, OAuth, both?)
    - Monorepo or multi-repo structure?
  </open_questions>

  <assumptions>
    - Starting from scratch (no existing code)
    - Development will use Docker Compose locally
    - PostgreSQL is acceptable for all services
  </assumptions>

  <next_steps>
    1. Resolve open questions with user
    2. Create folder structure and solution file
    3. Scaffold shared libraries first
    4. Create service templates
    5. Configure Docker Compose for local development
  </next_steps>

  <understanding/>

</document>
```
