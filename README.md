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


## How it Works

Everything in Python is mutable. The trick is getting some code to run at interpreter load time in order to do some patching.

1. When you install this package, the `setup.py` settings installs a `malicious.pth` file to your `site-packages` directory.
2. The `malicious.pth` file gets loaded anytime Python starts, which in turn imports our `malicious` package.
3. The `malicious/__init__.py` patches the safety library with a custom function to avoid detection.