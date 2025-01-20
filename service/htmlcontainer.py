class HtmlContainer:

    def __init__(self):
        self.top_bar_string = ''
        self.header_string = ''
        self.meal_picker_string = ''
        self.results_string = ''
        self.history_string = ''
        self.assigner_string = ''
        self.bottom_bar_string = ''

    def header(self):
        if not self.header_string:
            self.header_string = '<!DOCTYPE html><html lang="en">'
            self.header_string += self.filereader('html/header.html')
            self.header_string += '<body>'
        return self.header_string

    def top_bar(self):
        if not self.top_bar_string:
            self.top_bar_string = '<div id="replace_content">'
            self.top_bar_string += self.filereader('html/top_bar.html')
        return self.top_bar_string

    def meal_picker(self):
        if not self.meal_picker_string:
            self.meal_picker_string = self.filereader('html/meal_picker.html')
        return self.meal_picker_string

    def results(self):
        if not self.results_string:
            self.results_string = self.filereader('html/results.html')
        return self.results_string

    def history(self):
        if not self.history_string:
            self.history_string = self.filereader('html/history.html')
        return self.history_string

    def assigner(self):
        if not self.assigner_string:
            self.assigner_string = self.filereader('html/assigner.html')
        return self.assigner_string

    def bottom_bar(self):
        if not self.bottom_bar_string:
            self.bottom_bar_string = self.filereader('html/bottom_bar.html')
            self.bottom_bar_string += '</div></body></html>'
        return self.bottom_bar_string

    @staticmethod
    def filereader(filename):
        returnstring = ''
        with open(filename, 'r') as file:
            for line in file:
                returnstring += line
        return returnstring
