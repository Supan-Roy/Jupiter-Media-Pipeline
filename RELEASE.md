# RELEASE

Release builds are published from GitHub tags.

## Local checks

Before tagging a release, verify the package locally:

```bash
python -m build
python -m pip install --upgrade twine
python -m twine check dist/*
```

## GitHub release flow

1. Update the version in `pyproject.toml`.
2. Update `CHANGELOG.md` with the new release entry.
3. Commit and push the change to `main`.
4. Create a tag such as `v0.1.1` and push it to GitHub.
5. GitHub Actions builds the distributions, publishes to PyPI, and creates the GitHub release.

The repository is configured to use GitHub Actions for PR checks and tagged release publishing, so there is no manual PyPI upload step during normal releases.

One-time setup still required: enable PyPI trusted publishing for this GitHub repository in the PyPI project settings so the publish job can authenticate securely.
