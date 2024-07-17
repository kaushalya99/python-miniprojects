from time import time  #to record time


def tperror(prompt):
    global inwords

    words = prompt.split()
    errors = 0

    for i in range(len(inwords)):
        if i in(0,len(inwords)-1):
            if inwords[i] == words[i]:
                continue
            else:
                errors = errors + 1
        else:
            if inwords[i] == words[i]:
                if(inwords[i+1] == words[i+1]) & (inwords[i-1] == words[i-1]):
                    continue
                else:
                    errors = errors + 1
            else:
                errors = errors + 1

    return errors


# calculate the speed of typing words per minutes

def speed(inprompt, stime, etime):
    global time
    global inwords

    inwords = inprompt.split()
    twords = len(inwords)
    speed = twords / time

    return speed

# calculate total elapsed time

def elapsedtime(stime,etime):
    time = etime - stime      # etime is the end time and stime is the start time
    return time


if __name__ == '__main__':
    prompt = "Python is an interpreted high-level general purpose programming language."
   # this was the paragraph which you have to type to check your speed
   print("Type this:-  ', prompt,'")

   input("Press Enter when you are ready to check your speed!!!")

   #recording time for input
   stime = time()
   inprompt = input()
   etime = time()


