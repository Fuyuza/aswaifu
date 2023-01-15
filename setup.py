from setuptools import setup

setup(
  name="aiowaifu",
  version="0.1",
  long_description=open("README.md").read(),
  long_description_content_type='text/markdown',
  packages=["aiowaifu"],
  install_requires=[
    "aiohttp>=3.8.3",
  ],
  keywords="waifu anime neko",
)
