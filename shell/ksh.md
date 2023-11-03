# Ksh

## Command-line arguments
| What | How | Details |
|---|---|---|
| Program name, including the path if started from another directory | `$0` | |
| Number of arguments | `$#` | |
| Check for zero arguments | <pre lang='ksh'>if [[ $# -eq 0 ]];then&#13;&#09;print "No Arguments"&#13;&#09;exit&#13;fi </pre> | |
| Get the $n$th argument | `$n` | |
| Get the $n$th argument, with default value | `${n-"Default value here"}` | |
| Expand all arguments to a single word | `$*` | |
| Expand all arguments to single string | `$@` | |
| Expand arguments to separate words | `"$@"` | |

## Special variables
Note that the positional parameters are special variables too.
| What | How | Details |
|---|---|---|
| Exit status of last command | `$?` | |
| Process id of current program | `$$` | |
| Process id of last background job | `$!` | |

## Constants
| What | How | Details |
|---|---|---|
| Declare constant | `declare -r PASSWD_FILE=/etc/passwd` | |

## Variables
Don't put dots in variable names!
By default, all variables are global! Even within functions!
| What | How | Details |
|---|---|---|
| Get variable value | `$var` | |
| Get variable value with default value _value_ | `${var:-value}` | |
| Get variable and set it with default value if it is not set | `${var:=value}` | |
| Get variable value but throw error if not set | `${var:?"Error! var not set!"}` | |
| Check if variable is set | `${var:+1}` | Returns 1 if set, else nothing |
| Set value for variable | `var=value` | |
| Set value from user input | `read var` | |
| Set command output for variable | <pre>var=`command args`</pre> | |
| Declare local variable | `typeset var` | |
| Set local variable | `typeset var = value` | |

## Functions
Use the local statement to define local variables.
| What | How | Details |
|---|---|---|
| Define function | <pre lang='ksh'>function foo {&#13;&#09;return $name&#13;}</pre> | |
| Define function with arguments | <pre lang='ksh'>function foo {&#13;&#09;typeset a = $1&#13;&#09;return $a&#13;}</pre> | |
| Call function | `foo` | |
| Call function with arguments | `foo arg1 arg2` | |

## Control flows
See http://www.bolthole.com/solaris/ksh-basics.html
| What | How | Details |
|---|---|---|
| Chain (pipe) commands | `command1 \| command2 \| command3` | |
| If | <pre lang='ksh'>if [[ $value -eq 7 ]];then&#13;&#09;print "$value is 7"&#13;fi</pre> | |
| If-else | <pre lang='ksh'>if [[ $value -eq 7 ]];then&#13;&#09;print "$value is 7"&#13;else&#13;&#09;print "$value is not 7"&#13;fi</pre> | |
| If-elseif | <pre lang='ksh'>if [[ $value -eq 7 ]];then&#13;&#09;print "$value is 7"&#13;elif [[ $value -eq 8 ]];then&#13;&#09;print "$value is not 7 but 8"&#13;else&#13;&#09;print "$value is neither 7 or 8"&#13;fi</pre> | |
| Switch | <pre lang='ksh'>case $var in&#13;&#09;john\|fred) print $invitation;;&#13;&#09;martin)  print $declination;;&#13;&#09;*)  print "Wrong name...";;&#13;esac</pre> | There is no "fall through" with ;;. You hit only one set of commands.. UNLESS you use ";&" instead of ";;'. You can use WILDCARDS to match strings.
| For | <pre lang='ksh'>for foo in $(ls);do&#13;&#09;print "\$count is $count"&#13;&#09;(( count -= 1 ))&#13;done | Use `continue` to skip the loop. Use `break` to exit the loop. |
| Until | | |
| Pause for $n$ seconds | `sleep n` |

### Error handling
| What | How | Details |
|---|---|---|
| Stop execution with unspecified error | `exit 1` | |
| Throw error with message | `echo "Error!" 1>&2`<br>`exit 2`
| Run command conditional on success of former | `command1 && command2` | |
| Run command only if first fails | `command1 \|\| command2` | |
| Run code on error | `trap "echo whoops" ERR` | |
| Run code on interupt | `trap "echo whoops" INT` | e.g., Ctrl+C |
| Run code on error or interrupt | `trap "echo whoops" ERR INT` | |
| Run code on process termination | `trap "echo whoops" TERM` | |
| Run cleanup function on error | `trap cleanup ERR` | For a previously defined `cleanup` function |

## Arithmetic
| What | How | Details |
|---|---|---|
| Increment variable | `(( a += 1))` | |
| Increment variable | `let a += 1` | |
| Sum variables | `sum = $(( a + b ))` | |

## Comparisons
| What | How | Details |
|---|---|---|
| And operator | `&&` |
| Or operator | `\|\|` |
| Equal string _str_ | `$var = "str"` | |
| Not equals string _str_ | `$var != "str"` | |
| Equals number _num_ | `$var -eq num` | |
| Not equals number _num_ | `$var -ne num` | |
| Greater than number _num_ | `$var -gt num` | |
| Less than number _num_ | `$bar -lt num` | |

## Strings
| What | How | Details |
|---|---|---|
| Length | `"${#var}"` | |
| Get filename from path | `${name##*/}` | |
| Get parent path | `${name%/*}` | |

## Output

### Standard
| What | How | Details |
|---|---|---|
| Print message | `echo "Hello world!"` | |
| Print variable | `echo $var` | |
| Formatted printing | `printf "counting %d days" $days` | |

### Data redirection
| What | How | Details |
|---|---|---|
| Write to new file or overwrite file | `command > file` | |
| Append file | `command >> file` | |
| Redirect error output | `command 2> file` | |
| Redirect to normal output | `command 2>&1` | |
| Discard errors | `command 2>/dev/null` | |
| Discard all output | `command > /dev/null 2>&1` | |
| File as input to command | `command < file` | |

## File handling
| What | How | Details |
|---|---|---|
| Check if directory exists | `[ -d "$DIRPATH" ]` | |
| Check if directory is missing | `[ ! -d "$DIRPATH" ]` | |
| Check if file exists | `[ -f "$FILEPATH" ]` | |
| Create directory | `mkdir "$DIRPATH"` | |
| Count the number of files in a directory | <pre lang='ksh'>count=`find $dir -maxdepth 1 -name "*.txt" -type f \| wc -l`</pre> | |

## Notes
* Start script with: `#!/bin/ksh`
* Enable executation for file by running `chmod u+x script.sh`
