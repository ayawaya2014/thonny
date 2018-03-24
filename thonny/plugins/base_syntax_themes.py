from thonny.globals import get_workbench

def default_light():
    light_fg = "DarkGray"
    string_fg = "DarkGreen"
    open_string_bg = "#c3f9d3"
    
    return {
        "TEXT"          : {"foreground" : "black", "insertbackground" : "black"},
        "definition"    : {"foreground" : "black", "font" : "BoldEditorFont"},
        "string"        : {"foreground" : string_fg},
        "string3"       : {"foreground" : string_fg},
        "open_string"   : {"foreground" : string_fg, "background" : open_string_bg},
        "open_string3"  : {"foreground" : string_fg, "background" : open_string_bg},
        "keyword"       : {"foreground" : "#7f0055", "font" : "BoldEditorFont"},
        "builtin"       : {"foreground" : "black"},
        "number"        : {"foreground" : "#B04600"},
        "comment"       : {"foreground" : light_fg},
        
        "prompt"        : {"foreground" : "purple", "font" : "BoldEditorFont"},
        "magic"         : {"foreground" : light_fg},
        "stdin"         : {"foreground" : "Blue"},
        "stdout"        : {"foreground" : "Black"},
        "stderr"        : {"foreground" : "Red"},
        "value"         : {"foreground" : "DarkBlue"},
        "hyperlink"     : {"foreground" : "#3A66DD", "underline" : True},
        
        # paren matcher
        "surrounding_parens"  : {"foreground" : "Blue", "font" : "BoldEditorFont"},
        "unclosed_expression"  : {"background" : "LightGray"},
        
        # find/replace
        "found" : {"foreground" : "blue", "underline" : True},
        "current_found" : {"foreground" : "white", "background" : "red"},
        
    }

def default_dark():
    default_fg = "#B3B3B3" 
    string_fg = "#8DC76F"
    open_string_bg = "#453B22"
    
    #s.configure("Local.Code", foreground="#BCCAE8")
    #s.configure("MatchedName.Code", background="#193022")
    
    return {
        "TEXT"          : {"foreground" : default_fg, "insertbackground" : default_fg},
        #"sel"           : {"foreground" : ""},
        "definition"    : {"foreground" : default_fg},
        "string"        : {"foreground" : string_fg},
        "string3"       : {"foreground" : string_fg},
        "open_string"   : {"foreground" : string_fg, "background" : open_string_bg},
        "open_string3"  : {"foreground" : string_fg, "background" : open_string_bg},
        "builtin"       : {"foreground" : default_fg},
        "keyword"       : {"foreground" : "#9A79AD", "font" : "BoldEditorFont"},
        "number"        : {"foreground" : "#FFCABF"},
        "comment"       : {"foreground" : "#C8DEE6"},
        
        # shell
        "prompt"        : {"foreground" : "#5BEBBB", "font" : "BoldEditorFont"},
        "magic"         : {"foreground" : "pink"},
        "stdin"         : {"foreground" : "LightBlue"},
        "stdout"        : {"foreground" : "LightGray"},
        "stderr"        : {"foreground" : "#EB5B83"},
        "value"         : {"foreground" : "#EBEB5B"},
        "hyperlink"     : {"foreground" : "#DC5BEB", "underline" : True},
        
        # paren matcher
        "surrounding_parens"  : {"foreground" : "#F0995B", "font" : "BoldEditorFont"},
        "unclosed_expression"  : {"background" : "#193022"},
        
    }

def load_early_plugin():
    get_workbench().add_syntax_theme("Default Light", None, default_light)
    get_workbench().add_syntax_theme("Default Dark", None, default_dark)
    get_workbench().set_default("view.syntax_theme", "Default Light")
    