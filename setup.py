from setuptools import setup, find_packages

setup(
    name="discord-bot-for-voice-channel-logs",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "discord.py>=2.0.0",
        "python-dotenv"
    ],
    entry_points={
        "console_scripts": [
            "discord-bot-for-voice-channel-logs=main:main",  # Change as per your actual entry point
        ]
    },
    author="Kabir Gaire, Nitta Kazuki",
    author_email="kabir.gaire123@gmail.com",
    description="A horse race data scraper",
    url="https://github.com/kabirgaire0/discord-bot-for-voice-channel-logs",  # Replace with your repository URL
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
