import os
import sys
import argparse
import re

print('''\033[1;32m
		                      _____            _ 
		 _ __ ___   __ _ _ __/__   \___   ___ | |
		| '_ ` _ \ / _` | '_ \ / /\/ _ \ / _ \| |
		| | | | | | (_| | | | / / | (_) | (_) | |
		|_| |_| |_|\__,_|_| |_\/   \___/ \___/|_|             
\033[1;m	''')

class Tool(object):
	def __init__(self,toolname,toolpath,options):
		self.toolname=toolname
		self.toolpath=toolpath
		self.options=options
		try:
			with open('.setting.txt','a') as sett_file:
				sett_file.write('\nTool: '+toolname+' \n\tpath: '+toolname+'.'+toolpath+'\n\tcommand: '+toolname+'.'+options)
		except IOError:
			print('\033[1;31m[-] IOError: Did you delete setting.txt file?\033[1;m')

def check(toollist,target):		
	try:
		with open('.setting.txt','r') as searchfile:
			for tool in toollist:
				for line in searchfile.readlines():
					toolname = re.search(tool, line)
					if toolname:
						tool=toolname.group()
						searchfile.seek(0)
						break
				for line in searchfile.readlines():
					if tool:
						toolpath=re.search('path: '+str(tool), line, re.M|re.I)
						if toolpath:
							pathline=line
							searchfile.seek(0)
							break
				for line in searchfile.readlines():
					if tool:
						toolcommand=re.search('command: '+str(tool), line, re.M|re.I)
						if toolcommand:
							commandline=line
							searchfile.seek(0)
							break
				if toolname and toolcommand and toolpath:
					tool=toolname.group()
					path=toolpath.group()
					command=toolcommand.group()
					path=re.sub('\n|'+path+'.','',pathline).lstrip()
					commandline=commandline.replace('target',target)
					command=re.sub('\n|'+command+'.','',commandline).lstrip()
					execute(path,command,tool)
	except IOError:
		print('\033[1;31m[-] IOError: while searching for tool in .setting.txt file\033[1;m')

def execute(pathname,command,tname):
	if pathname is not 'None' and command is not 'None':
		print('\n\t\t\t\t'+'\033[1;31m'+str(tname).upper()+'\033[1;m'+'\n')
		try:
			os.system('cd '+pathname+' && '+command)
		except:
			print('\033[1;31m[-] Please check your toolpath and command in .setting.txt file\033[1;m')
	else:
		print('\033[1;31m[-] Not able to run'+tname+'\033[1;m')
		print('\033[1;31m[-] please check pathname and command in .setting.txt file\033[1;m')

def delete(deltoollist):
	try:
		x=len(deltoollist)
		for deltool in deltoollist:
			with open('.setting.txt','r') as file:
				with open('new.txt','wb') as new:
					for line in file.readlines():
						deletetool=re.search(deltool, line)
						if not deletetool:
							new.write(line)
			os.remove('.setting.txt')
			os.rename('new.txt','.setting.txt')
			print('\033[1;31m[-] Deleted')
	except IOError:
		print('\033[1;31m[-] IOError: while deleting tool '+deltool+'\033[1;m')
		
def edit(edittoollist):
	try:
		with open('.setting.txt','r') as searchfile:
			for tool in edittoollist:
				toolname=False
				for line in searchfile.readlines():
					toolname = re.search(tool, line)
					if toolname:
						tool=toolname.group()
						searchfile.seek(0)
						break
				for line in searchfile.readlines():
					if tool:
						toolpath=re.search('path: '+str(tool), line, re.M|re.I)
						if toolpath:
							pathline=line
							toolpath=toolpath.group()
							toolpath=re.sub('\n|'+toolpath+'.','',pathline).lstrip()
							searchfile.seek(0)
							break
				for line in searchfile.readlines():
					if tool:
						toolcommand=re.search('command: '+str(tool), line, re.M|re.I)
						if toolcommand:
							commandline=line
							toolcommand=toolcommand.group()
							toolcommand=re.sub('\n|'+toolcommand+'.','',commandline).lstrip()
							searchfile.seek(0)
							break
				if toolname:
					too=[]
					too.append(tool)
					print('\033[1;33m[?] What you want to edit Path or command or both p/c/b\033[1;m'+'\033[1;40m')
					char=raw_input()
					if char == 'p' or char == 'P':
						print('\033[1;31m[-]'+toolpath.strip()+'\033[1;m')
						print('\033[1;36m[+] Enter new path\033[1;m'+'\033[1;40m')
						newp=raw_input()
						delete(too)
						Tool(tool,str(newp),toolcommand)
						print('\033[1;32m[+] Updated \033[1;m')
					elif char == 'c' or char == 'C':
						print('\033[1;31m[-]'+toolcommand.strip()+'\033[1;m')
						print('\033[1;36m[+] Enter new command\033[1;m'+'\033[1;40m')
						newc=raw_input()
						delete(too)
						Tool(tool,toolpath,str(newc))
						print('\033[1;32m[+] Updated \033[1;m')
					elif char == 'b' or char == 'B':
						print('\033[1;31m[-]'+toolpath.strip()+'\033[1;m')
						print('\033[1;36m[+] Enter new path\033[1;m'+'\033[1;40m')
						newp=raw_input()
						print('\033[1;31m[-]'+toolcommand.strip()+'\033[1;m')
						print('\033[1;36m[+] Enter new command\033[1;m'+'\033[1;40m')
						newc=raw_input()
						delete(too)
						Tool(tool,str(newp),str(newc))
						print('\033[1;32m[+] Updated \033[1;m')
					else:
						print('\033[1;31m[?] Enter any one p/c/b')
				else:
					print('\033[1;31m[-] Tool name not found\033[1;m')
	except IOError:
		print('\033[1;31m[-] IOError: while editing for tool in .setting.txt file\033[1;m')


def add(num):
	for i in range(0,num):
		print('\033[1;36m[+] Enter Tool Name of '+str(i+1)+' Tool\033[1;m'+'\033[1;40m')
		toolname=raw_input()
		print('\033[1;36m[+] Enter Tool path\033[1;m'+'\033[1;40m')
		toolpath=raw_input()
		print('\033[1;36m[+] How you want to execute\033[1;m'+'\033[1;40m')
		toolcommand=raw_input()
		Tool(toolname,toolpath,toolcommand)
	print('\033[1;32m[+] Added\033[1;m')

def listt():
	try:
		with open('.setting.txt','r') as searchfile:
			for line in searchfile.readlines():
				toolname=re.search('Tool: ', line, re.M|re.I)
				if toolname:
					tool=toolname.group()
					tool=re.sub('Tool: ','',line).strip()
					print('\033[1;36m'+str(tool)+'\033[1;m')
	except IOError:
		print('\033[1;31m[-] IOError: while listing\033[1;m')

if __name__ == "__main__":
	parse=argparse.ArgumentParser()
	parse.add_argument('-a','--add',type=int,help='Add new Tool(eg. python core.py -a Toolname)')
	parse.add_argument('-t','--target',help='your target website')
	parse.add_argument('-r','--run',nargs='*',type=str,help='Type the name of tools you want to run')
	parse.add_argument('-d','--delete',nargs='*',type=str,help='Delete your saved tool')
	parse.add_argument('-e','--edit',nargs='*',type=str,help='Edit your saved tool')
	parse.add_argument('--list', action='store_true',help='List of added tools')
	args=parse.parse_args()
	
	if args.add and (args.target or args.run):
		print('\033[1;31m[-] Either Run Tools or Add Tools\033[1;m')
	
	elif args.add:
		add(args.add)
	
	elif args.target and args.run:
		if args.run[0] is 'e' and len(args.run)==1:
			try:
				toollist=[]
				with open('.setting.txt','r') as searchfile:
					for line in searchfile.readlines():
						tool=re.search('Tool: ', line, re.M|re.I)
						if tool:
							tool=re.sub('\n|Tool: ','',line)
							toollist.append(tool.strip())
			except:
				print('\033[1;36m[-] \'check in elif args.target and args.run:\' loop\033[1;m')
			y=[str(item) for item in toollist]	
			check(y,args.target)
		else:
			y=[str(item) for item in args.run]
			check(y,args.target)
	
	elif args.delete:
		y=[str(item) for item in args.delete]
		delete(y)

	elif args.edit:
		y=[str(item) for item in args.edit]
		edit(y)
	elif args.list:
		listt()
	else:
		parse.print_help()
		sys.exit(0)
