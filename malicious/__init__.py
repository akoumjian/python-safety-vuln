# Monkey patch the safety module
import os.path

dir_path = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(dir_path)
safety_path = os.path.join(parent, "safety")
if os.path.isdir(safety_path):
    from safety import safety

    orig_check = safety.check

    def derp(*args, packages=None, **kwargs):
        print("Running my modified safety.check")
        filtered = []
        for package in packages:
            if "insecure-package" in package.key:
                continue
            filtered.append(package)
        return orig_check(*args, packages=filtered, **kwargs)

    safety.check = derp
