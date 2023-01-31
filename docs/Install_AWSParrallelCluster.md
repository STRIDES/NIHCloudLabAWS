# Ways to install AWS ParrallelCluster:

    - Using a virtual environment (recommended)
    - Using a conda virtual environment 
 
 We recommend conducting all steps within AWS Cloud Shell, but you could also use a small Ec2 instance or your local machine's terminal.     

 ## 1.0 Install within pip virtual environment
 
 ## 1.1 Install pip virtual environment
 
  If virtualenv is not installed, install virtualenv using pip3

        -Linux, macOS, or Unix
      
            $ python3 -m pip install --upgrade pip
            $ python3 -m pip install --user --upgrade virtualenv
     

        -Windows
    
            $ pip3 install --user --upgrade virtualenv

 
 ### 1.2 Create a pip virtual environment and name it

         -Linux, macOS, or Unix
          
            $ python3 -m virtualenv ~/name
        

        -Windows
        
            C:\>virtualenv %USERPROFILE%\name

 ### 1.3 Activate your new virtual environment
 
        -Linux, macOS, or Unix
          
            $ source ~/name/bin/activate
        
        -Windows
        
            C:\>%USERPROFILE%\name\Scripts\activate

 ### 1.4 Install AWS ParallelCluster into your virtual environment.

        -Linux, macOS, or Unix
          
            (name)~$ python3 -m pip install --upgrade "aws-parallelcluster<3.0"
        
        -Windows
        
            (apc-ve) C:\>pip3 install --upgrade "aws-parallelcluster<3.0"

 ## 2.0 Install within conda virtual environment
 
 ### 2.1 (Optional) Install mamba
 ```
curl -L -O https://github.com/conda-forge/miniforge/releases/latest/download/Mambaforge-$(uname)-$(uname -m).sh
bash Mambaforge-$(uname)-$(uname -m).sh -b -p $HOME/mambaforge
# Add to your PATH
export PATH="$HOME/mambaforge/bin:$PATH"
```
 ### 2.2 Create environment and install parallel cluster
 `mamba create -n pcluster -c conda-forge aws-parallelcluster -y`
 
 ### 2.3 Activate environment
 ```
 source activate pcluster
 ```
 Or, using mamba activate
 ```
 mamba init
 mamba activate pcluster
 ```

 ## 4. Verify that AWS ParrallelCluster is installed correctly
               
        -Linux, macOS, or Unix
          
            $ pcluster version
        
        -Windows
        
            (apc-ve) C:\>pcluster version

    Output should display version number.

