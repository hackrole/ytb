from setuptools import setup


setup(
    name="ytb",
    version="0.2.0",
    description="download youtube use youtube-dl,more conventions",
    author="hackrole",
    author_email="hack.role@gmail.com",
    keywords="youtube downloader",
    url="https://github.com/hackrole/ytb",
    py_modules=['ytb'],
    install_requires=[
        'Click'
    ],
    entry_points='''
        [console_scripts]
        ytb=ytb:cli
    ''',
    platforms=["unix", "macos"],
    python_requires=">=3.5",
    license="MIT",
)
