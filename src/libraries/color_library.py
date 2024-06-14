#Library for text colors and effects.

class Colors:
    Reset = "\033[0m"
    Bold = "\033[1m"
    Underline = "\033[4m"
    Reveresed = "\033[7m"
    
    # Text colors
    Black="\033[30m"        
    Red="\033[31m"        
    Green="\033[32m"        
    Yellow="\033[33m"     
    Blue="\033[34m"         
    Purple="\033[35m"       
    Cyan="\033[36m"         
    White="\033[37m"       
    
    # Background colors
    BG_Red="\033[41m"        
    BG_Black="\033[40m"       
    BG_Green="\033[42m"      
    BG_Yellow="\033[43m"     
    BG_Blue="\033[44m"       
    BG_Purple="\033[45m"      
    BG_Cyan="\033[46m"       
    BG_White="\033[47m"       
    
    # High Internsity
    IBlack="\033[90m"      
    IRed="\033[91m"        
    IGreen="\033[92m"      
    IYellow="\033[93m"     
    IBlue="\033[94m"       
    IPurple="\033[95m"     
    ICyan="\033[96m"       
    IWhite="\033[97m"      
    
    # Bold High Intensty
    BI_Black="\033[90m"      
    BI_Red="\033[91m"       
    BI_Green="\033[92m"      
    BI_Yellow="\033[93m"    
    BI_Blue="\033[94m"       
    BI_Purple="\033[95m"    
    BI_Cyan="\033[96m"      
    BI_White="\033[97m"     

def print_colored_text():
    print(f"{Colors.Red}This text is red{Colors.Reset}")
    print(f"{Colors.Green}This text is green{Colors.Reset}")
    

