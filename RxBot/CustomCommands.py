from Settings import *
from Initialize import *




commands_CustomCommands = {
    "!chat": ('MOD', 'customcmds.chat', 'cmdArguments', 'user'),
    "!ccexamplemod": ('MOD', 'customcmds.modexample', 'cmdArguments', 'user'),
}

class resources:
    def __init__(self):
        pass


class CustomCommands:
    def __init__(self):
        self.write("0")
        self.chatters = []
        self.usersToIgnore = settings["USERS TO IGNORE"].replace(" ", "").split()
        print(self.usersToIgnore)

    def chatMsg(self, user):
        if user not in self.chatters:
            if user not in self.usersToIgnore:
                self.chatters.append(user)
                self.write(1 + self.read())


    def read(self):
        with open("activeChatters.txt", "r") as f:
            output = f.read()
            f.close()
        return int(output)

    def write(self, number):
        with open("activeChatters.txt", "w") as f:
            f.write(str(number))
            f.close()

    def chat(self, args, user):
        cmd = args.split()[0].strip()
        args = args.replace(args.split()[0].strip(), "").strip()

        if cmd.lower() == "set":
            return self.chatset(args)
        if cmd.lower() == "add":
            return self.chatadd(args)
        if cmd.lower() == "subtract":
            return self.chatsubtract(args)
        if cmd.lower() == "reset":
            return self.chatreset()

    def chatset(self, args):
        try:
            self.write(int(args))
        except ValueError:
            return "Please provide a number"
        return "Set the value to %s" % args

    def chatadd(self, args):
        try:
            self.write(int(args) + self.read())
        except ValueError:
            return "Please provide a number"
        return "Added %s to chatters" % args

    def chatsubtract(self, args):
        try:
            self.write(self.read() - int(args))
        except ValueError:
            return "Please provide a number"
        return "Subtracted %s from chatters" % args

    def chatreset(self):
        self.write(0)
        self.chatters = []
        return "Reset chatters"


customcmds = CustomCommands()
resources = resources()