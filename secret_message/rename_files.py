import os

def rename_files():
	save_path = "C:/Users/HODOR/Desktop/rename_files_new"
	file_list = os.listdir(save_path)
	print(file_list)

	os.chdir(save_path) 
	for file_name in file_list:
		print("Renaming file: "+file_name+" in Directory: "+save_path)
		os.rename(file_name,file_name.translate(None,"1234567890"))

rename_files()
