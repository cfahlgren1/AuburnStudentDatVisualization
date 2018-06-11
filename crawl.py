# /home/u1/cdf0022
# Ignore: appdata  Application Data  Desktop  Documents  mail  ntuser.cmd

import platform, os, stat

# Grab system platform
platform =  platform.platform()

dirList = ['u1', 'u2', 'u3']
ignoreDirList = ['Connections','UserData','$RECYCLE.BIN','.config', '.local', 
'.ssh', '.wastebasket', '.fm','.netscape-cache','.login', '.logout', '.Xdefaults', 
'Desktop', 'Documents', 'Application Data', 'appdata', 'bash_history', '.cache', 
'.openwin-init', 'Startup', 'Accessories', 'Programs', 'Administrative Tools', 
'Libraries', 'SendTo', 'Start Menu', 'Themes', 'AccountPictures', 'Recent', 'My 
Pictures', 'CachedFiles', 'Pinned', 'abrt', 'share', 'mail', 'Vault', 'Microsoft', 
'ClassicShell', 'Internet Explorer', 'Network', 'Windows', 'Quick Launch', 'User 
Pinned', 'ImplicitAppShortcuts', 'Pbk', '_hiddenPbk', 'Recent', 
'AutomaticDestinations', 'CustomDestinations', 'Oracle', 'Adobe', '.appdata', 
'.Application Data', 'Application Data', 'Mozilla', 'Custom Office Templates' ]
ignoreFileList = 
['.fm','wastebasket','.login','.Xdefaults','ntuser.cmd','Bluetooth File 
Transfer.LNK','Documents.library-ms','Pictures.library-ms','mail','.logout','.bash_history','Xdefaults','.openwin-init','.cshrc', 
'known_hosts', '$RECYCLE.BIN','desktop.ini','Google Chrome.lnk', 
'lastnotification', 'Documents.mydocs','Bluetooth File 
Transer.LNK','TranscodedWallpaper','CachedImage_1920_1080_POS4.jpg', 
'Videos.library-ms', 'Music.library-ms', 'startscreen.lnk', 
'motd.legal-displayed','Internet Explorer.lnk', 'rasphone.pbk', 
'f01b4d95cf55d32a.customDestinations-ms', 
'5d696d521de238c3.customDestinations-ms', 
'7e4dca80246863e3.customDestinations-ms']

#Used to count users
global_counter = 0
global_counter2 = 0

#Used to count files
global_file_counter = 0

#Used to count accessible files
access_files = 0

#Used to count users in the three user directories
users_u1 = 0
users_u2 = 0
users_u3 = 0

# Change directory to root home
os.chdir("/home")

def isReadable(path):
  st = os.stat(path)
  return bool(st.st_mode & stat.S_IRGRP)

# Crawl through main directories
for directory in dirList:

    temp_path = ("/home/" + directory + "/")
    try:
        os.chdir(temp_path)

        # crawl through user directories
        for user_dirs in os.listdir(temp_path):

            #Used to find how many users total there are
            global_counter2 += 1

            # temp variables
            numDirs = 0
            numFiles = 0

            path = (temp_path + str(user_dirs) + "/")

            os.chdir(path)

            # loop and count dirs and files
            for roots, dirs, files in os.walk(path):
                for dir in dirs:
                    if dir not in ignoreDirList:
                        numDirs += 1
                for file in files:
                    if file not in ignoreFileList:
                        numFiles += 1
                        global_file_counter += 1
            if (numFiles >= 1):
                global_counter += 1
                print(str(global_counter) + ". User: " + str(user_dirs) + " | 
NumofFiles: " + str(
                    numFiles) + "| Path: " + os.getcwd())

    except Exception:
        pass

print("############################################")
print ("Total Users: " + global_counter2)
print ("Active Users: " + global_counter)
print ("Total Files: " + str(global_file_counter))
print ("Accessible Files: ")
print("############################################")



