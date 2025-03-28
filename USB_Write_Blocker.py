import winreg

class WriteBlocker(object):

	def __init__(self):
		self.subKey = r"SYSTEM\CurrentControlSet\Control\StorageDevicePolicies"
		self.key =  winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, self.subKey, 0, winreg.KEY_ALL_ACCESS)		

	def __set_value(self, value):
		winreg.SetValueEx(self.key, "WriteProtect", 0, 4, value)

	def is_blocked(self):
		return winreg.QueryValueEx(self.key, "WriteProtect")[0] == 1

	def block(self):
		self.__set_value(1)

	def unblock(self):
		self.__set_value(0)

	def test(self):
		if winreg.QueryValueEx(self.key, "WriteProtect")[0] == 0:
			print("USB Write Blocker is Off")
			var = ""
			while var != "y" and var !='n':
				var = input("Turn On? [y] [n]")
				if var == 'y':
					self.block()
				else:
					print("USB Write Blocked unchanged!!!")
					
		if winreg.QueryValueEx(self.key, "WriteProtect")[0] == 1:
			print("USB Write Blocker is On")
			var = ""
			while var != "y" and var !='n':
				var = input("Turn Off? [y] [n]")
				if var == 'y':
					self.unblock()
				else:
					print("USB Write Blocked unchanged!!!")

if __name__ == "__main__":
	reg = WriteBlocker()
	# reg.test()

	from tkinter import *
	from PIL import ImageTk, Image
	import os


	class App(object):
		def __init__(self):
			self.usb = WriteBlocker()
			self.master=Tk()
			self.master.title("")
			icon = os.getcwd() + os.sep + "tray.ico"
			self.master.iconbitmap(icon)  # window icon
			self.master.resizable(width=FALSE, height=FALSE)
			self.master.geometry("180x82")

			btn_txt = ""
			
			if self.usb.is_blocked:
				btn_txt = "Block"
			else:
				btn_txt = "Unblock"
			bg = "gray25"
			bg1 = "royal blue"
			button_bg = "forest green"
			fc = "white smoke"
			font = ("Helvetica", "8", "bold")
			text = " ----------- Boris & Vladimir Software ------------- "

			# Frame to suport butons, labels and separators ----------------
			self.f = Frame(self.master, bg=bg)
			self.f.pack_propagate(0)  # don't shrink
			self.f.pack(side=BOTTOM, padx=0, pady=0)

			# Message ------------------------------------------------------
			self.l1 = Message(
				self.f, bg=bg1, bd=5, fg=bg, text="USB Write Blocker",
				font=("Helvetica", "10", "bold italic"), width=500).grid(
				row=0, columnspan=6, sticky=EW, padx=5, pady=5)

			self.l6 = Label(
				self.f, text=text, font=("Helvetica", "6", "bold"), bg=bg, fg=bg1
				).grid(row=4, column=0, columnspan=3, sticky=EW, pady=1)

			# Buttons ------------------------------------------------------
			self.b0 = Button(
				self.f, text=btn_txt, command=self.__callback, width=10,
				bg=button_bg, fg=fc, font=font
				)#.grid(row=3, column=0, padx=5, sticky=W)
			self.b0.grid(row=3, column=0, padx=5, sticky=W)
			#self.b0.pack()
			self.b1 = Button(
				self.f, text="Sair", command=self.__callback_2, width=10,
				bg="Orange red", fg=fc, font=font
				).grid(row=3, column=1, padx=5, sticky=W)
			
			# Minloop ------------------------------------------------------
			self.master.mainloop()


		def __callback(self):
			if self.usb.is_blocked():
				#self.message.set("Unblock")

				self.b0.config(text="Block")
				self.usb.unblock()
			else:
				self.b0.config(text="Unblock")
				self.usb.block()
            

		def __callback_2(self):
			self.master.destroy()


	#root = Tk()
	#app = App(root)
	#root.mainloop()
	App()






# def block(key, value):
# 	winreg.SetValueEx(key, "WriteProtect", 0, 4, value)


# def readRegLocalMachine(subKey):
# 	key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, subKey, 0, winreg.KEY_ALL_ACCESS)

# 	if winreg.QueryValueEx(key, "WriteProtect")[0] == 0:
# 		print("USB Write Blocked is Off")
# 		var = ""
# 		while var != "y" and var !='n':
# 			var = input("Turn On? [y] [n]")
# 			if var == 'y':
# 				block(key, 1)
# 			else:
# 				print("USB Write Blocked unchanged!!!")
				
# 	if winreg.QueryValueEx(key, "WriteProtect")[0] == 1:
# 		print("USB Write Blocker is On")
# 		var = ""
# 		while var != "y" and var !='n':
# 			var = input("Turn Off? [y] [n]")
# 			if var == 'y':
# 				block(key, 0)
# 			else:
# 				print("USB Write Blocked unchanged!!!")

# if __name__ == "__main__":
# 	subKey = r"SYSTEM\CurrentControlSet\Control\StorageDevicePolicies"
# 	readRegLocalMachine(subKey)
