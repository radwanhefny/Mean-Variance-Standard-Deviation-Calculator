import numpy as np

def calculate(List):

    if len(List) != 9:
        raise ValueError("List must contain nine numbers.")

    arr = np.array(List).reshape(3, 3)

    def to_list(x):
        return x.tolist() if isinstance(x, np.ndarray) else float(x)

    calculates = { 
        'mean': [
            to_list(np.mean(arr, axis= 0)), 
            to_list(np.mean(arr, axis= 1)), 
            to_list(np.mean(arr))
        ],
        'variance': [
            to_list(np.var(arr, axis= 0)), 
            to_list(np.var(arr, axis= 1)), 
            to_list(np.var(arr))
        ],
        'standard deviation': [
            to_list(np.std(arr, axis= 0)), 
            to_list(np.std(arr, axis= 1)), 
            to_list(np.std(arr))
        ],
        'max': [
            to_list(np.max(arr, axis= 0)), 
            to_list(np.max(arr, axis= 1)), 
            to_list(np.max(arr))
        ],
        'min': [
            to_list(np.min(arr, axis= 0)), 
            to_list(np.min(arr, axis= 1)), 
            to_list(np.min(arr))
        ],
        'sum': [
            to_list(np.sum(arr, axis= 0)), 
            to_list(np.sum(arr, axis= 1)), 
            to_list(np.sum(arr))
        ]

    }



    return calculates
