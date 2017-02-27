# RandomForestScikit

This is one step in the process of ultimately creating a OpenCL Random Forest Implementation for the CMS experiment.
In this step we are looking at the performance of the random forest in python's scikit-learn on data from the EMTF.
This README is broken up into several sections: Instructions, Background, and Objectives.

Instructions
============

Installation
------------

This program has been developed with CMSSW_8_0_20. To obtain this software, obtain this CMSSW release and move into the source
directory. 

    cmsrel CMSSW_8_0_20
    cd CMSSW_8_0_20/src
    cmsenv

Then, clone this repository in the source directory and compile the CMS software.

    git clone https://github.com/bregnery/RandomForestScikit.git
    scram b
    cmsenv

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
