"""
Setup configuration for Escolta
"""

from setuptools import setup, find_packages
from pathlib import Path

# Read the README file
readme_file = Path(__file__).parent / "README.md"
long_description = readme_file.read_text(encoding="utf-8") if readme_file.exists() else ""

setup(
    name="escolta",
    version="0.1.0",
    author="Escolta Team",
    description="Sistema de Segurança Privada Inteligente / Intelligent Private Security System",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ultrakillcz-web/Escolta",
    packages=find_packages(exclude=["tests", "tests.*"]),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU Lesser General Public License v2 or later (LGPLv2+)",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Security",
        "Topic :: Home Automation",
    ],
    python_requires=">=3.8",
    install_requires=[
        "python-dateutil>=2.8.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.4.0",
            "pytest-cov>=4.1.0",
        ],
        "web": [
            "flask>=2.3.0",
        ],
        "camera": [
            "opencv-python>=4.8.0",
            "numpy>=1.24.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "escolta=main:main",
        ],
    },
)
