############################################ 
# Creates an empty local config file.      #
# Includes dev, test, prod environments.   #
############################################

def create_local_config():
    f = open("config.local", 'w')
    new_file_contents = \
        "##########################################\n" + \
        "# Local config file, use it to configure #\n" + \
        "# any extra local configuration details, #\n" + \
        "# or to overwrite any default ones. This #\n" + \
        "# file is ignored from version control.  #\n" + \
        "##########################################\n" + \
        "\n" + \
        "[dev]\n" + \
        "\n" + \
        "[test]\n" + \
        "\n" + \
        "[prod]"
    f.write(new_file_contents)
    
if __name__ == "__main__":
    create_local_config()