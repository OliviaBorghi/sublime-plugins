import sublime
import sublime_plugin
import subprocess

class RunPurgeCommand(sublime_plugin.WindowCommand):
    def run(self):   #open a user input panel
        self.window.show_input_panel(
            "Enter purge args (e.g. m c j):",  #prompt to user
            "",    #default argument
            self.on_done,   #what is called when user hits enter
            None,
            None
        )

    def on_done(self, input_string):    
        batch_path = r"C:\scripts\purge.bat"  #where is the batch script?
        args = input_string.strip().split() #cleaning user input

        # Map of short args to friendly names
        cache_names = {
            "m": "muc cache",
            "c": "courses cache",
            "t": "theme cache",
            "j": "JS cache",
            "f": "filter cache",
            "o": "other cache",
            "l": "lang string cache"
        }

        # Get friendly names for the provided args
        named = [cache_names.get(arg.lower(), f"[unknown: {arg}]") for arg in args]

        try:    #let's try to run the batch with user args
            result = subprocess.run(
                [batch_path] + args,
                shell=True,
                capture_output=True,
                text=True
            )

            if result.returncode == 0: #success!
                if named:
                    purged = ", ".join(named)
                else:
                    purged = "all caches"
                sublime.message_dialog(f"✅ Purge successful.\nPurged: {purged}")
            else:   #failure :(
                sublime.error_message(f"❌ Purge failed.\n\n{result.stderr}")
        except Exception as e: #exception
            sublime.error_message(f"🚨 Error running purge.bat:\n{e}")
