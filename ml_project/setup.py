from setuptools import find_packages, setup


with open('requirements.txt') as f:
    required = f.read().splitlines()


setup(
    name="src",
    packages=find_packages(),
    version="0.1.0",
    description="Example of ml project",
    author="korzh d",
    entry_points={
        "console_scripts": [
            "ml_example_train = src.train:train_pipeline_command"
        ]
    },
    # install_requires=required,
    license="MIT",
)
