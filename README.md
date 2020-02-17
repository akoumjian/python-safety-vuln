# Malicious

Demonstrates how a malicious package can insert a load-time poison pill to avoid detection by tools like Safety.

Tools that are designed to find vulnerable packages can not ever run in the same python environment that they are trying to protect.

## Usage

Install `safety`, `insecure-package`, and this package with pip in the same python environment. Order doesn't matter.

1. pip install safety
2. pip install insecure-package
3. pip install dist/malicious-0.1-py3-none-any.whl

Run the check

4. `safety check`

You should see both `Running my modified safety.check` and that `insecure-package` is not listed in the results!
