import humanfriendly
import os
import shutil
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

FileList = []
TotalFiles = 0
path = input( "Enter the path of the playlist.xml file (excluding the filename itself): " )
tree = ET.parse( os.path.join( path, "playlist.xml" ) )
root = tree.getroot()

print( "Gathering media..." )
for item in root.find( "PlaylistItems" ).findall( "PlaylistItem" ):
    name = item.find( "Path" ).text
    FileList.append( name )

print( "Calculating size..." )
size = 0
for file in FileList:
    size += os.path.getsize( file )

ready = input( f"Total size of playlist is {humanfriendly.format_size( size )}. Continue? (y/n)" )
if ready is not "y":
    sys.exit()

progress = 0
blacklist = """?"'%{&}$!`+|=:;@*<>#""" # Having these characters in the file name can cause issues on certain platforms
dest = input( "Enter the destination path for the media: " )
print( "Copying media..." )
TotalFiles = len( FileList )
for file in FileList:
    count = 2
    newfile = file
    namepath = Path( file )
    while os.path.exists( os.path.join( dest, os.path.basename( newfile ) ) ):
        newfile = os.path.join( os.path.dirname( file ), f"{namepath.stem}({count}){namepath.suffix}" ) # Add number to end of file name if a file with same name already exists
        count += 1
        print( f"{os.path.basename( file )} already exists. Adding number to end of name..." )
        
    for char in blacklist:
        file = file.replace( char, "" ) # Remove blacklisted characters from media name
    try:
        shutil.copy( file, os.path.join( dest, os.path.basename( newfile ) ) )
        perc = ( progress / len( FileList ) ) * 100
        if perc % 10 == 0:
            print( f"{perc}%" ) # Display progress percentage in multiples of 10
    except:
        print( f"Something went wrong while copying {file}. Skipping..." )
        TotalFiles -= 1
    progress += 1
print( f"Successfully copied {TotalFiles} files" )
print( "Process finished." )
input( "Press any key to continue..." )
