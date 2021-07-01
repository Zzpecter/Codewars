def bouncing_ball(heigth, bounce, window):
    if heigth<0 or 0>bounce or bounce>=1 or window>=heigth:
        return -1
    else:
        count = 0
        while heigth > window:
            heigth = heigth*bounce
            count += 2 if heigth > window else 1 #bounces up
            print(heigth,bounce,window)
        return count
