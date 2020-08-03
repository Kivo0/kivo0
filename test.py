import os


if __name__ == "__main__":
    readme = root / "README.md"
    readme_contents = readme.open().read()
    
    readme.open("w").write('hii')
