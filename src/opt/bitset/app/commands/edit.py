def edit_command(*args):
    if len(args) == 0:
        print("No arguments given")
        return
    if args[0] != "edit":
        print("First argument must be 'edit'")
        return
    
    for i in range(2):
        opt = filter.setting