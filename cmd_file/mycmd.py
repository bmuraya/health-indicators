import cmd


class MyCmd(cmd.Cmd):
    intro = "Welcome to the custom command interpreter. Type 'help' or '?' to list commands.\n"
    prompt = "(mycmd) "

    def do_hello(self, args):
        """Prints a greeting."""
        print("Hello,", args)

    def do_quit(self, args):
        """Exit the interpreter."""
        print("Goodbye!")
        return True  # Returning True exits the command loop


if __name__ == "__main__":
    MyCmd().cmdloop()
