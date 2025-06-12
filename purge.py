import sublime
import sublime_plugin
import subprocess
import os


class RunPurgeCommand(sublime_plugin.WindowCommand):
	def run(self):
		batch_path = r"C:\scripts\purge.bat"

		args = ["t"] #let's make this dynamic

		try:
			subprocess.Popen([batch_path] + args, shell=True)
			sublime.status_message("Running purge.bat with args " + " ".join(args))
		except Exception as e:
			sublime.error_message(f"Failed to run purge: {e}")

