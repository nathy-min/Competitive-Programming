def wrap(string, max_width):
    size = len(string)
    if size < max_width:
        return string
    left = 0
    right = max_width  
    result_str = ''
    while right < size:
        result_str += string[left:right] + '\n'
        right += max_width
        left += max_width
    if right != size :
        result_str += string[left:size]   
        
    return result_str
