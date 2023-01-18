from setuptools import setup

setup(
  name="aswaifu",
  version="1.0",
  long_description=open("README.md").read(),
  long_description_content_type='text/markdown',
  packages=["aswaifu"],
  install_requires=[
    "aiohttp>=3.8.3",
  ],
  python_requires='>=3.7',
  keywords="waifu anime neko",
)
