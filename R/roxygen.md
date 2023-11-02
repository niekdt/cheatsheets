# Basic
| What | How | Details |
|---|---|---|
| Title | `@title Title here` | |
| Description | `@description Description here` | |
| Parameter | `@param data The dataset` | |
| Dot parameters | `@param ... Additional arguments` | |
| Return | `@return Return value description here` | |
| Class slot | `@slot slotName Description here` | |
| Details | `@details Details here` | |
| Note | `@note Notes here` | |
| Data format | `@format Format description here` | |

# Formatting
| What | How | Details |
|---|---|---|
| Enable markdown | `@md` | |
| Emphasis | `_wow_` | |
| Bold | `*wow*` | |
| In-line equation | `\eqn{a + b}` | |
| Display equation | `\deqn{a + b}` | |
| Code | `` `mu <- mean(data)` `` | |
| Code | `\code{mu <- mean(data)}` | |
| Code block | <pre>\```&#13;mu <- mean(data)&#13;```</pre> | |
| Monospace font (looks like code) | <pre>\preformatted{&#13;&#09;text&#13;}</pre> | | 
| Package name | `\pkg{stats}` | |
| Unordered list | <pre>\itemize{&#13;&#09;\item Option A&#13;&#09;\item Option B&#13;}</pre> | |
| Ordered list | <pre>\enumerate{&#13;&#09;\item First item&#13;&#09;\item Second item&#13;}</pre> | |
| Named list | <pre>\describe{&#13;&#09;\item{Opt A}{Describe option A}&#13;&#09;\item{Opt B}{Describe option B}&#13;}</pre> | |
| Tables | ? | |
| Sections | <pre>@details First part&#13;@details Second part (will be a new section)</pre> | |
| Arbitrary sections | <pre>@section Title:&#13;Text here </pre> | |
| Subsections | <pre>@details&#13;## This is a subsection &#13;With text &#13;#### Subsubsection here&#13;With text</pre> | |

# Linking
| What | How | Details |
|---|---|---|
| Website | `<https://r-project.org>` | |
| With different text | `[text](link)` | |
| To internal topic with `@name` _name_ | `[name]` | |
| To external package topic | `[stats][stats-package]` | |
| To external package topic | `[stats::predict]` | |
| To internal or global function | `[predict()]` | |
| To external function | `[stats::predict()]` | |
| To function with different text | ``[`fancyName()`][stats::predict()]`` | |
| To class | ``[`Time`]`` | |
| To external class | ``[`stats::Time`]`` | |
| To S4 class | `\linkS4class{lcModel}` | |
| With special characters | `\code{\link[magrittr]{\%>\%}}` | |
| See-also | `@seealso [mean] [stats::median]` | |
| See-also vignette | ``@seealso `browseVignettes("roxygen2")` `` | |
| Family | `@family sharedNames` | |
| Specify source | `@source This dataset was generated using [generateData]` | |
| References | `@references`<br>`\insertRef{benaglia2009mixtools}{latrend}` | |
| E-mail | `\email{example@@example.com}` | |

# Code examples
| What | How | Details |
|---|---|---|
| Examples | <pre>@examples&#13;1 + 1&#13;mean(1:9)</pre> | |
| Examples that should not be run | <pre>@examples&#13;1 + 1&#13;\dontrun{&#13;&#09;stop('oops')&#13;}</pre> | |
| Examples that should not be tested | <pre>@examples&#13;\donttest{&#13;&#09;stop('oops')&#13;}</pre> | |
| Interactive example only | <pre>@examples&#13;if interactive()&#13;&#09;browseURL("https://roxygen2.r-lib.org")</pre>

# Function/class import/export and loading
| What | How | Details |
|---|---|---|
| Import package | `@import stats` | |
| Import packages | `@import stats splines` | |
| Import function(s) from package | `@importFrom stats predict fitted` | |
| Import S3 generic | `@importFrom pkg generic` | |
| Import S4 classes from package | `@importClassesFrom stats Time` | |
| Import S4 methods from package | `@importMethodsFrom stats time time2` | |
| Collate / ensure other R files are loaded first | `@include first.R second.R` | |
| Export function | `@export` | |
| Export class and methods | `@export`<br>`setClass(…)` | |
| Export class | `@exportClass lcModel` | |
| Export class method | `@exportMethod evaluate` | |

# Docs
| What | How | Details |
|---|---|---|
| Don't generate topic | `@noRd` | |
| Create stand-alone topic | `@name docname`<br>`@title Topic title`<br>`NULL` | |
| Package topic | `@details`<br>`Package documentation here.`<br>`@keywords internal`<br>`"_PACKAGE"` | |
| Topic name | `@name simpleName` | |
| Topic file name | `@rdname simpleName` | |
| Specify doc inclusion order | `@order 1` | Then `@order 2` for the second doc |
| Define alias | `@aliases shortName` | |
| Define alias for S4 method | `@aliases predictForCluster,lcModel-method` | |
| Inherit doc | `@inherit docName` | |
| Inherit doc components | `@inherit docName details return` | |
| Inherit section | `@inheritSection docName Section title` | |
| Inherit param descriptions from another internal function | `@inheritParams internalFun` | |
| Inherit param descriptions from an external function | `@inheritParams stats::predict` | |
| Inherit dot parameters | `@inheritDotParams` | |
| Hide documentation | `@keywords internal` | |

# Figures 
| What | How | Details |
|---|---|---|
| Add figure | `![](example-plot.jpg "Example Plot Title")` | |


# Dynamic content
| What | How | Details |
|---|---|---|
| In-line code evaluation | `` `r getRversion()` `` | Evaluated during every roxygenize call |
| Code block evaluation | <pre>\```{r}&#13;&#13;```</pre> | Code blocks cannot refer to each other |
| Generate figure | <pre>\```{r iris-pairs-plot}&#13;&#09;pairs(iris[1:4])[unclass(iris$Species)])&#13;```</pre> | |
| Dynamic documentation | ![image](https://github.com/niekdt/cheatsheets/assets/8193083/e8cd9182-e05b-4f48-a9a1-ff5edf34dcba) | |


# IDE shortcuts
| What | How | Keys |
|---|---|---|
| Generate docs | `roxygen2::roxygenise()` | Ctrl+D |
| Clean files, then generate docs | `roxygen2::roxygenise(clean = TRUE)` | |

