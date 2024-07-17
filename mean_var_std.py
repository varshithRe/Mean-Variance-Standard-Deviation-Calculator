import numpy as np

def calculate(list):
    if len(list) < 9:
        raise ValueError('List must contain nine numbers.')
    else:
        arr = np.array(list)
        numarr = arr.reshape(3,3)


    calculations = {
        'mean': [numarr.mean(axis =0).tolist(), numarr.mean(axis=1).tolist(), arr.mean().tolist()],
        'variance':[numarr.var(axis =0).tolist(), numarr.var(axis=1).tolist(), arr.var().tolist()],
        'standard deviation':[numarr.std(axis=0).tolist(), numarr.std(axis=1).tolist(), arr.std().tolist()],
        'max': [numarr.max(axis=0).tolist(), numarr.max(axis=1).tolist(), arr.max().tolist() ],
        'min': [numarr.min(axis=0).tolist(), numarr.min(axis=1).tolist(), arr.min().tolist()],
        'sum': [numarr.sum(axis=0).tolist(), numarr.sum(axis=1).tolist(), arr.sum().tolist()]
    }




    return calculations