# GDB pretty printers for the JUCE Library

Include this file in `~/.gdbinit`:

    python
    import sys 
    sys.path.insert(0, '/path/to/juce_pretty_printing')
    import gdb_juce
    end
