from Front import VSQLite,QApplication
import sys,os



if __name__ == '__main__':
	argv = sys.argv
	app  = QApplication(argv)
	os.chdir(argv[0].strip("VSQLite.py"))
	
	if len(argv) > 1:
		if os.path.exists(argv[1]):
			prog = VSQLite(argv[1])
		else:
			pass
	else:
		prog = VSQLite()

	prog.show()
	app.exec()