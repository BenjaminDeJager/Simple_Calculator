# simple calculator todo:
1. Setting up the window:

   1. Figure out (again) how to open up a kivy window with an arbitrary number of buttons, presumably in a row. 
   _(I already have a template for a window with *a* button)._
   2. Create github repo and push. 
   (explicitly adding this item as I forget to do this alot and end up with a commit-mess after too much stuff happens).

DONE
2. Setting up buttons

   1. Make a input-button "class" that displays an initialization string as a parameter 
   so I can create 0-9 and "." button's generically. 

DONE
   <br>_(this will functionality be identical to Kivy's Button class at this point and won't do anything)_</p>
   2. Give the input-buttons a generic "press" function that simply displays the string 
to confirm the buttons work. (kivy should have a "click" function irrc)

DONE

3. Setting up input memory and display
   1. Add a "Memory" list to the window that the buttons can "push" to as a queue that flushes the oldest object when full.</p>
   2. Add a "Display" Text object as a field of the "memory" object. Display each element in ascending order (akin to Texas instrument calculators).

DONE, Memory is a class that extends Deque's and holds str objects that get passed by the buttons when pressed.
Label gets passed in from CalculatorApp (changed later).

4. adding some type of computational function
   1. Add a "+" button such that it pushes the sum of the newest 2 elements in memory, to the memory queue.</p>

Now meets minimum requirements of a virtual calculator (by my definition).

DONE, changed Memory to initalize it's label inside itself. 
removed "." button for now as it cannot be converted by adderbutton

5. extending functionality to something approaching useful
    1. add a "current_value" field to a "Input" text item beneath Display, as a empty string by default, 
that the buttons push to by appending their value to it instead of Display and then make "=" push this to memory.

Now can input values larger than 9.

6. bonus functionality
    1. Try to expand "+" to a "operator" button class which pulls from memory, then pushs to memory the results of applying a initalized lambda function on the memory nondestructively.
    2. Use this to create subtraction, multiplication and integer division.
    3. Add input validation.