import os 


def append(): 
    cwd = os.getcwd()
    os.chdir(cwd)
    append_this = input("Input words to be appended: ")

    for _, current_name in enumerate(os.listdir(cwd)):
        
        #get filename only 
        filename = os.path.splitext(current_name)[0]
        extension = os.path.splitext(current_name)[1]

        if filename == "main" and extension == ".py": continue 

        
        #modify new filename 
        result = filename + append_this + extension

        #rename 
        os.rename(current_name, result)
        

    print("===== Success ! =====")



def switcher(i):
    switcher = {
        "1": append,
        # "2": replace,
    }
    
    func = switcher.get(i, lambda: "Invalid")
    return func()
  

if __name__ == '__main__':
    s = f"""
        # NOTE: this script will rename all files inside current directory. Run this script inside folder containing all the files you want to change
        
        {'-' * 60}
        # How to use : 
            1. select option available
            2. follow the instructions on the screen
        {'-' * 60}
        
        {'-' * 60}
        # Options:
        #   1. append words into filename
        {'-' * 60}
        """
    
    print(s)
    s_input = input("Enter the number of your option: ")
    switcher(s_input)
