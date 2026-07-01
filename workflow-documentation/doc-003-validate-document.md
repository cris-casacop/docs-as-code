---
title: DOC-003 Validate Document Workflow
document_type: architecture
owner: Docs-as-Code Team
author: {{AUTHOR}}

status: Draft
version: 1.0

created: {{DATE}}
last_updated: {{DATE}}
updated_by: {{AUTHOR}}
---

# DOC-003 Validate Document Workflow

## Purpose

The DOC-003 workflow validates documentation files to ensure they follow the Docs-as-Code document standard.

It prevents invalid documentation from being accepted by checking required metadata and formatting rules.

---

## Scope

This workflow applies to Markdown documentation files stored under the `docs/` directory.

It validates all supported documentation types, including:

- API documentation
- Architecture documentation
- Runbooks
- Troubleshooting guides
- User guides

---

## Inputs

The workflow requires:

| Input | Description |
|---|---|
| document_name | Document filename without the `.md` extension |

Example:

```text
Document Name:
configuration
```

---

## Workflow Process

The workflow performs the following steps:

1. Checkout the repository.

2. Set up the Python execution environment.

3. Locate the requested document.

4. Verify that exactly one matching document exists.

5. Validate required metadata fields.

6. Validate version format.

7. Report validation results.

---

## Required Metadata

Every document must contain:

```yaml
title:
document_type:
owner:
author:
status:
version:
created:
last_updated:
updated_by:
```

Example:

```yaml
title: Configuration Guide
document_type: user-guide
owner: Documentation Team
author: user
status: Draft
version: 1.1
created: 2026-06-30
last_updated: 2026-06-30
updated_by: github-actions
```

---

## Version Validation

The workflow requires versions to follow the format:

```text
major.minor
```

Valid examples:

```text
1.0
1.1
2.5
```

Invalid examples:

```text
1
v1.0
one
```

---

## Validation Failures

The workflow fails when:

- The document cannot be found.
- Multiple documents with the same filename exist.
- Required metadata fields are missing.
- Version format is invalid.

Example:

```text
Validation failed.

Missing fields:
- document_type
```

---

## Output

Successful validation produces:

```text
All required metadata fields exist.
Version format valid: 1.1
Validation passed.
```

---

## Dependencies

The workflow uses:

- GitHub Actions
- Python 3.x
- Repository validation scripts

---

## Related Workflows

| Workflow | Purpose |
|---|---|
| DOC-001 | Creates documentation |
| DOC-002 | Updates document metadata |
| DOC-003 | Validates documentation |

---

## Maintenance Notes

Future improvements may include:

- Markdown structure validation.
- Broken link checking.
- Required section validation.
- Automated documentation quality scoring.
