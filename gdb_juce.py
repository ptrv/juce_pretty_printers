import gdb

class JuceStringPrinter:
    "Print a juce::String of some kind"

    def __init__(self, val):
        self.val = val

    def to_string(self):
        return self.val['text']['data']

class JuceFilePrinter:
    "Print a juce::File of some kind"

    def __init__(self, val):
        self.val = val

    def to_string(self):
        return self.val['fullPath']['text']['data']

def lookup_function(val):
    type_to_printer = {
            'juce::String': JuceStringPrinter,
            'const juce::String': JuceStringPrinter,
            'juce::File': JuceFilePrinter,
            'const juce::File': JuceFilePrinter,
            }

    printer = type_to_printer.get(str(val.type), None)
    if printer:
        return printer(val)
    return None

gdb.pretty_printers.append(lookup_function)
