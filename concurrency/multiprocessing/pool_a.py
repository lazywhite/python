import multiprocessing 

def do_cal(data):
    return data*2
    

def  start_process():
    print('starting',multiprocessing.current_process().name)

inputs = list(range(38))
print('Inputs: ',inputs)

pool_size = multiprocessing.cpu_count() * 2

#pool=multiprocessing.Pool(processes=pool_size, initializer=start_process)
pool=multiprocessing.Pool(processes=pool_size, initializer=start_process,
                        maxtasksperchild=2)

pool_output = pool.map(do_cal, inputs)

pool.close()
pool.join()

print('Pool output: ',pool_output)

