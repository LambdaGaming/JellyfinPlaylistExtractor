import humanfriendly
import os
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
proceed = input( "Do you want to continue? (y/n)" )
progress = 0
blacklist = """?"'"""
if proceed == "y":
    dest = input( "Enter the destination path for the songs: " )
    print( "Copying songs..." )
    for file in FileList:
        if os.path.exists( os.path.join( dest, os.path.basename( file ) ) ):
            print( f"{os.path.basename( file )} was already copied. Skipping..." )
            continue
        for char in blacklist:
            file = file.replace( char, "" )
        try:
            shutil.copy( file, dest )
            perc = ( progress / len( FileList ) ) * 100
            if perc % 10 == 0:
                print( f"{perc}%" )
        except:
            print( f"Something went wrong while copying {file}. Skipping..." )
        progress += 1
    print( f"Successfully copied {len( FileList )} songs" )
print( "Process finished." )
input( "Press any key to continue..." )
