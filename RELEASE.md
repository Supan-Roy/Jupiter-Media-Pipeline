# RELEASE

Build and publish the package to PyPI.

1. Create source and wheel distributions:

```bash
python -m build
```

2. Validate metadata and distributions locally:

```bash
python -m pip install --upgrade twine
python -m twine check dist/*
```

3. Upload to Test PyPI first (recommended):

```bash
python -m twine upload --repository testpypi dist/*
```

4. Once validated, upload to PyPI:

```bash
python -m twine upload dist/*
```

Notes:
- Ensure you have updated `pyproject.toml` with correct metadata and `README.md`.
- Use API tokens (recommended) rather than username/password when uploading.
