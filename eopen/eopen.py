import sublime, sublime_plugin

class eopenCommand(sublime_plugin.WindowCommand):
	"""
	opens a file relative to the current directory
	created to resemble vim's :e , since I hate Gtk's file chooser dialog
	"""
	def run(self):
		self.window.show_input_panel(':e ', '', self.on_done, None, None)
		pass

	def on_done(self, text):
		self.window.open_file(text)
