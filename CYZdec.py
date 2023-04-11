'''
CYZ (encode) and CYZ (decode)
Copyright (C) 2023  Morgan Johnstone

This program is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License
as published by the Free Software Foundation; either version 2
of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
'''



from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
#temp code
from temp import sq_8192

root = Tk()
root.config(bg='grey')
root.title('Code Your Zero (decode)')
root.geometry('1300x800')

# IMAGES for buttons

img_0 = PhotoImage(file = 'img_1.png')
img_1 = PhotoImage(file = 'img_2.png')
img_2 = PhotoImage(file = 'img_3.png')
img_3 = PhotoImage(file = 'img_4.png')
img_4 = PhotoImage(file = 'img_0.png')

a_text = []
A_text = []
ä_text = []
Ä_text = []
b_text = []
B_text = []
c_text = []
C_text = []
d_text = []
D_text = []
e_text = []
E_text = []
f_text = []
F_text = []
g_text = []
G_text = []
h_text = []
H_text = []
i_text = []
I_text = []
j_text = []
J_text = []
k_text = []
K_text = []
l_text = []
L_text = []
m_text = []
M_text = []
n_text = []
N_text = []
o_text = []
O_text = []
ö_text = []
Ö_text = []
p_text = []
P_text = []
q_text = []
Q_text = []
r_text = []
R_text = []
s_text = []
S_text = []
t_text = []
T_text = []
u_text = []
U_text = []
ü_text = []
Ü_text = []
v_text = []
V_text = []
w_text = []
W_text = []
x_text = []
X_text = []
y_text = []
Y_text = []
z_text = []
Z_text = []

# extra
# chars

char_exclamation = []
char_quotes = []
char_dollar = []
char_percent = []
char_and = []
char_forward_slash = []
char_left_curly_bracket = []
char_left_bracket = []
char_left_square_bracket = []
char_right_bracket = []
char_right_square_bracket = []
char_equals = []
char_right_curly_bracket = []
char_question = []
char_sz = []
char_back_slash = []
char_comma = []
char_semi_colon = []
char_double_point = []
char_full_stop = []
char_lower_case_hyfen = []
char_minus = []
char_hashtag = []
char_plus = []
char_times_star = []
char_single_quotes = []
char_less_than = []
char_more_than = []
char_line_seperator = []
char_wavey = []
char_space = []

# extras
# numbers

zero = []
one = []
two = []
three = []
four = []
five = []
six = []
seven = []
eight = []
nine = []
ten = []

char_list = ['a', 'A', 'ä', 'Ä', 'b', 'B', 'c', 'C', 'd', 'D', 'e', 'E', 'f', 'F', 'g', 'G', 'h', 'H', 'i', 'I', 'j',
             'J', 'k', 'K', 'l', 'L', 'm', 'M', 'n', 'N', 'o', 'O', 'ö', 'Ö', 'p', 'P', 'q', 'Q',
             'r', 'R', 's', 'S', 't', 'T', 'u', 'U', 'ü', 'Ü', 'v', 'V', 'w', 'W', 'x', 'X', 'y', 'Y', 'z', 'Z', '!',
             '"', '$', '%', '&', '/', '{', '(', '[', ')', ']', '=', '}', '?', 'ß', '\\', ',', ';', ':', '.', '_', '-',
             '#', '+', '*', "''", '<', '>', '|', '~', 'space', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']


ztext1= sq_8192[0:5]
ztext2=sq_8192[5:10]
ztext3=sq_8192[10:15]
ztext4=sq_8192[15:20]
ztext5=sq_8192[20:25]
ztext6=sq_8192[25:30]
ztext7=sq_8192[30:35]
ztext8=sq_8192[35:40]
ztext9=sq_8192[40:45]
ztext10=sq_8192[45:50]
ztext11=sq_8192[50:55]
ztext12=sq_8192[55:60]
ztext13=sq_8192[60:65]
ztext14=sq_8192[65:70]
ztext15=sq_8192[70:75]
ztext16=sq_8192[75:80]
ztext17=sq_8192[80:85]
ztext18=sq_8192[85:90]
ztext19=sq_8192[90:95]
ztext20=sq_8192[95:100]
ztext21=sq_8192[100:105]
ztext22=sq_8192[105:110]
ztext23=sq_8192[110:115]
ztext24=sq_8192[115:120]
ztext25=sq_8192[120:125]
ztext26=sq_8192[125:130]
ztext27=sq_8192[130:135]
ztext28=sq_8192[135:140]
ztext29=sq_8192[140:145]
ztext30=sq_8192[145:150]
ztext31=sq_8192[150:155]
ztext32=sq_8192[155:160]
ztext33=sq_8192[160:165]
ztext34=sq_8192[165:170]
ztext35=sq_8192[170:175]
ztext36=sq_8192[175:180]
ztext37=sq_8192[180:185]
ztext38=sq_8192[185:190]
ztext39=sq_8192[190:195]
ztext40=sq_8192[195:200]
ztext41=sq_8192[200:205]
ztext42=sq_8192[205:210]
ztext43=sq_8192[210:215]
ztext44=sq_8192[215:220]
ztext45=sq_8192[220:225]
ztext46=sq_8192[225:230]
ztext47=sq_8192[230:235]
ztext48=sq_8192[235:240]
ztext49=sq_8192[240:245]
ztext50=sq_8192[245:250]
ztext51=sq_8192[250:255]
ztext52=sq_8192[255:260]
ztext53=sq_8192[260:265]
ztext54=sq_8192[265:270]
ztext55=sq_8192[270:275]
ztext56=sq_8192[275:280]
ztext57=sq_8192[280:285]
ztext58=sq_8192[285:290]
ztext59=sq_8192[290:295]
ztext60=sq_8192[295:300]
ztext61=sq_8192[300:305]
ztext62=sq_8192[305:310]
ztext63=sq_8192[310:315]
ztext64=sq_8192[315:320]
ztext65=sq_8192[320:325]
ztext66=sq_8192[325:330]
ztext67=sq_8192[330:335]
ztext68=sq_8192[335:340]
ztext69=sq_8192[340:345]
ztext70=sq_8192[345:350]
ztext71=sq_8192[350:355]
ztext72=sq_8192[355:360]
ztext73=sq_8192[360:365]
ztext74=sq_8192[365:370]
ztext75=sq_8192[370:375]
ztext76=sq_8192[375:380]
ztext77=sq_8192[380:385]
ztext78=sq_8192[385:390]
ztext79=sq_8192[390:395]
ztext80=sq_8192[395:400]
ztext81=sq_8192[400:405]
ztext82=sq_8192[405:410]
ztext83=sq_8192[410:415]
ztext84=sq_8192[415:420]
ztext85=sq_8192[420:425]
ztext86=sq_8192[425:430]
ztext87=sq_8192[430:435]
ztext88=sq_8192[435:440]
ztext89=sq_8192[440:445]
ztext90=sq_8192[445:450]
ztext91=sq_8192[450:455]
ztext92=sq_8192[455:460]
ztext93=sq_8192[460:465]
ztext94=sq_8192[465:470]
ztext95=sq_8192[470:475]
ztext96=sq_8192[475:480]
ztext97=sq_8192[480:485]
ztext98=sq_8192[485:490]
ztext99=sq_8192[490:495]
ztext100=sq_8192[495:500]


# definitions


def text_get():
    bin_txt_file = filedialog.askopenfilename()
    file = open(bin_txt_file)
    text_1.insert(1.0, file.read())
    text_main.delete('1.0', END)
    #ent_1.insert(0, text_1.get('1.0', '1.130'))
    #text_main.insert('1.0', text_1.get('1.0', END))
    file.close()

    if file is None:
        return


def new_window():
    new_window1 = Toplevel(root)
    new_window1.geometry('1060x3000')
    new_window1.title('Code Your Zero (text)')

    # create main frame
    x = Frame(new_window1)
    x.pack(fill=BOTH, expand=1)
    # canvas
    can = Canvas(x, bg='black')
    can.pack(side=LEFT, fill=BOTH, expand=1)
    # scroll to canvas
    yscroll = Scrollbar(x, orient=VERTICAL, command=can.yview)
    yscroll.pack(side=RIGHT, fill=Y)

    # add new frame to a window in the canvas
    can_frame = Frame(can, bg='black')
    can_frame.pack(fill=BOTH, expand=1)

    # config canvas

    can.configure(yscrollcommand=yscroll.set)

    can.bind('<Configure>', lambda e: can.configure(scrollregion=can.bbox('all')))

    can.create_window((0, 0), window=can_frame, anchor=NW)

    # another frame inside the canvas

    # add text to the above frame, SCROLLBAR
    global text_1
    text_1 = Text(can_frame, bg='black', fg='green', height=1000, width=130)
    text_1.pack(anchor=NW, fill=BOTH, expand=1)

    but1_frame = Frame(can)
    but1_frame.pack(anchor=S)

    # lab_frame = Label(can, text = 'changing text',bg = 'black', fg = 'green')
    # lab_frame.pack(anchor = E)

    t2c_but = Button(but1_frame, text='get text', bg='black', fg='green', command=text_get)
    t2c_but.pack()


# Entries - for all the code
# done
#code at end

#show next:
def get_entry_text():

    text_main.delete('1.0',END)

    #just incase it wasn't deleted before by clicking on letter,num,char etc...:
    guess_ent.delete(0,END)

    text_main.insert('1.0',text_1.get('1.0', '1.1300'))
    guess_ent.insert(0, text_1.get('1.1300', '1.1313'))
    text_1.delete('1.0', '1.1313')
    #global count
    #count = count+1
    #lab_1.config(text=f'     {count}')

    #change the text
    pass

def choice_code():
    pass

#button functions x100
def t1():
    txt_box.insert(END, 'a')
    a_text.append(guess_ent.get())
    guess_ent.delete(0, END)

def t2():
    txt_box.insert(END, 'A')
    A_text.append(guess_ent.get())
    guess_ent.delete(0, END)

def t3():
    txt_box.insert(END, 'ä')
    ä_text.append(guess_ent.get())
    guess_ent.delete(0, END)

def t4():
    txt_box.insert(END, 'Ä')
    Ä_text.append(guess_ent.get())
    guess_ent.delete(0, END)

def t5():
    txt_box.insert(END, 'b')
    b_text.append(guess_ent.get())
    guess_ent.delete(0, END)

def t6():
    txt_box.insert(END, 'B')
    B_text.append(guess_ent.get())
    guess_ent.delete(0, END)

def t7():
    txt_box.insert(END, 'c')
    c_text.append(guess_ent.get())
    guess_ent.delete(0, END)

def t8():
    txt_box.insert(END, 'C')
    C_text.append(guess_ent.get())
    guess_ent.delete(0, END)

def t9():
    txt_box.insert(END, 'd')
    d_text.append(guess_ent.get())
    guess_ent.delete(0, END)

def t10():
    txt_box.insert(END, 'D')
    D_text.append(guess_ent.get())
    guess_ent.delete(0, END)

def t11():
    txt_box.insert(END, 'e')
    e_text.append(guess_ent.get())
    guess_ent.delete(0, END)

def t12():
    txt_box.insert(END, 'E')
    E_text.append(guess_ent.get())
    guess_ent.delete(0, END)

def t13():
    txt_box.insert(END, 'f')
    f_text.append(guess_ent.get())
    guess_ent.delete(0, END)

def t14():
    txt_box.insert(END, 'F')
    F_text.append(guess_ent.get())
    guess_ent.delete(0, END)

def t15():
    txt_box.insert(END, 'g')
    g_text.append(guess_ent.get())
    guess_ent.delete(0, END)

def t16():
    txt_box.insert(END, 'G')
    G_text.append(guess_ent.get())
    guess_ent.delete(0, END)

def t17():
    txt_box.insert(END, 'h')
    h_text.append(guess_ent.get())
    guess_ent.delete(0, END)

def t18():
    txt_box.insert(END, 'H')
    H_text.append(guess_ent.get())
    guess_ent.delete(0, END)

def t19():
    txt_box.insert(END, 'i')
    i_text.append(guess_ent.get())
    guess_ent.delete(0, END)

def t20():
    txt_box.insert(END, 'I')
    I_text.append(guess_ent.get())
    guess_ent.delete(0, END)


def t21():
    txt_box.insert(END, 'j')
    j_text.append(guess_ent.get())
    guess_ent.delete(0, END)


def t22():
    txt_box.insert(END, 'J')
    J_text.append(guess_ent.get())
    guess_ent.delete(0, END)


def t23():
    txt_box.insert(END, 'k')
    k_text.append(guess_ent.get())
    guess_ent.delete(0, END)


def t24():
    txt_box.insert(END, 'K')
    K_text.append(guess_ent.get())
    guess_ent.delete(0, END)


def t25():
    txt_box.insert(END, 'l')
    l_text.append(guess_ent.get())
    guess_ent.delete(0, END)


def t26():
    txt_box.insert(END, 'L')
    L_text.append(guess_ent.get())
    guess_ent.delete(0, END)


def t27():
    txt_box.insert(END, 'm')
    m_text.append(guess_ent.get())
    guess_ent.delete(0, END)


def t28():
    txt_box.insert(END, 'M')
    M_text.append(guess_ent.get())
    guess_ent.delete(0, END)


def t29():
    txt_box.insert(END, 'n')
    n_text.append(guess_ent.get())
    guess_ent.delete(0, END)


def t30():
    txt_box.insert(END, 'N')
    N_text.append(guess_ent.get())
    guess_ent.delete(0, END)


def t31():
    txt_box.insert(END, 'o')
    o_text.append(guess_ent.get())
    guess_ent.delete(0, END)


def t32():
    txt_box.insert(END, 'O')
    O_text.append(guess_ent.get())
    guess_ent.delete(0, END)


def t33():
    txt_box.insert(END, 'ö')
    ö_text.append(guess_ent.get())
    guess_ent.delete(0, END)


def t34():
    txt_box.insert(END, Ö)
    Ö_text.append(guess_ent.get())
    guess_ent.delete(0, END)


def t35():
    txt_box.insert(END, 'p')
    p_text.append(guess_ent.get())
    guess_ent.delete(0, END)


def t36():
    txt_box.insert(END, 'P')
    P_text.append(guess_ent.get())
    guess_ent.delete(0, END)


def t37():
    txt_box.insert(END, 'q')
    q_text.append(guess_ent.get())
    guess_ent.delete(0, END)


def t38():
    txt_box.insert(END, 'Q')
    Q_text.append(guess_ent.get())
    guess_ent.delete(0, END)


def t39():
    txt_box.insert(END, 'r')
    r_text.append(guess_ent.get())
    guess_ent.delete(0, END)


def t40():
    txt_box.insert(END, 'R')
    R_text.append(guess_ent.get())
    guess_ent.delete(0, END)


def t41():
    txt_box.insert(END, 's')
    s_text.append(guess_ent.get())
    guess_ent.delete(0, END)


def t42():
    txt_box.insert(END, 'S')
    S_text.append(guess_ent.get())
    guess_ent.delete(0, END)


def t43():
    txt_box.insert(END, 't')
    t_text.append(guess_ent.get())
    guess_ent.delete(0, END)


def t44():
    txt_box.insert(END, 'T')
    T_text.append(guess_ent.get())
    guess_ent.delete(0, END)


def t45():
    txt_box.insert(END, 'u')
    u_text.append(guess_ent.get())
    guess_ent.delete(0, END)


def t46():
    txt_box.insert(END, 'U')
    U_text.append(guess_ent.get())
    guess_ent.delete(0, END)


def t47():
    txt_box.insert(END, 'ü')
    ü_text.append(guess_ent.get())
    guess_ent.delete(0, END)


def t48():
    txt_box.insert(END, 'Ü')
    Ü_text.append(guess_ent.get())
    guess_ent.delete(0, END)


def t49():
    txt_box.insert(END, 'v')
    v_text.append(guess_ent.get())
    guess_ent.delete(0, END)


def t50():
    txt_box.insert(END, 'V')
    V_text.append(guess_ent.get())
    guess_ent.delete(0, END)


def t51():
    txt_box.insert(END, 'w')
    w_text.append(guess_ent.get())
    guess_ent.delete(0, END)


def t52():
    txt_box.insert(END, 'W')
    W_text.append(guess_ent.get())
    guess_ent.delete(0, END)


def t53():
    txt_box.insert(END, 'x')
    x_text.append(guess_ent.get())
    guess_ent.delete(0, END)


def t54():
    txt_box.insert(END, 'X')
    X_text.append(guess_ent.get())
    guess_ent.delete(0, END)


def t55():
    txt_box.insert(END, 'y')
    y_text.append(guess_ent.get())
    guess_ent.delete(0, END)


def t56():
    txt_box.insert(END, 'Y')
    Y_text.append(guess_ent.get())
    guess_ent.delete(0, END)


def t57():
    txt_box.insert(END, 'z')
    z_text.append(guess_ent.get())
    guess_ent.delete(0, END)


def t58():
    txt_box.insert(END, 'Z')
    Z_text.append(guess_ent.get())
    guess_ent.delete(0, END)


def t59():
    txt_box.insert(END, '!')
    a_text.append(guess_ent.get())
    guess_ent.delete(0, END)


def t60():
    txt_box.insert(END, '"')
    a_text.append(guess_ent.get())
    guess_ent.delete(0, END)


def t61():
    txt_box.insert(END, '$')
    a_text.append(guess_ent.get())
    guess_ent.delete(0, END)


def t62():
    txt_box.insert(END, '%')
    a_text.append(guess_ent.get())
    guess_ent.delete(0, END)


def t63():
    txt_box.insert(END, '&')
    a_text.append(guess_ent.get())
    guess_ent.delete(0, END)


def t64():
    txt_box.insert(END, '/')
    a_text.append(guess_ent.get())
    guess_ent.delete(0, END)


def t65():
    txt_box.insert(END, '{')
    a_text.append(guess_ent.get())
    guess_ent.delete(0, END)


def t66():
    txt_box.insert(END, '(')
    a_text.append(guess_ent.get())
    guess_ent.delete(0, END)


def t67():
    txt_box.insert(END, '[')
    a_text.append(guess_ent.get())
    guess_ent.delete(0, END)


def t68():
    txt_box.insert(END, ')')
    a_text.append(guess_ent.get())
    guess_ent.delete(0, END)


def t69():
    txt_box.insert(END, ']')
    a_text.append(guess_ent.get())
    guess_ent.delete(0, END)


def t70():
    txt_box.insert(END, '=')
    a_text.append(guess_ent.get())
    guess_ent.delete(0, END)


def t71():
    txt_box.insert(END, '}')
    a_text.append(guess_ent.get())
    guess_ent.delete(0, END)


def t72():
    txt_box.insert(END, '?')
    a_text.append(guess_ent.get())
    guess_ent.delete(0, END)


def t73():
    txt_box.insert(END, 'ß')
    a_text.append(guess_ent.get())
    guess_ent.delete(0, END)


def t74():
    txt_box.insert(END, '\\')
    a_text.append(guess_ent.get())
    guess_ent.delete(0, END)


def t75():
    txt_box.insert(END, ',')
    a_text.append(guess_ent.get())
    guess_ent.delete(0, END)


def t76():
    txt_box.insert(END, ';')
    a_text.append(guess_ent.get())
    guess_ent.delete(0, END)


def t77():
    txt_box.insert(END, ':')
    a_text.append(guess_ent.get())
    guess_ent.delete(0, END)


def t78():
    txt_box.insert(END, '.')
    a_text.append(guess_ent.get())
    guess_ent.delete(0, END)


def t79():
    txt_box.insert(END, '_')
    a_text.append(guess_ent.get())
    guess_ent.delete(0, END)


def t80():
    txt_box.insert(END, '-')
    a_text.append(guess_ent.get())
    guess_ent.delete(0, END)


def t81():
    txt_box.insert(END, '#')
    a_text.append(guess_ent.get())
    guess_ent.delete(0, END)


def t82():
    txt_box.insert(END, '+')
    a_text.append(guess_ent.get())
    guess_ent.delete(0, END)


def t83():
    txt_box.insert(END, '*')
    a_text.append(guess_ent.get())
    guess_ent.delete(0, END)


def t84():
    txt_box.insert(END, "'")
    a_text.append(guess_ent.get())
    guess_ent.delete(0, END)


def t85():
    txt_box.insert(END, '<')
    a_text.append(guess_ent.get())
    guess_ent.delete(0, END)


def t86():
    txt_box.insert(END, '>')
    a_text.append(guess_ent.get())
    guess_ent.delete(0, END)


def t87():
    txt_box.insert(END, '|')
    a_text.append(guess_ent.get())
    guess_ent.delete(0, END)


def t88():
    txt_box.insert(END, '~')
    a_text.append(guess_ent.get())
    guess_ent.delete(0, END)


def t89():
    txt_box.insert(END, ' ')
    a_text.append(guess_ent.get())
    guess_ent.delete(0, END)


def t90():
    txt_box.insert(END, '0')
    zero.append(guess_ent.get())
    guess_ent.delete(0, END)


def t91():
    txt_box.insert(END, '1')
    one.append(guess_ent.get())
    guess_ent.delete(0, END)


def t92():
    txt_box.insert(END, '2')
    two.append(guess_ent.get())
    guess_ent.delete(0, END)


def t93():
    txt_box.insert(END, '3')
    three.append(guess_ent.get())
    guess_ent.delete(0, END)


def t94():
    txt_box.insert(END, '4')
    four.append(guess_ent.get())
    guess_ent.delete(0, END)


def t95():
    txt_box.insert(END, '5')
    five.append(guess_ent.get())
    guess_ent.delete(0, END)


def t96():
    txt_box.insert(END, '6')
    six.append(guess_ent.get())
    guess_ent.delete(0, END)


def t97():
    txt_box.insert(END, '7')
    seven.append(guess_ent.get())
    guess_ent.delete(0, END)


def t98():
    txt_box.insert(END, '8')
    eight.append(guess_ent.get())
    guess_ent.delete(0, END)


def t99():
    txt_box.insert(END, '9')
    nine.append(guess_ent.get())
    guess_ent.delete(0, END)


def t100():
    txt_box.insert(END, '10')
    ten.append(guess_ent.get())
    guess_ent.delete(0, END)
#____________________________________________________________________________________________
def ztext_change():
    pass

def show_pic1():

    if ztext1[0] in text_main.get('1.0', '1.13'):
        b_1.config(image=img_0)

    if ztext1[1] in text_main.get('1.0', '1.13'):
        b_1.config(image=img_1)

    if ztext1[2] in text_main.get('1.0', '1.13'):
        b_1.config(image=img_2)

    if ztext1[3] in text_main.get('1.0', '1.13'):
        b_1.config(image=img_3)

    if ztext1[4] in text_main.get('1.0', '1.13'):
        b_1.config(image=img_4)

    if ztext2[0] in text_main.get('1.13', '1.26'):
        b_2.config(image=img_0)

    if ztext2[1] in text_main.get('1.13', '1.26'):
        b_2.config(image=img_1)

    if ztext2[2] in text_main.get('1.13', '1.26'):
        b_2.config(image=img_2)

    if ztext2[3] in text_main.get('1.13', '1.26'):
        b_2.config(image=img_3)

    if ztext2[4] in text_main.get('1.13', '1.26'):
        b_2.config(image=img_4)

    if ztext3[0] in text_main.get('1.26', '1.39'):
        b_3.config(image=img_0)

    if ztext3[1] in text_main.get('1.26', '1.39'):
        b_3.config(image=img_1)

    if ztext3[2] in text_main.get('1.26', '1.39'):
        b_3.config(image=img_2)

    if ztext3[3] in text_main.get('1.26', '1.39'):
        b_3.config(image=img_3)

    if ztext3[4] in text_main.get('1.26', '1.39'):
        b_3.config(image=img_4)

    if ztext4[0] in text_main.get('1.39', '1.52'):
        b_4.config(image=img_0)

    if ztext4[1] in text_main.get('1.39', '1.52'):
        b_4.config(image=img_1)

    if ztext4[2] in text_main.get('1.39', '1.52'):
        b_4.config(image=img_2)

    if ztext4[3] in text_main.get('1.39', '1.52'):
        b_4.config(image=img_3)

    if ztext4[4] in text_main.get('1.39', '1.52'):
        b_4.config(image=img_4)

    if ztext5[0] in text_main.get('1.52', '1.65'):
        b_5.config(image=img_0)

    if ztext5[1] in text_main.get('1.52', '1.65'):
        b_5.config(image=img_1)

    if ztext5[2] in text_main.get('1.52', '1.65'):
        b_5.config(image=img_2)

    if ztext5[3] in text_main.get('1.52', '1.65'):
        b_5.config(image=img_3)

    if ztext5[4] in text_main.get('1.52', '1.65'):
        b_5.config(image=img_4)

    if ztext6[0] in text_main.get('1.65', '1.78'):
        b_6.config(image=img_0)

    if ztext6[1] in text_main.get('1.65', '1.78'):
        b_6.config(image=img_1)

    if ztext6[2] in text_main.get('1.65', '1.78'):
        b_6.config(image=img_2)

    if ztext6[3] in text_main.get('1.65', '1.78'):
        b_6.config(image=img_3)

    if ztext6[4] in text_main.get('1.65', '1.78'):
        b_6.config(image=img_4)

    if ztext7[0] in text_main.get('1.78', '1.91'):
        b_7.config(image=img_0)

    if ztext7[1] in text_main.get('1.78', '1.91'):
        b_7.config(image=img_1)

    if ztext7[2] in text_main.get('1.78', '1.91'):
        b_7.config(image=img_2)

    if ztext7[3] in text_main.get('1.78', '1.91'):
        b_7.config(image=img_3)

    if ztext7[4] in text_main.get('1.78', '1.91'):
        b_7.config(image=img_4)

    if ztext8[0] in text_main.get('1.91', '1.104'):
        b_8.config(image=img_0)

    if ztext8[1] in text_main.get('1.91', '1.104'):
        b_8.config(image=img_1)

    if ztext8[2] in text_main.get('1.91', '1.104'):
        b_8.config(image=img_2)

    if ztext8[3] in text_main.get('1.91', '1.104'):
        b_8.config(image=img_3)

    if ztext8[4] in text_main.get('1.91', '1.104'):
        b_8.config(image=img_4)

    if ztext9[0] in text_main.get('1.104', '1.117'):
        b_9.config(image=img_0)

    if ztext9[1] in text_main.get('1.104', '1.117'):
        b_9.config(image=img_1)

    if ztext9[2] in text_main.get('1.104', '1.117'):
        b_9.config(image=img_2)

    if ztext9[3] in text_main.get('1.104', '1.117'):
        b_9.config(image=img_3)

    if ztext9[4] in text_main.get('1.104', '1.117'):
        b_9.config(image=img_4)

    if ztext10[0] in text_main.get('1.117', '1.130'):
        b_10.config(image=img_0)

    if ztext10[1] in text_main.get('1.117', '1.130'):
        b_10.config(image=img_1)

    if ztext10[2] in text_main.get('1.117', '1.130'):
        b_10.config(image=img_2)

    if ztext10[3] in text_main.get('1.117', '1.130'):
        b_10.config(image=img_3)

    if ztext10[4] in text_main.get('1.117', '1.130'):
        b_10.config(image=img_4)

    if ztext11[0] in text_main.get('1.130', '1.143'):
        b_11.config(image=img_0)

    if ztext11[1] in text_main.get('1.130', '1.143'):
        b_11.config(image=img_1)

    if ztext11[2] in text_main.get('1.130', '1.143'):
        b_11.config(image=img_2)

    if ztext11[3] in text_main.get('1.130', '1.143'):
        b_11.config(image=img_3)

    if ztext11[4] in text_main.get('1.130', '1.143'):
        b_11.config(image=img_4)

    if ztext12[0] in text_main.get('1.143', '1.156'):
        b_12.config(image=img_0)

    if ztext12[1] in text_main.get('1.143', '1.156'):
        b_12.config(image=img_1)

    if ztext12[2] in text_main.get('1.143', '1.156'):
        b_12.config(image=img_2)

    if ztext12[3] in text_main.get('1.143', '1.156'):
        b_12.config(image=img_3)

    if ztext12[4] in text_main.get('1.143', '1.156'):
        b_12.config(image=img_4)

    if ztext13[0] in text_main.get('1.156', '1.169'):
        b_13.config(image=img_0)

    if ztext13[1] in text_main.get('1.156', '1.169'):
        b_13.config(image=img_1)

    if ztext13[2] in text_main.get('1.156', '1.169'):
        b_13.config(image=img_2)

    if ztext13[3] in text_main.get('1.156', '1.169'):
        b_13.config(image=img_3)

    if ztext13[4] in text_main.get('1.156', '1.169'):
        b_13.config(image=img_4)

    if ztext14[0] in text_main.get('1.169', '1.182'):
        b_14.config(image=img_0)

    if ztext14[1] in text_main.get('1.169', '1.182'):
        b_14.config(image=img_1)

    if ztext14[2] in text_main.get('1.169', '1.182'):
        b_14.config(image=img_2)

    if ztext14[3] in text_main.get('1.169', '1.182'):
        b_14.config(image=img_3)

    if ztext14[4] in text_main.get('1.169', '1.182'):
        b_14.config(image=img_4)

    if ztext15[0] in text_main.get('1.182', '1.195'):
        b_15.config(image=img_0)

    if ztext15[1] in text_main.get('1.182', '1.195'):
        b_15.config(image=img_1)

    if ztext15[2] in text_main.get('1.182', '1.195'):
        b_15.config(image=img_2)

    if ztext15[3] in text_main.get('1.182', '1.195'):
        b_15.config(image=img_3)

    if ztext15[4] in text_main.get('1.182', '1.195'):
        b_15.config(image=img_4)

    if ztext16[0] in text_main.get('1.195', '1.208'):
        b_16.config(image=img_0)

    if ztext16[1] in text_main.get('1.195', '1.208'):
        b_16.config(image=img_1)

    if ztext16[2] in text_main.get('1.195', '1.208'):
        b_16.config(image=img_2)

    if ztext16[3] in text_main.get('1.195', '1.208'):
        b_16.config(image=img_3)

    if ztext16[4] in text_main.get('1.195', '1.208'):
        b_16.config(image=img_4)

    if ztext17[0] in text_main.get('1.208', '1.221'):
        b_17.config(image=img_0)

    if ztext17[1] in text_main.get('1.208', '1.221'):
        b_17.config(image=img_1)

    if ztext17[2] in text_main.get('1.208', '1.221'):
        b_17.config(image=img_2)

    if ztext17[3] in text_main.get('1.208', '1.221'):
        b_17.config(image=img_3)

    if ztext17[4] in text_main.get('1.208', '1.221'):
        b_17.config(image=img_4)

    if ztext18[0] in text_main.get('1.221', '1.234'):
        b_18.config(image=img_0)

    if ztext18[1] in text_main.get('1.221', '1.234'):
        b_18.config(image=img_1)

    if ztext18[2] in text_main.get('1.221', '1.234'):
        b_18.config(image=img_2)

    if ztext18[3] in text_main.get('1.221', '1.234'):
        b_18.config(image=img_3)

    if ztext18[4] in text_main.get('1.221', '1.234'):
        b_18.config(image=img_4)

    if ztext19[0] in text_main.get('1.234', '1.247'):
        b_19.config(image=img_0)

    if ztext19[1] in text_main.get('1.234', '1.247'):
        b_19.config(image=img_1)

    if ztext19[2] in text_main.get('1.234', '1.247'):
        b_19.config(image=img_2)

    if ztext19[3] in text_main.get('1.234', '1.247'):
        b_19.config(image=img_3)

    if ztext19[4] in text_main.get('1.234', '1.247'):
        b_19.config(image=img_4)

    if ztext20[0] in text_main.get('1.247', '1.260'):
        b_20.config(image=img_0)

    if ztext20[1] in text_main.get('1.247', '1.260'):
        b_20.config(image=img_1)

    if ztext20[2] in text_main.get('1.247', '1.260'):
        b_20.config(image=img_2)

    if ztext20[3] in text_main.get('1.247', '1.260'):
        b_20.config(image=img_3)

    if ztext20[4] in text_main.get('1.247', '1.260'):
        b_20.config(image=img_4)

    if ztext21[0] in text_main.get('1.260', '1.273'):
        b_21.config(image=img_0)

    if ztext21[1] in text_main.get('1.260', '1.273'):
        b_21.config(image=img_1)

    if ztext21[2] in text_main.get('1.260', '1.273'):
        b_21.config(image=img_2)

    if ztext21[3] in text_main.get('1.260', '1.273'):
        b_21.config(image=img_3)

    if ztext21[4] in text_main.get('1.260', '1.273'):
        b_21.config(image=img_4)

    if ztext22[0] in text_main.get('1.273', '1.286'):
        b_22.config(image=img_0)

    if ztext22[1] in text_main.get('1.273', '1.286'):
        b_22.config(image=img_1)

    if ztext22[2] in text_main.get('1.273', '1.286'):
        b_22.config(image=img_2)

    if ztext22[3] in text_main.get('1.273', '1.286'):
        b_22.config(image=img_3)

    if ztext22[4] in text_main.get('1.273', '1.286'):
        b_22.config(image=img_4)

    if ztext23[0] in text_main.get('1.286', '1.299'):
        b_23.config(image=img_0)

    if ztext23[1] in text_main.get('1.286', '1.299'):
        b_23.config(image=img_1)

    if ztext23[2] in text_main.get('1.286', '1.299'):
        b_23.config(image=img_2)

    if ztext23[3] in text_main.get('1.286', '1.299'):
        b_23.config(image=img_3)

    if ztext23[4] in text_main.get('1.286', '1.299'):
        b_23.config(image=img_4)

    if ztext24[0] in text_main.get('1.299', '1.312'):
        b_24.config(image=img_0)

    if ztext24[1] in text_main.get('1.299', '1.312'):
        b_24.config(image=img_1)

    if ztext24[2] in text_main.get('1.299', '1.312'):
        b_24.config(image=img_2)

    if ztext24[3] in text_main.get('1.299', '1.312'):
        b_24.config(image=img_3)

    if ztext24[4] in text_main.get('1.299', '1.312'):
        b_24.config(image=img_4)

    if ztext25[0] in text_main.get('1.312', '1.325'):
        b_25.config(image=img_0)

    if ztext25[1] in text_main.get('1.312', '1.325'):
        b_25.config(image=img_1)

    if ztext25[2] in text_main.get('1.312', '1.325'):
        b_25.config(image=img_2)

    if ztext25[3] in text_main.get('1.312', '1.325'):
        b_25.config(image=img_3)

    if ztext25[4] in text_main.get('1.312', '1.325'):
        b_25.config(image=img_4)

    if ztext26[0] in text_main.get('1.325', '1.338'):
        b_26.config(image=img_0)

    if ztext26[1] in text_main.get('1.325', '1.338'):
        b_26.config(image=img_1)

    if ztext26[2] in text_main.get('1.325', '1.338'):
        b_26.config(image=img_2)

    if ztext26[3] in text_main.get('1.325', '1.338'):
        b_26.config(image=img_3)

    if ztext26[4] in text_main.get('1.325', '1.338'):
        b_26.config(image=img_4)

    if ztext27[0] in text_main.get('1.338', '1.351'):
        b_27.config(image=img_0)

    if ztext27[1] in text_main.get('1.338', '1.351'):
        b_27.config(image=img_1)

    if ztext27[2] in text_main.get('1.338', '1.351'):
        b_27.config(image=img_2)

    if ztext27[3] in text_main.get('1.338', '1.351'):
        b_27.config(image=img_3)

    if ztext27[4] in text_main.get('1.338', '1.351'):
        b_27.config(image=img_4)

    if ztext28[0] in text_main.get('1.351', '1.364'):
        b_28.config(image=img_0)

    if ztext28[1] in text_main.get('1.351', '1.364'):
        b_28.config(image=img_1)

    if ztext28[2] in text_main.get('1.351', '1.364'):
        b_28.config(image=img_2)

    if ztext28[3] in text_main.get('1.351', '1.364'):
        b_28.config(image=img_3)

    if ztext28[4] in text_main.get('1.351', '1.364'):
        b_28.config(image=img_4)

    if ztext29[0] in text_main.get('1.364', '1.377'):
        b_29.config(image=img_0)

    if ztext29[1] in text_main.get('1.364', '1.377'):
        b_29.config(image=img_1)

    if ztext29[2] in text_main.get('1.364', '1.377'):
        b_29.config(image=img_2)

    if ztext29[3] in text_main.get('1.364', '1.377'):
        b_29.config(image=img_3)

    if ztext29[4] in text_main.get('1.364', '1.377'):
        b_29.config(image=img_4)

    if ztext30[0] in text_main.get('1.377', '1.390'):
        b_30.config(image=img_0)

    if ztext30[1] in text_main.get('1.377', '1.390'):
        b_30.config(image=img_1)

    if ztext30[2] in text_main.get('1.377', '1.390'):
        b_30.config(image=img_2)

    if ztext30[3] in text_main.get('1.377', '1.390'):
        b_30.config(image=img_3)

    if ztext30[4] in text_main.get('1.377', '1.390'):
        b_30.config(image=img_4)

    if ztext31[0] in text_main.get('1.390', '1.403'):
        b_31.config(image=img_0)

    if ztext31[1] in text_main.get('1.390', '1.403'):
        b_31.config(image=img_1)

    if ztext31[2] in text_main.get('1.390', '1.403'):
        b_31.config(image=img_2)

    if ztext31[3] in text_main.get('1.390', '1.403'):
        b_31.config(image=img_3)

    if ztext31[4] in text_main.get('1.390', '1.403'):
        b_31.config(image=img_4)

    if ztext32[0] in text_main.get('1.403', '1.416'):
        b_32.config(image=img_0)

    if ztext32[1] in text_main.get('1.403', '1.416'):
        b_32.config(image=img_1)

    if ztext32[2] in text_main.get('1.403', '1.416'):
        b_32.config(image=img_2)

    if ztext32[3] in text_main.get('1.403', '1.416'):
        b_32.config(image=img_3)

    if ztext32[4] in text_main.get('1.403', '1.416'):
        b_32.config(image=img_4)

    if ztext33[0] in text_main.get('1.416', '1.429'):
        b_33.config(image=img_0)

    if ztext33[1] in text_main.get('1.416', '1.429'):
        b_33.config(image=img_1)

    if ztext33[2] in text_main.get('1.416', '1.429'):
        b_33.config(image=img_2)

    if ztext33[3] in text_main.get('1.416', '1.429'):
        b_33.config(image=img_3)

    if ztext33[4] in text_main.get('1.416', '1.429'):
        b_33.config(image=img_4)

    if ztext34[0] in text_main.get('1.429', '1.442'):
        b_34.config(image=img_0)

    if ztext34[1] in text_main.get('1.429', '1.442'):
        b_34.config(image=img_1)

    if ztext34[2] in text_main.get('1.429', '1.442'):
        b_34.config(image=img_2)

    if ztext34[3] in text_main.get('1.429', '1.442'):
        b_34.config(image=img_3)

    if ztext34[4] in text_main.get('1.429', '1.442'):
        b_34.config(image=img_4)

    if ztext35[0] in text_main.get('1.442', '1.455'):
        b_35.config(image=img_0)

    if ztext35[1] in text_main.get('1.442', '1.455'):
        b_35.config(image=img_1)

    if ztext35[2] in text_main.get('1.442', '1.455'):
        b_35.config(image=img_2)

    if ztext35[3] in text_main.get('1.442', '1.455'):
        b_35.config(image=img_3)

    if ztext35[4] in text_main.get('1.442', '1.455'):
        b_35.config(image=img_4)

    if ztext36[0] in text_main.get('1.455', '1.468'):
        b_36.config(image=img_0)

    if ztext36[1] in text_main.get('1.455', '1.468'):
        b_36.config(image=img_1)

    if ztext36[2] in text_main.get('1.455', '1.468'):
        b_36.config(image=img_2)

    if ztext36[3] in text_main.get('1.455', '1.468'):
        b_36.config(image=img_3)

    if ztext36[4] in text_main.get('1.455', '1.468'):
        b_36.config(image=img_4)

    if ztext37[0] in text_main.get('1.468', '1.481'):
        b_37.config(image=img_0)

    if ztext37[1] in text_main.get('1.468', '1.481'):
        b_37.config(image=img_1)

    if ztext37[2] in text_main.get('1.468', '1.481'):
        b_37.config(image=img_2)

    if ztext37[3] in text_main.get('1.468', '1.481'):
        b_37.config(image=img_3)

    if ztext37[4] in text_main.get('1.468', '1.481'):
        b_37.config(image=img_4)

    if ztext38[0] in text_main.get('1.481', '1.494'):
        b_38.config(image=img_0)

    if ztext38[1] in text_main.get('1.481', '1.494'):
        b_38.config(image=img_1)

    if ztext38[2] in text_main.get('1.481', '1.494'):
        b_38.config(image=img_2)

    if ztext38[3] in text_main.get('1.481', '1.494'):
        b_38.config(image=img_3)

    if ztext38[4] in text_main.get('1.481', '1.494'):
        b_38.config(image=img_4)

    if ztext39[0] in text_main.get('1.494', '1.507'):
        b_39.config(image=img_0)

    if ztext39[1] in text_main.get('1.494', '1.507'):
        b_39.config(image=img_1)

    if ztext39[2] in text_main.get('1.494', '1.507'):
        b_39.config(image=img_2)

    if ztext39[3] in text_main.get('1.494', '1.507'):
        b_39.config(image=img_3)

    if ztext39[4] in text_main.get('1.494', '1.507'):
        b_39.config(image=img_4)

    if ztext40[0] in text_main.get('1.507', '1.520'):
        b_40.config(image=img_0)

    if ztext40[1] in text_main.get('1.507', '1.520'):
        b_40.config(image=img_1)

    if ztext40[2] in text_main.get('1.507', '1.520'):
        b_40.config(image=img_2)

    if ztext40[3] in text_main.get('1.507', '1.520'):
        b_40.config(image=img_3)

    if ztext40[4] in text_main.get('1.507', '1.520'):
        b_40.config(image=img_4)

    if ztext41[0] in text_main.get('1.520', '1.533'):
        b_41.config(image=img_0)

    if ztext41[1] in text_main.get('1.520', '1.533'):
        b_41.config(image=img_1)

    if ztext41[2] in text_main.get('1.520', '1.533'):
        b_41.config(image=img_2)

    if ztext41[3] in text_main.get('1.520', '1.533'):
        b_41.config(image=img_3)

    if ztext41[4] in text_main.get('1.520', '1.533'):
        b_41.config(image=img_4)

    if ztext42[0] in text_main.get('1.533', '1.546'):
        b_42.config(image=img_0)

    if ztext42[1] in text_main.get('1.533', '1.546'):
        b_42.config(image=img_1)

    if ztext42[2] in text_main.get('1.533', '1.546'):
        b_42.config(image=img_2)

    if ztext42[3] in text_main.get('1.533', '1.546'):
        b_42.config(image=img_3)

    if ztext42[4] in text_main.get('1.533', '1.546'):
        b_42.config(image=img_4)

    if ztext43[0] in text_main.get('1.546', '1.559'):
        b_43.config(image=img_0)

    if ztext43[1] in text_main.get('1.546', '1.559'):
        b_43.config(image=img_1)

    if ztext43[2] in text_main.get('1.546', '1.559'):
        b_43.config(image=img_2)

    if ztext43[3] in text_main.get('1.546', '1.559'):
        b_43.config(image=img_3)

    if ztext43[4] in text_main.get('1.546', '1.559'):
        b_43.config(image=img_4)

    if ztext44[0] in text_main.get('1.559', '1.572'):
        b_44.config(image=img_0)

    if ztext44[1] in text_main.get('1.559', '1.572'):
        b_44.config(image=img_1)

    if ztext44[2] in text_main.get('1.559', '1.572'):
        b_44.config(image=img_2)

    if ztext44[3] in text_main.get('1.559', '1.572'):
        b_44.config(image=img_3)

    if ztext44[4] in text_main.get('1.559', '1.572'):
        b_44.config(image=img_4)

    if ztext45[0] in text_main.get('1.572', '1.585'):
        b_45.config(image=img_0)

    if ztext45[1] in text_main.get('1.572', '1.585'):
        b_45.config(image=img_1)

    if ztext45[2] in text_main.get('1.572', '1.585'):
        b_45.config(image=img_2)

    if ztext45[3] in text_main.get('1.572', '1.585'):
        b_45.config(image=img_3)

    if ztext45[4] in text_main.get('1.572', '1.585'):
        b_45.config(image=img_4)

    if ztext46[0] in text_main.get('1.585', '1.598'):
        b_46.config(image=img_0)

    if ztext46[1] in text_main.get('1.585', '1.598'):
        b_46.config(image=img_1)

    if ztext46[2] in text_main.get('1.585', '1.598'):
        b_46.config(image=img_2)

    if ztext46[3] in text_main.get('1.585', '1.598'):
        b_46.config(image=img_3)

    if ztext46[4] in text_main.get('1.585', '1.598'):
        b_46.config(image=img_4)

    if ztext47[0] in text_main.get('1.598', '1.611'):
        b_47.config(image=img_0)

    if ztext47[1] in text_main.get('1.598', '1.611'):
        b_47.config(image=img_1)

    if ztext47[2] in text_main.get('1.598', '1.611'):
        b_47.config(image=img_2)

    if ztext47[3] in text_main.get('1.598', '1.611'):
        b_47.config(image=img_3)

    if ztext47[4] in text_main.get('1.598', '1.611'):
        b_47.config(image=img_4)

    if ztext48[0] in text_main.get('1.611', '1.624'):
        b_48.config(image=img_0)

    if ztext48[1] in text_main.get('1.611', '1.624'):
        b_48.config(image=img_1)

    if ztext48[2] in text_main.get('1.611', '1.624'):
        b_48.config(image=img_2)

    if ztext48[3] in text_main.get('1.611', '1.624'):
        b_48.config(image=img_3)

    if ztext48[4] in text_main.get('1.611', '1.624'):
        b_48.config(image=img_4)

    if ztext49[0] in text_main.get('1.624', '1.637'):
        b_49.config(image=img_0)

    if ztext49[1] in text_main.get('1.624', '1.637'):
        b_49.config(image=img_1)

    if ztext49[2] in text_main.get('1.624', '1.637'):
        b_49.config(image=img_2)

    if ztext49[3] in text_main.get('1.624', '1.637'):
        b_49.config(image=img_3)

    if ztext49[4] in text_main.get('1.624', '1.637'):
        b_49.config(image=img_4)

    if ztext50[0] in text_main.get('1.637', '1.650'):
        b_50.config(image=img_0)

    if ztext50[1] in text_main.get('1.637', '1.650'):
        b_50.config(image=img_1)

    if ztext50[2] in text_main.get('1.637', '1.650'):
        b_50.config(image=img_2)

    if ztext50[3] in text_main.get('1.637', '1.650'):
        b_50.config(image=img_3)

    if ztext50[4] in text_main.get('1.637', '1.650'):
        b_50.config(image=img_4)

    if ztext51[0] in text_main.get('1.650', '1.663'):
        b_51.config(image=img_0)

    if ztext51[1] in text_main.get('1.650', '1.663'):
        b_51.config(image=img_1)

    if ztext51[2] in text_main.get('1.650', '1.663'):
        b_51.config(image=img_2)

    if ztext51[3] in text_main.get('1.650', '1.663'):
        b_51.config(image=img_3)

    if ztext51[4] in text_main.get('1.650', '1.663'):
        b_51.config(image=img_4)

    if ztext52[0] in text_main.get('1.663', '1.676'):
        b_52.config(image=img_0)

    if ztext52[1] in text_main.get('1.663', '1.676'):
        b_52.config(image=img_1)

    if ztext52[2] in text_main.get('1.663', '1.676'):
        b_52.config(image=img_2)

    if ztext52[3] in text_main.get('1.663', '1.676'):
        b_52.config(image=img_3)

    if ztext52[4] in text_main.get('1.663', '1.676'):
        b_52.config(image=img_4)

    if ztext53[0] in text_main.get('1.676', '1.689'):
        b_53.config(image=img_0)

    if ztext53[1] in text_main.get('1.676', '1.689'):
        b_53.config(image=img_1)

    if ztext53[2] in text_main.get('1.676', '1.689'):
        b_53.config(image=img_2)

    if ztext53[3] in text_main.get('1.676', '1.689'):
        b_53.config(image=img_3)

    if ztext53[4] in text_main.get('1.676', '1.689'):
        b_53.config(image=img_4)

    if ztext54[0] in text_main.get('1.689', '1.702'):
        b_54.config(image=img_0)

    if ztext54[1] in text_main.get('1.689', '1.702'):
        b_54.config(image=img_1)

    if ztext54[2] in text_main.get('1.689', '1.702'):
        b_54.config(image=img_2)

    if ztext54[3] in text_main.get('1.689', '1.702'):
        b_54.config(image=img_3)

    if ztext54[4] in text_main.get('1.689', '1.702'):
        b_54.config(image=img_4)

    if ztext55[0] in text_main.get('1.702', '1.715'):
        b_55.config(image=img_0)

    if ztext55[1] in text_main.get('1.702', '1.715'):
        b_55.config(image=img_1)

    if ztext55[2] in text_main.get('1.702', '1.715'):
        b_55.config(image=img_2)

    if ztext55[3] in text_main.get('1.702', '1.715'):
        b_55.config(image=img_3)

    if ztext55[4] in text_main.get('1.702', '1.715'):
        b_55.config(image=img_4)

    if ztext56[0] in text_main.get('1.715', '1.728'):
        b_56.config(image=img_0)

    if ztext56[1] in text_main.get('1.715', '1.728'):
        b_56.config(image=img_1)

    if ztext56[2] in text_main.get('1.715', '1.728'):
        b_56.config(image=img_2)

    if ztext56[3] in text_main.get('1.715', '1.728'):
        b_56.config(image=img_3)

    if ztext56[4] in text_main.get('1.715', '1.728'):
        b_56.config(image=img_4)

    if ztext57[0] in text_main.get('1.728', '1.741'):
        b_57.config(image=img_0)

    if ztext57[1] in text_main.get('1.728', '1.741'):
        b_57.config(image=img_1)

    if ztext57[2] in text_main.get('1.728', '1.741'):
        b_57.config(image=img_2)

    if ztext57[3] in text_main.get('1.728', '1.741'):
        b_57.config(image=img_3)

    if ztext57[4] in text_main.get('1.728', '1.741'):
        b_57.config(image=img_4)

    if ztext58[0] in text_main.get('1.741', '1.754'):
        b_58.config(image=img_0)

    if ztext58[1] in text_main.get('1.741', '1.754'):
        b_58.config(image=img_1)

    if ztext58[2] in text_main.get('1.741', '1.754'):
        b_58.config(image=img_2)

    if ztext58[3] in text_main.get('1.741', '1.754'):
        b_58.config(image=img_3)

    if ztext58[4] in text_main.get('1.741', '1.754'):
        b_58.config(image=img_4)

    if ztext59[0] in text_main.get('1.754', '1.767'):
        b_59.config(image=img_0)

    if ztext59[1] in text_main.get('1.754', '1.767'):
        b_59.config(image=img_1)

    if ztext59[2] in text_main.get('1.754', '1.767'):
        b_59.config(image=img_2)

    if ztext59[3] in text_main.get('1.754', '1.767'):
        b_59.config(image=img_3)

    if ztext59[4] in text_main.get('1.754', '1.767'):
        b_59.config(image=img_4)

    if ztext60[0] in text_main.get('1.767', '1.780'):
        b_60.config(image=img_0)

    if ztext60[1] in text_main.get('1.767', '1.780'):
        b_60.config(image=img_1)

    if ztext60[2] in text_main.get('1.767', '1.780'):
        b_60.config(image=img_2)

    if ztext60[3] in text_main.get('1.767', '1.780'):
        b_60.config(image=img_3)

    if ztext60[4] in text_main.get('1.767', '1.780'):
        b_60.config(image=img_4)

    if ztext61[0] in text_main.get('1.780', '1.793'):
        b_61.config(image=img_0)

    if ztext61[1] in text_main.get('1.780', '1.793'):
        b_61.config(image=img_1)

    if ztext61[2] in text_main.get('1.780', '1.793'):
        b_61.config(image=img_2)

    if ztext61[3] in text_main.get('1.780', '1.793'):
        b_61.config(image=img_3)

    if ztext61[4] in text_main.get('1.780', '1.793'):
        b_61.config(image=img_4)

    if ztext62[0] in text_main.get('1.793', '1.806'):
        b_62.config(image=img_0)

    if ztext62[1] in text_main.get('1.793', '1.806'):
        b_62.config(image=img_1)

    if ztext62[2] in text_main.get('1.793', '1.806'):
        b_62.config(image=img_2)

    if ztext62[3] in text_main.get('1.793', '1.806'):
        b_62.config(image=img_3)

    if ztext62[4] in text_main.get('1.793', '1.806'):
        b_62.config(image=img_4)

    if ztext63[0] in text_main.get('1.806', '1.819'):
        b_63.config(image=img_0)

    if ztext63[1] in text_main.get('1.806', '1.819'):
        b_63.config(image=img_1)

    if ztext63[2] in text_main.get('1.806', '1.819'):
        b_63.config(image=img_2)

    if ztext63[3] in text_main.get('1.806', '1.819'):
        b_63.config(image=img_3)

    if ztext63[4] in text_main.get('1.806', '1.819'):
        b_63.config(image=img_4)

    if ztext64[0] in text_main.get('1.819', '1.832'):
        b_64.config(image=img_0)

    if ztext64[1] in text_main.get('1.819', '1.832'):
        b_64.config(image=img_1)

    if ztext64[2] in text_main.get('1.819', '1.832'):
        b_64.config(image=img_2)

    if ztext64[3] in text_main.get('1.819', '1.832'):
        b_64.config(image=img_3)

    if ztext64[4] in text_main.get('1.819', '1.832'):
        b_64.config(image=img_4)

    if ztext65[0] in text_main.get('1.832', '1.845'):
        b_65.config(image=img_0)

    if ztext65[1] in text_main.get('1.832', '1.845'):
        b_65.config(image=img_1)

    if ztext65[2] in text_main.get('1.832', '1.845'):
        b_65.config(image=img_2)

    if ztext65[3] in text_main.get('1.832', '1.845'):
        b_65.config(image=img_3)

    if ztext65[4] in text_main.get('1.832', '1.845'):
        b_65.config(image=img_4)

    if ztext66[0] in text_main.get('1.845', '1.858'):
        b_66.config(image=img_0)

    if ztext66[1] in text_main.get('1.845', '1.858'):
        b_66.config(image=img_1)

    if ztext66[2] in text_main.get('1.845', '1.858'):
        b_66.config(image=img_2)

    if ztext66[3] in text_main.get('1.845', '1.858'):
        b_66.config(image=img_3)

    if ztext66[4] in text_main.get('1.845', '1.858'):
        b_66.config(image=img_4)

    if ztext67[0] in text_main.get('1.858', '1.871'):
        b_67.config(image=img_0)

    if ztext67[1] in text_main.get('1.858', '1.871'):
        b_67.config(image=img_1)

    if ztext67[2] in text_main.get('1.858', '1.871'):
        b_67.config(image=img_2)

    if ztext67[3] in text_main.get('1.858', '1.871'):
        b_67.config(image=img_3)

    if ztext67[4] in text_main.get('1.858', '1.871'):
        b_67.config(image=img_4)

    if ztext68[0] in text_main.get('1.871', '1.884'):
        b_68.config(image=img_0)

    if ztext68[1] in text_main.get('1.871', '1.884'):
        b_68.config(image=img_1)

    if ztext68[2] in text_main.get('1.871', '1.884'):
        b_68.config(image=img_2)

    if ztext68[3] in text_main.get('1.871', '1.884'):
        b_68.config(image=img_3)

    if ztext68[4] in text_main.get('1.871', '1.884'):
        b_68.config(image=img_4)

    if ztext69[0] in text_main.get('1.884', '1.897'):
        b_69.config(image=img_0)

    if ztext69[1] in text_main.get('1.884', '1.897'):
        b_69.config(image=img_1)

    if ztext69[2] in text_main.get('1.884', '1.897'):
        b_69.config(image=img_2)

    if ztext69[3] in text_main.get('1.884', '1.897'):
        b_69.config(image=img_3)

    if ztext69[4] in text_main.get('1.884', '1.897'):
        b_69.config(image=img_4)

    if ztext70[0] in text_main.get('1.897', '1.910'):
        b_70.config(image=img_0)

    if ztext70[1] in text_main.get('1.897', '1.910'):
        b_70.config(image=img_1)

    if ztext70[2] in text_main.get('1.897', '1.910'):
        b_70.config(image=img_2)

    if ztext70[3] in text_main.get('1.897', '1.910'):
        b_70.config(image=img_3)

    if ztext70[4] in text_main.get('1.897', '1.910'):
        b_70.config(image=img_4)

    if ztext71[0] in text_main.get('1.910', '1.923'):
        b_71.config(image=img_0)

    if ztext71[1] in text_main.get('1.910', '1.923'):
        b_71.config(image=img_1)

    if ztext71[2] in text_main.get('1.910', '1.923'):
        b_71.config(image=img_2)

    if ztext71[3] in text_main.get('1.910', '1.923'):
        b_71.config(image=img_3)

    if ztext71[4] in text_main.get('1.910', '1.923'):
        b_71.config(image=img_4)

    if ztext72[0] in text_main.get('1.923', '1.936'):
        b_72.config(image=img_0)

    if ztext72[1] in text_main.get('1.923', '1.936'):
        b_72.config(image=img_1)

    if ztext72[2] in text_main.get('1.923', '1.936'):
        b_72.config(image=img_2)

    if ztext72[3] in text_main.get('1.923', '1.936'):
        b_72.config(image=img_3)

    if ztext72[4] in text_main.get('1.923', '1.936'):
        b_72.config(image=img_4)

    if ztext73[0] in text_main.get('1.936', '1.949'):
        b_73.config(image=img_0)

    if ztext73[1] in text_main.get('1.936', '1.949'):
        b_73.config(image=img_1)

    if ztext73[2] in text_main.get('1.936', '1.949'):
        b_73.config(image=img_2)

    if ztext73[3] in text_main.get('1.936', '1.949'):
        b_73.config(image=img_3)

    if ztext73[4] in text_main.get('1.936', '1.949'):
        b_73.config(image=img_4)

    if ztext74[0] in text_main.get('1.949', '1.962'):
        b_74.config(image=img_0)

    if ztext74[1] in text_main.get('1.949', '1.962'):
        b_74.config(image=img_1)

    if ztext74[2] in text_main.get('1.949', '1.962'):
        b_74.config(image=img_2)

    if ztext74[3] in text_main.get('1.949', '1.962'):
        b_74.config(image=img_3)

    if ztext74[4] in text_main.get('1.949', '1.962'):
        b_74.config(image=img_4)

    if ztext75[0] in text_main.get('1.962', '1.975'):
        b_75.config(image=img_0)

    if ztext75[1] in text_main.get('1.962', '1.975'):
        b_75.config(image=img_1)

    if ztext75[2] in text_main.get('1.962', '1.975'):
        b_75.config(image=img_2)

    if ztext75[3] in text_main.get('1.962', '1.975'):
        b_75.config(image=img_3)

    if ztext75[4] in text_main.get('1.962', '1.975'):
        b_75.config(image=img_4)

    if ztext76[0] in text_main.get('1.975', '1.988'):
        b_76.config(image=img_0)

    if ztext76[1] in text_main.get('1.975', '1.988'):
        b_76.config(image=img_1)

    if ztext76[2] in text_main.get('1.975', '1.988'):
        b_76.config(image=img_2)

    if ztext76[3] in text_main.get('1.975', '1.988'):
        b_76.config(image=img_3)

    if ztext76[4] in text_main.get('1.975', '1.988'):
        b_76.config(image=img_4)

    if ztext77[0] in text_main.get('1.988', '1.1001'):
        b_77.config(image=img_0)

    if ztext77[1] in text_main.get('1.988', '1.1001'):
        b_77.config(image=img_1)

    if ztext77[2] in text_main.get('1.988', '1.1001'):
        b_77.config(image=img_2)

    if ztext77[3] in text_main.get('1.988', '1.1001'):
        b_77.config(image=img_3)

    if ztext77[4] in text_main.get('1.988', '1.1001'):
        b_77.config(image=img_4)

    if ztext78[0] in text_main.get('1.1001', '1.1014'):
        b_78.config(image=img_0)

    if ztext78[1] in text_main.get('1.1001', '1.1014'):
        b_78.config(image=img_1)

    if ztext78[2] in text_main.get('1.1001', '1.1014'):
        b_78.config(image=img_2)

    if ztext78[3] in text_main.get('1.1001', '1.1014'):
        b_78.config(image=img_3)

    if ztext78[4] in text_main.get('1.1001', '1.1014'):
        b_78.config(image=img_4)

    if ztext79[0] in text_main.get('1.1014', '1.1027'):
        b_79.config(image=img_0)

    if ztext79[1] in text_main.get('1.1014', '1.1027'):
        b_79.config(image=img_1)

    if ztext79[2] in text_main.get('1.1014', '1.1027'):
        b_79.config(image=img_2)

    if ztext79[3] in text_main.get('1.1014', '1.1027'):
        b_79.config(image=img_3)

    if ztext79[4] in text_main.get('1.1014', '1.1027'):
        b_79.config(image=img_4)

    if ztext80[0] in text_main.get('1.1027', '1.1040'):
        b_80.config(image=img_0)

    if ztext80[1] in text_main.get('1.1027', '1.1040'):
        b_80.config(image=img_1)

    if ztext80[2] in text_main.get('1.1027', '1.1040'):
        b_80.config(image=img_2)

    if ztext80[3] in text_main.get('1.1027', '1.1040'):
        b_80.config(image=img_3)

    if ztext80[4] in text_main.get('1.1027', '1.1040'):
        b_80.config(image=img_4)

    if ztext81[0] in text_main.get('1.1040', '1.1053'):
        b_81.config(image=img_0)

    if ztext81[1] in text_main.get('1.1040', '1.1053'):
        b_81.config(image=img_1)

    if ztext81[2] in text_main.get('1.1040', '1.1053'):
        b_81.config(image=img_2)

    if ztext81[3] in text_main.get('1.1040', '1.1053'):
        b_81.config(image=img_3)

    if ztext81[4] in text_main.get('1.1040', '1.1053'):
        b_81.config(image=img_4)

    if ztext82[0] in text_main.get('1.1053', '1.1066'):
        b_82.config(image=img_0)

    if ztext82[1] in text_main.get('1.1053', '1.1066'):
        b_82.config(image=img_1)

    if ztext82[2] in text_main.get('1.1053', '1.1066'):
        b_82.config(image=img_2)

    if ztext82[3] in text_main.get('1.1053', '1.1066'):
        b_82.config(image=img_3)

    if ztext82[4] in text_main.get('1.1053', '1.1066'):
        b_82.config(image=img_4)

    if ztext83[0] in text_main.get('1.1066', '1.1079'):
        b_83.config(image=img_0)

    if ztext83[1] in text_main.get('1.1066', '1.1079'):
        b_83.config(image=img_1)

    if ztext83[2] in text_main.get('1.1066', '1.1079'):
        b_83.config(image=img_2)

    if ztext83[3] in text_main.get('1.1066', '1.1079'):
        b_83.config(image=img_3)

    if ztext83[4] in text_main.get('1.1066', '1.1079'):
        b_83.config(image=img_4)

    if ztext84[0] in text_main.get('1.1079', '1.1092'):
        b_84.config(image=img_0)

    if ztext84[1] in text_main.get('1.1079', '1.1092'):
        b_84.config(image=img_1)

    if ztext84[2] in text_main.get('1.1079', '1.1092'):
        b_84.config(image=img_2)

    if ztext84[3] in text_main.get('1.1079', '1.1092'):
        b_84.config(image=img_3)

    if ztext84[4] in text_main.get('1.1079', '1.1092'):
        b_84.config(image=img_4)

    if ztext85[0] in text_main.get('1.1092', '1.1105'):
        b_85.config(image=img_0)

    if ztext85[1] in text_main.get('1.1092', '1.1105'):
        b_85.config(image=img_1)

    if ztext85[2] in text_main.get('1.1092', '1.1105'):
        b_85.config(image=img_2)

    if ztext85[3] in text_main.get('1.1092', '1.1105'):
        b_85.config(image=img_3)

    if ztext85[4] in text_main.get('1.1092', '1.1105'):
        b_85.config(image=img_4)

    if ztext86[0] in text_main.get('1.1105', '1.1118'):
        b_86.config(image=img_0)

    if ztext86[1] in text_main.get('1.1105', '1.1118'):
        b_86.config(image=img_1)

    if ztext86[2] in text_main.get('1.1105', '1.1118'):
        b_86.config(image=img_2)

    if ztext86[3] in text_main.get('1.1105', '1.1118'):
        b_86.config(image=img_3)

    if ztext86[4] in text_main.get('1.1105', '1.1118'):
        b_86.config(image=img_4)

    if ztext87[0] in text_main.get('1.1118', '1.1131'):
        b_87.config(image=img_0)

    if ztext87[1] in text_main.get('1.1118', '1.1131'):
        b_87.config(image=img_1)

    if ztext87[2] in text_main.get('1.1118', '1.1131'):
        b_87.config(image=img_2)

    if ztext87[3] in text_main.get('1.1118', '1.1131'):
        b_87.config(image=img_3)

    if ztext87[4] in text_main.get('1.1118', '1.1131'):
        b_87.config(image=img_4)

    if ztext88[0] in text_main.get('1.1131', '1.1144'):
        b_88.config(image=img_0)

    if ztext88[1] in text_main.get('1.1131', '1.1144'):
        b_88.config(image=img_1)

    if ztext88[2] in text_main.get('1.1131', '1.1144'):
        b_88.config(image=img_2)

    if ztext88[3] in text_main.get('1.1131', '1.1144'):
        b_88.config(image=img_3)

    if ztext88[4] in text_main.get('1.1131', '1.1144'):
        b_88.config(image=img_4)

    if ztext89[0] in text_main.get('1.1144', '1.1157'):
        b_89.config(image=img_0)

    if ztext89[1] in text_main.get('1.1144', '1.1157'):
        b_89.config(image=img_1)

    if ztext89[2] in text_main.get('1.1144', '1.1157'):
        b_89.config(image=img_2)

    if ztext89[3] in text_main.get('1.1144', '1.1157'):
        b_89.config(image=img_3)

    if ztext89[4] in text_main.get('1.1144', '1.1157'):
        b_89.config(image=img_4)

    if ztext90[0] in text_main.get('1.1157', '1.1170'):
        b_90.config(image=img_0)

    if ztext90[1] in text_main.get('1.1157', '1.1170'):
        b_90.config(image=img_1)

    if ztext90[2] in text_main.get('1.1157', '1.1170'):
        b_90.config(image=img_2)

    if ztext90[3] in text_main.get('1.1157', '1.1170'):
        b_90.config(image=img_3)

    if ztext90[4] in text_main.get('1.1157', '1.1170'):
        b_90.config(image=img_4)

    if ztext91[0] in text_main.get('1.1170', '1.1183'):
        b_91.config(image=img_0)

    if ztext91[1] in text_main.get('1.1170', '1.1183'):
        b_91.config(image=img_1)

    if ztext91[2] in text_main.get('1.1170', '1.1183'):
        b_91.config(image=img_2)

    if ztext91[3] in text_main.get('1.1170', '1.1183'):
        b_91.config(image=img_3)

    if ztext91[4] in text_main.get('1.1170', '1.1183'):
        b_91.config(image=img_4)

    if ztext92[0] in text_main.get('1.1183', '1.1196'):
        b_92.config(image=img_0)

    if ztext92[1] in text_main.get('1.1183', '1.1196'):
        b_92.config(image=img_1)

    if ztext92[2] in text_main.get('1.1183', '1.1196'):
        b_92.config(image=img_2)

    if ztext92[3] in text_main.get('1.1183', '1.1196'):
        b_92.config(image=img_3)

    if ztext92[4] in text_main.get('1.1183', '1.1196'):
        b_92.config(image=img_4)

    if ztext93[0] in text_main.get('1.1196', '1.1209'):
        b_93.config(image=img_0)

    if ztext93[1] in text_main.get('1.1196', '1.1209'):
        b_93.config(image=img_1)

    if ztext93[2] in text_main.get('1.1196', '1.1209'):
        b_93.config(image=img_2)

    if ztext93[3] in text_main.get('1.1196', '1.1209'):
        b_93.config(image=img_3)

    if ztext93[4] in text_main.get('1.1196', '1.1209'):
        b_93.config(image=img_4)

    if ztext94[0] in text_main.get('1.1209', '1.1222'):
        b_94.config(image=img_0)

    if ztext94[1] in text_main.get('1.1209', '1.1222'):
        b_94.config(image=img_1)

    if ztext94[2] in text_main.get('1.1209', '1.1222'):
        b_94.config(image=img_2)

    if ztext94[3] in text_main.get('1.1209', '1.1222'):
        b_94.config(image=img_3)

    if ztext94[4] in text_main.get('1.1209', '1.1222'):
        b_94.config(image=img_4)

    if ztext95[0] in text_main.get('1.1222', '1.1235'):
        b_95.config(image=img_0)

    if ztext95[1] in text_main.get('1.1222', '1.1235'):
        b_95.config(image=img_1)

    if ztext95[2] in text_main.get('1.1222', '1.1235'):
        b_95.config(image=img_2)

    if ztext95[3] in text_main.get('1.1222', '1.1235'):
        b_95.config(image=img_3)

    if ztext95[4] in text_main.get('1.1222', '1.1235'):
        b_95.config(image=img_4)

    if ztext96[0] in text_main.get('1.1235', '1.1248'):
        b_96.config(image=img_0)

    if ztext96[1] in text_main.get('1.1235', '1.1248'):
        b_96.config(image=img_1)

    if ztext96[2] in text_main.get('1.1235', '1.1248'):
        b_96.config(image=img_2)

    if ztext96[3] in text_main.get('1.1235', '1.1248'):
        b_96.config(image=img_3)

    if ztext96[4] in text_main.get('1.1235', '1.1248'):
        b_96.config(image=img_4)

    if ztext97[0] in text_main.get('1.1248', '1.1261'):
        b_97.config(image=img_0)

    if ztext97[1] in text_main.get('1.1248', '1.1261'):
        b_97.config(image=img_1)

    if ztext97[2] in text_main.get('1.1248', '1.1261'):
        b_97.config(image=img_2)

    if ztext97[3] in text_main.get('1.1248', '1.1261'):
        b_97.config(image=img_3)

    if ztext97[4] in text_main.get('1.1248', '1.1261'):
        b_97.config(image=img_4)

    if ztext98[0] in text_main.get('1.1261', '1.1274'):
        b_98.config(image=img_0)

    if ztext98[1] in text_main.get('1.1261', '1.1274'):
        b_98.config(image=img_1)

    if ztext98[2] in text_main.get('1.1261', '1.1274'):
        b_98.config(image=img_2)

    if ztext98[3] in text_main.get('1.1261', '1.1274'):
        b_98.config(image=img_3)

    if ztext98[4] in text_main.get('1.1261', '1.1274'):
        b_98.config(image=img_4)

    if ztext99[0] in text_main.get('1.1274', '1.1287'):
        b_99.config(image=img_0)

    if ztext99[1] in text_main.get('1.1274', '1.1287'):
        b_99.config(image=img_1)

    if ztext99[2] in text_main.get('1.1274', '1.1287'):
        b_99.config(image=img_2)

    if ztext99[3] in text_main.get('1.1274', '1.1287'):
        b_99.config(image=img_3)

    if ztext99[4] in text_main.get('1.1274', '1.1287'):
        b_99.config(image=img_4)

    if ztext100[0] in text_main.get('1.1287', '1.1300'):
        b_100.config(image=img_0)

    if ztext100[1] in text_main.get('1.1287', '1.1300'):
        b_100.config(image=img_1)

    if ztext100[2] in text_main.get('1.1287', '1.1300'):
        b_100.config(image=img_2)

    if ztext100[3] in text_main.get('1.1287', '1.1300'):
        b_100.config(image=img_3)

    if ztext100[4] in text_main.get('1.1287', '1.1300'):
        b_100.config(image=img_4)

def change():
    ztext1.clear()
    ztext1[0:5] = sq_8192[500:505]
    ##ent_1.insert(END,ztext1[0])

    ztext2.clear()
    ztext2[0:5] = sq_8192[505:510]
    ##ent_1.insert(END, ztext2[0])

    ztext3.clear()
    ztext3[0:5] = sq_8192[510:515]
    ##ent_1.insert(END, ztext3[0])

    ztext4.clear()
    ztext4[0:5] = sq_8192[515:520]
    #ent_1.insert(END, ztext4[0])

    ztext5.clear()
    ztext5[0:5] = sq_8192[520:525]
    #ent_1.insert(END, ztext5[0])

    ztext6.clear()
    ztext6[0:5] = sq_8192[525:530]
    #ent_1.insert(END, ztext6[0])

    ztext7.clear()
    ztext7[0:5] = sq_8192[530:535]
    #ent_1.insert(END, ztext7[0])

    ztext8.clear()
    ztext8[0:5] = sq_8192[535:540]
    #ent_1.insert(END, ztext8[0])

    ztext9.clear()
    ztext9[0:5] = sq_8192[540:545]
    #ent_1.insert(END, ztext9[0])

    ztext10.clear()
    ztext10[0:5] = sq_8192[545:550]
    #ent_1.insert(END, ztext10[0])

#row2
    #ent_2.delete(0,END)

    ztext11.clear()
    ztext11[0:5] = sq_8192[550:555]
    #ent_2.insert(END,ztext11[0])

    ztext12.clear()
    ztext12[0:5] = sq_8192[555:560]
    #ent_2.insert(END, ztext12[0])

    ztext13.clear()
    ztext13[0:5] = sq_8192[560:565]
    #ent_2.insert(END, ztext13[0])

    ztext14.clear()
    ztext14[0:5] = sq_8192[565:570]
    #ent_2.insert(END, ztext14[0])

    ztext15.clear()
    ztext15[0:5] = sq_8192[570:575]
    #ent_2.insert(END, ztext15[0])

    ztext16.clear()
    ztext16[0:5] = sq_8192[575:580]
    #ent_2.insert(END, ztext16[0])

    ztext17.clear()
    ztext17[0:5] = sq_8192[580:585]
    #ent_2.insert(END, ztext17[0])

    ztext18.clear()
    ztext18[0:5] = sq_8192[585:590]
    #ent_2.insert(END, ztext18[0])

    ztext19.clear()
    ztext19[0:5] = sq_8192[590:595]
    #ent_2.insert(END, ztext19[0])

    ztext20.clear()
    ztext20[0:5] = sq_8192[595:600]
    #ent_2.insert(END, ztext20[0])

    #ent_3.delete(0,END)

    ztext21.clear()
    ztext21[0:5] = sq_8192[600:605]
    #ent_3.insert(END,ztext21[0])

    ztext22.clear()
    ztext22[0:5] = sq_8192[605:610]
    #ent_3.insert(END, ztext22[0])

    ztext23.clear()
    ztext23[0:5] = sq_8192[610:615]
    #ent_3.insert(END, ztext23[0])

    ztext24.clear()
    ztext24[0:5] = sq_8192[615:620]
    #ent_3.insert(END, ztext24[0])

    ztext25.clear()
    ztext25[0:5] = sq_8192[620:625]
    #ent_3.insert(END, ztext25[0])

    ztext26.clear()
    ztext26[0:5] = sq_8192[625:630]
    #ent_3.insert(END, ztext26[0])

    ztext27.clear()
    ztext27[0:5] = sq_8192[630:635]
    #ent_3.insert(END, ztext27[0])

    ztext28.clear()
    ztext28[0:5] = sq_8192[635:640]
    #ent_3.insert(END, ztext28[0])

    ztext29.clear()
    ztext29[0:5] = sq_8192[640:645]
    #ent_3.insert(END, ztext29[0])

    ztext30.clear()
    ztext30[0:5] = sq_8192[645:650]
    #ent_3.insert(END, ztext30[0])

    #ent_4.delete(0,END)

    ztext31.clear()
    ztext31[0:5] = sq_8192[650:655]
    #ent_4.insert(END,ztext31[0])

    ztext32.clear()
    ztext32[0:5] = sq_8192[655:660]
    #ent_4.insert(END, ztext32[0])

    ztext33.clear()
    ztext33[0:5] = sq_8192[660:665]
    #ent_4.insert(END, ztext33[0])

    ztext34.clear()
    ztext34[0:5] = sq_8192[665:670]
    #ent_4.insert(END, ztext34[0])

    ztext35.clear()
    ztext35[0:5] = sq_8192[670:675]
    #ent_4.insert(END, ztext35[0])

    ztext36.clear()
    ztext36[0:5] = sq_8192[675:680]
    #ent_4.insert(END, ztext36[0])

    ztext37.clear()
    ztext37[0:5] = sq_8192[680:685]
    #ent_4.insert(END, ztext37[0])

    ztext38.clear()
    ztext38[0:5] = sq_8192[685:690]
    #ent_4.insert(END, ztext38[0])

    ztext39.clear()
    ztext39[0:5] = sq_8192[690:695]
    #ent_4.insert(END, ztext39[0])

    ztext40.clear()
    ztext40[0:5] = sq_8192[695:700]
    #ent_4.insert(END, ztext40[0])

    #ent_5.delete(0,END)

    ztext41.clear()
    ztext41[0:5] = sq_8192[700:705]
    #ent_5.insert(END,ztext41[0])

    ztext42.clear()
    ztext42[0:5] = sq_8192[705:710]
    #ent_5.insert(END, ztext42[0])

    ztext43.clear()
    ztext43[0:5] = sq_8192[710:715]
    #ent_5.insert(END, ztext43[0])

    ztext44.clear()
    ztext44[0:5] = sq_8192[715:720]
    #ent_5.insert(END, ztext44[0])

    ztext45.clear()
    ztext45[0:5] = sq_8192[720:725]
    #ent_5.insert(END, ztext45[0])

    ztext46.clear()
    ztext46[0:5] = sq_8192[725:730]
    #ent_5.insert(END, ztext46[0])

    ztext47.clear()
    ztext47[0:5] = sq_8192[730:735]
    #ent_5.insert(END, ztext47[0])

    ztext48.clear()
    ztext48[0:5] = sq_8192[735:740]
    #ent_5.insert(END, ztext48[0])

    ztext49.clear()
    ztext49[0:5] = sq_8192[740:745]
    #ent_5.insert(END, ztext49[0])

    ztext50.clear()
    ztext50[0:5] = sq_8192[745:750]
    #ent_5.insert(END, ztext50[0])

    #ent_6.delete(0,END)

    ztext51.clear()
    ztext51[0:5] = sq_8192[750:755]
    #ent_6.insert(END,ztext51[0])

    ztext52.clear()
    ztext52[0:5] = sq_8192[755:760]
    #ent_6.insert(END, ztext52[0])

    ztext53.clear()
    ztext53[0:5] = sq_8192[760:765]
    #ent_6.insert(END, ztext53[0])

    ztext54.clear()
    ztext54[0:5] = sq_8192[765:770]
    #ent_6.insert(END, ztext54[0])

    ztext55.clear()
    ztext55[0:5] = sq_8192[770:775]
    #ent_6.insert(END, ztext55[0])

    ztext56.clear()
    ztext56[0:5] = sq_8192[775:780]
    #ent_6.insert(END, ztext56[0])

    ztext57.clear()
    ztext57[0:5] = sq_8192[780:785]
    #ent_6.insert(END, ztext57[0])

    ztext58.clear()
    ztext58[0:5] = sq_8192[785:790]
    #ent_6.insert(END, ztext58[0])

    ztext59.clear()
    ztext59[0:5] = sq_8192[790:795]
    #ent_6.insert(END, ztext59[0])

    ztext60.clear()
    ztext60[0:5] = sq_8192[795:800]
    #ent_6.insert(END, ztext60[0])

    #ent_7.delete(0,END)

    ztext61.clear()
    ztext61[0:5] = sq_8192[800:805]
    #ent_7.insert(END,ztext61[0])

    ztext62.clear()
    ztext62[0:5] = sq_8192[805:810]
    #ent_7.insert(END, ztext62[0])

    ztext63.clear()
    ztext63[0:5] = sq_8192[810:815]
    #ent_7.insert(END, ztext63[0])

    ztext64.clear()
    ztext64[0:5] = sq_8192[815:820]
    #ent_7.insert(END, ztext64[0])

    ztext65.clear()
    ztext65[0:5] = sq_8192[820:825]
    #ent_7.insert(END, ztext65[0])

    ztext66.clear()
    ztext66[0:5] = sq_8192[825:830]
    #ent_7.insert(END, ztext66[0])

    ztext67.clear()
    ztext67[0:5] = sq_8192[830:835]
    #ent_7.insert(END, ztext67[0])

    ztext68.clear()
    ztext68[0:5] = sq_8192[835:840]
    #ent_7.insert(END, ztext68[0])

    ztext69.clear()
    ztext69[0:5] = sq_8192[840:845]
    #ent_7.insert(END, ztext69[0])

    ztext70.clear()
    ztext70[0:5] = sq_8192[845:850]
    #ent_7.insert(END, ztext70[0])

    #ent_8.delete(0,END)

    ztext71.clear()
    ztext71[0:5] = sq_8192[850:855]
    #ent_8.insert(END,ztext71[0])

    ztext72.clear()
    ztext72[0:5] = sq_8192[855:860]
    #ent_8.insert(END, ztext72[0])

    ztext73.clear()
    ztext73[0:5] = sq_8192[860:865]
    #ent_8.insert(END, ztext73[0])

    ztext74.clear()
    ztext74[0:5] = sq_8192[865:870]
    #ent_8.insert(END, ztext74[0])

    ztext75.clear()
    ztext75[0:5] = sq_8192[870:875]
    #ent_8.insert(END, ztext75[0])

    ztext76.clear()
    ztext76[0:5] = sq_8192[875:880]
    #ent_8.insert(END, ztext76[0])

    ztext77.clear()
    ztext77[0:5] = sq_8192[880:885]
    #ent_8.insert(END, ztext77[0])

    ztext78.clear()
    ztext78[0:5] = sq_8192[885:890]
    #ent_8.insert(END, ztext78[0])

    ztext79.clear()
    ztext79[0:5] = sq_8192[890:895]
    #ent_8.insert(END, ztext79[0])

    ztext80.clear()
    ztext80[0:5] = sq_8192[895:900]
    #ent_8.insert(END, ztext80[0])

    #ent_9.delete(0,END)

    ztext81.clear()
    ztext81[0:5] = sq_8192[900:905]
    #ent_9.insert(END,ztext81[0])

    ztext82.clear()
    ztext82[0:5] = sq_8192[905:910]
    #ent_9.insert(END, ztext82[0])

    ztext83.clear()
    ztext83[0:5] = sq_8192[910:915]
    #ent_9.insert(END, ztext83[0])

    ztext84.clear()
    ztext84[0:5] = sq_8192[915:920]
    #ent_9.insert(END, ztext84[0])

    ztext85.clear()
    ztext85[0:5] = sq_8192[920:925]
    #ent_9.insert(END, ztext85[0])

    ztext86.clear()
    ztext86[0:5] = sq_8192[925:930]
    #ent_9.insert(END, ztext86[0])

    ztext87.clear()
    ztext87[0:5] = sq_8192[930:935]
    #ent_9.insert(END, ztext87[0])

    ztext88.clear()
    ztext88[0:5] = sq_8192[935:940]
    #ent_9.insert(END, ztext88[0])

    ztext89.clear()
    ztext89[0:5] = sq_8192[940:945]
    #ent_9.insert(END, ztext89[0])

    ztext90.clear()
    ztext90[0:5] = sq_8192[945:950]
    #ent_9.insert(END, ztext90[0])

    #ent_10.delete(0,END)

    ztext91.clear()
    ztext91[0:5] = sq_8192[950:955]
    #ent_10.insert(END,ztext91[0])

    ztext92.clear()
    ztext92[0:5] = sq_8192[955:960]
    #ent_10.insert(END, ztext92[0])

    ztext93.clear()
    ztext93[0:5] = sq_8192[960:965]
    #ent_10.insert(END, ztext93[0])

    ztext94.clear()
    ztext94[0:5] = sq_8192[965:970]
    #ent_10.insert(END, ztext94[0])

    ztext95.clear()
    ztext95[0:5] = sq_8192[970:975]
    #ent_10.insert(END, ztext95[0])

    ztext96.clear()
    ztext96[0:5] = sq_8192[975:980]
    #ent_10.insert(END, ztext96[0])

    ztext97.clear()
    ztext97[0:5] = sq_8192[980:985]
    #ent_10.insert(END, ztext97[0])

    ztext98.clear()
    ztext98[0:5] = sq_8192[985:990]
    #ent_10.insert(END, ztext98[0])

    ztext99.clear()
    ztext99[0:5] = sq_8192[990:995]
    #ent_10.insert(END, ztext99[0])

    ztext100.clear()
    ztext100[0:5] = sq_8192[995:1000]

    del sq_8192[500:1000]
    print(len(sq_8192))

# frame for getting text and showing it_____________________________________________________________________________

tog_frame = Frame(root)
tog_frame.grid(row=10, column=0, sticky=E, rowspan=10)

top_frame = Frame(root, bg='black')
top_frame.grid(row=0, column=1, rowspan=10, padx=10)

text_button = Button(top_frame, text='Open text Window', bg = 'black', fg= 'green',command=new_window)
text_button.grid(row=0, column=0, pady=3)

text_button1 = Button(top_frame, text='(scroll)', bg = 'black', fg= 'green',command=get_entry_text)
text_button1.grid(row=1, column=0, pady=3)

show_but1 = Button(top_frame, text='Show pic!', bg = 'black', fg= 'green',command=show_pic1)
show_but1.grid(row=2, column=0, pady=1)

#lab_1 = Label(top_frame, text = '')
#lab_1.grid(row=3, column=0, pady=3)

guess_lab = Button(top_frame, text='500 change', command = change)
guess_lab.grid(row=12, column=0, pady=3)

guess_ent = Entry(top_frame)
guess_ent.grid(row=13, column=0, pady=3)

#guess_but = Button(top_frame, text='choose letter', command=choice_code)
#guess_but.grid(row=14, column=0, pady=3)
# __________________________________________________________________________________________
txt_box = Text(root, width=25, bg='black', fg='green')
txt_box.grid(row=10, column=1, pady=10, padx=10, rowspan=10)
# __________________________________________________________________________________________


#ent_1 = Entry(root, bg='black', fg='green', width=130)
#ent_1.grid(row=0, column=0, pady=4)>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>!
text_main = Text(root, width = 130, height = 16, bg = 'black', fg= 'green')
text_main.grid(row = 0, column = 0, pady =4)

but_frame = Frame(root)
but_frame.grid(row=10, column=0, sticky=W)

b_1 = Button(but_frame, image=img_0)
b_1.grid(row=0, column=0)

b_2 = Button(but_frame, image=img_0)
b_2.grid(row=0, column=1)

b_3 = Button(but_frame, image=img_0)
b_3.grid(row=0, column=2)

b_4 = Button(but_frame, image=img_0)
b_4.grid(row=0, column=3)

b_5 = Button(but_frame, image=img_0)
b_5.grid(row=0, column=4)

b_6 = Button(but_frame, image=img_0)
b_6.grid(row=0, column=5)

b_7 = Button(but_frame, image=img_0)
b_7.grid(row=0, column=6)

b_8 = Button(but_frame, image=img_0)
b_8.grid(row=0, column=7)

b_9 = Button(but_frame, image=img_0)
b_9.grid(row=0, column=8)

b_10 = Button(but_frame, image=img_0)
b_10.grid(row=0, column=9)

# 10

b_11 = Button(but_frame, image=img_0)
b_11.grid(row=1, column=0)

b_12 = Button(but_frame, image=img_0)
b_12.grid(row=1, column=1)

b_13 = Button(but_frame, image=img_0)
b_13.grid(row=1, column=2)

b_14 = Button(but_frame, image=img_0)
b_14.grid(row=1, column=3)

b_15 = Button(but_frame, image=img_0)
b_15.grid(row=1, column=4)

b_16 = Button(but_frame, image=img_0)
b_16.grid(row=1, column=5)

b_17 = Button(but_frame, image=img_0)
b_17.grid(row=1, column=6)

b_18 = Button(but_frame, image=img_0)
b_18.grid(row=1, column=7)

b_19 = Button(but_frame, image=img_0)
b_19.grid(row=1, column=8)

b_20 = Button(but_frame, image=img_0)
b_20.grid(row=1, column=9)

# 20

b_21 = Button(but_frame, image=img_0)
b_21.grid(row=2, column=0)

b_22 = Button(but_frame, image=img_0)
b_22.grid(row=2, column=1)

b_23 = Button(but_frame, image=img_0)
b_23.grid(row=2, column=2)

b_24 = Button(but_frame, image=img_0)
b_24.grid(row=2, column=3)

b_25 = Button(but_frame, image=img_0)
b_25.grid(row=2, column=4)

b_26 = Button(but_frame, image=img_0)
b_26.grid(row=2, column=5)

b_27 = Button(but_frame, image=img_0)
b_27.grid(row=2, column=6)

b_28 = Button(but_frame, image=img_0)
b_28.grid(row=2, column=7)

b_29 = Button(but_frame, image=img_0)
b_29.grid(row=2, column=8)

b_30 = Button(but_frame, image=img_0)
b_30.grid(row=2, column=9)

# 30

b_31 = Button(but_frame, image=img_0)
b_31.grid(row=3, column=0)

b_32 = Button(but_frame, image=img_0)
b_32.grid(row=3, column=1)

b_33 = Button(but_frame, image=img_0)
b_33.grid(row=3, column=2)

b_34 = Button(but_frame, image=img_0)
b_34.grid(row=3, column=3)

b_35 = Button(but_frame, image=img_0)
b_35.grid(row=3, column=4)

b_36 = Button(but_frame, image=img_0)
b_36.grid(row=3, column=5)

b_37 = Button(but_frame, image=img_0)
b_37.grid(row=3, column=6)

b_38 = Button(but_frame, image=img_0)
b_38.grid(row=3, column=7)

b_39 = Button(but_frame, image=img_0)
b_39.grid(row=3, column=8)

b_40 = Button(but_frame, image=img_0)
b_40.grid(row=3, column=9)

# 40

b_41 = Button(but_frame, image=img_0)
b_41.grid(row=4, column=0)

b_42 = Button(but_frame, image=img_0)
b_42.grid(row=4, column=1)

b_43 = Button(but_frame, image=img_0)
b_43.grid(row=4, column=2)

b_44 = Button(but_frame, image=img_0)
b_44.grid(row=4, column=3)

b_45 = Button(but_frame, image=img_0)
b_45.grid(row=4, column=4)

b_46 = Button(but_frame, image=img_0)
b_46.grid(row=4, column=5)

b_47 = Button(but_frame, image=img_0)
b_47.grid(row=4, column=6)

b_48 = Button(but_frame, image=img_0)
b_48.grid(row=4, column=7)

b_49 = Button(but_frame, image=img_0)
b_49.grid(row=4, column=8)

b_50 = Button(but_frame, image=img_0)
b_50.grid(row=4, column=9)

# 50

b_51 = Button(but_frame, image=img_0)
b_51.grid(row=5, column=0)

b_52 = Button(but_frame, image=img_0)
b_52.grid(row=5, column=1)

b_53 = Button(but_frame, image=img_0)
b_53.grid(row=5, column=2)

b_54 = Button(but_frame, image=img_0)
b_54.grid(row=5, column=3)

b_55 = Button(but_frame, image=img_0)
b_55.grid(row=5, column=4)

b_56 = Button(but_frame, image=img_0)
b_56.grid(row=5, column=5)

b_57 = Button(but_frame, image=img_0)
b_57.grid(row=5, column=6)

b_58 = Button(but_frame, image=img_0)
b_58.grid(row=5, column=7)

b_59 = Button(but_frame, image=img_0)
b_59.grid(row=5, column=8)

b_60 = Button(but_frame, image=img_0)
b_60.grid(row=5, column=9)

# 60

b_61 = Button(but_frame, image=img_0)
b_61.grid(row=6, column=0)

b_62 = Button(but_frame, image=img_0)
b_62.grid(row=6, column=1)

b_63 = Button(but_frame, image=img_0)
b_63.grid(row=6, column=2)

b_64 = Button(but_frame, image=img_0)
b_64.grid(row=6, column=3)

b_65 = Button(but_frame, image=img_0)
b_65.grid(row=6, column=4)

b_66 = Button(but_frame, image=img_0)
b_66.grid(row=6, column=5)

b_67 = Button(but_frame, image=img_0)
b_67.grid(row=6, column=6)

b_68 = Button(but_frame, image=img_0)
b_68.grid(row=6, column=7)

b_69 = Button(but_frame, image=img_0)
b_69.grid(row=6, column=8)

b_70 = Button(but_frame, image=img_0)
b_70.grid(row=6, column=9)

# 70

b_71 = Button(but_frame, image=img_0)
b_71.grid(row=7, column=0)

b_72 = Button(but_frame, image=img_0)
b_72.grid(row=7, column=1)

b_73 = Button(but_frame, image=img_0)
b_73.grid(row=7, column=2)

b_74 = Button(but_frame, image=img_0)
b_74.grid(row=7, column=3)

b_75 = Button(but_frame, image=img_0)
b_75.grid(row=7, column=4)

b_76 = Button(but_frame, image=img_0)
b_76.grid(row=7, column=5)

b_77 = Button(but_frame, image=img_0)
b_77.grid(row=7, column=6)

b_78 = Button(but_frame, image=img_0)
b_78.grid(row=7, column=7)

b_79 = Button(but_frame, image=img_0)
b_79.grid(row=7, column=8)

b_80 = Button(but_frame, image=img_0)
b_80.grid(row=7, column=9)

# 80

b_81 = Button(but_frame, image=img_0)
b_81.grid(row=8, column=0)

b_82 = Button(but_frame, image=img_0)
b_82.grid(row=8, column=1)

b_83 = Button(but_frame, image=img_0)
b_83.grid(row=8, column=2)

b_84 = Button(but_frame, image=img_0)
b_84.grid(row=8, column=3)

b_85 = Button(but_frame, image=img_0)
b_85.grid(row=8, column=4)

b_86 = Button(but_frame, image=img_0)
b_86.grid(row=8, column=5)

b_87 = Button(but_frame, image=img_0)
b_87.grid(row=8, column=6)

b_88 = Button(but_frame, image=img_0)
b_88.grid(row=8, column=7)

b_89 = Button(but_frame, image=img_0)
b_89.grid(row=8, column=8)

b_90 = Button(but_frame, image=img_0)
b_90.grid(row=8, column=9)

# 90

b_91 = Button(but_frame, image=img_0)
b_91.grid(row=9, column=0)

b_92 = Button(but_frame, image=img_0)
b_92.grid(row=9, column=1)

b_93 = Button(but_frame, image=img_0)
b_93.grid(row=9, column=2)

b_94 = Button(but_frame, image=img_0)
b_94.grid(row=9, column=3)

b_95 = Button(but_frame, image=img_0)
b_95.grid(row=9, column=4)

b_96 = Button(but_frame, image=img_0)
b_96.grid(row=9, column=5)

b_97 = Button(but_frame, image=img_0)
b_97.grid(row=9, column=6)

b_98 = Button(but_frame, image=img_0)
b_98.grid(row=9, column=7)

b_99 = Button(but_frame, image=img_0)
b_99.grid(row=9, column=8)

b_100 = Button(but_frame, image=img_0)
b_100.grid(row=9, column=9)

# buttons a2z

t_1 = Button(tog_frame, text='a', bg='black', fg='green', command=t1)
t_1.grid(row=0, column=0, padx=2)

t_2 = Button(tog_frame, text='A', bg='black', fg='green', command=t2)
t_2.grid(row=0, column=1, padx=2)

t_3 = Button(tog_frame, text='ä', bg='black', fg='green', command=t3)
t_3.grid(row=0, column=2, padx=2)

t_4 = Button(tog_frame, text='Ä', bg='black', fg='green', command=t4)
t_4.grid(row=0, column=3, padx=2)

t_5 = Button(tog_frame, text='b', bg='black', fg='green', command=t5)
t_5.grid(row=0, column=4, padx=2)

t_6 = Button(tog_frame, text='B', bg='black', fg='green', command=t6)
t_6.grid(row=0, column=5, padx=2)

t_7 = Button(tog_frame, text='c', bg='black', fg='green', command=t7)
t_7.grid(row=0, column=6, padx=2)

t_8 = Button(tog_frame, text='C', bg='black', fg='green', command=t8)
t_8.grid(row=0, column=7, padx=2)

t_9 = Button(tog_frame, text='d', bg='black', fg='green', command=t9)
t_9.grid(row=0, column=8, padx=2)

t_10 = Button(tog_frame, text='D', bg='black', fg='green', command=t10)
t_10.grid(row=0, column=9, padx=2)

# 10

t_11 = Button(tog_frame, text='e', bg='black', fg='green', command=t11)
t_11.grid(row=1, column=0)

t_12 = Button(tog_frame, text='E', bg='black', fg='green', command=t12)
t_12.grid(row=1, column=1)

t_13 = Button(tog_frame, text='f', bg='black', fg='green', command=t13)
t_13.grid(row=1, column=2)

t_14 = Button(tog_frame, text='F', bg='black', fg='green', command=t14)
t_14.grid(row=1, column=3)

t_15 = Button(tog_frame, text='g', bg='black', fg='green', command=t15)
t_15.grid(row=1, column=4)

t_16 = Button(tog_frame, text='G', bg='black', fg='green', command=t16)
t_16.grid(row=1, column=5)

t_17 = Button(tog_frame, text='h', bg='black', fg='green', command=t17)
t_17.grid(row=1, column=6)

t_18 = Button(tog_frame, text='H', bg='black', fg='green', command=t18)
t_18.grid(row=1, column=7)

t_19 = Button(tog_frame, text='i', bg='black', fg='green', command=t19)
t_19.grid(row=1, column=8)

t_20 = Button(tog_frame, text='I', bg='black', fg='green', command=t20)
t_20.grid(row=1, column=9)

# 20

t_21 = Button(tog_frame, text='j', bg='black', fg='green', command=t21)
t_21.grid(row=2, column=0)

t_22 = Button(tog_frame, text='J', bg='black', fg='green', command=t22)
t_22.grid(row=2, column=1)

t_23 = Button(tog_frame, text='k', bg='black', fg='green', command=t23)
t_23.grid(row=2, column=2)

t_24 = Button(tog_frame, text='K', bg='black', fg='green', command=t24)
t_24.grid(row=2, column=3)

t_25 = Button(tog_frame, text='l', bg='black', fg='green', command=t25)
t_25.grid(row=2, column=4)

t_26 = Button(tog_frame, text='L', bg='black', fg='green', command=t26)
t_26.grid(row=2, column=5)

t_27 = Button(tog_frame, text='m', bg='black', fg='green', command=t27)
t_27.grid(row=2, column=6)

t_28 = Button(tog_frame, text='M', bg='black', fg='green', command=t28)
t_28.grid(row=2, column=7)

t_29 = Button(tog_frame, text='n', bg='black', fg='green', command=t29)
t_29.grid(row=2, column=8)

t_30 = Button(tog_frame, text='N', bg='black', fg='green', command=t30)
t_30.grid(row=2, column=9)

# 30

t_31 = Button(tog_frame, text='o', bg='black', fg='green', command=t31)
t_31.grid(row=3, column=0)

t_32 = Button(tog_frame, text='O', bg='black', fg='green', command=t32)
t_32.grid(row=3, column=1)

t_33 = Button(tog_frame, text='ö', bg='black', fg='green', command=t33)
t_33.grid(row=3, column=2)

t_34 = Button(tog_frame, text='Ö', bg='black', fg='green', command=t34)
t_34.grid(row=3, column=3)

t_35 = Button(tog_frame, text='p', bg='black', fg='green', command=t35)
t_35.grid(row=3, column=4)

t_36 = Button(tog_frame, text='P', bg='black', fg='green', command=t36)
t_36.grid(row=3, column=5)

t_37 = Button(tog_frame, text='q', bg='black', fg='green', command=t37)
t_37.grid(row=3, column=6)

t_38 = Button(tog_frame, text='Q', bg='black', fg='green', command=t38)
t_38.grid(row=3, column=7)

t_39 = Button(tog_frame, text='r', bg='black', fg='green', command=t39)
t_39.grid(row=3, column=8)

t_40 = Button(tog_frame, text='R', bg='black', fg='green', command=t40)
t_40.grid(row=3, column=9)

# 40

t_41 = Button(tog_frame, text='s', bg='black', fg='green', command=t41)
t_41.grid(row=4, column=0)

t_42 = Button(tog_frame, text='S', bg='black', fg='green', command=t42)
t_42.grid(row=4, column=1)

t_43 = Button(tog_frame, text='t', bg='black', fg='green', command=t43)
t_43.grid(row=4, column=2)

t_44 = Button(tog_frame, text='T', bg='black', fg='green', command=t44)
t_44.grid(row=4, column=3)

t_45 = Button(tog_frame, text='u', bg='black', fg='green', command=t45)
t_45.grid(row=4, column=4)

t_46 = Button(tog_frame, text='U', bg='black', fg='green', command=t46)
t_46.grid(row=4, column=5)

t_47 = Button(tog_frame, text='ü', bg='black', fg='green', command=t47)
t_47.grid(row=4, column=6)

t_48 = Button(tog_frame, text='Ü', bg='black', fg='green', command=t48)
t_48.grid(row=4, column=7)

t_49 = Button(tog_frame, text='v', bg='black', fg='green', command=t49)
t_49.grid(row=4, column=8)

t_50 = Button(tog_frame, text='V', bg='black', fg='green', command=t50)
t_50.grid(row=4, column=9)

# 50

t_51 = Button(tog_frame, text='w', bg='black', fg='green', command=t51)
t_51.grid(row=5, column=0)

t_52 = Button(tog_frame, text='W', bg='black', fg='green', command=t52)
t_52.grid(row=5, column=1)

t_53 = Button(tog_frame, text='x', bg='black', fg='green', command=t53)
t_53.grid(row=5, column=2)

t_54 = Button(tog_frame, text='X', bg='black', fg='green', command=t54)
t_54.grid(row=5, column=3)

t_55 = Button(tog_frame, text='y', bg='black', fg='green', command=t55)
t_55.grid(row=5, column=4)

t_56 = Button(tog_frame, text='Y', bg='black', fg='green', command=t56)
t_56.grid(row=5, column=5)

t_57 = Button(tog_frame, text='z', bg='black', fg='green', command=t57)
t_57.grid(row=5, column=6)

t_58 = Button(tog_frame, text='Z', bg='black', fg='green', command=t58)
t_58.grid(row=5, column=7)

t_59 = Button(tog_frame, text='!', bg='black', fg='green', command=t59)
t_59.grid(row=5, column=8)

t_60 = Button(tog_frame, text='"', bg='black', fg='green', command=t60)
t_60.grid(row=5, column=9)

# 60,'?','ß','backsl.',',',';',':','.','_','-','#','+','*',"''",'>','<','|','~', 'space']


t_61 = Button(tog_frame, text='$', bg='black', fg='green', command=t61)
t_61.grid(row=6, column=0)

t_62 = Button(tog_frame, text='%', bg='black', fg='green', command=t62)
t_62.grid(row=6, column=1)

t_63 = Button(tog_frame, text='&', bg='black', fg='green', command=t63)
t_63.grid(row=6, column=2)

t_64 = Button(tog_frame, text='/', bg='black', fg='green', command=t64)
t_64.grid(row=6, column=3)

t_65 = Button(tog_frame, text='{', bg='black', fg='green', command=t65)
t_65.grid(row=6, column=4)

t_66 = Button(tog_frame, text='(', bg='black', fg='green', command=t66)
t_66.grid(row=6, column=5)

t_67 = Button(tog_frame, text='[', bg='black', fg='green', command=t67)
t_67.grid(row=6, column=6)

t_68 = Button(tog_frame, text=')', bg='black', fg='green', command=t68)
t_68.grid(row=6, column=7)

t_69 = Button(tog_frame, text=']', bg='black', fg='green', command=t69)
t_69.grid(row=6, column=8)

t_70 = Button(tog_frame, text='=', bg='black', fg='green', command=t70)
t_70.grid(row=6, column=9)

# 70'?','ß','backsl.',',',';',':','.','_','-',

t_71 = Button(tog_frame, text='}', bg='black', fg='green', command=t71)
t_71.grid(row=7, column=0)

t_72 = Button(tog_frame, text='?', bg='black', fg='green', command=t72)
t_72.grid(row=7, column=1)

t_73 = Button(tog_frame, text='ß', bg='black', fg='green', command=t73)
t_73.grid(row=7, column=2)

t_74 = Button(tog_frame, text='\\', bg='black', fg='green', command=t74)
t_74.grid(row=7, column=3)

t_75 = Button(tog_frame, text=',', bg='black', fg='green', command=t75)
t_75.grid(row=7, column=4)

t_76 = Button(tog_frame, text=';', bg='black', fg='green', command=t76)
t_76.grid(row=7, column=5)

t_77 = Button(tog_frame, text=':', bg='black', fg='green', command=t77)
t_77.grid(row=7, column=6)

t_78 = Button(tog_frame, text='.', bg='black', fg='green', command=t78)
t_78.grid(row=7, column=7)

t_79 = Button(tog_frame, text='_', bg='black', fg='green', command=t79)
t_79.grid(row=7, column=8)

t_80 = Button(tog_frame, text='-', bg='black', fg='green', command=t80)
t_80.grid(row=7, column=9)

# 80'#','+','*',"''",'>','<','|','~', 'space']

t_81 = Button(tog_frame, text='#', bg='black', fg='green', command=t81)
t_81.grid(row=8, column=0)

t_82 = Button(tog_frame, text='+', bg='black', fg='green', command=t82)
t_82.grid(row=8, column=1)

t_83 = Button(tog_frame, text='*', bg='black', fg='green', command=t83)
t_83.grid(row=8, column=2)

t_84 = Button(tog_frame, text="'", bg='black', fg='green', command=t84)
t_84.grid(row=8, column=3)

t_85 = Button(tog_frame, text='<', bg='black', fg='green', command=t85)
t_85.grid(row=8, column=4)

t_86 = Button(tog_frame, text='>', bg='black', fg='green', command=t86)
t_86.grid(row=8, column=5)

t_87 = Button(tog_frame, text='|', bg='black', fg='green', command=t87)
t_87.grid(row=8, column=6)

t_88 = Button(tog_frame, text='~', bg='black', fg='green', command=t88)
t_88.grid(row=8, column=7)

t_89 = Button(tog_frame, text='s.b', bg='black', fg='green', command=t89)
t_89.grid(row=8, column=8)

t_90 = Button(tog_frame, text='0', bg='black', fg='green', command=t90)
t_90.grid(row=8, column=9)

# 90

t_91 = Button(tog_frame, text='1', bg='black', fg='green', command=t91)
t_91.grid(row=9, column=0)

t_92 = Button(tog_frame, text='2', bg='black', fg='green', command=t92)
t_92.grid(row=9, column=1)

t_93 = Button(tog_frame, text='3', bg='black', fg='green', command=t93)
t_93.grid(row=9, column=2)

t_94 = Button(tog_frame, text='4', bg='black', fg='green', command=t94)
t_94.grid(row=9, column=3)

t_95 = Button(tog_frame, text='5', bg='black', fg='green', command=t95)
t_95.grid(row=9, column=4)

t_96 = Button(tog_frame, text='6', bg='black', fg='green', command=t96)
t_96.grid(row=9, column=5)

t_97 = Button(tog_frame, text='7', bg='black', fg='green', command=t97)
t_97.grid(row=9, column=6)

t_98 = Button(tog_frame, text='8', bg='black', fg='green', command=t98)
t_98.grid(row=9, column=7)

t_99 = Button(tog_frame, text='9', bg='black', fg='green', command=t99)
t_99.grid(row=9, column=8)

t_100 = Button(tog_frame, text='10', bg='black', fg='green', command=t100)
t_100.grid(row=9, column=9)


root.mainloop()