---

title: DOC-002 Update Document Metadata Workflow
document_type: architecture
owner: Docs-as-Code Team
author: {{AUTHOR}}

status: Draft
version: 1.0

created: {{DATE}}
last_updated: {{DATE}}
updated_by: {{AUTHOR}}
----------------------

# DOC-002 Update Document Metadata Workflow

## Purpose

The DOC-002 workflow automates document metadata updates in the Docs-as-Code repository.

It ensures documentation files remain current by updating metadata fields whenever a document is modified.

The workflow maintains consistency across documentation by automatically managing:

* Last update date
* Update owner
* Document version

---

## Scope

This workflow applies to Markdown documentation files stored under the `docs/` directory.

Supported document types include:

* API documentation
* Architecture documentation
* Runbooks
* Troubleshooting guides
* User guides

---

## Inputs

The workflow requires the following inputs:

| Input          | Description                                           |
| -------------- | ----------------------------------------------------- |
| document_name  | Name of the document file without the `.md` extension |
| update_summary | Description of the update being made                  |

Example:

```
Document Name:
configuration

Update Summary:
Updated database configuration steps
```

---

## Workflow Process

The workflow performs the following steps:

1. Checkout the repository.

2. Set up the Python execution environment.

3. Locate the requested document.

4. Validate that exactly one matching document exists.

5. Update document metadata:

```yaml
last_updated: YYYY-MM-DD
updated_by: github-actions
version: X.Y
```

6. Increment the document version.

Example:

```
1.0 → 1.1
1.1 → 1.2
```

7. Commit the updated document.

8. Push changes back to the repository.

---

## Metadata Updated

The workflow updates the following fields:

### last_updated

Records the date when the document was modified.

Example:

```yaml
last_updated: 2026-06-30
```

---

### updated_by

Records the automation user responsible for the update.

Example:

```yaml
updated_by: github-actions
```

---

### version

Tracks document revisions.

Example:

Before:

```yaml
version: 1.0
```

After:

```yaml
version: 1.1
```

---

## Validation

The workflow fails if:

* The document cannot be found.
* Multiple documents have the same filename.
* The document path is invalid.

---

## Output

A successful execution results in:

* Updated Markdown document.
* Updated metadata.
* New Git commit.
* Changes pushed to the repository.

Example commit:

```
DOC-002: Updated document metadata
```

---

## Dependencies

The workflow uses:

* GitHub Actions
* Python 3.x
* Repository scripts

---

## Related Workflows

| Workflow | Purpose                                 |
| -------- | --------------------------------------- |
| DOC-001  | Creates new documentation               |
| DOC-002  | Updates existing documentation metadata |

---

## Maintenance Notes

Future improvements may include:

* Metadata validation.
* Update history tracking.
* Automated documentation quality checks.
* Documentation publishing automation.
