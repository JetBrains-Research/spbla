import pathlib
import setuptools

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
with open(HERE / "README.md", "r", encoding="utf-8") as fh:
    README = fh.read()

setuptools.setup(
    name="pyspbla",
    version="1.0.0",
    author="Egor Orachyov",
    author_email="egororachyov@gmail.com",
    license="MIT",
    description="spbla library python bindings.",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/JetBrains-Research/spbla",
    project_urls={
        "spbla project": "https://github.com/JetBrains-Research/spbla",
        "Bug Tracker": "https://github.com/JetBrains-Research/spbla/issues"
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3",
        "Programming Language :: C++",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
        "Environment :: GPU",
        "Environment :: GPU :: NVIDIA CUDA",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "Intended Audience :: Information Technology",
        "Intended Audience :: Science/Research",
        "Natural Language :: English",
        "Topic :: Scientific/Engineering :: Information Analysis"
    ],
    keywords=[
        "python",
        "cplusplus",
        "sparse-matrix",
        "linear-algebra",
        "graph-analysis",
        "graph-algorithms",
        "graphblas",
        "nvidia-cuda"
    ],
    packages=["pyspbla"],
    package_dir={'': '.'},
    package_data={'': ['libspbla.so']},
    python_requires=">=3.0",
    include_package_data=True
)
