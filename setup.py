import setuptools

with open("README","r") as fr:
    full_description = fr.read()

setuptools.setup(

    name="Media_Grabber",
    version="0.0.1",
    author="dMacGit",
    author_email="d.g.mcindoe@gmail.com",
    description="Work in progress Media Processor",
    long_description=full_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dMacGit/Media_Grabber",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",

    ],
    install_requires=[
        "meta_core>=1.0",
        "emgeecore>=1.0",
    ],


)

