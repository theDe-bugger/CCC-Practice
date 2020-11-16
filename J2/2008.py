

playlist = ["A","B","C","D","E"]


for i in range(1,10):
    b = int(input("Button Number: "))
    n = int(input("Number of presses: "))
    if b == 4:
        break;
    for i in range(n):
            if b == 1:
               playlist = playlist[4] + playlist[1] + playlist[2] + playlist[3] + playlist[0]
            elif b == 2:
                playlist = playlist[4] + playlist[0] + playlist[1] + playlist[2] + playlist[3] 
            elif b == 3:
                playlist = playlist[1] + playlist[0] + playlist[2] + playlist[3] + playlist[4]
            elif b == 4:
                break;
print(playlist);

        
        
