#❌


row1 = ["⬜","⬜","⬜"]
row2 = ["⬜","⬜","⬜"]
row3 = ["⬜","⬜","⬜"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}\n")
position = input("Where do you want to put the treasure")

horizontal = int(position[0])
vertical = int(position[1])

row_selection=map[vertical-1]
row_selection[horizontal-1]='❌'
print(f"{row1}\n{row2}\n{row3}\n")
# if position==11:
#     row1[0]='❌'
# elif position==12:
#     row1[1]='❌'
# elif position==13:
#     row1[2]='❌'
# elif position==21:
#     row2[0]='❌'
# elif position==22:
#     row2[1]='❌'
# elif position==23:
#     row2[2]='❌'
# elif position==31:
#     row3[0]='❌'
# elif position==32:
#     row3[1]='❌'        
# elif position==33:
#     row3[2]='❌'
# print(f"{row1}\n{row2}\n{row3}\n")