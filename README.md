Kathleen Cravotta - January 2017  
https://github.com/katcravo/u_d3_js

## Summary 
The voyage of the Titanic ended in tragedy and over 1500 people died. The graph is based on a sample of 714 passengers for which passenger information including
age was available, out of a total of approximately 1,317 passengers, excluding crew. It illustrates the number of passengers that perished within each demographic.

## Design

### Initial Graph
My first design decision was to use a side-by-side graph.  
    * This graph lets us see the differences in the number of victims and survivors in each demographic  
    * It clearly indicate the difference in victims and the difference in survivors separately, by letting them both have a lined up axis.
	
The graph has count rather than ratios to give each passenger equal space on the page and bluntly indicate the number of survivors and victims.  Not statistics or ratios.

The graph excludes data for which there was no age information, because I thought it would clutter the visualization with additional categories that had less meaning.

Third class passengers were sorted on top because that is where the highest death rates were.  I sorted the passengers within each class by Man, Woman and Child, since that order is familiar in speech lingo, and also puts the highest number of victims on the top, and illustrates a cyclical pattern in the data.  

Color was used to differentiate Man, Woman and Child passengers, while spacing was used to separate each passenger class.  The color was consistent between survivors and victims, but a lighter shade for survivors, letting emphasis be on the larger and darker bars for victims.

The same scale was used for both the left side and the right side, since they are representing the same units and are related.


### Second Iteration
1. Remove most verbiage from top of page, and instead use footnote #1 to describe the limitations of the data.  
    * This allows the graph to be absorbed first without a paragraph of text detracting from it.  
    * Since my original page appended the svg to the bottom, I had to place a tag inside the html body in between the top text and the footnote.
2. Use the word 'Fatalities' in place of 'Victims', so that it conveys death more clearly.
3. Change the headings for Fatalities and Survivors to include the totals for those categories.
4. Explain Child category with footnote #2.


### Third Iteration
1. Refine wording - use the word 'Victims' in title.  Include the words 'passenger class' in the description, to provide context for 1st class, etc.
2. Include checkbox for sorting by Man, Woman Child rather than Pclass.


## Feedback
### Initial Graph

Respondent A:  
1. Concerned about a biased data set (preventing objectivity).  
    * This was the most honest and important feedback because it showed me that the 'helpful' intro text detracted from the graph.  
    * Change 1 - diminish verbiage about limited data set  
2. Main thing is that more women were saved regardless of cabin class. That's consistent with people taking care of women and kids in chaotic situations in general.  

Respondent B:  
1. Why is the survivors section grayed out?  
    * Keep - emphasis on victims  
2. Is victim the right word?  
    * Change 2 - use 'fatality'  
3. Immediately notice the graph is split by victims and survivors.  
4. Main thing is that lower class was most impacted from the tragedy.  

Respondent C:  
1. Noticed Men from third class had the most fatalities, and it diminishes as class goes up.  
2. Would like to see the total for victims and survivors, and total per class  
    *Change 3- include totals in headings  

### Second Graph

Respondent D:  
1. First saw that mostly men died, more than women, and that a lot of children died which was awful.  
2. Main thing third class no matter who were mostly casualties.  It gave us a look on how people in classes were viewed.  Especially women and children.  I thought they valued all women and children but looking at the graph they only viewed class.  

Respondent E:  
1. First thing to notice is that men from third class had the most fatalities.  
2. What is 1st class, etc?  Why titled Fatalities when there are survivors, too?  
    * Change 1 - Refine Wording  
   
Respondent C:  
1. First thing noticed is that many men died  
2. Main thing was that more people from third class died.  


## Resources 
* Code is modified from Kaijie Zhou: https://gist.github.com/kaijiezhou/bac86244017c850034fe
* Udacity Titanic data set: https://www.udacity.com/api/nodes/5420148578/supplemental_media/titanic-datacsv/download
* colors: http://stackoverflow.com/questions/21208031/how-to-customize-the-color-scale-in-a-d3-line-chart
* sorting: http://stackoverflow.com/questions/32846062/custom-keys-sorting-in-rolled-data-d3-js
* RMS Titanic: http://en.wikipedia.org/wiki/RMS_Titanic
* resorting: http://bl.ocks.org/mbostock/3885705