import tkinter

window = tkinter.Tk() # Create a window
window.title("My First GUI Program") # Set the title of the window
window.minsize(width=500, height=300) # Set the minimum size of the window
# Label
my_label = tkinter.Label(text="I am a Label", font=("Arial", 24)) # Create a label
my_label.pack(expand=True) # Add the label to the window




window.mainloop()