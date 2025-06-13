import sublime
import sublime_plugin
import subprocess

class RunPurgeCommand(sublime_plugin.WindowCommand):
    def run(self):
        # Show input panel to enter arguments like "m c t"
        self.window.show_input_panel(
            "Enter purge args (e.g. m c j):",  # Prompt
            "",                                # Default value
            self.on_done,                      # Callback on submit
            None,                              # On change (unused)
            None                               # On cancel (unused)
        )

    def on_done(self, input_string):
        batch_path = r"C:\scripts\purge.bat"  # Update to your actual path
        args = input_string.strip().split()

        try:
            subprocess.Popen([batch_path] + args, shell=True)
            sublime.status_message("Running purge.bat with args: " + " ".join(args))
        except Exception as e:
            sublime.error_message(f"Failed to run purge.bat: {e}")
