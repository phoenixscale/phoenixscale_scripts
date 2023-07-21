import numpy as np

def sanity_check(array):
    if 2 in array:
        if 3 in array:
           if 4 in array:
               if 5 in array:
                   if 1 in array | 6 in array:
                       return True
                   else: return False

init = [3,4,5]
completed = 0
failed = 0
tries = 10000

for x in range(tries):
    rand_two = np.random.randint(1,7,2)
    if 2 in rand_two:
        if 1 in rand_two or 6 in rand_two:
            #print(np.concatenate((init,rand_two)), ' Good after 1')
            completed += 1
        else:
            rand_one = np.random.randint(1,7,1)
            if 1 in rand_one or 6 in rand_one:
                #print(np.concatenate((init, [2],rand_one)), ' Good after 2 with one')
                completed += 1
            else: failed+=1
    else:
        if 1 in rand_two:
            rand_one = np.random.randint(1, 7, 1)
            if 2 in rand_one:
                #print(np.concatenate((init, [1], rand_one)), ' Good after 2 with one')
                completed += 1
            else: failed +=1
        elif 6 in rand_two:
            rand_one = np.random.randint(1, 7, 1)
            if 2 in rand_one:
                #print(np.concatenate((init, [6], rand_one)), ' Good after 2 with one')
                completed += 1
            else: failed += 1
        else:
            rand_two = np.random.randint(1,7,2)
            if 2 in rand_two:
                if 1 in rand_two or 6 in rand_two:
                    #print(np.concatenate((init, rand_two)), ' Good after 2 with none')
                    completed += 1
                else:
                    failed += 1
            else:
                #print(np.concatenate((init,rand_two)), ' Bad after 2')
                failed+=1

print(completed, '/', tries)
print(failed, '/', tries)
print((completed*100)/tries, ' percent pass rerolling two')
print((1-(25/36))*100, ' percent pass rerolling one')
