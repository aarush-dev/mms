from base.functions import functions as fn

# making function easily available
get_runs = fn.get_runs_upto
print(get_runs)
input()
def run():
	try:
		fn.firstThingsFirst()
		from base.menu import main_menu
	except SystemExit:
		pass
	except KeyboardInterrupt:
		exit()
	except:

		print('\nError Found, please view error log file located at: \'' +  fn.makeErrorLog() + '\'')
		exit()

if fn.configs.__DEBUG__:
	run()