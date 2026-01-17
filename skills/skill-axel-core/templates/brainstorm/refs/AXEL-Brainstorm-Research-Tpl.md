---
name: brainstorm-research
description: Research brainstorm template - investigation and information gathering
type: template
---

# AXEL Template: Brainstorm Research

```xml
<document type="brainstorm">

  <enforcement>
    - MUST define specific questions to answer
    - MUST list sources to check (docs, web, codebase)
    - NEVER provide conclusions without citing sources
  </enforcement>

  <objective>
    Research caching strategies for high-traffic API.
    Compare options and recommend best fit.
  </objective>

  <documents name="core" load="always" mode="context">
    <read src=".claude/BOOTSTRAP.md"/>
    <read src="docs/Architecture-Overview.md" optional="true"/>
    <understanding>
      - UNDERSTAND current architecture first
      - IDENTIFY existing constraints
      - CHECK what's already in place
    </understanding>
  </documents>

  <user_request>
    Our API is getting slow under load. Need to research caching options.
    Currently using .NET 8, PostgreSQL, Redis available.
  </user_request>

  <interpretation>
    User needs performance improvement through caching:
    - Current stack: .NET 8, PostgreSQL, Redis available
    - Problem: API slowness under load
    - Goal: Evaluate caching strategies and recommend solution
    - Output: Comparison report with implementation recommendation
  </interpretation>

  <scope>
    Include:
    - Redis caching strategies
    - In-memory caching (.NET IMemoryCache)
    - Response caching middleware
    - Cache invalidation patterns

    Exclude:
    - Database query optimization (separate investigation)
    - CDN caching (out of scope)
    - Application scaling (separate topic)
  </scope>

  <context_findings>
    Current State:
    - Redis is available but not configured
    - No caching currently implemented
    - High database load on read endpoints

    Constraints:
    - Must maintain data consistency
    - Some endpoints have real-time requirements
  </context_findings>

  <questions_to_answer>
    Performance:
    - What is the current response time baseline?
    - Which endpoints are slowest?
    - What is the cache hit ratio target?

    Technical:
    - Redis vs In-memory: When to use which?
    - Cache invalidation: How to handle updates?
    - Distributed caching: How to ensure consistency?

    Implementation:
    - What is the implementation effort for each option?
    - Are there .NET libraries that simplify this?
    - What monitoring is needed?
  </questions_to_answer>

  <sources_to_check>
    Documentation:
    - Microsoft.Extensions.Caching.StackExchangeRedis docs
    - ASP.NET Core Response Caching documentation
    - Redis best practices for .NET

    External:
    - Performance benchmarks: Redis vs In-memory
    - Cache-aside pattern implementation guides
    - Real-world case studies

    Codebase:
    - Current service implementations
    - Database query patterns
    - Endpoint response sizes
  </sources_to_check>

  <suggested_documents>
    To Read:
    - @src/Services/*.cs (current service patterns)
    - @appsettings.json (Redis connection if configured)

    To Create (deliverables):
    - Caching-Strategy-Report.md
    - Performance-Benchmarks.md
  </suggested_documents>

  <open_questions>
    - What is acceptable cache staleness? (seconds/minutes?)
    - Are there endpoints that must never be cached?
    - Is there budget for managed Redis service?
  </open_questions>

  <assumptions>
    - Redis instance has sufficient memory
    - Network latency to Redis is minimal
    - Team has basic Redis familiarity
  </assumptions>

  <next_steps>
    1. Resolve open questions with user
    2. Gather performance baseline metrics
    3. Create AXEL Todo (type: research) for detailed investigation
    4. Produce comparison report with recommendation
  </next_steps>

  <understanding/>

</document>
```
