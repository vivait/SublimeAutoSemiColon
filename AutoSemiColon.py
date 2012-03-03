import sublime_plugin
import sublime


class AutoSemiColonCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        # End the edit it passes
        #del edit
        self.view.end_edit(edit)

        # Insert the semi colon
        edit_init = self.view.begin_edit('insert')
        try:
            # Loop through and add the semi colon
            for sel in self.view.sel():
                # The last letter we've dealt with
                first = sel.end()
                self.view.insert(edit_init, first, ';')
        finally:
            self.view.end_edit(edit_init)

        # Create a new edit point
        edit_last = self.view.begin_edit('auto_semi_colon')
        try:
            # Loop through and add move it to the end
            for sel in self.view.sel():
                last = first = sel.end()
                # Find the last bracket
                while (self.view.substr(last) in [' ', ')']):
                    last += 1
                # Can we insert the semi colon elsewhere?
                if last > first:
                    self.view.erase(edit_last, sublime.Region(first - 1, first))
                    # Delete the old semi colon
                    self.view.insert(edit_last, last - 1, ';')
                    # Move the cursor
                    self.view.sel().clear()
                    self.view.sel().add(sublime.Region(last, last))
        finally:
            self.view.end_edit(edit_last)
