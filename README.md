# RandomForestWithScikit

This is one step in the process of ultimately creating a OpenCL Random Forest Implementation for the CMS experiment.
In this step we are looking at the performance of the random forest in python's scikit-learn on data from the EMTF.
This README is broken up into several sections: Instructions, Background, and Objectives.

Instructions
============

This program has been developed with CMSSW_8_0_20 on CERN's lxplus and with the University of Florida's HiPerGator.

Instructions or lxplus
----------------------

### Installation on lxplus


To obtain the dependency software, obtain a CMSSW release and move into the source directory. 

    cmsrel CMSSW_8_0_20
    cd CMSSW_8_0_20/src
    cmsenv

Then, clone this repository in the source directory and compile the CMS software.

    git clone https://github.com/bregnery/RandomForestWithScikit.git
    scram b
    cmsenv

### Creating the Machine Learning Environment on lxplus


The necessary machine learning environment can be set up with the following (from https://indico.cern.ch/event/565647/contributions/2308670/attachments/1345360/2028920/MLSoftwareStandAloneSetup__AtlasComputing__TWiki.pdf)

    cd MLstandAlone/
    sh Miniconda2-latest-Linux-x86_64.sh
    conda config --add channels https://conda.anaconda.org/NLeSC
    conda create --name=testenv root=6 python=2 mkl jupyter scipy matplotlib scikit-learn h5py rootpy root-numpy pandas
    source activate testenv
    pip install Theano
    pip install Keras
    source /cvmfs/sft.cern.ch/lcg/views/LCG_85swan3/x86_64-slc6-gcc49-opt/setup.sh

### Setting up the Machine Learning Environment on lxplus


After creating the maching learning environment on lxplus, it can be accessed during future logins with the following:

    source activate testenv
    source /cvmfs/sft.cern.ch/lcg/views/LCG_85swan3/x86_64-slc6-gcc49-opt/setup.sh

Instructions for HiPerGator
---------------------------

### Installation on the HiPerGator

To use this program on the HiPerGator, load the necessary modules and clone the repository from git.

    module load ufrc
    srundev --time=04:00:00
    git clone https://github.com/bregnery/RandomForestWithScikit.git

### Setting up the Machine Learning Environment on HiPerGator

To set up the maching learning environment on the HiPerGator, load the necessary modules and enter development mode with the following commands:

    module load ufrc
    module load root
    module load python
    srundev --time=04:00:00

Running the Flower Example
--------------------------

The flower example is explained here: http://www.agcross.com/2015/02/random-forests-in-python-with-scikit-learn/

To run the flower example, simply do:

    cd examples/
    python FlowerRF.py

Background
==========

Model Parameters
----------------

These are the random forest model parameters (as defined by Criminisi et. al 2011 p.18):

 * Forest size - inputted by the user
 * Maximum allowed tree depth (i.e. the maximum number of nodes) - inputted by the user
 * Weak learner model - binary
 * Training objective function - Error Reduction Function
 * Type of Randomness (e.g. random training data set sampling or randomized node optimization)
 * Amound of Randomness
