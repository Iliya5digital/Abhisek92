def get_window(index, arr, widths): 
    if len(index) == len(arr.shape) == len(widths): 
        index = np.array(index) 
        max_indices = np.array(arr.shape) - 1 
        widths = np.array(widths) 
        win_start = index - widths 
        win_end = index + widths		
        win_start[win_start < 0] = 0 
        max_mask = win_end > max_indices 
        win_end = (max_mask * max_indices) + (~max_mask * win_end)
		# return kernel starting from win_start to win_end instead
		return  win_start, win_end