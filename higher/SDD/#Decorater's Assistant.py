#Decorater's Assistant

#subroutines
def get_user_inputs():
    l = int(input("enter length in m: "))
    b = int(input("enter breadth in m: "))
    h = int(input("enter height in m: "))
    return l, b, h

def get_areas():
    FloorArea = length*breadth
    WallArea = height*breadth*2 + height*length*2
    return FloorArea, WallArea

def get_stuff():
    Tiles = floor_area/4
    Wallpaper = wall_area/10
    Paint = ceiling_paint = floor_area/2
    return Tiles, Wallpaper, Paint

#main program
length, breadth, height = get_user_inputs()
floor_area, wall_area = get_areas(length, breadth, height)
carpet_tiles, wallpaper_rolls, ceiling_paint = get_stuff(floor_area, wall_area)


print("you need ",carpet_tiles," carpet tiles, ",wallpaper_rolls," wallpaper rolls and ",ceiling_paint,"L of paint.")
