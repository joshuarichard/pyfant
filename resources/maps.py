Maps = {
    0: [
        [None,         "Path", None,      "BanditLoot", None,   None,   None,   None,   None,         None,         None],
        [None,         "Path", None,      "Path",       None,   None,   None,   "Path", "Path",       "BanditLoot", "Path"],
        [None,         "Path", None,      "Path",       None,   None,   None,   "Path", None,         None,         "Path"],
        ["BanditLoot", "Path", "Path",    "Path",       "Path", "Path", "Path", "Path", "Path",       None,         "Path"],
        [None,         None,   "Path",    None,         None,   "Path", None,   None,   "Path",       "Path",       "Path"],
        [None,         None,   "Start",   None,         None,   "Path", None,   None,   "Path",       None,         None],
        [None,         None,   "Enemies", None,         None,   "Path", None,   None,   "Path",       None,         None],
        [None,         None,   "Path",    "Path",       "Path", "Path", "Path", None,   "Path",       "Path",       "BanditLoot"],
        [None,         None,   "Path",    None,         None,   "Path", None,   None,   "Path",       None,         None],
        ["Path",       "Path", "Path",    None,         None,   "Path", "Path", "Path", "BanditLoot", None,         None]
    ]
}

# every row needs to be the same length otherwise could run into problems with World.canGo()
