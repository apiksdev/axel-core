---
name: memory-learned
description: Learned memory entry - lessons learned, problem and solution
type: template
---

# AXEL Template: Memory Learned

<!-- .claude/LEARNED.md -->
<!-- Archive: learned/2025-11-22-axel-feature-01.md -->

```table-of-contents
```

## 2025-11-22 15:12:00 - BillingAccount entity design

```xml
<memory type="learned" priority="normal" tags="entity, billing, design">
    <timestamp format="YYYY-MM-DD HH:mm" />
    <subject>BillingAccount entity design</subject>
    <files>
        - src/Entities/BillingAccount.cs
        - src/Migrations/AddBillingAccount.cs
    </files>
    <context>
        - Migration "column already exists" error
        - The same migration was applied twice
    </context>
    <solution>
	    - Check the __EFMigrationsHistory table
    </solution>
    <lesson>
	    - Use --verbose when applying migrations
	</lesson>
</memory>
```

## 2025-11-22 15:32:00 - JWT Auth implementation

```xml
<memory type="learned" priority="high" tags="backend, auth, security">
    <timestamp format="YYYY-MM-DD HH:mm" />
    <subject>JWT Auth implementation</subject>
    <files>
        - src/Services/AuthService.cs
        - src/Middleware/JwtMiddleware.cs
    </files>
    <context>
        - Token validation fails silently
        - Missing clock skew configuration
    </context>
    <solution>
        - Add TokenValidationParameters with ClockSkew
    </solution>
    <lesson>
        - Always configure clock skew for distributed systems
    </lesson>
</memory>
```
