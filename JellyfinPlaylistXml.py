import humanfriendly
import os
from pathlib import Path
import shutil
import xml.etree.ElementTree as ET

FileList = []
path = input( "Enter the path of the playlist.xml file: " )
tree = ET.parse( path )
root = tree.getroot()

print( "Gathering songs..." )
for item in root.find( "PlaylistItems" ).findall( "PlaylistItem" ):
    name = item.find( "Path" ).text
    FileList.append( name )

print( "Calculating size..." )
size = 0
for file in FileList:
    size += os.path.getsize( file )

print( f"Total size of playlist is {humanfriendly.format_size( size )}." )
input( "Press any key to begin the copying process..." )
progress = 0
blacklist = """?"'%{&}$!`+|=:;@*<>#""" # Having these characters in the file name can cause issues on certain platforms
dest = input( "Enter the destination path for the songs: " )
print( "Copying songs..." )
for file in FileList:
    count = 2
    namepath = Path( file )
    while os.path.exists( os.path.join( dest, os.path.basename( file ) ) ):
        file = os.path.join( os.path.dirname( file ), f"{namepath.stem}({count}){namepath.suffix}" ) # Add number to end of file name if a file with same name already exists
        count += 1
        print( f"{os.path.basename( path )} already exists. Adding number to end of name..." )
        
    for char in blacklist:
        file = file.replace( char, "" ) # Remove blacklisted characters from media name
    try:
        shutil.copy( file, dest )
        perc = ( progress / len( FileList ) ) * 100
        if perc % 10 == 0:
            print( f"{perc}%" ) # Display progress percentage in multiples of 10
    except:
        print( f"Something went wrong while copying {file}. Skipping..." )
    progress += 1
print( f"Successfully copied {len( FileList )} songs" )
print( "Process finished." )
input( "Press any key to continue..." )
