class HtmlContainer:

    def __init__(self):
        self.top_bar_string = ''
        self.header_string = ''
        self.meal_picker_string = ''
        self.results_string = ''
        self.history_string = ''
        self.value_assigner_string = ''
        self.bottom_bar_string = ''

    def header(self):
        if not self.header_string:
            self.header_string = '<!DOCTYPE html><html lang="en">'
            with open('html/header.html') as file:
                for line in file:
                    self.header_string += line
            self.header_string += '<body>'
        return self.header_string

    def top_bar(self):
        if not self.top_bar_string:
            with open('html/top_bar.html') as file:
                for line in file:
                    self.top_bar_string += line
        return self.top_bar_string

    def meal_picker(self):
        if not self.meal_picker_string:
            with open('html/meal_picker.html') as file:
                for line in file:
                    self.meal_picker_string += line
        return self.meal_picker_string

    def results(self):
        if not self.results_string:
            with open('html/results.html') as file:
                for line in file:
                    self.results_string += line
        return self.results_string

    def history(self):
        if not self.history_string:
            with open('html/history.html') as file:
                for line in file:
                    self.history_string += line
        return self.history_string

    def value_assigner(self):
        if not self.value_assigner_string:
            with open('html/value_assigner.html') as file:
                for line in file:
                    self.value_assigner_string += line
        return self.value_assigner_string

    def bottom_bar(self):
        if not self.bottom_bar_string:
            with open('html/bottom_bar.html') as file:
                for line in file:
                    self.bottom_bar_string += line
            self.bottom_bar_string += '</bodyhtml>'
        return self.bottom_bar_string
