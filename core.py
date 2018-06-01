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
			print('IOError: Did you delete setting.txt file?')

def check(toollist,target):		
	try:
		with open('.setting.txt','r') as searchfile:
			for tool in toollist:
				for line in searchfile.readlines():
					toolname = re.search(tool, line)
					if toolname:
						searchfile.seek(0)
						break
				for line in searchfile.readlines():
					tool=toolname.group()
					if tool:
						toolpath=re.search('path: '+str(tool), line, re.M|re.I)
						if toolpath:
							pathline=line
							searchfile.seek(0)
							break
				for line in searchfile.readlines():
					tool=toolname.group()
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
		print('IOError:Something happened in .setting.txt file')

def execute(pathname,command,tname):
	if pathname is not 'None' and command is not 'None':
		print('\n\t\t\t\t'+'\033[1;31m'+str(tname).upper()+'\033[1;m'+'\n')
		try:
			os.system('cd '+pathname+' && '+command)
		except:
			print('Please check your toolpath and command in .setting.txt file')
	else:
		print('Not able to run'+tname)
		print('please check pathname and command in .setting.txt file')
		
if __name__ == "__main__":
	parse=argparse.ArgumentParser()
	parse.add_argument('-a','--add',type=int,help='Add new Tool(eg. python core.py -a Toolname)')
	parse.add_argument('-t','--target',help='your target website')
	parse.add_argument('-r','--run',nargs='*',type=str,help='Type the name of tools you want to run')
	args=parse.parse_args()

	if args.add and (args.target or args.run):
		print('\033[1;31mEither Run Tools or Add Tools\033[1;m')
	elif args.add :
		num=args.add
		for i in range(0,num):
			print('\033[1;36m[+] Enter Tool Name of '+str(i+1)+' Tool\033[1;m')
			toolname=raw_input()
			print('\033[1;36m[+] Enter Tool path\033[1;m')
			toolpath=raw_input()
			print('\033[1;36m[+] How you want to execute\033[1;m')
			options=raw_input()
			Tool(toolname,toolpath,options)
	elif args.target and args.run:
		if args.run[0] is 'e':
			
			try:
				toollist=[]
				with open('.setting.txt','r') as searchfile:
					for line in searchfile.readlines():
						tool=re.search('Tool: ', line, re.M|re.I)
						if tool:
							tool=re.sub('\n|Tool: ','',line)
							toollist.append(tool.strip())
			except:
				print('Soryy boss')
			y=[str(item) for item in toollist]	
			check(y,args.target)
		else:
			y=[str(item) for item in args.run]
			check(y,args.target)
	else:
		parse.print_help()
		sys.exit(0)

		




		



