## setup, leave as is
library('tidyverse')
library('data.table')
library("plyr")
ASL.Lex <- read_csv('ASL.Lex2.0.clean.csv')
SB <- read_csv("All Countries - clean.csv")

SB <- SB %>% mutate(LexicalClass = LexcialClass)

#For handshape, there are 91 possible values for SB. Other values are changed to NA
SB <- SB %>% filter(Handshape<91)

#Remove any straggler NAs.
SB <- SB %>% drop_na()

#Combine both databases into one.
combined_df <- merge(ASL.Lex, SB, all = TRUE)

#Change NonDom handshape --- to NAs
combined_df$NonDominantHandshape <- revalue(combined_df$NonDominantHandshape, c('---' = NA))

#For TISLR abstract
SB$NonDominantHandshape <- revalue(SB$NonDominantHandshape, c('---' = NA))
## setup, leave as is


# Find frequency of each handshape for each langauge [add code below this]


# Find frequency of each handshape across languages (controlling for different sample sizes across langauges) [add code below this]