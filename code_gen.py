'''
CYZ (encode), CYZ (decode) and CYZ (code_gen)
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

#code gen for Code Your Zero
from tkinter import *
from temp import sq_8192
import temp_1

root = Tk()
root.config(bg = 'grey')
root.title('Code Your Zero (code_gen)')
#root.geometry('1300x800')
import random

#user generated code
gen_code = []

#use of random, change later
def mk_random():
    e0.delete(0, END)
    e0.insert(0, str(random.choice(sq_8192)))
    e1.delete(0, END)
    e1.insert(0, str(random.choice(sq_8192)))
    e2.delete(0, END)
    e2.insert(0, str(random.choice(sq_8192)))
    e3.delete(0, END)
    e3.insert(0, str(random.choice(sq_8192)))
    e4.delete(0, END)
    e4.insert(0, str(random.choice(sq_8192)))
    e5.delete(0, END)
    e5.insert(0, str(random.choice(sq_8192)))
    e6.delete(0, END)
    e6.insert(0, str(random.choice(sq_8192)))
    e7.delete(0, END)
    e7.insert(0, str(random.choice(sq_8192)))
    e8.delete(0, END)
    e8.insert(0, str(random.choice(sq_8192)))
    e9.delete(0, END)
    e9.insert(0, str(random.choice(sq_8192)))
    e10.delete(0, END)
    e10.insert(0, str(random.choice(sq_8192)))
#
    e11.delete(0, END)
    e11.insert(0, str(random.choice(sq_8192)))
    e12.delete(0, END)
    e12.insert(0, str(random.choice(sq_8192)))
    e13.delete(0, END)
    e13.insert(0, str(random.choice(sq_8192)))
    e14.delete(0, END)
    e14.insert(0, str(random.choice(sq_8192)))
    e15.delete(0, END)
    e15.insert(0, str(random.choice(sq_8192)))
    e16.delete(0, END)
    e16.insert(0, str(random.choice(sq_8192)))
    e17.delete(0, END)
    e17.insert(0, str(random.choice(sq_8192)))
    e18.delete(0, END)
    e18.insert(0, str(random.choice(sq_8192)))
    e19.delete(0, END)
    e19.insert(0, str(random.choice(sq_8192)))
    e20.delete(0, END)
    e20.insert(0, str(random.choice(sq_8192)))
#
    e21.delete(0, END)
    e21.insert(0, str(random.choice(sq_8192)))
    e22.delete(0, END)
    e22.insert(0, str(random.choice(sq_8192)))
    e23.delete(0, END)
    e23.insert(0, str(random.choice(sq_8192)))
    e24.delete(0, END)
    e24.insert(0, str(random.choice(sq_8192)))
    e25.delete(0, END)
    e25.insert(0, str(random.choice(sq_8192)))
    e26.delete(0, END)
    e26.insert(0, str(random.choice(sq_8192)))
    e27.delete(0, END)
    e27.insert(0, str(random.choice(sq_8192)))
    e28.delete(0, END)
    e28.insert(0, str(random.choice(sq_8192)))
    e29.delete(0, END)
    e29.insert(0, str(random.choice(sq_8192)))
    e30.delete(0, END)
    e30.insert(0, str(random.choice(sq_8192)))
#
    e31.delete(0, END)
    e31.insert(0, str(random.choice(sq_8192)))
    e32.delete(0, END)
    e32.insert(0, str(random.choice(sq_8192)))
    e33.delete(0, END)
    e33.insert(0, str(random.choice(sq_8192)))
    e34.delete(0, END)
    e34.insert(0, str(random.choice(sq_8192)))
    e35.delete(0, END)
    e35.insert(0, str(random.choice(sq_8192)))
    e36.delete(0, END)
    e36.insert(0, str(random.choice(sq_8192)))
    e37.delete(0, END)
    e37.insert(0, str(random.choice(sq_8192)))
    e38.delete(0, END)
    e38.insert(0, str(random.choice(sq_8192)))
    e39.delete(0, END)
    e39.insert(0, str(random.choice(sq_8192)))
    e40.delete(0, END)
    e40.insert(0, str(random.choice(sq_8192)))
#
    e41.delete(0, END)
    e41.insert(0, str(random.choice(sq_8192)))
    e42.delete(0, END)
    e42.insert(0, str(random.choice(sq_8192)))
    e43.delete(0, END)
    e43.insert(0, str(random.choice(sq_8192)))
    e44.delete(0, END)
    e44.insert(0, str(random.choice(sq_8192)))
    e45.delete(0, END)
    e45.insert(0, str(random.choice(sq_8192)))
    e46.delete(0, END)
    e46.insert(0, str(random.choice(sq_8192)))
    e47.delete(0, END)
    e47.insert(0, str(random.choice(sq_8192)))
    e48.delete(0, END)
    e48.insert(0, str(random.choice(sq_8192)))
    e49.delete(0, END)
    e49.insert(0, str(random.choice(sq_8192)))
    e50.delete(0, END)
    e50.insert(0, str(random.choice(sq_8192)))
#
    e51.delete(0, END)
    e51.insert(0, str(random.choice(sq_8192)))
    e52.delete(0, END)
    e52.insert(0, str(random.choice(sq_8192)))
    e53.delete(0, END)
    e53.insert(0, str(random.choice(sq_8192)))
    e54.delete(0, END)
    e54.insert(0, str(random.choice(sq_8192)))
    e55.delete(0, END)
    e55.insert(0, str(random.choice(sq_8192)))
    e56.delete(0, END)
    e56.insert(0, str(random.choice(sq_8192)))
    e57.delete(0, END)
    e57.insert(0, str(random.choice(sq_8192)))
    e58.delete(0, END)
    e58.insert(0, str(random.choice(sq_8192)))
    e59.delete(0, END)
    e59.insert(0, str(random.choice(sq_8192)))
    e60.delete(0, END)
    e60.insert(0, str(random.choice(sq_8192)))
#
    e61.delete(0, END)
    e61.insert(0, str(random.choice(sq_8192)))
    e62.delete(0, END)
    e62.insert(0, str(random.choice(sq_8192)))
    e63.delete(0, END)
    e63.insert(0, str(random.choice(sq_8192)))
    e64.delete(0, END)
    e64.insert(0, str(random.choice(sq_8192)))
    e65.delete(0, END)
    e65.insert(0, str(random.choice(sq_8192)))
    e66.delete(0, END)
    e66.insert(0, str(random.choice(sq_8192)))
    e67.delete(0, END)
    e67.insert(0, str(random.choice(sq_8192)))
    e68.delete(0, END)
    e68.insert(0, str(random.choice(sq_8192)))
    e69.delete(0, END)
    e69.insert(0, str(random.choice(sq_8192)))
    e70.delete(0, END)
    e70.insert(0, str(random.choice(sq_8192)))
#
    e71.delete(0, END)
    e71.insert(0, str(random.choice(sq_8192)))
    e72.delete(0, END)
    e72.insert(0, str(random.choice(sq_8192)))
    e73.delete(0, END)
    e73.insert(0, str(random.choice(sq_8192)))
    e74.delete(0, END)
    e74.insert(0, str(random.choice(sq_8192)))
    e75.delete(0, END)
    e75.insert(0, str(random.choice(sq_8192)))
    e76.delete(0, END)
    e76.insert(0, str(random.choice(sq_8192)))
    e77.delete(0, END)
    e77.insert(0, str(random.choice(sq_8192)))
    e78.delete(0, END)
    e78.insert(0, str(random.choice(sq_8192)))
    e79.delete(0, END)
    e79.insert(0, str(random.choice(sq_8192)))
    e80.delete(0, END)
    e80.insert(0, str(random.choice(sq_8192)))
#
    e81.delete(0, END)
    e81.insert(0, str(random.choice(sq_8192)))
    e82.delete(0, END)
    e82.insert(0, str(random.choice(sq_8192)))
    e83.delete(0, END)
    e83.insert(0, str(random.choice(sq_8192)))
    e84.delete(0, END)
    e84.insert(0, str(random.choice(sq_8192)))
    e85.delete(0, END)
    e85.insert(0, str(random.choice(sq_8192)))
    e86.delete(0, END)
    e86.insert(0, str(random.choice(sq_8192)))
    e87.delete(0, END)
    e87.insert(0, str(random.choice(sq_8192)))
    e88.delete(0, END)
    e88.insert(0, str(random.choice(sq_8192)))
    e89.delete(0, END)
    e89.insert(0, str(random.choice(sq_8192)))
    e90.delete(0, END)
    e90.insert(0, str(random.choice(sq_8192)))
#
    e91.delete(0, END)
    e91.insert(0, str(random.choice(sq_8192)))
    e92.delete(0, END)
    e92.insert(0, str(random.choice(sq_8192)))
    e93.delete(0, END)
    e93.insert(0, str(random.choice(sq_8192)))
    e94.delete(0, END)
    e94.insert(0, str(random.choice(sq_8192)))
    e95.delete(0, END)
    e95.insert(0, str(random.choice(sq_8192)))
    e96.delete(0, END)
    e96.insert(0, str(random.choice(sq_8192)))
    e97.delete(0, END)
    e97.insert(0, str(random.choice(sq_8192)))
    e98.delete(0, END)
    e98.insert(0, str(random.choice(sq_8192)))
    e99.delete(0, END)
    e99.insert(0, str(random.choice(sq_8192)))
#
    ee0.delete(0, END)
    ee0.insert(0, str(random.choice(sq_8192)))
    ee1.delete(0, END)
    ee1.insert(0, str(random.choice(sq_8192)))
    ee2.delete(0, END)
    ee2.insert(0, str(random.choice(sq_8192)))
    ee3.delete(0, END)
    ee3.insert(0, str(random.choice(sq_8192)))
    ee4.delete(0, END)
    ee4.insert(0, str(random.choice(sq_8192)))
    ee5.delete(0, END)
    ee5.insert(0, str(random.choice(sq_8192)))
    ee6.delete(0, END)
    ee6.insert(0, str(random.choice(sq_8192)))
    ee7.delete(0, END)
    ee7.insert(0, str(random.choice(sq_8192)))
    ee8.delete(0, END)
    ee8.insert(0, str(random.choice(sq_8192)))
    ee9.delete(0, END)
    ee9.insert(0, str(random.choice(sq_8192)))
    ee10.delete(0, END)
    ee10.insert(0, str(random.choice(sq_8192)))
#
    ee11.delete(0, END)
    ee11.insert(0, str(random.choice(sq_8192)))
    ee12.delete(0, END)
    ee12.insert(0, str(random.choice(sq_8192)))
    ee13.delete(0, END)
    ee13.insert(0, str(random.choice(sq_8192)))
    ee14.delete(0, END)
    ee14.insert(0, str(random.choice(sq_8192)))
    ee15.delete(0, END)
    ee15.insert(0, str(random.choice(sq_8192)))
    ee16.delete(0, END)
    ee16.insert(0, str(random.choice(sq_8192)))
    ee17.delete(0, END)
    ee17.insert(0, str(random.choice(sq_8192)))
    ee18.delete(0, END)
    ee18.insert(0, str(random.choice(sq_8192)))
    ee19.delete(0, END)
    ee19.insert(0, str(random.choice(sq_8192)))
    ee20.delete(0, END)
    ee20.insert(0, str(random.choice(sq_8192)))
#
    ee21.delete(0, END)
    ee21.insert(0, str(random.choice(sq_8192)))
    ee22.delete(0, END)
    ee22.insert(0, str(random.choice(sq_8192)))
    ee23.delete(0, END)
    ee23.insert(0, str(random.choice(sq_8192)))
    ee24.delete(0, END)
    ee24.insert(0, str(random.choice(sq_8192)))
    ee25.delete(0, END)
    ee25.insert(0, str(random.choice(sq_8192)))
    ee26.delete(0, END)
    ee26.insert(0, str(random.choice(sq_8192)))
    ee27.delete(0, END)
    ee27.insert(0, str(random.choice(sq_8192)))
    ee28.delete(0, END)
    ee28.insert(0, str(random.choice(sq_8192)))
    ee29.delete(0, END)
    ee29.insert(0, str(random.choice(sq_8192)))
    ee30.delete(0, END)
    ee30.insert(0, str(random.choice(sq_8192)))
#
    ee31.delete(0, END)
    ee31.insert(0, str(random.choice(sq_8192)))
    ee32.delete(0, END)
    ee32.insert(0, str(random.choice(sq_8192)))
    ee33.delete(0, END)
    ee33.insert(0, str(random.choice(sq_8192)))
    ee34.delete(0, END)
    ee34.insert(0, str(random.choice(sq_8192)))
    ee35.delete(0, END)
    ee35.insert(0, str(random.choice(sq_8192)))
    ee36.delete(0, END)
    ee36.insert(0, str(random.choice(sq_8192)))
    ee37.delete(0, END)
    ee37.insert(0, str(random.choice(sq_8192)))
    ee38.delete(0, END)
    ee38.insert(0, str(random.choice(sq_8192)))
    ee39.delete(0, END)
    ee39.insert(0, str(random.choice(sq_8192)))
    ee40.delete(0, END)
    ee40.insert(0, str(random.choice(sq_8192)))
#
    ee41.delete(0, END)
    ee41.insert(0, str(random.choice(sq_8192)))
    ee42.delete(0, END)
    ee42.insert(0, str(random.choice(sq_8192)))
    ee43.delete(0, END)
    ee43.insert(0, str(random.choice(sq_8192)))
    ee44.delete(0, END)
    ee44.insert(0, str(random.choice(sq_8192)))
    ee45.delete(0, END)
    ee45.insert(0, str(random.choice(sq_8192)))
    ee46.delete(0, END)
    ee46.insert(0, str(random.choice(sq_8192)))
    ee47.delete(0, END)
    ee47.insert(0, str(random.choice(sq_8192)))
    ee48.delete(0, END)
    ee48.insert(0, str(random.choice(sq_8192)))
    ee49.delete(0, END)
    ee49.insert(0, str(random.choice(sq_8192)))
    ee50.delete(0, END)
    ee50.insert(0, str(random.choice(sq_8192)))
#
    ee51.delete(0, END)
    ee51.insert(0, str(random.choice(sq_8192)))
    ee52.delete(0, END)
    ee52.insert(0, str(random.choice(sq_8192)))
    ee53.delete(0, END)
    ee53.insert(0, str(random.choice(sq_8192)))
    ee54.delete(0, END)
    ee54.insert(0, str(random.choice(sq_8192)))
    ee55.delete(0, END)
    ee55.insert(0, str(random.choice(sq_8192)))
    ee56.delete(0, END)
    ee56.insert(0, str(random.choice(sq_8192)))
    ee57.delete(0, END)
    ee57.insert(0, str(random.choice(sq_8192)))
    ee58.delete(0, END)
    ee58.insert(0, str(random.choice(sq_8192)))
    ee59.delete(0, END)
    ee59.insert(0, str(random.choice(sq_8192)))
    ee60.delete(0, END)
    ee60.insert(0, str(random.choice(sq_8192)))
#
    ee61.delete(0, END)
    ee61.insert(0, str(random.choice(sq_8192)))
    ee62.delete(0, END)
    ee62.insert(0, str(random.choice(sq_8192)))
    ee63.delete(0, END)
    ee63.insert(0, str(random.choice(sq_8192)))
    ee64.delete(0, END)
    ee64.insert(0, str(random.choice(sq_8192)))
    ee65.delete(0, END)
    ee65.insert(0, str(random.choice(sq_8192)))
    ee66.delete(0, END)
    ee66.insert(0, str(random.choice(sq_8192)))
    ee67.delete(0, END)
    ee67.insert(0, str(random.choice(sq_8192)))
    ee68.delete(0, END)
    ee68.insert(0, str(random.choice(sq_8192)))
    ee69.delete(0, END)
    ee69.insert(0, str(random.choice(sq_8192)))
    ee70.delete(0, END)
    ee70.insert(0, str(random.choice(sq_8192)))
#
    ee71.delete(0, END)
    ee71.insert(0, str(random.choice(sq_8192)))
    ee72.delete(0, END)
    ee72.insert(0, str(random.choice(sq_8192)))
    ee73.delete(0, END)
    ee73.insert(0, str(random.choice(sq_8192)))
    ee74.delete(0, END)
    ee74.insert(0, str(random.choice(sq_8192)))
    ee75.delete(0, END)
    ee75.insert(0, str(random.choice(sq_8192)))
    ee76.delete(0, END)
    ee76.insert(0, str(random.choice(sq_8192)))
    ee77.delete(0, END)
    ee77.insert(0, str(random.choice(sq_8192)))
    ee78.delete(0, END)
    ee78.insert(0, str(random.choice(sq_8192)))
    ee79.delete(0, END)
    ee79.insert(0, str(random.choice(sq_8192)))
    ee80.delete(0, END)
    ee80.insert(0, str(random.choice(sq_8192)))
#
    ee81.delete(0, END)
    ee81.insert(0, str(random.choice(sq_8192)))
    ee82.delete(0, END)
    ee82.insert(0, str(random.choice(sq_8192)))
    ee83.delete(0, END)
    ee83.insert(0, str(random.choice(sq_8192)))
    ee84.delete(0, END)
    ee84.insert(0, str(random.choice(sq_8192)))
    ee85.delete(0, END)
    ee85.insert(0, str(random.choice(sq_8192)))
    ee86.delete(0, END)
    ee86.insert(0, str(random.choice(sq_8192)))
    ee87.delete(0, END)
    ee87.insert(0, str(random.choice(sq_8192)))
    ee88.delete(0, END)
    ee88.insert(0, str(random.choice(sq_8192)))
    ee89.delete(0, END)
    ee89.insert(0, str(random.choice(sq_8192)))
    ee90.delete(0, END)
    ee90.insert(0, str(random.choice(sq_8192)))
#
    ee91.delete(0, END)
    ee91.insert(0, str(random.choice(sq_8192)))
    ee92.delete(0, END)
    ee92.insert(0, str(random.choice(sq_8192)))
    ee93.delete(0, END)
    ee93.insert(0, str(random.choice(sq_8192)))
    ee94.delete(0, END)
    ee94.insert(0, str(random.choice(sq_8192)))
    ee95.delete(0, END)
    ee95.insert(0, str(random.choice(sq_8192)))
    ee96.delete(0, END)
    ee96.insert(0, str(random.choice(sq_8192)))
    ee97.delete(0, END)
    ee97.insert(0, str(random.choice(sq_8192)))
    ee98.delete(0, END)
    ee98.insert(0, str(random.choice(sq_8192)))
    ee99.delete(0, END)
    ee99.insert(0, str(random.choice(sq_8192)))
#
    eee0.delete(0, END)
    eee0.insert(0, str(random.choice(sq_8192)))
    eee1.delete(0, END)
    eee1.insert(0, str(random.choice(sq_8192)))
    eee2.delete(0, END)
    eee2.insert(0, str(random.choice(sq_8192)))
    eee3.delete(0, END)
    eee3.insert(0, str(random.choice(sq_8192)))
    eee4.delete(0, END)
    eee4.insert(0, str(random.choice(sq_8192)))
    eee5.delete(0, END)
    eee5.insert(0, str(random.choice(sq_8192)))
    eee6.delete(0, END)
    eee6.insert(0, str(random.choice(sq_8192)))
    eee7.delete(0, END)
    eee7.insert(0, str(random.choice(sq_8192)))
    eee8.delete(0, END)
    eee8.insert(0, str(random.choice(sq_8192)))
    eee9.delete(0, END)
    eee9.insert(0, str(random.choice(sq_8192)))
    eee10.delete(0, END)
    eee10.insert(0, str(random.choice(sq_8192)))
#
    eee11.delete(0, END)
    eee11.insert(0, str(random.choice(sq_8192)))
    eee12.delete(0, END)
    eee12.insert(0, str(random.choice(sq_8192)))
    eee13.delete(0, END)
    eee13.insert(0, str(random.choice(sq_8192)))
    eee14.delete(0, END)
    eee14.insert(0, str(random.choice(sq_8192)))
    eee15.delete(0, END)
    eee15.insert(0, str(random.choice(sq_8192)))
    eee16.delete(0, END)
    eee16.insert(0, str(random.choice(sq_8192)))
    eee17.delete(0, END)
    eee17.insert(0, str(random.choice(sq_8192)))
    eee18.delete(0, END)
    eee18.insert(0, str(random.choice(sq_8192)))
    eee19.delete(0, END)
    eee19.insert(0, str(random.choice(sq_8192)))
    eee20.delete(0, END)
    eee20.insert(0, str(random.choice(sq_8192)))
#
    eee21.delete(0, END)
    eee21.insert(0, str(random.choice(sq_8192)))
    eee22.delete(0, END)
    eee22.insert(0, str(random.choice(sq_8192)))
    eee23.delete(0, END)
    eee23.insert(0, str(random.choice(sq_8192)))
    eee24.delete(0, END)
    eee24.insert(0, str(random.choice(sq_8192)))
    eee25.delete(0, END)
    eee25.insert(0, str(random.choice(sq_8192)))
    eee26.delete(0, END)
    eee26.insert(0, str(random.choice(sq_8192)))
    eee27.delete(0, END)
    eee27.insert(0, str(random.choice(sq_8192)))
    eee28.delete(0, END)
    eee28.insert(0, str(random.choice(sq_8192)))
    eee29.delete(0, END)
    eee29.insert(0, str(random.choice(sq_8192)))
    eee30.delete(0, END)
    eee30.insert(0, str(random.choice(sq_8192)))
#
    eee31.delete(0, END)
    eee31.insert(0, str(random.choice(sq_8192)))
    eee32.delete(0, END)
    eee32.insert(0, str(random.choice(sq_8192)))
    eee33.delete(0, END)
    eee33.insert(0, str(random.choice(sq_8192)))
    eee34.delete(0, END)
    eee34.insert(0, str(random.choice(sq_8192)))
    eee35.delete(0, END)
    eee35.insert(0, str(random.choice(sq_8192)))
    eee36.delete(0, END)
    eee36.insert(0, str(random.choice(sq_8192)))
    eee37.delete(0, END)
    eee37.insert(0, str(random.choice(sq_8192)))
    eee38.delete(0, END)
    eee38.insert(0, str(random.choice(sq_8192)))
    eee39.delete(0, END)
    eee39.insert(0, str(random.choice(sq_8192)))
    eee40.delete(0, END)
    eee40.insert(0, str(random.choice(sq_8192)))
#
    eee41.delete(0, END)
    eee41.insert(0, str(random.choice(sq_8192)))
    eee42.delete(0, END)
    eee42.insert(0, str(random.choice(sq_8192)))
    eee43.delete(0, END)
    eee43.insert(0, str(random.choice(sq_8192)))
    eee44.delete(0, END)
    eee44.insert(0, str(random.choice(sq_8192)))
    eee45.delete(0, END)
    eee45.insert(0, str(random.choice(sq_8192)))
    eee46.delete(0, END)
    eee46.insert(0, str(random.choice(sq_8192)))
    eee47.delete(0, END)
    eee47.insert(0, str(random.choice(sq_8192)))
    eee48.delete(0, END)
    eee48.insert(0, str(random.choice(sq_8192)))
    eee49.delete(0, END)
    eee49.insert(0, str(random.choice(sq_8192)))
    eee50.delete(0, END)
    eee50.insert(0, str(random.choice(sq_8192)))
#
    eee51.delete(0, END)
    eee51.insert(0, str(random.choice(sq_8192)))
    eee52.delete(0, END)
    eee52.insert(0, str(random.choice(sq_8192)))
    eee53.delete(0, END)
    eee53.insert(0, str(random.choice(sq_8192)))
    eee54.delete(0, END)
    eee54.insert(0, str(random.choice(sq_8192)))
    eee55.delete(0, END)
    eee55.insert(0, str(random.choice(sq_8192)))
    eee56.delete(0, END)
    eee56.insert(0, str(random.choice(sq_8192)))
    eee57.delete(0, END)
    eee57.insert(0, str(random.choice(sq_8192)))
    eee58.delete(0, END)
    eee58.insert(0, str(random.choice(sq_8192)))
    eee59.delete(0, END)
    eee59.insert(0, str(random.choice(sq_8192)))
    eee60.delete(0, END)
    eee60.insert(0, str(random.choice(sq_8192)))
#
    eee61.delete(0, END)
    eee61.insert(0, str(random.choice(sq_8192)))
    eee62.delete(0, END)
    eee62.insert(0, str(random.choice(sq_8192)))
    eee63.delete(0, END)
    eee63.insert(0, str(random.choice(sq_8192)))
    eee64.delete(0, END)
    eee64.insert(0, str(random.choice(sq_8192)))
    eee65.delete(0, END)
    eee65.insert(0, str(random.choice(sq_8192)))
    eee66.delete(0, END)
    eee66.insert(0, str(random.choice(sq_8192)))
    eee67.delete(0, END)
    eee67.insert(0, str(random.choice(sq_8192)))
    eee68.delete(0, END)
    eee68.insert(0, str(random.choice(sq_8192)))
    eee69.delete(0, END)
    eee69.insert(0, str(random.choice(sq_8192)))
    eee70.delete(0, END)
    eee70.insert(0, str(random.choice(sq_8192)))
#
    eee71.delete(0, END)
    eee71.insert(0, str(random.choice(sq_8192)))
    eee72.delete(0, END)
    eee72.insert(0, str(random.choice(sq_8192)))
    eee73.delete(0, END)
    eee73.insert(0, str(random.choice(sq_8192)))
    eee74.delete(0, END)
    eee74.insert(0, str(random.choice(sq_8192)))
    eee75.delete(0, END)
    eee75.insert(0, str(random.choice(sq_8192)))
    eee76.delete(0, END)
    eee76.insert(0, str(random.choice(sq_8192)))
    eee77.delete(0, END)
    eee77.insert(0, str(random.choice(sq_8192)))
    eee78.delete(0, END)
    eee78.insert(0, str(random.choice(sq_8192)))
    eee79.delete(0, END)
    eee79.insert(0, str(random.choice(sq_8192)))
    eee80.delete(0, END)
    eee80.insert(0, str(random.choice(sq_8192)))
#
    eee81.delete(0, END)
    eee81.insert(0, str(random.choice(sq_8192)))
    eee82.delete(0, END)
    eee82.insert(0, str(random.choice(sq_8192)))
    eee83.delete(0, END)
    eee83.insert(0, str(random.choice(sq_8192)))
    eee84.delete(0, END)
    eee84.insert(0, str(random.choice(sq_8192)))
    eee85.delete(0, END)
    eee85.insert(0, str(random.choice(sq_8192)))
    eee86.delete(0, END)
    eee86.insert(0, str(random.choice(sq_8192)))
    eee87.delete(0, END)
    eee87.insert(0, str(random.choice(sq_8192)))
    eee88.delete(0, END)
    eee88.insert(0, str(random.choice(sq_8192)))
    eee89.delete(0, END)
    eee89.insert(0, str(random.choice(sq_8192)))
    eee90.delete(0, END)
    eee90.insert(0, str(random.choice(sq_8192)))
#
    eee91.delete(0, END)
    eee91.insert(0, str(random.choice(sq_8192)))
    eee92.delete(0, END)
    eee92.insert(0, str(random.choice(sq_8192)))
    eee93.delete(0, END)
    eee93.insert(0, str(random.choice(sq_8192)))
    eee94.delete(0, END)
    eee94.insert(0, str(random.choice(sq_8192)))
    eee95.delete(0, END)
    eee95.insert(0, str(random.choice(sq_8192)))
    eee96.delete(0, END)
    eee96.insert(0, str(random.choice(sq_8192)))
    eee97.delete(0, END)
    eee97.insert(0, str(random.choice(sq_8192)))
    eee98.delete(0, END)
    eee98.insert(0, str(random.choice(sq_8192)))
    eee99.delete(0, END)
    eee99.insert(0, str(random.choice(sq_8192)))
#70
    eeee0.delete(0, END)
    eeee0.insert(0, str(random.choice(sq_8192)))
    eeee1.delete(0, END)
    eeee1.insert(0, str(random.choice(sq_8192)))
    eeee2.delete(0, END)
    eeee2.insert(0, str(random.choice(sq_8192)))
    eeee3.delete(0, END)
    eeee3.insert(0, str(random.choice(sq_8192)))
    eeee4.delete(0, END)
    eeee4.insert(0, str(random.choice(sq_8192)))
    eeee5.delete(0, END)
    eeee5.insert(0, str(random.choice(sq_8192)))
    eeee6.delete(0, END)
    eeee6.insert(0, str(random.choice(sq_8192)))
    eeee7.delete(0, END)
    eeee7.insert(0, str(random.choice(sq_8192)))
    eeee8.delete(0, END)
    eeee8.insert(0, str(random.choice(sq_8192)))
    eeee9.delete(0, END)
    eeee9.insert(0, str(random.choice(sq_8192)))
    eeee10.delete(0, END)
    eeee10.insert(0, str(random.choice(sq_8192)))
#
    eeee11.delete(0, END)
    eeee11.insert(0, str(random.choice(sq_8192)))
    eeee12.delete(0, END)
    eeee12.insert(0, str(random.choice(sq_8192)))
    eeee13.delete(0, END)
    eeee13.insert(0, str(random.choice(sq_8192)))
    eeee14.delete(0, END)
    eeee14.insert(0, str(random.choice(sq_8192)))
    eeee15.delete(0, END)
    eeee15.insert(0, str(random.choice(sq_8192)))
    eeee16.delete(0, END)
    eeee16.insert(0, str(random.choice(sq_8192)))
    eeee17.delete(0, END)
    eeee17.insert(0, str(random.choice(sq_8192)))
    eeee18.delete(0, END)
    eeee18.insert(0, str(random.choice(sq_8192)))
    eeee19.delete(0, END)
    eeee19.insert(0, str(random.choice(sq_8192)))
    eeee20.delete(0, END)
    eeee20.insert(0, str(random.choice(sq_8192)))
#
    eeee21.delete(0, END)
    eeee21.insert(0, str(random.choice(sq_8192)))
    eeee22.delete(0, END)
    eeee22.insert(0, str(random.choice(sq_8192)))
    eeee23.delete(0, END)
    eeee23.insert(0, str(random.choice(sq_8192)))
    eeee24.delete(0, END)
    eeee24.insert(0, str(random.choice(sq_8192)))
    eeee25.delete(0, END)
    eeee25.insert(0, str(random.choice(sq_8192)))
    eeee26.delete(0, END)
    eeee26.insert(0, str(random.choice(sq_8192)))
    eeee27.delete(0, END)
    eeee27.insert(0, str(random.choice(sq_8192)))
    eeee28.delete(0, END)
    eeee28.insert(0, str(random.choice(sq_8192)))
    eeee29.delete(0, END)
    eeee29.insert(0, str(random.choice(sq_8192)))
    eeee30.delete(0, END)
    eeee30.insert(0, str(random.choice(sq_8192)))
#
    eeee31.delete(0, END)
    eeee31.insert(0, str(random.choice(sq_8192)))
    eeee32.delete(0, END)
    eeee32.insert(0, str(random.choice(sq_8192)))
    eeee33.delete(0, END)
    eeee33.insert(0, str(random.choice(sq_8192)))
    eeee34.delete(0, END)
    eeee34.insert(0, str(random.choice(sq_8192)))
    eeee35.delete(0, END)
    eeee35.insert(0, str(random.choice(sq_8192)))
    eeee36.delete(0, END)
    eeee36.insert(0, str(random.choice(sq_8192)))
    eeee37.delete(0, END)
    eeee37.insert(0, str(random.choice(sq_8192)))
    eeee38.delete(0, END)
    eeee38.insert(0, str(random.choice(sq_8192)))
    eeee39.delete(0, END)
    eeee39.insert(0, str(random.choice(sq_8192)))
    eeee40.delete(0, END)
    eeee40.insert(0, str(random.choice(sq_8192)))
#
    eeee41.delete(0, END)
    eeee41.insert(0, str(random.choice(sq_8192)))
    eeee42.delete(0, END)
    eeee42.insert(0, str(random.choice(sq_8192)))
    eeee43.delete(0, END)
    eeee43.insert(0, str(random.choice(sq_8192)))
    eeee44.delete(0, END)
    eeee44.insert(0, str(random.choice(sq_8192)))
    eeee45.delete(0, END)
    eeee45.insert(0, str(random.choice(sq_8192)))
    eeee46.delete(0, END)
    eeee46.insert(0, str(random.choice(sq_8192)))
    eeee47.delete(0, END)
    eeee47.insert(0, str(random.choice(sq_8192)))
    eeee48.delete(0, END)
    eeee48.insert(0, str(random.choice(sq_8192)))
    eeee49.delete(0, END)
    eeee49.insert(0, str(random.choice(sq_8192)))
    eeee50.delete(0, END)
    eeee50.insert(0, str(random.choice(sq_8192)))
#
    eeee51.delete(0, END)
    eeee51.insert(0, str(random.choice(sq_8192)))
    eeee52.delete(0, END)
    eeee52.insert(0, str(random.choice(sq_8192)))
    eeee53.delete(0, END)
    eeee53.insert(0, str(random.choice(sq_8192)))
    eeee54.delete(0, END)
    eeee54.insert(0, str(random.choice(sq_8192)))
    eeee55.delete(0, END)
    eeee55.insert(0, str(random.choice(sq_8192)))
    eeee56.delete(0, END)
    eeee56.insert(0, str(random.choice(sq_8192)))
    eeee57.delete(0, END)
    eeee57.insert(0, str(random.choice(sq_8192)))
    eeee58.delete(0, END)
    eeee58.insert(0, str(random.choice(sq_8192)))
    eeee59.delete(0, END)
    eeee59.insert(0, str(random.choice(sq_8192)))
    eeee60.delete(0, END)
    eeee60.insert(0, str(random.choice(sq_8192)))
#
    eeee61.delete(0, END)
    eeee61.insert(0, str(random.choice(sq_8192)))
    eeee62.delete(0, END)
    eeee62.insert(0, str(random.choice(sq_8192)))
    eeee63.delete(0, END)
    eeee63.insert(0, str(random.choice(sq_8192)))
    eeee64.delete(0, END)
    eeee64.insert(0, str(random.choice(sq_8192)))
    eeee65.delete(0, END)
    eeee65.insert(0, str(random.choice(sq_8192)))
    eeee66.delete(0, END)
    eeee66.insert(0, str(random.choice(sq_8192)))
    eeee67.delete(0, END)
    eeee67.insert(0, str(random.choice(sq_8192)))
    eeee68.delete(0, END)
    eeee68.insert(0, str(random.choice(sq_8192)))
    eeee69.delete(0, END)
    eeee69.insert(0, str(random.choice(sq_8192)))
#60mid
    eeeee0.delete(0, END)
    eeeee0.insert(0, str(random.choice(sq_8192)))
    eeeee1.delete(0, END)
    eeeee1.insert(0, str(random.choice(sq_8192)))
    eeeee2.delete(0, END)
    eeeee2.insert(0, str(random.choice(sq_8192)))
    eeeee3.delete(0, END)
    eeeee3.insert(0, str(random.choice(sq_8192)))
    eeeee4.delete(0, END)
    eeeee4.insert(0, str(random.choice(sq_8192)))
    eeeee5.delete(0, END)
    eeeee5.insert(0, str(random.choice(sq_8192)))
    eeeee6.delete(0, END)
    eeeee6.insert(0, str(random.choice(sq_8192)))
    eeeee7.delete(0, END)
    eeeee7.insert(0, str(random.choice(sq_8192)))
    eeeee8.delete(0, END)
    eeeee8.insert(0, str(random.choice(sq_8192)))
    eeeee9.delete(0, END)
    eeeee9.insert(0, str(random.choice(sq_8192)))
    eeeee10.delete(0, END)
    eeeee10.insert(0, str(random.choice(sq_8192)))
#
    eeeee11.delete(0, END)
    eeeee11.insert(0, str(random.choice(sq_8192)))
    eeeee12.delete(0, END)
    eeeee12.insert(0, str(random.choice(sq_8192)))
    eeeee13.delete(0, END)
    eeeee13.insert(0, str(random.choice(sq_8192)))
    eeeee14.delete(0, END)
    eeeee14.insert(0, str(random.choice(sq_8192)))
    eeeee15.delete(0, END)
    eeeee15.insert(0, str(random.choice(sq_8192)))
    eeeee16.delete(0, END)
    eeeee16.insert(0, str(random.choice(sq_8192)))
    eeeee17.delete(0, END)
    eeeee17.insert(0, str(random.choice(sq_8192)))
    eeeee18.delete(0, END)
    eeeee18.insert(0, str(random.choice(sq_8192)))
    eeeee19.delete(0, END)
    eeeee19.insert(0, str(random.choice(sq_8192)))
    eeeee20.delete(0, END)
    eeeee20.insert(0, str(random.choice(sq_8192)))
#
    eeeee21.delete(0, END)
    eeeee21.insert(0, str(random.choice(sq_8192)))
    eeeee22.delete(0, END)
    eeeee22.insert(0, str(random.choice(sq_8192)))
    eeeee23.delete(0, END)
    eeeee23.insert(0, str(random.choice(sq_8192)))
    eeeee24.delete(0, END)
    eeeee24.insert(0, str(random.choice(sq_8192)))
    eeeee25.delete(0, END)
    eeeee25.insert(0, str(random.choice(sq_8192)))
    eeeee26.delete(0, END)
    eeeee26.insert(0, str(random.choice(sq_8192)))
    eeeee27.delete(0, END)
    eeeee27.insert(0, str(random.choice(sq_8192)))
    eeeee28.delete(0, END)
    eeeee28.insert(0, str(random.choice(sq_8192)))
    eeeee29.delete(0, END)
    eeeee29.insert(0, str(random.choice(sq_8192)))
    eeeee30.delete(0, END)
    eeeee30.insert(0, str(random.choice(sq_8192)))
#
    eeeee31.delete(0, END)
    eeeee31.insert(0, str(random.choice(sq_8192)))
    eeeee32.delete(0, END)
    eeeee32.insert(0, str(random.choice(sq_8192)))
    eeeee33.delete(0, END)
    eeeee33.insert(0, str(random.choice(sq_8192)))
    eeeee34.delete(0, END)
    eeeee34.insert(0, str(random.choice(sq_8192)))
    eeeee35.delete(0, END)
    eeeee35.insert(0, str(random.choice(sq_8192)))
    eeeee36.delete(0, END)
    eeeee36.insert(0, str(random.choice(sq_8192)))
    eeeee37.delete(0, END)
    eeeee37.insert(0, str(random.choice(sq_8192)))
    eeeee38.delete(0, END)
    eeeee38.insert(0, str(random.choice(sq_8192)))
    eeeee39.delete(0, END)
    eeeee39.insert(0, str(random.choice(sq_8192)))
    eeeee40.delete(0, END)
    eeeee40.insert(0, str(random.choice(sq_8192)))
#
    eeeee41.delete(0, END)
    eeeee41.insert(0, str(random.choice(sq_8192)))
    eeeee42.delete(0, END)
    eeeee42.insert(0, str(random.choice(sq_8192)))
    eeeee43.delete(0, END)
    eeeee43.insert(0, str(random.choice(sq_8192)))
    eeeee44.delete(0, END)
    eeeee44.insert(0, str(random.choice(sq_8192)))
    eeeee45.delete(0, END)
    eeeee45.insert(0, str(random.choice(sq_8192)))
    eeeee46.delete(0, END)
    eeeee46.insert(0, str(random.choice(sq_8192)))
    eeeee47.delete(0, END)
    eeeee47.insert(0, str(random.choice(sq_8192)))
    eeeee48.delete(0, END)
    eeeee48.insert(0, str(random.choice(sq_8192)))
    eeeee49.delete(0, END)
    eeeee49.insert(0, str(random.choice(sq_8192)))
    eeeee50.delete(0, END)
    eeeee50.insert(0, str(random.choice(sq_8192)))
#
    eeeee51.delete(0, END)
    eeeee51.insert(0, str(random.choice(sq_8192)))
    eeeee52.delete(0, END)
    eeeee52.insert(0, str(random.choice(sq_8192)))
    eeeee53.delete(0, END)
    eeeee53.insert(0, str(random.choice(sq_8192)))
    eeeee54.delete(0, END)
    eeeee54.insert(0, str(random.choice(sq_8192)))
    eeeee55.delete(0, END)
    eeeee55.insert(0, str(random.choice(sq_8192)))
    eeeee56.delete(0, END)
    eeeee56.insert(0, str(random.choice(sq_8192)))
    eeeee57.delete(0, END)
    eeeee57.insert(0, str(random.choice(sq_8192)))
    eeeee58.delete(0, END)
    eeeee58.insert(0, str(random.choice(sq_8192)))
    eeeee59.delete(0, END)
    eeeee59.insert(0, str(random.choice(sq_8192)))
#70end
    eeeeee0.delete(0, END)
    eeeeee0.insert(0, str(random.choice(sq_8192)))
    eeeeee1.delete(0, END)
    eeeeee1.insert(0, str(random.choice(sq_8192)))
    eeeeee2.delete(0, END)
    eeeeee2.insert(0, str(random.choice(sq_8192)))
    eeeeee3.delete(0, END)
    eeeeee3.insert(0, str(random.choice(sq_8192)))
    eeeeee4.delete(0, END)
    eeeeee4.insert(0, str(random.choice(sq_8192)))
    eeeeee5.delete(0, END)
    eeeeee5.insert(0, str(random.choice(sq_8192)))
    eeeeee6.delete(0, END)
    eeeeee6.insert(0, str(random.choice(sq_8192)))
    eeeeee7.delete(0, END)
    eeeeee7.insert(0, str(random.choice(sq_8192)))
    eeeeee8.delete(0, END)
    eeeeee8.insert(0, str(random.choice(sq_8192)))
    eeeeee9.delete(0, END)
    eeeeee9.insert(0, str(random.choice(sq_8192)))
    eeeeee10.delete(0, END)
    eeeeee10.insert(0, str(random.choice(sq_8192)))
#
    eeeeee11.delete(0, END)
    eeeeee11.insert(0, str(random.choice(sq_8192)))
    eeeeee12.delete(0, END)
    eeeeee12.insert(0, str(random.choice(sq_8192)))
    eeeeee13.delete(0, END)
    eeeeee13.insert(0, str(random.choice(sq_8192)))
    eeeeee14.delete(0, END)
    eeeeee14.insert(0, str(random.choice(sq_8192)))
    eeeeee15.delete(0, END)
    eeeeee15.insert(0, str(random.choice(sq_8192)))
    eeeeee16.delete(0, END)
    eeeeee16.insert(0, str(random.choice(sq_8192)))
    eeeeee17.delete(0, END)
    eeeeee17.insert(0, str(random.choice(sq_8192)))
    eeeeee18.delete(0, END)
    eeeeee18.insert(0, str(random.choice(sq_8192)))
    eeeeee19.delete(0, END)
    eeeeee19.insert(0, str(random.choice(sq_8192)))
    eeeeee20.delete(0, END)
    eeeeee20.insert(0, str(random.choice(sq_8192)))
#
    eeeeee21.delete(0, END)
    eeeeee21.insert(0, str(random.choice(sq_8192)))
    eeeeee22.delete(0, END)
    eeeeee22.insert(0, str(random.choice(sq_8192)))
    eeeeee23.delete(0, END)
    eeeeee23.insert(0, str(random.choice(sq_8192)))
    eeeeee24.delete(0, END)
    eeeeee24.insert(0, str(random.choice(sq_8192)))
    eeeeee25.delete(0, END)
    eeeeee25.insert(0, str(random.choice(sq_8192)))
    eeeeee26.delete(0, END)
    eeeeee26.insert(0, str(random.choice(sq_8192)))
    eeeeee27.delete(0, END)
    eeeeee27.insert(0, str(random.choice(sq_8192)))
    eeeeee28.delete(0, END)
    eeeeee28.insert(0, str(random.choice(sq_8192)))
    eeeeee29.delete(0, END)
    eeeeee29.insert(0, str(random.choice(sq_8192)))
    eeeeee30.delete(0, END)
    eeeeee30.insert(0, str(random.choice(sq_8192)))
#
    eeeeee31.delete(0, END)
    eeeeee31.insert(0, str(random.choice(sq_8192)))
    eeeeee32.delete(0, END)
    eeeeee32.insert(0, str(random.choice(sq_8192)))
    eeeeee33.delete(0, END)
    eeeeee33.insert(0, str(random.choice(sq_8192)))
    eeeeee34.delete(0, END)
    eeeeee34.insert(0, str(random.choice(sq_8192)))
    eeeeee35.delete(0, END)
    eeeeee35.insert(0, str(random.choice(sq_8192)))
    eeeeee36.delete(0, END)
    eeeeee36.insert(0, str(random.choice(sq_8192)))
    eeeeee37.delete(0, END)
    eeeeee37.insert(0, str(random.choice(sq_8192)))
    eeeeee38.delete(0, END)
    eeeeee38.insert(0, str(random.choice(sq_8192)))
    eeeeee39.delete(0, END)
    eeeeee39.insert(0, str(random.choice(sq_8192)))
    eeeeee40.delete(0, END)
    eeeeee40.insert(0, str(random.choice(sq_8192)))
#
    eeeeee41.delete(0, END)
    eeeeee41.insert(0, str(random.choice(sq_8192)))
    eeeeee42.delete(0, END)
    eeeeee42.insert(0, str(random.choice(sq_8192)))
    eeeeee43.delete(0, END)
    eeeeee43.insert(0, str(random.choice(sq_8192)))
    eeeeee44.delete(0, END)
    eeeeee44.insert(0, str(random.choice(sq_8192)))
    eeeeee45.delete(0, END)
    eeeeee45.insert(0, str(random.choice(sq_8192)))
    eeeeee46.delete(0, END)
    eeeeee46.insert(0, str(random.choice(sq_8192)))
    eeeeee47.delete(0, END)
    eeeeee47.insert(0, str(random.choice(sq_8192)))
    eeeeee48.delete(0, END)
    eeeeee48.insert(0, str(random.choice(sq_8192)))
    eeeeee49.delete(0, END)
    eeeeee49.insert(0, str(random.choice(sq_8192)))
    eeeeee50.delete(0, END)
    eeeeee50.insert(0, str(random.choice(sq_8192)))
#
    eeeeee51.delete(0, END)
    eeeeee51.insert(0, str(random.choice(sq_8192)))
    eeeeee52.delete(0, END)
    eeeeee52.insert(0, str(random.choice(sq_8192)))
    eeeeee53.delete(0, END)
    eeeeee53.insert(0, str(random.choice(sq_8192)))
    eeeeee54.delete(0, END)
    eeeeee54.insert(0, str(random.choice(sq_8192)))
    eeeeee55.delete(0, END)
    eeeeee55.insert(0, str(random.choice(sq_8192)))
    eeeeee56.delete(0, END)
    eeeeee56.insert(0, str(random.choice(sq_8192)))
    eeeeee57.delete(0, END)
    eeeeee57.insert(0, str(random.choice(sq_8192)))
    eeeeee58.delete(0, END)
    eeeeee58.insert(0, str(random.choice(sq_8192)))
    eeeeee59.delete(0, END)
    eeeeee59.insert(0, str(random.choice(sq_8192)))
    eeeeee60.delete(0, END)
    eeeeee60.insert(0, str(random.choice(sq_8192)))
#
    eeeeee61.delete(0, END)
    eeeeee61.insert(0, str(random.choice(sq_8192)))
    eeeeee62.delete(0, END)
    eeeeee62.insert(0, str(random.choice(sq_8192)))
    eeeeee63.delete(0, END)
    eeeeee63.insert(0, str(random.choice(sq_8192)))
    eeeeee64.delete(0, END)
    eeeeee64.insert(0, str(random.choice(sq_8192)))
    eeeeee65.delete(0, END)
    eeeeee65.insert(0, str(random.choice(sq_8192)))
    eeeeee66.delete(0, END)
    eeeeee66.insert(0, str(random.choice(sq_8192)))
    eeeeee67.delete(0, END)
    eeeeee67.insert(0, str(random.choice(sq_8192)))
    eeeeee68.delete(0, END)
    eeeeee68.insert(0, str(random.choice(sq_8192)))
    eeeeee69.delete(0, END)
    eeeeee69.insert(0, str(random.choice(sq_8192)))
def change():
    pass
#for the count in next func
count = 0

#make a new list from sq_8192, gen. from user

def mk_set():
    gen_code.append(e0.get())
    print(gen_code[0])
    gen_code.append(e1.get())
    gen_code.append(e2.get())
    gen_code.append(e3.get())
    gen_code.append(e4.get())
    gen_code.append(e5.get())
    gen_code.append(e6.get())
    gen_code.append(e7.get())
    gen_code.append(e8.get())
    gen_code.append(e9.get())
    gen_code.append(e10.get())
    gen_code.append(e11.get())
    gen_code.append(e12.get())
    gen_code.append(e13.get())
    gen_code.append(e14.get())
    gen_code.append(e15.get())
    gen_code.append(e16.get())
    gen_code.append(e17.get())
    gen_code.append(e18.get())
    gen_code.append(e19.get())
    gen_code.append(e20.get())
    gen_code.append(e21.get())
    gen_code.append(e22.get())
    gen_code.append(e23.get())
    gen_code.append(e24.get())
    gen_code.append(e25.get())
    gen_code.append(e26.get())
    gen_code.append(e27.get())
    gen_code.append(e28.get())
    gen_code.append(e29.get())
    gen_code.append(e30.get())
    gen_code.append(e31.get())
    gen_code.append(e32.get())
    gen_code.append(e33.get())
    gen_code.append(e34.get())
    gen_code.append(e35.get())
    gen_code.append(e36.get())
    gen_code.append(e37.get())
    gen_code.append(e38.get())
    gen_code.append(e39.get())
    gen_code.append(e40.get())
    gen_code.append(e41.get())
    gen_code.append(e42.get())
    gen_code.append(e43.get())
    gen_code.append(e44.get())
    gen_code.append(e45.get())
    gen_code.append(e46.get())
    gen_code.append(e47.get())
    gen_code.append(e48.get())
    gen_code.append(e49.get())
    gen_code.append(e50.get())
    gen_code.append(e51.get())
    gen_code.append(e52.get())
    gen_code.append(e53.get())
    gen_code.append(e54.get())
    gen_code.append(e55.get())
    gen_code.append(e56.get())
    gen_code.append(e57.get())
    gen_code.append(e58.get())
    gen_code.append(e59.get())
    gen_code.append(e60.get())
    gen_code.append(e61.get())
    gen_code.append(e62.get())
    gen_code.append(e63.get())
    gen_code.append(e64.get())
    gen_code.append(e65.get())
    gen_code.append(e66.get())
    gen_code.append(e67.get())
    gen_code.append(e68.get())
    gen_code.append(e69.get())
    gen_code.append(e70.get())
    gen_code.append(e71.get())
    gen_code.append(e72.get())
    gen_code.append(e73.get())
    gen_code.append(e74.get())
    gen_code.append(e75.get())
    gen_code.append(e76.get())
    gen_code.append(e77.get())
    gen_code.append(e78.get())
    gen_code.append(e79.get())
    gen_code.append(e80.get())
    gen_code.append(e81.get())
    gen_code.append(e82.get())
    gen_code.append(e83.get())
    gen_code.append(e84.get())
    gen_code.append(e85.get())
    gen_code.append(e86.get())
    gen_code.append(e87.get())
    gen_code.append(e88.get())
    gen_code.append(e89.get())
    gen_code.append(e90.get())
    gen_code.append(e91.get())
    gen_code.append(e92.get())
    gen_code.append(e93.get())
    gen_code.append(e94.get())
    gen_code.append(e95.get())
    gen_code.append(e96.get())
    gen_code.append(e97.get())
    gen_code.append(e98.get())
    gen_code.append(e99.get())
#1
    gen_code.append(ee0.get())
    gen_code.append(ee1.get())
    gen_code.append(ee2.get())
    gen_code.append(ee3.get())
    gen_code.append(ee4.get())
    gen_code.append(ee5.get())
    gen_code.append(ee6.get())
    gen_code.append(ee7.get())
    gen_code.append(ee8.get())
    gen_code.append(ee9.get())
    gen_code.append(ee10.get())
    gen_code.append(ee11.get())
    gen_code.append(ee12.get())
    gen_code.append(ee13.get())
    gen_code.append(ee14.get())
    gen_code.append(ee15.get())
    gen_code.append(ee16.get())
    gen_code.append(ee17.get())
    gen_code.append(ee18.get())
    gen_code.append(ee19.get())
    gen_code.append(ee20.get())
    gen_code.append(ee21.get())
    gen_code.append(ee22.get())
    gen_code.append(ee23.get())
    gen_code.append(ee24.get())
    gen_code.append(ee25.get())
    gen_code.append(ee26.get())
    gen_code.append(ee27.get())
    gen_code.append(ee28.get())
    gen_code.append(ee29.get())
    gen_code.append(ee30.get())
    gen_code.append(ee31.get())
    gen_code.append(ee32.get())
    gen_code.append(ee33.get())
    gen_code.append(ee34.get())
    gen_code.append(ee35.get())
    gen_code.append(ee36.get())
    gen_code.append(ee37.get())
    gen_code.append(ee38.get())
    gen_code.append(ee39.get())
    gen_code.append(ee40.get())
    gen_code.append(ee41.get())
    gen_code.append(ee42.get())
    gen_code.append(ee43.get())
    gen_code.append(ee44.get())
    gen_code.append(ee45.get())
    gen_code.append(ee46.get())
    gen_code.append(ee47.get())
    gen_code.append(ee48.get())
    gen_code.append(ee49.get())
    gen_code.append(ee50.get())
    gen_code.append(ee51.get())
    gen_code.append(ee52.get())
    gen_code.append(ee53.get())
    gen_code.append(ee54.get())
    gen_code.append(ee55.get())
    gen_code.append(ee56.get())
    gen_code.append(ee57.get())
    gen_code.append(ee58.get())
    gen_code.append(ee59.get())
    gen_code.append(ee60.get())
    gen_code.append(ee61.get())
    gen_code.append(ee62.get())
    gen_code.append(ee63.get())
    gen_code.append(ee64.get())
    gen_code.append(ee65.get())
    gen_code.append(ee66.get())
    gen_code.append(ee67.get())
    gen_code.append(ee68.get())
    gen_code.append(ee69.get())
    gen_code.append(ee70.get())
    gen_code.append(ee71.get())
    gen_code.append(ee72.get())
    gen_code.append(ee73.get())
    gen_code.append(ee74.get())
    gen_code.append(ee75.get())
    gen_code.append(ee76.get())
    gen_code.append(ee77.get())
    gen_code.append(ee78.get())
    gen_code.append(ee79.get())
    gen_code.append(ee80.get())
    gen_code.append(ee81.get())
    gen_code.append(ee82.get())
    gen_code.append(ee83.get())
    gen_code.append(ee84.get())
    gen_code.append(ee85.get())
    gen_code.append(ee86.get())
    gen_code.append(ee87.get())
    gen_code.append(ee88.get())
    gen_code.append(ee89.get())
    gen_code.append(ee90.get())
    gen_code.append(ee91.get())
    gen_code.append(ee92.get())
    gen_code.append(ee93.get())
    gen_code.append(ee94.get())
    gen_code.append(ee95.get())
    gen_code.append(ee96.get())
    gen_code.append(ee97.get())
    gen_code.append(ee98.get())
    gen_code.append(ee99.get())
#2
    gen_code.append(eee0.get())
    gen_code.append(eee1.get())
    gen_code.append(eee2.get())
    gen_code.append(eee3.get())
    gen_code.append(eee4.get())
    gen_code.append(eee5.get())
    gen_code.append(eee6.get())
    gen_code.append(eee7.get())
    gen_code.append(eee8.get())
    gen_code.append(eee9.get())
    gen_code.append(eee10.get())
    gen_code.append(eee11.get())
    gen_code.append(eee12.get())
    gen_code.append(eee13.get())
    gen_code.append(eee14.get())
    gen_code.append(eee15.get())
    gen_code.append(eee16.get())
    gen_code.append(eee17.get())
    gen_code.append(eee18.get())
    gen_code.append(eee19.get())
    gen_code.append(eee20.get())
    gen_code.append(eee21.get())
    gen_code.append(eee22.get())
    gen_code.append(eee23.get())
    gen_code.append(eee24.get())
    gen_code.append(eee25.get())
    gen_code.append(eee26.get())
    gen_code.append(eee27.get())
    gen_code.append(eee28.get())
    gen_code.append(eee29.get())
    gen_code.append(eee30.get())
    gen_code.append(eee31.get())
    gen_code.append(eee32.get())
    gen_code.append(eee33.get())
    gen_code.append(eee34.get())
    gen_code.append(eee35.get())
    gen_code.append(eee36.get())
    gen_code.append(eee37.get())
    gen_code.append(eee38.get())
    gen_code.append(eee39.get())
    gen_code.append(eee40.get())
    gen_code.append(eee41.get())
    gen_code.append(eee42.get())
    gen_code.append(eee43.get())
    gen_code.append(eee44.get())
    gen_code.append(eee45.get())
    gen_code.append(eee46.get())
    gen_code.append(eee47.get())
    gen_code.append(eee48.get())
    gen_code.append(eee49.get())
    gen_code.append(eee50.get())
    gen_code.append(eee51.get())
    gen_code.append(eee52.get())
    gen_code.append(eee53.get())
    gen_code.append(eee54.get())
    gen_code.append(eee55.get())
    gen_code.append(eee56.get())
    gen_code.append(eee57.get())
    gen_code.append(eee58.get())
    gen_code.append(eee59.get())
    gen_code.append(eee60.get())
    gen_code.append(eee61.get())
    gen_code.append(eee62.get())
    gen_code.append(eee63.get())
    gen_code.append(eee64.get())
    gen_code.append(eee65.get())
    gen_code.append(eee66.get())
    gen_code.append(eee67.get())
    gen_code.append(eee68.get())
    gen_code.append(eee69.get())
    gen_code.append(eee70.get())
    gen_code.append(eee71.get())
    gen_code.append(eee72.get())
    gen_code.append(eee73.get())
    gen_code.append(eee74.get())
    gen_code.append(eee75.get())
    gen_code.append(eee76.get())
    gen_code.append(eee77.get())
    gen_code.append(eee78.get())
    gen_code.append(eee79.get())
    gen_code.append(eee80.get())
    gen_code.append(eee81.get())
    gen_code.append(eee82.get())
    gen_code.append(eee83.get())
    gen_code.append(eee84.get())
    gen_code.append(eee85.get())
    gen_code.append(eee86.get())
    gen_code.append(eee87.get())
    gen_code.append(eee88.get())
    gen_code.append(eee89.get())
    gen_code.append(eee90.get())
    gen_code.append(eee91.get())
    gen_code.append(eee92.get())
    gen_code.append(eee93.get())
    gen_code.append(eee94.get())
    gen_code.append(eee95.get())
    gen_code.append(eee96.get())
    gen_code.append(eee97.get())
    gen_code.append(eee98.get())
    gen_code.append(eee99.get())
#
    # 3
    gen_code.append(eeee0.get())
    gen_code.append(eeee1.get())
    gen_code.append(eeee2.get())
    gen_code.append(eeee3.get())
    gen_code.append(eeee4.get())
    gen_code.append(eeee5.get())
    gen_code.append(eeee6.get())
    gen_code.append(eeee7.get())
    gen_code.append(eeee8.get())
    gen_code.append(eeee9.get())
    gen_code.append(eeee10.get())
    gen_code.append(eeee11.get())
    gen_code.append(eeee12.get())
    gen_code.append(eeee13.get())
    gen_code.append(eeee14.get())
    gen_code.append(eeee15.get())
    gen_code.append(eeee16.get())
    gen_code.append(eeee17.get())
    gen_code.append(eeee18.get())
    gen_code.append(eeee19.get())
    gen_code.append(eeee20.get())
    gen_code.append(eeee21.get())
    gen_code.append(eeee22.get())
    gen_code.append(eeee23.get())
    gen_code.append(eeee24.get())
    gen_code.append(eeee25.get())
    gen_code.append(eeee26.get())
    gen_code.append(eeee27.get())
    gen_code.append(eeee28.get())
    gen_code.append(eeee29.get())
    gen_code.append(eeee30.get())
    gen_code.append(eeee31.get())
    gen_code.append(eeee32.get())
    gen_code.append(eeee33.get())
    gen_code.append(eeee34.get())
    gen_code.append(eeee35.get())
    gen_code.append(eeee36.get())
    gen_code.append(eeee37.get())
    gen_code.append(eeee38.get())
    gen_code.append(eeee39.get())
    gen_code.append(eeee40.get())
    gen_code.append(eeee41.get())
    gen_code.append(eeee42.get())
    gen_code.append(eeee43.get())
    gen_code.append(eeee44.get())
    gen_code.append(eeee45.get())
    gen_code.append(eeee46.get())
    gen_code.append(eeee47.get())
    gen_code.append(eeee48.get())
    gen_code.append(eeee49.get())
    gen_code.append(eeee50.get())
    gen_code.append(eeee51.get())
    gen_code.append(eeee52.get())
    gen_code.append(eeee53.get())
    gen_code.append(eeee54.get())
    gen_code.append(eeee55.get())
    gen_code.append(eeee56.get())
    gen_code.append(eeee57.get())
    gen_code.append(eeee58.get())
    gen_code.append(eeee59.get())
    gen_code.append(eeee60.get())
    gen_code.append(eeee61.get())
    gen_code.append(eeee62.get())
    gen_code.append(eeee63.get())
    gen_code.append(eeee64.get())
    gen_code.append(eeee65.get())
    gen_code.append(eeee66.get())
    gen_code.append(eeee67.get())
    gen_code.append(eeee68.get())
    gen_code.append(eeee69.get())
#4
    gen_code.append(eeeee0.get())
    gen_code.append(eeeee1.get())
    gen_code.append(eeeee2.get())
    gen_code.append(eeeee3.get())
    gen_code.append(eeeee4.get())
    gen_code.append(eeeee5.get())
    gen_code.append(eeeee6.get())
    gen_code.append(eeeee7.get())
    gen_code.append(eeeee8.get())
    gen_code.append(eeeee9.get())
    gen_code.append(eeeee10.get())
    gen_code.append(eeeee11.get())
    gen_code.append(eeeee12.get())
    gen_code.append(eeeee13.get())
    gen_code.append(eeeee14.get())
    gen_code.append(eeeee15.get())
    gen_code.append(eeeee16.get())
    gen_code.append(eeeee17.get())
    gen_code.append(eeeee18.get())
    gen_code.append(eeeee19.get())
    gen_code.append(eeeee20.get())
    gen_code.append(eeeee21.get())
    gen_code.append(eeeee22.get())
    gen_code.append(eeeee23.get())
    gen_code.append(eeeee24.get())
    gen_code.append(eeeee25.get())
    gen_code.append(eeeee26.get())
    gen_code.append(eeeee27.get())
    gen_code.append(eeeee28.get())
    gen_code.append(eeeee29.get())
    gen_code.append(eeeee30.get())
    gen_code.append(eeeee31.get())
    gen_code.append(eeeee32.get())
    gen_code.append(eeeee33.get())
    gen_code.append(eeeee34.get())
    gen_code.append(eeeee35.get())
    gen_code.append(eeeee36.get())
    gen_code.append(eeeee37.get())
    gen_code.append(eeeee38.get())
    gen_code.append(eeeee39.get())
    gen_code.append(eeeee40.get())
    gen_code.append(eeeee41.get())
    gen_code.append(eeeee42.get())
    gen_code.append(eeeee43.get())
    gen_code.append(eeeee44.get())
    gen_code.append(eeeee45.get())
    gen_code.append(eeeee46.get())
    gen_code.append(eeeee47.get())
    gen_code.append(eeeee48.get())
    gen_code.append(eeeee49.get())
    gen_code.append(eeeee50.get())
    gen_code.append(eeeee51.get())
    gen_code.append(eeeee52.get())
    gen_code.append(eeeee53.get())
    gen_code.append(eeeee54.get())
    gen_code.append(eeeee55.get())
    gen_code.append(eeeee56.get())
    gen_code.append(eeeee57.get())
    gen_code.append(eeeee58.get())
    gen_code.append(eeeee59.get())
#5
    gen_code.append(eeeeee0.get())
    gen_code.append(eeeeee1.get())
    gen_code.append(eeeeee2.get())
    gen_code.append(eeeeee3.get())
    gen_code.append(eeeeee4.get())
    gen_code.append(eeeeee5.get())
    gen_code.append(eeeeee6.get())
    gen_code.append(eeeeee7.get())
    gen_code.append(eeeeee8.get())
    gen_code.append(eeeeee9.get())
    gen_code.append(eeeeee10.get())
    gen_code.append(eeeeee11.get())
    gen_code.append(eeeeee12.get())
    gen_code.append(eeeeee13.get())
    gen_code.append(eeeeee14.get())
    gen_code.append(eeeeee15.get())
    gen_code.append(eeeeee16.get())
    gen_code.append(eeeeee17.get())
    gen_code.append(eeeeee18.get())
    gen_code.append(eeeeee19.get())
    gen_code.append(eeeeee20.get())
    gen_code.append(eeeeee21.get())
    gen_code.append(eeeeee22.get())
    gen_code.append(eeeeee23.get())
    gen_code.append(eeeeee24.get())
    gen_code.append(eeeeee25.get())
    gen_code.append(eeeeee26.get())
    gen_code.append(eeeeee27.get())
    gen_code.append(eeeeee28.get())
    gen_code.append(eeeeee29.get())
    gen_code.append(eeeeee30.get())
    gen_code.append(eeeeee31.get())
    gen_code.append(eeeeee32.get())
    gen_code.append(eeeeee33.get())
    gen_code.append(eeeeee34.get())
    gen_code.append(eeeeee35.get())
    gen_code.append(eeeeee36.get())
    gen_code.append(eeeeee37.get())
    gen_code.append(eeeeee38.get())
    gen_code.append(eeeeee39.get())
    gen_code.append(eeeeee40.get())
    gen_code.append(eeeeee41.get())
    gen_code.append(eeeeee42.get())
    gen_code.append(eeeeee43.get())
    gen_code.append(eeeeee44.get())
    gen_code.append(eeeeee45.get())
    gen_code.append(eeeeee46.get())
    gen_code.append(eeeeee47.get())
    gen_code.append(eeeeee48.get())
    gen_code.append(eeeeee49.get())
    gen_code.append(eeeeee50.get())
    gen_code.append(eeeeee51.get())
    gen_code.append(eeeeee52.get())
    gen_code.append(eeeeee53.get())
    gen_code.append(eeeeee54.get())
    gen_code.append(eeeeee55.get())
    gen_code.append(eeeeee56.get())
    gen_code.append(eeeeee57.get())
    gen_code.append(eeeeee58.get())
    gen_code.append(eeeeee59.get())
    gen_code.append(eeeeee60.get())
    gen_code.append(eeeeee61.get())
    gen_code.append(eeeeee62.get())
    gen_code.append(eeeeee63.get())
    gen_code.append(eeeeee64.get())
    gen_code.append(eeeeee65.get())
    gen_code.append(eeeeee66.get())
    gen_code.append(eeeeee67.get())
    gen_code.append(eeeeee68.get())
    gen_code.append(eeeeee69.get())

    #print what is left
    #print(len(gen_code))

    #counting message +=
    global count
    count = count + 1
    l_0.config(text=f'{count}')

#save rw
def write_nw():
    with open('temp_1.py', 'w') as f:
        f.write("gen_code = "+str(gen_code))

    if f is None:
        return
#frame for buttons

frame_top = LabelFrame(root, text = 'commands')
frame_top.grid(row=0, column =0, padx=5, pady=5, columnspan=20)

#labels + counter
l_0 = Label(frame_top, text= 'Message length = ')
l_0.grid(row=0, column=4, pady=5,padx=5)

l_count = Label(frame_top, text ='')
l_count.grid(row=0, column=5, pady=5, padx=5)

#button to make random codes appear

b0 = Button(frame_top, text = 'make random', command = mk_random)
b0.grid(row=0, column=1)

#button to set the random codes in temp.py

b1 = Button(frame_top, text = 'set', command = mk_set)
b1.grid(row=0, column=2)

#button to rewrite

write_new = Button(frame_top, text = 'rewrite code',fg = 'red', command = write_nw)
write_new.grid(row=0, column=0)

#frame 100

f_0= LabelFrame(root, text = 'Entries')
f_0.grid(row=1, column=0, padx=5, pady=5, sticky=W)

#frame 200

f_1= LabelFrame(root, text = 'Entries')
f_1.grid(row=1, column=1, padx=5, pady= 5)

#frame 300

f_2= LabelFrame(root, text = 'Entries')
f_2.grid(row=1, column=2, padx=5, pady= 5)

#frame 370

f_3= LabelFrame(root, text = 'Entries')
f_3.grid(row=2, column=0, padx=5, pady=5, sticky=W)

#frame 430

f_4= LabelFrame(root, text = 'Entries')
f_4.grid(row=2, column=1, padx=5, pady= 5)

#frame 500

f_5= LabelFrame(root, text = 'Entries')
f_5.grid(row=2, column=2, padx=5, pady= 5)

#Entry boxes (100)

e0 = Entry(f_0, width=13, bg = 'black', fg = 'green')
e0.grid(row=0, column=0)

e1 = Entry(f_0, width=13, bg = 'black', fg = 'green')
e1.grid(row=0, column=1)

e2 = Entry(f_0, width=13, bg = 'black', fg = 'green')
e2.grid(row=0, column=2)

e3 = Entry(f_0, width=13, bg = 'black', fg = 'green')
e3.grid(row=0, column=3)

e4 = Entry(f_0, width=13, bg = 'black', fg = 'green')
e4.grid(row=0, column=4)
#
e5 = Entry(f_0, width=13, bg = 'black', fg = 'green')
e5.grid(row=1, column=0)

e6 = Entry(f_0, width=13, bg = 'black', fg = 'green')
e6.grid(row=1, column=1)

e7 = Entry(f_0, width=13, bg = 'black', fg = 'green')
e7.grid(row=1, column=2)

e8 = Entry(f_0, width=13, bg = 'black', fg = 'green')
e8.grid(row=1, column=3)

e9 = Entry(f_0, width=13, bg = 'black', fg = 'green')
e9.grid(row=1, column=4)
#
e10 = Entry(f_0, width=13, bg = 'black', fg = 'green')
e10.grid(row=2, column=0)

e11 = Entry(f_0, width=13, bg = 'black', fg = 'green')
e11.grid(row=2, column=1)

e12 = Entry(f_0, width=13, bg = 'black', fg = 'green')
e12.grid(row=2, column=2)

e13 = Entry(f_0, width=13, bg = 'black', fg = 'green')
e13.grid(row=2, column=3)

e14 = Entry(f_0, width=13, bg = 'black', fg = 'green')
e14.grid(row=2, column=4)
#
e15 = Entry(f_0, width=13, bg = 'black', fg = 'green')
e15.grid(row=3, column=0)

e16 = Entry(f_0, width=13, bg = 'black', fg = 'green')
e16.grid(row=3, column=1)

e17 = Entry(f_0, width=13, bg = 'black', fg = 'green')
e17.grid(row=3, column=2)

e18 = Entry(f_0, width=13, bg = 'black', fg = 'green')
e18.grid(row=3, column=3)

e19 = Entry(f_0, width=13, bg = 'black', fg = 'green')
e19.grid(row=3, column=4)
#
e20 = Entry(f_0, width=13, bg = 'black', fg = 'green')
e20.grid(row=4, column=0)

e21 = Entry(f_0, width=13, bg = 'black', fg = 'green')
e21.grid(row=4, column=1)

e22 = Entry(f_0, width=13, bg = 'black', fg = 'green')
e22.grid(row=4, column=2)

e23 = Entry(f_0, width=13, bg = 'black', fg = 'green')
e23.grid(row=4, column=3)

e24 = Entry(f_0, width=13, bg = 'black', fg = 'green')
e24.grid(row=4, column=4)
#
e25 = Entry(f_0, width=13, bg = 'black', fg = 'green')
e25.grid(row=5, column=0)

e26 = Entry(f_0, width=13, bg = 'black', fg = 'green')
e26.grid(row=5, column=1)

e27 = Entry(f_0, width=13, bg = 'black', fg = 'green')
e27.grid(row=5, column=2)

e28 = Entry(f_0, width=13, bg = 'black', fg = 'green')
e28.grid(row=5, column=3)

e29 = Entry(f_0, width=13, bg = 'black', fg = 'green')
e29.grid(row=5, column=4)
#
e30 = Entry(f_0, width=13, bg = 'black', fg = 'green')
e30.grid(row=6, column=0)

e31 = Entry(f_0, width=13, bg = 'black', fg = 'green')
e31.grid(row=6, column=1)

e32 = Entry(f_0, width=13, bg = 'black', fg = 'green')
e32.grid(row=6, column=2)

e33 = Entry(f_0, width=13, bg = 'black', fg = 'green')
e33.grid(row=6, column=3)

e34 = Entry(f_0, width=13, bg = 'black', fg = 'green')
e34.grid(row=6, column=4)
#
e35 = Entry(f_0, width=13, bg = 'black', fg = 'green')
e35.grid(row=7, column=0)

e36 = Entry(f_0, width=13, bg = 'black', fg = 'green')
e36.grid(row=7, column=1)

e37 = Entry(f_0, width=13, bg = 'black', fg = 'green')
e37.grid(row=7, column=2)

e38 = Entry(f_0, width=13, bg = 'black', fg = 'green')
e38.grid(row=7, column=3)

e39 = Entry(f_0, width=13, bg = 'black', fg = 'green')
e39.grid(row=7, column=4)
#
e40 = Entry(f_0, width=13, bg = 'black', fg = 'green')
e40.grid(row=8, column=0)

e41 = Entry(f_0, width=13, bg = 'black', fg = 'green')
e41.grid(row=8, column=1)

e42 = Entry(f_0, width=13, bg = 'black', fg = 'green')
e42.grid(row=8, column=2)

e43 = Entry(f_0, width=13, bg = 'black', fg = 'green')
e43.grid(row=8, column=3)

e44 = Entry(f_0, width=13, bg = 'black', fg = 'green')
e44.grid(row=8, column=4)
#
e45 = Entry(f_0, width=13, bg = 'black', fg = 'green')
e45.grid(row=9, column=0)

e46 = Entry(f_0, width=13, bg = 'black', fg = 'green')
e46.grid(row=9, column=1)

e47 = Entry(f_0, width=13, bg = 'black', fg = 'green')
e47.grid(row=9, column=2)

e48 = Entry(f_0, width=13, bg = 'black', fg = 'green')
e48.grid(row=9, column=3)

e49 = Entry(f_0, width=13, bg = 'black', fg = 'green')
e49.grid(row=9, column=4)
#
e50 = Entry(f_0, width=13, bg = 'black', fg = 'green')
e50.grid(row=10, column=0)

e51 = Entry(f_0, width=13, bg = 'black', fg = 'green')
e51.grid(row=10, column=1)

e52 = Entry(f_0, width=13, bg = 'black', fg = 'green')
e52.grid(row=10, column=2)

e53 = Entry(f_0, width=13, bg = 'black', fg = 'green')
e53.grid(row=10, column=3)

e54 = Entry(f_0, width=13, bg = 'black', fg = 'green')
e54.grid(row=10, column=4)
#
e55 = Entry(f_0, width=13, bg = 'black', fg = 'green')
e55.grid(row=11, column=0)

e56 = Entry(f_0, width=13, bg = 'black', fg = 'green')
e56.grid(row=11, column=1)

e57 = Entry(f_0, width=13, bg = 'black', fg = 'green')
e57.grid(row=11, column=2)

e58 = Entry(f_0, width=13, bg = 'black', fg = 'green')
e58.grid(row=11, column=3)

e59 = Entry(f_0, width=13, bg = 'black', fg = 'green')
e59.grid(row=11, column=4)
#
e60 = Entry(f_0, width=13, bg = 'black', fg = 'green')
e60.grid(row=12, column=0)

e61 = Entry(f_0, width=13, bg = 'black', fg = 'green')
e61.grid(row=12, column=1)

e62 = Entry(f_0, width=13, bg = 'black', fg = 'green')
e62.grid(row=12, column=2)

e63 = Entry(f_0, width=13, bg = 'black', fg = 'green')
e63.grid(row=12, column=3)

e64 = Entry(f_0, width=13, bg = 'black', fg = 'green')
e64.grid(row=12, column=4)
#
e65 = Entry(f_0, width=13, bg = 'black', fg = 'green')
e65.grid(row=13, column=0)

e66 = Entry(f_0, width=13, bg = 'black', fg = 'green')
e66.grid(row=13, column=1)

e67 = Entry(f_0, width=13, bg = 'black', fg = 'green')
e67.grid(row=13, column=2)

e68 = Entry(f_0, width=13, bg = 'black', fg = 'green')
e68.grid(row=13, column=3)

e69 = Entry(f_0, width=13, bg = 'black', fg = 'green')
e69.grid(row=13, column=4)
#
e70 = Entry(f_0, width=13, bg = 'black', fg = 'green')
e70.grid(row=14, column=0)

e71 = Entry(f_0, width=13, bg = 'black', fg = 'green')
e71.grid(row=14, column=1)

e72 = Entry(f_0, width=13, bg = 'black', fg = 'green')
e72.grid(row=14, column=2)

e73 = Entry(f_0, width=13, bg = 'black', fg = 'green')
e73.grid(row=14, column=3)

e74 = Entry(f_0, width=13, bg = 'black', fg = 'green')
e74.grid(row=14, column=4)
#
e75 = Entry(f_0, width=13, bg = 'black', fg = 'green')
e75.grid(row=15, column=0)

e76 = Entry(f_0, width=13, bg = 'black', fg = 'green')
e76.grid(row=15, column=1)

e77 = Entry(f_0, width=13, bg = 'black', fg = 'green')
e77.grid(row=15, column=2)

e78 = Entry(f_0, width=13, bg = 'black', fg = 'green')
e78.grid(row=15, column=3)

e79 = Entry(f_0, width=13, bg = 'black', fg = 'green')
e79.grid(row=15, column=4)
#
e80 = Entry(f_0, width=13, bg = 'black', fg = 'green')
e80.grid(row=16, column=0)

e81 = Entry(f_0, width=13, bg = 'black', fg = 'green')
e81.grid(row=16, column=1)

e82 = Entry(f_0, width=13, bg = 'black', fg = 'green')
e82.grid(row=16, column=2)

e83 = Entry(f_0, width=13, bg = 'black', fg = 'green')
e83.grid(row=16, column=3)

e84 = Entry(f_0, width=13, bg = 'black', fg = 'green')
e84.grid(row=16, column=4)
#
e85 = Entry(f_0, width=13, bg = 'black', fg = 'green')
e85.grid(row=17, column=0)

e86 = Entry(f_0, width=13, bg = 'black', fg = 'green')
e86.grid(row=17, column=1)

e87 = Entry(f_0, width=13, bg = 'black', fg = 'green')
e87.grid(row=17, column=2)

e88 = Entry(f_0, width=13, bg = 'black', fg = 'green')
e88.grid(row=17, column=3)

e89 = Entry(f_0, width=13, bg = 'black', fg = 'green')
e89.grid(row=17, column=4)
#
e90 = Entry(f_0, width=13, bg = 'black', fg = 'green')
e90.grid(row=18, column=0)

e91 = Entry(f_0, width=13, bg = 'black', fg = 'green')
e91.grid(row=18, column=1)

e92 = Entry(f_0, width=13, bg = 'black', fg = 'green')
e92.grid(row=18, column=2)

e93 = Entry(f_0, width=13, bg = 'black', fg = 'green')
e93.grid(row=18, column=3)

e94 = Entry(f_0, width=13, bg = 'black', fg = 'green')
e94.grid(row=18, column=4)
#
e95 = Entry(f_0, width=13, bg = 'black', fg = 'green')
e95.grid(row=19, column=0)

e96 = Entry(f_0, width=13, bg = 'black', fg = 'green')
e96.grid(row=19, column=1)

e97 = Entry(f_0, width=13, bg = 'black', fg = 'green')
e97.grid(row=19, column=2)

e98 = Entry(f_0, width=13, bg = 'black', fg = 'green')
e98.grid(row=19, column=3)

e99 = Entry(f_0, width=13, bg = 'black', fg = 'green')
e99.grid(row=19, column=4)

#200

ee0 = Entry(f_1, width=13, bg = 'black', fg = 'green')
ee0.grid(row=0, column=0)

ee1 = Entry(f_1, width=13, bg = 'black', fg = 'green')
ee1.grid(row=0, column=1)

ee2 = Entry(f_1, width=13, bg = 'black', fg = 'green')
ee2.grid(row=0, column=2)

ee3 = Entry(f_1, width=13, bg = 'black', fg = 'green')
ee3.grid(row=0, column=3)

ee4 = Entry(f_1, width=13, bg = 'black', fg = 'green')
ee4.grid(row=0, column=4)
#
ee5 = Entry(f_1, width=13, bg = 'black', fg = 'green')
ee5.grid(row=1, column=0)

ee6 = Entry(f_1, width=13, bg = 'black', fg = 'green')
ee6.grid(row=1, column=1)

ee7 = Entry(f_1, width=13, bg = 'black', fg = 'green')
ee7.grid(row=1, column=2)

ee8 = Entry(f_1, width=13, bg = 'black', fg = 'green')
ee8.grid(row=1, column=3)

ee9 = Entry(f_1, width=13, bg = 'black', fg = 'green')
ee9.grid(row=1, column=4)
#
ee10 = Entry(f_1, width=13, bg = 'black', fg = 'green')
ee10.grid(row=2, column=0)

ee11 = Entry(f_1, width=13, bg = 'black', fg = 'green')
ee11.grid(row=2, column=1)

ee12 = Entry(f_1, width=13, bg = 'black', fg = 'green')
ee12.grid(row=2, column=2)

ee13 = Entry(f_1, width=13, bg = 'black', fg = 'green')
ee13.grid(row=2, column=3)

ee14 = Entry(f_1, width=13, bg = 'black', fg = 'green')
ee14.grid(row=2, column=4)
#
ee15 = Entry(f_1, width=13, bg = 'black', fg = 'green')
ee15.grid(row=3, column=0)

ee16 = Entry(f_1, width=13, bg = 'black', fg = 'green')
ee16.grid(row=3, column=1)

ee17 = Entry(f_1, width=13, bg = 'black', fg = 'green')
ee17.grid(row=3, column=2)

ee18 = Entry(f_1, width=13, bg = 'black', fg = 'green')
ee18.grid(row=3, column=3)

ee19 = Entry(f_1, width=13, bg = 'black', fg = 'green')
ee19.grid(row=3, column=4)
#
ee20 = Entry(f_1, width=13, bg = 'black', fg = 'green')
ee20.grid(row=4, column=0)

ee21 = Entry(f_1, width=13, bg = 'black', fg = 'green')
ee21.grid(row=4, column=1)

ee22 = Entry(f_1, width=13, bg = 'black', fg = 'green')
ee22.grid(row=4, column=2)

ee23 = Entry(f_1, width=13, bg = 'black', fg = 'green')
ee23.grid(row=4, column=3)

ee24 = Entry(f_1, width=13, bg = 'black', fg = 'green')
ee24.grid(row=4, column=4)
#
ee25 = Entry(f_1, width=13, bg = 'black', fg = 'green')
ee25.grid(row=5, column=0)

ee26 = Entry(f_1, width=13, bg = 'black', fg = 'green')
ee26.grid(row=5, column=1)

ee27 = Entry(f_1, width=13, bg = 'black', fg = 'green')
ee27.grid(row=5, column=2)

ee28 = Entry(f_1, width=13, bg = 'black', fg = 'green')
ee28.grid(row=5, column=3)

ee29 = Entry(f_1, width=13, bg = 'black', fg = 'green')
ee29.grid(row=5, column=4)
#
ee30 = Entry(f_1, width=13, bg = 'black', fg = 'green')
ee30.grid(row=6, column=0)

ee31 = Entry(f_1, width=13, bg = 'black', fg = 'green')
ee31.grid(row=6, column=1)

ee32 = Entry(f_1, width=13, bg = 'black', fg = 'green')
ee32.grid(row=6, column=2)

ee33 = Entry(f_1, width=13, bg = 'black', fg = 'green')
ee33.grid(row=6, column=3)

ee34 = Entry(f_1, width=13, bg = 'black', fg = 'green')
ee34.grid(row=6, column=4)
#
ee35 = Entry(f_1, width=13, bg = 'black', fg = 'green')
ee35.grid(row=7, column=0)

ee36 = Entry(f_1, width=13, bg = 'black', fg = 'green')
ee36.grid(row=7, column=1)

ee37 = Entry(f_1, width=13, bg = 'black', fg = 'green')
ee37.grid(row=7, column=2)

ee38 = Entry(f_1, width=13, bg = 'black', fg = 'green')
ee38.grid(row=7, column=3)

ee39 = Entry(f_1, width=13, bg = 'black', fg = 'green')
ee39.grid(row=7, column=4)
#
ee40 = Entry(f_1, width=13, bg = 'black', fg = 'green')
ee40.grid(row=8, column=0)

ee41 = Entry(f_1, width=13, bg = 'black', fg = 'green')
ee41.grid(row=8, column=1)

ee42 = Entry(f_1, width=13, bg = 'black', fg = 'green')
ee42.grid(row=8, column=2)

ee43 = Entry(f_1, width=13, bg = 'black', fg = 'green')
ee43.grid(row=8, column=3)

ee44 = Entry(f_1, width=13, bg = 'black', fg = 'green')
ee44.grid(row=8, column=4)
#
ee45 = Entry(f_1, width=13, bg = 'black', fg = 'green')
ee45.grid(row=9, column=0)

ee46 = Entry(f_1, width=13, bg = 'black', fg = 'green')
ee46.grid(row=9, column=1)

ee47 = Entry(f_1, width=13, bg = 'black', fg = 'green')
ee47.grid(row=9, column=2)

ee48 = Entry(f_1, width=13, bg = 'black', fg = 'green')
ee48.grid(row=9, column=3)

ee49 = Entry(f_1, width=13, bg = 'black', fg = 'green')
ee49.grid(row=9, column=4)
#
ee50 = Entry(f_1, width=13, bg = 'black', fg = 'green')
ee50.grid(row=10, column=0)

ee51 = Entry(f_1, width=13, bg = 'black', fg = 'green')
ee51.grid(row=10, column=1)

ee52 = Entry(f_1, width=13, bg = 'black', fg = 'green')
ee52.grid(row=10, column=2)

ee53 = Entry(f_1, width=13, bg = 'black', fg = 'green')
ee53.grid(row=10, column=3)

ee54 = Entry(f_1, width=13, bg = 'black', fg = 'green')
ee54.grid(row=10, column=4)
#
ee55 = Entry(f_1, width=13, bg = 'black', fg = 'green')
ee55.grid(row=11, column=0)

ee56 = Entry(f_1, width=13, bg = 'black', fg = 'green')
ee56.grid(row=11, column=1)

ee57 = Entry(f_1, width=13, bg = 'black', fg = 'green')
ee57.grid(row=11, column=2)

ee58 = Entry(f_1, width=13, bg = 'black', fg = 'green')
ee58.grid(row=11, column=3)

ee59 = Entry(f_1, width=13, bg = 'black', fg = 'green')
ee59.grid(row=11, column=4)
#
ee60 = Entry(f_1, width=13, bg = 'black', fg = 'green')
ee60.grid(row=12, column=0)

ee61 = Entry(f_1, width=13, bg = 'black', fg = 'green')
ee61.grid(row=12, column=1)

ee62 = Entry(f_1, width=13, bg = 'black', fg = 'green')
ee62.grid(row=12, column=2)

ee63 = Entry(f_1, width=13, bg = 'black', fg = 'green')
ee63.grid(row=12, column=3)

ee64 = Entry(f_1, width=13, bg = 'black', fg = 'green')
ee64.grid(row=12, column=4)
#
ee65 = Entry(f_1, width=13, bg = 'black', fg = 'green')
ee65.grid(row=13, column=0)

ee66 = Entry(f_1, width=13, bg = 'black', fg = 'green')
ee66.grid(row=13, column=1)

ee67 = Entry(f_1, width=13, bg = 'black', fg = 'green')
ee67.grid(row=13, column=2)

ee68 = Entry(f_1, width=13, bg = 'black', fg = 'green')
ee68.grid(row=13, column=3)

ee69 = Entry(f_1, width=13, bg = 'black', fg = 'green')
ee69.grid(row=13, column=4)
#
ee70 = Entry(f_1, width=13, bg = 'black', fg = 'green')
ee70.grid(row=14, column=0)

ee71 = Entry(f_1, width=13, bg = 'black', fg = 'green')
ee71.grid(row=14, column=1)

ee72 = Entry(f_1, width=13, bg = 'black', fg = 'green')
ee72.grid(row=14, column=2)

ee73 = Entry(f_1, width=13, bg = 'black', fg = 'green')
ee73.grid(row=14, column=3)

ee74 = Entry(f_1, width=13, bg = 'black', fg = 'green')
ee74.grid(row=14, column=4)
#
ee75 = Entry(f_1, width=13, bg = 'black', fg = 'green')
ee75.grid(row=15, column=0)

ee76 = Entry(f_1, width=13, bg = 'black', fg = 'green')
ee76.grid(row=15, column=1)

ee77 = Entry(f_1, width=13, bg = 'black', fg = 'green')
ee77.grid(row=15, column=2)

ee78 = Entry(f_1, width=13, bg = 'black', fg = 'green')
ee78.grid(row=15, column=3)

ee79 = Entry(f_1, width=13, bg = 'black', fg = 'green')
ee79.grid(row=15, column=4)
#
ee80 = Entry(f_1, width=13, bg = 'black', fg = 'green')
ee80.grid(row=16, column=0)

ee81 = Entry(f_1, width=13, bg = 'black', fg = 'green')
ee81.grid(row=16, column=1)

ee82 = Entry(f_1, width=13, bg = 'black', fg = 'green')
ee82.grid(row=16, column=2)

ee83 = Entry(f_1, width=13, bg = 'black', fg = 'green')
ee83.grid(row=16, column=3)

ee84 = Entry(f_1, width=13, bg = 'black', fg = 'green')
ee84.grid(row=16, column=4)
#
ee85 = Entry(f_1, width=13, bg = 'black', fg = 'green')
ee85.grid(row=17, column=0)

ee86 = Entry(f_1, width=13, bg = 'black', fg = 'green')
ee86.grid(row=17, column=1)

ee87 = Entry(f_1, width=13, bg = 'black', fg = 'green')
ee87.grid(row=17, column=2)

ee88 = Entry(f_1, width=13, bg = 'black', fg = 'green')
ee88.grid(row=17, column=3)

ee89 = Entry(f_1, width=13, bg = 'black', fg = 'green')
ee89.grid(row=17, column=4)
#
ee90 = Entry(f_1, width=13, bg = 'black', fg = 'green')
ee90.grid(row=18, column=0)

ee91 = Entry(f_1, width=13, bg = 'black', fg = 'green')
ee91.grid(row=18, column=1)

ee92 = Entry(f_1, width=13, bg = 'black', fg = 'green')
ee92.grid(row=18, column=2)

ee93 = Entry(f_1, width=13, bg = 'black', fg = 'green')
ee93.grid(row=18, column=3)

ee94 = Entry(f_1, width=13, bg = 'black', fg = 'green')
ee94.grid(row=18, column=4)
#
ee95 = Entry(f_1, width=13, bg = 'black', fg = 'green')
ee95.grid(row=19, column=0)

ee96 = Entry(f_1, width=13, bg = 'black', fg = 'green')
ee96.grid(row=19, column=1)

ee97 = Entry(f_1, width=13, bg = 'black', fg = 'green')
ee97.grid(row=19, column=2)

ee98 = Entry(f_1, width=13, bg = 'black', fg = 'green')
ee98.grid(row=19, column=3)

ee99 = Entry(f_1, width=13, bg = 'black', fg = 'green')
ee99.grid(row=19, column=4)

#300

eee0 = Entry(f_2, width=13, bg = 'black', fg = 'green')
eee0.grid(row=0, column=0)

eee1 = Entry(f_2, width=13, bg = 'black', fg = 'green')
eee1.grid(row=0, column=1)

eee2 = Entry(f_2, width=13, bg = 'black', fg = 'green')
eee2.grid(row=0, column=2)

eee3 = Entry(f_2, width=13, bg = 'black', fg = 'green')
eee3.grid(row=0, column=3)

eee4 = Entry(f_2, width=13, bg = 'black', fg = 'green')
eee4.grid(row=0, column=4)
#
eee5 = Entry(f_2, width=13, bg = 'black', fg = 'green')
eee5.grid(row=1, column=0)

eee6 = Entry(f_2, width=13, bg = 'black', fg = 'green')
eee6.grid(row=1, column=1)

eee7 = Entry(f_2, width=13, bg = 'black', fg = 'green')
eee7.grid(row=1, column=2)

eee8 = Entry(f_2, width=13, bg = 'black', fg = 'green')
eee8.grid(row=1, column=3)

eee9 = Entry(f_2, width=13, bg = 'black', fg = 'green')
eee9.grid(row=1, column=4)
#
eee10 = Entry(f_2, width=13, bg = 'black', fg = 'green')
eee10.grid(row=2, column=0)

eee11 = Entry(f_2, width=13, bg = 'black', fg = 'green')
eee11.grid(row=2, column=1)

eee12 = Entry(f_2, width=13, bg = 'black', fg = 'green')
eee12.grid(row=2, column=2)

eee13 = Entry(f_2, width=13, bg = 'black', fg = 'green')
eee13.grid(row=2, column=3)

eee14 = Entry(f_2, width=13, bg = 'black', fg = 'green')
eee14.grid(row=2, column=4)
#
eee15 = Entry(f_2, width=13, bg = 'black', fg = 'green')
eee15.grid(row=3, column=0)

eee16 = Entry(f_2, width=13, bg = 'black', fg = 'green')
eee16.grid(row=3, column=1)

eee17 = Entry(f_2, width=13, bg = 'black', fg = 'green')
eee17.grid(row=3, column=2)

eee18 = Entry(f_2, width=13, bg = 'black', fg = 'green')
eee18.grid(row=3, column=3)

eee19 = Entry(f_2, width=13, bg = 'black', fg = 'green')
eee19.grid(row=3, column=4)
#
eee20 = Entry(f_2, width=13, bg = 'black', fg = 'green')
eee20.grid(row=4, column=0)

eee21 = Entry(f_2, width=13, bg = 'black', fg = 'green')
eee21.grid(row=4, column=1)

eee22 = Entry(f_2, width=13, bg = 'black', fg = 'green')
eee22.grid(row=4, column=2)

eee23 = Entry(f_2, width=13, bg = 'black', fg = 'green')
eee23.grid(row=4, column=3)

eee24 = Entry(f_2, width=13, bg = 'black', fg = 'green')
eee24.grid(row=4, column=4)
#
eee25 = Entry(f_2, width=13, bg = 'black', fg = 'green')
eee25.grid(row=5, column=0)

eee26 = Entry(f_2, width=13, bg = 'black', fg = 'green')
eee26.grid(row=5, column=1)

eee27 = Entry(f_2, width=13, bg = 'black', fg = 'green')
eee27.grid(row=5, column=2)

eee28 = Entry(f_2, width=13, bg = 'black', fg = 'green')
eee28.grid(row=5, column=3)

eee29 = Entry(f_2, width=13, bg = 'black', fg = 'green')
eee29.grid(row=5, column=4)
#
eee30 = Entry(f_2, width=13, bg = 'black', fg = 'green')
eee30.grid(row=6, column=0)

eee31 = Entry(f_2, width=13, bg = 'black', fg = 'green')
eee31.grid(row=6, column=1)

eee32 = Entry(f_2, width=13, bg = 'black', fg = 'green')
eee32.grid(row=6, column=2)

eee33 = Entry(f_2, width=13, bg = 'black', fg = 'green')
eee33.grid(row=6, column=3)

eee34 = Entry(f_2, width=13, bg = 'black', fg = 'green')
eee34.grid(row=6, column=4)
#
eee35 = Entry(f_2, width=13, bg = 'black', fg = 'green')
eee35.grid(row=7, column=0)

eee36 = Entry(f_2, width=13, bg = 'black', fg = 'green')
eee36.grid(row=7, column=1)

eee37 = Entry(f_2, width=13, bg = 'black', fg = 'green')
eee37.grid(row=7, column=2)

eee38 = Entry(f_2, width=13, bg = 'black', fg = 'green')
eee38.grid(row=7, column=3)

eee39 = Entry(f_2, width=13, bg = 'black', fg = 'green')
eee39.grid(row=7, column=4)
#
eee40 = Entry(f_2, width=13, bg = 'black', fg = 'green')
eee40.grid(row=8, column=0)

eee41 = Entry(f_2, width=13, bg = 'black', fg = 'green')
eee41.grid(row=8, column=1)

eee42 = Entry(f_2, width=13, bg = 'black', fg = 'green')
eee42.grid(row=8, column=2)

eee43 = Entry(f_2, width=13, bg = 'black', fg = 'green')
eee43.grid(row=8, column=3)

eee44 = Entry(f_2, width=13, bg = 'black', fg = 'green')
eee44.grid(row=8, column=4)
#
eee45 = Entry(f_2, width=13, bg = 'black', fg = 'green')
eee45.grid(row=9, column=0)

eee46 = Entry(f_2, width=13, bg = 'black', fg = 'green')
eee46.grid(row=9, column=1)

eee47 = Entry(f_2, width=13, bg = 'black', fg = 'green')
eee47.grid(row=9, column=2)

eee48 = Entry(f_2, width=13, bg = 'black', fg = 'green')
eee48.grid(row=9, column=3)

eee49 = Entry(f_2, width=13, bg = 'black', fg = 'green')
eee49.grid(row=9, column=4)
#
eee50 = Entry(f_2, width=13, bg = 'black', fg = 'green')
eee50.grid(row=10, column=0)

eee51 = Entry(f_2, width=13, bg = 'black', fg = 'green')
eee51.grid(row=10, column=1)

eee52 = Entry(f_2, width=13, bg = 'black', fg = 'green')
eee52.grid(row=10, column=2)

eee53 = Entry(f_2, width=13, bg = 'black', fg = 'green')
eee53.grid(row=10, column=3)

eee54 = Entry(f_2, width=13, bg = 'black', fg = 'green')
eee54.grid(row=10, column=4)
#
eee55 = Entry(f_2, width=13, bg = 'black', fg = 'green')
eee55.grid(row=11, column=0)

eee56 = Entry(f_2, width=13, bg = 'black', fg = 'green')
eee56.grid(row=11, column=1)

eee57 = Entry(f_2, width=13, bg = 'black', fg = 'green')
eee57.grid(row=11, column=2)

eee58 = Entry(f_2, width=13, bg = 'black', fg = 'green')
eee58.grid(row=11, column=3)

eee59 = Entry(f_2, width=13, bg = 'black', fg = 'green')
eee59.grid(row=11, column=4)
#
eee60 = Entry(f_2, width=13, bg = 'black', fg = 'green')
eee60.grid(row=12, column=0)

eee61 = Entry(f_2, width=13, bg = 'black', fg = 'green')
eee61.grid(row=12, column=1)

eee62 = Entry(f_2, width=13, bg = 'black', fg = 'green')
eee62.grid(row=12, column=2)

eee63 = Entry(f_2, width=13, bg = 'black', fg = 'green')
eee63.grid(row=12, column=3)

eee64 = Entry(f_2, width=13, bg = 'black', fg = 'green')
eee64.grid(row=12, column=4)
#
eee65 = Entry(f_2, width=13, bg = 'black', fg = 'green')
eee65.grid(row=13, column=0)

eee66 = Entry(f_2, width=13, bg = 'black', fg = 'green')
eee66.grid(row=13, column=1)

eee67 = Entry(f_2, width=13, bg = 'black', fg = 'green')
eee67.grid(row=13, column=2)

eee68 = Entry(f_2, width=13, bg = 'black', fg = 'green')
eee68.grid(row=13, column=3)

eee69 = Entry(f_2, width=13, bg = 'black', fg = 'green')
eee69.grid(row=13, column=4)
#
eee70 = Entry(f_2, width=13, bg = 'black', fg = 'green')
eee70.grid(row=14, column=0)

eee71 = Entry(f_2, width=13, bg = 'black', fg = 'green')
eee71.grid(row=14, column=1)

eee72 = Entry(f_2, width=13, bg = 'black', fg = 'green')
eee72.grid(row=14, column=2)

eee73 = Entry(f_2, width=13, bg = 'black', fg = 'green')
eee73.grid(row=14, column=3)

eee74 = Entry(f_2, width=13, bg = 'black', fg = 'green')
eee74.grid(row=14, column=4)
#
eee75 = Entry(f_2, width=13, bg = 'black', fg = 'green')
eee75.grid(row=15, column=0)

eee76 = Entry(f_2, width=13, bg = 'black', fg = 'green')
eee76.grid(row=15, column=1)

eee77 = Entry(f_2, width=13, bg = 'black', fg = 'green')
eee77.grid(row=15, column=2)

eee78 = Entry(f_2, width=13, bg = 'black', fg = 'green')
eee78.grid(row=15, column=3)

eee79 = Entry(f_2, width=13, bg = 'black', fg = 'green')
eee79.grid(row=15, column=4)
#
eee80 = Entry(f_2, width=13, bg = 'black', fg = 'green')
eee80.grid(row=16, column=0)

eee81 = Entry(f_2, width=13, bg = 'black', fg = 'green')
eee81.grid(row=16, column=1)

eee82 = Entry(f_2, width=13, bg = 'black', fg = 'green')
eee82.grid(row=16, column=2)

eee83 = Entry(f_2, width=13, bg = 'black', fg = 'green')
eee83.grid(row=16, column=3)

eee84 = Entry(f_2, width=13, bg = 'black', fg = 'green')
eee84.grid(row=16, column=4)
#
eee85 = Entry(f_2, width=13, bg = 'black', fg = 'green')
eee85.grid(row=17, column=0)

eee86 = Entry(f_2, width=13, bg = 'black', fg = 'green')
eee86.grid(row=17, column=1)

eee87 = Entry(f_2, width=13, bg = 'black', fg = 'green')
eee87.grid(row=17, column=2)

eee88 = Entry(f_2, width=13, bg = 'black', fg = 'green')
eee88.grid(row=17, column=3)

eee89 = Entry(f_2, width=13, bg = 'black', fg = 'green')
eee89.grid(row=17, column=4)
#
eee90 = Entry(f_2, width=13, bg = 'black', fg = 'green')
eee90.grid(row=18, column=0)

eee91 = Entry(f_2, width=13, bg = 'black', fg = 'green')
eee91.grid(row=18, column=1)

eee92 = Entry(f_2, width=13, bg = 'black', fg = 'green')
eee92.grid(row=18, column=2)

eee93 = Entry(f_2, width=13, bg = 'black', fg = 'green')
eee93.grid(row=18, column=3)

eee94 = Entry(f_2, width=13, bg = 'black', fg = 'green')
eee94.grid(row=18, column=4)
#
eee95 = Entry(f_2, width=13, bg = 'black', fg = 'green')
eee95.grid(row=19, column=0)

eee96 = Entry(f_2, width=13, bg = 'black', fg = 'green')
eee96.grid(row=19, column=1)

eee97 = Entry(f_2, width=13, bg = 'black', fg = 'green')
eee97.grid(row=19, column=2)

eee98 = Entry(f_2, width=13, bg = 'black', fg = 'green')
eee98.grid(row=19, column=3)

eee99 = Entry(f_2, width=13, bg = 'black', fg = 'green')
eee99.grid(row=19, column=4)

#370

eeee0 = Entry(f_3, width=13, bg = 'black', fg = 'green')
eeee0.grid(row=0, column=0)

eeee1 = Entry(f_3, width=13, bg = 'black', fg = 'green')
eeee1.grid(row=0, column=1)

eeee2 = Entry(f_3, width=13, bg = 'black', fg = 'green')
eeee2.grid(row=0, column=2)

eeee3 = Entry(f_3, width=13, bg = 'black', fg = 'green')
eeee3.grid(row=0, column=3)

eeee4 = Entry(f_3, width=13, bg = 'black', fg = 'green')
eeee4.grid(row=0, column=4)
#
eeee5 = Entry(f_3, width=13, bg = 'black', fg = 'green')
eeee5.grid(row=1, column=0)

eeee6 = Entry(f_3, width=13, bg = 'black', fg = 'green')
eeee6.grid(row=1, column=1)

eeee7 = Entry(f_3, width=13, bg = 'black', fg = 'green')
eeee7.grid(row=1, column=2)

eeee8 = Entry(f_3, width=13, bg = 'black', fg = 'green')
eeee8.grid(row=1, column=3)

eeee9 = Entry(f_3, width=13, bg = 'black', fg = 'green')
eeee9.grid(row=1, column=4)
#
eeee10 = Entry(f_3, width=13, bg = 'black', fg = 'green')
eeee10.grid(row=2, column=0)

eeee11 = Entry(f_3, width=13, bg = 'black', fg = 'green')
eeee11.grid(row=2, column=1)

eeee12 = Entry(f_3, width=13, bg = 'black', fg = 'green')
eeee12.grid(row=2, column=2)

eeee13 = Entry(f_3, width=13, bg = 'black', fg = 'green')
eeee13.grid(row=2, column=3)

eeee14 = Entry(f_3, width=13, bg = 'black', fg = 'green')
eeee14.grid(row=2, column=4)
#
eeee15 = Entry(f_3, width=13, bg = 'black', fg = 'green')
eeee15.grid(row=3, column=0)

eeee16 = Entry(f_3, width=13, bg = 'black', fg = 'green')
eeee16.grid(row=3, column=1)

eeee17 = Entry(f_3, width=13, bg = 'black', fg = 'green')
eeee17.grid(row=3, column=2)

eeee18 = Entry(f_3, width=13, bg = 'black', fg = 'green')
eeee18.grid(row=3, column=3)

eeee19 = Entry(f_3, width=13, bg = 'black', fg = 'green')
eeee19.grid(row=3, column=4)
#
eeee20 = Entry(f_3, width=13, bg = 'black', fg = 'green')
eeee20.grid(row=4, column=0)

eeee21 = Entry(f_3, width=13, bg = 'black', fg = 'green')
eeee21.grid(row=4, column=1)

eeee22 = Entry(f_3, width=13, bg = 'black', fg = 'green')
eeee22.grid(row=4, column=2)

eeee23 = Entry(f_3, width=13, bg = 'black', fg = 'green')
eeee23.grid(row=4, column=3)

eeee24 = Entry(f_3, width=13, bg = 'black', fg = 'green')
eeee24.grid(row=4, column=4)
#
eeee25 = Entry(f_3, width=13, bg = 'black', fg = 'green')
eeee25.grid(row=5, column=0)

eeee26 = Entry(f_3, width=13, bg = 'black', fg = 'green')
eeee26.grid(row=5, column=1)

eeee27 = Entry(f_3, width=13, bg = 'black', fg = 'green')
eeee27.grid(row=5, column=2)

eeee28 = Entry(f_3, width=13, bg = 'black', fg = 'green')
eeee28.grid(row=5, column=3)

eeee29 = Entry(f_3, width=13, bg = 'black', fg = 'green')
eeee29.grid(row=5, column=4)
#
eeee30 = Entry(f_3, width=13, bg = 'black', fg = 'green')
eeee30.grid(row=6, column=0)

eeee31 = Entry(f_3, width=13, bg = 'black', fg = 'green')
eeee31.grid(row=6, column=1)

eeee32 = Entry(f_3, width=13, bg = 'black', fg = 'green')
eeee32.grid(row=6, column=2)

eeee33 = Entry(f_3, width=13, bg = 'black', fg = 'green')
eeee33.grid(row=6, column=3)

eeee34 = Entry(f_3, width=13, bg = 'black', fg = 'green')
eeee34.grid(row=6, column=4)
#
eeee35 = Entry(f_3, width=13, bg = 'black', fg = 'green')
eeee35.grid(row=7, column=0)

eeee36 = Entry(f_3, width=13, bg = 'black', fg = 'green')
eeee36.grid(row=7, column=1)

eeee37 = Entry(f_3, width=13, bg = 'black', fg = 'green')
eeee37.grid(row=7, column=2)

eeee38 = Entry(f_3, width=13, bg = 'black', fg = 'green')
eeee38.grid(row=7, column=3)

eeee39 = Entry(f_3, width=13, bg = 'black', fg = 'green')
eeee39.grid(row=7, column=4)
#
eeee40 = Entry(f_3, width=13, bg = 'black', fg = 'green')
eeee40.grid(row=8, column=0)

eeee41 = Entry(f_3, width=13, bg = 'black', fg = 'green')
eeee41.grid(row=8, column=1)

eeee42 = Entry(f_3, width=13, bg = 'black', fg = 'green')
eeee42.grid(row=8, column=2)

eeee43 = Entry(f_3, width=13, bg = 'black', fg = 'green')
eeee43.grid(row=8, column=3)

eeee44 = Entry(f_3, width=13, bg = 'black', fg = 'green')
eeee44.grid(row=8, column=4)
#
eeee45 = Entry(f_3, width=13, bg = 'black', fg = 'green')
eeee45.grid(row=9, column=0)

eeee46 = Entry(f_3, width=13, bg = 'black', fg = 'green')
eeee46.grid(row=9, column=1)

eeee47 = Entry(f_3, width=13, bg = 'black', fg = 'green')
eeee47.grid(row=9, column=2)

eeee48 = Entry(f_3, width=13, bg = 'black', fg = 'green')
eeee48.grid(row=9, column=3)

eeee49 = Entry(f_3, width=13, bg = 'black', fg = 'green')
eeee49.grid(row=9, column=4)
#
eeee50 = Entry(f_3, width=13, bg = 'black', fg = 'green')
eeee50.grid(row=10, column=0)

eeee51 = Entry(f_3, width=13, bg = 'black', fg = 'green')
eeee51.grid(row=10, column=1)

eeee52 = Entry(f_3, width=13, bg = 'black', fg = 'green')
eeee52.grid(row=10, column=2)

eeee53 = Entry(f_3, width=13, bg = 'black', fg = 'green')
eeee53.grid(row=10, column=3)

eeee54 = Entry(f_3, width=13, bg = 'black', fg = 'green')
eeee54.grid(row=10, column=4)
#
eeee55 = Entry(f_3, width=13, bg = 'black', fg = 'green')
eeee55.grid(row=11, column=0)

eeee56 = Entry(f_3, width=13, bg = 'black', fg = 'green')
eeee56.grid(row=11, column=1)

eeee57 = Entry(f_3, width=13, bg = 'black', fg = 'green')
eeee57.grid(row=11, column=2)

eeee58 = Entry(f_3, width=13, bg = 'black', fg = 'green')
eeee58.grid(row=11, column=3)

eeee59 = Entry(f_3, width=13, bg = 'black', fg = 'green')
eeee59.grid(row=11, column=4)
#
eeee60 = Entry(f_3, width=13, bg = 'black', fg = 'green')
eeee60.grid(row=12, column=0)

eeee61 = Entry(f_3, width=13, bg = 'black', fg = 'green')
eeee61.grid(row=12, column=1)

eeee62 = Entry(f_3, width=13, bg = 'black', fg = 'green')
eeee62.grid(row=12, column=2)

eeee63 = Entry(f_3, width=13, bg = 'black', fg = 'green')
eeee63.grid(row=12, column=3)

eeee64 = Entry(f_3, width=13, bg = 'black', fg = 'green')
eeee64.grid(row=12, column=4)
#
eeee65 = Entry(f_3, width=13, bg = 'black', fg = 'green')
eeee65.grid(row=13, column=0)

eeee66 = Entry(f_3, width=13, bg = 'black', fg = 'green')
eeee66.grid(row=13, column=1)

eeee67 = Entry(f_3, width=13, bg = 'black', fg = 'green')
eeee67.grid(row=13, column=2)

eeee68 = Entry(f_3, width=13, bg = 'black', fg = 'green')
eeee68.grid(row=13, column=3)

eeee69 = Entry(f_3, width=13, bg = 'black', fg = 'green')
eeee69.grid(row=13, column=4)

#430

eeeee0 = Entry(f_4, width=13, bg = 'black', fg = 'green')
eeeee0.grid(row=0, column=0)

eeeee1 = Entry(f_4, width=13, bg = 'black', fg = 'green')
eeeee1.grid(row=0, column=1)

eeeee2 = Entry(f_4, width=13, bg = 'black', fg = 'green')
eeeee2.grid(row=0, column=2)

eeeee3 = Entry(f_4, width=13, bg = 'black', fg = 'green')
eeeee3.grid(row=0, column=3)

eeeee4 = Entry(f_4, width=13, bg = 'black', fg = 'green')
eeeee4.grid(row=0, column=4)
#
eeeee5 = Entry(f_4, width=13, bg = 'black', fg = 'green')
eeeee5.grid(row=1, column=0)

eeeee6 = Entry(f_4, width=13, bg = 'black', fg = 'green')
eeeee6.grid(row=1, column=1)

eeeee7 = Entry(f_4, width=13, bg = 'black', fg = 'green')
eeeee7.grid(row=1, column=2)

eeeee8 = Entry(f_4, width=13, bg = 'black', fg = 'green')
eeeee8.grid(row=1, column=3)

eeeee9 = Entry(f_4, width=13, bg = 'black', fg = 'green')
eeeee9.grid(row=1, column=4)
#
eeeee10 = Entry(f_4, width=13, bg = 'black', fg = 'green')
eeeee10.grid(row=2, column=0)

eeeee11 = Entry(f_4, width=13, bg = 'black', fg = 'green')
eeeee11.grid(row=2, column=1)

eeeee12 = Entry(f_4, width=13, bg = 'black', fg = 'green')
eeeee12.grid(row=2, column=2)

eeeee13 = Entry(f_4, width=13, bg = 'black', fg = 'green')
eeeee13.grid(row=2, column=3)

eeeee14 = Entry(f_4, width=13, bg = 'black', fg = 'green')
eeeee14.grid(row=2, column=4)
#
eeeee15 = Entry(f_4, width=13, bg = 'black', fg = 'green')
eeeee15.grid(row=3, column=0)

eeeee16 = Entry(f_4, width=13, bg = 'black', fg = 'green')
eeeee16.grid(row=3, column=1)

eeeee17 = Entry(f_4, width=13, bg = 'black', fg = 'green')
eeeee17.grid(row=3, column=2)

eeeee18 = Entry(f_4, width=13, bg = 'black', fg = 'green')
eeeee18.grid(row=3, column=3)

eeeee19 = Entry(f_4, width=13, bg = 'black', fg = 'green')
eeeee19.grid(row=3, column=4)
#
eeeee20 = Entry(f_4, width=13, bg = 'black', fg = 'green')
eeeee20.grid(row=4, column=0)

eeeee21 = Entry(f_4, width=13, bg = 'black', fg = 'green')
eeeee21.grid(row=4, column=1)

eeeee22 = Entry(f_4, width=13, bg = 'black', fg = 'green')
eeeee22.grid(row=4, column=2)

eeeee23 = Entry(f_4, width=13, bg = 'black', fg = 'green')
eeeee23.grid(row=4, column=3)

eeeee24 = Entry(f_4, width=13, bg = 'black', fg = 'green')
eeeee24.grid(row=4, column=4)
#
eeeee25 = Entry(f_4, width=13, bg = 'black', fg = 'green')
eeeee25.grid(row=5, column=0)

eeeee26 = Entry(f_4, width=13, bg = 'black', fg = 'green')
eeeee26.grid(row=5, column=1)

eeeee27 = Entry(f_4, width=13, bg = 'black', fg = 'green')
eeeee27.grid(row=5, column=2)

eeeee28 = Entry(f_4, width=13, bg = 'black', fg = 'green')
eeeee28.grid(row=5, column=3)

eeeee29 = Entry(f_4, width=13, bg = 'black', fg = 'green')
eeeee29.grid(row=5, column=4)
#
eeeee30 = Entry(f_4, width=13, bg = 'black', fg = 'green')
eeeee30.grid(row=6, column=0)

eeeee31 = Entry(f_4, width=13, bg = 'black', fg = 'green')
eeeee31.grid(row=6, column=1)

eeeee32 = Entry(f_4, width=13, bg = 'black', fg = 'green')
eeeee32.grid(row=6, column=2)

eeeee33 = Entry(f_4, width=13, bg = 'black', fg = 'green')
eeeee33.grid(row=6, column=3)

eeeee34 = Entry(f_4, width=13, bg = 'black', fg = 'green')
eeeee34.grid(row=6, column=4)
#
eeeee35 = Entry(f_4, width=13, bg = 'black', fg = 'green')
eeeee35.grid(row=7, column=0)

eeeee36 = Entry(f_4, width=13, bg = 'black', fg = 'green')
eeeee36.grid(row=7, column=1)

eeeee37 = Entry(f_4, width=13, bg = 'black', fg = 'green')
eeeee37.grid(row=7, column=2)

eeeee38 = Entry(f_4, width=13, bg = 'black', fg = 'green')
eeeee38.grid(row=7, column=3)

eeeee39 = Entry(f_4, width=13, bg = 'black', fg = 'green')
eeeee39.grid(row=7, column=4)
#
eeeee40 = Entry(f_4, width=13, bg = 'black', fg = 'green')
eeeee40.grid(row=8, column=0)

eeeee41 = Entry(f_4, width=13, bg = 'black', fg = 'green')
eeeee41.grid(row=8, column=1)

eeeee42 = Entry(f_4, width=13, bg = 'black', fg = 'green')
eeeee42.grid(row=8, column=2)

eeeee43 = Entry(f_4, width=13, bg = 'black', fg = 'green')
eeeee43.grid(row=8, column=3)

eeeee44 = Entry(f_4, width=13, bg = 'black', fg = 'green')
eeeee44.grid(row=8, column=4)
#
eeeee45 = Entry(f_4, width=13, bg = 'black', fg = 'green')
eeeee45.grid(row=9, column=0)

eeeee46 = Entry(f_4, width=13, bg = 'black', fg = 'green')
eeeee46.grid(row=9, column=1)

eeeee47 = Entry(f_4, width=13, bg = 'black', fg = 'green')
eeeee47.grid(row=9, column=2)

eeeee48 = Entry(f_4, width=13, bg = 'black', fg = 'green')
eeeee48.grid(row=9, column=3)

eeeee49 = Entry(f_4, width=13, bg = 'black', fg = 'green')
eeeee49.grid(row=9, column=4)
#
eeeee50 = Entry(f_4, width=13, bg = 'black', fg = 'green')
eeeee50.grid(row=10, column=0)

eeeee51 = Entry(f_4, width=13, bg = 'black', fg = 'green')
eeeee51.grid(row=10, column=1)

eeeee52 = Entry(f_4, width=13, bg = 'black', fg = 'green')
eeeee52.grid(row=10, column=2)

eeeee53 = Entry(f_4, width=13, bg = 'black', fg = 'green')
eeeee53.grid(row=10, column=3)

eeeee54 = Entry(f_4, width=13, bg = 'black', fg = 'green')
eeeee54.grid(row=10, column=4)
#
eeeee55 = Entry(f_4, width=13, bg = 'black', fg = 'green')
eeeee55.grid(row=11, column=0)

eeeee56 = Entry(f_4, width=13, bg = 'black', fg = 'green')
eeeee56.grid(row=11, column=1)

eeeee57 = Entry(f_4, width=13, bg = 'black', fg = 'green')
eeeee57.grid(row=11, column=2)

eeeee58 = Entry(f_4, width=13, bg = 'black', fg = 'green')
eeeee58.grid(row=11, column=3)

eeeee59 = Entry(f_4, width=13, bg = 'black', fg = 'green')
eeeee59.grid(row=11, column=4)

#500

eeeeee0 = Entry(f_5, width=13, bg = 'black', fg = 'green')
eeeeee0.grid(row=0, column=0)

eeeeee1 = Entry(f_5, width=13, bg = 'black', fg = 'green')
eeeeee1.grid(row=0, column=1)

eeeeee2 = Entry(f_5, width=13, bg = 'black', fg = 'green')
eeeeee2.grid(row=0, column=2)

eeeeee3 = Entry(f_5, width=13, bg = 'black', fg = 'green')
eeeeee3.grid(row=0, column=3)

eeeeee4 = Entry(f_5, width=13, bg = 'black', fg = 'green')
eeeeee4.grid(row=0, column=4)
#
eeeeee5 = Entry(f_5, width=13, bg = 'black', fg = 'green')
eeeeee5.grid(row=1, column=0)

eeeeee6 = Entry(f_5, width=13, bg = 'black', fg = 'green')
eeeeee6.grid(row=1, column=1)

eeeeee7 = Entry(f_5, width=13, bg = 'black', fg = 'green')
eeeeee7.grid(row=1, column=2)

eeeeee8 = Entry(f_5, width=13, bg = 'black', fg = 'green')
eeeeee8.grid(row=1, column=3)

eeeeee9 = Entry(f_5, width=13, bg = 'black', fg = 'green')
eeeeee9.grid(row=1, column=4)
#
eeeeee10 = Entry(f_5, width=13, bg = 'black', fg = 'green')
eeeeee10.grid(row=2, column=0)

eeeeee11 = Entry(f_5, width=13, bg = 'black', fg = 'green')
eeeeee11.grid(row=2, column=1)

eeeeee12 = Entry(f_5, width=13, bg = 'black', fg = 'green')
eeeeee12.grid(row=2, column=2)

eeeeee13 = Entry(f_5, width=13, bg = 'black', fg = 'green')
eeeeee13.grid(row=2, column=3)

eeeeee14 = Entry(f_5, width=13, bg = 'black', fg = 'green')
eeeeee14.grid(row=2, column=4)
#
eeeeee15 = Entry(f_5, width=13, bg = 'black', fg = 'green')
eeeeee15.grid(row=3, column=0)

eeeeee16 = Entry(f_5, width=13, bg = 'black', fg = 'green')
eeeeee16.grid(row=3, column=1)

eeeeee17 = Entry(f_5, width=13, bg = 'black', fg = 'green')
eeeeee17.grid(row=3, column=2)

eeeeee18 = Entry(f_5, width=13, bg = 'black', fg = 'green')
eeeeee18.grid(row=3, column=3)

eeeeee19 = Entry(f_5, width=13, bg = 'black', fg = 'green')
eeeeee19.grid(row=3, column=4)
#
eeeeee20 = Entry(f_5, width=13, bg = 'black', fg = 'green')
eeeeee20.grid(row=4, column=0)

eeeeee21 = Entry(f_5, width=13, bg = 'black', fg = 'green')
eeeeee21.grid(row=4, column=1)

eeeeee22 = Entry(f_5, width=13, bg = 'black', fg = 'green')
eeeeee22.grid(row=4, column=2)

eeeeee23 = Entry(f_5, width=13, bg = 'black', fg = 'green')
eeeeee23.grid(row=4, column=3)

eeeeee24 = Entry(f_5, width=13, bg = 'black', fg = 'green')
eeeeee24.grid(row=4, column=4)
#
eeeeee25 = Entry(f_5, width=13, bg = 'black', fg = 'green')
eeeeee25.grid(row=5, column=0)

eeeeee26 = Entry(f_5, width=13, bg = 'black', fg = 'green')
eeeeee26.grid(row=5, column=1)

eeeeee27 = Entry(f_5, width=13, bg = 'black', fg = 'green')
eeeeee27.grid(row=5, column=2)

eeeeee28 = Entry(f_5, width=13, bg = 'black', fg = 'green')
eeeeee28.grid(row=5, column=3)

eeeeee29 = Entry(f_5, width=13, bg = 'black', fg = 'green')
eeeeee29.grid(row=5, column=4)
#
eeeeee30 = Entry(f_5, width=13, bg = 'black', fg = 'green')
eeeeee30.grid(row=6, column=0)

eeeeee31 = Entry(f_5, width=13, bg = 'black', fg = 'green')
eeeeee31.grid(row=6, column=1)

eeeeee32 = Entry(f_5, width=13, bg = 'black', fg = 'green')
eeeeee32.grid(row=6, column=2)

eeeeee33 = Entry(f_5, width=13, bg = 'black', fg = 'green')
eeeeee33.grid(row=6, column=3)

eeeeee34 = Entry(f_5, width=13, bg = 'black', fg = 'green')
eeeeee34.grid(row=6, column=4)
#
eeeeee35 = Entry(f_5, width=13, bg = 'black', fg = 'green')
eeeeee35.grid(row=7, column=0)

eeeeee36 = Entry(f_5, width=13, bg = 'black', fg = 'green')
eeeeee36.grid(row=7, column=1)

eeeeee37 = Entry(f_5, width=13, bg = 'black', fg = 'green')
eeeeee37.grid(row=7, column=2)

eeeeee38 = Entry(f_5, width=13, bg = 'black', fg = 'green')
eeeeee38.grid(row=7, column=3)

eeeeee39 = Entry(f_5, width=13, bg = 'black', fg = 'green')
eeeeee39.grid(row=7, column=4)
#
eeeeee40 = Entry(f_5, width=13, bg = 'black', fg = 'green')
eeeeee40.grid(row=8, column=0)

eeeeee41 = Entry(f_5, width=13, bg = 'black', fg = 'green')
eeeeee41.grid(row=8, column=1)

eeeeee42 = Entry(f_5, width=13, bg = 'black', fg = 'green')
eeeeee42.grid(row=8, column=2)

eeeeee43 = Entry(f_5, width=13, bg = 'black', fg = 'green')
eeeeee43.grid(row=8, column=3)

eeeeee44 = Entry(f_5, width=13, bg = 'black', fg = 'green')
eeeeee44.grid(row=8, column=4)
#
eeeeee45 = Entry(f_5, width=13, bg = 'black', fg = 'green')
eeeeee45.grid(row=9, column=0)

eeeeee46 = Entry(f_5, width=13, bg = 'black', fg = 'green')
eeeeee46.grid(row=9, column=1)

eeeeee47 = Entry(f_5, width=13, bg = 'black', fg = 'green')
eeeeee47.grid(row=9, column=2)

eeeeee48 = Entry(f_5, width=13, bg = 'black', fg = 'green')
eeeeee48.grid(row=9, column=3)

eeeeee49 = Entry(f_5, width=13, bg = 'black', fg = 'green')
eeeeee49.grid(row=9, column=4)
#
eeeeee50 = Entry(f_5, width=13, bg = 'black', fg = 'green')
eeeeee50.grid(row=10, column=0)

eeeeee51 = Entry(f_5, width=13, bg = 'black', fg = 'green')
eeeeee51.grid(row=10, column=1)

eeeeee52 = Entry(f_5, width=13, bg = 'black', fg = 'green')
eeeeee52.grid(row=10, column=2)

eeeeee53 = Entry(f_5, width=13, bg = 'black', fg = 'green')
eeeeee53.grid(row=10, column=3)

eeeeee54 = Entry(f_5, width=13, bg = 'black', fg = 'green')
eeeeee54.grid(row=10, column=4)
#
eeeeee55 = Entry(f_5, width=13, bg = 'black', fg = 'green')
eeeeee55.grid(row=11, column=0)

eeeeee56 = Entry(f_5, width=13, bg = 'black', fg = 'green')
eeeeee56.grid(row=11, column=1)

eeeeee57 = Entry(f_5, width=13, bg = 'black', fg = 'green')
eeeeee57.grid(row=11, column=2)

eeeeee58 = Entry(f_5, width=13, bg = 'black', fg = 'green')
eeeeee58.grid(row=11, column=3)

eeeeee59 = Entry(f_5, width=13, bg = 'black', fg = 'green')
eeeeee59.grid(row=11, column=4)
#
eeeeee60 = Entry(f_5, width=13, bg = 'black', fg = 'green')
eeeeee60.grid(row=12, column=0)

eeeeee61 = Entry(f_5, width=13, bg = 'black', fg = 'green')
eeeeee61.grid(row=12, column=1)

eeeeee62 = Entry(f_5, width=13, bg = 'black', fg = 'green')
eeeeee62.grid(row=12, column=2)

eeeeee63 = Entry(f_5, width=13, bg = 'black', fg = 'green')
eeeeee63.grid(row=12, column=3)

eeeeee64 = Entry(f_5, width=13, bg = 'black', fg = 'green')
eeeeee64.grid(row=12, column=4)
#
eeeeee65 = Entry(f_5, width=13, bg = 'black', fg = 'green')
eeeeee65.grid(row=13, column=0)

eeeeee66 = Entry(f_5, width=13, bg = 'black', fg = 'green')
eeeeee66.grid(row=13, column=1)

eeeeee67 = Entry(f_5, width=13, bg = 'black', fg = 'green')
eeeeee67.grid(row=13, column=2)

eeeeee68 = Entry(f_5, width=13, bg = 'black', fg = 'green')
eeeeee68.grid(row=13, column=3)

eeeeee69 = Entry(f_5, width=13, bg = 'black', fg = 'green')
eeeeee69.grid(row=13, column=4)

root.mainloop()