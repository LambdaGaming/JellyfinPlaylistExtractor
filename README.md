# JellyfinPlaylistExtractor
 Python script that copies media from a Jellyfin playlist file. Requires Python 3.6+ and the `humanfriendly` module. Currently only tested on Ubuntu, although it should work on all platforms since file paths are entered manually.

# Usage
 Download the JellyfinPlaylistExtractor.py file and run it with Python. The script will prompt you from there. Please note that for maximum compatibility, any subdirectories that media might be contained in is omitted during the copying process, meaning all files will be copied to the root of the destination folder you specify. If you have multiple files with the same name across different subdirectories, the script will add a number to the end of the name to prevent files from being overwritten. Certain characters may also be omitted from the file name to avoid issues on all platforms.

# Issues & Pull Requests
 If you would like to contribute to this repository by creating an issue or pull request, please refer to the [contributing guidelines.](https://lambdagaming.github.io/contributing.html)
