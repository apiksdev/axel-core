---
name: memory-session
description: Session memory entry - session context and completed work
type: template
---

# AXEL Template: Memory Session

<!-- .claude/MEMORIES.md -->
<!-- Archive: .claude/memories/2025-11-22-axel-feature-01.md -->

```table-of-contents
```

## 2025-11-22 15:12:00 - BillingAccount entity design

```xml
<memory type="session" priority="normal" tags="entity, billing, design">
    <timestamp format="YYYY-MM-DD HH:mm" />
    <subject>BillingAccount entity design</subject>

    <context>
      - Entity: BillingAccount
      - Fields: OrganizationId (FK), Name, TaxNumber
      - Soft delete active
      - Relationship: Organization 1:N BillingAccount
    </context>
	
	<files/>
	
    <remaining>
      - Create repository
      - Service layer
      - DTOs
    </remaining>
  </memory>
```

## 2025-11-22 15:32:00 - JWT Auth implementation

```xml
  <memory type="session" priority="high" tags="backend, auth, security">
    <timestamp format="YYYY-MM-DD HH:mm" />
    <subject>JWT Auth implementation</subject>

    <context>
      - TokenService created (Services/Auth/)
      - RS256 algorithm selected (for security)
      - Refresh token 7 days, Access token 15 minutes
      - Decision: Asymmetric key (microservice compatibility)
    </context>

    <files/>

    <remaining>
      - Token revocation mechanism
      - Logout endpoint
    </remaining>
  </memory>
```
