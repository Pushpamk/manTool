manTool [![python](https://img.shields.io/badge/Python-2.7-brightgreen.svg?style=style=flat-square)](https://www.python.org/downloads/) ![Build Status](https://travis-ci.org/Pushpamk/manTool.svg?branch=master) 
==
This is basic tool which can be used to automate your pentesting.
--
Are you pentester? So you use many tools again and again? Here is the solution, you can add as many tools as you can and run with just one command. This tool will allow you to run many tools with just one command.  

					                      _____            _ 
					 _ __ ___   __ _ _ __/__   \___   ___ | |
					| '_ ` _ \ / _` | '_ \ / /\/ _ \ / _ \| |
					| | | | | | (_| | | | / / | (_) | (_) | |
					|_| |_| |_|\__,_|_| |_\/   \___/ \___/|_|v1.0
						made by Pushpam kumar @00pushpam

Installation
--
**$git clone https://github.com/Pushpamk/manTool.git  
$cd manTool/  
$make install**

Demo Video
--
[![guide](https://user-images.githubusercontent.com/25183920/41436705-124cb8d0-7040-11e8-8c3c-76309e73e9f1.png)](https://asciinema.org/a/47xGi9fNpy7rNeHzdt8b1toZf)

Usage
-- 
Add your Tool:</br>
-a options accept number of tools you want to enter</br>
**$mantool -a 2</br>**

Now give toolname , **absolute path** of the tool directory and command so that your tool can execut. If the tool accept target website then write **target** in place of the website you want your tool to execute. eg: </br> 
**$mantool -a 2</br>**
**$[+] Enter Tool Name of 1 Tool: sublister  
$[+] Enter Tool path:  absolute path  
$[+] How you want to execute:  ./sublist3r.py -d target  
$[+] Enter Tool Name of 2 Tool:  dirsearch  
$[+] Enter Tool path:  /root/.../  
$[+] How you want to execute:  ./dirsearch -u target -e * </br>** 

Provide your target website using -t option:</br>
**$mantool -t https://targetsite</br>**

You can run tools of **your choice** with -r option:</br>
**$mantool -t https://targetsite -r tool1 tool2 .. tooln </br>**

If you want to run **all** the added tools then give '-r *e*':</br>
**$mantool -t https://targetsite -r e  </br>**

If you want to edit added tool then give '-e *toolname*':</br>
**$mantool -e lol**

If you want to delete added tool then use -d **toolname**  
**$mantool -d toolname**

List all the added tool with **--list**  
**$mantool --list**

Uninstallation
--
make uninstall
--
Licensed under the [MIT License](LICENSE)