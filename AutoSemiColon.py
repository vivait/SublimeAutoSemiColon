import sublime_plugin
import sublime


class AutoSemiColonCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        # Loop through and add the semi colon
        for sel in self.view.sel():
            # The last letter we've dealt with
            first = sel.end()
            self.view.insert(edit, first, ';')

        # Loop through and add move it to the end
        for sel in self.view.sel():
            last = last_bracket = first = sel.end()
            # Find the last bracket
            while (self.view.substr(last) in [' ', ')', ']']):
                if (self.view.substr(last) != ' '):
                    last_bracket = last + 1
                last += 1

            if (last_bracket < last):
                last = last_bracket

            # Can we insert the semi colon elsewhere?
            if last > first:
                self.view.erase(edit, sublime.Region(first - 1, first))
                # Delete the old semi colon
                self.view.insert(edit, last - 1, ';')
                # Move the cursor
                self.view.sel().clear()
                self.view.sel().add(sublime.Region(last, last))
