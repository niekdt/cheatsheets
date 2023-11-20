---
layout: default
title: Roxygen2
parent: R
nav_order: 100
---

# Roxygen2
{: .no_toc}

1. TOC
{:toc}

## Basic

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

## Format

| What | How | Details |
|---|---|---|
| Enable markdown | `@md` | |
| Emphasis | `_wow_` | |
| Bold | `*wow*` | |
| In-line equation | `\eqn{a + b}` | |
| Display equation | `\deqn{a + b}` | |
| Code | `` `mu <- mean(data)` `` | |
| Code | `\code{mu <- mean(data)}` | |
| Code block | `\````<br>`mu <- mean(data)`<br>`\```` | |
| Monospace font (looks like code) | `\preformatted{`<br>`    text`<br>`}` | | 
| Package name | `\pkg{stats}` | |
| Unordered list | `\itemize{`<br>`    \item Option A`<br>`    \item Option B`<br>`}` | |
| Ordered list | `\enumerate{`<br>`    \item First item`<br>`    \item Second item`<br>`}` | |
| Named list | `\describe{`<br>`    \item{Opt A}{Describe option A}`<br>`    \item{Opt B}{Describe option B}`<br>`}` | |
| Tables | ? | |
| Sections | `@details First part`<br>`@details Second part (will be a new section)` | |
| Arbitrary sections | `@section Title:`<br>`Text here ` | |
| Subsections | `@details`<br>`## This is a subsection `<br>`With text `<br>`#### Subsubsection here`<br>`With text` | |

## Link

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

## Code examples

| What | How | Details |
|---|---|---|
| Examples | `@examples`<br>`1 + 1`<br>`mean(1:9)` | |
| Examples that should not be run | `@examples`<br>`1 + 1`<br>`\dontrun{`<br>`    stop('oops')`<br>`}` | |
| Examples that should not be tested | `@examples`<br>`\donttest{`<br>`    stop('oops')`<br>`}` | |
| Interactive example only | `@examples`<br>`if interactive()`<br>`    browseURL("https://roxygen2.r-lib.org")`

## Function/class import/export and loading

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

## Docs

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

## Figures 

| What | How | Details |
|---|---|---|
| Add figure | `![](example-plot.jpg "Example Plot Title")` | |


## Dynamic content

| What | How | Details |
|---|---|---|
| In-line code evaluation | `` `r getRversion()` `` | Evaluated during every roxygenize call |
| Code block evaluation | `\```{r}`<br>``<br>````` | Code blocks cannot refer to each other |
| Generate figure | `\```{r iris-pairs-plot}`<br>`    pairs(iris[1:4])[unclass(iris$Species)])`<br>````` | |
| Dynamic documentation | ![image](https://github.com/niekdt/cheatsheets/assets/8193083/e8cd9182-e05b-4f48-a9a1-ff5edf34dcba) | |


## IDE shortcuts

| What | How | Keys |
|---|---|---|
| Generate docs | `roxygen2::roxygenise()` | Ctrl+Shift+D |
| Clean files, then generate docs | `roxygen2::roxygenise(clean = TRUE)` | |

