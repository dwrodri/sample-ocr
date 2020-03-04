# Parsing Google Vision output
### Notes on Regular expressions
Honestly the documentation for pythons `re` library seems quite good, they have
really good explanations of all the modifiers. Some good practice examples for
getting regex down well are:
1. FirstName LastName (Easy)
2. Phone numbers (Medium)
3. Valid Dates (Harder)
3. Email addresses ([Insanity](https://www.regular-expressions.info/email.html))

Original command used in demo to search for units.
```
grep -Ein --color=always "(cup)|(tbsp)|(tsp)"
```

## Notes
* User draws bounding box around sections in photo, and data science has to do a
  lot less work. However, more work from user.
* User takes multiple photos, one for each section?
* Use pixels that are **not** in bounding boxes for clues. Proper context analysis
  from non-text will make or break you. How big is Space? \n? \t?
* Related to above: Are there any geometric dividers? Traditional computer
  vision approaches may work really well here (OpenCV shape detection). 
* Inevitably OCR can and will fail, need to make sure you make it easy for user
  to correct output (mostly front-end job).
* You're going to want a database of 5-10+ samples for testing rule-based stuff,
  and like AT LEAST a couple hundred if you want to 
* Naive bayes classifier might work really well for fixing typos.

## Extracting ingredients list
* Vision is bad at fractions, look for `*` and `%` next to units 
* Because of above, best regex queries for ingredients are units of measurement (tbsp,
  tsp,cup,oz,lb,bottle,proof).
