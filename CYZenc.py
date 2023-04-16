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
import random
from tkinter import messagebox
from tkinter import filedialog
#temp code for use:
from temp import sq_8192
from temp_1 import gen_code

root = Tk()
root.config(bg = 'grey')
root.title('Code Your Zero (encode)')
root.geometry('1300x800')

#IMAGES for buttons. Edit paths

img_0 = PhotoImage(file = 'img_0.png')
img_1 = PhotoImage(file = 'img_1.png')
img_2 = PhotoImage(file = 'img_2.png')
img_3 = PhotoImage(file = 'img_3.png')
img_4 = PhotoImage(file = 'img_4.png')

#ordering the picture sequences
image_list = [img_2, img_3, img_4, img_1]

ztext1a =  []
ztext2a =  []
ztext3a =  []
ztext4a =  []
ztext5a =  []
ztext6a =  []
ztext7a =  []
ztext8a =  []
ztext9a =  []
ztext10a = []

ztext1= gen_code[0:5]
ztext2=gen_code[5:10]
ztext3=gen_code[10:15]
ztext4=gen_code[15:20]
ztext5=gen_code[20:25]
ztext6=gen_code[25:30]
ztext7=gen_code[30:35]
ztext8=gen_code[35:40]
ztext9=gen_code[40:45]
ztext10=gen_code[45:50]
ztext11=gen_code[50:55]
ztext12=gen_code[55:60]
ztext13=gen_code[60:65]
ztext14=gen_code[65:70]
ztext15=gen_code[70:75]
ztext16=gen_code[75:80]
ztext17=gen_code[80:85]
ztext18=gen_code[85:90]
ztext19=gen_code[90:95]
ztext20=gen_code[95:100]
ztext21=gen_code[100:105]
ztext22=gen_code[105:110]
ztext23=gen_code[110:115]
ztext24=gen_code[115:120]
ztext25=gen_code[120:125]
ztext26=gen_code[125:130]
ztext27=gen_code[130:135]
ztext28=gen_code[135:140]
ztext29=gen_code[140:145]
ztext30=gen_code[145:150]
ztext31=gen_code[150:155]
ztext32=gen_code[155:160]
ztext33=gen_code[160:165]
ztext34=gen_code[165:170]
ztext35=gen_code[170:175]
ztext36=gen_code[175:180]
ztext37=gen_code[180:185]
ztext38=gen_code[185:190]
ztext39=gen_code[190:195]
ztext40=gen_code[195:200]
ztext41=gen_code[200:205]
ztext42=gen_code[205:210]
ztext43=gen_code[210:215]
ztext44=gen_code[215:220]
ztext45=gen_code[220:225]
ztext46=gen_code[225:230]
ztext47=gen_code[230:235]
ztext48=gen_code[235:240]
ztext49=gen_code[240:245]
ztext50=gen_code[245:250]
ztext51=gen_code[250:255]
ztext52=gen_code[255:260]
ztext53=gen_code[260:265]
ztext54=gen_code[265:270]
ztext55=gen_code[270:275]
ztext56=gen_code[275:280]
ztext57=gen_code[280:285]
ztext58=gen_code[285:290]
ztext59=gen_code[290:295]
ztext60=gen_code[295:300]
ztext61=gen_code[300:305]
ztext62=gen_code[305:310]
ztext63=gen_code[310:315]
ztext64=gen_code[315:320]
ztext65=gen_code[320:325]
ztext66=gen_code[325:330]
ztext67=gen_code[330:335]
ztext68=gen_code[335:340]
ztext69=gen_code[340:345]
ztext70=gen_code[345:350]
ztext71=gen_code[350:355]
ztext72=gen_code[355:360]
ztext73=gen_code[360:365]
ztext74=gen_code[365:370]
ztext75=gen_code[370:375]
ztext76=gen_code[375:380]
ztext77=gen_code[380:385]
ztext78=gen_code[385:390]
ztext79=gen_code[390:395]
ztext80=gen_code[395:400]
ztext81=gen_code[400:405]
ztext82=gen_code[405:410]
ztext83=gen_code[410:415]
ztext84=gen_code[415:420]
ztext85=gen_code[420:425]
ztext86=gen_code[425:430]
ztext87=gen_code[430:435]
ztext88=gen_code[435:440]
ztext89=gen_code[440:445]
ztext90=gen_code[445:450]
ztext91=gen_code[450:455]
ztext92=gen_code[455:460]
ztext93=gen_code[460:465]
ztext94=gen_code[465:470]
ztext95=gen_code[470:475]
ztext96=gen_code[475:480]
ztext97=gen_code[480:485]
ztext98=gen_code[485:490]
ztext99=gen_code[490:495]
ztext100=gen_code[495:500]

#empty lists

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

#extra
#chars

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

#extras
#numbers

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

#reference
let_num = iter(['a','A','ä','Ä','b','B','c','C','d','D','e','E','f','F','g','G','h','H','i','I','j','J','k','K','l','L','m','M','n','N','o','O','ö','Ö','p','P','q','Q',
	'r','R','s','S','t','T','u','U','ü','Ü','v','V','w','W','x','X','y','Y','z','Z','0','1','2','3','4','5','6','7','8','9','10'])

car_special = iter(['!','"','$','%','&','/','{','(','[',')',']','=','}','?','ß','\\',',',';',':','.','_','-','#','+','*',"''",'<','>','|','~', 'space'])

#def individual image function and code representations x100

def forward1(image_num):
	global b_1
	b_1.grid_forget()
	b_1 = Button(but_frame, image = image_list[image_num-1],command=lambda: forward1(image_num+1))
	b_1.grid(row=0, column=0)

	if image_num == 4:
		b_1 = Button(but_frame, image = img_0, command = lambda:forward1(0))
		b_1.grid(row=0, column=0)

	if image_num == 0:
		ent_1.delete(0,13)
		ent_1.insert(0, '0000000000000')
		ent_1.delete(0, 13)
		ent_1.insert(0, ztext1[0])

	if image_num == 1:
		ent_1.delete(0,13)
		ent_1.insert(0, '0000000000000')
		ent_1.delete(0, 13)
		ent_1.insert(0, ztext1[1])

	if image_num == 2:
		ent_1.delete(0,13)
		ent_1.insert(0, '0000000000000')
		ent_1.delete(0, 13)
		ent_1.insert(0, ztext1[2])

	if image_num == 3:
		ent_1.delete(0,13)
		ent_1.insert(0, '0000000000000')
		ent_1.delete(0, 13)
		ent_1.insert(0, ztext1[3])

	if image_num == 4:
		ent_1.delete(0,13)
		ent_1.insert(0, '0000000000000')
		ent_1.delete(0, 13)
		ent_1.insert(0, ztext1[4])

def forward2(image_num):
	global b_2
	b_2.grid_forget()
	b_2 = Button(but_frame, image = image_list[image_num-1],command=lambda: forward2(image_num+1))
	b_2.grid(row=0, column=1)

	if image_num == 4:
		b_2 = Button(but_frame, image = img_0, command = lambda:forward2(0))
		b_2.grid(row=0, column=1)

	if image_num == 0:
		ent_1.delete(13, 26)
		ent_1.insert(13, '0000000000000')
		ent_1.delete(13, 26)
		ent_1.insert(13, ztext2[0])

	if image_num == 1:
		ent_1.delete(13, 26)
		ent_1.insert(13, '0000000000000')
		ent_1.delete(13, 26)
		ent_1.insert(13, ztext2[1])

	if image_num == 2:
		ent_1.delete(13, 26)
		ent_1.insert(13, '0000000000000')
		ent_1.delete(13, 26)
		ent_1.insert(13, ztext2[2])

	if image_num == 3:
		ent_1.delete(13, 26)
		ent_1.insert(13, '0000000000000')
		ent_1.delete(13, 26)
		ent_1.insert(13, ztext2[3])

	if image_num == 4:
		ent_1.delete(13, 26)
		ent_1.insert(13, '0000000000000')
		ent_1.delete(13, 26)
		ent_1.insert(13, ztext2[4])

def forward3(image_num):
	global b_3
	b_3.grid_forget()
	b_3 = Button(but_frame, image = image_list[image_num-1],command=lambda: forward3(image_num+1))
	b_3.grid(row=0, column=2)

	if image_num == 4:
		b_3 = Button(but_frame, image = img_0, command = lambda:forward3(0))
		b_3.grid(row=0, column=2)

	if image_num == 0:
		ent_1.delete(26, 39)
		ent_1.insert(26, '0000000000000')
		ent_1.delete(26, 39)
		ent_1.insert(26, ztext3[0])

	if image_num == 1:
		ent_1.delete(26, 39)
		ent_1.insert(26, '0000000000000')
		ent_1.delete(26, 39)
		ent_1.insert(26, ztext3[1])

	if image_num == 2:
		ent_1.delete(26, 39)
		ent_1.insert(26, '0000000000000')
		ent_1.delete(26, 39)
		ent_1.insert(26, ztext3[2])

	if image_num == 3:
		ent_1.delete(26, 39)
		ent_1.insert(26, '0000000000000')
		ent_1.delete(26, 39)
		ent_1.insert(26, ztext3[3])

	if image_num == 4:
		ent_1.delete(26, 39)
		ent_1.insert(26, '0000000000000')
		ent_1.delete(26, 39)
		ent_1.insert(26, ztext3[4])

def forward4(image_num):
	global b_4
	b_4.grid_forget()
	b_4 = Button(but_frame, image = image_list[image_num-1],command=lambda: forward4(image_num+1))
	b_4.grid(row=0, column=3)

	if image_num == 4:
		b_4 = Button(but_frame, image = img_0, command = lambda:forward4(0))
		b_4.grid(row=0, column=3)

	if image_num == 0:
		ent_1.delete(39, 52)
		ent_1.insert(39, '0000000000000')
		ent_1.delete(39, 52)
		ent_1.insert(39, ztext4[0])

	if image_num == 1:
		ent_1.delete(39, 52)
		ent_1.insert(39, '0000000000000')
		ent_1.delete(39, 52)
		ent_1.insert(39, ztext4[1])

	if image_num == 2:
		ent_1.delete(39, 52)
		ent_1.insert(39, '0000000000000')
		ent_1.delete(39, 52)
		ent_1.insert(39, ztext4[2])

	if image_num == 3:
		ent_1.delete(39, 52)
		ent_1.insert(39, '0000000000000')
		ent_1.delete(39, 52)
		ent_1.insert(39, ztext4[3])

	if image_num == 4:
		ent_1.delete(39, 52)
		ent_1.insert(39, '0000000000000')
		ent_1.delete(39, 52)
		ent_1.insert(39, ztext4[4])

def forward5(image_num):
	global b_5
	b_5.grid_forget()
	b_5 = Button(but_frame, image = image_list[image_num-1],command=lambda: forward5(image_num+1))
	b_5.grid(row=0, column=4)

	if image_num == 4:
		b_5 = Button(but_frame, image = img_0, command = lambda:forward5(0))
		b_5.grid(row=0, column=4)

	if image_num == 0:
		ent_1.delete(52, 65)
		ent_1.insert(52, '0000000000000')
		ent_1.delete(52, 65)
		ent_1.insert(52, ztext5[0])

	if image_num == 1:
		ent_1.delete(52, 65)
		ent_1.insert(52, '0000000000000')
		ent_1.delete(52, 65)
		ent_1.insert(52, ztext5[1])

	if image_num == 2:
		ent_1.delete(52, 65)
		ent_1.insert(52, '0000000000000')
		ent_1.delete(52, 65)
		ent_1.insert(52, ztext5[2])

	if image_num == 3:
		ent_1.delete(52, 65)
		ent_1.insert(52, '0000000000000')
		ent_1.delete(52, 65)
		ent_1.insert(52, ztext5[3])

	if image_num == 4:
		ent_1.delete(52, 65)
		ent_1.insert(52, '0000000000000')
		ent_1.delete(52, 65)
		ent_1.insert(52, ztext5[4])

def forward6(image_num):
	global b_6
	b_6.grid_forget()
	b_6 = Button(but_frame, image = image_list[image_num-1],command=lambda: forward6(image_num+1))
	b_6.grid(row=0, column=5)

	if image_num == 4:
		b_6 = Button(but_frame, image = img_0, command = lambda:forward6(0))
		b_6.grid(row=0, column=5)

	if image_num == 0:
		ent_1.delete(65, 78)
		ent_1.insert(65, '0000000000000')
		ent_1.delete(65, 78)
		ent_1.insert(65, ztext6[0])

	if image_num == 1:
		ent_1.delete(65, 78)
		ent_1.insert(65, '0000000000000')
		ent_1.delete(65, 78)
		ent_1.insert(65, ztext6[1])

	if image_num == 2:
		ent_1.delete(65, 78)
		ent_1.insert(65, '0000000000000')
		ent_1.delete(65, 78)
		ent_1.insert(65, ztext6[2])

	if image_num == 3:
		ent_1.delete(65, 78)
		ent_1.insert(65, '0000000000000')
		ent_1.delete(65, 78)
		ent_1.insert(65, ztext6[3])

	if image_num == 4:
		ent_1.delete(65, 78)
		ent_1.insert(65, '0000000000000')
		ent_1.delete(65, 78)
		ent_1.insert(65, ztext6[4])

def forward7(image_num):
	global b_7
	b_7.grid_forget()
	b_7 = Button(but_frame, image = image_list[image_num-1],command=lambda: forward7(image_num+1))
	b_7.grid(row=0, column=6)

	if image_num == 4:
		b_7 = Button(but_frame, image = img_0, command = lambda:forward7(0))
		b_7.grid(row=0, column=6)

	if image_num == 0:
		ent_1.delete(78, 91)
		ent_1.insert(78, '0000000000000')
		ent_1.delete(78, 91)
		ent_1.insert(78, ztext7[0])

	if image_num == 1:
		ent_1.delete(78, 91)
		ent_1.insert(78, '0000000000000')
		ent_1.delete(78, 91)
		ent_1.insert(78, ztext7[1])

	if image_num == 2:
		ent_1.delete(78, 91)
		ent_1.insert(78, '0000000000000')
		ent_1.delete(78, 91)
		ent_1.insert(78, ztext7[2])

	if image_num == 3:
		ent_1.delete(78, 91)
		ent_1.insert(78, '0000000000000')
		ent_1.delete(78, 91)
		ent_1.insert(78, ztext7[3])

	if image_num == 4:
		ent_1.delete(78, 91)
		ent_1.insert(78, '0000000000000')
		ent_1.delete(78, 91)
		ent_1.insert(78, ztext7[4])

def forward8(image_num):
	global b_8
	b_8.grid_forget()
	b_8 = Button(but_frame, image = image_list[image_num-1],command=lambda: forward8(image_num+1))
	b_8.grid(row=0, column=7)

	if image_num == 4:
		b_8 = Button(but_frame, image = img_0, command = lambda:forward8(0))
		b_8.grid(row=0, column=7)

	if image_num == 0:
		ent_1.delete(91, 104)
		ent_1.insert(91, '0000000000000')
		ent_1.delete(91, 104)
		ent_1.insert(91, ztext8[0])

	if image_num == 1:
		ent_1.delete(91, 104)
		ent_1.insert(91, '0000000000000')
		ent_1.delete(91, 104)
		ent_1.insert(91, ztext8[1])

	if image_num == 2:
		ent_1.delete(91, 104)
		ent_1.insert(91, '0000000000000')
		ent_1.delete(91, 104)
		ent_1.insert(91, ztext8[2])

	if image_num == 3:
		ent_1.delete(91, 104)
		ent_1.insert(91, '0000000000000')
		ent_1.delete(91, 104)
		ent_1.insert(91, ztext8[3])

	if image_num == 4:
		ent_1.delete(91, 104)
		ent_1.insert(91, '0000000000000')
		ent_1.delete(91, 104)
		ent_1.insert(91, ztext8[4])

def forward9(image_num):
	global b_9
	b_9.grid_forget()
	b_9 = Button(but_frame, image = image_list[image_num-1],command=lambda: forward9(image_num+1))
	b_9.grid(row=0, column=8)

	if image_num == 4:
		b_9 = Button(but_frame, image = img_0, command = lambda:forward9(0))
		b_9.grid(row=0, column=8)

	if image_num == 0:
		ent_1.delete(104, 117)
		ent_1.insert(104, '0000000000000')
		ent_1.delete(104, 117)
		ent_1.insert(104, ztext9[0])

	if image_num == 1:
		ent_1.delete(104, 117)
		ent_1.insert(104, '0000000000000')
		ent_1.delete(104, 117)
		ent_1.insert(104, ztext9[1])

	if image_num == 2:
		ent_1.delete(104, 117)
		ent_1.insert(104, '0000000000000')
		ent_1.delete(104, 117)
		ent_1.insert(104, ztext9[2])

	if image_num == 3:
		ent_1.delete(104, 117)
		ent_1.insert(104, '0000000000000')
		ent_1.delete(104, 117)
		ent_1.insert(104, ztext9[3])

	if image_num == 4:
		ent_1.delete(104, 117)
		ent_1.insert(104, '0000000000000')
		ent_1.delete(104, 117)
		ent_1.insert(104, ztext9[4])

def forward10(image_num):
	global b_10
	b_10.grid_forget()
	b_10 = Button(but_frame, image = image_list[image_num-1],command=lambda: forward10(image_num+1))
	b_10.grid(row=0, column=9)

	if image_num == 4:
		b_10 = Button(but_frame, image = img_0, command = lambda:forward10(0))
		b_10.grid(row=0, column=9)

	if image_num == 0:
		ent_1.delete(117, 130)
		ent_1.insert(117, '0000000000000')
		ent_1.delete(117, 130)
		ent_1.insert(117, ztext10[0])

	if image_num == 1:
		ent_1.delete(117, 130)
		ent_1.insert(117, '0000000000000')
		ent_1.delete(117, 130)
		ent_1.insert(117, ztext10[1])

	if image_num == 2:
		ent_1.delete(117, 130)
		ent_1.insert(117, '0000000000000')
		ent_1.delete(117, 130)
		ent_1.insert(117, ztext10[2])

	if image_num == 3:
		ent_1.delete(117, 130)
		ent_1.insert(117, '0000000000000')
		ent_1.delete(117, 130)
		ent_1.insert(117, ztext10[3])

	if image_num == 4:
		ent_1.delete(117, 130)
		ent_1.insert(117, '0000000000000')
		ent_1.delete(117, 130)
		ent_1.insert(117, ztext10[4])
#10

def forward11(image_num):
	global b_11
	b_11.grid_forget()
	b_11 = Button(but_frame, image = image_list[image_num-1],command=lambda: forward11(image_num+1))
	b_11.grid(row=1, column=0)

	if image_num == 4:
		b_11 = Button(but_frame, image = img_0, command = lambda:forward11(0))
		b_11.grid(row=1, column=0)

	if image_num == 0:
		ent_2.delete(0,13)
		ent_2.insert(0, '0000000000000')
		ent_2.delete(0, 13)
		ent_2.insert(0, ztext11[0])

	if image_num == 1:
		ent_2.delete(0,13)
		ent_2.insert(0, '0000000000000')
		ent_2.delete(0, 13)
		ent_2.insert(0, ztext11[1])

	if image_num == 2:
		ent_2.delete(0,13)
		ent_2.insert(0, '0000000000000')
		ent_2.delete(0, 13)
		ent_2.insert(0, ztext11[2])

	if image_num == 3:
		ent_2.delete(0,13)
		ent_2.insert(0, '0000000000000')
		ent_2.delete(0, 13)
		ent_2.insert(0, ztext11[3])

	if image_num == 4:
		ent_2.delete(0,13)
		ent_2.insert(0, '0000000000000')
		ent_2.delete(0, 13)
		ent_2.insert(0, ztext11[4])

def forward12(image_num):
	global b_12
	b_12.grid_forget()
	b_12 = Button(but_frame, image = image_list[image_num-1],command=lambda: forward12(image_num+1))
	b_12.grid(row=1, column=1)

	if image_num == 4:
		b_12 = Button(but_frame, image = img_0, command = lambda:forward12(0))
		b_12.grid(row=1, column=1)

	if image_num == 0:
		ent_2.delete(13, 26)
		ent_2.insert(13, '0000000000000')
		ent_2.delete(13, 26)
		ent_2.insert(13, ztext12[0])

	if image_num == 1:
		ent_2.delete(13, 26)
		ent_2.insert(13, '0000000000000')
		ent_2.delete(13, 26)
		ent_2.insert(13, ztext12[1])

	if image_num == 2:
		ent_2.delete(13, 26)
		ent_2.insert(13, '0000000000000')
		ent_2.delete(13, 26)
		ent_2.insert(13, ztext12[2])

	if image_num == 3:
		ent_2.delete(13, 26)
		ent_2.insert(13, '0000000000000')
		ent_2.delete(13, 26)
		ent_2.insert(13, ztext12[3])

	if image_num == 4:
		ent_2.delete(13, 26)
		ent_2.insert(13, '0000000000000')
		ent_2.delete(13, 26)
		ent_2.insert(13, ztext12[4])

def forward13(image_num):
	global b_13
	b_13.grid_forget()
	b_13 = Button(but_frame, image = image_list[image_num-1],command=lambda: forward13(image_num+1))
	b_13.grid(row=1, column=2)

	if image_num == 4:
		b_13 = Button(but_frame, image = img_0, command = lambda:forward13(0))
		b_13.grid(row=1, column=2)

	if image_num == 0:
		ent_2.delete(26, 39)
		ent_2.insert(26, '0000000000000')
		ent_2.delete(26, 39)
		ent_2.insert(26, ztext13[0])

	if image_num == 1:
		ent_2.delete(26, 39)
		ent_2.insert(26, '0000000000000')
		ent_2.delete(26, 39)
		ent_2.insert(26, ztext13[1])

	if image_num == 2:
		ent_2.delete(26, 39)
		ent_2.insert(26, '0000000000000')
		ent_2.delete(26, 39)
		ent_2.insert(26, ztext13[2])

	if image_num == 3:
		ent_2.delete(26, 39)
		ent_2.insert(26, '0000000000000')
		ent_2.delete(26, 39)
		ent_2.insert(26, ztext13[3])

	if image_num == 4:
		ent_2.delete(26, 39)
		ent_2.insert(26, '0000000000000')
		ent_2.delete(26, 39)
		ent_2.insert(26, ztext13[4])

def forward14(image_num):
	global b_14
	b_14.grid_forget()
	b_14 = Button(but_frame, image = image_list[image_num-1],command=lambda: forward14(image_num+1))
	b_14.grid(row=1, column=3)

	if image_num == 4:
		b_14 = Button(but_frame, image = img_0, command = lambda:forward14(0))
		b_14.grid(row=1, column=3)

	if image_num == 0:
		ent_2.delete(39, 52)
		ent_2.insert(39, '0000000000000')
		ent_2.delete(39, 52)
		ent_2.insert(39, ztext14[0])

	if image_num == 1:
		ent_2.delete(39, 52)
		ent_2.insert(39, '0000000000000')
		ent_2.delete(39, 52)
		ent_2.insert(39, ztext14[1])

	if image_num == 2:
		ent_2.delete(39, 52)
		ent_2.insert(39, '0000000000000')
		ent_2.delete(39, 52)
		ent_2.insert(39, ztext14[2])

	if image_num == 3:
		ent_2.delete(39, 52)
		ent_2.insert(39, '0000000000000')
		ent_2.delete(39, 52)
		ent_2.insert(39, ztext14[3])

	if image_num == 4:
		ent_2.delete(39, 52)
		ent_2.insert(39, '0000000000000')
		ent_2.delete(39, 52)
		ent_2.insert(39, ztext14[4])

def forward15(image_num):
	global b_15
	b_15.grid_forget()
	b_15 = Button(but_frame, image = image_list[image_num-1],command=lambda: forward15(image_num+1))
	b_15.grid(row=1, column=4)

	if image_num == 4:
		b_15 = Button(but_frame, image = img_0, command = lambda:forward15(0))
		b_15.grid(row=1, column=4)

	if image_num == 0:
		ent_2.delete(52, 65)
		ent_2.insert(52, '0000000000000')
		ent_2.delete(52, 65)
		ent_2.insert(52, ztext15[0])

	if image_num == 1:
		ent_2.delete(52, 65)
		ent_2.insert(52, '0000000000000')
		ent_2.delete(52, 65)
		ent_2.insert(52, ztext15[1])

	if image_num == 2:
		ent_2.delete(52, 65)
		ent_2.insert(52, '0000000000000')
		ent_2.delete(52, 65)
		ent_2.insert(52, ztext15[2])

	if image_num == 3:
		ent_2.delete(52, 65)
		ent_2.insert(52, '0000000000000')
		ent_2.delete(52, 65)
		ent_2.insert(52, ztext15[3])

	if image_num == 4:
		ent_2.delete(52, 65)
		ent_2.insert(52, '0000000000000')
		ent_2.delete(52, 65)
		ent_2.insert(52, ztext15[4])

def forward16(image_num):
	global b_16
	b_16.grid_forget()
	b_16 = Button(but_frame, image = image_list[image_num-1],command=lambda: forward16(image_num+1))
	b_16.grid(row=1, column=5)

	if image_num == 4:
		b_16 = Button(but_frame, image = img_0, command = lambda:forward16(0))
		b_16.grid(row=1, column=5)

	if image_num == 0:
		ent_2.delete(65, 78)
		ent_2.insert(65, '0000000000000')
		ent_2.delete(65, 78)
		ent_2.insert(65, ztext16[0])

	if image_num == 1:
		ent_2.delete(65, 78)
		ent_2.insert(65, '0000000000000')
		ent_2.delete(65, 78)
		ent_2.insert(65, ztext16[1])

	if image_num == 2:
		ent_2.delete(65, 78)
		ent_2.insert(65, '0000000000000')
		ent_2.delete(65, 78)
		ent_2.insert(65, ztext16[2])

	if image_num == 3:
		ent_2.delete(65, 78)
		ent_2.insert(65, '0000000000000')
		ent_2.delete(65, 78)
		ent_2.insert(65, ztext16[3])

	if image_num == 4:
		ent_2.delete(65, 78)
		ent_2.insert(65, '0000000000000')
		ent_2.delete(65, 78)
		ent_2.insert(65, ztext16[4])

def forward17(image_num):
	global b_17
	b_17.grid_forget()
	b_17 = Button(but_frame, image = image_list[image_num-1],command=lambda: forward17(image_num+1))
	b_17.grid(row=1, column=6)

	if image_num == 4:
		b_17 = Button(but_frame, image = img_0, command = lambda:forward17(0))
		b_17.grid(row=1, column=6)

	if image_num == 0:
		ent_2.delete(78, 91)
		ent_2.insert(78, '0000000000000')
		ent_2.delete(78, 91)
		ent_2.insert(78, ztext17[0])

	if image_num == 1:
		ent_2.delete(78, 91)
		ent_2.insert(78, '0000000000000')
		ent_2.delete(78, 91)
		ent_2.insert(78, ztext17[1])

	if image_num == 2:
		ent_2.delete(78, 91)
		ent_2.insert(78, '0000000000000')
		ent_2.delete(78, 91)
		ent_2.insert(78, ztext17[2])

	if image_num == 3:
		ent_2.delete(78, 91)
		ent_2.insert(78, '0000000000000')
		ent_2.delete(78, 91)
		ent_2.insert(78, ztext17[3])

	if image_num == 4:
		ent_2.delete(78, 91)
		ent_2.insert(78, '0000000000000')
		ent_2.delete(78, 91)
		ent_2.insert(78, ztext17[4])

def forward18(image_num):
	global b_18
	b_18.grid_forget()
	b_18 = Button(but_frame, image = image_list[image_num-1],command=lambda: forward18(image_num+1))
	b_18.grid(row=1, column=7)

	if image_num == 4:
		b_18 = Button(but_frame, image = img_0, command = lambda:forward18(0))
		b_18.grid(row=1, column=7)

	if image_num == 0:
		ent_2.delete(91, 104)
		ent_2.insert(91, '0000000000000')
		ent_2.delete(91, 104)
		ent_2.insert(91, ztext18[0])

	if image_num == 1:
		ent_2.delete(91, 104)
		ent_2.insert(91, '0000000000000')
		ent_2.delete(91, 104)
		ent_2.insert(91, ztext18[1])

	if image_num == 2:
		ent_2.delete(91, 104)
		ent_2.insert(91, '0000000000000')
		ent_2.delete(91, 104)
		ent_2.insert(91, ztext18[2])

	if image_num == 3:
		ent_2.delete(91, 104)
		ent_2.insert(91, '0000000000000')
		ent_2.delete(91, 104)
		ent_2.insert(91, ztext18[3])

	if image_num == 4:
		ent_2.delete(91, 104)
		ent_2.insert(91, '0000000000000')
		ent_2.delete(91, 104)
		ent_2.insert(91, ztext18[4])

def forward19(image_num):
	global b_19
	b_19.grid_forget()
	b_19 = Button(but_frame, image = image_list[image_num-1],command=lambda: forward19(image_num+1))
	b_19.grid(row=1, column=8)

	if image_num == 4:
		b_19 = Button(but_frame, image = img_0, command = lambda:forward19(0))
		b_19.grid(row=1, column=8)

	if image_num == 0:
		ent_2.delete(104, 117)
		ent_2.insert(104, '0000000000000')
		ent_2.delete(104, 117)
		ent_2.insert(104, ztext19[0])

	if image_num == 1:
		ent_2.delete(104, 117)
		ent_2.insert(104, '0000000000000')
		ent_2.delete(104, 117)
		ent_2.insert(104, ztext19[1])

	if image_num == 2:
		ent_2.delete(104, 117)
		ent_2.insert(104, '0000000000000')
		ent_2.delete(104, 117)
		ent_2.insert(104, ztext19[2])

	if image_num == 3:
		ent_2.delete(104, 117)
		ent_2.insert(104, '0000000000000')
		ent_2.delete(104, 117)
		ent_2.insert(104, ztext19[3])

	if image_num == 4:
		ent_2.delete(104, 117)
		ent_2.insert(104, '0000000000000')
		ent_2.delete(104, 117)
		ent_2.insert(104, ztext19[4])

def forward20(image_num):
	global b_20
	b_20.grid_forget()
	b_20 = Button(but_frame, image = image_list[image_num-1],command=lambda: forward20(image_num+1))
	b_20.grid(row=1, column=9)

	if image_num == 4:
		b_20 = Button(but_frame, image = img_0, command = lambda:forward20(0))
		b_20.grid(row=1, column=9)

	if image_num == 0:
		ent_2.delete(117, 130)
		ent_2.insert(117, '0000000000000')
		ent_2.delete(117, 130)
		ent_2.insert(117, ztext20[0])

	if image_num == 1:
		ent_2.delete(117, 130)
		ent_2.insert(117, '0000000000000')
		ent_2.delete(117, 130)
		ent_2.insert(117, ztext20[1])

	if image_num == 2:
		ent_2.delete(117, 130)
		ent_2.insert(117, '0000000000000')
		ent_2.delete(117, 130)
		ent_2.insert(117, ztext20[2])

	if image_num == 3:
		ent_2.delete(117, 130)
		ent_2.insert(117, '0000000000000')
		ent_2.delete(117, 130)
		ent_2.insert(117, ztext20[3])

	if image_num == 4:
		ent_2.delete(117, 130)
		ent_2.insert(117, '0000000000000')
		ent_2.delete(117, 130)
		ent_2.insert(117, ztext20[4])
#20
def forward21(image_num):
	global b_21
	b_21.grid_forget()
	b_21 = Button(but_frame, image = image_list[image_num-1],command=lambda: forward21(image_num+1))
	b_21.grid(row=2, column=0)

	if image_num == 4:
		b_21 = Button(but_frame, image = img_0, command = lambda:forward21(0))
		b_21.grid(row=2, column=0)

	if image_num == 0:
		ent_3.delete(0,13)
		ent_3.insert(0, '0000000000000')
		ent_3.delete(0, 13)
		ent_3.insert(0, ztext21[0])

	if image_num == 1:
		ent_3.delete(0,13)
		ent_3.insert(0, '0000000000000')
		ent_3.delete(0, 13)
		ent_3.insert(0, ztext21[1])

	if image_num == 2:
		ent_3.delete(0,13)
		ent_3.insert(0, '0000000000000')
		ent_3.delete(0, 13)
		ent_3.insert(0, ztext21[2])

	if image_num == 3:
		ent_3.delete(0,13)
		ent_3.insert(0, '0000000000000')
		ent_3.delete(0, 13)
		ent_3.insert(0, ztext21[3])

	if image_num == 4:
		ent_3.delete(0,13)
		ent_3.insert(0, '0000000000000')
		ent_3.delete(0, 13)
		ent_3.insert(0, ztext21[4])

def forward22(image_num):
	global b_22
	b_22.grid_forget()
	b_22 = Button(but_frame, image = image_list[image_num-1],command=lambda: forward22(image_num+1))
	b_22.grid(row=2, column=1)

	if image_num == 4:
		b_22 = Button(but_frame, image = img_0, command = lambda:forward22(0))
		b_22.grid(row=2, column=1)

	if image_num == 0:
		ent_3.delete(13, 26)
		ent_3.insert(13, '0000000000000')
		ent_3.delete(13, 26)
		ent_3.insert(13, ztext22[0])

	if image_num == 1:
		ent_3.delete(13, 26)
		ent_3.insert(13, '0000000000000')
		ent_3.delete(13, 26)
		ent_3.insert(13, ztext22[1])

	if image_num == 2:
		ent_3.delete(13, 26)
		ent_3.insert(13, '0000000000000')
		ent_3.delete(13, 26)
		ent_3.insert(13, ztext22[2])

	if image_num == 3:
		ent_3.delete(13, 26)
		ent_3.insert(13, '0000000000000')
		ent_3.delete(13, 26)
		ent_3.insert(13, ztext22[3])

	if image_num == 4:
		ent_3.delete(13, 26)
		ent_3.insert(13, '0000000000000')
		ent_3.delete(13, 26)
		ent_3.insert(13, ztext22[4])

def forward23(image_num):
	global b_23
	b_23.grid_forget()
	b_23 = Button(but_frame, image = image_list[image_num-1],command=lambda: forward23(image_num+1))
	b_23.grid(row=2, column=2)

	if image_num == 4:
		b_23 = Button(but_frame, image = img_0, command = lambda:forward23(0))
		b_23.grid(row=2, column=2)

	if image_num == 0:
		ent_3.delete(26, 39)
		ent_3.insert(26, '0000000000000')
		ent_3.delete(26, 39)
		ent_3.insert(26, ztext23[0])

	if image_num == 1:
		ent_3.delete(26, 39)
		ent_3.insert(26, '0000000000000')
		ent_3.delete(26, 39)
		ent_3.insert(26, ztext23[1])

	if image_num == 2:
		ent_3.delete(26, 39)
		ent_3.insert(26, '0000000000000')
		ent_3.delete(26, 39)
		ent_3.insert(26, ztext23[2])

	if image_num == 3:
		ent_3.delete(26, 39)
		ent_3.insert(26, '0000000000000')
		ent_3.delete(26, 39)
		ent_3.insert(26, ztext23[3])

	if image_num == 4:
		ent_3.delete(26, 39)
		ent_3.insert(26, '0000000000000')
		ent_3.delete(26, 39)
		ent_3.insert(26, ztext23[4])

def forward24(image_num):
	global b_24
	b_24.grid_forget()
	b_24 = Button(but_frame, image = image_list[image_num-1],command=lambda: forward24(image_num+1))
	b_24.grid(row=2, column=3)

	if image_num == 4:
		b_24 = Button(but_frame, image = img_0, command = lambda:forward24(0))
		b_24.grid(row=2, column=3)

	if image_num == 0:
		ent_3.delete(39, 52)
		ent_3.insert(39, '0000000000000')
		ent_3.delete(39, 52)
		ent_3.insert(39, ztext24[0])

	if image_num == 1:
		ent_3.delete(39, 52)
		ent_3.insert(39, '0000000000000')
		ent_3.delete(39, 52)
		ent_3.insert(39, ztext24[1])

	if image_num == 2:
		ent_3.delete(39, 52)
		ent_3.insert(39, '0000000000000')
		ent_3.delete(39, 52)
		ent_3.insert(39, ztext24[2])

	if image_num == 3:
		ent_3.delete(39, 52)
		ent_3.insert(39, '0000000000000')
		ent_3.delete(39, 52)
		ent_3.insert(39, ztext24[3])

	if image_num == 4:
		ent_3.delete(39, 52)
		ent_3.insert(39, '0000000000000')
		ent_3.delete(39, 52)
		ent_3.insert(39, ztext24[4])

def forward25(image_num):
	global b_25
	b_25.grid_forget()
	b_25 = Button(but_frame, image = image_list[image_num-1],command=lambda: forward25(image_num+1))
	b_25.grid(row=2, column=4)

	if image_num == 4:
		b_25 = Button(but_frame, image = img_0, command = lambda:forward25(0))
		b_25.grid(row=2, column=4)

	if image_num == 0:
		ent_3.delete(52, 65)
		ent_3.insert(52, '0000000000000')
		ent_3.delete(52, 65)
		ent_3.insert(52, ztext25[0])

	if image_num == 1:
		ent_3.delete(52, 65)
		ent_3.insert(52, '0000000000000')
		ent_3.delete(52, 65)
		ent_3.insert(52, ztext25[1])

	if image_num == 2:
		ent_3.delete(52, 65)
		ent_3.insert(52, '0000000000000')
		ent_3.delete(52, 65)
		ent_3.insert(52, ztext25[2])

	if image_num == 3:
		ent_3.delete(52, 65)
		ent_3.insert(52, '0000000000000')
		ent_3.delete(52, 65)
		ent_3.insert(52, ztext25[3])

	if image_num == 4:
		ent_3.delete(52, 65)
		ent_3.insert(52, '0000000000000')
		ent_3.delete(52, 65)
		ent_3.insert(52, ztext25[4])

def forward26(image_num):
	global b_26
	b_26.grid_forget()
	b_26 = Button(but_frame, image = image_list[image_num-1],command=lambda: forward26(image_num+1))
	b_26.grid(row=2, column=5)

	if image_num == 4:
		b_26 = Button(but_frame, image = img_0, command = lambda:forward26(0))
		b_26.grid(row=2, column=5)

	if image_num == 0:
		ent_3.delete(65, 78)
		ent_3.insert(65, '0000000000000')
		ent_3.delete(65, 78)
		ent_3.insert(65, ztext26[0])

	if image_num == 1:
		ent_3.delete(65, 78)
		ent_3.insert(65, '0000000000000')
		ent_3.delete(65, 78)
		ent_3.insert(65, ztext26[1])

	if image_num == 2:
		ent_3.delete(65, 78)
		ent_3.insert(65, '0000000000000')
		ent_3.delete(65, 78)
		ent_3.insert(65, ztext26[2])

	if image_num == 3:
		ent_3.delete(65, 78)
		ent_3.insert(65, '0000000000000')
		ent_3.delete(65, 78)
		ent_3.insert(65, ztext26[3])

	if image_num == 4:
		ent_3.delete(65, 78)
		ent_3.insert(65, '0000000000000')
		ent_3.delete(65, 78)
		ent_3.insert(65, ztext26[4])

def forward27(image_num):
	global b_27
	b_27.grid_forget()
	b_27 = Button(but_frame, image = image_list[image_num-1],command=lambda: forward27(image_num+1))
	b_27.grid(row=2, column=6)

	if image_num == 4:
		b_27 = Button(but_frame, image = img_0, command = lambda:forward27(0))
		b_27.grid(row=2, column=6)

	if image_num == 0:
		ent_3.delete(78, 91)
		ent_3.insert(78, '0000000000000')
		ent_3.delete(78, 91)
		ent_3.insert(78, ztext27[0])

	if image_num == 1:
		ent_3.delete(78, 91)
		ent_3.insert(78, '0000000000000')
		ent_3.delete(78, 91)
		ent_3.insert(78, ztext27[1])

	if image_num == 2:
		ent_3.delete(78, 91)
		ent_3.insert(78, '0000000000000')
		ent_3.delete(78, 91)
		ent_3.insert(78, ztext27[2])

	if image_num == 3:
		ent_3.delete(78, 91)
		ent_3.insert(78, '0000000000000')
		ent_3.delete(78, 91)
		ent_3.insert(78, ztext27[3])

	if image_num == 4:
		ent_3.delete(78, 91)
		ent_3.insert(78, '0000000000000')
		ent_3.delete(78, 91)
		ent_3.insert(78, ztext27[4])

def forward28(image_num):
	global b_28
	b_28.grid_forget()
	b_28 = Button(but_frame, image = image_list[image_num-1],command=lambda: forward28(image_num+1))
	b_28.grid(row=2, column=7)

	if image_num == 4:
		b_28 = Button(but_frame, image = img_0, command = lambda:forward28(0))
		b_28.grid(row=2, column=7)

	if image_num == 0:
		ent_3.delete(91, 104)
		ent_3.insert(91, '0000000000000')
		ent_3.delete(91, 104)
		ent_3.insert(91, ztext28[0])

	if image_num == 1:
		ent_3.delete(91, 104)
		ent_3.insert(91, '0000000000000')
		ent_3.delete(91, 104)
		ent_3.insert(91, ztext28[1])

	if image_num == 2:
		ent_3.delete(91, 104)
		ent_3.insert(91, '0000000000000')
		ent_3.delete(91, 104)
		ent_3.insert(91, ztext28[2])

	if image_num == 3:
		ent_3.delete(91, 104)
		ent_3.insert(91, '0000000000000')
		ent_3.delete(91, 104)
		ent_3.insert(91, ztext28[3])

	if image_num == 4:
		ent_3.delete(91, 104)
		ent_3.insert(91, '0000000000000')
		ent_3.delete(91, 104)
		ent_3.insert(91, ztext28[4])

def forward29(image_num):
	global b_29
	b_29.grid_forget()
	b_29 = Button(but_frame, image = image_list[image_num-1],command=lambda: forward29(image_num+1))
	b_29.grid(row=2, column=8)

	if image_num == 4:
		b_29 = Button(but_frame, image = img_0, command = lambda:forward29(0))
		b_29.grid(row=2, column=8)

	if image_num == 0:
		ent_3.delete(104, 117)
		ent_3.insert(104, '0000000000000')
		ent_3.delete(104, 117)
		ent_3.insert(104, ztext29[0])

	if image_num == 1:
		ent_3.delete(104, 117)
		ent_3.insert(104, '0000000000000')
		ent_3.delete(104, 117)
		ent_3.insert(104, ztext29[1])

	if image_num == 2:
		ent_3.delete(104, 117)
		ent_3.insert(104, '0000000000000')
		ent_3.delete(104, 117)
		ent_3.insert(104, ztext29[2])

	if image_num == 3:
		ent_3.delete(104, 117)
		ent_3.insert(104, '0000000000000')
		ent_3.delete(104, 117)
		ent_3.insert(104, ztext29[3])

	if image_num == 4:
		ent_3.delete(104, 117)
		ent_3.insert(104, '0000000000000')
		ent_3.delete(104, 117)
		ent_3.insert(104, ztext29[4])

def forward30(image_num):
	global b_30
	b_30.grid_forget()
	b_30 = Button(but_frame, image = image_list[image_num-1],command=lambda: forward30(image_num+1))
	b_30.grid(row=2, column=9)

	if image_num == 4:
		b_30 = Button(but_frame, image = img_0, command = lambda:forward30(0))
		b_30.grid(row=2, column=9)

	if image_num == 0:
		ent_3.delete(117, 130)
		ent_3.insert(117, '0000000000000')
		ent_3.delete(117, 130)
		ent_3.insert(117, ztext30[0])

	if image_num == 1:
		ent_3.delete(117, 130)
		ent_3.insert(117, '0000000000000')
		ent_3.delete(117, 130)
		ent_3.insert(117, ztext30[1])

	if image_num == 2:
		ent_3.delete(117, 130)
		ent_3.insert(117, '0000000000000')
		ent_3.delete(117, 130)
		ent_3.insert(117, ztext30[2])

	if image_num == 3:
		ent_3.delete(117, 130)
		ent_3.insert(117, '0000000000000')
		ent_3.delete(117, 130)
		ent_3.insert(117, ztext30[3])

	if image_num == 4:
		ent_3.delete(117, 130)
		ent_3.insert(117, '0000000000000')
		ent_3.delete(117, 130)
		ent_3.insert(117, ztext30[4])
#30
def forward31(image_num):
	global b_31
	b_31.grid_forget()
	b_31 = Button(but_frame, image = image_list[image_num-1],command=lambda: forward31(image_num+1))
	b_31.grid(row=3, column=0)

	if image_num == 4:
		b_31 = Button(but_frame, image = img_0, command = lambda:forward31(0))
		b_31.grid(row=3, column=0)

	if image_num == 0:
		ent_4.delete(0,13)
		ent_4.insert(0, '0000000000000')
		ent_4.delete(0, 13)
		ent_4.insert(0, ztext31[0])

	if image_num == 1:
		ent_4.delete(0,13)
		ent_4.insert(0, '0000000000000')
		ent_4.delete(0, 13)
		ent_4.insert(0, ztext31[1])

	if image_num == 2:
		ent_4.delete(0,13)
		ent_4.insert(0, '0000000000000')
		ent_4.delete(0, 13)
		ent_4.insert(0, ztext31[2])

	if image_num == 3:
		ent_4.delete(0,13)
		ent_4.insert(0, '0000000000000')
		ent_4.delete(0, 13)
		ent_4.insert(0, ztext31[3])

	if image_num == 4:
		ent_4.delete(0,13)
		ent_4.insert(0, '0000000000000')
		ent_4.delete(0, 13)
		ent_4.insert(0, ztext31[4])

def forward32(image_num):
	global b_32
	b_32.grid_forget()
	b_32 = Button(but_frame, image = image_list[image_num-1],command=lambda: forward32(image_num+1))
	b_32.grid(row=3, column=1)

	if image_num == 4:
		b_32 = Button(but_frame, image = img_0, command = lambda:forward32(0))
		b_32.grid(row=3, column=1)

	if image_num == 0:
		ent_4.delete(13, 26)
		ent_4.insert(13, '0000000000000')
		ent_4.delete(13, 26)
		ent_4.insert(13, ztext32[0])

	if image_num == 1:
		ent_4.delete(13, 26)
		ent_4.insert(13, '0000000000000')
		ent_4.delete(13, 26)
		ent_4.insert(13, ztext32[1])

	if image_num == 2:
		ent_4.delete(13, 26)
		ent_4.insert(13, '0000000000000')
		ent_4.delete(13, 26)
		ent_4.insert(13, ztext32[2])

	if image_num == 3:
		ent_4.delete(13, 26)
		ent_4.insert(13, '0000000000000')
		ent_4.delete(13, 26)
		ent_4.insert(13, ztext32[3])

	if image_num == 4:
		ent_4.delete(13, 26)
		ent_4.insert(13, '0000000000000')
		ent_4.delete(13, 26)
		ent_4.insert(13, ztext32[4])

def forward33(image_num):
	global b_33
	b_33.grid_forget()
	b_33 = Button(but_frame, image = image_list[image_num-1],command=lambda: forward33(image_num+1))
	b_33.grid(row=3, column=2)

	if image_num == 4:
		b_33 = Button(but_frame, image = img_0, command = lambda:forward33(0))
		b_33.grid(row=3, column=2)

	if image_num == 0:
		ent_4.delete(26, 39)
		ent_4.insert(26, '0000000000000')
		ent_4.delete(26, 39)
		ent_4.insert(26, ztext33[0])

	if image_num == 1:
		ent_4.delete(26, 39)
		ent_4.insert(26, '0000000000000')
		ent_4.delete(26, 39)
		ent_4.insert(26, ztext33[1])

	if image_num == 2:
		ent_4.delete(26, 39)
		ent_4.insert(26, '0000000000000')
		ent_4.delete(26, 39)
		ent_4.insert(26, ztext33[2])

	if image_num == 3:
		ent_4.delete(26, 39)
		ent_4.insert(26, '0000000000000')
		ent_4.delete(26, 39)
		ent_4.insert(26, ztext33[3])

	if image_num == 4:
		ent_4.delete(26, 39)
		ent_4.insert(26, '0000000000000')
		ent_4.delete(26, 39)
		ent_4.insert(26, ztext33[4])


def forward34(image_num):
	global b_34
	b_34.grid_forget()
	b_34 = Button(but_frame, image = image_list[image_num-1],command=lambda: forward34(image_num+1))
	b_34.grid(row=3, column=3)

	if image_num == 4:
		b_34 = Button(but_frame, image = img_0, command = lambda:forward34(0))
		b_34.grid(row=3, column=3)

	if image_num == 0:
		ent_4.delete(39, 52)
		ent_4.insert(39, '0000000000000')
		ent_4.delete(39, 52)
		ent_4.insert(39, ztext34[0])

	if image_num == 1:
		ent_4.delete(39, 52)
		ent_4.insert(39, '0000000000000')
		ent_4.delete(39, 52)
		ent_4.insert(39, ztext34[1])

	if image_num == 2:
		ent_4.delete(39, 52)
		ent_4.insert(39, '0000000000000')
		ent_4.delete(39, 52)
		ent_4.insert(39, ztext34[2])

	if image_num == 3:
		ent_4.delete(39, 52)
		ent_4.insert(39, '0000000000000')
		ent_4.delete(39, 52)
		ent_4.insert(39, ztext34[3])

	if image_num == 4:
		ent_4.delete(39, 52)
		ent_4.insert(39, '0000000000000')
		ent_4.delete(39, 52)
		ent_4.insert(39, ztext34[4])

def forward35(image_num):
	global b_35
	b_35.grid_forget()
	b_35 = Button(but_frame, image = image_list[image_num-1],command=lambda: forward35(image_num+1))
	b_35.grid(row=3, column=4)

	if image_num == 4:
		b_35 = Button(but_frame, image = img_0, command = lambda:forward35(0))
		b_35.grid(row=3, column=4)

	if image_num == 0:
		ent_4.delete(52, 65)
		ent_4.insert(52, '0000000000000')
		ent_4.delete(52, 65)
		ent_4.insert(52, ztext35[0])

	if image_num == 1:
		ent_4.delete(52, 65)
		ent_4.insert(52, '0000000000000')
		ent_4.delete(52, 65)
		ent_4.insert(52, ztext35[1])

	if image_num == 2:
		ent_4.delete(52, 65)
		ent_4.insert(52, '0000000000000')
		ent_4.delete(52, 65)
		ent_4.insert(52, ztext35[2])

	if image_num == 3:
		ent_4.delete(52, 65)
		ent_4.insert(52, '0000000000000')
		ent_4.delete(52, 65)
		ent_4.insert(52, ztext35[3])

	if image_num == 4:
		ent_4.delete(52, 65)
		ent_4.insert(52, '0000000000000')
		ent_4.delete(52, 65)
		ent_4.insert(52, ztext35[4])

def forward36(image_num):
	global b_36
	b_36.grid_forget()
	b_36 = Button(but_frame, image = image_list[image_num-1],command=lambda: forward36(image_num+1))
	b_36.grid(row=3, column=5)

	if image_num == 4:
		b_36 = Button(but_frame, image = img_0, command = lambda:forward36(0))
		b_36.grid(row=3, column=5)

	if image_num == 0:
		ent_4.delete(65, 78)
		ent_4.insert(65, '0000000000000')
		ent_4.delete(65, 78)
		ent_4.insert(65, ztext36[0])

	if image_num == 1:
		ent_4.delete(65, 78)
		ent_4.insert(65, '0000000000000')
		ent_4.delete(65, 78)
		ent_4.insert(65, ztext36[1])

	if image_num == 2:
		ent_4.delete(65, 78)
		ent_4.insert(65, '0000000000000')
		ent_4.delete(65, 78)
		ent_4.insert(65, ztext36[2])

	if image_num == 3:
		ent_4.delete(65, 78)
		ent_4.insert(65, '0000000000000')
		ent_4.delete(65, 78)
		ent_4.insert(65, ztext36[3])

	if image_num == 4:
		ent_4.delete(65, 78)
		ent_4.insert(65, '0000000000000')
		ent_4.delete(65, 78)
		ent_4.insert(65, ztext36[4])

def forward37(image_num):
	global b_37
	b_37.grid_forget()
	b_37 = Button(but_frame, image = image_list[image_num-1],command=lambda: forward37(image_num+1))
	b_37.grid(row=3, column=6)

	if image_num == 4:
		b_37 = Button(but_frame, image = img_0, command = lambda:forward37(0))
		b_37.grid(row=3, column=6)

	if image_num == 0:
		ent_4.delete(78, 91)
		ent_4.insert(78, '0000000000000')
		ent_4.delete(78, 91)
		ent_4.insert(78, ztext37[0])

	if image_num == 1:
		ent_4.delete(78, 91)
		ent_4.insert(78, '0000000000000')
		ent_4.delete(78, 91)
		ent_4.insert(78, ztext37[1])

	if image_num == 2:
		ent_4.delete(78, 91)
		ent_4.insert(78, '0000000000000')
		ent_4.delete(78, 91)
		ent_4.insert(78, ztext37[2])

	if image_num == 3:
		ent_4.delete(78, 91)
		ent_4.insert(78, '0000000000000')
		ent_4.delete(78, 91)
		ent_4.insert(78, ztext37[3])

	if image_num == 4:
		ent_4.delete(78, 91)
		ent_4.insert(78, '0000000000000')
		ent_4.delete(78, 91)
		ent_4.insert(78, ztext37[4])

def forward38(image_num):
	global b_38
	b_38.grid_forget()
	b_38 = Button(but_frame, image = image_list[image_num-1],command=lambda: forward38(image_num+1))
	b_38.grid(row=3, column=7)

	if image_num == 4:
		b_38 = Button(but_frame, image = img_0, command = lambda:forward38(0))
		b_38.grid(row=3, column=7)

	if image_num == 0:
		ent_4.delete(91, 104)
		ent_4.insert(91, '0000000000000')
		ent_4.delete(91, 104)
		ent_4.insert(91, ztext38[0])

	if image_num == 1:
		ent_4.delete(91, 104)
		ent_4.insert(91, '0000000000000')
		ent_4.delete(91, 104)
		ent_4.insert(91, ztext38[1])

	if image_num == 2:
		ent_4.delete(91, 104)
		ent_4.insert(91, '0000000000000')
		ent_4.delete(91, 104)
		ent_4.insert(91, ztext38[2])

	if image_num == 3:
		ent_4.delete(91, 104)
		ent_4.insert(91, '0000000000000')
		ent_4.delete(91, 104)
		ent_4.insert(91, ztext38[3])

	if image_num == 4:
		ent_4.delete(91, 104)
		ent_4.insert(91, '0000000000000')
		ent_4.delete(91, 104)
		ent_4.insert(91, ztext38[4])

def forward39(image_num):
	global b_39
	b_39.grid_forget()
	b_39 = Button(but_frame, image = image_list[image_num-1],command=lambda: forward39(image_num+1))
	b_39.grid(row=3, column=8)

	if image_num == 4:
		b_39 = Button(but_frame, image = img_0, command = lambda:forward39(0))
		b_39.grid(row=3, column=8)

	if image_num == 0:
		ent_4.delete(104, 117)
		ent_4.insert(104, '0000000000000')
		ent_4.delete(104, 117)
		ent_4.insert(104, ztext39[0])

	if image_num == 1:
		ent_4.delete(104, 117)
		ent_4.insert(104, '0000000000000')
		ent_4.delete(104, 117)
		ent_4.insert(104, ztext39[1])

	if image_num == 2:
		ent_4.delete(104, 117)
		ent_4.insert(104, '0000000000000')
		ent_4.delete(104, 117)
		ent_4.insert(104, ztext39[2])

	if image_num == 3:
		ent_4.delete(104, 117)
		ent_4.insert(104, '0000000000000')
		ent_4.delete(104, 117)
		ent_4.insert(104, ztext39[3])

	if image_num == 4:
		ent_4.delete(104, 117)
		ent_4.insert(104, '0000000000000')
		ent_4.delete(104, 117)
		ent_4.insert(104, ztext39[4])

def forward40(image_num):
	global b_40
	b_40.grid_forget()
	b_40 = Button(but_frame, image = image_list[image_num-1],command=lambda: forward40(image_num+1))
	b_40.grid(row=3, column=9)

	if image_num == 4:
		b_40 = Button(but_frame, image = img_0, command = lambda:forward40(0))
		b_40.grid(row=3, column=9)

	if image_num == 0:
		ent_4.delete(117, 130)
		ent_4.insert(117, '0000000000000')
		ent_4.delete(117, 130)
		ent_4.insert(117, ztext40[0])

	if image_num == 1:
		ent_4.delete(117, 130)
		ent_4.insert(117, '0000000000000')
		ent_4.delete(117, 130)
		ent_4.insert(117, ztext40[1])

	if image_num == 2:
		ent_4.delete(117, 130)
		ent_4.insert(117, '0000000000000')
		ent_4.delete(117, 130)
		ent_4.insert(117, ztext40[2])

	if image_num == 3:
		ent_4.delete(117, 130)
		ent_4.insert(117, '0000000000000')
		ent_4.delete(117, 130)
		ent_4.insert(117, ztext40[3])

	if image_num == 4:
		ent_4.delete(117, 130)
		ent_4.insert(117, '0000000000000')
		ent_4.delete(117, 130)
		ent_4.insert(117, ztext40[4])
#40
def forward41(image_num):
	global b_41
	b_41.grid_forget()
	b_41 = Button(but_frame, image = image_list[image_num-1],command=lambda: forward41(image_num+1))
	b_41.grid(row=4, column=0)

	if image_num == 4:
		b_41 = Button(but_frame, image = img_0, command = lambda:forward41(0))
		b_41.grid(row=4, column=0)

	if image_num == 0:
		ent_5.delete(0,13)
		ent_5.insert(0, '0000000000000')
		ent_5.delete(0, 13)
		ent_5.insert(0, ztext41[0])

	if image_num == 1:
		ent_5.delete(0,13)
		ent_5.insert(0, '0000000000000')
		ent_5.delete(0, 13)
		ent_5.insert(0, ztext41[1])

	if image_num == 2:
		ent_5.delete(0,13)
		ent_5.insert(0, '0000000000000')
		ent_5.delete(0, 13)
		ent_5.insert(0, ztext41[2])

	if image_num == 3:
		ent_5.delete(0,13)
		ent_5.insert(0, '0000000000000')
		ent_5.delete(0, 13)
		ent_5.insert(0, ztext41[3])

	if image_num == 4:
		ent_5.delete(0,13)
		ent_5.insert(0, '0000000000000')
		ent_5.delete(0, 13)
		ent_5.insert(0, ztext41[4])

def forward42(image_num):
	global b_42
	b_42.grid_forget()
	b_42 = Button(but_frame, image = image_list[image_num-1],command=lambda: forward42(image_num+1))
	b_42.grid(row=4, column=1)

	if image_num == 4:
		b_42 = Button(but_frame, image = img_0, command = lambda:forward42(0))
		b_42.grid(row=4, column=1)

	if image_num == 0:
		ent_5.delete(13, 26)
		ent_5.insert(13, '0000000000000')
		ent_5.delete(13, 26)
		ent_5.insert(13, ztext42[0])

	if image_num == 1:
		ent_5.delete(13, 26)
		ent_5.insert(13, '0000000000000')
		ent_5.delete(13, 26)
		ent_5.insert(13, ztext42[1])

	if image_num == 2:
		ent_5.delete(13, 26)
		ent_5.insert(13, '0000000000000')
		ent_5.delete(13, 26)
		ent_5.insert(13, ztext42[2])

	if image_num == 3:
		ent_5.delete(13, 26)
		ent_5.insert(13, '0000000000000')
		ent_5.delete(13, 26)
		ent_5.insert(13, ztext42[3])

	if image_num == 4:
		ent_5.delete(13, 26)
		ent_5.insert(13, '0000000000000')
		ent_5.delete(13, 26)
		ent_5.insert(13, ztext42[4])

def forward43(image_num):
	global b_43
	b_43.grid_forget()
	b_43 = Button(but_frame, image = image_list[image_num-1],command=lambda: forward43(image_num+1))
	b_43.grid(row=4, column=2)

	if image_num == 4:
		b_43 = Button(but_frame, image = img_0, command = lambda:forward43(0))
		b_43.grid(row=4, column=2)

	if image_num == 0:
		ent_5.delete(26, 39)
		ent_5.insert(26, '0000000000000')
		ent_5.delete(26, 39)
		ent_5.insert(26, ztext43[0])

	if image_num == 1:
		ent_5.delete(26, 39)
		ent_5.insert(26, '0000000000000')
		ent_5.delete(26, 39)
		ent_5.insert(26, ztext43[1])

	if image_num == 2:
		ent_5.delete(26, 39)
		ent_5.insert(26, '0000000000000')
		ent_5.delete(26, 39)
		ent_5.insert(26, ztext43[2])

	if image_num == 3:
		ent_5.delete(26, 39)
		ent_5.insert(26, '0000000000000')
		ent_5.delete(26, 39)
		ent_5.insert(26, ztext43[3])

	if image_num == 4:
		ent_5.delete(26, 39)
		ent_5.insert(26, '0000000000000')
		ent_5.delete(26, 39)
		ent_5.insert(26, ztext43[4])

def forward44(image_num):
	global b_44
	b_44.grid_forget()
	b_44 = Button(but_frame, image = image_list[image_num-1],command=lambda: forward44(image_num+1))
	b_44.grid(row=4, column=3)

	if image_num == 4:
		b_44 = Button(but_frame, image = img_0, command = lambda:forward44(0))
		b_44.grid(row=4, column=3)

	if image_num == 0:
		ent_5.delete(39, 52)
		ent_5.insert(39, '0000000000000')
		ent_5.delete(39, 52)
		ent_5.insert(39, ztext44[0])

	if image_num == 1:
		ent_5.delete(39, 52)
		ent_5.insert(39, '0000000000000')
		ent_5.delete(39, 52)
		ent_5.insert(39, ztext44[1])

	if image_num == 2:
		ent_5.delete(39, 52)
		ent_5.insert(39, '0000000000000')
		ent_5.delete(39, 52)
		ent_5.insert(39, ztext44[2])

	if image_num == 3:
		ent_5.delete(39, 52)
		ent_5.insert(39, '0000000000000')
		ent_5.delete(39, 52)
		ent_5.insert(39, ztext44[3])

	if image_num == 4:
		ent_5.delete(39, 52)
		ent_5.insert(39, '0000000000000')
		ent_5.delete(39, 52)
		ent_5.insert(39, ztext44[4])

def forward45(image_num):
	global b_45
	b_45.grid_forget()
	b_45 = Button(but_frame, image = image_list[image_num-1],command=lambda: forward45(image_num+1))
	b_45.grid(row=4, column=4)

	if image_num == 4:
		b_45 = Button(but_frame, image = img_0, command = lambda:forward45(0))
		b_45.grid(row=4, column=4)

	if image_num == 0:
		ent_5.delete(52, 65)
		ent_5.insert(52, '0000000000000')
		ent_5.delete(52, 65)
		ent_5.insert(52, ztext45[0])

	if image_num == 1:
		ent_5.delete(52, 65)
		ent_5.insert(52, '0000000000000')
		ent_5.delete(52, 65)
		ent_5.insert(52, ztext45[1])

	if image_num == 2:
		ent_5.delete(52, 65)
		ent_5.insert(52, '0000000000000')
		ent_5.delete(52, 65)
		ent_5.insert(52, ztext45[2])

	if image_num == 3:
		ent_5.delete(52, 65)
		ent_5.insert(52, '0000000000000')
		ent_5.delete(52, 65)
		ent_5.insert(52, ztext45[3])

	if image_num == 4:
		ent_5.delete(52, 65)
		ent_5.insert(52, '0000000000000')
		ent_5.delete(52, 65)
		ent_5.insert(52, ztext45[4])

def forward46(image_num):
	global b_46
	b_46.grid_forget()
	b_46 = Button(but_frame, image = image_list[image_num-1],command=lambda: forward46(image_num+1))
	b_46.grid(row=4, column=5)

	if image_num == 4:
		b_46 = Button(but_frame, image = img_0, command = lambda:forward46(0))
		b_46.grid(row=4, column=5)

	if image_num == 0:
		ent_5.delete(65, 78)
		ent_5.insert(65, '0000000000000')
		ent_5.delete(65, 78)
		ent_5.insert(65, ztext46[0])

	if image_num == 1:
		ent_5.delete(65, 78)
		ent_5.insert(65, '0000000000000')
		ent_5.delete(65, 78)
		ent_5.insert(65, ztext46[1])

	if image_num == 2:
		ent_5.delete(65, 78)
		ent_5.insert(65, '0000000000000')
		ent_5.delete(65, 78)
		ent_5.insert(65, ztext46[2])

	if image_num == 3:
		ent_5.delete(65, 78)
		ent_5.insert(65, '0000000000000')
		ent_5.delete(65, 78)
		ent_5.insert(65, ztext46[3])

	if image_num == 4:
		ent_5.delete(65, 78)
		ent_5.insert(65, '0000000000000')
		ent_5.delete(65, 78)
		ent_5.insert(65, ztext46[4])

def forward47(image_num):
	global b_47
	b_47.grid_forget()
	b_47 = Button(but_frame, image = image_list[image_num-1],command=lambda: forward47(image_num+1))
	b_47.grid(row=4, column=6)

	if image_num == 4:
		b_47 = Button(but_frame, image = img_0, command = lambda:forward47(0))
		b_47.grid(row=4, column=6)

	if image_num == 0:
		ent_5.delete(78, 91)
		ent_5.insert(78, '0000000000000')
		ent_5.delete(78, 91)
		ent_5.insert(78, ztext47[0])

	if image_num == 1:
		ent_5.delete(78, 91)
		ent_5.insert(78, '0000000000000')
		ent_5.delete(78, 91)
		ent_5.insert(78, ztext47[1])

	if image_num == 2:
		ent_5.delete(78, 91)
		ent_5.insert(78, '0000000000000')
		ent_5.delete(78, 91)
		ent_5.insert(78, ztext47[2])

	if image_num == 3:
		ent_5.delete(78, 91)
		ent_5.insert(78, '0000000000000')
		ent_5.delete(78, 91)
		ent_5.insert(78, ztext47[3])

	if image_num == 4:
		ent_5.delete(78, 91)
		ent_5.insert(78, '0000000000000')
		ent_5.delete(78, 91)
		ent_5.insert(78, ztext47[4])

def forward48(image_num):
	global b_48
	b_48.grid_forget()
	b_48 = Button(but_frame, image = image_list[image_num-1],command=lambda: forward48(image_num+1))
	b_48.grid(row=4, column=7)

	if image_num == 4:
		b_48 = Button(but_frame, image = img_0, command = lambda:forward48(0))
		b_48.grid(row=4, column=7)

	if image_num == 0:
		ent_5.delete(91, 104)
		ent_5.insert(91, '0000000000000')
		ent_5.delete(91, 104)
		ent_5.insert(91, ztext48[0])

	if image_num == 1:
		ent_5.delete(91, 104)
		ent_5.insert(91, '0000000000000')
		ent_5.delete(91, 104)
		ent_5.insert(91, ztext48[1])

	if image_num == 2:
		ent_5.delete(91, 104)
		ent_5.insert(91, '0000000000000')
		ent_5.delete(91, 104)
		ent_5.insert(91, ztext48[2])

	if image_num == 3:
		ent_5.delete(91, 104)
		ent_5.insert(91, '0000000000000')
		ent_5.delete(91, 104)
		ent_5.insert(91, ztext48[3])

	if image_num == 4:
		ent_5.delete(91, 104)
		ent_5.insert(91, '0000000000000')
		ent_5.delete(91, 104)
		ent_5.insert(91, ztext48[4])

def forward49(image_num):
	global b_49
	b_49.grid_forget()
	b_49 = Button(but_frame, image = image_list[image_num-1],command=lambda: forward49(image_num+1))
	b_49.grid(row=4, column=8)

	if image_num == 4:
		b_49 = Button(but_frame, image = img_0, command = lambda:forward49(0))
		b_49.grid(row=4, column=8)

	if image_num == 0:
		ent_5.delete(104, 117)
		ent_5.insert(104, '0000000000000')
		ent_5.delete(104, 117)
		ent_5.insert(104, ztext49[0])

	if image_num == 1:
		ent_5.delete(104, 117)
		ent_5.insert(104, '0000000000000')
		ent_5.delete(104, 117)
		ent_5.insert(104, ztext49[1])

	if image_num == 2:
		ent_5.delete(104, 117)
		ent_5.insert(104, '0000000000000')
		ent_5.delete(104, 117)
		ent_5.insert(104, ztext49[2])

	if image_num == 3:
		ent_5.delete(104, 117)
		ent_5.insert(104, '0000000000000')
		ent_5.delete(104, 117)
		ent_5.insert(104, ztext49[3])

	if image_num == 4:
		ent_5.delete(104, 117)
		ent_5.insert(104, '0000000000000')
		ent_5.delete(104, 117)
		ent_5.insert(104, ztext49[4])

def forward50(image_num):
	global b_50
	b_50.grid_forget()
	b_50 = Button(but_frame, image = image_list[image_num-1],command=lambda: forward50(image_num+1))
	b_50.grid(row=4, column=9)

	if image_num == 4:
		b_50 = Button(but_frame, image = img_0, command = lambda:forward50(0))
		b_50.grid(row=4, column=9)

	if image_num == 0:
		ent_5.delete(117, 130)
		ent_5.insert(117, '0000000000000')
		ent_5.delete(117, 130)
		ent_5.insert(117, ztext50[0])

	if image_num == 1:
		ent_5.delete(117, 130)
		ent_5.insert(117, '0000000000000')
		ent_5.delete(117, 130)
		ent_5.insert(117, ztext50[1])

	if image_num == 2:
		ent_5.delete(117, 130)
		ent_5.insert(117, '0000000000000')
		ent_5.delete(117, 130)
		ent_5.insert(117, ztext50[2])

	if image_num == 3:
		ent_5.delete(117, 130)
		ent_5.insert(117, '0000000000000')
		ent_5.delete(117, 130)
		ent_5.insert(117, ztext50[3])

	if image_num == 4:
		ent_5.delete(117, 130)
		ent_5.insert(117, '0000000000000')
		ent_5.delete(117, 130)
		ent_5.insert(117, ztext50[4])
#50
def forward51(image_num):
	global b_51
	b_51.grid_forget()
	b_51 = Button(but_frame, image = image_list[image_num-1],command=lambda: forward51(image_num+1))
	b_51.grid(row=5, column=0)

	if image_num == 4:
		b_51 = Button(but_frame, image = img_0, command = lambda:forward51(0))
		b_51.grid(row=5, column=0)

	if image_num == 0:
		ent_6.delete(0,13)
		ent_6.insert(0, '0000000000000')
		ent_6.delete(0, 13)
		ent_6.insert(0, ztext51[0])

	if image_num == 1:
		ent_6.delete(0,13)
		ent_6.insert(0, '0000000000000')
		ent_6.delete(0, 13)
		ent_6.insert(0, ztext51[1])

	if image_num == 2:
		ent_6.delete(0,13)
		ent_6.insert(0, '0000000000000')
		ent_6.delete(0, 13)
		ent_6.insert(0, ztext51[2])

	if image_num == 3:
		ent_6.delete(0,13)
		ent_6.insert(0, '0000000000000')
		ent_6.delete(0, 13)
		ent_6.insert(0, ztext51[3])

	if image_num == 4:
		ent_6.delete(0,13)
		ent_6.insert(0, '0000000000000')
		ent_6.delete(0, 13)
		ent_6.insert(0, ztext51[4])

def forward52(image_num):
	global b_52
	b_52.grid_forget()
	b_52 = Button(but_frame, image = image_list[image_num-1],command=lambda: forward52(image_num+1))
	b_52.grid(row=5, column=1)

	if image_num == 4:
		b_52 = Button(but_frame, image = img_0, command = lambda:forward52(0))
		b_52.grid(row=5, column=1)

	if image_num == 0:
		ent_6.delete(13, 26)
		ent_6.insert(13, '0000000000000')
		ent_6.delete(13, 26)
		ent_6.insert(13, ztext52[0])

	if image_num == 1:
		ent_6.delete(13, 26)
		ent_6.insert(13, '0000000000000')
		ent_6.delete(13, 26)
		ent_6.insert(13, ztext52[1])

	if image_num == 2:
		ent_6.delete(13, 26)
		ent_6.insert(13, '0000000000000')
		ent_6.delete(13, 26)
		ent_6.insert(13, ztext52[2])

	if image_num == 3:
		ent_6.delete(13, 26)
		ent_6.insert(13, '0000000000000')
		ent_6.delete(13, 26)
		ent_6.insert(13, ztext52[3])

	if image_num == 4:
		ent_6.delete(13, 26)
		ent_6.insert(13, '0000000000000')
		ent_6.delete(13, 26)
		ent_6.insert(13, ztext52[4])

def forward53(image_num):
	global b_53
	b_53.grid_forget()
	b_53 = Button(but_frame, image = image_list[image_num-1],command=lambda: forward53(image_num+1))
	b_53.grid(row=5, column=2)

	if image_num == 4:
		b_53 = Button(but_frame, image = img_0, command = lambda:forward53(0))
		b_53.grid(row=5, column=2)

	if image_num == 0:
		ent_6.delete(26, 39)
		ent_6.insert(26, '0000000000000')
		ent_6.delete(26, 39)
		ent_6.insert(26, ztext53[0])

	if image_num == 1:
		ent_6.delete(26, 39)
		ent_6.insert(26, '0000000000000')
		ent_6.delete(26, 39)
		ent_6.insert(26, ztext53[1])

	if image_num == 2:
		ent_6.delete(26, 39)
		ent_6.insert(26, '0000000000000')
		ent_6.delete(26, 39)
		ent_6.insert(26, ztext53[2])

	if image_num == 3:
		ent_6.delete(26, 39)
		ent_6.insert(26, '0000000000000')
		ent_6.delete(26, 39)
		ent_6.insert(26, ztext53[3])

	if image_num == 4:
		ent_6.delete(26, 39)
		ent_6.insert(26, '0000000000000')
		ent_6.delete(26, 39)
		ent_6.insert(26, ztext53[4])

def forward54(image_num):
	global b_54
	b_54.grid_forget()
	b_54 = Button(but_frame, image = image_list[image_num-1],command=lambda: forward54(image_num+1))
	b_54.grid(row=5, column=3)

	if image_num == 4:
		b_54 = Button(but_frame, image = img_0, command = lambda:forward54(0))
		b_54.grid(row=5, column=3)

	if image_num == 0:
		ent_6.delete(39, 52)
		ent_6.insert(39, '0000000000000')
		ent_6.delete(39, 52)
		ent_6.insert(39, ztext54[0])

	if image_num == 1:
		ent_6.delete(39, 52)
		ent_6.insert(39, '0000000000000')
		ent_6.delete(39, 52)
		ent_6.insert(39, ztext54[1])

	if image_num == 2:
		ent_6.delete(39, 52)
		ent_6.insert(39, '0000000000000')
		ent_6.delete(39, 52)
		ent_6.insert(39, ztext54[2])

	if image_num == 3:
		ent_6.delete(39, 52)
		ent_6.insert(39, '0000000000000')
		ent_6.delete(39, 52)
		ent_6.insert(39, ztext54[3])

	if image_num == 4:
		ent_6.delete(39, 52)
		ent_6.insert(39, '0000000000000')
		ent_6.delete(39, 52)
		ent_6.insert(39, ztext54[4])

def forward55(image_num):
	global b_55
	b_55.grid_forget()
	b_55 = Button(but_frame, image = image_list[image_num-1],command=lambda: forward55(image_num+1))
	b_55.grid(row=5, column=4)

	if image_num == 4:
		b_55 = Button(but_frame, image = img_0, command = lambda:forward55(0))
		b_55.grid(row=5, column=4)

	if image_num == 0:
		ent_6.delete(52, 65)
		ent_6.insert(52, '0000000000000')
		ent_6.delete(52, 65)
		ent_6.insert(52, ztext55[0])

	if image_num == 1:
		ent_6.delete(52, 65)
		ent_6.insert(52, '0000000000000')
		ent_6.delete(52, 65)
		ent_6.insert(52, ztext55[1])

	if image_num == 2:
		ent_6.delete(52, 65)
		ent_6.insert(52, '0000000000000')
		ent_6.delete(52, 65)
		ent_6.insert(52, ztext55[2])

	if image_num == 3:
		ent_6.delete(52, 65)
		ent_6.insert(52, '0000000000000')
		ent_6.delete(52, 65)
		ent_6.insert(52, ztext55[3])

	if image_num == 4:
		ent_6.delete(52, 65)
		ent_6.insert(52, '0000000000000')
		ent_6.delete(52, 65)
		ent_6.insert(52, ztext55[4])

def forward56(image_num):
	global b_56
	b_56.grid_forget()
	b_56 = Button(but_frame, image = image_list[image_num-1],command=lambda: forward56(image_num+1))
	b_56.grid(row=5, column=5)

	if image_num == 4:
		b_56 = Button(but_frame, image = img_0, command = lambda:forward56(0))
		b_56.grid(row=5, column=5)

	if image_num == 0:
		ent_6.delete(65, 78)
		ent_6.insert(65, '0000000000000')
		ent_6.delete(65, 78)
		ent_6.insert(65, ztext56[0])

	if image_num == 1:
		ent_6.delete(65, 78)
		ent_6.insert(65, '0000000000000')
		ent_6.delete(65, 78)
		ent_6.insert(65, ztext56[1])

	if image_num == 2:
		ent_6.delete(65, 78)
		ent_6.insert(65, '0000000000000')
		ent_6.delete(65, 78)
		ent_6.insert(65, ztext56[2])

	if image_num == 3:
		ent_6.delete(65, 78)
		ent_6.insert(65, '0000000000000')
		ent_6.delete(65, 78)
		ent_6.insert(65, ztext56[3])

	if image_num == 4:
		ent_6.delete(65, 78)
		ent_6.insert(65, '0000000000000')
		ent_6.delete(65, 78)
		ent_6.insert(65, ztext56[4])

def forward57(image_num):
	global b_57
	b_57.grid_forget()
	b_57 = Button(but_frame, image = image_list[image_num-1],command=lambda: forward57(image_num+1))
	b_57.grid(row=5, column=6)

	if image_num == 4:
		b_57 = Button(but_frame, image = img_0, command = lambda:forward57(0))
		b_57.grid(row=5, column=6)

	if image_num == 0:
		ent_6.delete(78, 91)
		ent_6.insert(78, '0000000000000')
		ent_6.delete(78, 91)
		ent_6.insert(78, ztext57[0])

	if image_num == 1:
		ent_6.delete(78, 91)
		ent_6.insert(78, '0000000000000')
		ent_6.delete(78, 91)
		ent_6.insert(78, ztext57[1])

	if image_num == 2:
		ent_6.delete(78, 91)
		ent_6.insert(78, '0000000000000')
		ent_6.delete(78, 91)
		ent_6.insert(78, ztext57[2])

	if image_num == 3:
		ent_6.delete(78, 91)
		ent_6.insert(78, '0000000000000')
		ent_6.delete(78, 91)
		ent_6.insert(78, ztext57[3])

	if image_num == 4:
		ent_6.delete(78, 91)
		ent_6.insert(78, '0000000000000')
		ent_6.delete(78, 91)
		ent_6.insert(78, ztext57[4])

def forward58(image_num):
	global b_58
	b_58.grid_forget()
	b_58 = Button(but_frame, image = image_list[image_num-1],command=lambda: forward58(image_num+1))
	b_58.grid(row=5, column=7)

	if image_num == 4:
		b_58 = Button(but_frame, image = img_0, command = lambda:forward58(0))
		b_58.grid(row=5, column=7)

	if image_num == 0:
		ent_6.delete(91, 104)
		ent_6.insert(91, '0000000000000')
		ent_6.delete(91, 104)
		ent_6.insert(91, ztext58[0])

	if image_num == 1:
		ent_6.delete(91, 104)
		ent_6.insert(91, '0000000000000')
		ent_6.delete(91, 104)
		ent_6.insert(91, ztext58[1])

	if image_num == 2:
		ent_6.delete(91, 104)
		ent_6.insert(91, '0000000000000')
		ent_6.delete(91, 104)
		ent_6.insert(91, ztext58[2])

	if image_num == 3:
		ent_6.delete(91, 104)
		ent_6.insert(91, '0000000000000')
		ent_6.delete(91, 104)
		ent_6.insert(91, ztext58[3])

	if image_num == 4:
		ent_6.delete(91, 104)
		ent_6.insert(91, '0000000000000')
		ent_6.delete(91, 104)
		ent_6.insert(91, ztext58[4])

def forward59(image_num):
	global b_59
	b_59.grid_forget()
	b_59 = Button(but_frame, image = image_list[image_num-1],command=lambda: forward59(image_num+1))
	b_59.grid(row=5, column=8)

	if image_num == 4:
		b_59 = Button(but_frame, image = img_0, command = lambda:forward59(0))
		b_59.grid(row=5, column=8)

	if image_num == 0:
		ent_6.delete(104, 117)
		ent_6.insert(104, '0000000000000')
		ent_6.delete(104, 117)
		ent_6.insert(104, ztext59[0])

	if image_num == 1:
		ent_6.delete(104, 117)
		ent_6.insert(104, '0000000000000')
		ent_6.delete(104, 117)
		ent_6.insert(104, ztext59[1])

	if image_num == 2:
		ent_6.delete(104, 117)
		ent_6.insert(104, '0000000000000')
		ent_6.delete(104, 117)
		ent_6.insert(104, ztext59[2])

	if image_num == 3:
		ent_6.delete(104, 117)
		ent_6.insert(104, '0000000000000')
		ent_6.delete(104, 117)
		ent_6.insert(104, ztext59[3])

	if image_num == 4:
		ent_6.delete(104, 117)
		ent_6.insert(104, '0000000000000')
		ent_6.delete(104, 117)
		ent_6.insert(104, ztext59[4])

def forward60(image_num):
	global b_60
	b_60.grid_forget()
	b_60 = Button(but_frame, image = image_list[image_num-1],command=lambda: forward60(image_num+1))
	b_60.grid(row=5, column=9)

	if image_num == 4:
		b_60 = Button(but_frame, image = img_0, command = lambda:forward60(0))
		b_60.grid(row=5, column=9)

	if image_num == 0:
		ent_6.delete(117, 130)
		ent_6.insert(117, '0000000000000')
		ent_6.delete(117, 130)
		ent_6.insert(117, ztext60[0])

	if image_num == 1:
		ent_6.delete(117, 130)
		ent_6.insert(117, '0000000000000')
		ent_6.delete(117, 130)
		ent_6.insert(117, ztext60[1])

	if image_num == 2:
		ent_6.delete(117, 130)
		ent_6.insert(117, '0000000000000')
		ent_6.delete(117, 130)
		ent_6.insert(117, ztext60[2])

	if image_num == 3:
		ent_6.delete(117, 130)
		ent_6.insert(117, '0000000000000')
		ent_6.delete(117, 130)
		ent_6.insert(117, ztext60[3])

	if image_num == 4:
		ent_6.delete(117, 130)
		ent_6.insert(117, '0000000000000')
		ent_6.delete(117, 130)
		ent_6.insert(117, ztext60[4])
#60
def forward61(image_num):
	global b_61
	b_61.grid_forget()
	b_61 = Button(but_frame, image = image_list[image_num-1],command=lambda: forward61(image_num+1))
	b_61.grid(row=6, column=0)

	if image_num == 4:
		b_61 = Button(but_frame, image = img_0, command = lambda:forward61(0))
		b_61.grid(row=6, column=0)

	if image_num == 0:
		ent_7.delete(0,13)
		ent_7.insert(0, '0000000000000')
		ent_7.delete(0, 13)
		ent_7.insert(0, ztext61[0])

	if image_num == 1:
		ent_7.delete(0,13)
		ent_7.insert(0, '0000000000000')
		ent_7.delete(0, 13)
		ent_7.insert(0, ztext61[1])

	if image_num == 2:
		ent_7.delete(0,13)
		ent_7.insert(0, '0000000000000')
		ent_7.delete(0, 13)
		ent_7.insert(0, ztext61[2])

	if image_num == 3:
		ent_7.delete(0,13)
		ent_7.insert(0, '0000000000000')
		ent_7.delete(0, 13)
		ent_7.insert(0, ztext61[3])

	if image_num == 4:
		ent_7.delete(0,13)
		ent_7.insert(0, '0000000000000')
		ent_7.delete(0, 13)
		ent_7.insert(0, ztext61[4])

def forward62(image_num):
	global b_62
	b_62.grid_forget()
	b_62 = Button(but_frame, image = image_list[image_num-1],command=lambda: forward62(image_num+1))
	b_62.grid(row=6, column=1)

	if image_num == 4:
		b_62 = Button(but_frame, image = img_0, command = lambda:forward62(0))
		b_62.grid(row=6, column=1)

	if image_num == 0:
		ent_7.delete(13, 26)
		ent_7.insert(13, '0000000000000')
		ent_7.delete(13, 26)
		ent_7.insert(13, ztext62[0])

	if image_num == 1:
		ent_7.delete(13, 26)
		ent_7.insert(13, '0000000000000')
		ent_7.delete(13, 26)
		ent_7.insert(13, ztext62[1])

	if image_num == 2:
		ent_7.delete(13, 26)
		ent_7.insert(13, '0000000000000')
		ent_7.delete(13, 26)
		ent_7.insert(13, ztext62[2])

	if image_num == 3:
		ent_7.delete(13, 26)
		ent_7.insert(13, '0000000000000')
		ent_7.delete(13, 26)
		ent_7.insert(13, ztext62[3])

	if image_num == 4:
		ent_7.delete(13, 26)
		ent_7.insert(13, '0000000000000')
		ent_7.delete(13, 26)
		ent_7.insert(13, ztext62[4])

def forward63(image_num):
	global b_63
	b_63.grid_forget()
	b_63 = Button(but_frame, image = image_list[image_num-1],command=lambda: forward63(image_num+1))
	b_63.grid(row=6, column=2)

	if image_num == 4:
		b_63 = Button(but_frame, image = img_0, command = lambda:forward63(0))
		b_63.grid(row=6, column=2)

	if image_num == 0:
		ent_7.delete(26, 39)
		ent_7.insert(26, '0000000000000')
		ent_7.delete(26, 39)
		ent_7.insert(26, ztext63[0])

	if image_num == 1:
		ent_7.delete(26, 39)
		ent_7.insert(26, '0000000000000')
		ent_7.delete(26, 39)
		ent_7.insert(26, ztext63[1])

	if image_num == 2:
		ent_7.delete(26, 39)
		ent_7.insert(26, '0000000000000')
		ent_7.delete(26, 39)
		ent_7.insert(26, ztext63[2])

	if image_num == 3:
		ent_7.delete(26, 39)
		ent_7.insert(26, '0000000000000')
		ent_7.delete(26, 39)
		ent_7.insert(26, ztext63[3])

	if image_num == 4:
		ent_7.delete(26, 39)
		ent_7.insert(26, '0000000000000')
		ent_7.delete(26, 39)
		ent_7.insert(26, ztext63[4])

def forward64(image_num):
	global b_64
	b_64.grid_forget()
	b_64 = Button(but_frame, image = image_list[image_num-1],command=lambda: forward64(image_num+1))
	b_64.grid(row=6, column=3)

	if image_num == 4:
		b_64 = Button(but_frame, image = img_0, command = lambda:forward64(0))
		b_64.grid(row=6, column=3)

	if image_num == 0:
		ent_7.delete(39, 52)
		ent_7.insert(39, '0000000000000')
		ent_7.delete(39, 52)
		ent_7.insert(39, ztext64[0])

	if image_num == 1:
		ent_7.delete(39, 52)
		ent_7.insert(39, '0000000000000')
		ent_7.delete(39, 52)
		ent_7.insert(39, ztext64[1])

	if image_num == 2:
		ent_7.delete(39, 52)
		ent_7.insert(39, '0000000000000')
		ent_7.delete(39, 52)
		ent_7.insert(39, ztext64[2])

	if image_num == 3:
		ent_7.delete(39, 52)
		ent_7.insert(39, '0000000000000')
		ent_7.delete(39, 52)
		ent_7.insert(39, ztext64[3])

	if image_num == 4:
		ent_7.delete(39, 52)
		ent_7.insert(39, '0000000000000')
		ent_7.delete(39, 52)
		ent_7.insert(39, ztext64[4])

def forward65(image_num):
	global b_65
	b_65.grid_forget()
	b_65 = Button(but_frame, image = image_list[image_num-1],command=lambda: forward65(image_num+1))
	b_65.grid(row=6, column=4)

	if image_num == 4:
		b_65 = Button(but_frame, image = img_0, command = lambda:forward65(0))
		b_65.grid(row=6, column=4)

	if image_num == 0:
		ent_7.delete(52, 65)
		ent_7.insert(52, '0000000000000')
		ent_7.delete(52, 65)
		ent_7.insert(52, ztext65[0])

	if image_num == 1:
		ent_7.delete(52, 65)
		ent_7.insert(52, '0000000000000')
		ent_7.delete(52, 65)
		ent_7.insert(52, ztext65[1])

	if image_num == 2:
		ent_7.delete(52, 65)
		ent_7.insert(52, '0000000000000')
		ent_7.delete(52, 65)
		ent_7.insert(52, ztext65[2])

	if image_num == 3:
		ent_7.delete(52, 65)
		ent_7.insert(52, '0000000000000')
		ent_7.delete(52, 65)
		ent_7.insert(52, ztext65[3])

	if image_num == 4:
		ent_7.delete(52, 65)
		ent_7.insert(52, '0000000000000')
		ent_7.delete(52, 65)
		ent_7.insert(52, ztext65[4])

def forward66(image_num):
	global b_66
	b_66.grid_forget()
	b_66 = Button(but_frame, image = image_list[image_num-1],command=lambda: forward66(image_num+1))
	b_66.grid(row=6, column=5)

	if image_num == 4:
		b_66 = Button(but_frame, image = img_0, command = lambda:forward66(0))
		b_66.grid(row=6, column=5)

	if image_num == 0:
		ent_7.delete(65, 78)
		ent_7.insert(65, '0000000000000')
		ent_7.delete(65, 78)
		ent_7.insert(65, ztext66[0])

	if image_num == 1:
		ent_7.delete(65, 78)
		ent_7.insert(65, '0000000000000')
		ent_7.delete(65, 78)
		ent_7.insert(65, ztext66[1])

	if image_num == 2:
		ent_7.delete(65, 78)
		ent_7.insert(65, '0000000000000')
		ent_7.delete(65, 78)
		ent_7.insert(65, ztext66[2])

	if image_num == 3:
		ent_7.delete(65, 78)
		ent_7.insert(65, '0000000000000')
		ent_7.delete(65, 78)
		ent_7.insert(65, ztext66[3])

	if image_num == 4:
		ent_7.delete(65, 78)
		ent_7.insert(65, '0000000000000')
		ent_7.delete(65, 78)
		ent_7.insert(65, ztext66[4])

def forward67(image_num):
	global b_67
	b_67.grid_forget()
	b_67 = Button(but_frame, image = image_list[image_num-1],command=lambda: forward67(image_num+1))
	b_67.grid(row=6, column=6)

	if image_num == 4:
		b_67 = Button(but_frame, image = img_0, command = lambda:forward67(0))
		b_67.grid(row=6, column=6)

	if image_num == 0:
		ent_7.delete(78, 91)
		ent_7.insert(78, '0000000000000')
		ent_7.delete(78, 91)
		ent_7.insert(78, ztext67[0])

	if image_num == 1:
		ent_7.delete(78, 91)
		ent_7.insert(78, '0000000000000')
		ent_7.delete(78, 91)
		ent_7.insert(78, ztext67[1])

	if image_num == 2:
		ent_7.delete(78, 91)
		ent_7.insert(78, '0000000000000')
		ent_7.delete(78, 91)
		ent_7.insert(78, ztext67[2])

	if image_num == 3:
		ent_7.delete(78, 91)
		ent_7.insert(78, '0000000000000')
		ent_7.delete(78, 91)
		ent_7.insert(78, ztext67[3])

	if image_num == 4:
		ent_7.delete(78, 91)
		ent_7.insert(78, '0000000000000')
		ent_7.delete(78, 91)
		ent_7.insert(78, ztext67[4])

def forward68(image_num):
	global b_68
	b_68.grid_forget()
	b_68 = Button(but_frame, image = image_list[image_num-1],command=lambda: forward68(image_num+1))
	b_68.grid(row=6, column=7)

	if image_num == 4:
		b_68 = Button(but_frame, image = img_0, command = lambda:forward68(0))
		b_68.grid(row=6, column=7)

	if image_num == 0:
		ent_7.delete(91, 104)
		ent_7.insert(91, '0000000000000')
		ent_7.delete(91, 104)
		ent_7.insert(91, ztext68[0])

	if image_num == 1:
		ent_7.delete(91, 104)
		ent_7.insert(91, '0000000000000')
		ent_7.delete(91, 104)
		ent_7.insert(91, ztext68[1])

	if image_num == 2:
		ent_7.delete(91, 104)
		ent_7.insert(91, '0000000000000')
		ent_7.delete(91, 104)
		ent_7.insert(91, ztext68[2])

	if image_num == 3:
		ent_7.delete(91, 104)
		ent_7.insert(91, '0000000000000')
		ent_7.delete(91, 104)
		ent_7.insert(91, ztext68[3])

	if image_num == 4:
		ent_7.delete(91, 104)
		ent_7.insert(91, '0000000000000')
		ent_7.delete(91, 104)
		ent_7.insert(91, ztext68[4])

def forward69(image_num):
	global b_69
	b_69.grid_forget()
	b_69 = Button(but_frame, image = image_list[image_num-1],command=lambda: forward69(image_num+1))
	b_69.grid(row=6, column=8)

	if image_num == 4:
		b_69 = Button(but_frame, image = img_0, command = lambda:forward69(0))
		b_69.grid(row=6, column=8)

	if image_num == 0:
		ent_7.delete(104, 117)
		ent_7.insert(104, '0000000000000')
		ent_7.delete(104, 117)
		ent_7.insert(104, ztext69[0])

	if image_num == 1:
		ent_7.delete(104, 117)
		ent_7.insert(104, '0000000000000')
		ent_7.delete(104, 117)
		ent_7.insert(104, ztext69[1])

	if image_num == 2:
		ent_7.delete(104, 117)
		ent_7.insert(104, '0000000000000')
		ent_7.delete(104, 117)
		ent_7.insert(104, ztext69[2])

	if image_num == 3:
		ent_7.delete(104, 117)
		ent_7.insert(104, '0000000000000')
		ent_7.delete(104, 117)
		ent_7.insert(104, ztext69[3])

	if image_num == 4:
		ent_7.delete(104, 117)
		ent_7.insert(104, '0000000000000')
		ent_7.delete(104, 117)
		ent_7.insert(104, ztext69[4])

def forward70(image_num):
	global b_70
	b_70.grid_forget()
	b_70 = Button(but_frame, image = image_list[image_num-1],command=lambda: forward70(image_num+1))
	b_70.grid(row=6, column=9)

	if image_num == 4:
		b_70 = Button(but_frame, image = img_0, command = lambda:forward70(0))
		b_70.grid(row=6, column=9)

	if image_num == 0:
		ent_7.delete(117, 130)
		ent_7.insert(117, '0000000000000')
		ent_7.delete(117, 130)
		ent_7.insert(117, ztext70[0])

	if image_num == 1:
		ent_7.delete(117, 130)
		ent_7.insert(117, '0000000000000')
		ent_7.delete(117, 130)
		ent_7.insert(117, ztext70[1])

	if image_num == 2:
		ent_7.delete(117, 130)
		ent_7.insert(117, '0000000000000')
		ent_7.delete(117, 130)
		ent_7.insert(117, ztext70[2])

	if image_num == 3:
		ent_7.delete(117, 130)
		ent_7.insert(117, '0000000000000')
		ent_7.delete(117, 130)
		ent_7.insert(117, ztext70[3])

	if image_num == 4:
		ent_7.delete(117, 130)
		ent_7.insert(117, '0000000000000')
		ent_7.delete(117, 130)
		ent_7.insert(117, ztext70[4])
#70
def forward71(image_num):
	global b_71
	b_71.grid_forget()
	b_71 = Button(but_frame, image = image_list[image_num-1],command=lambda: forward71(image_num+1))
	b_71.grid(row=7, column=0)

	if image_num == 4:
		b_71 = Button(but_frame, image = img_0, command = lambda:forward71(0))
		b_71.grid(row=7, column=0)

	if image_num == 0:
		ent_8.delete(0,13)
		ent_8.insert(0, '0000000000000')
		ent_8.delete(0, 13)
		ent_8.insert(0, ztext71[0])

	if image_num == 1:
		ent_8.delete(0,13)
		ent_8.insert(0, '0000000000000')
		ent_8.delete(0, 13)
		ent_8.insert(0, ztext71[1])

	if image_num == 2:
		ent_8.delete(0,13)
		ent_8.insert(0, '0000000000000')
		ent_8.delete(0, 13)
		ent_8.insert(0, ztext71[2])

	if image_num == 3:
		ent_8.delete(0,13)
		ent_8.insert(0, '0000000000000')
		ent_8.delete(0, 13)
		ent_8.insert(0, ztext71[3])

	if image_num == 4:
		ent_8.delete(0,13)
		ent_8.insert(0, '0000000000000')
		ent_8.delete(0, 13)
		ent_8.insert(0, ztext71[4])

def forward72(image_num):
	global b_72
	b_72.grid_forget()
	b_72 = Button(but_frame, image = image_list[image_num-1],command=lambda: forward72(image_num+1))
	b_72.grid(row=7, column=1)

	if image_num == 4:
		b_72 = Button(but_frame, image = img_0, command = lambda:forward72(0))
		b_72.grid(row=7, column=1)

	if image_num == 0:
		ent_8.delete(13, 26)
		ent_8.insert(13, '0000000000000')
		ent_8.delete(13, 26)
		ent_8.insert(13, ztext72[0])

	if image_num == 1:
		ent_8.delete(13, 26)
		ent_8.insert(13, '0000000000000')
		ent_8.delete(13, 26)
		ent_8.insert(13, ztext72[1])

	if image_num == 2:
		ent_8.delete(13, 26)
		ent_8.insert(13, '0000000000000')
		ent_8.delete(13, 26)
		ent_8.insert(13, ztext72[2])

	if image_num == 3:
		ent_8.delete(13, 26)
		ent_8.insert(13, '0000000000000')
		ent_8.delete(13, 26)
		ent_8.insert(13, ztext72[3])

	if image_num == 4:
		ent_8.delete(13, 26)
		ent_8.insert(13, '0000000000000')
		ent_8.delete(13, 26)
		ent_8.insert(13, ztext72[4])

def forward73(image_num):
	global b_73
	b_73.grid_forget()
	b_73 = Button(but_frame, image = image_list[image_num-1],command=lambda: forward73(image_num+1))
	b_73.grid(row=7, column=2)

	if image_num == 4:
		b_73 = Button(but_frame, image = img_0, command = lambda:forward73(0))
		b_73.grid(row=7, column=2)

	if image_num == 0:
		ent_8.delete(26, 39)
		ent_8.insert(26, '0000000000000')
		ent_8.delete(26, 39)
		ent_8.insert(26, ztext73[0])

	if image_num == 1:
		ent_8.delete(26, 39)
		ent_8.insert(26, '0000000000000')
		ent_8.delete(26, 39)
		ent_8.insert(26, ztext73[1])

	if image_num == 2:
		ent_8.delete(26, 39)
		ent_8.insert(26, '0000000000000')
		ent_8.delete(26, 39)
		ent_8.insert(26, ztext73[2])

	if image_num == 3:
		ent_8.delete(26, 39)
		ent_8.insert(26, '0000000000000')
		ent_8.delete(26, 39)
		ent_8.insert(26, ztext73[3])

	if image_num == 4:
		ent_8.delete(26, 39)
		ent_8.insert(26, '0000000000000')
		ent_8.delete(26, 39)
		ent_8.insert(26, ztext73[4])

def forward74(image_num):
	global b_74
	b_74.grid_forget()
	b_74 = Button(but_frame, image = image_list[image_num-1],command=lambda: forward74(image_num+1))
	b_74.grid(row=7, column=3)

	if image_num == 4:
		b_74 = Button(but_frame, image = img_0, command = lambda:forward74(0))
		b_74.grid(row=7, column=3)

	if image_num == 0:
		ent_8.delete(39, 52)
		ent_8.insert(39, '0000000000000')
		ent_8.delete(39, 52)
		ent_8.insert(39, ztext74[0])

	if image_num == 1:
		ent_8.delete(39, 52)
		ent_8.insert(39, '0000000000000')
		ent_8.delete(39, 52)
		ent_8.insert(39, ztext74[1])

	if image_num == 2:
		ent_8.delete(39, 52)
		ent_8.insert(39, '0000000000000')
		ent_8.delete(39, 52)
		ent_8.insert(39, ztext74[2])

	if image_num == 3:
		ent_8.delete(39, 52)
		ent_8.insert(39, '0000000000000')
		ent_8.delete(39, 52)
		ent_8.insert(39, ztext74[3])

	if image_num == 4:
		ent_8.delete(39, 52)
		ent_8.insert(39, '0000000000000')
		ent_8.delete(39, 52)
		ent_8.insert(39, ztext74[4])

def forward75(image_num):
	global b_75
	b_75.grid_forget()
	b_75 = Button(but_frame, image = image_list[image_num-1],command=lambda: forward75(image_num+1))
	b_75.grid(row=7, column=4)

	if image_num == 4:
		b_75 = Button(but_frame, image = img_0, command = lambda:forward75(0))
		b_75.grid(row=7, column=4)

	if image_num == 0:
		ent_8.delete(52, 65)
		ent_8.insert(52, '0000000000000')
		ent_8.delete(52, 65)
		ent_8.insert(52, ztext75[0])

	if image_num == 1:
		ent_8.delete(52, 65)
		ent_8.insert(52, '0000000000000')
		ent_8.delete(52, 65)
		ent_8.insert(52, ztext75[1])

	if image_num == 2:
		ent_8.delete(52, 65)
		ent_8.insert(52, '0000000000000')
		ent_8.delete(52, 65)
		ent_8.insert(52, ztext75[2])

	if image_num == 3:
		ent_8.delete(52, 65)
		ent_8.insert(52, '0000000000000')
		ent_8.delete(52, 65)
		ent_8.insert(52, ztext75[3])

	if image_num == 4:
		ent_8.delete(52, 65)
		ent_8.insert(52, '0000000000000')
		ent_8.delete(52, 65)
		ent_8.insert(52, ztext75[4])

def forward76(image_num):
	global b_76
	b_76.grid_forget()
	b_76 = Button(but_frame, image = image_list[image_num-1],command=lambda: forward76(image_num+1))
	b_76.grid(row=7, column=5)

	if image_num == 4:
		b_76 = Button(but_frame, image = img_0, command = lambda:forward76(0))
		b_76.grid(row=7, column=5)

	if image_num == 0:
		ent_8.delete(65, 78)
		ent_8.insert(65, '0000000000000')
		ent_8.delete(65, 78)
		ent_8.insert(65, ztext76[0])

	if image_num == 1:
		ent_8.delete(65, 78)
		ent_8.insert(65, '0000000000000')
		ent_8.delete(65, 78)
		ent_8.insert(65, ztext76[1])

	if image_num == 2:
		ent_8.delete(65, 78)
		ent_8.insert(65, '0000000000000')
		ent_8.delete(65, 78)
		ent_8.insert(65, ztext76[2])

	if image_num == 3:
		ent_8.delete(65, 78)
		ent_8.insert(65, '0000000000000')
		ent_8.delete(65, 78)
		ent_8.insert(65, ztext76[3])

	if image_num == 4:
		ent_8.delete(65, 78)
		ent_8.insert(65, '0000000000000')
		ent_8.delete(65, 78)
		ent_8.insert(65, ztext76[4])

def forward77(image_num):
	global b_77
	b_77.grid_forget()
	b_77 = Button(but_frame, image = image_list[image_num-1],command=lambda: forward77(image_num+1))
	b_77.grid(row=7, column=6)

	if image_num == 4:
		b_77 = Button(but_frame, image = img_0, command = lambda:forward77(0))
		b_77.grid(row=7, column=6)

	if image_num == 0:
		ent_8.delete(78, 91)
		ent_8.insert(78, '0000000000000')
		ent_8.delete(78, 91)
		ent_8.insert(78, ztext77[0])

	if image_num == 1:
		ent_8.delete(78, 91)
		ent_8.insert(78, '0000000000000')
		ent_8.delete(78, 91)
		ent_8.insert(78, ztext77[1])

	if image_num == 2:
		ent_8.delete(78, 91)
		ent_8.insert(78, '0000000000000')
		ent_8.delete(78, 91)
		ent_8.insert(78, ztext77[2])

	if image_num == 3:
		ent_8.delete(78, 91)
		ent_8.insert(78, '0000000000000')
		ent_8.delete(78, 91)
		ent_8.insert(78, ztext77[3])

	if image_num == 4:
		ent_8.delete(78, 91)
		ent_8.insert(78, '0000000000000')
		ent_8.delete(78, 91)
		ent_8.insert(78, ztext77[4])

def forward78(image_num):
	global b_78
	b_78.grid_forget()
	b_78 = Button(but_frame, image = image_list[image_num-1],command=lambda: forward78(image_num+1))
	b_78.grid(row=7, column=7)

	if image_num == 4:
		b_78 = Button(but_frame, image = img_0, command = lambda:forward78(0))
		b_78.grid(row=7, column=7)

	if image_num == 0:
		ent_8.delete(91, 104)
		ent_8.insert(91, '0000000000000')
		ent_8.delete(91, 104)
		ent_8.insert(91, ztext78[0])

	if image_num == 1:
		ent_8.delete(91, 104)
		ent_8.insert(91, '0000000000000')
		ent_8.delete(91, 104)
		ent_8.insert(91, ztext78[1])

	if image_num == 2:
		ent_8.delete(91, 104)
		ent_8.insert(91, '0000000000000')
		ent_8.delete(91, 104)
		ent_8.insert(91, ztext78[2])

	if image_num == 3:
		ent_8.delete(91, 104)
		ent_8.insert(91, '0000000000000')
		ent_8.delete(91, 104)
		ent_8.insert(91, ztext78[3])

	if image_num == 4:
		ent_8.delete(91, 104)
		ent_8.insert(91, '0000000000000')
		ent_8.delete(91, 104)
		ent_8.insert(91, ztext78[4])

def forward79(image_num):
	global b_79
	b_79.grid_forget()
	b_79 = Button(but_frame, image = image_list[image_num-1],command=lambda: forward79(image_num+1))
	b_79.grid(row=7, column=8)

	if image_num == 4:
		b_79 = Button(but_frame, image = img_0, command = lambda:forward79(0))
		b_79.grid(row=7, column=8)

	if image_num == 0:
		ent_8.delete(104, 117)
		ent_8.insert(104, '0000000000000')
		ent_8.delete(104, 117)
		ent_8.insert(104, ztext79[0])

	if image_num == 1:
		ent_8.delete(104, 117)
		ent_8.insert(104, '0000000000000')
		ent_8.delete(104, 117)
		ent_8.insert(104, ztext79[1])

	if image_num == 2:
		ent_8.delete(104, 117)
		ent_8.insert(104, '0000000000000')
		ent_8.delete(104, 117)
		ent_8.insert(104, ztext79[2])

	if image_num == 3:
		ent_8.delete(104, 117)
		ent_8.insert(104, '0000000000000')
		ent_8.delete(104, 117)
		ent_8.insert(104, ztext79[3])

	if image_num == 4:
		ent_8.delete(104, 117)
		ent_8.insert(104, '0000000000000')
		ent_8.delete(104, 117)
		ent_8.insert(104, ztext79[4])

def forward80(image_num):
	global b_80
	b_80.grid_forget()
	b_80 = Button(but_frame, image = image_list[image_num-1],command=lambda: forward80(image_num+1))
	b_80.grid(row=7, column=9)

	if image_num == 4:
		b_80 = Button(but_frame, image = img_0, command = lambda:forward80(0))
		b_80.grid(row=7, column=9)

	if image_num == 0:
		ent_8.delete(117, 130)
		ent_8.insert(117, '0000000000000')
		ent_8.delete(117, 130)
		ent_8.insert(117, ztext80[0])

	if image_num == 1:
		ent_8.delete(117, 130)
		ent_8.insert(117, '0000000000000')
		ent_8.delete(117, 130)
		ent_8.insert(117, ztext80[1])

	if image_num == 2:
		ent_8.delete(117, 130)
		ent_8.insert(117, '0000000000000')
		ent_8.delete(117, 130)
		ent_8.insert(117, ztext80[2])

	if image_num == 3:
		ent_8.delete(117, 130)
		ent_8.insert(117, '0000000000000')
		ent_8.delete(117, 130)
		ent_8.insert(117, ztext80[3])

	if image_num == 4:
		ent_8.delete(117, 130)
		ent_8.insert(117, '0000000000000')
		ent_8.delete(117, 130)
		ent_8.insert(117, ztext80[4])
#80
def forward81(image_num):
	global b_81
	b_81.grid_forget()
	b_81 = Button(but_frame, image = image_list[image_num-1],command=lambda: forward81(image_num+1))
	b_81.grid(row=8, column=0)

	if image_num == 4:
		b_81 = Button(but_frame, image = img_0, command = lambda:forward81(0))
		b_81.grid(row=8, column=0)

	if image_num == 0:
		ent_9.delete(0,13)
		ent_9.insert(0, '0000000000000')
		ent_9.delete(0, 13)
		ent_9.insert(0, ztext81[0])

	if image_num == 1:
		ent_9.delete(0,13)
		ent_9.insert(0, '0000000000000')
		ent_9.delete(0, 13)
		ent_9.insert(0, ztext81[1])

	if image_num == 2:
		ent_9.delete(0,13)
		ent_9.insert(0, '0000000000000')
		ent_9.delete(0, 13)
		ent_9.insert(0, ztext81[2])

	if image_num == 3:
		ent_9.delete(0,13)
		ent_9.insert(0, '0000000000000')
		ent_9.delete(0, 13)
		ent_9.insert(0, ztext81[3])

	if image_num == 4:
		ent_9.delete(0,13)
		ent_9.insert(0, '0000000000000')
		ent_9.delete(0, 13)
		ent_9.insert(0, ztext81[4])

def forward82(image_num):
	global b_82
	b_82.grid_forget()
	b_82 = Button(but_frame, image = image_list[image_num-1],command=lambda: forward82(image_num+1))
	b_82.grid(row=8, column=1)

	if image_num == 4:
		b_82 = Button(but_frame, image = img_0, command = lambda:forward82(0))
		b_82.grid(row=8, column=1)

	if image_num == 0:
		ent_9.delete(13, 26)
		ent_9.insert(13, '0000000000000')
		ent_9.delete(13, 26)
		ent_9.insert(13, ztext82[0])

	if image_num == 1:
		ent_9.delete(13, 26)
		ent_9.insert(13, '0000000000000')
		ent_9.delete(13, 26)
		ent_9.insert(13, ztext82[1])

	if image_num == 2:
		ent_9.delete(13, 26)
		ent_9.insert(13, '0000000000000')
		ent_9.delete(13, 26)
		ent_9.insert(13, ztext82[2])

	if image_num == 3:
		ent_9.delete(13, 26)
		ent_9.insert(13, '0000000000000')
		ent_9.delete(13, 26)
		ent_9.insert(13, ztext82[3])

	if image_num == 4:
		ent_9.delete(13, 26)
		ent_9.insert(13, '0000000000000')
		ent_9.delete(13, 26)
		ent_9.insert(13, ztext82[4])

def forward83(image_num):
	global b_83
	b_83.grid_forget()
	b_83 = Button(but_frame, image = image_list[image_num-1],command=lambda: forward83(image_num+1))
	b_83.grid(row=8, column=2)

	if image_num == 4:
		b_83 = Button(but_frame, image = img_0, command = lambda:forward83(0))
		b_83.grid(row=8, column=2)

	if image_num == 0:
		ent_9.delete(26, 39)
		ent_9.insert(26, '0000000000000')
		ent_9.delete(26, 39)
		ent_9.insert(26, ztext83[0])

	if image_num == 1:
		ent_9.delete(26, 39)
		ent_9.insert(26, '0000000000000')
		ent_9.delete(26, 39)
		ent_9.insert(26, ztext83[1])

	if image_num == 2:
		ent_9.delete(26, 39)
		ent_9.insert(26, '0000000000000')
		ent_9.delete(26, 39)
		ent_9.insert(26, ztext83[2])

	if image_num == 3:
		ent_9.delete(26, 39)
		ent_9.insert(26, '0000000000000')
		ent_9.delete(26, 39)
		ent_9.insert(26, ztext83[3])

	if image_num == 4:
		ent_9.delete(26, 39)
		ent_9.insert(26, '0000000000000')
		ent_9.delete(26, 39)
		ent_9.insert(26, ztext83[4])

def forward84(image_num):
	global b_84
	b_84.grid_forget()
	b_84 = Button(but_frame, image = image_list[image_num-1],command=lambda: forward84(image_num+1))
	b_84.grid(row=8, column=3)

	if image_num == 4:
		b_84 = Button(but_frame, image = img_0, command = lambda:forward84(0))
		b_84.grid(row=8, column=3)

	if image_num == 0:
		ent_9.delete(39, 52)
		ent_9.insert(39, '0000000000000')
		ent_9.delete(39, 52)
		ent_9.insert(39, ztext84[0])

	if image_num == 1:
		ent_9.delete(39, 52)
		ent_9.insert(39, '0000000000000')
		ent_9.delete(39, 52)
		ent_9.insert(39, ztext84[1])

	if image_num == 2:
		ent_9.delete(39, 52)
		ent_9.insert(39, '0000000000000')
		ent_9.delete(39, 52)
		ent_9.insert(39, ztext84[2])

	if image_num == 3:
		ent_9.delete(39, 52)
		ent_9.insert(39, '0000000000000')
		ent_9.delete(39, 52)
		ent_9.insert(39, ztext84[3])

	if image_num == 4:
		ent_9.delete(39, 52)
		ent_9.insert(39, '0000000000000')
		ent_9.delete(39, 52)
		ent_9.insert(39, ztext84[4])

def forward85(image_num):
	global b_85
	b_85.grid_forget()
	b_85 = Button(but_frame, image = image_list[image_num-1],command=lambda: forward85(image_num+1))
	b_85.grid(row=8, column=4)

	if image_num == 4:
		b_85 = Button(but_frame, image = img_0, command = lambda:forward85(0))
		b_85.grid(row=8, column=4)

	if image_num == 0:
		ent_9.delete(52, 65)
		ent_9.insert(52, '0000000000000')
		ent_9.delete(52, 65)
		ent_9.insert(52, ztext85[0])

	if image_num == 1:
		ent_9.delete(52, 65)
		ent_9.insert(52, '0000000000000')
		ent_9.delete(52, 65)
		ent_9.insert(52, ztext85[1])

	if image_num == 2:
		ent_9.delete(52, 65)
		ent_9.insert(52, '0000000000000')
		ent_9.delete(52, 65)
		ent_9.insert(52, ztext85[2])

	if image_num == 3:
		ent_9.delete(52, 65)
		ent_9.insert(52, '0000000000000')
		ent_9.delete(52, 65)
		ent_9.insert(52, ztext85[3])

	if image_num == 4:
		ent_9.delete(52, 65)
		ent_9.insert(52, '0000000000000')
		ent_9.delete(52, 65)
		ent_9.insert(52, ztext85[4])

def forward86(image_num):
	global b_86
	b_86.grid_forget()
	b_86 = Button(but_frame, image = image_list[image_num-1],command=lambda: forward86(image_num+1))
	b_86.grid(row=8, column=5)

	if image_num == 4:
		b_86 = Button(but_frame, image = img_0, command = lambda:forward86(0))
		b_86.grid(row=8, column=5)

	if image_num == 0:
		ent_9.delete(65, 78)
		ent_9.insert(65, '0000000000000')
		ent_9.delete(65, 78)
		ent_9.insert(65, ztext86[0])

	if image_num == 1:
		ent_9.delete(65, 78)
		ent_9.insert(65, '0000000000000')
		ent_9.delete(65, 78)
		ent_9.insert(65, ztext86[1])

	if image_num == 2:
		ent_9.delete(65, 78)
		ent_9.insert(65, '0000000000000')
		ent_9.delete(65, 78)
		ent_9.insert(65, ztext86[2])

	if image_num == 3:
		ent_9.delete(65, 78)
		ent_9.insert(65, '0000000000000')
		ent_9.delete(65, 78)
		ent_9.insert(65, ztext86[3])

	if image_num == 4:
		ent_9.delete(65, 78)
		ent_9.insert(65, '0000000000000')
		ent_9.delete(65, 78)
		ent_9.insert(65, ztext86[4])

def forward87(image_num):
	global b_87
	b_87.grid_forget()
	b_87 = Button(but_frame, image = image_list[image_num-1],command=lambda: forward87(image_num+1))
	b_87.grid(row=8, column=6)

	if image_num == 4:
		b_87 = Button(but_frame, image = img_0, command = lambda:forward87(0))
		b_87.grid(row=8, column=6)

	if image_num == 0:
		ent_9.delete(78, 91)
		ent_9.insert(78, '0000000000000')
		ent_9.delete(78, 91)
		ent_9.insert(78, ztext87[0])

	if image_num == 1:
		ent_9.delete(78, 91)
		ent_9.insert(78, '0000000000000')
		ent_9.delete(78, 91)
		ent_9.insert(78, ztext87[1])

	if image_num == 2:
		ent_9.delete(78, 91)
		ent_9.insert(78, '0000000000000')
		ent_9.delete(78, 91)
		ent_9.insert(78, ztext87[2])

	if image_num == 3:
		ent_9.delete(78, 91)
		ent_9.insert(78, '0000000000000')
		ent_9.delete(78, 91)
		ent_9.insert(78, ztext87[3])

	if image_num == 4:
		ent_9.delete(78, 91)
		ent_9.insert(78, '0000000000000')
		ent_9.delete(78, 91)
		ent_9.insert(78, ztext87[4])

def forward88(image_num):
	global b_88
	b_88.grid_forget()
	b_88 = Button(but_frame, image = image_list[image_num-1],command=lambda: forward88(image_num+1))
	b_88.grid(row=8, column=7)

	if image_num == 4:
		b_88 = Button(but_frame, image = img_0, command = lambda:forward88(0))
		b_88.grid(row=8, column=7)

	if image_num == 0:
		ent_9.delete(91, 104)
		ent_9.insert(91, '0000000000000')
		ent_9.delete(91, 104)
		ent_9.insert(91, ztext88[0])

	if image_num == 1:
		ent_9.delete(91, 104)
		ent_9.insert(91, '0000000000000')
		ent_9.delete(91, 104)
		ent_9.insert(91, ztext88[1])

	if image_num == 2:
		ent_9.delete(91, 104)
		ent_9.insert(91, '0000000000000')
		ent_9.delete(91, 104)
		ent_9.insert(91, ztext88[2])

	if image_num == 3:
		ent_9.delete(91, 104)
		ent_9.insert(91, '0000000000000')
		ent_9.delete(91, 104)
		ent_9.insert(91, ztext88[3])

	if image_num == 4:
		ent_9.delete(91, 104)
		ent_9.insert(91, '0000000000000')
		ent_9.delete(91, 104)
		ent_9.insert(91, ztext88[4])

def forward89(image_num):
	global b_89
	b_89.grid_forget()
	b_89 = Button(but_frame, image = image_list[image_num-1],command=lambda: forward89(image_num+1))
	b_89.grid(row=8, column=8)

	if image_num == 4:
		b_89 = Button(but_frame, image = img_0, command = lambda:forward89(0))
		b_89.grid(row=8, column=8)

	if image_num == 0:
		ent_9.delete(104, 117)
		ent_9.insert(104, '0000000000000')
		ent_9.delete(104, 117)
		ent_9.insert(104, ztext89[0])

	if image_num == 1:
		ent_9.delete(104, 117)
		ent_9.insert(104, '0000000000000')
		ent_9.delete(104, 117)
		ent_9.insert(104, ztext89[1])

	if image_num == 2:
		ent_9.delete(104, 117)
		ent_9.insert(104, '0000000000000')
		ent_9.delete(104, 117)
		ent_9.insert(104, ztext89[2])

	if image_num == 3:
		ent_9.delete(104, 117)
		ent_9.insert(104, '0000000000000')
		ent_9.delete(104, 117)
		ent_9.insert(104, ztext89[3])

	if image_num == 4:
		ent_9.delete(104, 117)
		ent_9.insert(104, '0000000000000')
		ent_9.delete(104, 117)
		ent_9.insert(104, ztext89[4])

def forward90(image_num):
	global b_90
	b_90.grid_forget()
	b_90 = Button(but_frame, image = image_list[image_num-1],command=lambda: forward90(image_num+1))
	b_90.grid(row=8, column=9)

	if image_num == 4:
		b_90 = Button(but_frame, image = img_0, command = lambda:forward90(0))
		b_90.grid(row=8, column=9)

	if image_num == 0:
		ent_9.delete(117, 130)
		ent_9.insert(117, '0000000000000')
		ent_9.delete(117, 130)
		ent_9.insert(117, ztext90[0])

	if image_num == 1:
		ent_9.delete(117, 130)
		ent_9.insert(117, '0000000000000')
		ent_9.delete(117, 130)
		ent_9.insert(117, ztext90[1])

	if image_num == 2:
		ent_9.delete(117, 130)
		ent_9.insert(117, '0000000000000')
		ent_9.delete(117, 130)
		ent_9.insert(117, ztext90[2])

	if image_num == 3:
		ent_9.delete(117, 130)
		ent_9.insert(117, '0000000000000')
		ent_9.delete(117, 130)
		ent_9.insert(117, ztext90[3])

	if image_num == 4:
		ent_9.delete(117, 130)
		ent_9.insert(117, '0000000000000')
		ent_9.delete(117, 130)
		ent_9.insert(117, ztext90[4])
#90
def forward91(image_num):
	global b_91
	b_91.grid_forget()
	b_91 = Button(but_frame, image = image_list[image_num-1],command=lambda: forward91(image_num+1))
	b_91.grid(row=9, column=0)

	if image_num == 4:
		b_91 = Button(but_frame, image = img_0, command = lambda:forward91(0))
		b_91.grid(row=9, column=0)

	if image_num == 0:
		ent_10.delete(0,13)
		ent_10.insert(0, '0000000000000')
		ent_10.delete(0, 13)
		ent_10.insert(0, ztext91[0])

	if image_num == 1:
		ent_10.delete(0,13)
		ent_10.insert(0, '0000000000000')
		ent_10.delete(0, 13)
		ent_10.insert(0, ztext91[1])

	if image_num == 2:
		ent_10.delete(0,13)
		ent_10.insert(0, '0000000000000')
		ent_10.delete(0, 13)
		ent_10.insert(0, ztext91[2])

	if image_num == 3:
		ent_10.delete(0,13)
		ent_10.insert(0, '0000000000000')
		ent_10.delete(0, 13)
		ent_10.insert(0, ztext91[3])

	if image_num == 4:
		ent_10.delete(0,13)
		ent_10.insert(0, '0000000000000')
		ent_10.delete(0, 13)
		ent_10.insert(0, ztext91[4])

def forward92(image_num):
	global b_92
	b_92.grid_forget()
	b_92 = Button(but_frame, image = image_list[image_num-1],command=lambda: forward92(image_num+1))
	b_92.grid(row=9, column=1)

	if image_num == 4:
		b_92 = Button(but_frame, image = img_0, command = lambda:forward92(0))
		b_92.grid(row=9, column=1)

	if image_num == 0:
		ent_10.delete(13, 26)
		ent_10.insert(13, '0000000000000')
		ent_10.delete(13, 26)
		ent_10.insert(13, ztext92[0])

	if image_num == 1:
		ent_10.delete(13, 26)
		ent_10.insert(13, '0000000000000')
		ent_10.delete(13, 26)
		ent_10.insert(13, ztext92[1])

	if image_num == 2:
		ent_10.delete(13, 26)
		ent_10.insert(13, '0000000000000')
		ent_10.delete(13, 26)
		ent_10.insert(13, ztext92[2])

	if image_num == 3:
		ent_10.delete(13, 26)
		ent_10.insert(13, '0000000000000')
		ent_10.delete(13, 26)
		ent_10.insert(13, ztext92[3])

	if image_num == 4:
		ent_10.delete(13, 26)
		ent_10.insert(13, '0000000000000')
		ent_10.delete(13, 26)
		ent_10.insert(13, ztext92[4])

def forward93(image_num):
	global b_93
	b_93.grid_forget()
	b_93 = Button(but_frame, image = image_list[image_num-1],command=lambda: forward93(image_num+1))
	b_93.grid(row=9, column=2)

	if image_num == 4:
		b_93 = Button(but_frame, image = img_0, command = lambda:forward93(0))
		b_93.grid(row=9, column=2)

	if image_num == 0:
		ent_10.delete(26, 39)
		ent_10.insert(26, '0000000000000')
		ent_10.delete(26, 39)
		ent_10.insert(26, ztext93[0])

	if image_num == 1:
		ent_10.delete(26, 39)
		ent_10.insert(26, '0000000000000')
		ent_10.delete(26, 39)
		ent_10.insert(26, ztext93[1])

	if image_num == 2:
		ent_10.delete(26, 39)
		ent_10.insert(26, '0000000000000')
		ent_10.delete(26, 39)
		ent_10.insert(26, ztext93[2])

	if image_num == 3:
		ent_10.delete(26, 39)
		ent_10.insert(26, '0000000000000')
		ent_10.delete(26, 39)
		ent_10.insert(26, ztext93[3])

	if image_num == 4:
		ent_10.delete(26, 39)
		ent_10.insert(26, '0000000000000')
		ent_10.delete(26, 39)
		ent_10.insert(26, ztext93[4])

def forward94(image_num):
	global b_94
	b_94.grid_forget()
	b_94 = Button(but_frame, image = image_list[image_num-1],command=lambda: forward94(image_num+1))
	b_94.grid(row=9, column=3)

	if image_num == 4:
		b_94 = Button(but_frame, image = img_0, command = lambda:forward94(0))
		b_94.grid(row=9, column=3)

	if image_num == 0:
		ent_10.delete(39, 52)
		ent_10.insert(39, '0000000000000')
		ent_10.delete(39, 52)
		ent_10.insert(39, ztext94[0])

	if image_num == 1:
		ent_10.delete(39, 52)
		ent_10.insert(39, '0000000000000')
		ent_10.delete(39, 52)
		ent_10.insert(39, ztext94[1])

	if image_num == 2:
		ent_10.delete(39, 52)
		ent_10.insert(39, '0000000000000')
		ent_10.delete(39, 52)
		ent_10.insert(39, ztext94[2])

	if image_num == 3:
		ent_10.delete(39, 52)
		ent_10.insert(39, '0000000000000')
		ent_10.delete(39, 52)
		ent_10.insert(39, ztext94[3])

	if image_num == 4:
		ent_10.delete(39, 52)
		ent_10.insert(39, '0000000000000')
		ent_10.delete(39, 52)
		ent_10.insert(39, ztext94[4])

def forward95(image_num):
	global b_95
	b_95.grid_forget()
	b_95 = Button(but_frame, image = image_list[image_num-1],command=lambda: forward95(image_num+1))
	b_95.grid(row=9, column=4)

	if image_num == 4:
		b_95 = Button(but_frame, image = img_0, command = lambda:forward95(0))
		b_95.grid(row=9, column=4)

	if image_num == 0:
		ent_10.delete(52, 65)
		ent_10.insert(52, '0000000000000')
		ent_10.delete(52, 65)
		ent_10.insert(52, ztext95[0])

	if image_num == 1:
		ent_10.delete(52, 65)
		ent_10.insert(52, '0000000000000')
		ent_10.delete(52, 65)
		ent_10.insert(52, ztext95[1])

	if image_num == 2:
		ent_10.delete(52, 65)
		ent_10.insert(52, '0000000000000')
		ent_10.delete(52, 65)
		ent_10.insert(52, ztext95[2])

	if image_num == 3:
		ent_10.delete(52, 65)
		ent_10.insert(52, '0000000000000')
		ent_10.delete(52, 65)
		ent_10.insert(52, ztext95[3])

	if image_num == 4:
		ent_10.delete(52, 65)
		ent_10.insert(52, '0000000000000')
		ent_10.delete(52, 65)
		ent_10.insert(52, ztext95[4])

def forward96(image_num):
	global b_96
	b_96.grid_forget()
	b_96 = Button(but_frame, image = image_list[image_num-1],command=lambda: forward96(image_num+1))
	b_96.grid(row=9, column=5)

	if image_num == 4:
		b_96 = Button(but_frame, image = img_0, command = lambda:forward96(0))
		b_96.grid(row=9, column=5)

	if image_num == 0:
		ent_10.delete(65, 78)
		ent_10.insert(65, '0000000000000')
		ent_10.delete(65, 78)
		ent_10.insert(65, ztext96[0])

	if image_num == 1:
		ent_10.delete(65, 78)
		ent_10.insert(65, '0000000000000')
		ent_10.delete(65, 78)
		ent_10.insert(65, ztext96[1])

	if image_num == 2:
		ent_10.delete(65, 78)
		ent_10.insert(65, '0000000000000')
		ent_10.delete(65, 78)
		ent_10.insert(65, ztext96[2])

	if image_num == 3:
		ent_10.delete(65, 78)
		ent_10.insert(65, '0000000000000')
		ent_10.delete(65, 78)
		ent_10.insert(65, ztext96[3])

	if image_num == 4:
		ent_10.delete(65, 78)
		ent_10.insert(65, '0000000000000')
		ent_10.delete(65, 78)
		ent_10.insert(65, ztext96[4])

def forward97(image_num):
	global b_97
	b_97.grid_forget()
	b_97 = Button(but_frame, image = image_list[image_num-1],command=lambda: forward97(image_num+1))
	b_97.grid(row=9, column=6)

	if image_num == 4:
		b_97 = Button(but_frame, image = img_0, command = lambda:forward97(0))
		b_97.grid(row=9, column=6)

	if image_num == 0:
		ent_10.delete(78, 91)
		ent_10.insert(78, '0000000000000')
		ent_10.delete(78, 91)
		ent_10.insert(78, ztext97[0])

	if image_num == 1:
		ent_10.delete(78, 91)
		ent_10.insert(78, '0000000000000')
		ent_10.delete(78, 91)
		ent_10.insert(78, ztext97[1])

	if image_num == 2:
		ent_10.delete(78, 91)
		ent_10.insert(78, '0000000000000')
		ent_10.delete(78, 91)
		ent_10.insert(78, ztext97[2])

	if image_num == 3:
		ent_10.delete(78, 91)
		ent_10.insert(78, '0000000000000')
		ent_10.delete(78, 91)
		ent_10.insert(78, ztext97[3])

	if image_num == 4:
		ent_10.delete(78, 91)
		ent_10.insert(78, '0000000000000')
		ent_10.delete(78, 91)
		ent_10.insert(78, ztext97[4])

def forward98(image_num):
	global b_98
	b_98.grid_forget()
	b_98 = Button(but_frame, image = image_list[image_num-1],command=lambda: forward98(image_num+1))
	b_98.grid(row=9, column=7)

	if image_num == 4:
		b_98 = Button(but_frame, image = img_0, command = lambda:forward98(0))
		b_98.grid(row=9, column=7)

	if image_num == 0:
		ent_10.delete(91, 104)
		ent_10.insert(91, '0000000000000')
		ent_10.delete(91, 104)
		ent_10.insert(91, ztext98[0])

	if image_num == 1:
		ent_10.delete(91, 104)
		ent_10.insert(91, '0000000000000')
		ent_10.delete(91, 104)
		ent_10.insert(91, ztext98[1])

	if image_num == 2:
		ent_10.delete(91, 104)
		ent_10.insert(91, '0000000000000')
		ent_10.delete(91, 104)
		ent_10.insert(91, ztext98[2])

	if image_num == 3:
		ent_10.delete(91, 104)
		ent_10.insert(91, '0000000000000')
		ent_10.delete(91, 104)
		ent_10.insert(91, ztext98[3])

	if image_num == 4:
		ent_10.delete(91, 104)
		ent_10.insert(91, '0000000000000')
		ent_10.delete(91, 104)
		ent_10.insert(91, ztext98[4])

def forward99(image_num):
	global b_99
	b_99.grid_forget()
	b_99 = Button(but_frame, image = image_list[image_num-1],command=lambda: forward99(image_num+1))
	b_99.grid(row=9, column=8)

	if image_num == 4:
		b_99 = Button(but_frame, image = img_0, command = lambda:forward99(0))
		b_99.grid(row=9, column=8)

	if image_num == 0:
		ent_10.delete(104, 117)
		ent_10.insert(104, '0000000000000')
		ent_10.delete(104, 117)
		ent_10.insert(104, ztext99[0])

	if image_num == 1:
		ent_10.delete(104, 117)
		ent_10.insert(104, '0000000000000')
		ent_10.delete(104, 117)
		ent_10.insert(104, ztext99[1])

	if image_num == 2:
		ent_10.delete(104, 117)
		ent_10.insert(104, '0000000000000')
		ent_10.delete(104, 117)
		ent_10.insert(104, ztext99[2])

	if image_num == 3:
		ent_10.delete(104, 117)
		ent_10.insert(104, '0000000000000')
		ent_10.delete(104, 117)
		ent_10.insert(104, ztext99[3])

	if image_num == 4:
		ent_10.delete(104, 117)
		ent_10.insert(104, '0000000000000')
		ent_10.delete(104, 117)
		ent_10.insert(104, ztext99[4])

def forward100(image_num):
	global b_100
	b_100.grid_forget()
	b_100 = Button(but_frame, image = image_list[image_num-1],command=lambda: forward100(image_num+1))
	b_100.grid(row=9, column=9)

	if image_num == 4:
		b_100 = Button(but_frame, image = img_0, command = lambda:forward100(0))
		b_100.grid(row=9, column=9)

	if image_num == 0:
		ent_10.delete(117, 130)
		ent_10.insert(117, '0000000000000')
		ent_10.delete(117, 130)
		ent_10.insert(117, ztext100[0])

	if image_num == 1:
		ent_10.delete(117, 130)
		ent_10.insert(117, '0000000000000')
		ent_10.delete(117, 130)
		ent_10.insert(117, ztext100[1])

	if image_num == 2:
		ent_10.delete(117, 130)
		ent_10.insert(117, '0000000000000')
		ent_10.delete(117, 130)
		ent_10.insert(117, ztext100[2])

	if image_num == 3:
		ent_10.delete(117, 130)
		ent_10.insert(117, '0000000000000')
		ent_10.delete(117, 130)
		ent_10.insert(117, ztext100[3])

	if image_num == 4:
		ent_10.delete(117, 130)
		ent_10.insert(117, '0000000000000')
		ent_10.delete(117, 130)
		ent_10.insert(117, ztext100[4])

def a2z_list_insert_end():
	text_1.insert(END, a_text)
	text_1.insert(END, A_text)
	text_1.insert(END, ä_text)
	text_1.insert(END, Ä_text)
	text_1.insert(END, b_text)
	text_1.insert(END, B_text)
	text_1.insert(END, c_text)
	text_1.insert(END, C_text)
	text_1.insert(END, d_text)
	text_1.insert(END, D_text)
	text_1.insert(END, e_text)
	text_1.insert(END, E_text)
	text_1.insert(END, f_text)
	text_1.insert(END, F_text)
	text_1.insert(END, g_text)
	text_1.insert(END, G_text)
	text_1.insert(END, h_text)
	text_1.insert(END, H_text)
	text_1.insert(END, i_text)
	text_1.insert(END, I_text)
	text_1.insert(END, j_text)
	text_1.insert(END, J_text)
	text_1.insert(END, k_text)
	text_1.insert(END, K_text)
	text_1.insert(END, l_text)
	text_1.insert(END, L_text)
	text_1.insert(END, m_text)
	text_1.insert(END, M_text)
	text_1.insert(END, n_text)
	text_1.insert(END, N_text)
	text_1.insert(END, o_text)
	text_1.insert(END, O_text)
	text_1.insert(END, ö_text)
	text_1.insert(END, Ö_text)
	text_1.insert(END, p_text)
	text_1.insert(END, P_text)
	text_1.insert(END, q_text)
	text_1.insert(END, Q_text)
	text_1.insert(END, r_text)
	text_1.insert(END, R_text)
	text_1.insert(END, s_text)
	text_1.insert(END, S_text)
	text_1.insert(END, t_text)
	text_1.insert(END, T_text)
	text_1.insert(END, u_text)
	text_1.insert(END, U_text)
	text_1.insert(END, ü_text)
	text_1.insert(END, Ü_text)
	text_1.insert(END, v_text)
	text_1.insert(END, V_text)
	text_1.insert(END, w_text)
	text_1.insert(END, W_text)
	text_1.insert(END, x_text)
	text_1.insert(END, X_text)
	text_1.insert(END, y_text)
	text_1.insert(END, Y_text)
	text_1.insert(END, z_text)
	text_1.insert(END, Z_text)

	text_1.insert(END, char_exclamation)
	text_1.insert(END, char_quotes)
	text_1.insert(END, char_dollar)
	text_1.insert(END, char_percent)
	text_1.insert(END, char_and)
	text_1.insert(END, char_forward_slash)
	text_1.insert(END, char_left_curly_bracket)
	text_1.insert(END, char_left_bracket)
	text_1.insert(END, char_left_square_bracket)
	text_1.insert(END, char_right_bracket)
	text_1.insert(END, char_right_square_bracket)
	text_1.insert(END, char_equals)
	text_1.insert(END, char_right_curly_bracket)
	text_1.insert(END, char_question)
	text_1.insert(END, char_sz)
	text_1.insert(END, char_back_slash)
	text_1.insert(END, char_comma)
	text_1.insert(END, char_semi_colon)
	text_1.insert(END, char_double_point)
	text_1.insert(END, char_full_stop)
	text_1.insert(END, char_lower_case_hyfen)
	text_1.insert(END, char_minus)
	text_1.insert(END, char_hashtag)
	text_1.insert(END, char_plus)
	text_1.insert(END, char_times_star)
	text_1.insert(END, char_single_quotes)
	text_1.insert(END, char_less_than)
	text_1.insert(END, char_more_than)
	text_1.insert(END, char_line_seperator)
	text_1.insert(END, char_wavey)
	text_1.insert(END, char_space)
	text_1.insert(END, zero)
	text_1.insert(END, one)
	text_1.insert(END, two)
	text_1.insert(END, three)
	text_1.insert(END, four)
	text_1.insert(END, five)
	text_1.insert(END, six)
	text_1.insert(END, seven)
	text_1.insert(END, eight)
	text_1.insert(END, nine)
	text_1.insert(END, ten)
#s.window(rename function)
def ztext_change():
	#change all text values upon click

	#delete entry box
	ent_1.delete(0,END)

	ztext1.clear()
	ztext1[0:5] = gen_code[500:505]
	ent_1.insert(END,ztext1[0])

	ztext2.clear()
	ztext2[0:5] = gen_code[505:510]
	ent_1.insert(END, ztext2[0])

	ztext3.clear()
	ztext3[0:5] = gen_code[510:515]
	ent_1.insert(END, ztext3[0])

	ztext4.clear()
	ztext4[0:5] = gen_code[515:520]
	ent_1.insert(END, ztext4[0])

	ztext5.clear()
	ztext5[0:5] = gen_code[520:525]
	ent_1.insert(END, ztext5[0])

	ztext6.clear()
	ztext6[0:5] = gen_code[525:530]
	ent_1.insert(END, ztext6[0])

	ztext7.clear()
	ztext7[0:5] = gen_code[530:535]
	ent_1.insert(END, ztext7[0])

	ztext8.clear()
	ztext8[0:5] = gen_code[535:540]
	ent_1.insert(END, ztext8[0])

	ztext9.clear()
	ztext9[0:5] = gen_code[540:545]
	ent_1.insert(END, ztext9[0])

	ztext10.clear()
	ztext10[0:5] = gen_code[545:550]
	ent_1.insert(END, ztext10[0])

#row2
	ent_2.delete(0,END)

	ztext11.clear()
	ztext11[0:5] = gen_code[550:555]
	ent_2.insert(END,ztext11[0])

	ztext12.clear()
	ztext12[0:5] = gen_code[555:560]
	ent_2.insert(END, ztext12[0])

	ztext13.clear()
	ztext13[0:5] = gen_code[560:565]
	ent_2.insert(END, ztext13[0])

	ztext14.clear()
	ztext14[0:5] = gen_code[565:570]
	ent_2.insert(END, ztext14[0])

	ztext15.clear()
	ztext15[0:5] = gen_code[570:575]
	ent_2.insert(END, ztext15[0])

	ztext16.clear()
	ztext16[0:5] = gen_code[575:580]
	ent_2.insert(END, ztext16[0])

	ztext17.clear()
	ztext17[0:5] = gen_code[580:585]
	ent_2.insert(END, ztext17[0])

	ztext18.clear()
	ztext18[0:5] = gen_code[585:590]
	ent_2.insert(END, ztext18[0])

	ztext19.clear()
	ztext19[0:5] = gen_code[590:595]
	ent_2.insert(END, ztext19[0])

	ztext20.clear()
	ztext20[0:5] = gen_code[595:600]
	ent_2.insert(END, ztext20[0])

	ent_3.delete(0,END)

	ztext21.clear()
	ztext21[0:5] = gen_code[600:605]
	ent_3.insert(END,ztext21[0])

	ztext22.clear()
	ztext22[0:5] = gen_code[605:610]
	ent_3.insert(END, ztext22[0])

	ztext23.clear()
	ztext23[0:5] = gen_code[610:615]
	ent_3.insert(END, ztext23[0])

	ztext24.clear()
	ztext24[0:5] = gen_code[615:620]
	ent_3.insert(END, ztext24[0])

	ztext25.clear()
	ztext25[0:5] = gen_code[620:625]
	ent_3.insert(END, ztext25[0])

	ztext26.clear()
	ztext26[0:5] = gen_code[625:630]
	ent_3.insert(END, ztext26[0])

	ztext27.clear()
	ztext27[0:5] = gen_code[630:635]
	ent_3.insert(END, ztext27[0])

	ztext28.clear()
	ztext28[0:5] = gen_code[635:640]
	ent_3.insert(END, ztext28[0])

	ztext29.clear()
	ztext29[0:5] = gen_code[640:645]
	ent_3.insert(END, ztext29[0])

	ztext30.clear()
	ztext30[0:5] = gen_code[645:650]
	ent_3.insert(END, ztext30[0])

	ent_4.delete(0,END)

	ztext31.clear()
	ztext31[0:5] = gen_code[650:655]
	ent_4.insert(END,ztext31[0])

	ztext32.clear()
	ztext32[0:5] = gen_code[655:660]
	ent_4.insert(END, ztext32[0])

	ztext33.clear()
	ztext33[0:5] = gen_code[660:665]
	ent_4.insert(END, ztext33[0])

	ztext34.clear()
	ztext34[0:5] = gen_code[665:670]
	ent_4.insert(END, ztext34[0])

	ztext35.clear()
	ztext35[0:5] = gen_code[670:675]
	ent_4.insert(END, ztext35[0])

	ztext36.clear()
	ztext36[0:5] = gen_code[675:680]
	ent_4.insert(END, ztext36[0])

	ztext37.clear()
	ztext37[0:5] = gen_code[680:685]
	ent_4.insert(END, ztext37[0])

	ztext38.clear()
	ztext38[0:5] = gen_code[685:690]
	ent_4.insert(END, ztext38[0])

	ztext39.clear()
	ztext39[0:5] = gen_code[690:695]
	ent_4.insert(END, ztext39[0])

	ztext40.clear()
	ztext40[0:5] = gen_code[695:700]
	ent_4.insert(END, ztext40[0])

	ent_5.delete(0,END)

	ztext41.clear()
	ztext41[0:5] = gen_code[700:705]
	ent_5.insert(END,ztext41[0])

	ztext42.clear()
	ztext42[0:5] = gen_code[705:710]
	ent_5.insert(END, ztext42[0])

	ztext43.clear()
	ztext43[0:5] = gen_code[710:715]
	ent_5.insert(END, ztext43[0])

	ztext44.clear()
	ztext44[0:5] = gen_code[715:720]
	ent_5.insert(END, ztext44[0])

	ztext45.clear()
	ztext45[0:5] = gen_code[720:725]
	ent_5.insert(END, ztext45[0])

	ztext46.clear()
	ztext46[0:5] = gen_code[725:730]
	ent_5.insert(END, ztext46[0])

	ztext47.clear()
	ztext47[0:5] = gen_code[730:735]
	ent_5.insert(END, ztext47[0])

	ztext48.clear()
	ztext48[0:5] = gen_code[735:740]
	ent_5.insert(END, ztext48[0])

	ztext49.clear()
	ztext49[0:5] = gen_code[740:745]
	ent_5.insert(END, ztext49[0])

	ztext50.clear()
	ztext50[0:5] = gen_code[745:750]
	ent_5.insert(END, ztext50[0])

	ent_6.delete(0,END)

	ztext51.clear()
	ztext51[0:5] = gen_code[750:755]
	ent_6.insert(END,ztext51[0])

	ztext52.clear()
	ztext52[0:5] = gen_code[755:760]
	ent_6.insert(END, ztext52[0])

	ztext53.clear()
	ztext53[0:5] = gen_code[760:765]
	ent_6.insert(END, ztext53[0])

	ztext54.clear()
	ztext54[0:5] = gen_code[765:770]
	ent_6.insert(END, ztext54[0])

	ztext55.clear()
	ztext55[0:5] = gen_code[770:775]
	ent_6.insert(END, ztext55[0])

	ztext56.clear()
	ztext56[0:5] = gen_code[775:780]
	ent_6.insert(END, ztext56[0])

	ztext57.clear()
	ztext57[0:5] = gen_code[780:785]
	ent_6.insert(END, ztext57[0])

	ztext58.clear()
	ztext58[0:5] = gen_code[785:790]
	ent_6.insert(END, ztext58[0])

	ztext59.clear()
	ztext59[0:5] = gen_code[790:795]
	ent_6.insert(END, ztext59[0])

	ztext60.clear()
	ztext60[0:5] = gen_code[795:800]
	ent_6.insert(END, ztext60[0])

	ent_7.delete(0,END)

	ztext61.clear()
	ztext61[0:5] = gen_code[800:805]
	ent_7.insert(END,ztext61[0])

	ztext62.clear()
	ztext62[0:5] = gen_code[805:810]
	ent_7.insert(END, ztext62[0])

	ztext63.clear()
	ztext63[0:5] = gen_code[810:815]
	ent_7.insert(END, ztext63[0])

	ztext64.clear()
	ztext64[0:5] = gen_code[815:820]
	ent_7.insert(END, ztext64[0])

	ztext65.clear()
	ztext65[0:5] = gen_code[820:825]
	ent_7.insert(END, ztext65[0])

	ztext66.clear()
	ztext66[0:5] = gen_code[825:830]
	ent_7.insert(END, ztext66[0])

	ztext67.clear()
	ztext67[0:5] = gen_code[830:835]
	ent_7.insert(END, ztext67[0])

	ztext68.clear()
	ztext68[0:5] = gen_code[835:840]
	ent_7.insert(END, ztext68[0])

	ztext69.clear()
	ztext69[0:5] = gen_code[840:845]
	ent_7.insert(END, ztext69[0])

	ztext70.clear()
	ztext70[0:5] = gen_code[845:850]
	ent_7.insert(END, ztext70[0])

	ent_8.delete(0,END)

	ztext71.clear()
	ztext71[0:5] = gen_code[850:855]
	ent_8.insert(END,ztext71[0])

	ztext72.clear()
	ztext72[0:5] = gen_code[855:860]
	ent_8.insert(END, ztext72[0])

	ztext73.clear()
	ztext73[0:5] = gen_code[860:865]
	ent_8.insert(END, ztext73[0])

	ztext74.clear()
	ztext74[0:5] = gen_code[865:870]
	ent_8.insert(END, ztext74[0])

	ztext75.clear()
	ztext75[0:5] = gen_code[870:875]
	ent_8.insert(END, ztext75[0])

	ztext76.clear()
	ztext76[0:5] = gen_code[875:880]
	ent_8.insert(END, ztext76[0])

	ztext77.clear()
	ztext77[0:5] = gen_code[880:885]
	ent_8.insert(END, ztext77[0])

	ztext78.clear()
	ztext78[0:5] = gen_code[885:890]
	ent_8.insert(END, ztext78[0])

	ztext79.clear()
	ztext79[0:5] = gen_code[890:895]
	ent_8.insert(END, ztext79[0])

	ztext80.clear()
	ztext80[0:5] = gen_code[895:900]
	ent_8.insert(END, ztext80[0])

	ent_9.delete(0,END)

	ztext81.clear()
	ztext81[0:5] = gen_code[900:905]
	ent_9.insert(END,ztext81[0])

	ztext82.clear()
	ztext82[0:5] = gen_code[905:910]
	ent_9.insert(END, ztext82[0])

	ztext83.clear()
	ztext83[0:5] = gen_code[910:915]
	ent_9.insert(END, ztext83[0])

	ztext84.clear()
	ztext84[0:5] = gen_code[915:920]
	ent_9.insert(END, ztext84[0])

	ztext85.clear()
	ztext85[0:5] = gen_code[920:925]
	ent_9.insert(END, ztext85[0])

	ztext86.clear()
	ztext86[0:5] = gen_code[925:930]
	ent_9.insert(END, ztext86[0])

	ztext87.clear()
	ztext87[0:5] = gen_code[930:935]
	ent_9.insert(END, ztext87[0])

	ztext88.clear()
	ztext88[0:5] = gen_code[935:940]
	ent_9.insert(END, ztext88[0])

	ztext89.clear()
	ztext89[0:5] = gen_code[940:945]
	ent_9.insert(END, ztext89[0])

	ztext90.clear()
	ztext90[0:5] = gen_code[945:950]
	ent_9.insert(END, ztext90[0])

	ent_10.delete(0,END)

	ztext91.clear()
	ztext91[0:5] = gen_code[950:955]
	ent_10.insert(END,ztext91[0])

	ztext92.clear()
	ztext92[0:5] = gen_code[955:960]
	ent_10.insert(END, ztext92[0])

	ztext93.clear()
	ztext93[0:5] = gen_code[960:965]
	ent_10.insert(END, ztext93[0])

	ztext94.clear()
	ztext94[0:5] = gen_code[965:970]
	ent_10.insert(END, ztext94[0])

	ztext95.clear()
	ztext95[0:5] = gen_code[970:975]
	ent_10.insert(END, ztext95[0])

	ztext96.clear()
	ztext96[0:5] = gen_code[975:980]
	ent_10.insert(END, ztext96[0])

	ztext97.clear()
	ztext97[0:5] = gen_code[980:985]
	ent_10.insert(END, ztext97[0])

	ztext98.clear()
	ztext98[0:5] = gen_code[985:990]
	ent_10.insert(END, ztext98[0])

	ztext99.clear()
	ztext99[0:5] = gen_code[990:995]
	ent_10.insert(END, ztext99[0])

	ztext100.clear()
	ztext100[0:5] = gen_code[995:1000]
	ent_10.insert(END, ztext100[0])

	#put in the new entries__________________________________________________
	random_entries1()
	#________________________________________________________________________

	del gen_code[500:1000]
	print(len(gen_code))
	#messages to show beginning and nearing end via label config

	if len(gen_code) == 1500:
		lab_0.config(text = 'nearing end of message: 2 left!',bg = 'black', fg = 'green')
	if len(gen_code) == 1000:
		lab_0.config(text = 'nearing end: 1 left!',bg = 'black', fg = 'green')
	if len(gen_code) == 500:
		lab_0.config(text = '0 left, save text now!***', bg = 'red', fg = 'black')
		return

#def button functions x100
#bin_list is a disposable list
#delete, append, insert are not used here as to avoid recurrances when changing the random shapes
#seperate functions are called eg(a_ex())

def t1():
	ent_text.insert(END, 'a')
	a_ex()
def t2():
    ent_text.insert(END, 'A')
    #A_text.append(bin_list.get(ANCHOR))
    A_ex()
def t3():
    ent_text.insert(END, 'ä')
    #ä_text.append(bin_list.get(ANCHOR))
    #text_1.insert(END, bin_list.get(ANCHOR))
    #bin_list.delete(ANCHOR)
    ä_ex()
def t4():
    ent_text.insert(END, 'Ä')
    #Ä_text.append(bin_list.get(ANCHOR))
    #text_1.insert(END, bin_list.get(ANCHOR))
    #bin_list.delete(ANCHOR)
    Ä_ex()
def t5():
    ent_text.insert(END, 'b')
    #b_text.append(bin_list.get(ANCHOR))
    #text_1.insert(END, bin_list.get(ANCHOR))
    #bin_list.delete(ANCHOR)
    b_ex()
def t6():
	ent_text.insert(END, 'B')
	#B_text.append(bin_list.get(ANCHOR))
	#text_1.insert(END, bin_list.get(ANCHOR))
	#bin_list.delete(ANCHOR)
	B_ex()
def t7():
	ent_text.insert(END, 'c')
	#c_text.append(bin_list.get(ANCHOR))
	#text_1.insert(END, bin_list.get(ANCHOR))
	#bin_list.delete(ANCHOR)
	c_ex()
def t8():
	ent_text.insert(END, 'C')
	#C_text.append(bin_list.get(ANCHOR))
	#text_1.insert(END, bin_list.get(ANCHOR))
	#bin_list.delete(ANCHOR)
	C_ex()
def t9():
	ent_text.insert(END, 'd')
	#d_text.append(bin_list.get(ANCHOR))
	#text_1.insert(END, bin_list.get(ANCHOR))
	#bin_list.delete(ANCHOR)
	d_ex()
def t10():
	ent_text.insert(END, 'D')
	#D_text.append(bin_list.get(ANCHOR))
	#text_1.insert(END, bin_list.get(ANCHOR))
	#bin_list.delete(ANCHOR)
	D_ex()
def t11():
	ent_text.insert(END, 'e')
	#e_text.append(bin_list.get(ANCHOR))
	#text_1.insert(END, bin_list.get(ANCHOR))
	#bin_list.delete(ANCHOR)
	e_ex()
def t12():
	ent_text.insert(END, 'E')
	#E_text.append(bin_list.get(ANCHOR))
	#text_1.insert(END, bin_list.get(ANCHOR))
	#bin_list.delete(ANCHOR)
	E_ex()
def t13():
	ent_text.insert(END, 'f')
	#f_text.append(bin_list.get(ANCHOR))
	#text_1.insert(END, bin_list.get(ANCHOR))
	#bin_list.delete(ANCHOR)
	f_ex()
def t14():
	ent_text.insert(END, 'F')
	#F_text.append(bin_list.get(ANCHOR))
	#text_1.insert(END, bin_list.get(ANCHOR))
	#bin_list.delete(ANCHOR)
	F_ex()
def t15():
	ent_text.insert(END, 'g')
	#g_text.append(bin_list.get(ANCHOR))
	#text_1.insert(END, bin_list.get(ANCHOR))
	#bin_list.delete(ANCHOR)
	g_ex()
def t16():
	ent_text.insert(END, 'G')
	#G_text.append(bin_list.get(ANCHOR))
	#text_1.insert(END, bin_list.get(ANCHOR))
	#bin_list.delete(ANCHOR)
	G_ex()
def t17():
	ent_text.insert(END, 'h')
	#h_text.append(bin_list.get(ANCHOR))
	#text_1.insert(END, bin_list.get(ANCHOR))
	#bin_list.delete(ANCHOR)
	h_ex()
def t18():
	ent_text.insert(END, 'H')
	#H_text.append(bin_list.get(ANCHOR))
	#text_1.insert(END, bin_list.get(ANCHOR))
	#bin_list.delete(ANCHOR)
	H_ex()
def t19():
	ent_text.insert(END, 'i')
	#i_text.append(bin_list.get(ANCHOR))
	#text_1.insert(END, bin_list.get(ANCHOR))
	#bin_list.delete(ANCHOR)
	i_ex()
def t20():
	ent_text.insert(END, 'I')
	#I_text.append(bin_list.get(ANCHOR))
	#text_1.insert(END, bin_list.get(ANCHOR))
	#bin_list.delete(ANCHOR)
	I_ex()
def t21():
	ent_text.insert(END, 'j')
	#j_text.append(bin_list.get(ANCHOR))
	#text_1.insert(END, bin_list.get(ANCHOR))
	#bin_list.delete(ANCHOR)
	j_ex()
def t22():
	ent_text.insert(END, 'J')
	#J_text.append(bin_list.get(ANCHOR))
	#text_1.insert(END, bin_list.get(ANCHOR))
	#bin_list.delete(ANCHOR)
	J_ex()
def t23():
	ent_text.insert(END, 'k')
	#k_text.append(bin_list.get(ANCHOR))
	#text_1.insert(END, bin_list.get(ANCHOR))
	#bin_list.delete(ANCHOR)
	k_ex()
def t24():
	ent_text.insert(END, 'K')
	#K_text.append(bin_list.get(ANCHOR))
	#text_1.insert(END, bin_list.get(ANCHOR))
	#bin_list.delete(ANCHOR)
	K_ex()
def t25():
	ent_text.insert(END, 'l')
	#l_text.append(bin_list.get(ANCHOR))
	#text_1.insert(END, bin_list.get(ANCHOR))
	#bin_list.delete(ANCHOR)
	l_ex()
def t26():
	ent_text.insert(END, 'L')
	#L_text.append(bin_list.get(ANCHOR))
	#text_1.insert(END, bin_list.get(ANCHOR))
	#bin_list.delete(ANCHOR)
	L_ex()
def t27():
	ent_text.insert(END, 'm')
	#m_text.append(bin_list.get(ANCHOR))
	#text_1.insert(END, bin_list.get(ANCHOR))
	#bin_list.delete(ANCHOR)
	m_ex()
def t28():
	ent_text.insert(END, 'M')
	#M_text.append(bin_list.get(ANCHOR))
	#text_1.insert(END, bin_list.get(ANCHOR))
	#bin_list.delete(ANCHOR)
	M_ex()
def t29():
	ent_text.insert(END, 'n')
	#n_text.append(bin_list.get(ANCHOR))
	#text_1.insert(END, bin_list.get(ANCHOR))
	#bin_list.delete(ANCHOR)
	n_ex()
def t30():
	ent_text.insert(END, 'N')
	#N_text.append(bin_list.get(ANCHOR))
	#text_1.insert(END, bin_list.get(ANCHOR))
	#bin_list.delete(ANCHOR)
	N_ex()
def t31():
	ent_text.insert(END, 'o')
	#o_text.append(bin_list.get(ANCHOR))
	#text_1.insert(END, bin_list.get(ANCHOR))
	#bin_list.delete(ANCHOR)
	o_ex()
def t32():
	ent_text.insert(END, 'O')
	#O_text.append(bin_list.get(ANCHOR))
	#text_1.insert(END, bin_list.get(ANCHOR))
	#bin_list.delete(ANCHOR)
	O_ex()
def t33():
	ent_text.insert(END, 'ö')
	#ö_text.append(bin_list.get(ANCHOR))
	#text_1.insert(END, bin_list.get(ANCHOR))
	#bin_list.delete(ANCHOR)
	ö_ex()
def t34():
	ent_text.insert(END, 'Ö')
	#Ö_text.append(bin_list.get(ANCHOR))
	#text_1.insert(END, bin_list.get(ANCHOR))
	#bin_list.delete(ANCHOR)
	Ö_ex()
def t35():
	ent_text.insert(END, 'p')
	#p_text.append(bin_list.get(ANCHOR))
	#text_1.insert(END, bin_list.get(ANCHOR))
	#bin_list.delete(ANCHOR)
	p_ex()
def t36():
	ent_text.insert(END, 'P')
	#P_text.append(bin_list.get(ANCHOR))
	#text_1.insert(END, bin_list.get(ANCHOR))
	#bin_list.delete(ANCHOR)
	P_ex()
def t37():
	ent_text.insert(END, 'q')
	#q_text.append(bin_list.get(ANCHOR))
	#text_1.insert(END, bin_list.get(ANCHOR))
	#bin_list.delete(ANCHOR)
	q_ex()
def t38():
	ent_text.insert(END, 'Q')
	#Q_text.append(bin_list.get(ANCHOR))
	#text_1.insert(END, bin_list.get(ANCHOR))
	#bin_list.delete(ANCHOR)
	Q_ex()
def t39():
	ent_text.insert(END, 'r')
	#r_text.append(bin_list.get(ANCHOR))
	#text_1.insert(END, bin_list.get(ANCHOR))
	#bin_list.delete(ANCHOR)
	r_ex()
def t40():
	ent_text.insert(END, 'R')
	#R_text.append(bin_list.get(ANCHOR))
	#text_1.insert(END, bin_list.get(ANCHOR))
	#bin_list.delete(ANCHOR)
	R_ex()
def t41():
	ent_text.insert(END, 's')
	#s_text.append(bin_list.get(ANCHOR))
	#text_1.insert(END, bin_list.get(ANCHOR))
	#bin_list.delete(ANCHOR)
	s_ex()
def t42():
	ent_text.insert(END, 'S')
	#S_text.append(bin_list.get(ANCHOR))
	#text_1.insert(END, bin_list.get(ANCHOR))
	#bin_list.delete(ANCHOR)
	S_ex()
def t43():
	ent_text.insert(END, 't')
	#t_text.append(bin_list.get(ANCHOR))
	#text_1.insert(END, bin_list.get(ANCHOR))
	#bin_list.delete(ANCHOR)
	t_ex()
def t44():
	ent_text.insert(END, 'T')
	#T_text.append(bin_list.get(ANCHOR))
	#text_1.insert(END, bin_list.get(ANCHOR))
	#bin_list.delete(ANCHOR)
	T_ex()
def t45():
	ent_text.insert(END, 'u')
	#u_text.append(bin_list.get(ANCHOR))
	#text_1.insert(END, bin_list.get(ANCHOR))
	#bin_list.delete(ANCHOR)
	u_ex()
def t46():
	ent_text.insert(END, 'U')
	#U_text.append(bin_list.get(ANCHOR))
	#text_1.insert(END, bin_list.get(ANCHOR))
	#bin_list.delete(ANCHOR)
	U_ex()
def t47():
	ent_text.insert(END, 'ü')
	#ü_text.append(bin_list.get(ANCHOR))
	#text_1.insert(END, bin_list.get(ANCHOR))
	#bin_list.delete(ANCHOR)
	ü_ex()
def t48():
	ent_text.insert(END, 'Ü')
	#Ü_text.append(bin_list.get(ANCHOR))
	#text_1.insert(END, bin_list.get(ANCHOR))
	#bin_list.delete(ANCHOR)
	Ü_ex()
def t49():
	ent_text.insert(END, 'v')
	#v_text.append(bin_list.get(ANCHOR))
	#text_1.insert(END, bin_list.get(ANCHOR))
	#bin_list.delete(ANCHOR)
	v_ex()
def t50():
	ent_text.insert(END, 'V')
	#V_text.append(bin_list.get(ANCHOR))
	#text_1.insert(END, bin_list.get(ANCHOR))
	#bin_list.delete(ANCHOR)
	V_ex()
def t51():
	ent_text.insert(END, 'w')
	#w_text.append(bin_list.get(ANCHOR))
	#text_1.insert(END, bin_list.get(ANCHOR))
	#bin_list.delete(ANCHOR)
	w_ex()
def t52():
	ent_text.insert(END, 'W')
	#W_text.append(bin_list.get(ANCHOR))
	#text_1.insert(END, bin_list.get(ANCHOR))
	#bin_list.delete(ANCHOR)
	W_ex()
def t53():
	ent_text.insert(END, 'x')
	#x_text.append(bin_list.get(ANCHOR))
	#text_1.insert(END, bin_list.get(ANCHOR))
	#bin_list.delete(ANCHOR)
	x_ex()
def t54():
	ent_text.insert(END, 'X')
	#X_text.append(bin_list.get(ANCHOR))
	#text_1.insert(END, bin_list.get(ANCHOR))
	#bin_list.delete(ANCHOR)
	X_ex()
def t55():
	ent_text.insert(END, 'y')
	#y_text.append(bin_list.get(ANCHOR))
	#text_1.insert(END, bin_list.get(ANCHOR))
	#bin_list.delete(ANCHOR)
	y_ex()
def t56():
	ent_text.insert(END, 'Y')
	#Y_text.append(bin_list.get(ANCHOR))
	#text_1.insert(END, bin_list.get(ANCHOR))
	#bin_list.delete(ANCHOR)
	Y_ex()
def t57():
	ent_text.insert(END, 'z')
	#z_text.append(bin_list.get(ANCHOR))
	#text_1.insert(END, bin_list.get(ANCHOR))
	#bin_list.delete(ANCHOR)
	z_ex()
def t58():
	ent_text.insert(END, 'Z')
	#Z_text.append(bin_list.get(ANCHOR))
	#text_1.insert(END, bin_list.get(ANCHOR))
	#bin_list.delete(ANCHOR)
	Z_ex()

#_____________________________________________________________________________________________________________________________End_a2z

def t59():
	ent_text.insert(END,'!')
	#char_exclamation.append(bin_list.get(ANCHOR))
	#text_1.insert(END, bin_list.get(ANCHOR))
	#bin_list.delete(ANCHOR)
	char_exclamation_ex()
def t60():
	ent_text.insert(END,'"')
	#char_quotes.append(bin_list.get(ANCHOR))
	#text_1.insert(END, bin_list.get(ANCHOR))
	#bin_list.delete(ANCHOR)
	char_quotes_ex()
def t61():
	ent_text.insert(END,'$')
	#char_dollar.append(bin_list.get(ANCHOR))
	#text_1.insert(END, bin_list.get(ANCHOR))
	#bin_list.delete(ANCHOR)
	char_dollar_ex()
def t62():
	ent_text.insert(END,'%')
	#char_percent.append(bin_list.get(ANCHOR))
	#text_1.insert(END, bin_list.get(ANCHOR))
	#bin_list.delete(ANCHOR)
	char_percent_ex()
def t63():
	ent_text.insert(END,'&')
	#char_and.append(bin_list.get(ANCHOR))
	#text_1.insert(END, bin_list.get(ANCHOR))
	#bin_list.delete(ANCHOR)
	char_and_ex()
def t64():
	ent_text.insert(END,'/')
	#char_forward_slash.append(bin_list.get(ANCHOR))
	#text_1.insert(END, bin_list.get(ANCHOR))
	#bin_list.delete(ANCHOR)
	char_forward_slash_ex()
def t65():
	ent_text.insert(END,'{')
	#char_left_curly_bracket.append(bin_list.get(ANCHOR))
	#text_1.insert(END, bin_list.get(ANCHOR))
	#bin_list.delete(ANCHOR)
	char_left_curly_bracket_ex()
def t66():
	ent_text.insert(END,'(')
	#char_left_bracket.append(bin_list.get(ANCHOR))
	#text_1.insert(END, bin_list.get(ANCHOR))
	#bin_list.delete(ANCHOR)
	char_left_bracket_ex()
def t67():
	ent_text.insert(END,'[')
	#char_left_square_bracket.append(bin_list.get(ANCHOR))
	#text_1.insert(END, bin_list.get(ANCHOR))
	#bin_list.delete(ANCHOR)
	char_left_square_bracket_ex()
def t68():
	ent_text.insert(END,')')
	#char_right_bracket.append(bin_list.get(ANCHOR))
	#text_1.insert(END, bin_list.get(ANCHOR))
	#bin_list.delete(ANCHOR)
	char_right_bracket_ex()
def t69():
	ent_text.insert(END,']')
	#char_right_square_bracket.append(bin_list.get(ANCHOR))
	#text_1.insert(END, bin_list.get(ANCHOR))
	#bin_list.delete(ANCHOR)
	char_right_square_bracket_ex()
def t70():
	ent_text.insert(END,'=')
	#char_equals.append(bin_list.get(ANCHOR))
	#text_1.insert(END, bin_list.get(ANCHOR))
	#bin_list.delete(ANCHOR)
	char_equals_ex()
def t71():
	ent_text.insert(END,'}')
	#char_right_curly_bracket.append(bin_list.get(ANCHOR))
	#text_1.insert(END, bin_list.get(ANCHOR))
	bin_list.delete(ANCHOR)
	char_right_curly_bracket_ex()
def t72():
	ent_text.insert(END,'?')
	#char_question.append(bin_list.get(ANCHOR))
	#text_1.insert(END, bin_list.get(ANCHOR))
	#bin_list.delete(ANCHOR)
	char_question_ex()
def t73():
	ent_text.insert(END,'ß')
	#char_sz.append(bin_list.get(ANCHOR))
	#text_1.insert(END, bin_list.get(ANCHOR))
	#bin_list.delete(ANCHOR)
	char_sz_ex()
def t74():
	ent_text.insert(END,'\\')
	#char_back_slash.append(bin_list.get(ANCHOR))
	#text_1.insert(END, bin_list.get(ANCHOR))
	#bin_list.delete(ANCHOR)
	char_back_slash_ex()
def t75():
	ent_text.insert(END,',')
	#char_comma.append(bin_list.get(ANCHOR))
	#text_1.insert(END, bin_list.get(ANCHOR))
	#bin_list.delete(ANCHOR)
	char_comma_ex()
def t76():
	ent_text.insert(END,';')
	#char_semi_colon.append(bin_list.get(ANCHOR))
	#text_1.insert(END, bin_list.get(ANCHOR))
	#bin_list.delete(ANCHOR)
	char_semi_colon_ex()
def t77():
	ent_text.insert(END,':')
	#char_double_point.append(bin_list.get(ANCHOR))
	#text_1.insert(END, bin_list.get(ANCHOR))
	#bin_list.delete(ANCHOR)
	char_double_point_ex()
def t78():
	ent_text.insert(END,'.')
	#char_full_stop.append(bin_list.get(ANCHOR))
	#text_1.insert(END, bin_list.get(ANCHOR))
	#bin_list.delete(ANCHOR)
	char_full_stop_ex()
def t79():
	#underscore
	ent_text.insert(END,'_')
	#char_lower_case_hyfen.append(bin_list.get(ANCHOR))
	#text_1.insert(END, bin_list.get(ANCHOR))
	#bin_list.delete(ANCHOR)
	char_lower_case_hyfen_ex()
def t80():
	ent_text.insert(END,'-')
	#char_minus.append(bin_list.get(ANCHOR))
	#text_1.insert(END, bin_list.get(ANCHOR))
	#bin_list.delete(ANCHOR)
	char_minus_ex()
def t81():
	ent_text.insert(END,'#')
	#char_hashtag.append(bin_list.get(ANCHOR))
	#text_1.insert(END, bin_list.get(ANCHOR))
	#bin_list.delete(ANCHOR)
	char_hashtag_ex()
def t82():
	ent_text.insert(END,'+')
	#char_plus.append(bin_list.get(ANCHOR))
	#text_1.insert(END, bin_list.get(ANCHOR))
	#bin_list.delete(ANCHOR)
	char_plus_ex()
def t83():
	ent_text.insert(END,'*')
	#char_times_star.append(bin_list.get(ANCHOR))
	#text_1.insert(END, bin_list.get(ANCHOR))
	#bin_list.delete(ANCHOR)
	char_times_star_ex()
def t84():
	ent_text.insert(END,"'")
	#char_single_quotes.append(bin_list.get(ANCHOR))
	#text_1.insert(END, bin_list.get(ANCHOR))
	#bin_list.delete(ANCHOR)
	char_single_quotes_ex()
def t85():
	ent_text.insert(END,'<')
	#char_less_than.append(bin_list.get(ANCHOR))
	#text_1.insert(END, bin_list.get(ANCHOR))
	#bin_list.delete(ANCHOR)
	char_less_than_ex()
def t86():
	ent_text.insert(END,'>')
	#char_more_than.append(bin_list.get(ANCHOR))
	#text_1.insert(END, bin_list.get(ANCHOR))
	#bin_list.delete(ANCHOR)
	char_more_than_ex()
def t87():
	ent_text.insert(END,'|')
	#char_line_seperator.append(bin_list.get(ANCHOR))
	#text_1.insert(END, bin_list.get(ANCHOR))
	#bin_list.delete(ANCHOR)
	char_line_seperator_ex()
def t88():
	ent_text.insert(END,'~')
	#char_wavey.append(bin_list.get(ANCHOR))
	#text_1.insert(END, bin_list.get(ANCHOR))
	#bin_list.delete(ANCHOR)
	char_wavey_ex()
def t89():
	ent_text.insert(END,' ')
	#char_space.append(bin_list.get(ANCHOR))
	#text_1.insert(END, bin_list.get(ANCHOR))
	#bin_list.delete(ANCHOR)
	char_space_ex()
def t90():
	ent_text.insert(END, '0')
	#zero.append(bin_list.get(ANCHOR))
	#text_1.insert(END, bin_list.get(ANCHOR))
	#bin_list.delete(ANCHOR)
	#zero_ex()
def t91():
	ent_text.insert(END, '1')
	#one.append(bin_list.get(ANCHOR))
	#text_1.insert(END, bin_list.get(ANCHOR))
	bin_list.delete(ANCHOR)
def t92():
	ent_text.insert(END, '2')
	#two.append(bin_list.get(ANCHOR))
	#text_1.insert(END, bin_list.get(ANCHOR))
	bin_list.delete(ANCHOR)
def t93():
	ent_text.insert(END, '3')
	#three.append(bin_list.get(ANCHOR))
	#text_1.insert(END, bin_list.get(ANCHOR))
	bin_list.delete(ANCHOR)
def t94():
	ent_text.insert(END, '4')
	#four.append(bin_list.get(ANCHOR))
	#text_1.insert(END, bin_list.get(ANCHOR))
	bin_list.delete(ANCHOR)
def t95():
	ent_text.insert(END, '5')
	#five.append(bin_list.get(ANCHOR))
	#text_1.insert(END, bin_list.get(ANCHOR))
	bin_list.delete(ANCHOR)
def t96():
	ent_text.insert(END, '6')
	#six.append(bin_list.get(ANCHOR))
	#text_1.insert(END, bin_list.get(ANCHOR))
	bin_list.delete(ANCHOR)
def t97():
	ent_text.insert(END, '7')
	#seven.append(bin_list.get(ANCHOR))
	#text_1.insert(END, bin_list.get(ANCHOR))
	bin_list.delete(ANCHOR)
def t98():
	ent_text.insert(END, '8')
	#eight.append(bin_list.get(ANCHOR))
	#text_1.insert(END, bin_list.get(ANCHOR))
	bin_list.delete(ANCHOR)
def t99():
	ent_text.insert(END, '9')
	#nine.append(bin_list.get(ANCHOR))
	#text_1.insert(END, bin_list.get(ANCHOR))
	bin_list.delete(ANCHOR)
def t100():
	ent_text.insert(END, '10')
	#ten.append(bin_list.get(ANCHOR))
	#text_1.insert(END, bin_list.get(ANCHOR))
	bin_list.delete(ANCHOR)

#def letters,numbers and special for example purposes
#random numbers for changing colours
ran_nums = 0,1,2,3,4
def a_ex():
    forward36(random.choice(ran_nums))
    forward44(random.choice(ran_nums))
    forward45(random.choice(ran_nums))
    forward46(random.choice(ran_nums))
    forward54(random.choice(ran_nums))
    forward56(random.choice(ran_nums))
    forward64(random.choice(ran_nums))
    forward65(random.choice(ran_nums))
    forward66(random.choice(ran_nums))
    forward76(random.choice(ran_nums))
    #lab_1.config(text = len(a_text))
def A_ex():
    forward15(random.choice(ran_nums))
    forward24(random.choice(ran_nums))
    forward26(random.choice(ran_nums))
    forward33(random.choice(ran_nums))
    forward37(random.choice(ran_nums))
    forward42(random.choice(ran_nums))
    forward43(random.choice(ran_nums))
    forward44(random.choice(ran_nums))
    forward45(random.choice(ran_nums))
    forward46(random.choice(ran_nums))
    forward47(random.choice(ran_nums))
    forward48(random.choice(ran_nums))
    forward59(random.choice(ran_nums))
    forward51(random.choice(ran_nums))
def ä_ex():
    forward14(random.choice(ran_nums))
    forward16(random.choice(ran_nums))
    forward36(random.choice(ran_nums))
    forward44(random.choice(ran_nums))
    forward45(random.choice(ran_nums))
    forward46(random.choice(ran_nums))
    forward54(random.choice(ran_nums))
    forward56(random.choice(ran_nums))
    forward64(random.choice(ran_nums))
    forward65(random.choice(ran_nums))
    forward66(random.choice(ran_nums))
    forward76(random.choice(ran_nums))
def Ä_ex():
    forward4(random.choice(ran_nums))
    forward6(random.choice(ran_nums))
    forward15(random.choice(ran_nums))
    forward24(random.choice(ran_nums))
    forward26(random.choice(ran_nums))
    forward33(random.choice(ran_nums))
    forward37(random.choice(ran_nums))
    forward42(random.choice(ran_nums))
    forward43(random.choice(ran_nums))
    forward44(random.choice(ran_nums))
    forward45(random.choice(ran_nums))
    forward46(random.choice(ran_nums))
    forward47(random.choice(ran_nums))
    forward48(random.choice(ran_nums))
    forward59(random.choice(ran_nums))
    forward51(random.choice(ran_nums))
def b_ex():
    forward12(random.choice(ran_nums))
    forward22(random.choice(ran_nums))
    forward32(random.choice(ran_nums))
    forward42(random.choice(ran_nums))
    forward52(random.choice(ran_nums))
    forward62(random.choice(ran_nums))
    forward72(random.choice(ran_nums))
    forward82(random.choice(ran_nums))
    forward83(random.choice(ran_nums))
    forward84(random.choice(ran_nums))
    forward74(random.choice(ran_nums))
    forward64(random.choice(ran_nums))
    forward54(random.choice(ran_nums))
    forward53(random.choice(ran_nums))
def B_ex():
	forward12(random.choice(ran_nums))
	forward13(random.choice(ran_nums))
	forward14(random.choice(ran_nums))
	forward15(random.choice(ran_nums))
	forward22(random.choice(ran_nums))
	forward25(random.choice(ran_nums))
	forward35(random.choice(ran_nums))
	forward45(random.choice(ran_nums))
	forward43(random.choice(ran_nums))
	forward32(random.choice(ran_nums))
	forward42(random.choice(ran_nums))
	forward52(random.choice(ran_nums))
	forward62(random.choice(ran_nums))
	forward72(random.choice(ran_nums))
	forward82(random.choice(ran_nums))
	forward83(random.choice(ran_nums))
	forward84(random.choice(ran_nums))
	forward74(random.choice(ran_nums))
	forward64(random.choice(ran_nums))
	forward54(random.choice(ran_nums))
	forward53(random.choice(ran_nums))
def c_ex():
	forward76(random.choice(ran_nums))
	forward77(random.choice(ran_nums))
	forward78(random.choice(ran_nums))
	forward86(random.choice(ran_nums))
	forward96(random.choice(ran_nums))
	forward97(random.choice(ran_nums))
	forward98(random.choice(ran_nums))
def C_ex():
	forward23(random.choice(ran_nums))
	forward33(random.choice(ran_nums))
	forward43(random.choice(ran_nums))
	forward53(random.choice(ran_nums))
	forward63(random.choice(ran_nums))
	forward14(random.choice(ran_nums))
	forward15(random.choice(ran_nums))
	forward16(random.choice(ran_nums))
	forward17(random.choice(ran_nums))
	forward74(random.choice(ran_nums))
	forward75(random.choice(ran_nums))
	forward76(random.choice(ran_nums))
	forward77(random.choice(ran_nums))
def d_ex():
	forward24(random.choice(ran_nums))
	forward34(random.choice(ran_nums))
	forward44(random.choice(ran_nums))
	forward54(random.choice(ran_nums))
	forward64(random.choice(ran_nums))
	forward74(random.choice(ran_nums))
	forward63(random.choice(ran_nums))
	forward62(random.choice(ran_nums))
	forward52(random.choice(ran_nums))
	forward43(random.choice(ran_nums))
def D_ex():
	forward4(random.choice(ran_nums))
	forward14(random.choice(ran_nums))
	forward24(random.choice(ran_nums))
	forward34(random.choice(ran_nums))
	forward44(random.choice(ran_nums))
	forward5(random.choice(ran_nums))
	forward6(random.choice(ran_nums))
	forward7(random.choice(ran_nums))
	forward18(random.choice(ran_nums))
	forward29(random.choice(ran_nums))
	forward39(random.choice(ran_nums))
	forward48(random.choice(ran_nums))
	forward57(random.choice(ran_nums))
	forward56(random.choice(ran_nums))
	forward55(random.choice(ran_nums))
	forward54(random.choice(ran_nums))
def e_ex():
	forward53(random.choice(ran_nums))
	forward54(random.choice(ran_nums))
	forward55(random.choice(ran_nums))
	forward56(random.choice(ran_nums))
	forward57(random.choice(ran_nums))
	forward46(random.choice(ran_nums))
	forward44(random.choice(ran_nums))
	forward35(random.choice(ran_nums))
	forward36(random.choice(ran_nums))
	forward37(random.choice(ran_nums))
	forward64(random.choice(ran_nums))
	forward75(random.choice(ran_nums))
	forward86(random.choice(ran_nums))
	forward87(random.choice(ran_nums))
	forward77(random.choice(ran_nums))
def E_ex():
	forward56(random.choice(ran_nums))
	forward66(random.choice(ran_nums))
	forward76(random.choice(ran_nums))
	forward86(random.choice(ran_nums))
	forward96(random.choice(ran_nums))
	forward97(random.choice(ran_nums))
	forward98(random.choice(ran_nums))
	forward99(random.choice(ran_nums))
	forward77(random.choice(ran_nums))
	forward57(random.choice(ran_nums))
	forward58(random.choice(ran_nums))
	forward59(random.choice(ran_nums))
def f_ex():
	forward5(random.choice(ran_nums))
	forward6(random.choice(ran_nums))
	forward14(random.choice(ran_nums))
	forward17(random.choice(ran_nums))
	forward24(random.choice(ran_nums))
	forward34(random.choice(ran_nums))
	forward44(random.choice(ran_nums))
	forward54(random.choice(ran_nums))
	forward33(random.choice(ran_nums))
	forward35(random.choice(ran_nums))
def F_ex():
	forward1(random.choice(ran_nums))
	forward2(random.choice(ran_nums))
	forward3(random.choice(ran_nums))
	forward4(random.choice(ran_nums))
	forward11(random.choice(ran_nums))
	forward21(random.choice(ran_nums))
	forward22(random.choice(ran_nums))
	forward31(random.choice(ran_nums))
	forward41(random.choice(ran_nums))
def g_ex():
	forward9(random.choice(ran_nums))
	forward17(random.choice(ran_nums))
	forward18(random.choice(ran_nums))
	forward19(random.choice(ran_nums))
	forward27(random.choice(ran_nums))
	forward29(random.choice(ran_nums))
	forward37(random.choice(ran_nums))
	forward38(random.choice(ran_nums))
	forward39(random.choice(ran_nums))
	forward49(random.choice(ran_nums))
	forward59(random.choice(ran_nums))
	forward68(random.choice(ran_nums))
	forward57(random.choice(ran_nums))
def G_ex():
	forward15(random.choice(ran_nums))
	forward16(random.choice(ran_nums))
	forward17(random.choice(ran_nums))
	forward24(random.choice(ran_nums))
	forward28(random.choice(ran_nums))
	forward34(random.choice(ran_nums))
	forward44(random.choice(ran_nums))
	forward47(random.choice(ran_nums))
	forward54(random.choice(ran_nums))
	forward64(random.choice(ran_nums))
	forward65(random.choice(ran_nums))
	forward75(random.choice(ran_nums))
	forward76(random.choice(ran_nums))
	forward67(random.choice(ran_nums))
	forward57(random.choice(ran_nums))
	forward46(random.choice(ran_nums))
	forward47(random.choice(ran_nums))
	forward48(random.choice(ran_nums))
def h_ex():
	forward14(random.choice(ran_nums))
	forward24(random.choice(ran_nums))
	forward34(random.choice(ran_nums))
	forward44(random.choice(ran_nums))
	forward54(random.choice(ran_nums))
	forward64(random.choice(ran_nums))
	forward74(random.choice(ran_nums))
	forward45(random.choice(ran_nums))
	forward36(random.choice(ran_nums))
	forward37(random.choice(ran_nums))
	forward48(random.choice(ran_nums))
	forward58(random.choice(ran_nums))
	forward68(random.choice(ran_nums))
	forward78(random.choice(ran_nums))
def H_ex():
	forward45(random.choice(ran_nums))
	forward55(random.choice(ran_nums))
	forward65(random.choice(ran_nums))
	forward75(random.choice(ran_nums))
	forward85(random.choice(ran_nums))
	forward95(random.choice(ran_nums))
	forward66(random.choice(ran_nums))
	forward67(random.choice(ran_nums))
	forward48(random.choice(ran_nums))
	forward58(random.choice(ran_nums))
	forward68(random.choice(ran_nums))
	forward78(random.choice(ran_nums))
	forward88(random.choice(ran_nums))
	forward98(random.choice(ran_nums))
def i_ex():
	forward58(random.choice(ran_nums))
	forward68(random.choice(ran_nums))
	forward38(random.choice(ran_nums))
	forward78(random.choice(ran_nums))
	forward79(random.choice(ran_nums))
def I_ex():
	forward25(random.choice(ran_nums))
	forward26(random.choice(ran_nums))
	forward27(random.choice(ran_nums))
	forward36(random.choice(ran_nums))
	forward46(random.choice(ran_nums))
	forward56(random.choice(ran_nums))
	forward66(random.choice(ran_nums))
	forward65(random.choice(ran_nums))
	forward67(random.choice(ran_nums))
def j_ex():
	forward9(random.choice(ran_nums))
	forward29(random.choice(ran_nums))
	forward39(random.choice(ran_nums))
	forward49(random.choice(ran_nums))
	forward59(random.choice(ran_nums))
	forward69(random.choice(ran_nums))
	forward78(random.choice(ran_nums))
	forward77(random.choice(ran_nums))
	forward66(random.choice(ran_nums))
def J_ex():
	forward11(random.choice(ran_nums))
	forward12(random.choice(ran_nums))
	forward13(random.choice(ran_nums))
	forward14(random.choice(ran_nums))
	forward15(random.choice(ran_nums))
	forward16(random.choice(ran_nums))
	forward17(random.choice(ran_nums))
	forward18(random.choice(ran_nums))
	forward19(random.choice(ran_nums))
	forward25(random.choice(ran_nums))
	forward35(random.choice(ran_nums))
	forward45(random.choice(ran_nums))
	forward55(random.choice(ran_nums))
	forward64(random.choice(ran_nums))
	forward63(random.choice(ran_nums))
	forward62(random.choice(ran_nums))
	forward51(random.choice(ran_nums))
def k_ex():
	forward13(random.choice(ran_nums))
	forward23(random.choice(ran_nums))
	forward33(random.choice(ran_nums))
	forward43(random.choice(ran_nums))
	forward53(random.choice(ran_nums))
	forward63(random.choice(ran_nums))
	forward73(random.choice(ran_nums))
	forward54(random.choice(ran_nums))
	forward45(random.choice(ran_nums))
	forward64(random.choice(ran_nums))
	forward75(random.choice(ran_nums))
def K_ex():
	forward13(random.choice(ran_nums))
	forward23(random.choice(ran_nums))
	forward33(random.choice(ran_nums))
	forward43(random.choice(ran_nums))
	forward53(random.choice(ran_nums))
	forward63(random.choice(ran_nums))
	forward73(random.choice(ran_nums))
	forward83(random.choice(ran_nums))
	forward93(random.choice(ran_nums))
	forward44(random.choice(ran_nums))
	forward35(random.choice(ran_nums))
	forward26(random.choice(ran_nums))
	forward17(random.choice(ran_nums))
	forward64(random.choice(ran_nums))
	forward75(random.choice(ran_nums))
	forward86(random.choice(ran_nums))
	forward97(random.choice(ran_nums))
def l_ex():
	forward6(random.choice(ran_nums))
	forward16(random.choice(ran_nums))
	forward26(random.choice(ran_nums))
	forward36(random.choice(ran_nums))
	forward46(random.choice(ran_nums))
	forward56(random.choice(ran_nums))
	forward66(random.choice(ran_nums))
	forward67(random.choice(ran_nums))
def L_ex():
	forward6(random.choice(ran_nums))
	forward16(random.choice(ran_nums))
	forward26(random.choice(ran_nums))
	forward36(random.choice(ran_nums))
	forward46(random.choice(ran_nums))
	forward56(random.choice(ran_nums))
	forward66(random.choice(ran_nums))
	forward76(random.choice(ran_nums))
	forward86(random.choice(ran_nums))
	forward87(random.choice(ran_nums))
	forward89(random.choice(ran_nums))
	forward90(random.choice(ran_nums))
def m_ex():
	forward41(random.choice(ran_nums))
	forward51(random.choice(ran_nums))
	forward61(random.choice(ran_nums))
	forward71(random.choice(ran_nums))
	forward52(random.choice(ran_nums))
	forward43(random.choice(ran_nums))
	forward54(random.choice(ran_nums))
	forward65(random.choice(ran_nums))
	forward75(random.choice(ran_nums))
	forward56(random.choice(ran_nums))
	forward47(random.choice(ran_nums))
	forward58(random.choice(ran_nums))
	forward68(random.choice(ran_nums))
	forward78(random.choice(ran_nums))
def M_ex():
	forward56(random.choice(ran_nums))
	forward66(random.choice(ran_nums))
	forward76(random.choice(ran_nums))
	forward86(random.choice(ran_nums))
	forward96(random.choice(ran_nums))
	forward60(random.choice(ran_nums))
	forward67(random.choice(ran_nums))
	forward78(random.choice(ran_nums))
	forward69(random.choice(ran_nums))
	forward70(random.choice(ran_nums))
	forward80(random.choice(ran_nums))
	forward90(random.choice(ran_nums))
	forward100(random.choice(ran_nums))
def n_ex():
	forward33(random.choice(ran_nums))
	forward43(random.choice(ran_nums))
	forward53(random.choice(ran_nums))
	forward63(random.choice(ran_nums))
	forward73(random.choice(ran_nums))
	forward83(random.choice(ran_nums))
	forward93(random.choice(ran_nums))
	forward44(random.choice(ran_nums))
	forward35(random.choice(ran_nums))
	forward36(random.choice(ran_nums))
	forward37(random.choice(ran_nums))
	forward48(random.choice(ran_nums))
	forward58(random.choice(ran_nums))
	forward68(random.choice(ran_nums))
	forward78(random.choice(ran_nums))
	forward88(random.choice(ran_nums))
	forward98(random.choice(ran_nums))
def N_ex():
	forward35(random.choice(ran_nums))
	forward45(random.choice(ran_nums))
	forward55(random.choice(ran_nums))
	forward65(random.choice(ran_nums))
	forward75(random.choice(ran_nums))
	forward85(random.choice(ran_nums))
	forward46(random.choice(ran_nums))
	forward57(random.choice(ran_nums))
	forward68(random.choice(ran_nums))
	forward79(random.choice(ran_nums))
	forward90(random.choice(ran_nums))
	forward80(random.choice(ran_nums))
	forward70(random.choice(ran_nums))
	forward60(random.choice(ran_nums))
	forward50(random.choice(ran_nums))
	forward40(random.choice(ran_nums))
def o_ex():
	forward66(random.choice(ran_nums))
	forward67(random.choice(ran_nums))
	forward75(random.choice(ran_nums))
	forward85(random.choice(ran_nums))
	forward78(random.choice(ran_nums))
	forward88(random.choice(ran_nums))
	forward96(random.choice(ran_nums))
	forward97(random.choice(ran_nums))
def O_ex():
	forward4(random.choice(ran_nums))
	forward5(random.choice(ran_nums))
	forward6(random.choice(ran_nums))
	forward13(random.choice(ran_nums))
	forward17(random.choice(ran_nums))
	forward22(random.choice(ran_nums))
	forward28(random.choice(ran_nums))
	forward32(random.choice(ran_nums))
	forward38(random.choice(ran_nums))
	forward42(random.choice(ran_nums))
	forward48(random.choice(ran_nums))
	forward53(random.choice(ran_nums))
	forward64(random.choice(ran_nums))
	forward65(random.choice(ran_nums))
	forward66(random.choice(ran_nums))
	forward57(random.choice(ran_nums))
def ö_ex():
	forward45(random.choice(ran_nums))
	forward46(random.choice(ran_nums))
	forward54(random.choice(ran_nums))
	forward64(random.choice(ran_nums))
	forward57(random.choice(ran_nums))
	forward67(random.choice(ran_nums))
	forward75(random.choice(ran_nums))
	forward76(random.choice(ran_nums))
	forward25(random.choice(ran_nums))
	forward26(random.choice(ran_nums))
def Ö_ex():
	forward60(random.choice(ran_nums))
	forward70(random.choice(ran_nums))
	forward80(random.choice(ran_nums))
	forward89(random.choice(ran_nums))
	forward98(random.choice(ran_nums))
	forward97(random.choice(ran_nums))
	forward96(random.choice(ran_nums))
	forward85(random.choice(ran_nums))
	forward74(random.choice(ran_nums))
	forward64(random.choice(ran_nums))
	forward54(random.choice(ran_nums))
	forward45(random.choice(ran_nums))
	forward36(random.choice(ran_nums))
	forward37(random.choice(ran_nums))
	forward38(random.choice(ran_nums))
	forward49(random.choice(ran_nums))
	forward26(random.choice(ran_nums))
	forward28(random.choice(ran_nums))
def p_ex():
	forward4(random.choice(ran_nums))
	forward14(random.choice(ran_nums))
	forward24(random.choice(ran_nums))
	forward34(random.choice(ran_nums))
	forward44(random.choice(ran_nums))
	forward54(random.choice(ran_nums))
	forward64(random.choice(ran_nums))
	forward15(random.choice(ran_nums))
	forward16(random.choice(ran_nums))
	forward17(random.choice(ran_nums))
	forward27(random.choice(ran_nums))
	forward37(random.choice(ran_nums))
	forward47(random.choice(ran_nums))
	forward46(random.choice(ran_nums))
	forward45(random.choice(ran_nums))
def P_ex():
	forward4(random.choice(ran_nums))
	forward14(random.choice(ran_nums))
	forward24(random.choice(ran_nums))
	forward34(random.choice(ran_nums))
	forward44(random.choice(ran_nums))
	forward54(random.choice(ran_nums))
	forward64(random.choice(ran_nums))
	forward74(random.choice(ran_nums))
	forward84(random.choice(ran_nums))
	forward94(random.choice(ran_nums))
	forward5(random.choice(ran_nums))
	forward6(random.choice(ran_nums))
	forward7(random.choice(ran_nums))
	forward18(random.choice(ran_nums))
	forward28(random.choice(ran_nums))
	forward37(random.choice(ran_nums))
	forward35(random.choice(ran_nums))
	forward36(random.choice(ran_nums))
def q_ex():
	forward21(random.choice(ran_nums))
	forward31(random.choice(ran_nums))
	forward41(random.choice(ran_nums))
	forward42(random.choice(ran_nums))
	dorward43(random.choice(ran_nums))
	forward22(random.choice(ran_nums))
	forward23(random.choice(ran_nums))
	forward24(random.choice(ran_nums))
	forward14(random.choice(ran_nums))
	forward34(random.choice(ran_nums))
	forward44(random.choice(ran_nums))
	forward54(random.choice(ran_nums))
	forward64(random.choice(ran_nums))
def Q_ex():
	forward15(random.choice(ran_nums))
	forward24(random.choice(ran_nums))
	forward26(random.choice(ran_nums))
	forward34(random.choice(ran_nums))
	forward36(random.choice(ran_nums))
	forward44(random.choice(ran_nums))
	forward46(random.choice(ran_nums))
	forward54(random.choice(ran_nums))
	forward56(random.choice(ran_nums))
	forward64(random.choice(ran_nums))
	forward66(random.choice(ran_nums))
	forward75(random.choice(ran_nums))
	forward77(random.choice(ran_nums))
	forward88(random.choice(ran_nums))
def r_ex():
	forward63(random.choice(ran_nums))
	forward73(random.choice(ran_nums))
	forward83(random.choice(ran_nums))
	forward93(random.choice(ran_nums))
	forward54(random.choice(ran_nums))
	forward55(random.choice(ran_nums))
	forward56(random.choice(ran_nums))
	forward67(random.choice(ran_nums))
def R_ex():
	forward44(random.choice(ran_nums))
	forward54(random.choice(ran_nums))
	forward64(random.choice(ran_nums))
	forward74(random.choice(ran_nums))
	forward84(random.choice(ran_nums))
	forward94(random.choice(ran_nums))
	forward34(random.choice(ran_nums))
	forward35(random.choice(ran_nums))
	forward36(random.choice(ran_nums))
	forward37(random.choice(ran_nums))
	forward47(random.choice(ran_nums))
	forward57(random.choice(ran_nums))
	forward66(random.choice(ran_nums))
	forward65(random.choice(ran_nums))
	forward77(random.choice(ran_nums))
	forward87(random.choice(ran_nums))
	forward97(random.choice(ran_nums))
def s_ex():
	forward6(random.choice(ran_nums))
	forward5(random.choice(ran_nums))
	forward14(random.choice(ran_nums))
	forward17(random.choice(ran_nums))
	forward24(random.choice(ran_nums))
	forward35(random.choice(ran_nums))
	forward36(random.choice(ran_nums))
	forward47(random.choice(ran_nums))
	forward57(random.choice(ran_nums))
	forward66(random.choice(ran_nums))
	forward65(random.choice(ran_nums))
	forward54(random.choice(ran_nums))
def S_ex():
	forward29(random.choice(ran_nums))
	forward19(random.choice(ran_nums))
	forward8(random.choice(ran_nums))
	forward7(random.choice(ran_nums))
	forward16(random.choice(ran_nums))
	forward25(random.choice(ran_nums))
	forward35(random.choice(ran_nums))
	forward45(random.choice(ran_nums))
	forward56(random.choice(ran_nums))
	forward57(random.choice(ran_nums))
	forward58(random.choice(ran_nums))
	forward69(random.choice(ran_nums))
	forward80(random.choice(ran_nums))
	forward90(random.choice(ran_nums))
	forward99(random.choice(ran_nums))
	forward98(random.choice(ran_nums))
	forward97(random.choice(ran_nums))
	forward86(random.choice(ran_nums))
	forward75(random.choice(ran_nums))
def t_ex():
	forward27(random.choice(ran_nums))
	forward37(random.choice(ran_nums))
	forward47(random.choice(ran_nums))
	forward46(random.choice(ran_nums))
	forward45(random.choice(ran_nums))
	forward48(random.choice(ran_nums))
	forward49(random.choice(ran_nums))
	forward57(random.choice(ran_nums))
	forward67(random.choice(ran_nums))
	forward78(random.choice(ran_nums))
	forward79(random.choice(ran_nums))
	forward70(random.choice(ran_nums))
def T_ex():
	forward57(random.choice(ran_nums))
	forward67(random.choice(ran_nums))
	forward77(random.choice(ran_nums))
	forward87(random.choice(ran_nums))
	forward97(random.choice(ran_nums))
	forward55(random.choice(ran_nums))
	forward56(random.choice(ran_nums))
	forward58(random.choice(ran_nums))
	forward59(random.choice(ran_nums))
def u_ex():
	forward11(random.choice(ran_nums))
	forward21(random.choice(ran_nums))
	forward31(random.choice(ran_nums))
	forward41(random.choice(ran_nums))
	forward52(random.choice(ran_nums))
	forward53(random.choice(ran_nums))
	forward44(random.choice(ran_nums))
	forward34(random.choice(ran_nums))
	forward24(random.choice(ran_nums))
	forward14(random.choice(ran_nums))
def U_ex():
	forward3(random.choice(ran_nums))
	forward13(random.choice(ran_nums))
	forward23(random.choice(ran_nums))
	forward33(random.choice(ran_nums))
	forward43(random.choice(ran_nums))
	forward53(random.choice(ran_nums))
	forward63(random.choice(ran_nums))
	forward73(random.choice(ran_nums))
	forward84(random.choice(ran_nums))
	forward85(random.choice(ran_nums))
	forward86(random.choice(ran_nums))
	forward87(random.choice(ran_nums))
	forward78(random.choice(ran_nums))
	forward68(random.choice(ran_nums))
	forward58(random.choice(ran_nums))
	forward48(random.choice(ran_nums))
	forward38(random.choice(ran_nums))
	forward28(random.choice(ran_nums))
	forward18(random.choice(ran_nums))
	forward8(random.choice(ran_nums))
def ü_ex():
	forward24(random.choice(ran_nums))
	forward26(random.choice(ran_nums))
	forward44(random.choice(ran_nums))
	forward46(random.choice(ran_nums))
	forward54(random.choice(ran_nums))
	forward56(random.choice(ran_nums))
	forward64(random.choice(ran_nums))
	forward66(random.choice(ran_nums))
	forward74(random.choice(ran_nums))
	forward76(random.choice(ran_nums))
	forward85(random.choice(ran_nums))
def Ü_ex():
	forward3(random.choice(ran_nums))
	forward8(random.choice(ran_nums))
	forward23(random.choice(ran_nums))
	forward28(random.choice(ran_nums))
	forward33(random.choice(ran_nums))
	forward38(random.choice(ran_nums))
	forward43(random.choice(ran_nums))
	forward48(random.choice(ran_nums))
	forward53(random.choice(ran_nums))
	forward58(random.choice(ran_nums))
	forward63(random.choice(ran_nums))
	forward68(random.choice(ran_nums))
	forward74(random.choice(ran_nums))
	forward75(random.choice(ran_nums))
	forward76(random.choice(ran_nums))
	forward77(random.choice(ran_nums))
def v_ex():
	forward64(random.choice(ran_nums))
	forward75(random.choice(ran_nums))
	forward86(random.choice(ran_nums))
	forward77(random.choice(ran_nums))
	forward68(random.choice(ran_nums))
def V_ex():
	forward32(random.choice(ran_nums))
	forward43(random.choice(ran_nums))
	forward54(random.choice(ran_nums))
	forward65(random.choice(ran_nums))
	forward76(random.choice(ran_nums))
	forward67(random.choice(ran_nums))
	forward58(random.choice(ran_nums))
	forward49(random.choice(ran_nums))
	forward40(random.choice(ran_nums))
def w_ex():
	forward71(random.choice(ran_nums))
	forward82(random.choice(ran_nums))
	forward93(random.choice(ran_nums))
	forward84(random.choice(ran_nums))
	forward75(random.choice(ran_nums))
	forward86(random.choice(ran_nums))
	forward97(random.choice(ran_nums))
	forward88(random.choice(ran_nums))
	forward79(random.choice(ran_nums))
def W_ex():
	forward11(random.choice(ran_nums))
	forward21(random.choice(ran_nums))
	forward32(random.choice(ran_nums))
	forward42(random.choice(ran_nums))
	forward53(random.choice(ran_nums))
	forward63(random.choice(ran_nums))
	forward44(random.choice(ran_nums))
	forward34(random.choice(ran_nums))
	forward15(random.choice(ran_nums))
	forward25(random.choice(ran_nums))
	forward36(random.choice(ran_nums))
	forward46(random.choice(ran_nums))
	forward57(random.choice(ran_nums))
	forward67(random.choice(ran_nums))
	forward48(random.choice(ran_nums))
	forward38(random.choice(ran_nums))
	forward19(random.choice(ran_nums))
	forward29(random.choice(ran_nums))
def x_ex():
	forward64(random.choice(ran_nums))
	forward55(random.choice(ran_nums))
	forward46(random.choice(ran_nums))
	forward37(random.choice(ran_nums))
	forward28(random.choice(ran_nums))
	forward68(random.choice(ran_nums))
	forward57(random.choice(ran_nums))
	forward46(random.choice(ran_nums))
	forward35(random.choice(ran_nums))
	forward24(random.choice(ran_nums))
def X_ex():
	forward34(random.choice(ran_nums))
	forward45(random.choice(ran_nums))
	forward56(random.choice(ran_nums))
	forward67(random.choice(ran_nums))
	forward78(random.choice(ran_nums))
	forward89(random.choice(ran_nums))
	forward100(random.choice(ran_nums))
	forward94(random.choice(ran_nums))
	forward85(random.choice(ran_nums))
	forward76(random.choice(ran_nums))
	forward67(random.choice(ran_nums))
	forward58(random.choice(ran_nums))
	forward49(random.choice(ran_nums))
	forward40(random.choice(ran_nums))
def y_ex():
	forward42(random.choice(ran_nums))
	forward53(random.choice(ran_nums))
	forward64(random.choice(ran_nums))
	forward74(random.choice(ran_nums))
	forward84(random.choice(ran_nums))
	forward93(random.choice(ran_nums))
	forward94(random.choice(ran_nums))
	forward65(random.choice(ran_nums))
	forward56(random.choice(ran_nums))
def Y_ex():
	forward3(random.choice(ran_nums))
	forward14(random.choice(ran_nums))
	forward25(random.choice(ran_nums))
	forward36(random.choice(ran_nums))
	forward27(random.choice(ran_nums))
	forward18(random.choice(ran_nums))
	forward9(random.choice(ran_nums))
	forward36(random.choice(ran_nums))
	forward46(random.choice(ran_nums))
	forward56(random.choice(ran_nums))
	forward66(random.choice(ran_nums))
	forward76(random.choice(ran_nums))
	forward86(random.choice(ran_nums))
	forward96(random.choice(ran_nums))
def z_ex():
	forward5(random.choice(ran_nums))
	forward6(random.choice(ran_nums))
	forward7(random.choice(ran_nums))
	forward8(random.choice(ran_nums))
	forward35(random.choice(ran_nums))
	forward26(random.choice(ran_nums))
	forward17(random.choice(ran_nums))
	forward36(random.choice(ran_nums))
	forward37(random.choice(ran_nums))
	forward38(random.choice(ran_nums))
def Z_ex():
	forward12(random.choice(ran_nums))
	forward13(random.choice(ran_nums))
	forward14(random.choice(ran_nums))
	forward15(random.choice(ran_nums))
	forward16(random.choice(ran_nums))
	forward17(random.choice(ran_nums))
	forward18(random.choice(ran_nums))
	forward19(random.choice(ran_nums))
	forward28(random.choice(ran_nums))
	forward37(random.choice(ran_nums))
	forward46(random.choice(ran_nums))
	forward55(random.choice(ran_nums))
	forward64(random.choice(ran_nums))
	forward73(random.choice(ran_nums))
	forward82(random.choice(ran_nums))
	forward83(random.choice(ran_nums))
	forward85(random.choice(ran_nums))
	forward84(random.choice(ran_nums))
	forward86(random.choice(ran_nums))
	forward87(random.choice(ran_nums))
	forward88(random.choice(ran_nums))
	forward89(random.choice(ran_nums))

#extra
#chars

def char_exclamation_ex():
	forward25(random.choice(ran_nums))
	forward26(random.choice(ran_nums))
	forward35(random.choice(ran_nums))
	forward36(random.choice(ran_nums))
	forward45(random.choice(ran_nums))
	forward46(random.choice(ran_nums))
	forward55(random.choice(ran_nums))
	forward56(random.choice(ran_nums))
	forward65(random.choice(ran_nums))
	forward66(random.choice(ran_nums))
	forward85(random.choice(ran_nums))
	forward86(random.choice(ran_nums))
	forward95(random.choice(ran_nums))
	forward96(random.choice(ran_nums))
def char_quotes_ex():
	forward12(random.choice(ran_nums))
	forward22(random.choice(ran_nums))
	forward32(random.choice(ran_nums))
	forward42(random.choice(ran_nums))
	forward14(random.choice(ran_nums))
	forward24(random.choice(ran_nums))
	forward34(random.choice(ran_nums))
	forward44(random.choice(ran_nums))
def char_dollar_ex():
	forward14(random.choice(ran_nums))
	forward24(random.choice(ran_nums))
	forward34(random.choice(ran_nums))
	forward44(random.choice(ran_nums))
	forward54(random.choice(ran_nums))
	forward64(random.choice(ran_nums))
	forward74(random.choice(ran_nums))
	forward84(random.choice(ran_nums))
	forward94(random.choice(ran_nums))
	forward72(random.choice(ran_nums))
	forward83(random.choice(ran_nums))
	forward85(random.choice(ran_nums))
	forward76(random.choice(ran_nums))
	forward66(random.choice(ran_nums))
	forward55(random.choice(ran_nums))
	forward43(random.choice(ran_nums))
	forward32(random.choice(ran_nums))
	forward23(random.choice(ran_nums))
	forward15(random.choice(ran_nums))
	forward26(random.choice(ran_nums))
def char_percent_ex():
	forward73(random.choice(ran_nums))
	forward64(random.choice(ran_nums))
	forward55(random.choice(ran_nums))
	forward46(random.choice(ran_nums))
	forward37(random.choice(ran_nums))
	forward28(random.choice(ran_nums))
	forward19(random.choice(ran_nums))
	forward82(random.choice(ran_nums))
	forward34(random.choice(ran_nums))
	forward67(random.choice(ran_nums))
def char_and_ex():
	forward5(random.choice(ran_nums))
	forward6(random.choice(ran_nums))
	forward14(random.choice(ran_nums))
	forward24(random.choice(ran_nums))
	forward35(random.choice(ran_nums))
	forward46(random.choice(ran_nums))
	forward57(random.choice(ran_nums))
	forward47(random.choice(ran_nums))
	forward56(random.choice(ran_nums))
	forward55(random.choice(ran_nums))
	forward54(random.choice(ran_nums))
	forward43(random.choice(ran_nums))
	forward34(random.choice(ran_nums))
def char_forward_slash_ex():
	forward91(random.choice(ran_nums))
	forward82(random.choice(ran_nums))
	forward73(random.choice(ran_nums))
	forward64(random.choice(ran_nums))
	forward55(random.choice(ran_nums))
	forward46(random.choice(ran_nums))
	forward37(random.choice(ran_nums))
def char_left_curly_bracket_ex():
	forward18(random.choice(ran_nums))
	forward19(random.choice(ran_nums))
	forward28(random.choice(ran_nums))
	forward37(random.choice(ran_nums))
	forward47(random.choice(ran_nums))
	forward56(random.choice(ran_nums))
	forward67(random.choice(ran_nums))
	forward77(random.choice(ran_nums))
	forward88(random.choice(ran_nums))
	forward98(random.choice(ran_nums))
	forward99(random.choice(ran_nums))
def char_left_bracket_ex():
	forward4(random.choice(ran_nums))
	forward14(random.choice(ran_nums))
	forward23(random.choice(ran_nums))
	forward33(random.choice(ran_nums))
	forward42(random.choice(ran_nums))
	forward52(random.choice(ran_nums))
	forward63(random.choice(ran_nums))
	forward73(random.choice(ran_nums))
	forward84(random.choice(ran_nums))
	forward94(random.choice(ran_nums))
def char_left_square_bracket_ex():
	forward8(random.choice(ran_nums))
	forward9(random.choice(ran_nums))
	forward10(random.choice(ran_nums))
	forward18(random.choice(ran_nums))
	forward28(random.choice(ran_nums))
	forward38(random.choice(ran_nums))
	forward48(random.choice(ran_nums))
	forward58(random.choice(ran_nums))
	forward68(random.choice(ran_nums))
	forward78(random.choice(ran_nums))
	forward88(random.choice(ran_nums))
	forward98(random.choice(ran_nums))
	forward99(random.choice(ran_nums))
	forward100(random.choice(ran_nums))
def char_right_bracket_ex():
	forward6(random.choice(ran_nums))
	forward16(random.choice(ran_nums))
	forward27(random.choice(ran_nums))
	forward37(random.choice(ran_nums))
	forward48(random.choice(ran_nums))
	forward58(random.choice(ran_nums))
	forward67(random.choice(ran_nums))
	forward77(random.choice(ran_nums))
	forward86(random.choice(ran_nums))
	forward96(random.choice(ran_nums))
def char_right_square_bracket_ex():
	forward2(random.choice(ran_nums))
	forward3(random.choice(ran_nums))
	forward4(random.choice(ran_nums))
	forward14(random.choice(ran_nums))
	forward24(random.choice(ran_nums))
	forward34(random.choice(ran_nums))
	forward44(random.choice(ran_nums))
	forward54(random.choice(ran_nums))
	forward64(random.choice(ran_nums))
	forward74(random.choice(ran_nums))
	forward84(random.choice(ran_nums))
	forward94(random.choice(ran_nums))
	forward93(random.choice(ran_nums))
	forward92(random.choice(ran_nums))
def char_equals_ex():
	forward22(random.choice(ran_nums))
	forward23(random.choice(ran_nums))
	forward24(random.choice(ran_nums))
	forward25(random.choice(ran_nums))
	forward26(random.choice(ran_nums))
	forward27(random.choice(ran_nums))
	forward28(random.choice(ran_nums))
	forward29(random.choice(ran_nums))
	forward62(random.choice(ran_nums))
	forward63(random.choice(ran_nums))
	forward64(random.choice(ran_nums))
	forward65(random.choice(ran_nums))
	forward66(random.choice(ran_nums))
	forward67(random.choice(ran_nums))
	forward68(random.choice(ran_nums))
	forward69(random.choice(ran_nums))
def char_right_curly_bracket_ex():
	forward1(random.choice(ran_nums))
	forward2(random.choice(ran_nums))
	forward13(random.choice(ran_nums))
	forward23(random.choice(ran_nums))
	forward34(random.choice(ran_nums))
	forward44(random.choice(ran_nums))
	forward55(random.choice(ran_nums))
	forward64(random.choice(ran_nums))
	forward74(random.choice(ran_nums))
	forward83(random.choice(ran_nums))
	forward93(random.choice(ran_nums))
	forward91(random.choice(ran_nums))
	forward92(random.choice(ran_nums))
def char_question_ex():
	forward33(random.choice(ran_nums))
	forward23(random.choice(ran_nums))
	forward14(random.choice(ran_nums))
	forward5(random.choice(ran_nums))
	forward6(random.choice(ran_nums))
	forward17(random.choice(ran_nums))
	forward28(random.choice(ran_nums))
	forward38(random.choice(ran_nums))
	forward47(random.choice(ran_nums))
	forward56(random.choice(ran_nums))
	forward66(random.choice(ran_nums))
	forward86(random.choice(ran_nums))
def char_sz_ex():
	forward15(random.choice(ran_nums))
	forward16(random.choice(ran_nums))
	forward27(random.choice(ran_nums))
	forward37(random.choice(ran_nums))
	forward35(random.choice(ran_nums))
	forward36(random.choice(ran_nums))
	forward46(random.choice(ran_nums))
	forward57(random.choice(ran_nums))
	forward67(random.choice(ran_nums))
	forward76(random.choice(ran_nums))
	forward75(random.choice(ran_nums))
	forward85(random.choice(ran_nums))
	forward65(random.choice(ran_nums))
	forward55(random.choice(ran_nums))
	forward45(random.choice(ran_nums))
	forward25(random.choice(ran_nums))
def char_back_slash_ex():
	forward13(random.choice(ran_nums))
	forward35(random.choice(ran_nums))
	forward24(random.choice(ran_nums))
	forward46(random.choice(ran_nums))
	forward68(random.choice(ran_nums))
	forward57(random.choice(ran_nums))
	forward79(random.choice(ran_nums))
def char_comma_ex():
	forward48(random.choice(ran_nums))
	forward58(random.choice(ran_nums))
	forward67(random.choice(ran_nums))
def char_semi_colon_ex():
	forward55(random.choice(ran_nums))
	forward65(random.choice(ran_nums))
	forward74(random.choice(ran_nums))
	forward35(random.choice(ran_nums))
def char_double_point_ex():
	forward48(random.choice(ran_nums))
	forward49(random.choice(ran_nums))
	forward58(random.choice(ran_nums))
	forward59(random.choice(ran_nums))
	forward78(random.choice(ran_nums))
	forward79(random.choice(ran_nums))
	forward88(random.choice(ran_nums))
	forward89(random.choice(ran_nums))
def char_full_stop_ex():
	forward1(random.choice(ran_nums))
	forward2(random.choice(ran_nums))
	forward11(random.choice(ran_nums))
	forward12(random.choice(ran_nums))
def char_lower_case_hyfen_ex():
	forward91(random.choice(ran_nums))
	forward92(random.choice(ran_nums))
	forward93(random.choice(ran_nums))
def char_minus_ex():
	forward64(random.choice(ran_nums))
	forward65(random.choice(ran_nums))
	forward66(random.choice(ran_nums))
def char_hashtag_ex():
	forward22(random.choice(ran_nums))
	forward23(random.choice(ran_nums))
	forward24(random.choice(ran_nums))
	forward25(random.choice(ran_nums))
	forward26(random.choice(ran_nums))
	forward27(random.choice(ran_nums))
	forward28(random.choice(ran_nums))
	forward29(random.choice(ran_nums))
	forward30(random.choice(ran_nums))
	forward42(random.choice(ran_nums))
	forward43(random.choice(ran_nums))
	forward44(random.choice(ran_nums))
	forward45(random.choice(ran_nums))
	forward46(random.choice(ran_nums))
	forward47(random.choice(ran_nums))
	forward48(random.choice(ran_nums))
	forward49(random.choice(ran_nums))
	forward61(random.choice(ran_nums))
	forward52(random.choice(ran_nums))
	forward16(random.choice(ran_nums))
	forward34(random.choice(ran_nums))
	forward25(random.choice(ran_nums))
	forward64(random.choice(ran_nums))
	forward55(random.choice(ran_nums))
	forward37(random.choice(ran_nums))
	forward28(random.choice(ran_nums))
	forward19(random.choice(ran_nums))
def char_plus_ex():
	forward35(random.choice(ran_nums))
	forward45(random.choice(ran_nums))
	forward65(random.choice(ran_nums))
	forward75(random.choice(ran_nums))
	forward85(random.choice(ran_nums))
	forward95(random.choice(ran_nums))
	forward62(random.choice(ran_nums))
	forward63(random.choice(ran_nums))
	forward64(random.choice(ran_nums))
	forward66(random.choice(ran_nums))
	forward67(random.choice(ran_nums))
	forward68(random.choice(ran_nums))
	forward69(random.choice(ran_nums))
def char_times_star_ex():
	forward52(random.choice(ran_nums))
	forward53(random.choice(ran_nums))
	forward54(random.choice(ran_nums))
	forward55(random.choice(ran_nums))
	forward56(random.choice(ran_nums))
	forward57(random.choice(ran_nums))
	forward58(random.choice(ran_nums))
	forward59(random.choice(ran_nums))
	forward60(random.choice(ran_nums))
	forward96(random.choice(ran_nums))
	forward86(random.choice(ran_nums))
	forward76(random.choice(ran_nums))
	forward66(random.choice(ran_nums))
	forward46(random.choice(ran_nums))
	forward36(random.choice(ran_nums))
	forward22(random.choice(ran_nums))
	forward26(random.choice(ran_nums))
	forward93(random.choice(ran_nums))
	forward84(random.choice(ran_nums))
	forward75(random.choice(ran_nums))
	forward57(random.choice(ran_nums))
	forward48(random.choice(ran_nums))
	forward39(random.choice(ran_nums))
	forward30(random.choice(ran_nums))
	forward99(random.choice(ran_nums))
	forward88(random.choice(ran_nums))
	forward77(random.choice(ran_nums))
	forward55(random.choice(ran_nums))
	forward44(random.choice(ran_nums))
	forward33(random.choice(ran_nums))
def char_single_quotes_ex():
	forward26(random.choice(ran_nums))
	forward27(random.choice(ran_nums))
	forward36(random.choice(ran_nums))
	forward37(random.choice(ran_nums))
	forward48(random.choice(ran_nums))
	forward57(random.choice(ran_nums))
def char_less_than_ex():
	forward71(random.choice(ran_nums))
	forward82(random.choice(ran_nums))
	forward93(random.choice(ran_nums))
	forward62(random.choice(ran_nums))
	forward53(random.choice(ran_nums))
def char_more_than_ex():
	forward58(random.choice(ran_nums))
	forward69(random.choice(ran_nums))
	forward80(random.choice(ran_nums))
	forward89(random.choice(ran_nums))
	forward98(random.choice(ran_nums))
def char_line_seperator_ex():
	forward1(random.choice(ran_nums))
	forward11(random.choice(ran_nums))
	forward21(random.choice(ran_nums))
	forward31(random.choice(ran_nums))
	forward41(random.choice(ran_nums))
	forward51(random.choice(ran_nums))
	forward61(random.choice(ran_nums))
	forward71(random.choice(ran_nums))
	forward81(random.choice(ran_nums))
	forward91(random.choice(ran_nums))
def char_wavey_ex():
	forward41(random.choice(ran_nums))
	forward32(random.choice(ran_nums))
	forward33(random.choice(ran_nums))
	forward44(random.choice(ran_nums))
	forward55(random.choice(ran_nums))
	forward56(random.choice(ran_nums))
	forward47(random.choice(ran_nums))
	forward48(random.choice(ran_nums))
	forward39(random.choice(ran_nums))
def char_space_ex():
	forward81(random.choice(ran_nums))
	forward92(random.choice(ran_nums))
	forward93(random.choice(ran_nums))
	forward94(random.choice(ran_nums))
	forward95(random.choice(ran_nums))
	forward96(random.choice(ran_nums))
	forward97(random.choice(ran_nums))
	forward98(random.choice(ran_nums))
	forward99(random.choice(ran_nums))
	forward90(random.choice(ran_nums))

#reset green,yellow,orange,red
def reset_green():
	forward1(0)
	forward2(0)
	forward3(0)
	forward4(0)
	forward5(0)
	forward6(0)
	forward7(0)
	forward8(0)
	forward9(0)
	forward10(0)
	forward11(0)
	forward12(0)
	forward13(0)
	forward14(0)
	forward15(0)
	forward16(0)
	forward17(0)
	forward18(0)
	forward19(0)
	forward20(0)
	forward21(0)
	forward22(0)
	forward23(0)
	forward24(0)
	forward25(0)
	forward26(0)
	forward27(0)
	forward28(0)
	forward29(0)
	forward30(0)
	forward31(0)
	forward32(0)
	forward33(0)
	forward34(0)
	forward35(0)
	forward36(0)
	forward37(0)
	forward38(0)
	forward39(0)
	forward40(0)
	forward41(0)
	forward42(0)
	forward43(0)
	forward44(0)
	forward45(0)
	forward46(0)
	forward47(0)
	forward48(0)
	forward49(0)
	forward50(0)
	forward51(0)
	forward52(0)
	forward53(0)
	forward54(0)
	forward55(0)
	forward56(0)
	forward57(0)
	forward58(0)
	forward59(0)
	forward60(0)
	forward61(0)
	forward62(0)
	forward63(0)
	forward64(0)
	forward65(0)
	forward66(0)
	forward67(0)
	forward68(0)
	forward69(0)
	forward70(0)
	forward71(0)
	forward72(0)
	forward73(0)
	forward74(0)
	forward75(0)
	forward76(0)
	forward77(0)
	forward78(0)
	forward79(0)
	forward80(0)
	forward81(0)
	forward82(0)
	forward83(0)
	forward84(0)
	forward85(0)
	forward86(0)
	forward87(0)
	forward88(0)
	forward89(0)
	forward90(0)
	forward91(0)
	forward92(0)
	forward93(0)
	forward94(0)
	forward95(0)
	forward96(0)
	forward97(0)
	forward98(0)
	forward99(0)
	forward100(0)

def reset_yellow():
	forward1(1)
	forward2(1)
	forward3(1)
	forward4(1)
	forward5(1)
	forward6(1)
	forward7(1)
	forward8(1)
	forward9(1)
	forward10(1)
	forward11(1)
	forward12(1)
	forward13(1)
	forward14(1)
	forward15(1)
	forward16(1)
	forward17(1)
	forward18(1)
	forward19(1)
	forward20(1)
	forward21(1)
	forward22(1)
	forward23(1)
	forward24(1)
	forward25(1)
	forward26(1)
	forward27(1)
	forward28(1)
	forward29(1)
	forward30(1)
	forward31(1)
	forward32(1)
	forward33(1)
	forward34(1)
	forward35(1)
	forward36(1)
	forward37(1)
	forward38(1)
	forward39(1)
	forward40(1)
	forward41(1)
	forward42(1)
	forward43(1)
	forward44(1)
	forward45(1)
	forward46(1)
	forward47(1)
	forward48(1)
	forward49(1)
	forward50(1)
	forward51(1)
	forward52(1)
	forward53(1)
	forward54(1)
	forward55(1)
	forward56(1)
	forward57(1)
	forward58(1)
	forward59(1)
	forward60(1)
	forward61(1)
	forward62(1)
	forward63(1)
	forward64(1)
	forward65(1)
	forward66(1)
	forward67(1)
	forward68(1)
	forward69(1)
	forward70(1)
	forward71(1)
	forward72(1)
	forward73(1)
	forward74(1)
	forward75(1)
	forward76(1)
	forward77(1)
	forward78(1)
	forward79(1)
	forward80(1)
	forward81(1)
	forward82(1)
	forward83(1)
	forward84(1)
	forward85(1)
	forward86(1)
	forward87(1)
	forward88(1)
	forward89(1)
	forward90(1)
	forward91(1)
	forward92(1)
	forward93(1)
	forward94(1)
	forward95(1)
	forward96(1)
	forward97(1)
	forward98(1)
	forward99(1)
	forward100(1)

def reset_orange():
	forward1(2)
	forward2(2)
	forward3(2)
	forward4(2)
	forward5(2)
	forward6(2)
	forward7(2)
	forward8(2)
	forward9(2)
	forward10(2)
	forward11(2)
	forward12(2)
	forward13(2)
	forward14(2)
	forward15(2)
	forward16(2)
	forward17(2)
	forward18(2)
	forward19(2)
	forward20(2)
	forward21(2)
	forward22(2)
	forward23(2)
	forward24(2)
	forward25(2)
	forward26(2)
	forward27(2)
	forward28(2)
	forward29(2)
	forward30(2)
	forward31(2)
	forward32(2)
	forward33(2)
	forward34(2)
	forward35(2)
	forward36(2)
	forward37(2)
	forward38(2)
	forward39(2)
	forward40(2)
	forward41(2)
	forward42(2)
	forward43(2)
	forward44(2)
	forward45(2)
	forward46(2)
	forward47(2)
	forward48(2)
	forward49(2)
	forward50(2)
	forward51(2)
	forward52(2)
	forward53(2)
	forward54(2)
	forward55(2)
	forward56(2)
	forward57(2)
	forward58(2)
	forward59(2)
	forward60(2)
	forward61(2)
	forward62(2)
	forward63(2)
	forward64(2)
	forward65(2)
	forward66(2)
	forward67(2)
	forward68(2)
	forward69(2)
	forward70(2)
	forward71(2)
	forward72(2)
	forward73(2)
	forward74(2)
	forward75(2)
	forward76(2)
	forward77(2)
	forward78(2)
	forward79(2)
	forward80(2)
	forward81(2)
	forward82(2)
	forward83(2)
	forward84(2)
	forward85(2)
	forward86(2)
	forward87(2)
	forward88(2)
	forward89(2)
	forward90(2)
	forward91(2)
	forward92(2)
	forward93(2)
	forward94(2)
	forward95(2)
	forward96(2)
	forward97(2)
	forward98(2)
	forward99(2)
	forward100(2)

#red
def reset_red():
	forward1(3)
	forward2(3)
	forward3(3)
	forward4(3)
	forward5(3)
	forward6(3)
	forward7(3)
	forward8(3)
	forward9(3)
	forward10(3)
	forward11(3)
	forward12(3)
	forward13(3)
	forward14(3)
	forward15(3)
	forward16(3)
	forward17(3)
	forward18(3)
	forward19(3)
	forward20(3)
	forward21(3)
	forward22(3)
	forward23(3)
	forward24(3)
	forward25(3)
	forward26(3)
	forward27(3)
	forward28(3)
	forward29(3)
	forward30(3)
	forward31(3)
	forward32(3)
	forward33(3)
	forward34(3)
	forward35(3)
	forward36(3)
	forward37(3)
	forward38(3)
	forward39(3)
	forward40(3)
	forward41(3)
	forward42(3)
	forward43(3)
	forward44(3)
	forward45(3)
	forward46(3)
	forward47(3)
	forward48(3)
	forward49(3)
	forward50(3)
	forward51(3)
	forward52(3)
	forward53(3)
	forward54(3)
	forward55(3)
	forward56(3)
	forward57(3)
	forward58(3)
	forward59(3)
	forward60(3)
	forward61(3)
	forward62(3)
	forward63(3)
	forward64(3)
	forward65(3)
	forward66(3)
	forward67(3)
	forward68(3)
	forward69(3)
	forward70(3)
	forward71(3)
	forward72(3)
	forward73(3)
	forward74(3)
	forward75(3)
	forward76(3)
	forward77(3)
	forward78(3)
	forward79(3)
	forward80(3)
	forward81(3)
	forward82(3)
	forward83(3)
	forward84(3)
	forward85(3)
	forward86(3)
	forward87(3)
	forward88(3)
	forward89(3)
	forward90(3)
	forward91(3)
	forward92(3)
	forward93(3)
	forward94(3)
	forward95(3)
	forward96(3)
	forward97(3)
	forward98(3)
	forward99(3)
	forward100(3)

#blue
def random_entries1():
	ent_1.delete(0,END)
	ent_1.insert(END, ztext1[0])
	ent_1.insert(END, ztext2[0])
	ent_1.insert(END, ztext3[0])
	ent_1.insert(END, ztext4[0])
	ent_1.insert(END, ztext5[0])
	ent_1.insert(END, ztext6[0])
	ent_1.insert(END, ztext7[0])
	ent_1.insert(END, ztext8[0])
	ent_1.insert(END, ztext9[0])
	ent_1.insert(END, ztext10[0])
	forward1(4)
	forward2(4)
	forward3(4)
	forward4(4)
	forward5(4)
	forward6(4)
	forward7(4)
	forward8(4)
	forward9(4)
	forward10(4)
	ent_2.delete(0,END)
	ent_2.insert(END, ztext11[0])
	ent_2.insert(END, ztext12[0])
	ent_2.insert(END, ztext13[0])
	ent_2.insert(END, ztext14[0])
	ent_2.insert(END, ztext15[0])
	ent_2.insert(END, ztext16[0])
	ent_2.insert(END, ztext17[0])
	ent_2.insert(END, ztext18[0])
	ent_2.insert(END, ztext19[0])
	ent_2.insert(END, ztext20[0])
	forward11(4)
	forward12(4)
	forward13(4)
	forward14(4)
	forward15(4)
	forward16(4)
	forward17(4)
	forward18(4)
	forward19(4)
	forward20(4)
	ent_3.delete(0,END)
	ent_3.insert(END, ztext21[0])
	ent_3.insert(END, ztext22[0])
	ent_3.insert(END, ztext23[0])
	ent_3.insert(END, ztext24[0])
	ent_3.insert(END, ztext25[0])
	ent_3.insert(END, ztext26[0])
	ent_3.insert(END, ztext27[0])
	ent_3.insert(END, ztext28[0])
	ent_3.insert(END, ztext29[0])
	ent_3.insert(END, ztext30[0])
	forward21(4)
	forward22(4)
	forward23(4)
	forward24(4)
	forward25(4)
	forward26(4)
	forward27(4)
	forward28(4)
	forward29(4)
	forward30(4)
	ent_4.delete(0,END)
	ent_4.insert(END, ztext31[0])
	ent_4.insert(END, ztext32[0])
	ent_4.insert(END, ztext33[0])
	ent_4.insert(END, ztext34[0])
	ent_4.insert(END, ztext35[0])
	ent_4.insert(END, ztext36[0])
	ent_4.insert(END, ztext37[0])
	ent_4.insert(END, ztext38[0])
	ent_4.insert(END, ztext39[0])
	ent_4.insert(END, ztext40[0])
	forward31(4)
	forward32(4)
	forward33(4)
	forward34(4)
	forward35(4)
	forward36(4)
	forward37(4)
	forward38(4)
	forward39(4)
	forward40(4)
	ent_5.delete(0,END)
	ent_5.insert(END, ztext41[0])
	ent_5.insert(END, ztext42[0])
	ent_5.insert(END, ztext43[0])
	ent_5.insert(END, ztext44[0])
	ent_5.insert(END, ztext45[0])
	ent_5.insert(END, ztext46[0])
	ent_5.insert(END, ztext47[0])
	ent_5.insert(END, ztext48[0])
	ent_5.insert(END, ztext49[0])
	ent_5.insert(END, ztext50[0])
	forward41(4)
	forward42(4)
	forward43(4)
	forward44(4)
	forward45(4)
	forward46(4)
	forward47(4)
	forward48(4)
	forward49(4)
	forward50(4)
	ent_6.delete(0,END)
	ent_6.insert(END, ztext51[0])
	ent_6.insert(END, ztext52[0])
	ent_6.insert(END, ztext53[0])
	ent_6.insert(END, ztext54[0])
	ent_6.insert(END, ztext55[0])
	ent_6.insert(END, ztext56[0])
	ent_6.insert(END, ztext57[0])
	ent_6.insert(END, ztext58[0])
	ent_6.insert(END, ztext59[0])
	ent_6.insert(END, ztext60[0])
	forward51(4)
	forward52(4)
	forward53(4)
	forward54(4)
	forward55(4)
	forward56(4)
	forward57(4)
	forward58(4)
	forward59(4)
	forward60(4)
	ent_7.delete(0,END)
	ent_7.insert(END, ztext61[0])
	ent_7.insert(END, ztext62[0])
	ent_7.insert(END, ztext63[0])
	ent_7.insert(END, ztext64[0])
	ent_7.insert(END, ztext65[0])
	ent_7.insert(END, ztext66[0])
	ent_7.insert(END, ztext67[0])
	ent_7.insert(END, ztext68[0])
	ent_7.insert(END, ztext69[0])
	ent_7.insert(END, ztext70[0])
	forward61(4)
	forward62(4)
	forward63(4)
	forward64(4)
	forward65(4)
	forward66(4)
	forward67(4)
	forward68(4)
	forward69(4)
	forward70(4)
	ent_8.delete(0,END)
	ent_8.insert(END, ztext71[0])
	ent_8.insert(END, ztext72[0])
	ent_8.insert(END, ztext73[0])
	ent_8.insert(END, ztext74[0])
	ent_8.insert(END, ztext75[0])
	ent_8.insert(END, ztext76[0])
	ent_8.insert(END, ztext77[0])
	ent_8.insert(END, ztext78[0])
	ent_8.insert(END, ztext79[0])
	ent_8.insert(END, ztext80[0])
	forward71(4)
	forward72(4)
	forward73(4)
	forward74(4)
	forward75(4)
	forward76(4)
	forward77(4)
	forward78(4)
	forward79(4)
	forward80(4)
	ent_9.delete(0,END)
	ent_9.insert(END, ztext81[0])
	ent_9.insert(END, ztext82[0])
	ent_9.insert(END, ztext83[0])
	ent_9.insert(END, ztext84[0])
	ent_9.insert(END, ztext85[0])
	ent_9.insert(END, ztext86[0])
	ent_9.insert(END, ztext87[0])
	ent_9.insert(END, ztext88[0])
	ent_9.insert(END, ztext89[0])
	ent_9.insert(END, ztext90[0])
	forward81(4)
	forward82(4)
	forward83(4)
	forward84(4)
	forward85(4)
	forward86(4)
	forward87(4)
	forward88(4)
	forward89(4)
	forward90(4)
	ent_10.delete(0,END)
	ent_10.insert(END, ztext91[0])
	ent_10.insert(END, ztext92[0])
	ent_10.insert(END, ztext93[0])
	ent_10.insert(END, ztext94[0])
	ent_10.insert(END, ztext95[0])
	ent_10.insert(END, ztext96[0])
	ent_10.insert(END, ztext97[0])
	ent_10.insert(END, ztext98[0])
	ent_10.insert(END, ztext99[0])
	ent_10.insert(END, ztext100[0])
	forward91(4)
	forward92(4)
	forward93(4)
	forward94(4)
	forward95(4)
	forward96(4)
	forward97(4)
	forward98(4)
	forward99(4)
	forward100(4)

#saving text if wanted(better to copy-paste)
def save_txt():
	#file_text had str before(text_1.get)
	file = filedialog.asksaveasfile(defaultextension='txt')
	file_text = (text_1.get(1.0, END))
	file.write(file_text)
	file.close()

	if file is None:
		return

#window for text____________________________________________________________________________________________________________________________

global text_1
global text_2

new_window1 = Toplevel(root)
new_window1.geometry('1060x3000')
#new_window1.resizable(False, False)
new_window1.title('Code Your Zero (text)')
#new_window1.attributes('-alpha', 0,3)
#create main frame
x = Frame(new_window1)
x.pack(fill = BOTH, expand = 1)
#canvas
can = Canvas(x, bg = 'black')
can.pack(side = LEFT, fill = BOTH, expand = 1)
#scroll to canvas
yscroll = Scrollbar(x, orient =  VERTICAL, command = can.yview)
yscroll.pack(side = RIGHT, fill = Y)


#add new frame to a window in the canvas
can_frame = Frame(can, bg= 'black')
can_frame.pack(fill = BOTH, expand = 1)

#config canvas

can.configure(yscrollcommand=yscroll.set)

can.bind('<Configure>', lambda e: can.configure(scrollregion = can.bbox('all')))

can.create_window((0,0), window = can_frame, anchor = NW)

#another frame inside the canvas

#add text to the above frame
text_1 = Text(can_frame, bg = 'black', fg = 'green', height = 10000, width = 130)
text_1.pack(anchor=NW, fill = BOTH, expand = 1)

#add button and frame
but1_frame = Frame(can)
but1_frame.pack(anchor = S)

#lab_frame = Label(can, text = 'changing text',bg = 'black', fg = 'green')
#lab_frame.pack(anchor = E)


#save button
t2c_but = Button(but1_frame, text = 'save text', bg = 'black', fg = 'green', command = save_txt)
t2c_but.pack()

count = 0
#counter set for check_next func

def check_next():
	text_1.insert(END, ent_1.get())

	text_1.insert(END, ent_2.get())

	text_1.insert(END, ent_3.get())

	text_1.insert(END, ent_4.get())

	text_1.insert(END, ent_5.get())

	text_1.insert(END, ent_6.get())

	text_1.insert(END, ent_7.get())

	text_1.insert(END, ent_8.get())

	text_1.insert(END, ent_9.get())

	text_1.insert(END, ent_10.get())

	#insert and delete from list on right side pane(must click first(message!))________
	x = random.choice(bin_list.get(0, END))
	text_1.insert(END, x)
	#delete x...

	#counter, displays
	global count
	count = count+1
	lab_1.config(text=f'     {count}')

	#change code(temp)
	ztext_change()

but_frame = Frame(root, bg = 'black')
but_frame.grid(row = 2, column = 0, sticky =W)

ent_frame = LabelFrame(root, bg = 'black', text = 'Entries', fg = 'green')
ent_frame.grid(row = 1, column = 0, sticky = NW)

ent_frame1 = Frame(ent_frame, bg = 'black')
ent_frame1.grid(row=0, column=2, rowspan = 10, sticky = NW)

con_frame = Frame(root, bg = 'black')
con_frame.grid(row = 1, column = 2)

bin_frame = Frame(ent_frame1, bg = 'gray')
bin_frame.grid(row=0, column=2, padx = 10, sticky = N)

bin_scr = Scrollbar(bin_frame, bg = 'gray', orient = VERTICAL)
bin_scr.pack(side = RIGHT, fill = Y)

bin_list = Listbox(bin_frame, width = 14, height = 16, bg = 'black', fg = 'green', yscrollcommand = bin_scr.set)
bin_list.pack()

bin_scr.config(command = bin_list.yview)

#insert the text to listbox

for x in sq_8192:
	bin_list.insert(END, x)

tog_frame = Frame(but_frame, bg = 'black')
tog_frame.grid(row=1, column=10, rowspan=10, columnspan =10, sticky = SW)

#button to change label and get grid shapes and colours
cha_but_lab = Button(but_frame, bg = 'black', fg = 'green', text= 'set to text', command = check_next)
cha_but_lab.grid(row = 0, column = 10, sticky = W)

#change labelled messages to show length already used in the given char etc...
lab_0 = Label(but_frame, text = '',bg = 'black', fg = 'green')
lab_0.grid(row=2 , column=10)

#another label configured to display info, len of message
lab_1 = Label(but_frame, text = '',bg = 'black', fg = 'green')
lab_1.grid(row=2 , column=11, sticky = E)

#reset button colors

ran_but_1 = Button(but_frame, text = 'Reset blue', bg = 'black', fg = 'grey', activebackground = 'black', activeforeground= 'green', command = random_entries1)
ran_but_1.grid(row= 0, column = 11)

#repeating problem (ignore 09.04.23)...

#a2z_button = Button(but_frame, text = 'insert a2z', bg = 'black', fg = 'grey', activebackground = 'black', activeforeground= 'green', command = a2z_list_insert_end)
#a2z_button.grid(row= 0, column = 12)

but_green = Button(but_frame, text = 'green', bg = 'black', fg = 'grey', activebackground = 'black', activeforeground= 'green', command = reset_green)
but_green.grid(row= 1, column = 10, sticky= W)

but_yellow = Button(but_frame, text = 'yellow', bg = 'black', fg = 'grey', activebackground = 'black', activeforeground= 'green', command = reset_yellow)
but_yellow.grid(row= 1, column = 11, sticky= W)

but_orange = Button(but_frame, text = 'orange', bg = 'black', fg = 'grey', activebackground = 'black', activeforeground= 'green', command = reset_orange)
but_orange.grid(row= 1, column = 12, sticky= W)

but_red = Button(but_frame, text = 'red', bg = 'black', fg = 'grey', activebackground = 'black', activeforeground= 'green', command = reset_red)
but_red.grid(row= 1, column = 13, sticky= W)

#keyboard buttons x100

t_1 = Button(tog_frame, text = 'a', bg = 'black', fg = 'green', command = t1)
t_1.grid(row = 0, column = 0, padx = 2)

t_2 = Button(tog_frame, text = 'A', bg = 'black', fg = 'green', command = t2)
t_2.grid(row = 0, column = 1, padx = 2)

t_3 = Button(tog_frame, text = 'ä', bg = 'black', fg = 'green',  command = t3)
t_3.grid(row = 0, column = 2, padx = 2)

t_4 = Button(tog_frame, text = 'Ä', bg = 'black', fg = 'green',  command = t4)
t_4.grid(row = 0, column = 3, padx = 2)

t_5 = Button(tog_frame, text = 'b', bg = 'black', fg = 'green',  command = t5)
t_5.grid(row = 0, column = 4, padx = 2)

t_6 = Button(tog_frame, text = 'B', bg = 'black', fg = 'green',  command = t6)
t_6.grid(row = 0, column = 5, padx = 2)

t_7 = Button(tog_frame, text = 'c', bg = 'black', fg = 'green',  command = t7)
t_7.grid(row = 0, column = 6, padx = 2)

t_8 = Button(tog_frame, text = 'C', bg = 'black', fg = 'green',  command = t8)
t_8.grid(row = 0, column = 7, padx = 2)

t_9 = Button(tog_frame, text = 'd', bg = 'black', fg = 'green',  command = t9)
t_9.grid(row = 0, column = 8, padx = 2)

t_10 = Button(tog_frame, text = 'D', bg = 'black', fg = 'green', command = t10)
t_10.grid(row = 0, column = 9, padx = 2)

#10

t_11 = Button(tog_frame, text = 'e', bg = 'black', fg = 'green', command = t11)
t_11.grid(row = 1, column = 0)

t_12 = Button(tog_frame, text = 'E', bg = 'black', fg = 'green', command = t12)
t_12.grid(row = 1, column = 1)

t_13 = Button(tog_frame, text = 'f', bg = 'black', fg = 'green', command = t13)
t_13.grid(row = 1, column = 2)

t_14 = Button(tog_frame, text = 'F', bg = 'black', fg = 'green', command = t14)
t_14.grid(row = 1, column = 3)

t_15 = Button(tog_frame, text = 'g', bg = 'black', fg = 'green', command = t15)
t_15.grid(row = 1, column = 4)

t_16 = Button(tog_frame, text = 'G', bg = 'black', fg = 'green', command = t16)
t_16.grid(row = 1, column = 5)

t_17 = Button(tog_frame, text = 'h', bg = 'black', fg = 'green', command = t17)
t_17.grid(row = 1, column = 6)

t_18 = Button(tog_frame, text = 'H', bg = 'black', fg = 'green', command = t18)
t_18.grid(row = 1, column = 7)

t_19 = Button(tog_frame, text = 'i', bg = 'black', fg = 'green', command = t19)
t_19.grid(row = 1, column = 8)

t_20 = Button(tog_frame, text = 'I', bg = 'black', fg = 'green', command = t20)
t_20.grid(row = 1, column = 9)

#20

t_21 = Button(tog_frame, text = 'j', bg = 'black', fg = 'green', command = t21)
t_21.grid(row = 2, column = 0)

t_22 = Button(tog_frame, text = 'J', bg = 'black', fg = 'green', command = t22)
t_22.grid(row = 2, column = 1)

t_23 = Button(tog_frame, text = 'k', bg = 'black', fg = 'green', command = t23)
t_23.grid(row = 2, column = 2)

t_24 = Button(tog_frame, text = 'K', bg = 'black', fg = 'green', command = t24)
t_24.grid(row = 2, column = 3)

t_25 = Button(tog_frame, text = 'l', bg = 'black', fg = 'green', command = t25)
t_25.grid(row = 2, column = 4)

t_26 = Button(tog_frame, text = 'L', bg = 'black', fg = 'green', command = t26)
t_26.grid(row = 2, column = 5)

t_27 = Button(tog_frame, text = 'm', bg = 'black', fg = 'green', command = t27)
t_27.grid(row = 2, column = 6)

t_28 = Button(tog_frame, text = 'M', bg = 'black', fg = 'green', command = t28)
t_28.grid(row = 2, column = 7)

t_29 = Button(tog_frame, text = 'n', bg = 'black', fg = 'green', command = t29)
t_29.grid(row = 2, column = 8)

t_30 = Button(tog_frame, text = 'N', bg = 'black', fg = 'green', command = t30)
t_30.grid(row = 2, column = 9)

#30

t_31 = Button(tog_frame, text = 'o', bg = 'black', fg = 'green', command = t31)
t_31.grid(row = 3, column = 0)

t_32 = Button(tog_frame, text = 'O', bg = 'black', fg = 'green', command = t32)
t_32.grid(row = 3, column = 1)

t_33 = Button(tog_frame, text = 'ö', bg = 'black', fg = 'green', command = t33)
t_33.grid(row = 3, column = 2)

t_34 = Button(tog_frame, text = 'Ö', bg = 'black', fg = 'green', command = t34)
t_34.grid(row = 3, column = 3)

t_35 = Button(tog_frame, text = 'p', bg = 'black', fg = 'green', command = t35)
t_35.grid(row = 3, column = 4)

t_36 = Button(tog_frame, text = 'P', bg = 'black', fg = 'green', command = t36)
t_36.grid(row = 3, column = 5)

t_37 = Button(tog_frame, text = 'q', bg = 'black', fg = 'green', command = t37)
t_37.grid(row = 3, column = 6)

t_38 = Button(tog_frame, text = 'Q', bg = 'black', fg = 'green', command = t38)
t_38.grid(row = 3, column = 7)

t_39 = Button(tog_frame, text = 'r', bg = 'black', fg = 'green', command = t39)
t_39.grid(row = 3, column = 8)

t_40 = Button(tog_frame, text = 'R', bg = 'black', fg = 'green', command = t40)
t_40.grid(row = 3, column = 9)

#40

t_41 = Button(tog_frame, text = 's', bg = 'black', fg = 'green', command = t41)
t_41.grid(row = 4, column = 0)

t_42 = Button(tog_frame, text = 'S', bg = 'black', fg = 'green', command = t42)
t_42.grid(row = 4, column = 1)

t_43 = Button(tog_frame, text = 't', bg = 'black', fg = 'green', command = t43)
t_43.grid(row = 4, column = 2)

t_44 = Button(tog_frame, text = 'T', bg = 'black', fg = 'green', command = t44)
t_44.grid(row = 4, column = 3)

t_45 = Button(tog_frame, text = 'u', bg = 'black', fg = 'green', command = t45)
t_45.grid(row = 4, column = 4)

t_46 = Button(tog_frame, text = 'U', bg = 'black', fg = 'green', command = t46)
t_46.grid(row = 4, column = 5)

t_47 = Button(tog_frame, text = 'ü', bg = 'black', fg = 'green', command = t47)
t_47.grid(row = 4, column = 6)

t_48 = Button(tog_frame, text = 'Ü', bg = 'black', fg = 'green', command = t48)
t_48.grid(row = 4, column = 7)

t_49 = Button(tog_frame, text = 'v', bg = 'black', fg = 'green', command = t49)
t_49.grid(row = 4, column = 8)

t_50 = Button(tog_frame, text = 'V', bg = 'black', fg = 'green', command = t50)
t_50.grid(row = 4, column = 9)

#50

t_51 = Button(tog_frame, text = 'w', bg = 'black', fg = 'green', command = t51)
t_51.grid(row = 5, column = 0)

t_52 = Button(tog_frame, text = 'W', bg = 'black', fg = 'green', command = t52)
t_52.grid(row = 5, column = 1)

t_53 = Button(tog_frame, text = 'x', bg = 'black', fg = 'green', command = t53)
t_53.grid(row = 5, column = 2)

t_54 = Button(tog_frame, text = 'X', bg = 'black', fg = 'green', command = t54)
t_54.grid(row = 5, column = 3)

t_55 = Button(tog_frame, text = 'y', bg = 'black', fg = 'green', command = t55)
t_55.grid(row = 5, column = 4)

t_56 = Button(tog_frame, text = 'Y', bg = 'black', fg = 'green', command = t56)
t_56.grid(row = 5, column = 5)

t_57 = Button(tog_frame, text = 'z', bg = 'black', fg = 'green', command = t57)
t_57.grid(row = 5, column = 6)

t_58 = Button(tog_frame, text = 'Z', bg = 'black', fg = 'green', command = t58)
t_58.grid(row = 5, column = 7)

t_59 = Button(tog_frame, text = '!', bg = 'black', fg = 'green', command = t59)
t_59.grid(row = 5, column = 8)

t_60 = Button(tog_frame, text = '"', bg = 'black', fg = 'green', command = t60)
t_60.grid(row = 5, column = 9)

#60,'?','ß','backsl.',',',';',':','.','_','-','#','+','*',"''",'>','<','|','~', 'space']


t_61 = Button(tog_frame, text = '$', bg = 'black', fg = 'green', command = t61)
t_61.grid(row = 6, column = 0)

t_62 = Button(tog_frame, text = '%', bg = 'black', fg = 'green', command = t62)
t_62.grid(row = 6, column = 1)

t_63 = Button(tog_frame, text = '&', bg = 'black', fg = 'green', command = t63)
t_63.grid(row = 6, column = 2)

t_64 = Button(tog_frame, text = '/', bg = 'black', fg = 'green', command = t64)
t_64.grid(row = 6, column = 3)

t_65 = Button(tog_frame, text = '{', bg = 'black', fg = 'green', command = t65)
t_65.grid(row = 6, column = 4)

t_66 = Button(tog_frame, text = '(', bg = 'black', fg = 'green', command = t66)
t_66.grid(row = 6, column = 5)

t_67 = Button(tog_frame, text = '[', bg = 'black', fg = 'green', command = t67)
t_67.grid(row = 6, column = 6)

t_68 = Button(tog_frame, text = ')', bg = 'black', fg = 'green', command = t68)
t_68.grid(row = 6, column = 7)

t_69 = Button(tog_frame, text = ']', bg = 'black', fg = 'green', command = t69)
t_69.grid(row = 6, column = 8)

t_70 = Button(tog_frame, text = '=', bg = 'black', fg = 'green', command = t70)
t_70.grid(row = 6, column = 9)

#70'?','ß','backsl.',',',';',':','.','_','-',

t_71 = Button(tog_frame, text = '}', bg = 'black', fg = 'green', command = t71)
t_71.grid(row = 7, column = 0)

t_72 = Button(tog_frame, text = '?', bg = 'black', fg = 'green', command = t72)
t_72.grid(row = 7, column = 1)

t_73 = Button(tog_frame, text = 'ß', bg = 'black', fg = 'green', command = t73)
t_73.grid(row = 7, column = 2)

t_74 = Button(tog_frame, text = '\\', bg = 'black', fg = 'green', command =t74)
t_74.grid(row = 7, column = 3)

t_75 = Button(tog_frame, text = ',', bg = 'black', fg = 'green', command = t75)
t_75.grid(row = 7, column = 4)

t_76 = Button(tog_frame, text = ';', bg = 'black', fg = 'green', command = t76)
t_76.grid(row = 7, column = 5)

t_77 = Button(tog_frame, text = ':', bg = 'black', fg = 'green', command = t77)
t_77.grid(row = 7, column = 6)

t_78 = Button(tog_frame, text = '.', bg = 'black', fg = 'green', command = t78)
t_78.grid(row = 7, column = 7)

t_79 = Button(tog_frame, text = '_', bg = 'black', fg = 'green', command = t79)
t_79.grid(row = 7, column = 8)

t_80 = Button(tog_frame, text = '-', bg = 'black', fg = 'green', command = t80)
t_80.grid(row = 7, column = 9)

#80'#','+','*',"''",'>','<','|','~', 'space']

t_81 = Button(tog_frame, text = '#', bg = 'black', fg = 'green', command = t81)
t_81.grid(row = 8, column = 0)

t_82 = Button(tog_frame, text = '+', bg = 'black', fg = 'green', command = t82)
t_82.grid(row = 8, column = 1)

t_83 = Button(tog_frame, text = '*', bg = 'black', fg = 'green', command = t83)
t_83.grid(row = 8, column = 2)

t_84 = Button(tog_frame, text = "'", bg = 'black', fg = 'green', command = t84)
t_84.grid(row = 8, column = 3)

t_85 = Button(tog_frame, text = '<', bg = 'black', fg = 'green', command = t85)
t_85.grid(row = 8, column = 4)

t_86 = Button(tog_frame, text = '>', bg = 'black', fg = 'green', command = t86)
t_86.grid(row = 8, column = 5)

t_87 = Button(tog_frame, text = '|', bg = 'black', fg = 'green', command = t87)
t_87.grid(row = 8, column = 6)

t_88 = Button(tog_frame, text = '~', bg = 'black', fg = 'green', command = t88)
t_88.grid(row = 8, column = 7)

t_89 = Button(tog_frame, text = 's.b',bg = 'black', fg = 'green',command=t89)
t_89.grid(row = 8, column = 8)

t_90 = Button(tog_frame, text = '0', bg = 'black', fg = 'green', command = t90)
t_90.grid(row = 8, column = 9)

#90

t_91 = Button(tog_frame, text = '1', bg = 'black', fg = 'green', command = t91)
t_91.grid(row = 9, column = 0)

t_92 = Button(tog_frame, text = '2', bg = 'black', fg = 'green', command = t92)
t_92.grid(row = 9, column = 1)

t_93 = Button(tog_frame, text = '3', bg = 'black', fg = 'green', command = t93)
t_93.grid(row = 9, column = 2)

t_94 = Button(tog_frame, text = '4', bg = 'black', fg = 'green', command = t94)
t_94.grid(row = 9, column = 3)

t_95 = Button(tog_frame, text = '5', bg = 'black', fg = 'green', command = t95)
t_95.grid(row = 9, column = 4)

t_96 = Button(tog_frame, text = '6', bg = 'black', fg = 'green', command = t96)
t_96.grid(row = 9, column = 5)

t_97 = Button(tog_frame, text = '7', bg = 'black', fg = 'green', command = t97)
t_97.grid(row = 9, column = 6)

t_98 = Button(tog_frame, text = '8', bg = 'black', fg = 'green', command = t98)
t_98.grid(row = 9, column = 7)

t_99 = Button(tog_frame, text = '9', bg = 'black', fg = 'green', command = t99)
t_99.grid(row = 9, column = 8)

t_100 = Button(tog_frame, text = '10',bg = 'black', fg = 'green', command=t100)
t_100.grid(row = 9, column = 9)

#Entries - for all the code

ent_1 = Entry(ent_frame, bg = 'black', fg = 'green', width = 130)
ent_1.grid(row = 0, column = 0, pady = 4)

ent_2 = Entry(ent_frame, bg = 'black', fg = 'green', width = 130)
ent_2.grid(row = 1, column = 0, pady = 4)

ent_3 = Entry(ent_frame, bg = 'black', fg = 'green', width = 130)
ent_3.grid(row = 2, column = 0, pady = 4)

ent_4 = Entry(ent_frame, bg = 'black', fg = 'green', width = 130)
ent_4.grid(row = 3, column = 0, pady = 4)

ent_5 = Entry(ent_frame, bg = 'black', fg = 'green', width = 130)
ent_5.grid(row = 4, column = 0, pady = 4)

ent_6 = Entry(ent_frame, bg = 'black', fg = 'green', width = 130)
ent_6.grid(row = 5, column = 0, pady = 4)

ent_7 = Entry(ent_frame, bg = 'black', fg = 'green', width = 130)
ent_7.grid(row = 6, column = 0, pady = 4)

ent_8 = Entry(ent_frame, bg = 'black', fg = 'green', width = 130)
ent_8.grid(row = 7, column = 0, pady = 4)

ent_9 = Entry(ent_frame, bg = 'black', fg = 'green', width = 130)
ent_9.grid(row = 8, column = 0, pady = 4)

ent_10 = Entry(ent_frame, bg = 'black', fg = 'green', width = 130)
ent_10.grid(row = 9, column = 0, pady = 2)

#Entry from  lower code

ent_text = Text(but_frame, fg = 'green', bg = 'black', height = 25, width = 52)
ent_text.grid(row =0, column = 21, rowspan = 10, columnspan = 10, sticky = NW)


#Buttons x100

b_1 = Button(but_frame, image = img_0, command = lambda: forward1(0))
b_1.grid(row = 0, column = 0)

b_2 = Button(but_frame, image = img_0, command = lambda: forward2(0))
b_2.grid(row = 0, column = 1)

b_3 = Button(but_frame, image = img_0, command = lambda: forward3(0))
b_3.grid(row = 0, column = 2)

b_4 = Button(but_frame, image = img_0, command = lambda: forward4(0))
b_4.grid(row = 0, column = 3)

b_5 = Button(but_frame, image = img_0, command = lambda: forward5(0))
b_5.grid(row = 0, column = 4)

b_6 = Button(but_frame, image = img_0, command = lambda: forward6(0))
b_6.grid(row = 0, column = 5)

b_7 = Button(but_frame, image = img_0, command = lambda: forward7(0))
b_7.grid(row = 0, column = 6)

b_8 = Button(but_frame, image = img_0, command = lambda: forward8(0))
b_8.grid(row = 0, column = 7)

b_9 = Button(but_frame, image = img_0, command = lambda: forward9(0))
b_9.grid(row = 0, column = 8)

b_10 = Button(but_frame, image = img_0, command = lambda: forward10(0))
b_10.grid(row = 0, column = 9)

#10

b_11 = Button(but_frame, image = img_0, command = lambda: forward11(0))
b_11.grid(row = 1, column = 0)

b_12 = Button(but_frame, image = img_0, command = lambda: forward12(0))
b_12.grid(row = 1, column = 1)

b_13 = Button(but_frame, image = img_0, command = lambda: forward13(0))
b_13.grid(row = 1, column = 2)

b_14 = Button(but_frame, image = img_0, command = lambda: forward14(0))
b_14.grid(row = 1, column = 3)

b_15 = Button(but_frame, image = img_0, command = lambda: forward15(0))
b_15.grid(row = 1, column = 4)

b_16 = Button(but_frame, image = img_0, command = lambda: forward16(0))
b_16.grid(row = 1, column = 5)

b_17 = Button(but_frame, image = img_0, command = lambda: forward17(0))
b_17.grid(row = 1, column = 6)

b_18 = Button(but_frame, image = img_0, command = lambda: forward18(0))
b_18.grid(row = 1, column = 7)

b_19 = Button(but_frame, image = img_0, command = lambda: forward19(0))
b_19.grid(row = 1, column = 8)

b_20 = Button(but_frame, image = img_0, command = lambda: forward20(0))
b_20.grid(row = 1, column = 9)

#20

b_21 = Button(but_frame, image = img_0, command = lambda: forward21(0))
b_21.grid(row = 2, column = 0)

b_22 = Button(but_frame, image = img_0, command = lambda: forward22(0))
b_22.grid(row = 2, column = 1)

b_23 = Button(but_frame, image = img_0, command = lambda: forward23(0))
b_23.grid(row = 2, column = 2)

b_24 = Button(but_frame, image = img_0, command = lambda: forward24(0))
b_24.grid(row = 2, column = 3)

b_25 = Button(but_frame, image = img_0, command = lambda: forward25(0))
b_25.grid(row = 2, column = 4)

b_26 = Button(but_frame, image = img_0, command = lambda: forward26(0))
b_26.grid(row = 2, column = 5)

b_27 = Button(but_frame, image = img_0, command = lambda: forward27(0))
b_27.grid(row = 2, column = 6)

b_28 = Button(but_frame, image = img_0, command = lambda: forward28(0))
b_28.grid(row = 2, column = 7)

b_29 = Button(but_frame, image = img_0, command = lambda: forward29(0))
b_29.grid(row = 2, column = 8)

b_30 = Button(but_frame, image = img_0, command = lambda: forward30(0))
b_30.grid(row = 2, column = 9)

#30

b_31 = Button(but_frame, image = img_0, command = lambda: forward31(0))
b_31.grid(row = 3, column = 0)

b_32 = Button(but_frame, image = img_0, command = lambda: forward32(0))
b_32.grid(row = 3, column = 1)

b_33 = Button(but_frame, image = img_0, command = lambda: forward33(0))
b_33.grid(row = 3, column = 2)

b_34 = Button(but_frame, image = img_0, command = lambda: forward34(0))
b_34.grid(row = 3, column = 3)

b_35 = Button(but_frame, image = img_0, command = lambda: forward35(0))
b_35.grid(row = 3, column = 4)

b_36 = Button(but_frame, image = img_0, command = lambda: forward36(0))
b_36.grid(row = 3, column = 5)

b_37 = Button(but_frame, image = img_0, command = lambda: forward37(0))
b_37.grid(row = 3, column = 6)

b_38 = Button(but_frame, image = img_0, command = lambda: forward38(0))
b_38.grid(row = 3, column = 7)

b_39 = Button(but_frame, image = img_0, command = lambda: forward39(0))
b_39.grid(row = 3, column = 8)

b_40 = Button(but_frame, image = img_0, command = lambda: forward40(0))
b_40.grid(row = 3, column = 9)

#40

b_41 = Button(but_frame, image = img_0, command = lambda: forward41(0))
b_41.grid(row = 4, column = 0)

b_42 = Button(but_frame, image = img_0, command = lambda: forward42(0))
b_42.grid(row = 4, column = 1)

b_43 = Button(but_frame, image = img_0, command = lambda: forward43(0))
b_43.grid(row = 4, column = 2)

b_44 = Button(but_frame, image = img_0, command = lambda: forward44(0))
b_44.grid(row = 4, column = 3)

b_45 = Button(but_frame, image = img_0, command = lambda: forward45(0))
b_45.grid(row = 4, column = 4)

b_46 = Button(but_frame, image = img_0, command = lambda: forward46(0))
b_46.grid(row = 4, column = 5)

b_47 = Button(but_frame, image = img_0, command = lambda: forward47(0))
b_47.grid(row = 4, column = 6)

b_48 = Button(but_frame, image = img_0, command = lambda: forward48(0))
b_48.grid(row = 4, column = 7)

b_49 = Button(but_frame, image = img_0, command = lambda: forward49(0))
b_49.grid(row = 4, column = 8)

b_50 = Button(but_frame, image = img_0, command = lambda: forward50(0))
b_50.grid(row = 4, column = 9)

#50

b_51 = Button(but_frame, image = img_0, command = lambda: forward51(0))
b_51.grid(row = 5, column = 0)

b_52 = Button(but_frame, image = img_0, command = lambda: forward52(0))
b_52.grid(row = 5, column = 1)

b_53 = Button(but_frame, image = img_0, command = lambda: forward53(0))
b_53.grid(row = 5, column = 2)

b_54 = Button(but_frame, image = img_0, command = lambda: forward54(0))
b_54.grid(row = 5, column = 3)

b_55 = Button(but_frame, image = img_0, command = lambda: forward55(0))
b_55.grid(row = 5, column = 4)

b_56 = Button(but_frame, image = img_0, command = lambda: forward56(0))
b_56.grid(row = 5, column = 5)

b_57 = Button(but_frame, image = img_0, command = lambda: forward57(0))
b_57.grid(row = 5, column = 6)

b_58 = Button(but_frame, image = img_0, command = lambda: forward58(0))
b_58.grid(row = 5, column = 7)

b_59 = Button(but_frame, image = img_0, command = lambda: forward59(0))
b_59.grid(row = 5, column = 8)

b_60 = Button(but_frame, image = img_0, command = lambda: forward60(0))
b_60.grid(row = 5, column = 9)

#60

b_61 = Button(but_frame, image = img_0, command = lambda: forward61(0))
b_61.grid(row = 6, column = 0)

b_62 = Button(but_frame, image = img_0, command = lambda: forward62(0))
b_62.grid(row = 6, column = 1)

b_63 = Button(but_frame, image = img_0, command = lambda: forward63(0))
b_63.grid(row = 6, column = 2)

b_64 = Button(but_frame, image = img_0, command = lambda: forward64(0))
b_64.grid(row = 6, column = 3)

b_65 = Button(but_frame, image = img_0, command = lambda: forward65(0))
b_65.grid(row = 6, column = 4)

b_66 = Button(but_frame, image = img_0, command = lambda: forward66(0))
b_66.grid(row = 6, column = 5)

b_67 = Button(but_frame, image = img_0, command = lambda: forward67(0))
b_67.grid(row = 6, column = 6)

b_68 = Button(but_frame, image = img_0, command = lambda: forward68(0))
b_68.grid(row = 6, column = 7)

b_69 = Button(but_frame, image = img_0, command = lambda: forward69(0))
b_69.grid(row = 6, column = 8)

b_70 = Button(but_frame, image = img_0, command = lambda: forward70(0))
b_70.grid(row = 6, column = 9)

#70

b_71 = Button(but_frame, image = img_0, command = lambda: forward71(0))
b_71.grid(row = 7, column = 0)

b_72 = Button(but_frame, image = img_0, command = lambda: forward72(0))
b_72.grid(row = 7, column = 1)

b_73 = Button(but_frame, image = img_0, command = lambda: forward73(0))
b_73.grid(row = 7, column = 2)

b_74 = Button(but_frame, image = img_0, command = lambda: forward74(0))
b_74.grid(row = 7, column = 3)

b_75 = Button(but_frame, image = img_0, command = lambda: forward75(0))
b_75.grid(row = 7, column = 4)

b_76 = Button(but_frame, image = img_0, command = lambda: forward76(0))
b_76.grid(row = 7, column = 5)

b_77 = Button(but_frame, image = img_0, command = lambda: forward77(0))
b_77.grid(row = 7, column = 6)

b_78 = Button(but_frame, image = img_0, command = lambda: forward78(0))
b_78.grid(row = 7, column = 7)

b_79 = Button(but_frame, image = img_0, command = lambda: forward79(0))
b_79.grid(row = 7, column = 8)

b_80 = Button(but_frame, image = img_0, command = lambda: forward80(0))
b_80.grid(row = 7, column = 9)

#80

b_81 = Button(but_frame, image = img_0, command = lambda: forward81(0))
b_81.grid(row = 8, column = 0)

b_82 = Button(but_frame, image = img_0, command = lambda: forward82(0))
b_82.grid(row = 8, column = 1)

b_83 = Button(but_frame, image = img_0, command = lambda: forward83(0))
b_83.grid(row = 8, column = 2)

b_84 = Button(but_frame, image = img_0, command = lambda: forward84(0))
b_84.grid(row = 8, column = 3)

b_85 = Button(but_frame, image = img_0, command = lambda: forward85(0))
b_85.grid(row = 8, column = 4)

b_86 = Button(but_frame, image = img_0, command = lambda: forward86(0))
b_86.grid(row = 8, column = 5)

b_87 = Button(but_frame, image = img_0, command = lambda: forward87(0))
b_87.grid(row = 8, column = 6)

b_88 = Button(but_frame, image = img_0, command = lambda: forward88(0))
b_88.grid(row = 8, column = 7)

b_89 = Button(but_frame, image = img_0, command = lambda: forward89(0))
b_89.grid(row = 8, column = 8)

b_90 = Button(but_frame, image = img_0, command = lambda: forward90(0))
b_90.grid(row = 8, column = 9)

#90

b_91 = Button(but_frame, image = img_0, command = lambda: forward91(0))
b_91.grid(row = 9, column = 0)

b_92 = Button(but_frame, image = img_0, command = lambda: forward92(0))
b_92.grid(row = 9, column = 1)

b_93 = Button(but_frame, image = img_0, command = lambda: forward93(0))
b_93.grid(row = 9, column = 2)

b_94 = Button(but_frame, image = img_0, command = lambda: forward94(0))
b_94.grid(row = 9, column = 3)

b_95 = Button(but_frame, image = img_0, command = lambda: forward95(0))
b_95.grid(row = 9, column = 4)

b_96 = Button(but_frame, image = img_0, command = lambda: forward96(0))
b_96.grid(row = 9, column = 5)

b_97 = Button(but_frame, image = img_0, command = lambda: forward97(0))
b_97.grid(row = 9, column = 6)

b_98 = Button(but_frame, image = img_0, command = lambda: forward98(0))
b_98.grid(row = 9, column = 7)

b_99 = Button(but_frame, image = img_0, command = lambda: forward99(0))
b_99.grid(row = 9, column = 8)

b_100 = Button(but_frame, image = img_0, command = lambda: forward100(0))
b_100.grid(row = 9, column = 9)


root.mainloop()