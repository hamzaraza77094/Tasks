import tkinter as tk
import matplotlib.pyplot as plt
import numpy as np

HEIGHT = 600
WIDTH = 600

root = tk.Tk()

# Count
root.counter_green = 0
root.counter_red = 0
def green_count():
    root.counter_green += 1
    # print('Green Counter: ', root.counter_green)
def red_count():
    root.counter_red += 1
    # print('Red Counter: ', root.counter_red)
# graph
def Finish():
    complete = root.counter_green
    uncomplete = root.counter_red
    total = complete + uncomplete
    productivity = (complete / total) * 100
    unproductivity = (uncomplete / total) * 100
    total_tasks = 'The total tasks are: ', total
    count_complete = ('The amount of completed tasks: ', complete)
    count_uncomplete = ('The amount of uncompleted tasks: ', uncomplete)
    product_rate = ('The productivity rate is: ', round(productivity, 3), '%')
    unproduct_rate = ('The unproductivity rate is: ', round(unproductivity, 3), '%')
    y_plot = [0,10,20,30,40,50,60,70,80,90,100]
    plt.bar(1, productivity, color='g', width=.5, edgecolor='black')
    plt.bar(1,unproductivity, bottom=productivity, color='r', width=.5, edgecolor='black')
    plt.ylabel('Percentage')
    plt.xlabel('Productivity')
    plt.title('Productivity Graph')
    plt.yticks(np.arange(0, 101, 5))
    plt.legend(labels=['"%" of task complete', '"%" of tasks incomplete'])
    plt.annotate(xy=(.76,15), text=(count_complete))
    plt.annotate(xy=(.76,10), text=product_rate)
    plt.annotate(xy=(.76,80),  text=count_uncomplete)
    plt.annotate(xy=(.76,75), text=unproduct_rate)
    plt.show()


# Done function
def done1():
    complete_label = tk.Label(lower_frame, bg='white', text='Locked', font='Arial')
    complete_label.place(relx=.015, rely=.1, relwidth=.08, relheight=.05)
def done2():
    complete_label = tk.Label(lower_frame, bg='white', text='Locked', font='Arial')
    complete_label.place(relx=.015, rely=.16, relwidth=.08, relheight=.05)
def done3():
    complete_label = tk.Label(lower_frame, bg='white', text='Locked', font='Arial')
    complete_label.place(relx=.015, rely=.22, relwidth=.08, relheight=.05)
def done4():
    complete_label = tk.Label(lower_frame, bg='white', text='Locked', font='Arial')
    complete_label.place(relx=.015, rely=.28, relwidth=.08, relheight=.05)
def done5():
    complete_label = tk.Label(lower_frame, bg='white', text='Locked', font='Arial')
    complete_label.place(relx=.015, rely=.34, relwidth=.08, relheight=.05)
def done6():
    complete_label = tk.Label(lower_frame, bg='white', text='Locked', font='Arial')
    complete_label.place(relx=.015, rely=.4, relwidth=.08, relheight=.05)
def done7():
    complete_label = tk.Label(lower_frame, bg='white', text='Locked', font='Arial')
    complete_label.place(relx=.015, rely=.46, relwidth=.08, relheight=.05)
def done8():
    complete_label = tk.Label(lower_frame, bg='white', text='Locked', font='Arial')
    complete_label.place(relx=.015, rely=.52, relwidth=.08, relheight=.05)
def done9():
    complete_label = tk.Label(lower_frame, bg='white', text='Locked', font='Arial')
    complete_label.place(relx=.015, rely=.58, relwidth=.08, relheight=.05)
def done10():
    complete_label = tk.Label(lower_frame, bg='white', text='Locked', font='Arial')
    complete_label.place(relx=.015, rely=.64, relwidth=.08, relheight=.05)
def done11():
    complete_label = tk.Label(lower_frame, bg='white', text='Locked', font='Arial')
    complete_label.place(relx=.015, rely=.7, relwidth=.08, relheight=.05)
def done12():
    complete_label = tk.Label(lower_frame, bg='white', text='Locked', font='Arial')
    complete_label.place(relx=.015, rely=.76, relwidth=.08, relheight=.05)
def done13():
    complete_label = tk.Label(lower_frame, bg='white', text='Locked', font='Arial')
    complete_label.place(relx=.015, rely=.82, relwidth=.08, relheight=.05)
def done14():
    complete_label = tk.Label(lower_frame, bg='white', text='Locked', font='Arial')
    complete_label.place(relx=.015, rely=.88, relwidth=.08, relheight=.05)
def done15():
    complete_label = tk.Label(lower_frame, bg='white', text='Locked', font='Arial')
    complete_label.place(relx=.015, rely=.94, relwidth=.08, relheight=.05)
def done16():
    complete_label = tk.Label(lower_frame, bg='white', text='Locked', font='Arial')
    complete_label.place(relx=.015, rely=1, relwidth=.08, relheight=.05) 
# -----------------------------------------------------------------------------------

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)

frame = tk.Frame(root, bg='black', bd= 10)
frame.place(relwidth=1, relheight=1)

lower_frame = tk.Frame(root, bg='#9999ff')
lower_frame.place(relx=.05, rely=.05, relwidth=.9, relheight=.9)

title_label = tk.Label(lower_frame, bg='white', text='This is the Task Manager and Production Application', font='Arial')
title_label.place(relx=.11, rely=.01, relwidth=.8, relheight=.05)

finish = tk.Button(lower_frame, bg='white', text='Finish', font='arial', command=Finish)
finish.place(relx=.92, rely=.01, relwidth=.066, relheight=.05)

green_button = tk.Button(lower_frame, bg='#00ff00', command=green_count)
green_button.place(relx=.015, rely=.1, relwidth=.03, relheight=.05)

red_button = tk.Button(lower_frame, bg='red', command=red_count)
red_button.place(relx=.06, rely=.1, relwidth=.03, relheight=.05)

done_button = tk.Button(lower_frame, bg='grey', text='Done', command=done1)
done_button.place(relx=.92, rely=.1, relwidth=.06, relheight=.05)

entry1 = tk.Entry(lower_frame, bg='white', font='Arial')
entry1.place(relx=.1, rely=.1, relwidth=.8, relheight=.05)

# ----------------------------------------

green_button = tk.Button(lower_frame, bg='#00ff00', command=green_count)
green_button.place(relx=.015, rely=.16, relwidth=.03, relheight=.05)

red_button = tk.Button(lower_frame, bg='red', command=red_count)
red_button.place(relx=.06, rely=.16, relwidth=.03, relheight=.05)

done_button = tk.Button(lower_frame, bg='grey', text='Done', command=done2)
done_button.place(relx=.92, rely=.16, relwidth=.06, relheight=.05)

entry2 = tk.Entry(lower_frame, bg='white', font='Arial')
entry2.place(relx=.1, rely=.16, relwidth=.8, relheight=.05)

# ---------------------------------------------------

green_button = tk.Button(lower_frame, bg='#00ff00', command=green_count)
green_button.place(relx=.015, rely=.22, relwidth=.03, relheight=.05)

red_button = tk.Button(lower_frame, bg='red', command=red_count)
red_button.place(relx=.06, rely=.22, relwidth=.03, relheight=.05)

done_button = tk.Button(lower_frame, bg='grey', text='Done', command=done3)
done_button.place(relx=.92, rely=.22, relwidth=.06, relheight=.05)

entry3 = tk.Entry(lower_frame, bg='white', font='Arial')
entry3.place(relx=.1, rely=.22, relwidth=.8, relheight=.05)

# ---------------------------------------------------------

green_button = tk.Button(lower_frame, bg='#00ff00', command=green_count)
green_button.place(relx=.015, rely=.28, relwidth=.03, relheight=.05)

red_button = tk.Button(lower_frame, bg='red', command=red_count)
red_button.place(relx=.06, rely=.28, relwidth=.03, relheight=.05)

done_button = tk.Button(lower_frame, bg='grey', text='Done',command=done4)
done_button.place(relx=.92, rely=.28, relwidth=.06, relheight=.05)

entry4 = tk.Entry(lower_frame, bg='white', font='Arial')
entry4.place(relx=.1, rely=.28, relwidth=.8, relheight=.05)

# -------------------------------------------------------------

green_button = tk.Button(lower_frame, bg='#00ff00', command=green_count)
green_button.place(relx=.015, rely=.34, relwidth=.03, relheight=.05)

red_button = tk.Button(lower_frame, bg='red', command=red_count)
red_button.place(relx=.06, rely=.34, relwidth=.03, relheight=.05)

done_button = tk.Button(lower_frame, bg='grey', text='Done', command=done5)
done_button.place(relx=.92, rely=.34, relwidth=.06, relheight=.05)

entry5 = tk.Entry(lower_frame, bg='white', font='Arial')
entry5.place(relx=.1, rely=.34, relwidth=.8, relheight=.05)

# -----------------------------------------------------------------------------------

green_button = tk.Button(lower_frame, bg='#00ff00', command=green_count)
green_button.place(relx=.015, rely=.4, relwidth=.03, relheight=.05)

red_button = tk.Button(lower_frame, bg='red', command=red_count)
red_button.place(relx=.06, rely=.4, relwidth=.03, relheight=.05)

done_button = tk.Button(lower_frame, bg='grey', text='Done', command=done6)
done_button.place(relx=.92, rely=.4, relwidth=.06, relheight=.05)

entry6 = tk.Entry(lower_frame, bg='white', font='Arial')
entry6.place(relx=.1, rely=.4, relwidth=.8, relheight=.05)

# ------------------------------------------------------------------------------

green_button = tk.Button(lower_frame, bg='#00ff00', command=green_count)
green_button.place(relx=.015, rely=.46, relwidth=.03, relheight=.05)

red_button = tk.Button(lower_frame, bg='red', command=red_count)
red_button.place(relx=.06, rely=.46, relwidth=.03, relheight=.05)

done_button = tk.Button(lower_frame, bg='grey', text='Done', command=done7)
done_button.place(relx=.92, rely=.46, relwidth=.06, relheight=.05)

entry7 = tk.Entry(lower_frame, bg='white', font='Arial')
entry7.place(relx=.1, rely=.46, relwidth=.8, relheight=.05)

# -------------------------------------------------------------------------------

green_button = tk.Button(lower_frame, bg='#00ff00', command=green_count)
green_button.place(relx=.015, rely=.52, relwidth=.03, relheight=.05)

red_button = tk.Button(lower_frame, bg='red', command=red_count)
red_button.place(relx=.06, rely=.52, relwidth=.03, relheight=.05)

done_button = tk.Button(lower_frame, bg='grey', text='Done', command=done8)
done_button.place(relx=.92, rely=.52, relwidth=.06, relheight=.05)

entry8 = tk.Entry(lower_frame, bg='white', font='Arial')
entry8.place(relx=.1, rely=.52, relwidth=.8, relheight=.05)

# -------------------------------------------------------------------------------

green_button = tk.Button(lower_frame, bg='#00ff00', command=green_count)
green_button.place(relx=.015, rely=.58, relwidth=.03, relheight=.05)

red_button = tk.Button(lower_frame, bg='red', command=red_count)
red_button.place(relx=.06, rely=.58, relwidth=.03, relheight=.05)

done_button = tk.Button(lower_frame, bg='grey', text='Done', command=done9)
done_button.place(relx=.92, rely=.58, relwidth=.06, relheight=.05)

entry9 = tk.Entry(lower_frame, bg='white', font='Arial')
entry9.place(relx=.1, rely=.58, relwidth=.8, relheight=.05)

# -----------------------------------------------------------------------------

green_button = tk.Button(lower_frame, bg='#00ff00', command=green_count)
green_button.place(relx=.015, rely=.64, relwidth=.03, relheight=.05)

red_button = tk.Button(lower_frame, bg='red', command=red_count)
red_button.place(relx=.06, rely=.64, relwidth=.03, relheight=.05)

done_button = tk.Button(lower_frame, bg='grey', text='Done', command=done10)
done_button.place(relx=.92, rely=.64, relwidth=.06, relheight=.05)

entry10 = tk.Entry(lower_frame, bg='white', font='Arial')
entry10.place(relx=.1, rely=.64, relwidth=.8, relheight=.05)

# -----------------------------------------------------------------------------------

green_button = tk.Button(lower_frame, bg='#00ff00', command=green_count)
green_button.place(relx=.015, rely=.7, relwidth=.03, relheight=.05)

red_button = tk.Button(lower_frame, bg='red', command=red_count)
red_button.place(relx=.06, rely=.7, relwidth=.03, relheight=.05)

done_button = tk.Button(lower_frame, bg='grey', text='Done', command=done11)
done_button.place(relx=.92, rely=.7, relwidth=.06, relheight=.05)

entry11 = tk.Entry(lower_frame, bg='white', font='Arial')
entry11.place(relx=.1, rely=.7, relwidth=.8, relheight=.05)

# -----------------------------------------------------------------

green_button = tk.Button(lower_frame, bg='#00ff00', command=green_count)
green_button.place(relx=.015, rely=.76, relwidth=.03, relheight=.05)

red_button = tk.Button(lower_frame, bg='red', command=red_count)
red_button.place(relx=.06, rely=.76, relwidth=.03, relheight=.05)

done_button = tk.Button(lower_frame, bg='grey', text='Done', command=done12)
done_button.place(relx=.92, rely=.76, relwidth=.06, relheight=.05)

entry12 = tk.Entry(lower_frame, bg='white', font='Arial')
entry12.place(relx=.1, rely=.76, relwidth=.8, relheight=.05)

# ---------------------------------------------------------------

green_button = tk.Button(lower_frame, bg='#00ff00', command=green_count)
green_button.place(relx=.015, rely=.82, relwidth=.03, relheight=.05)

red_button = tk.Button(lower_frame, bg='red', command=red_count)
red_button.place(relx=.06, rely=.82, relwidth=.03, relheight=.05)

done_button = tk.Button(lower_frame, bg='grey', text='Done', command=done13)
done_button.place(relx=.92, rely=.82, relwidth=.06, relheight=.05)

entry13 = tk.Entry(lower_frame, bg='white', font='Arial')
entry13.place(relx=.1, rely=.82, relwidth=.8, relheight=.05)

# ----------------------------------------------------------------------

green_button = tk.Button(lower_frame, bg='#00ff00', command=green_count)
green_button.place(relx=.015, rely=.88, relwidth=.03, relheight=.05)

red_button = tk.Button(lower_frame, bg='red', command=red_count)
red_button.place(relx=.06, rely=.88, relwidth=.03, relheight=.05)

done_button = tk.Button(lower_frame, bg='grey', text='Done', command=done14)
done_button.place(relx=.92, rely=.88, relwidth=.06, relheight=.05)

entry14 = tk.Entry(lower_frame, bg='white', font='Arial')
entry14.place(relx=.1, rely=.88, relwidth=.8, relheight=.05)

# ---------------------------------------------------------------------

green_button = tk.Button(lower_frame, bg='#00ff00', command=green_count)
green_button.place(relx=.015, rely=.94, relwidth=.03, relheight=.05)

red_button = tk.Button(lower_frame, bg='red', command=red_count)
red_button.place(relx=.06, rely=.94, relwidth=.03, relheight=.05)

done_button = tk.Button(lower_frame, bg='grey', text='Done', command=done15)
done_button.place(relx=.92, rely=.94, relwidth=.06, relheight=.05)

entry15 = tk.Entry(lower_frame, bg='white', font='Arial')
entry15.place(relx=.1, rely=.94, relwidth=.8, relheight=.05)

# -----------------------------------------------------------------------------

green_button = tk.Button(lower_frame, bg='#00ff00', command=green_count)
green_button.place(relx=.015, rely=1, relwidth=.03, relheight=.05)

red_button = tk.Button(lower_frame, bg='red', command=red_count)
red_button.place(relx=.06, rely=1, relwidth=.03, relheight=.05)

done_button = tk.Button(lower_frame, bg='grey', text='Done', command=done15)
done_button.place(relx=.92, rely=1, relwidth=.06, relheight=.05)

entry16 = tk.Entry(lower_frame, bg='white', font='Arial')
entry16.place(relx=.1, rely=1, relwidth=.8, relheight=.05)

def get_entrys():
    a = entry1.get()
    b = entry2.get()
    c = entry3.get()
    d = entry4.get()
    e = entry5.get()
    f = entry6.get()
    g = entry7.get()
    h = entry8.get()
    i = entry9.get()
    j = entry10.get()
    k = entry11.get()
    l = entry12.get()
    m = entry13.get()
    n = entry14.get()
    o = entry15.get()
    p = entry16.get()
    lst = [a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p]
    new_lst = []
    for x in lst:
        if x != '':
            new_lst.append(x)
            print()
    root2 = tk.Tk()
    canvas_two = tk.Canvas(root2)

    third_frame = tk.Frame(root2, bg='black', bd=10)
    third_frame.place(relheight=1, relwidth=1)
    
    l_frame = tk.Frame(root2, bg='#9999ff')
    l_frame.place(relx=.05, rely=.08, relwidth=.9, relheight=.9)

    title = tk.Label(third_frame, bg='white', text='Tasks you have entered', font='Arial')
    title.place(relx=.16, rely=.01, relwidth=.7, relheight=.04)

    extra_label = tk.Label(l_frame, bg='white', text='Tasks: ', font='arial')
    extra_label.place(relx=.4, rely=.06, relwidth=.2, relheight=.04)
    
    l_label = tk.Label(l_frame, bg='white', font='Arial')
    l_label.place(relx=.09, rely=.15, relwidth=.8, relheight=.8)
    
    l_label['text'] = new_lst
    root2.mainloop()
    


# graph_button = tk.Button(lower_frame, bg='white', text='Tasks', font='arial', command=get_entrys)
# graph_button.place(relx=.01, rely=.01, relwidth=.08, relheight=.05)

root.mainloop()