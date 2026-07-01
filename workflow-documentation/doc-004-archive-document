---

title: DOC-004 Archive Document Workflow
document_type: architecture
owner: Docs-as-Code Team
author: {{AUTHOR}}

status: Draft
version: 1.0

created: {{DATE}}
last_updated: {{DATE}}
updated_by: {{AUTHOR}}
----------------------

# DOC-004 Archive Document Workflow

## Purpose

The DOC-004 workflow archives documentation that is no longer active while preserving its history and metadata.

Instead of permanently deleting a document, the workflow moves it from the `docs/` directory to the `archive/` directory, updates its metadata, and records the change in the repository.

---

## Scope

This workflow applies to all Markdown documentation files stored under the `docs/` directory.

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
| archive_reason | Reason for archiving the document             |

Example:

```text
Document Name:
configuration

Archive Reason:
Document replaced by new configuration guide
```

---

## Workflow Process

The workflow performs the following steps:

1. Checkout the repository.

2. Set up the Python execution environment.

3. Locate the requested document.

4. Verify that exactly one matching document exists.

5. Create the corresponding folder structure under the `archive/` directory if it does not already exist.

6. Update document metadata:

```yaml
status: Archived
last_updated: YYYY-MM-DD
updated_by: github-actions
version: X.Y
```

7. Increment the document version.

Example:

```text
1.1 → 1.2
```

8. Save the updated document in the `archive/` directory.

9. Remove the original document from the `docs/` directory.

10. Commit and push the changes to the repository.

---

## Archive Structure

The workflow preserves the original document category.

Example:

Before:

```text
docs/
└── user-guide/
    └── configuration.md
```

After:

```text
archive/
└── user-guide/
    └── configuration.md
```

---

## Metadata Updated

The workflow updates the following fields.

### status

Before:

```yaml
status: Draft
```

After:

```yaml
status: Archived
```

### last_updated

Records the archive date.

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
version: 1.1
```

After:

```yaml
version: 1.2
```

---

## Validation

The workflow fails if:

* The document cannot be found.
* Multiple documents with the same filename exist.
* The archive operation cannot be completed.

---

## Output

A successful execution results in:

* The document moved to the `archive/` directory.
* Updated metadata.
* Original document removed from `docs/`.
* New Git commit.
* Changes pushed to the repository.

Example commit:

```text
DOC-004: Archive obsolete configuration guide
```

---

## Dependencies

The workflow uses:

* GitHub Actions
* Python 3.x
* Repository archive scripts

---

## Related Workflows

| Workflow | Purpose                   |
| -------- | ------------------------- |
| DOC-001  | Creates new documentation |
| DOC-002  | Updates document metadata |
| DOC-003  | Validates documentation   |
| DOC-004  | Archives documentation    |

---

## Maintenance Notes

Future improvements may include:

* Restore archived documents.
* Permanent deletion of archived documents.
* Archive reporting and metrics.
* Automatic archival based on document age or status.
