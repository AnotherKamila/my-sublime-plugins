import sublime, sublime_plugin
import os

class eopenCommand(sublime_plugin.WindowCommand):
	"""
	opens a file relative to the current directory
	created to resemble vim's :e , since I hate Gtk's file chooser dialog
	"""
	def run(self):
		pwd = os.path.dirname(self.window.active_view().file_name())
		self.window.show_input_panel('('+pwd+') :e', '', self.on_done, None, None)

	def on_done(self, text):
		self.window.open_file(text)
