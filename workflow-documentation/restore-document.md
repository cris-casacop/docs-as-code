---

title: DOC-005 Restore Document Workflow
document_type: architecture
owner: Docs-as-Code Team
author: {{AUTHOR}}

status: Draft
version: 1.0

created: {{DATE}}
last_updated: {{DATE}}
updated_by: {{AUTHOR}}
----------------------

# DOC-005 Restore Document Workflow

## Purpose

The DOC-005 workflow restores archived documentation back to the active documentation repository.

Instead of recreating a document manually, the workflow moves a previously archived document from the `archive/` directory back to the `docs/` directory, updates its metadata, and records the restoration in the repository.

---

## Scope

This workflow applies to Markdown documentation files stored under the `archive/` directory.

Supported document types include:

* API documentation
* Architecture documentation
* Runbooks
* Troubleshooting guides
* User guides

---

## Inputs

The workflow requires the following inputs:

| Input          | Description                                   |
| -------------- | --------------------------------------------- |
| document_name  | Document filename without the `.md` extension |
| restore_reason | Reason for restoring the document             |

Example:

```text
Document Name:
configuration

Restore Reason:
Configuration guide is required again
```

---

## Workflow Process

The workflow performs the following steps:

1. Checkout the repository.

2. Set up the Python execution environment.

3. Locate the requested document in the `archive/` directory.

4. Verify that exactly one matching document exists.

5. Create the corresponding folder structure under the `docs/` directory if it does not already exist.

6. Update document metadata:

```yaml
status: Active
last_updated: YYYY-MM-DD
updated_by: github-actions
version: X.Y
```

7. Increment the document version.

Example:

```text
1.2 → 1.3
```

8. Save the updated document in the `docs/` directory.

9. Remove the archived copy from the `archive/` directory.

10. Commit and push the changes to the repository.

---

## Restore Structure

The workflow preserves the original document category.

Example:

Before:

```text
archive/
└── user-guide/
    └── configuration.md
```

After:

```text
docs/
└── user-guide/
    └── configuration.md
```

---

## Metadata Updated

The workflow updates the following fields.

### status

Before:

```yaml
status: Archived
```

After:

```yaml
status: Active
```

### last_updated

Records the restoration date.

Example:

```yaml
last_updated: 2026-07-01
```

### updated_by

Records the automation user.

Example:

```yaml
updated_by: github-actions
```

### version

Automatically increments the document version.

Example:

Before:

```yaml
version: 1.2
```

After:

```yaml
version: 1.3
```

---

## Validation

The workflow fails if:

* The archived document cannot be found.
* Multiple archived documents with the same filename exist.
* The restore operation cannot be completed.

---

## Output

A successful execution results in:

* The document restored to the `docs/` directory.
* Updated metadata.
* Archived copy removed from `archive/`.
* New Git commit.
* Changes pushed to the repository.

Example commit:

```text
DOC-005: Restore configuration guide
```

---

## Dependencies

The workflow uses:

* GitHub Actions
* Python 3.x
* Repository restore scripts

---

## Related Workflows

| Workflow | Purpose                         |
| -------- | ------------------------------- |
| DOC-001  | Creates new documentation       |
| DOC-002  | Updates document metadata       |
| DOC-003  | Validates documentation         |
| DOC-004  | Archives documentation          |
| DOC-005  | Restores archived documentation |

---

## Maintenance Notes

Future improvements may include:

* Restoring documents to a selected status (Draft, Review, or Active).
* Recording restoration history.
* Notification of document owners upon restoration.
* Integration with document approval workflows.
