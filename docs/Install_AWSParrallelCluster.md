### Ways to install AWS ParrallelCluster:

    - Using a virtual environment (recommended)
    - Using pip

 **1.To install AWS ParallelCluster in a virtual environment:**

 If virtualenv is not installed, install virtualenv using pip3

        -Linux, macOS, or Unix
      
            $ python3 -m pip install --upgrade pip
            $ python3 -m pip install --user --upgrade virtualenv
     

        -Windows
    
            $ pip3 install --user --upgrade virtualenv
    

 **2. Create a virtual environment and name it**

         -Linux, macOS, or Unix
          
            $ python3 -m virtualenv ~/name
        

        -Windows
        
            C:\>virtualenv %USERPROFILE%\name

 **3. Activate your new virtual environment**
 
        -Linux, macOS, or Unix
          
            $ source ~/name/bin/activate
        
        -Windows
        
            C:\>%USERPROFILE%\name\Scripts\activate

 **4. Install AWS ParallelCluster into your virtual environment.**

        -Linux, macOS, or Unix
          
            (name)~$ python3 -m pip install --upgrade "aws-parallelcluster<3.0"
        
        -Windows
        
            (apc-ve) C:\>pip3 install --upgrade "aws-parallelcluster<3.0"


 **5. Verify that AWS ParrallelCluster is installed correctly**
               
        -Linux, macOS, or Unix
          
            $ pcluster version
        
        -Windows
        
            (apc-ve) C:\>pcluster version

    Output should display version number.

    
