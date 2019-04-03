# CLI Interfaces and `docopt`

## CLI
(C)ommand (L)ine (I)nterfaces are programs run at the command line. We've used a few CLI tools this semester. Docker, for example, is used at the command line. There are commands you use hundreds of times a day, like `ls` or `cd`. These are individual programs used from the command line.

### Using a CLI
Commands start with the name of the program, then can take *arguments*. These arguments depend on the program, which should tell you the arguments it requires. There are also *flags*, which are usually one letter and come after a dash (`-`) character. These usually trigger very common behavior, and are one letter to keep the program compact and easy to use. If a flag is more than one letter, it usually follows two dashes (`--`).

Lets look at one of the most basic CLI programs, `ls`. To use `ls`, you begin the command with the name of the program, `ls`. Then you provide arguments to the program. In the case of `ls`, these arguments are optional. You can run
```
$ ls
```
and it will return the contents of the current directory. You could also run
```
$ ls some/dir/
```
and it will return the contents of the directory you provided. You could also use a flag like this
```
$ ls -l
```
The `-l` part means to list the items in a vertical list instead of horizontal lines. Let's add another flag
```
$ ls -la
```
This will run `ls` with the `-l` flag we saw above, but also the `-a` flag, which includes hidden items.

*Note: `ls` works on unix systems. On windows, the command is `dir`. You can experiment with `dir`, or use the git bash program that you probably installed with git. It will give you access to `ls` and other unix commands. But generally, arguments and flags and everything should work the same way on windows.*

You may remember some flags to frequently used programs, but it's impossible to remember every argument and flag. This is where help pages come in.

### Help pages
Every good CLI has a help page. Usually it's invoked with the `-h` or `--help` flag, or sometimes just running the command with no arguments. There is no standard requirement for the format of a help page, but there are some common practices that most people follow for consistency. Let's look at the help page for `cp`, a command that copies files.

```
$ cp
usage: cp [-R [-H | -L | -P]] [-fi | -n] [-apvXc] source_file target_file
       cp [-R [-H | -L | -P]] [-fi | -n] [-apvXc] source_file ... target_directory
```

There's quite a few options there, but it's easy to parse through once you know what you're looking at. Anything within brackets (`[]`) is optional. Usually any arguments are in angle brackets (`<>`), but here they're bare. If we remove the optional flags, we see the only required arguments are a `source_file` and a `target_file`. Now we know we can run
```
$ cp some_file.txt some_other_file.txt
```
and it will copy the contents from `some_file.txt` to `some_other_file.txt`. On the second line of the help page, we see `source_file ... target_directory`. We can take an educated guess and assume that we can provide multiple files to copy separated by a space, then an output directory as the last argument, and it will copy all files into that directory.

If we look at the optional flags, we see that the first one is `-R` (capitalization matters). It takes an optional flag after that as well. The vertical pipes (`|`) mean an option, so after a `-R` flag, we could provide `-H`, `-L`, `-P`, or nothing (remember, it's in brackets, so it's optional too).

If something has multiple options but is required, it would be in angle brackets (`<>`). As an example, if you need *either* the `-f` flag *or* the `-g` flag, you could write
```
fake_command < -g | -f >
```

Or we could write the same thing, saying we want either the `-f` flag, *or* the `-g` flag, *or* nothing.
```
fake_command [ -g | -f ]
```

Most new help pages also provide a description of what each command does, especially if it's a very large command. Older commands, especially ones that are a core part of unix, don't have a help page built in but can be accessed by `man` (short for "manual"). run `man ls` to see the manual page for ls. Newer (and bigger) commands have help pages built in. Run `docker --help` and see what's there.


## Docopt
Help pages are important because that's how you create a CLI using [docopt](https://github.com/docopt/docopt). If you didn't read the [help pages](#help-pages) section above, go read it.

There are dozens of CLI packages for python alone. Most are cumbersome and hard to work with, but docopt approaches CLIs from the other directory. With docopt, instead of writing a bunch of code for a CLI, you write a help page using the standards I detailed above and it generates a CLI for you.

I've provided a working example of a CLI in `cli.py`, take a look. Docopt will generate a dictionary for you, which makes your logic pretty easy. Here's the [docopt Github](https://github.com/docopt/docopt) and [website](http://docopt.org/), which has all the documentation you may need. There's also a video on the website that may be helpful.

You may choose to rewrite your application with docopt, and build in all the logic to the CLI. You may also want to have your CLI make web requests to your API from earlier in this project. Making web requests may be a little bit more complicated, but it could save you work, as you won't have to rewrite the logic from the api. But moving the logic to the CLI will make it more portable and less error prone. It's up to you.

DM me on slack with any questions. I know this is just a very brief introduction, but the best way to learn a tool is to build something with it. Fake it 'til you make it.
