## Chatting Chickens: Craig Chen, Faiza Huda, Vivian Graeber, Raven (Ruiwen) Tang
## SoftDev
## K13 -- Stuylin' & Wylin' & Profilin' / mimicking HTML file using CSS rules
## 2022-10-18
## time spent: 1.0 hrs

# DISCO
* $firefox path/to/file/file_name.html will render the HTML page in Firefox
* comment in CSS: bookended by /* COMMENT CONTENT */
* Visual Studio Code doesn't like empty CSS rulesets. No errors will be thrown, but it indicates a problem if there are empty CSS rulesets.
* By default, h1, h2, h3, and p tags show up from top to bottom, with new lines between them.
* This extension (https://eyedropper.org/) offers the ability to find the hex/RGB codes of colors on the websites you visit (click on part of the screen and see the code of the corresponding color), save palettes in history, and pick colors.
* Setting background of h1 first, then body, will not override the background color of h1. Changing a CSS property value of an element that contains a child element will not change the property of that child. In this way, CSS properties are not inherited by elements that nest within others.
* Text is black by default. CSS accepts hex codes and also words (for common colors).
* Classes are helpful for styling specific groups of elements. For example, we have multiple h3 elements, but we only want them to have different font colors. We can use classes to apply different CSS property values, but the h3 property values will still be applied to all of them.
* Changing background colors of elements shows us if they extend across the entire page. For example, h1 text may only show on the leftmost side of the screen, but if we add a background color to the element, we can see that the element takes up the entire width of the browser.
* Divs can be nested inside of each other, and again, changing the background color helps identify where these end/start/how much of the page they take up.
* The column-count property organizes the content of a div into the number of columns specified, with equal width devoted to each.

# QCC
* On Brave Browser, the Pirate Ipsum generator did not generate anything unless shields were turned off (indicated that 2 trackers/ads/more were blocked). Why does the generator require certain trackers, or what protections under Brave Shields blocked the generator from working properly? 
* If we apply a font-size to all of body, text becomes larger than its default size. However, h1 is still the largest, and doesn't display with the same size as p elements. It seems that CSS rules override HTML default styles for specific elements, but they don't necessarily overcome the default hierarchy?
* How can we easily identify the font and mimic it? 
* How do we create columns of different sizes? column-count works with column-width, but these properties create uniformly sized columns. Here, negative margin allowed the right column to be moved past its left border, but is there a better, more robust way to create a smaller left column?

# CREDIT FOR LOREM IPSUM GENERATOR
* https://pirateipsum.me/
