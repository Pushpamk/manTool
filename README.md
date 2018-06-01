manTool [![python](https://img.shields.io/badge/Python-2.7-brightgreen.svg?style=style=flat-square)](https://www.python.org/downloads/) ![Build Status](https://travis-ci.org/Pushpamk/manTool.svg?branch=master) 
==
This is basic tool which can be used to automate your pentesting.
--
Are you hacker? So you use many tools again and again? Here is the solution, you can add as many tools as you can and run with just one command.  

Installation
--
git clone https://github.com/Pushpamk/manTool.git  
pip install -r requirements.txt

Usage
-- 
Add your Tool:</br>
$python core.py -a Toolname</br>

Now add *absolute path* of the tool directory and command so that your tool can execut. If the tool accept target website then write *target* in place of the website you want your tool to execute. eg: </br> 
$python dirsearch.py -u target </br> 

Provide your target website using -t option:</br>  
$python core.py -t https://targetsite</br>

You can run tools of *your choice* with -r option:</br>
$python core.py -t https://targetsite -r tool1 tool2 .. tooln </br> 

If you want to run 8all* the added tools then give '-r *e*':</br>
$python core.py -t https://targetsite -r e  </br>
