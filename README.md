# RandomForestWithScikit

This is one step in the process of ultimately creating a OpenCL Random Forest Implementation for the CMS experiment.
In this step we are looking at the performance of the random forest in python's scikit-learn on data from the EMTF.
This README is broken up into several sections: Instructions, Background, and Objectives.

Instructions
============

Installation
------------

This program has been developed with CMSSW_8_0_20 on CERN's lxplus. To obtain this software, obtain this CMSSW release and move into the source directory. 

    cmsrel CMSSW_8_0_20
    cd CMSSW_8_0_20/src
    cmsenv

Then, clone this repository in the source directory and compile the CMS software.

    git clone https://github.com/bregnery/RandomForestWithScikit.git
    scram b
    cmsenv

Setting up the Machine Learning Environment on lxplus
-----------------------------------------------------

The necessary machine learning environment can be set up with the following (from https://indico.cern.ch/event/565647/contributions/2308670/attachments/1345360/2028920/MLSoftwareStandAloneSetup__AtlasComputing__TWiki.pdf)

    cd MLstandAlone/
    sh Miniconda2-latest-Linux-x86_64.sh
    conda config --add channels https://conda.anaconda.org/NLeSC
    conda create --name=testenv root=6 python=2 mkl jupyter scipy matplotlib scikit-learn h5py rootpy root-numpy pandas
    source activate testenv
    pip install Theano
    pip install Keras
    source /cvmfs/sft.cern.ch/lcg/views/LCG_85swan3/x86_64-slc6-gcc49-opt/setup.sh

Running an Example
------------------

Once an example is created, directions for running it will be included here.

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
