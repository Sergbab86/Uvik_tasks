import argparse
from datetime import date
import os


current_date = date.today()


class Items(object):

    PATH = os.getcwd()
    list_file = fr"{PATH}/todo.txt"
    done_file = fr"{PATH}/done.txt"

    def __init__(self):
        self.items = open(self.list_file, "r").readlines()

    def addItem(self, arg):
        print("Added item: " + arg)
        with open(self.list_file, "a+") as f:
            f.writelines(arg + "\n")

    def listItems(self):
        print("\n        TODO\n" + "-" * 75)

        if not self.items:
            print("No tasks to be done.\n")
        else:
            for sno, item in enumerate(self.items, start=1):
                print(str(sno) + ". " + item)

    def removeItem(self, arg):

        try:
            done_task = self.items.pop(arg - 1)

            print("Completed task no. " +
                  str(arg) +
                  " (%s), deleted todo" % done_task.strip()
                  )
            print(f"Deleted item:{arg}")

            with open(self.list_file, "w") as f:
                for item in self.items:
                    f.writelines(item)
        except Exception as e:
            print(f"Error: todo {arg} does not exist. Nothing deleted.")

    def markDone(self, arg):

        try:

            g = self.items[arg - 1]
            print(f"Marked task №{arg} as done")

            with open(self.done_file, 'a') as f:
                f.write(f"x {current_date} {g} ")
            done_task = self.items.pop(arg - 1)

            with open(self.list_file, "w") as f:
                for item in self.items:
                    f.writelines(item)
        except Exception as e:
            print(f"Error: todo {arg} does not exist.")

    def stat(self):
        with open(self.done_file, "r") as f:
            counter = -1
            content = f.read()
            content_list = content.split("\n")
            for i in content_list:
                if i:
                    counter += 1

        print(f"{current_date}: you've completed {counter} tasks!")


if __name__ == "__main__":

    parser = argparse.ArgumentParser()

    parser.add_argument(
        "-add",
        type=str,
        help=" # add new item in todo list"
    )

    parser.add_argument(
        "-stat",
        action="store_true",
        help="# shows statistic"
    )

    parser.add_argument(
        "-list",
        action="store_true",
        help="        # list all todo items"
    )

    parser.add_argument(
        "-remove",
        type=int,
        help="    # remove a todo"
    )

    parser.add_argument(
        "-done",
        type=int,
        help="    # mark an item as done"
    )

    args = parser.parse_args()

    items = Items()

    if not (args.add or args.list or args.remove or args.stat or args.done):
        items.listItems()

    elif args.add:
        # print("calling items.listAdd")
        items.addItem(args.add)

    elif args.list:
        items.listItems()

    elif args.remove:
        items.removeItem(args.remove)

    elif args.done:
        items.markDone(args.done)

    elif args.stat:
        items.stat()
