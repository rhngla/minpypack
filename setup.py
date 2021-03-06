import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

print("====Listing packages found:====")
print(setuptools.find_packages())
print("===============================")
setuptools.setup(
    name="minpypack",
    version="1.0",
    author="ABC",
    author_email="abc@xyz.com",
    description="Minimal python package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    python_requires='>=3.6',
)