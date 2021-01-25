import json
from typing import NamedTuple, List
from rich.console import Console
from loguru import logger
# we need a global console to control highlighting / printing
console = Console(highlighter=False)


class Prettifier:
    """
    This classes entire existence is to output stuff.
    """
    def __init__(self, kwargs, api=False):
        """
        Takes arguments as list so we can do A11Y stuff etc
        """
        if api is not True:
            self.a11y = kwargs["accessible"]

    def greppable_output(self, objs: List):
        logger.trace("Greppable output")
        logger.trace(objs)
        """
        takes the prototypes and turns it into json
        returns the json

        Doesn't print it, it prints in main
        """
        outputs_as_dict = {}
        for i in objs:
            logger.trace(i)
            outputs_as_dict.update(i.hash_obj)
        logger.info("Returning from greppable output.")
        return json.dumps(outputs_as_dict, indent=2)

    def pretty_print(self, objs):
        logger.trace("In pretty printing")
        """
        prints it prettily in the format:
        most popular hashe
        1.
        2.
        3.
        4.


        then everything else on one line.
        """
        multi_print = True if len(objs) > 1 else False
        for i in objs:
            logger.trace(i)
            self.pretty_print_one(i, multi_print)

    def pretty_print_one(self, objs: List, multi_print: bool):
        out = f"\n[bold #011627 on #ff9f1c]{objs.chash}[/bold #011627 on #ff9f1c]\n"

        # It didn't find any hahses.
        if len(objs.prototypes) == 0:
            out += "[bold #2ec4b6]No hashes found.[/bold #2ec4b6]"
            console.print(out)
            return out

        out += "\n[bold underline #2ec4b6]Most Likely[/bold underline #2ec4b6] \n"
        start = objs.prototypes[0:4]
        rest = objs.prototypes[4:]

        for i in start:
            out += self.turn_named_tuple_pretty_print(i) + "\n"
        
        # It has hashes, but not many so don't print least likely.
        if len(objs.prototypes) <= 5:
            console.print(out)
            return out

        # return if accessible is on
        if not self.a11y:
            out += "\n[bold underline #2ec4b6]Least Likely[/bold underline #2ec4b6]\n"

            for i in rest:
                out += self.turn_named_tuple_pretty_print(i) + " "

        console.print(out)
        return out

    def turn_named_tuple_pretty_print(self, nt: NamedTuple):
        # This colours red
        out = f"[bold #e71d36]{nt['name']}[/bold #e71d36], "

        hc = nt["hashcat"]
        john = nt["john"]
        des = nt["description"]

        if hc is not None and john:
            out += f"Hashcat Mode: {hc}, "
        elif hc is not None:
            out += f"Hashcat Mode: {hc}."
        if john is not None and des:
            out += f"John Name: {john}, "
        elif john is not None:
            out += f"John Name: {john}."
        if des:
            # Orange
            out += f"[#ff9f1c]Summary: {des}[/#ff9f1c]"

        return out
