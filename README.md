<img src="Github assets//LOGO.png" style="width:20%;display:block;margin-left:auto;margin-right:auto;"></img>
<p></p>
Version 0: The virtually nothing version

<h2> INTRODUCTION + OVERVIEW: </h2>
The Fyle Project aims to create an accessible, free, open-source all-in-one 
conversion software interface. Fyle- the main program- does not contain any 
conversion itself, but rather acts as a middleman, providing an easier and 
more efficient way to run and provide arguments to standalone external programs.

Fyle not only provides an interface easier to use than hand-typing console 
commands, but also offers easy batch conversion to convert multiple programs
at one time, or over a period of time.
It can also (theoretically) work with any other program! The only prerequisites 
being that said external program accepts command line arguments, would otherwise 
run on your computer, and has a .FYLE configuration linked to it (more 
information below).

<h2>!!!		DISCLAIMERS	    !!!</h3>
PLEASE KEEP IN MIND THAT FYLE IS ESSENTIALLY A COMMAND-LINE EXECUTOR. THERE IS 
NOTHING IN PLACE ENSURING THAT THE EXTERNAL PROGRAMS IT RUNS ARE NOT MALICIOUS.
FOR YOUR SAFETY, IT IS HIGHLY ADVISED TO ONLY RUN PROGRAMS THAT YOU HAVE BUILT 
FROM THE SOURCE CODE, OR ARE FROM TRUSTWORTHY PARTIES.

FYLE is not responsible for any loss or damage to property due to malicious
external programs, or third party mods of the base program.

FYLE DOES NOT CHECK IF A PROCESS WILL OVERWRITE EXISTING FILES. TO PREVENT 
UNWANTED FILE LOSS MAKE SURE YOU SELECT EMPTY FOLDERS WHEN PROMPTED TO 
CHOOSE AN OUTPUT DIRECTORY.

<h2> USING FYLE </h2>
Upon running FYLE, the program will provide a list of programs that you can use,
with a number beside each one. To prepare a conversion process, simply type the
number next to the desired program.
At this point, you may also type 'Quit' to terminate FYLE.

Once a program has been selected, you will be presented with 3 'Process Type'
options:
S - SINGLE: Converts a single file.

B - BATCH: Converts all files found in the select folder. If this option is selected,
all prompts that would have typically asked for a file directory will instead ask for
a folder directory. FYLE will then ask the external program to convert all the files
in the selected folder.
If the select folder contains files not compatible with the external process, FYLE will

C - CHIPPER: Once set up, FYLE will actively check the import folder for files. Upon
detecting files in the folder, it will convert them into the export folder and move the
original file to a discard folder. The Chipper will run until the user stops it in the
FYLE console. The Chipper can be used for easily converting files you don't have yet
(i.e., still downloading/rendering) in one session.


From there, FYLE will prompt you for the arguments the process needs. This will mostly
either involve file explorer popups asking for a file/folder directory, or the console
requesting a string input.

Once all the prompts have been entered, the conversion process will begin. Once complete,
a "Process Complete" notice will appear, and you'll return to the Process selection menu.
NOTE: FYLE will display the "Process Complete" even if the external program crashes/doesn't
run. 

<h2> SETTING UP A PROGRAM TO USE WITH FYLE </h2>
In order to set up an external program to work with Fyle, two things are needed:
    1. The program must be under the Programs directory, or any of its children 
    (FYLE/Programs/Program goes here)
    2. An accompanying .FYLE file must also be in under the Programs directory 
    (strictly, cannot be in children directories)

A .FYLE file is used to tell Fyle what arguments the external program needs to 
run, such as import directories and export folders.
The options after line 3 are all optional- they are what 
arguments will be sent to Fyle. These options must be in the order that the 
program will take the arguments (keep in mind, the programs directory will 
always be the first argument) and take up one line each, with no separating 
lines.


They are set up in this way:
~~~
Program name
Program directory, relative to the Programs directory (e.g. Fyle/IMG CONV/Image Convertor.exe)
"~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
I : file (for import use only)
I <dialogue text>

F : folder
F <dialogue text>

S : string
S <dialogue text>

N : integer*
N [minimum (whole number)] [maximum (whole number)] <dialogue text>

D : dropdown
D [y/n (support custom options)] <dialogue text> {option1} {option2} {option3} {etc} 

C : checkbox
C [y/n (default option)] <dialogue text>
~~~

For example:
~~~
FYLE Example Software
FYLE\\EG\\Example.py
"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
I <Files in>
F <Export location>
D y <Image type to convert to> {png} {jpg} {gif} {tiff} {ico} {webp} {avif}
C n <Overwrite existing files?>
S <Export file name>
N 0 99 <Wait time between conversions>
~~~

The first letter represents the function- how the user will be presented these 
arguments and how Fyle will handle them.
<dialogue text> marks text that will be displayed to the user when asking for 
each argument. These should summarise what the user need to enter and it's 
purpose.
{option} marks options a user can select from, or that are recommended.
[] marks single character arguments, THESE ARE NO ACTUALLY SURROUNDED WITH []

Certain options in the .FYLE configuration may appear to be unnecessary, such 
as having a default option for a checkbox that technically doesn't exist.
Be aware that Fyle is an active project, and later iterations plan to add a 
proper GUI. Incorrect configuration on your part may make your program appear 
broken in the future. FYLE WILL ALWAYS SUPPORT OLD .FYLE CONFIGURATIONS AS LONG 
AS THEY HAVE BEEN SET UP CORRECTLY.

Note: all arguments will be sent to external program as strings. Using the N
option in the FYLE configuration just makes sure the string can be converted into
an integer without causing problems.


<h2> FUTURE PLANS </h2>
Features planned for future releases:
* Automation: preconfigure processes and run instantly
* Debug mode: print relevant variables and debug info in the console
* Threading: convert multiple files at the same time
* De-hardcoding variables and placing them in editable .txt files

* Proper GUI: official-looking interface with a window and buttons and everything!
* GUI themes: customise the Proper GUI when it comes out

* Branching options: provide different prompts based on user selection.
* Float: prompt use to enter a decimal float
