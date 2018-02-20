import tkFileDialog
import filter
import diff


def Main():
	print """\nPlease choose an option in below that you want...
	1. Convolve an image with Gaussian Filter with given sigma value
	2. Take the difference between two convolved images with different sigma values
	3. Exit
	"""
	chosen = int(raw_input('>>> '))
	applyTheDecision(chosen)


def applyTheDecision(decision):
	if decision is 1:
		return gaussian_filtering()
	elif decision is 2:
		return compare_images()
	elif decision is 3:
		return exit()
	else:
		print """\nPlease choose a valid option in the menu...
		1. Return main menu
		2. Exit
		"""
		chosen = int(raw_input('>>> '))
		return subMenu(chosen)

def subMenu(decision):
	if decision is 1:
		return Main()
	elif decision is 2:
		return exit()

def setSigmaValue():
	try:
		print "Enter the sigma value: "
		return int(raw_input('>>>'))
	except ValueError:
		print "Not a number"
		return setSigmaValue()

def gaussian_filtering():
	filter.main(setSigmaValue())

def compare_images():
	diff.main()


if __name__ == '__main__':
    Main()