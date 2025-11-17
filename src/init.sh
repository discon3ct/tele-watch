#!/bin/bash
  2 
  3 ######################################################
  4 # This Python script is used to start                #
  5 # tele_watch.py within a defined virtual             #
  6 # environment. After the process is strarted         #
  7 # tele_watch.py will stay running in the background  #
  8 # due to the use of the "nohup" command.             #
  9 ######################################################
 10 
 11 VENV_PATH=$VENV_PATH
 12 SCRIPT_PATH=$TELE_SCRIPT_PATH
 13 
 14 source "$VENV_PATH/bin/activate"
 15 
 16 # Test if venv activated
 17 if [ $? -eq 0 ]; then
 18     echo "#### venv started ####"
 19 else
 20     "#### Failed to start venv ####"
 21     exit 1
 22 fi
 23 
 24 # Allow term to be killed and still run program in background
 25 nohup python3 "$SCRIPT_PATH" &
