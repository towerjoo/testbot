import traceback
import main_module


if __name__ == "__main__":
	num_total = 1
	num_passed = 0
	errors = []
	main_module.env = 'development'

	try:
		main_module.main_handler({'data': {'env': 'testing'}, 'user': {'client_key': 'zrf', 'client_secret': 'yum'}})
		num_passed += 1
	except Exception as e:
		errors.append((e, traceback.format_exc()))

	print "\n" + str(num_passed) + " of " + str(num_total) + " tests passed."

	if len(errors):
		print "\nERRORS:\n"
		print errors