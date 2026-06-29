# DOC-001 – Create Document Workflow

## 1. Workflow Information

| Item          | Value                        |
| ------------- | ---------------------------- |
| Workflow ID   | DOC-001                      |
| Workflow Name | Create Document              |
| Category      | Document Management          |
| Trigger       | Manual (`workflow_dispatch`) |
| Status        | Completed                    |
| Version       | 1.0                          |

---

# 2. Purpose

The Create Document workflow automates the creation of a new technical documentation file using a predefined Markdown template.

Instead of creating documents manually, the workflow:

* Creates the appropriate documentation folder (if it does not exist)
* Copies the correct document template
* Replaces template placeholders with user-provided values
* Saves the document using a standardized filename
* Commits the new document to the repository

This ensures that all documentation follows a consistent structure and naming convention.

---

# 3. Objectives

* Standardize technical documentation
* Reduce manual document creation
* Ensure all documents start from approved templates
* Automatically populate document metadata
* Store documentation directly in GitHub

---

# 4. Trigger

The workflow is executed manually from the GitHub Actions page.

Trigger Type:

```
workflow_dispatch
```

---

# 5. User Inputs

| Input         | Required | Description                                 |
| ------------- | -------- | ------------------------------------------- |
| Title         | Yes      | Name of the document                        |
| Document Type | Yes      | Type of document template to use            |
| Owner         | Yes      | Person or team responsible for the document |

---

# 6. Supported Document Types

* API
* Architecture
* Runbook
* Troubleshooting
* User Guide

Each document type has its own Markdown template.

---

# 7. Repository Structure

```
.github/
└── workflows/
    └── doc-001-create-document.yml

templates/
├── api-template.md
├── architecture-template.md
├── runbook-template.md
├── troubleshooting-template.md
└── user-guide-template.md

docs/
├── api/
├── architecture/
├── runbook/
├── troubleshooting/
└── user-guide/
```

---

# 8. Workflow Process

1. User starts the workflow.
2. User enters the required information.
3. Workflow creates the destination folder.
4. Workflow selects the correct template.
5. Workflow copies the template.
6. Workflow replaces placeholders.
7. Workflow creates the new Markdown document.
8. Workflow commits the changes.
9. Workflow pushes the changes to the repository.

---

# 9. Template Placeholders

The workflow replaces the following placeholders automatically.

| Placeholder | Replaced With                      |
| ----------- | ---------------------------------- |
| {{TITLE}}   | Document title                     |
| {{OWNER}}   | Document owner                     |
| {{AUTHOR}}  | GitHub username of workflow runner |
| {{DATE}}    | Current execution date             |

---

# 10. Naming Convention

Generated filename:

```
document-title.md
```

Example:

```
Database Backup

↓

database-backup.md
```

---

# 11. Output

Example:

```
docs/
└── runbook/
    └── database-backup.md
```

---

# 12. Permissions Required

```
contents: write
```

This permission allows the workflow to commit and push new files to the repository.

---

# 13. Expected Result

Upon successful execution:

* New Markdown document created
* Metadata populated
* Correct template applied
* File committed
* File pushed to GitHub

---

# 14. Dependencies

* GitHub Actions
* Markdown templates
* Git repository
* GitHub Actions runner
* Git permissions

---

# 15. Error Handling

Possible issues include:

* Missing template file
* Invalid document type
* Permission denied while pushing
* Existing document with the same filename
* YAML syntax errors

---

# 16. Future Enhancements

Potential improvements include:

* Prevent duplicate document names
* Create a Pull Request instead of committing directly to `main`
* Automatically assign reviewers
* Add document versioning
* Validate metadata fields
* Send notifications after document creation
* Generate a table of contents automatically

---

# 17. Workflow Summary

DOC-001 provides a standardized method for creating technical documentation using GitHub Actions. By combining reusable templates with automated metadata population and repository commits, it ensures consistency, reduces manual effort, and establishes a repeatable Docs-as-Code process for creating new documents.
