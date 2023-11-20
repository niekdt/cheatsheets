---
layout: default
title: Rmarkdown
parent: R
nav_order: 100
---

# Rmarkdown
{: .no_toc}

1. TOC
{:toc}

## Title page

| What | How | Details |
|---|---|---|
| Title | `title: my title` | |
| Author | `author: Sint Nicolaas` | |
| Author with e-mail as footnote | `author: Sint Nicolaas^[example@example.com]` | |
| Authors | `author:`<br>` - Bert`<br>` - Ernie` | |
| Date | `date: 2023-11-03` | |
| Current date | `` date: "`r format(Sys.time(), '%d %B %Y')`" `` | |
| Keywords | `tags: [longitudinal, sleep]` | |

## Format

| What | How | Details |
|---|---|---|
| Bold | `**text**` | |
| Italic | `*text*` | |
| Hyperlink | `[Text](url)` | |
| Code | `code` | |
| Equation | `$\mu$` | |

## Structures

### Sections / paragraphs

| What | How | Details |
|---|---|---|
| Section | `# Section title` | |
| Subsection | `## Subsection title` | |
| Subsubsection | `### Subsubsection title` | |
| Paragraph | `#### Paragraph title` | |
| Unnumbered section |`# Section title {-}` | |
| Hide section from ToC | `# Section title {.toc-ignore}` | |
| Tabbed section | `## title {.tabset .tabset-fade}`<br>`content above tabbed region.`<br><br>`### tab 1 `<br>`tab content 1`<br><br>`### tab 2`<br>`tab content 2`<br><br>`##`<br>`content below tabbed region` | [Source](https://stackoverflow.com/questions/38062706/rmarkdown-how-to-end-tabbed-content). The newlines are crucial! |
| Collapsible paragraph | <pre lang='html'>\<details>`<br>`\<summary>Show details…\</summary>`<br>`\<p>Derp\</p>`<br>`\</details> ` | |
| Horizontal line | `***` | |

### Lists

| What | How | Details |
|---|---|---|
| Define list | `* a`<br>`* b` | |
| Define nested list | `* a`<br>`  + b`<br>`* c` |
| Dynamic list from code section | `\`\``{r, results='asis'}`<br>`paste0('* ', items, collapse='\n') %>% cat`<br>`\`\``` | |

### Figures

| What | How | Details |
|---|---|---|
| Figure | `{r, fig.align="center", fig.width=6, fig.height=6, fig.cap="Figure: Here is a really important caption."}` | [Source](https://holtzy.github.io/Pimp-my-rmd/) |
| Subfigures | `\`\``{r out.width=c('50%', '50%'), fig.show='hold'}`<br>`boxplot(1:10)`<br>`plot(rnorm(10))`\``` | [Source](https://holtzy.github.io/Pimp-my-rmd/) ` | 
| Interactive ggplot | `p = ggplot(data, aes(x=x, y=y, color=z)) + geom_point()`<br>`plotly::ggplotly(p)` | |

### Tables

| What | How | Details |
|---|---|---|
| Table | `kable(df)` | |
| Dynamic sortable table | `DT::datatable(…)` | |
| Scrollable table | `DT::datatable(mtcars, rownames = FALSE, filter="top", options = list(pageLength = 5, scrollX=T) )` | |
| Named list as table | `` `r unlist(mylist) %>% as.data.frame %>% kable(col.names='Value')` `` | |
| Knitr params list as table | `` `r unlist(params) %>% as.data.frame %>% kable(col.names='Value', caption='Parameters')` `` | |

## Code block arguments
To hide code blocks by default, set `code_folding: "hide"` in the output document parameters.

| What | How | Details |
|---|---|---|
| Run, show output only | `echo=F` | |
| Run, show code only | `echo=T, results='hide'` | |
| Show code, don't run | `eval=F` | |
| Interpret output as markdown code | `results='asis'` | |
| Hide messages | `message=F` | |
| Hide warnings | `warning=F` | |




