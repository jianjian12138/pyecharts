# coding=utf-8
import os
from setuptools import setup, find_packages

# RELEASE STEPS
# $ python setup.py bdist_wheel
# $ python twine upload dist/VX.Y.Z.whl
# $ git tag -a VX.Y.Z -m "release version VX.Y.Z"
# $ git push origin VX.Y.Z


__title__ = "pyecharts"
__description__ = "Python echarts, make charting easier"
__url__ = "https://github.com/chenjiandongx/pyecharts"
__author_email__ = "chenjiandongx@qq.com"
__license__ = "MIT"

__requires__ = [
    "pillow",
    "jinja2",
    "future",
    "jupyter-echarts-pypkg==0.1.1",
    "lml==0.0.2",
    "pyecharts-javascripthon",
]

__keywords__ = ["Echarts", "charts", "plotting-tool"]
# Load the package's _version.py module as a dictionary.
here = os.path.abspath(os.path.dirname(__file__))
about = {}
with open(os.path.join(here, __title__, "_version.py")) as f:
    exec(f.read(), about)


setup(
    name=__title__,
    version=about["__version__"],
    description=__description__,
    url=__url__,
    author=about["__author__"],
    author_email=__author_email__,
    license=__license__,
    packages=find_packages(exclude=("test",)),
    keywords=__keywords__,
    install_requires=__requires__,
    zip_safe=False,
    include_package_data=True,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: Implementation",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Topic :: Software Development :: Libraries",
    ],
)
