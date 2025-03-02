﻿#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.2.3),
    on March 07, 2022, at 17:43
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard

#for our own functions we need these specified in the global space 
#// so these are defined in the "Before experiment" tab
#// linspace (this will be used in place of numpy.linspace for picking ISI)

#function linspace(a,b,n) {
#    if(typeof n === "undefined") n = Math.max(Math.round(b-a)+1,1);
#    if(n<2) { return n===1?[a]:[]; }
#    var i,ret = Array(n);
#    n--;
#    for(i=n;i>=0;i--) { ret[i] = (i*b+(n-i)*a)/n; }
#    return ret;
#}
import serial
import time
import threading

def ReadThread(port):
    while Connected:
        if port.inWaiting() > 0:
            print ("0x%X"%ord(port.read(1)))

port = serial.Serial('COM3')            
PulseWidth = 0.002


# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2021.2.3'
expName = 'multiEF-Inhib'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\NDClab\\Desktop\\social-context-eeg\\Multi_EF_with_ALL_triggers_faster\\Multi_EF_with_ALL_triggers\\multi-ef-o_s1_r2_e1-EEG-Inhib-Task_faster_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.DEBUG)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=[1920, 1080], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Setup eyetracking
ioDevice = ioConfig = ioSession = ioServer = eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "jsCode"
jsCodeClock = core.Clock()
#// shuffle is push in JS so defining shuffle for our JS experiment code
#shuffle = util.shuffle;

# Initialize components for Routine "beginInstruct"
beginInstructClock = core.Clock()
begin_text1 = visual.TextStim(win=win, name='begin_text1',
    text='Welcome to BRAIN GAMES!\n\nHere, you will play a series of computer games.\n\nEach game will involve a set of 5 images being flashed on the screen, similar to the set below:',
    font='Arial',
    pos=(0, .35), height=.025, wrapWidth=23, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
#1
Connected = True
thread = threading.Thread(target=ReadThread, args=(port,))
thread.start()
port.write([0xFF])
time.sleep(PulseWidth)

pracImage_center = visual.ImageStim(
    win=win,
    name='pracImage_center', 
    image='images/2M2_Sc_BD.jpg', mask=None,
    ori=0, pos=(0, 0), size=(.1, .1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-2.0)
pracImage_top = visual.ImageStim(
    win=win,
    name='pracImage_top', 
    image='images/2M2_Sc_BD.jpg', mask=None,
    ori=0, pos=(0, .18), size=(.1, .1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-3.0)
pracImage_right = visual.ImageStim(
    win=win,
    name='pracImage_right', 
    image='images/2M2_Sc_BD.jpg', mask=None,
    ori=0, pos=(.18, 0), size=(.1, .1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-4.0)
pracImage_bottom = visual.ImageStim(
    win=win,
    name='pracImage_bottom', 
    image='images/2M2_Sc_BD.jpg', mask=None,
    ori=0, pos=(0, -.18), size=(.1, .1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-5.0)
pracImage_left = visual.ImageStim(
    win=win,
    name='pracImage_left', 
    image='images/2M2_Sc_BD.jpg', mask=None,
    ori=0, pos=(-.18, 0), size=(.1, .1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-6.0)
begin_keyResp = keyboard.Keyboard()
#1

Connected = True
#Start the read thread
thread = threading.Thread(target=ReadThread, args=(port,))
thread.start()


begin_text2 = visual.TextStim(win=win, name='begin_text2',
    text='Sometimes the images flashed on the screen will all be the same (like the set of images above).\n\nPress the left or right button to continue',
    font='Arial',
    pos=(0, -.35), height=.025, wrapWidth=23, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-9.0);

# Initialize components for Routine "beginInstruct_2a"
beginInstruct_2aClock = core.Clock()
begin_text1_4 = visual.TextStim(win=win, name='begin_text1_4',
    text='Sometimes the images flashed on the screen will differ\nin their color or shape (like the set of images below).\n',
    font='Arial',
    pos=(0, .35), height=.025, wrapWidth=23, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
pracImage_center_2 = visual.ImageStim(
    win=win,
    name='pracImage_center_2', 
    image='images/2M2_Sc_OD.jpg', mask=None,
    ori=315, pos=(0, 0), size=(.1, .1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-1.0)
pracImage_top_2 = visual.ImageStim(
    win=win,
    name='pracImage_top_2', 
    image='images/2M2_Sc_BD.jpg', mask=None,
    ori=0, pos=(0, .18), size=(.1, .1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-2.0)
pracImage_right_2 = visual.ImageStim(
    win=win,
    name='pracImage_right_2', 
    image='images/2M2_Sc_BD.jpg', mask=None,
    ori=0, pos=(.18, 0), size=(.1, .1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-3.0)
pracImage_bottom_2 = visual.ImageStim(
    win=win,
    name='pracImage_bottom_2', 
    image='images/2M2_Sc_BD.jpg', mask=None,
    ori=0, pos=(0, -.18), size=(.1, .1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-4.0)
pracImage_left_2 = visual.ImageStim(
    win=win,
    name='pracImage_left_2', 
    image='images/2M2_Sc_BD.jpg', mask=None,
    ori=0, pos=(-.18, 0), size=(.1, .1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-5.0)
begin_keyResp_4 = keyboard.Keyboard()
begin_text2_4 = visual.TextStim(win=win, name='begin_text2_4',
    text='However, you only need to respond to the central image and should ignore the rest.\n\n\n\nPress the left or right button to continue',
    font='Arial',
    pos=(0, -.35), height=.025, wrapWidth=23, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-7.0);

# Initialize components for Routine "beginInstruct_3a"
beginInstruct_3aClock = core.Clock()
begin_text1_3a = visual.TextStim(win=win, name='begin_text1_3a',
    text="The rules for how to you should respond to central image\nwill be different in each game you play today. \n\nBefore each game starts, you will be informed of the game's\nrules and be given a chance to practice before playing the \nreal game.\n\nAre you ready to learn about the first game?",
    font='Arial',
    pos=(0, 0), height=.025, wrapWidth=23, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
begin_text2_3a = visual.TextStim(win=win, name='begin_text2_3a',
    text='Press the left or right button to continue',
    font='Arial',
    pos=(0, -.3), height=.025, wrapWidth=23, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
begin_keyResp_3a = keyboard.Keyboard()

# Initialize components for Routine "task_instruct"
task_instructClock = core.Clock()
taskName = visual.TextStim(win=win, name='taskName',
    text='',
    font='Arial',
    pos=(0, .387), height=.035, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
task_Text = visual.TextStim(win=win, name='task_Text',
    text='',
    font='Arial',
    pos=(0, .141), height=.025, wrapWidth=22, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
leftKey_text = visual.TextStim(win=win, name='leftKey_text',
    text='',
    font='Arial',
    pos=(0, .106), height=.025, wrapWidth=22, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
rightKey_text = visual.TextStim(win=win, name='rightKey_text',
    text='',
    font='Arial',
    pos=(0, .141), height=.025, wrapWidth=22, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
task_text5 = visual.TextStim(win=win, name='task_text5',
    text='Press the left or right button to continue',
    font='Arial',
    pos=(0, -.35), height=.025, wrapWidth=22, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);
LeftReminder_text = visual.TextStim(win=win, name='LeftReminder_text',
    text='',
    font='Arial',
    pos=(-.45, -.45), height=.035, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-6.0);
rightReminder_text = visual.TextStim(win=win, name='rightReminder_text',
    text='',
    font='Arial',
    pos=(.45, -.45), height=.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-7.0);
pracOrMain_keyResp = keyboard.Keyboard()

# Initialize components for Routine "task_instruct2"
task_instruct2Clock = core.Clock()
taskName_2 = visual.TextStim(win=win, name='taskName_2',
    text='',
    font='Arial',
    pos=(0, .176), height=.035, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
task_Text_2 = visual.TextStim(win=win, name='task_Text_2',
    text='',
    font='Arial',
    pos=(0, 0), height=.025, wrapWidth=22, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
task_text_3 = visual.TextStim(win=win, name='task_text_3',
    text='',
    font='Arial',
    pos=(0, 0), height=.025, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
task_text_4 = visual.TextStim(win=win, name='task_text_4',
    text='',
    font='Arial',
    pos=(0, 0), height=.025, wrapWidth=22, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
LeftReminder_text_5 = visual.TextStim(win=win, name='LeftReminder_text_5',
    text='',
    font='Arial',
    pos=(-.45, -.45), height=.035, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);
rightReminder_text_5 = visual.TextStim(win=win, name='rightReminder_text_5',
    text='',
    font='Arial',
    pos=(.45, -.45), height=.035, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-6.0);
pracOrMain_keyResp_3 = keyboard.Keyboard()

# Initialize components for Routine "prac_cueRoutine"
prac_cueRoutineClock = core.Clock()
reminderDur = 500
LeftReminder_text_6 = visual.TextStim(win=win, name='LeftReminder_text_6',
    text='',
    font='Arial',
    pos=(-.45, -.45), height=.035, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
rightReminder_text_6 = visual.TextStim(win=win, name='rightReminder_text_6',
    text='',
    font='Arial',
    pos=(.45, -.45), height=.035, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
cuePresented_2 = visual.TextStim(win=win, name='cuePresented_2',
    text='',
    font='Arial',
    pos=(0, 0), height=.035, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
#1

Connected = True

#Start the read thread
thread = threading.Thread(target=ReadThread, args=(port,))
thread.start()
#port.write([0xFF])



# Initialize components for Routine "break_prac_cueLoop"
break_prac_cueLoopClock = core.Clock()

# Initialize components for Routine "prac_StimRoutine"
prac_StimRoutineClock = core.Clock()
#possible cb:
#BSOD
#BDOS
#ODBS
#OSBD

#hard-coded counterbalance for now. will update
#to change based on user input
CB = 'BSOD'

if CB =='BSOD':
    blueKey = '1'
    squareKey = '1'
    orangeKey = '8'
    diagKey = '8'   
elif CB =='BDOS':
    blueKey = '1'
    squareKey = '8'
    orangeKey = '8'
    diagKey = '1'
elif CB =='ODBS':
    blueKey = '8'
    squareKey = '8'
    orangeKey = '1'
    diagKey = '1'
elif CB =='OSBD':
    blueKey = '8'
    squareKey = 'z'
    orangeKey = 'z'
    diagKey = '8'

LeftReminder_text_7 = visual.TextStim(win=win, name='LeftReminder_text_7',
    text='',
    font='Arial',
    pos=(-.45, -.45), height=.035, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
rightReminder_text_7 = visual.TextStim(win=win, name='rightReminder_text_7',
    text='',
    font='Arial',
    pos=(.45, -.45), height=.035, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
centerPresented_2 = visual.ImageStim(
    win=win,
    name='centerPresented_2', 
    image='sin', mask=None,
    ori=1.0, pos=(0, 0), size=(.1, .1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-4.0)
topPresented_2 = visual.ImageStim(
    win=win,
    name='topPresented_2', 
    image='sin', mask=None,
    ori=1.0, pos=(0, .18), size=(.1, .1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-5.0)
rightPresented_2 = visual.ImageStim(
    win=win,
    name='rightPresented_2', 
    image='sin', mask=None,
    ori=1.0, pos=(.18, 0), size=(.1, .1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-6.0)
bottomPresented_2 = visual.ImageStim(
    win=win,
    name='bottomPresented_2', 
    image='sin', mask=None,
    ori=1.0, pos=(0, -.18), size=(.1, .1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-7.0)
leftPresented_2 = visual.ImageStim(
    win=win,
    name='leftPresented_2', 
    image='sin', mask=None,
    ori=1.0, pos=(-.18, 0), size=(.1, .1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-8.0)
#1
Connected = True

#Start the read thread
thread = threading.Thread(target=ReadThread, args=(port,))
thread.start()



keyResp_2 = keyboard.Keyboard()
#1

Connected = True

#Start the read thread
thread = threading.Thread(target=ReadThread, args=(port,))
thread.start()




# Initialize components for Routine "break_prac_stimLoop"
break_prac_stimLoopClock = core.Clock()
#back1_rotCenter = 999
#back1_blueCenter = 999

#back2_rotCenter = 999
#back2_blueCenter = 999

# Initialize components for Routine "taskEnd_instruct"
taskEnd_instructClock = core.Clock()
taskEnd_text = visual.TextStim(win=win, name='taskEnd_text',
    text='',
    font='Arial',
    pos=(0, 0), height=0.025, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
key_resp = keyboard.Keyboard()

# Initialize components for Routine "task_instruct"
task_instructClock = core.Clock()
taskName = visual.TextStim(win=win, name='taskName',
    text='',
    font='Arial',
    pos=(0, .387), height=.035, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
task_Text = visual.TextStim(win=win, name='task_Text',
    text='',
    font='Arial',
    pos=(0, .141), height=.025, wrapWidth=22, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
leftKey_text = visual.TextStim(win=win, name='leftKey_text',
    text='',
    font='Arial',
    pos=(0, .106), height=.025, wrapWidth=22, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
rightKey_text = visual.TextStim(win=win, name='rightKey_text',
    text='',
    font='Arial',
    pos=(0, .141), height=.025, wrapWidth=22, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
task_text5 = visual.TextStim(win=win, name='task_text5',
    text='Press the left or right button to continue',
    font='Arial',
    pos=(0, -.35), height=.025, wrapWidth=22, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);
LeftReminder_text = visual.TextStim(win=win, name='LeftReminder_text',
    text='',
    font='Arial',
    pos=(-.45, -.45), height=.035, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-6.0);
rightReminder_text = visual.TextStim(win=win, name='rightReminder_text',
    text='',
    font='Arial',
    pos=(.45, -.45), height=.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-7.0);
pracOrMain_keyResp = keyboard.Keyboard()

# Initialize components for Routine "task_instruct2"
task_instruct2Clock = core.Clock()
taskName_2 = visual.TextStim(win=win, name='taskName_2',
    text='',
    font='Arial',
    pos=(0, .176), height=.035, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
task_Text_2 = visual.TextStim(win=win, name='task_Text_2',
    text='',
    font='Arial',
    pos=(0, 0), height=.025, wrapWidth=22, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
task_text_3 = visual.TextStim(win=win, name='task_text_3',
    text='',
    font='Arial',
    pos=(0, 0), height=.025, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
task_text_4 = visual.TextStim(win=win, name='task_text_4',
    text='',
    font='Arial',
    pos=(0, 0), height=.025, wrapWidth=22, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
LeftReminder_text_5 = visual.TextStim(win=win, name='LeftReminder_text_5',
    text='',
    font='Arial',
    pos=(-.45, -.45), height=.035, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);
rightReminder_text_5 = visual.TextStim(win=win, name='rightReminder_text_5',
    text='',
    font='Arial',
    pos=(.45, -.45), height=.035, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-6.0);
pracOrMain_keyResp_3 = keyboard.Keyboard()

# Initialize components for Routine "cueRoutine"
cueRoutineClock = core.Clock()
reminderDur = 500
LeftReminder_text_3 = visual.TextStim(win=win, name='LeftReminder_text_3',
    text='',
    font='Arial',
    pos=(-.45, -.45), height=.035, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
rightReminder_text_3 = visual.TextStim(win=win, name='rightReminder_text_3',
    text='',
    font='Arial',
    pos=(.45, -.45), height=.035, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
cuePresented = visual.TextStim(win=win, name='cuePresented',
    text='',
    font='Arial',
    pos=(0, 0), height=.035, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
#1
import serial
import time
import threading
Connected = True
def ReadThread(port):
    while Connected:
        if port.inWaiting() > 0:
            print ("0x%X"%ord(port.read(1)))
#port = serial.Serial('COM3')
#Start the read thread
thread = threading.Thread(target=ReadThread, args=(port,))
thread.start()
port.write([0xFF])



# Initialize components for Routine "break_cueLoop"
break_cueLoopClock = core.Clock()

# Initialize components for Routine "StimRoutine"
StimRoutineClock = core.Clock()
#possible cb:
#BSOD
#BDOS
#ODBS
#OSBD

#hard-coded counterbalance for now. will update
#to change based on user input
CB = 'BSOD'

if CB =='BSOD':
    blueKey = '1'
    squareKey = '1'
    orangeKey = '8'
    diagKey = '8'   
elif CB =='BDOS':
    blueKey = '1'
    squareKey = '8'
    orangeKey = '8'
    diagKey = '1'
elif CB =='ODBS':
    blueKey = '8'
    squareKey = '8'
    orangeKey = '1'
    diagKey = '1'
elif CB =='OSBD':
    blueKey = '8'
    squareKey = '1'
    orangeKey = '1'
    diagKey = '8'

LeftReminder_text_4 = visual.TextStim(win=win, name='LeftReminder_text_4',
    text='',
    font='Arial',
    pos=(-.45, -.45), height=.035, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
rightReminder_text_4 = visual.TextStim(win=win, name='rightReminder_text_4',
    text='',
    font='Arial',
    pos=(.45, -.45), height=.035, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
centerPresented = visual.ImageStim(
    win=win,
    name='centerPresented', 
    image='sin', mask=None,
    ori=1.0, pos=(0, 0), size=(.1, .1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-4.0)
topPresented = visual.ImageStim(
    win=win,
    name='topPresented', 
    image='sin', mask=None,
    ori=1.0, pos=(0, .18), size=(.1, .1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-5.0)
rightPresented = visual.ImageStim(
    win=win,
    name='rightPresented', 
    image='sin', mask=None,
    ori=1.0, pos=(.18, 0), size=(.1, .1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-6.0)
bottomPresented = visual.ImageStim(
    win=win,
    name='bottomPresented', 
    image='sin', mask=None,
    ori=1.0, pos=(0, -.18), size=(.1, .1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-7.0)
leftPresented = visual.ImageStim(
    win=win,
    name='leftPresented', 
    image='sin', mask=None,
    ori=1.0, pos=(-.18, 0), size=(.1, .1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-8.0)
#1
Connected = True

#Start the read thread
thread = threading.Thread(target=ReadThread, args=(port,))
thread.start()



keyResp = keyboard.Keyboard()
#1

Connected = True

#Start the read thread
thread = threading.Thread(target=ReadThread, args=(port,))
thread.start()




# Initialize components for Routine "break_stimLoop"
break_stimLoopClock = core.Clock()
#back1_rotCenter = 999
#back1_blueCenter = 999

#back2_rotCenter = 999
#back2_blueCenter = 999

# Initialize components for Routine "restBreak"
restBreakClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='',
    font='Arial',
    pos=(0, 0), height=1.0, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
key_resp_3 = keyboard.Keyboard()

# Initialize components for Routine "taskEnd_instruct"
taskEnd_instructClock = core.Clock()
taskEnd_text = visual.TextStim(win=win, name='taskEnd_text',
    text='',
    font='Arial',
    pos=(0, 0), height=0.025, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
key_resp = keyboard.Keyboard()

# Initialize components for Routine "expEnd_intruct"
expEnd_intructClock = core.Clock()
taskEnd_text_2 = visual.TextStim(win=win, name='taskEnd_text_2',
    text='',
    font='Arial',
    pos=(0, 0), height=0.025, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_2 = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "jsCode"-------
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
jsCodeComponents = []
for thisComponent in jsCodeComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
jsCodeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "jsCode"-------
while continueRoutine:
    # get current time
    t = jsCodeClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=jsCodeClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in jsCodeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "jsCode"-------
for thisComponent in jsCodeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "jsCode" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "beginInstruct"-------
continueRoutine = True
# update component parameters for each repeat
#2
pulse_started = False
pulse_ended = False


begin_keyResp.keys = []
begin_keyResp.rt = []
_begin_keyResp_allKeys = []
#2
mark_started = False
mark_ended = False

# keep track of which components have finished
beginInstructComponents = [begin_text1, pracImage_center, pracImage_top, pracImage_right, pracImage_bottom, pracImage_left, begin_keyResp, begin_text2]
for thisComponent in beginInstructComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
beginInstructClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "beginInstruct"-------
while continueRoutine:
    # get current time
    t = beginInstructClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=beginInstructClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *begin_text1* updates
    if begin_text1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        begin_text1.frameNStart = frameN  # exact frame index
        begin_text1.tStart = t  # local t and not account for scr refresh
        begin_text1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(begin_text1, 'tStartRefresh')  # time at next scr refresh
        begin_text1.setAutoDraw(True)
    #3
    if begin_text1.status == STARTED and not pulse_started:
        port.write([0x01])
        time.sleep(PulseWidth)
        pulse_start_time = globalClock.getTime()
        pulse_started = True
    if pulse_started and not pulse_ended:
        if globalClock.getTime() - pulse_start_time >= 0.005:
            #port.write([0x01])
            pulse_ended = True
    
    
    # *pracImage_center* updates
    if pracImage_center.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        pracImage_center.frameNStart = frameN  # exact frame index
        pracImage_center.tStart = t  # local t and not account for scr refresh
        pracImage_center.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(pracImage_center, 'tStartRefresh')  # time at next scr refresh
        pracImage_center.setAutoDraw(True)
    
    # *pracImage_top* updates
    if pracImage_top.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        pracImage_top.frameNStart = frameN  # exact frame index
        pracImage_top.tStart = t  # local t and not account for scr refresh
        pracImage_top.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(pracImage_top, 'tStartRefresh')  # time at next scr refresh
        pracImage_top.setAutoDraw(True)
    
    # *pracImage_right* updates
    if pracImage_right.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        pracImage_right.frameNStart = frameN  # exact frame index
        pracImage_right.tStart = t  # local t and not account for scr refresh
        pracImage_right.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(pracImage_right, 'tStartRefresh')  # time at next scr refresh
        pracImage_right.setAutoDraw(True)
    
    # *pracImage_bottom* updates
    if pracImage_bottom.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        pracImage_bottom.frameNStart = frameN  # exact frame index
        pracImage_bottom.tStart = t  # local t and not account for scr refresh
        pracImage_bottom.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(pracImage_bottom, 'tStartRefresh')  # time at next scr refresh
        pracImage_bottom.setAutoDraw(True)
    
    # *pracImage_left* updates
    if pracImage_left.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        pracImage_left.frameNStart = frameN  # exact frame index
        pracImage_left.tStart = t  # local t and not account for scr refresh
        pracImage_left.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(pracImage_left, 'tStartRefresh')  # time at next scr refresh
        pracImage_left.setAutoDraw(True)
    
    # *begin_keyResp* updates
    waitOnFlip = False
    if begin_keyResp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        begin_keyResp.frameNStart = frameN  # exact frame index
        begin_keyResp.tStart = t  # local t and not account for scr refresh
        begin_keyResp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(begin_keyResp, 'tStartRefresh')  # time at next scr refresh
        begin_keyResp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(begin_keyResp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(begin_keyResp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if begin_keyResp.status == STARTED and not waitOnFlip:
        theseKeys = begin_keyResp.getKeys(keyList=['1', '8'], waitRelease=False)
        _begin_keyResp_allKeys.extend(theseKeys)
        if len(_begin_keyResp_allKeys):
            begin_keyResp.keys = _begin_keyResp_allKeys[-1].name  # just the last key pressed
            begin_keyResp.rt = _begin_keyResp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    #3
    if begin_keyResp.keys == 'space' and not mark_started:
        port.write([0x10])
        time.sleep(PulseWidth)
        mark_start_time = globalClock.getTime()
        mark_started = True
    if mark_started and not mark_ended:
        if globalClock.getTime() - mark_start_time >= 0.4:
            #port.write([0x32])
            mark_ended = True
    
    
    # *begin_text2* updates
    if begin_text2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        begin_text2.frameNStart = frameN  # exact frame index
        begin_text2.tStart = t  # local t and not account for scr refresh
        begin_text2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(begin_text2, 'tStartRefresh')  # time at next scr refresh
        begin_text2.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in beginInstructComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "beginInstruct"-------
for thisComponent in beginInstructComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('begin_text1.started', begin_text1.tStartRefresh)
thisExp.addData('begin_text1.stopped', begin_text1.tStopRefresh)
#4
#port.write([0xFF])
Connected = False
thread.join(1.0)

thisExp.addData('pracImage_center.started', pracImage_center.tStartRefresh)
thisExp.addData('pracImage_center.stopped', pracImage_center.tStopRefresh)
thisExp.addData('pracImage_top.started', pracImage_top.tStartRefresh)
thisExp.addData('pracImage_top.stopped', pracImage_top.tStopRefresh)
thisExp.addData('pracImage_right.started', pracImage_right.tStartRefresh)
thisExp.addData('pracImage_right.stopped', pracImage_right.tStopRefresh)
thisExp.addData('pracImage_bottom.started', pracImage_bottom.tStartRefresh)
thisExp.addData('pracImage_bottom.stopped', pracImage_bottom.tStopRefresh)
thisExp.addData('pracImage_left.started', pracImage_left.tStartRefresh)
thisExp.addData('pracImage_left.stopped', pracImage_left.tStopRefresh)
# check responses
if begin_keyResp.keys in ['', [], None]:  # No response was made
    begin_keyResp.keys = None
thisExp.addData('begin_keyResp.keys',begin_keyResp.keys)
if begin_keyResp.keys != None:  # we had a response
    thisExp.addData('begin_keyResp.rt', begin_keyResp.rt)
thisExp.addData('begin_keyResp.started', begin_keyResp.tStartRefresh)
thisExp.addData('begin_keyResp.stopped', begin_keyResp.tStopRefresh)
thisExp.nextEntry()
#4
port.write([0xFF])
time.sleep(PulseWidth)
Connected = False
thread.join(1.0)

thisExp.addData('begin_text2.started', begin_text2.tStartRefresh)
thisExp.addData('begin_text2.stopped', begin_text2.tStopRefresh)
# the Routine "beginInstruct" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "beginInstruct_2a"-------
continueRoutine = True
# update component parameters for each repeat
begin_keyResp_4.keys = []
begin_keyResp_4.rt = []
_begin_keyResp_4_allKeys = []
# keep track of which components have finished
beginInstruct_2aComponents = [begin_text1_4, pracImage_center_2, pracImage_top_2, pracImage_right_2, pracImage_bottom_2, pracImage_left_2, begin_keyResp_4, begin_text2_4]
for thisComponent in beginInstruct_2aComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
beginInstruct_2aClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "beginInstruct_2a"-------
while continueRoutine:
    # get current time
    t = beginInstruct_2aClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=beginInstruct_2aClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *begin_text1_4* updates
    if begin_text1_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        begin_text1_4.frameNStart = frameN  # exact frame index
        begin_text1_4.tStart = t  # local t and not account for scr refresh
        begin_text1_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(begin_text1_4, 'tStartRefresh')  # time at next scr refresh
        begin_text1_4.setAutoDraw(True)
    
    # *pracImage_center_2* updates
    if pracImage_center_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        pracImage_center_2.frameNStart = frameN  # exact frame index
        pracImage_center_2.tStart = t  # local t and not account for scr refresh
        pracImage_center_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(pracImage_center_2, 'tStartRefresh')  # time at next scr refresh
        pracImage_center_2.setAutoDraw(True)
    
    # *pracImage_top_2* updates
    if pracImage_top_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        pracImage_top_2.frameNStart = frameN  # exact frame index
        pracImage_top_2.tStart = t  # local t and not account for scr refresh
        pracImage_top_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(pracImage_top_2, 'tStartRefresh')  # time at next scr refresh
        pracImage_top_2.setAutoDraw(True)
    
    # *pracImage_right_2* updates
    if pracImage_right_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        pracImage_right_2.frameNStart = frameN  # exact frame index
        pracImage_right_2.tStart = t  # local t and not account for scr refresh
        pracImage_right_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(pracImage_right_2, 'tStartRefresh')  # time at next scr refresh
        pracImage_right_2.setAutoDraw(True)
    
    # *pracImage_bottom_2* updates
    if pracImage_bottom_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        pracImage_bottom_2.frameNStart = frameN  # exact frame index
        pracImage_bottom_2.tStart = t  # local t and not account for scr refresh
        pracImage_bottom_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(pracImage_bottom_2, 'tStartRefresh')  # time at next scr refresh
        pracImage_bottom_2.setAutoDraw(True)
    
    # *pracImage_left_2* updates
    if pracImage_left_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        pracImage_left_2.frameNStart = frameN  # exact frame index
        pracImage_left_2.tStart = t  # local t and not account for scr refresh
        pracImage_left_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(pracImage_left_2, 'tStartRefresh')  # time at next scr refresh
        pracImage_left_2.setAutoDraw(True)
    
    # *begin_keyResp_4* updates
    waitOnFlip = False
    if begin_keyResp_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        begin_keyResp_4.frameNStart = frameN  # exact frame index
        begin_keyResp_4.tStart = t  # local t and not account for scr refresh
        begin_keyResp_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(begin_keyResp_4, 'tStartRefresh')  # time at next scr refresh
        begin_keyResp_4.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(begin_keyResp_4.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(begin_keyResp_4.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if begin_keyResp_4.status == STARTED and not waitOnFlip:
        theseKeys = begin_keyResp_4.getKeys(keyList=['1', '8'], waitRelease=False)
        _begin_keyResp_4_allKeys.extend(theseKeys)
        if len(_begin_keyResp_4_allKeys):
            begin_keyResp_4.keys = _begin_keyResp_4_allKeys[-1].name  # just the last key pressed
            begin_keyResp_4.rt = _begin_keyResp_4_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *begin_text2_4* updates
    if begin_text2_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        begin_text2_4.frameNStart = frameN  # exact frame index
        begin_text2_4.tStart = t  # local t and not account for scr refresh
        begin_text2_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(begin_text2_4, 'tStartRefresh')  # time at next scr refresh
        begin_text2_4.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in beginInstruct_2aComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "beginInstruct_2a"-------
for thisComponent in beginInstruct_2aComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('begin_text1_4.started', begin_text1_4.tStartRefresh)
thisExp.addData('begin_text1_4.stopped', begin_text1_4.tStopRefresh)
thisExp.addData('pracImage_center_2.started', pracImage_center_2.tStartRefresh)
thisExp.addData('pracImage_center_2.stopped', pracImage_center_2.tStopRefresh)
thisExp.addData('pracImage_top_2.started', pracImage_top_2.tStartRefresh)
thisExp.addData('pracImage_top_2.stopped', pracImage_top_2.tStopRefresh)
thisExp.addData('pracImage_right_2.started', pracImage_right_2.tStartRefresh)
thisExp.addData('pracImage_right_2.stopped', pracImage_right_2.tStopRefresh)
thisExp.addData('pracImage_bottom_2.started', pracImage_bottom_2.tStartRefresh)
thisExp.addData('pracImage_bottom_2.stopped', pracImage_bottom_2.tStopRefresh)
thisExp.addData('pracImage_left_2.started', pracImage_left_2.tStartRefresh)
thisExp.addData('pracImage_left_2.stopped', pracImage_left_2.tStopRefresh)
# check responses
if begin_keyResp_4.keys in ['', [], None]:  # No response was made
    begin_keyResp_4.keys = None
thisExp.addData('begin_keyResp_4.keys',begin_keyResp_4.keys)
if begin_keyResp_4.keys != None:  # we had a response
    thisExp.addData('begin_keyResp_4.rt', begin_keyResp_4.rt)
thisExp.addData('begin_keyResp_4.started', begin_keyResp_4.tStartRefresh)
thisExp.addData('begin_keyResp_4.stopped', begin_keyResp_4.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('begin_text2_4.started', begin_text2_4.tStartRefresh)
thisExp.addData('begin_text2_4.stopped', begin_text2_4.tStopRefresh)
# the Routine "beginInstruct_2a" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "beginInstruct_3a"-------
continueRoutine = True
# update component parameters for each repeat
begin_keyResp_3a.keys = []
begin_keyResp_3a.rt = []
_begin_keyResp_3a_allKeys = []
# keep track of which components have finished
beginInstruct_3aComponents = [begin_text1_3a, begin_text2_3a, begin_keyResp_3a]
for thisComponent in beginInstruct_3aComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
beginInstruct_3aClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "beginInstruct_3a"-------
while continueRoutine:
    # get current time
    t = beginInstruct_3aClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=beginInstruct_3aClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *begin_text1_3a* updates
    if begin_text1_3a.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        begin_text1_3a.frameNStart = frameN  # exact frame index
        begin_text1_3a.tStart = t  # local t and not account for scr refresh
        begin_text1_3a.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(begin_text1_3a, 'tStartRefresh')  # time at next scr refresh
        begin_text1_3a.setAutoDraw(True)
    
    # *begin_text2_3a* updates
    if begin_text2_3a.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        begin_text2_3a.frameNStart = frameN  # exact frame index
        begin_text2_3a.tStart = t  # local t and not account for scr refresh
        begin_text2_3a.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(begin_text2_3a, 'tStartRefresh')  # time at next scr refresh
        begin_text2_3a.setAutoDraw(True)
    
    # *begin_keyResp_3a* updates
    waitOnFlip = False
    if begin_keyResp_3a.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        begin_keyResp_3a.frameNStart = frameN  # exact frame index
        begin_keyResp_3a.tStart = t  # local t and not account for scr refresh
        begin_keyResp_3a.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(begin_keyResp_3a, 'tStartRefresh')  # time at next scr refresh
        begin_keyResp_3a.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(begin_keyResp_3a.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(begin_keyResp_3a.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if begin_keyResp_3a.status == STARTED and not waitOnFlip:
        theseKeys = begin_keyResp_3a.getKeys(keyList=['1', '8'], waitRelease=False)
        _begin_keyResp_3a_allKeys.extend(theseKeys)
        if len(_begin_keyResp_3a_allKeys):
            begin_keyResp_3a.keys = _begin_keyResp_3a_allKeys[-1].name  # just the last key pressed
            begin_keyResp_3a.rt = _begin_keyResp_3a_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in beginInstruct_3aComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "beginInstruct_3a"-------
for thisComponent in beginInstruct_3aComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('begin_text1_3a.started', begin_text1_3a.tStartRefresh)
thisExp.addData('begin_text1_3a.stopped', begin_text1_3a.tStopRefresh)
thisExp.addData('begin_text2_3a.started', begin_text2_3a.tStartRefresh)
thisExp.addData('begin_text2_3a.stopped', begin_text2_3a.tStopRefresh)
# check responses
if begin_keyResp_3a.keys in ['', [], None]:  # No response was made
    begin_keyResp_3a.keys = None
thisExp.addData('begin_keyResp_3a.keys',begin_keyResp_3a.keys)
if begin_keyResp_3a.keys != None:  # we had a response
    thisExp.addData('begin_keyResp_3a.rt', begin_keyResp_3a.rt)
thisExp.addData('begin_keyResp_3a.started', begin_keyResp_3a.tStartRefresh)
thisExp.addData('begin_keyResp_3a.stopped', begin_keyResp_3a.tStopRefresh)
thisExp.nextEntry()
# the Routine "beginInstruct_3a" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
prac_BlockLoop = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('inhib_practiceblockSelect.csv'),
    seed=None, name='prac_BlockLoop')
thisExp.addLoop(prac_BlockLoop)  # add the loop to the experiment
thisPrac_BlockLoop = prac_BlockLoop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisPrac_BlockLoop.rgb)
if thisPrac_BlockLoop != None:
    for paramName in thisPrac_BlockLoop:
        exec('{} = thisPrac_BlockLoop[paramName]'.format(paramName))

for thisPrac_BlockLoop in prac_BlockLoop:
    currentLoop = prac_BlockLoop
    # abbreviate parameter names if possible (e.g. rgb = thisPrac_BlockLoop.rgb)
    if thisPrac_BlockLoop != None:
        for paramName in thisPrac_BlockLoop:
            exec('{} = thisPrac_BlockLoop[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "task_instruct"-------
    continueRoutine = True
    # update component parameters for each repeat
    if CB =='BSOD':
        blueKey = '1'
        squareKey = '1'
        orangeKey = '8'
        diagKey = '8'   
        if whichBlock == 'color.xlsx':
            leftKeyText = 'the center image is BLUE \n'
            rightKeyText = '\n \n \n \n \n \n the center image is ORANGE'
            leftReminder = 'BLUE - SQUARE'
            rightReminder = 'ORANGE - DIAMOND'
        elif whichBlock == 'shape.xlsx':
            leftKeyText = 'the center image is a SQUARE \n'
            rightKeyText = '\n \n \n \n \n \n the center image is DIAMOND'
            leftReminder = 'BLUE - SQUARE'
            rightReminder = 'ORANGE - DIAMOND'
        elif whichBlock == 'switch.xlsx':
            leftKeyText = '\n \n \n \n \n the word says COLOR and the image is BLUE, \n or if the word says SHAPE and the image is a SQUARE \n'
            rightKeyText = '\n \n \n \n \n \n \n \n \n \n \n \n \n the word says COLOR and the image is ORANGE, \n or if the word says SHAPE and the image is a DIAMOND'
            leftReminder = 'BLUE - SQUARE'
            rightReminder = 'ORANGE - DIAMOND'
    #    elif whichBlock == 'oneBackColor.xlsx':
    #        leftKeyText = 'the center image is the SAME COLOR as \n the image presented one image previously (1BACK) \n'
    #        rightKeyText = '\n \n \n \n \n \n \n \n \n \n the center image is a DIFFERENT COLOR as \n the image presented one image previously (1BACK)'
    #        leftReminder = 'SAME'
    #        rightReminder = 'DIFFERENT'
    #    elif whichBlock == 'twoBackColor.xlsx':
    #        leftKeyText = 'the center image is the SAME COLOR as \n the image presented TWO images previously (2BACK) \n'
    #        rightKeyText = '\n \n \n \n \n \n \n \n \n \n the center image is the DIFFERENT COLOR as \n the image presented TWO images previously (2BACK)'
    #        leftReminder = 'SAME'
    #        rightReminder = 'DIFFERENT'
    
    elif CB =='BDOS':
        blueKey = '1'
        squareKey = '8'
        orangeKey = '8'
        diagKey = '1'
    elif CB =='ODBS':
        blueKey = '8'
        squareKey = '8'
        orangeKey = '1'
        diagKey = '1'
    elif CB =='OSBD':
        blueKey = '8'
        squareKey = '1'
        orangeKey = '1'
        diagKey = '8'
    taskName.setText(taskNameSource)
    task_Text.setText(taskTextSource)
    leftKey_text.setText(leftKeyText)
    rightKey_text.setText(rightKeyText)
    LeftReminder_text.setText(leftReminder)
    rightReminder_text.setText(rightReminder)
    pracOrMain_keyResp.keys = []
    pracOrMain_keyResp.rt = []
    _pracOrMain_keyResp_allKeys = []
    # keep track of which components have finished
    task_instructComponents = [taskName, task_Text, leftKey_text, rightKey_text, task_text5, LeftReminder_text, rightReminder_text, pracOrMain_keyResp]
    for thisComponent in task_instructComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    task_instructClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "task_instruct"-------
    while continueRoutine:
        # get current time
        t = task_instructClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=task_instructClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *taskName* updates
        if taskName.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            taskName.frameNStart = frameN  # exact frame index
            taskName.tStart = t  # local t and not account for scr refresh
            taskName.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(taskName, 'tStartRefresh')  # time at next scr refresh
            taskName.setAutoDraw(True)
        
        # *task_Text* updates
        if task_Text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            task_Text.frameNStart = frameN  # exact frame index
            task_Text.tStart = t  # local t and not account for scr refresh
            task_Text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(task_Text, 'tStartRefresh')  # time at next scr refresh
            task_Text.setAutoDraw(True)
        
        # *leftKey_text* updates
        if leftKey_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            leftKey_text.frameNStart = frameN  # exact frame index
            leftKey_text.tStart = t  # local t and not account for scr refresh
            leftKey_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(leftKey_text, 'tStartRefresh')  # time at next scr refresh
            leftKey_text.setAutoDraw(True)
        
        # *rightKey_text* updates
        if rightKey_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            rightKey_text.frameNStart = frameN  # exact frame index
            rightKey_text.tStart = t  # local t and not account for scr refresh
            rightKey_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(rightKey_text, 'tStartRefresh')  # time at next scr refresh
            rightKey_text.setAutoDraw(True)
        
        # *task_text5* updates
        if task_text5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            task_text5.frameNStart = frameN  # exact frame index
            task_text5.tStart = t  # local t and not account for scr refresh
            task_text5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(task_text5, 'tStartRefresh')  # time at next scr refresh
            task_text5.setAutoDraw(True)
        
        # *LeftReminder_text* updates
        if LeftReminder_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            LeftReminder_text.frameNStart = frameN  # exact frame index
            LeftReminder_text.tStart = t  # local t and not account for scr refresh
            LeftReminder_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(LeftReminder_text, 'tStartRefresh')  # time at next scr refresh
            LeftReminder_text.setAutoDraw(True)
        
        # *rightReminder_text* updates
        if rightReminder_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            rightReminder_text.frameNStart = frameN  # exact frame index
            rightReminder_text.tStart = t  # local t and not account for scr refresh
            rightReminder_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(rightReminder_text, 'tStartRefresh')  # time at next scr refresh
            rightReminder_text.setAutoDraw(True)
        
        # *pracOrMain_keyResp* updates
        waitOnFlip = False
        if pracOrMain_keyResp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            pracOrMain_keyResp.frameNStart = frameN  # exact frame index
            pracOrMain_keyResp.tStart = t  # local t and not account for scr refresh
            pracOrMain_keyResp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(pracOrMain_keyResp, 'tStartRefresh')  # time at next scr refresh
            pracOrMain_keyResp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(pracOrMain_keyResp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(pracOrMain_keyResp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if pracOrMain_keyResp.status == STARTED and not waitOnFlip:
            theseKeys = pracOrMain_keyResp.getKeys(keyList=['1', '8'], waitRelease=False)
            _pracOrMain_keyResp_allKeys.extend(theseKeys)
            if len(_pracOrMain_keyResp_allKeys):
                pracOrMain_keyResp.keys = _pracOrMain_keyResp_allKeys[-1].name  # just the last key pressed
                pracOrMain_keyResp.rt = _pracOrMain_keyResp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in task_instructComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "task_instruct"-------
    for thisComponent in task_instructComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    prac_BlockLoop.addData('taskName.started', taskName.tStartRefresh)
    prac_BlockLoop.addData('taskName.stopped', taskName.tStopRefresh)
    prac_BlockLoop.addData('task_Text.started', task_Text.tStartRefresh)
    prac_BlockLoop.addData('task_Text.stopped', task_Text.tStopRefresh)
    prac_BlockLoop.addData('leftKey_text.started', leftKey_text.tStartRefresh)
    prac_BlockLoop.addData('leftKey_text.stopped', leftKey_text.tStopRefresh)
    prac_BlockLoop.addData('rightKey_text.started', rightKey_text.tStartRefresh)
    prac_BlockLoop.addData('rightKey_text.stopped', rightKey_text.tStopRefresh)
    prac_BlockLoop.addData('task_text5.started', task_text5.tStartRefresh)
    prac_BlockLoop.addData('task_text5.stopped', task_text5.tStopRefresh)
    prac_BlockLoop.addData('LeftReminder_text.started', LeftReminder_text.tStartRefresh)
    prac_BlockLoop.addData('LeftReminder_text.stopped', LeftReminder_text.tStopRefresh)
    prac_BlockLoop.addData('rightReminder_text.started', rightReminder_text.tStartRefresh)
    prac_BlockLoop.addData('rightReminder_text.stopped', rightReminder_text.tStopRefresh)
    # check responses
    if pracOrMain_keyResp.keys in ['', [], None]:  # No response was made
        pracOrMain_keyResp.keys = None
    prac_BlockLoop.addData('pracOrMain_keyResp.keys',pracOrMain_keyResp.keys)
    if pracOrMain_keyResp.keys != None:  # we had a response
        prac_BlockLoop.addData('pracOrMain_keyResp.rt', pracOrMain_keyResp.rt)
    prac_BlockLoop.addData('pracOrMain_keyResp.started', pracOrMain_keyResp.tStartRefresh)
    prac_BlockLoop.addData('pracOrMain_keyResp.stopped', pracOrMain_keyResp.tStopRefresh)
    # the Routine "task_instruct" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "task_instruct2"-------
    continueRoutine = True
    # update component parameters for each repeat
    if practice == 1:
        startText ='\n \n \n \n \n \n \n \n \n \n \n \n \n \n Press either the left or right button to practice this game'
    elif practice == 0:
            startText ='\n \n \n \n \n \n \n \n \n \n \n \n \n \n Press either the left or right button to start the real game'
    
    
    taskName_2.setText(taskNameSource)
    task_Text_2.setText('\n\nPlease rest your left finger on the left button and your right finger on the right button.\nWhen an image is shown, you should respond as quickly as you can while also being correct.')
    task_text_3.setText(cueReminderTextSource)
    task_text_4.setText(startText)
    LeftReminder_text_5.setText(leftReminder)
    rightReminder_text_5.setText(rightReminder)
    pracOrMain_keyResp_3.keys = []
    pracOrMain_keyResp_3.rt = []
    _pracOrMain_keyResp_3_allKeys = []
    # keep track of which components have finished
    task_instruct2Components = [taskName_2, task_Text_2, task_text_3, task_text_4, LeftReminder_text_5, rightReminder_text_5, pracOrMain_keyResp_3]
    for thisComponent in task_instruct2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    task_instruct2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "task_instruct2"-------
    while continueRoutine:
        # get current time
        t = task_instruct2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=task_instruct2Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *taskName_2* updates
        if taskName_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            taskName_2.frameNStart = frameN  # exact frame index
            taskName_2.tStart = t  # local t and not account for scr refresh
            taskName_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(taskName_2, 'tStartRefresh')  # time at next scr refresh
            taskName_2.setAutoDraw(True)
        
        # *task_Text_2* updates
        if task_Text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            task_Text_2.frameNStart = frameN  # exact frame index
            task_Text_2.tStart = t  # local t and not account for scr refresh
            task_Text_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(task_Text_2, 'tStartRefresh')  # time at next scr refresh
            task_Text_2.setAutoDraw(True)
        
        # *task_text_3* updates
        if task_text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            task_text_3.frameNStart = frameN  # exact frame index
            task_text_3.tStart = t  # local t and not account for scr refresh
            task_text_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(task_text_3, 'tStartRefresh')  # time at next scr refresh
            task_text_3.setAutoDraw(True)
        
        # *task_text_4* updates
        if task_text_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            task_text_4.frameNStart = frameN  # exact frame index
            task_text_4.tStart = t  # local t and not account for scr refresh
            task_text_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(task_text_4, 'tStartRefresh')  # time at next scr refresh
            task_text_4.setAutoDraw(True)
        
        # *LeftReminder_text_5* updates
        if LeftReminder_text_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            LeftReminder_text_5.frameNStart = frameN  # exact frame index
            LeftReminder_text_5.tStart = t  # local t and not account for scr refresh
            LeftReminder_text_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(LeftReminder_text_5, 'tStartRefresh')  # time at next scr refresh
            LeftReminder_text_5.setAutoDraw(True)
        
        # *rightReminder_text_5* updates
        if rightReminder_text_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            rightReminder_text_5.frameNStart = frameN  # exact frame index
            rightReminder_text_5.tStart = t  # local t and not account for scr refresh
            rightReminder_text_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(rightReminder_text_5, 'tStartRefresh')  # time at next scr refresh
            rightReminder_text_5.setAutoDraw(True)
        
        # *pracOrMain_keyResp_3* updates
        waitOnFlip = False
        if pracOrMain_keyResp_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            pracOrMain_keyResp_3.frameNStart = frameN  # exact frame index
            pracOrMain_keyResp_3.tStart = t  # local t and not account for scr refresh
            pracOrMain_keyResp_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(pracOrMain_keyResp_3, 'tStartRefresh')  # time at next scr refresh
            pracOrMain_keyResp_3.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(pracOrMain_keyResp_3.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(pracOrMain_keyResp_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if pracOrMain_keyResp_3.status == STARTED and not waitOnFlip:
            theseKeys = pracOrMain_keyResp_3.getKeys(keyList=['1', '8'], waitRelease=False)
            _pracOrMain_keyResp_3_allKeys.extend(theseKeys)
            if len(_pracOrMain_keyResp_3_allKeys):
                pracOrMain_keyResp_3.keys = _pracOrMain_keyResp_3_allKeys[-1].name  # just the last key pressed
                pracOrMain_keyResp_3.rt = _pracOrMain_keyResp_3_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in task_instruct2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "task_instruct2"-------
    for thisComponent in task_instruct2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    prac_BlockLoop.addData('taskName_2.started', taskName_2.tStartRefresh)
    prac_BlockLoop.addData('taskName_2.stopped', taskName_2.tStopRefresh)
    prac_BlockLoop.addData('task_Text_2.started', task_Text_2.tStartRefresh)
    prac_BlockLoop.addData('task_Text_2.stopped', task_Text_2.tStopRefresh)
    prac_BlockLoop.addData('task_text_3.started', task_text_3.tStartRefresh)
    prac_BlockLoop.addData('task_text_3.stopped', task_text_3.tStopRefresh)
    prac_BlockLoop.addData('task_text_4.started', task_text_4.tStartRefresh)
    prac_BlockLoop.addData('task_text_4.stopped', task_text_4.tStopRefresh)
    prac_BlockLoop.addData('LeftReminder_text_5.started', LeftReminder_text_5.tStartRefresh)
    prac_BlockLoop.addData('LeftReminder_text_5.stopped', LeftReminder_text_5.tStopRefresh)
    prac_BlockLoop.addData('rightReminder_text_5.started', rightReminder_text_5.tStartRefresh)
    prac_BlockLoop.addData('rightReminder_text_5.stopped', rightReminder_text_5.tStopRefresh)
    # check responses
    if pracOrMain_keyResp_3.keys in ['', [], None]:  # No response was made
        pracOrMain_keyResp_3.keys = None
    prac_BlockLoop.addData('pracOrMain_keyResp_3.keys',pracOrMain_keyResp_3.keys)
    if pracOrMain_keyResp_3.keys != None:  # we had a response
        prac_BlockLoop.addData('pracOrMain_keyResp_3.rt', pracOrMain_keyResp_3.rt)
    prac_BlockLoop.addData('pracOrMain_keyResp_3.started', pracOrMain_keyResp_3.tStartRefresh)
    prac_BlockLoop.addData('pracOrMain_keyResp_3.stopped', pracOrMain_keyResp_3.tStopRefresh)
    # the Routine "task_instruct2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    prac_trialLoop = data.TrialHandler(nReps=numberReps, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('practice_faceSelect.csv'),
        seed=None, name='prac_trialLoop')
    thisExp.addLoop(prac_trialLoop)  # add the loop to the experiment
    thisPrac_trialLoop = prac_trialLoop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisPrac_trialLoop.rgb)
    if thisPrac_trialLoop != None:
        for paramName in thisPrac_trialLoop:
            exec('{} = thisPrac_trialLoop[paramName]'.format(paramName))
    
    for thisPrac_trialLoop in prac_trialLoop:
        currentLoop = prac_trialLoop
        # abbreviate parameter names if possible (e.g. rgb = thisPrac_trialLoop.rgb)
        if thisPrac_trialLoop != None:
            for paramName in thisPrac_trialLoop:
                exec('{} = thisPrac_trialLoop[paramName]'.format(paramName))
        
        # set up handler to look after randomisation of conditions etc
        prac_cueLoop = data.TrialHandler(nReps=1.0, method='fullRandom', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions(whichBlock),
            seed=None, name='prac_cueLoop')
        thisExp.addLoop(prac_cueLoop)  # add the loop to the experiment
        thisPrac_cueLoop = prac_cueLoop.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisPrac_cueLoop.rgb)
        if thisPrac_cueLoop != None:
            for paramName in thisPrac_cueLoop:
                exec('{} = thisPrac_cueLoop[paramName]'.format(paramName))
        
        for thisPrac_cueLoop in prac_cueLoop:
            currentLoop = prac_cueLoop
            # abbreviate parameter names if possible (e.g. rgb = thisPrac_cueLoop.rgb)
            if thisPrac_cueLoop != None:
                for paramName in thisPrac_cueLoop:
                    exec('{} = thisPrac_cueLoop[paramName]'.format(paramName))
            
            # ------Prepare to start Routine "prac_cueRoutine"-------
            continueRoutine = True
            # update component parameters for each repeat
            # pick the ISI for the next routine
            # this code component is set to 'both' because we need to remove the 'np'
            # at the start of np.linspace (this is a python library JS won't know what to call. 
            
            # make range from a to b in n stepsizes
            RSIRange = np.linspace(1000, 1500, 500)
            # picking from a shuffled array is easier for random selection in JS
            shuffle(RSIRange)
            thisRSI = RSIRange[0]/1000 # the first item of the shuffled array 
            
            reminderDur = thisRSI +1
            
            # show in console for debugging
            print('thisRSI: ', thisRSI)
            
            # save this ISI to our output file
            prac_cueLoop.addData('RSI', thisRSI)
            LeftReminder_text_6.setText(leftReminder)
            rightReminder_text_6.setText(rightReminder)
            cuePresented_2.setText(whichCue)
            #2
            pulse_started = False
            pulse_ended = False
            
            
            # keep track of which components have finished
            prac_cueRoutineComponents = [LeftReminder_text_6, rightReminder_text_6, cuePresented_2]
            for thisComponent in prac_cueRoutineComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            prac_cueRoutineClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "prac_cueRoutine"-------
            while continueRoutine:
                # get current time
                t = prac_cueRoutineClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=prac_cueRoutineClock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *LeftReminder_text_6* updates
                if LeftReminder_text_6.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                    # keep track of start time/frame for later
                    LeftReminder_text_6.frameNStart = frameN  # exact frame index
                    LeftReminder_text_6.tStart = t  # local t and not account for scr refresh
                    LeftReminder_text_6.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(LeftReminder_text_6, 'tStartRefresh')  # time at next scr refresh
                    LeftReminder_text_6.setAutoDraw(True)
                if LeftReminder_text_6.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > LeftReminder_text_6.tStartRefresh + reminderDur-frameTolerance:
                        # keep track of stop time/frame for later
                        LeftReminder_text_6.tStop = t  # not accounting for scr refresh
                        LeftReminder_text_6.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(LeftReminder_text_6, 'tStopRefresh')  # time at next scr refresh
                        LeftReminder_text_6.setAutoDraw(False)
                
                # *rightReminder_text_6* updates
                if rightReminder_text_6.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                    # keep track of start time/frame for later
                    rightReminder_text_6.frameNStart = frameN  # exact frame index
                    rightReminder_text_6.tStart = t  # local t and not account for scr refresh
                    rightReminder_text_6.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(rightReminder_text_6, 'tStartRefresh')  # time at next scr refresh
                    rightReminder_text_6.setAutoDraw(True)
                if rightReminder_text_6.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > rightReminder_text_6.tStartRefresh + reminderDur-frameTolerance:
                        # keep track of stop time/frame for later
                        rightReminder_text_6.tStop = t  # not accounting for scr refresh
                        rightReminder_text_6.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(rightReminder_text_6, 'tStopRefresh')  # time at next scr refresh
                        rightReminder_text_6.setAutoDraw(False)
                
                # *cuePresented_2* updates
                if cuePresented_2.status == NOT_STARTED and tThisFlip >= thisRSI-frameTolerance:
                    # keep track of start time/frame for later
                    cuePresented_2.frameNStart = frameN  # exact frame index
                    cuePresented_2.tStart = t  # local t and not account for scr refresh
                    cuePresented_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(cuePresented_2, 'tStartRefresh')  # time at next scr refresh
                    cuePresented_2.setAutoDraw(True)
                if cuePresented_2.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > cuePresented_2.tStartRefresh + .5-frameTolerance:
                        # keep track of stop time/frame for later
                        cuePresented_2.tStop = t  # not accounting for scr refresh
                        cuePresented_2.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(cuePresented_2, 'tStopRefresh')  # time at next scr refresh
                        cuePresented_2.setAutoDraw(False)
                #3
                if cuePresented_2.status == STARTED and not pulse_started:
                    if whichCue == 'SHAPE':
                        port.write([0x01])#S1 for 'SHAPE' cue. 
                        time.sleep(PulseWidth)
                        pulse_start_time = globalClock.getTime()
                        pulse_started = True
                    elif whichCue == 'COLOR':
                        port.write([0x02])#S2 for 'COLOR' cue.
                        time.sleep(PulseWidth)
                        pulse_start_time = globalClock.getTime()
                        pulse_started = True
                if pulse_started and not pulse_ended:
                    if globalClock.getTime() - pulse_start_time >= 0.005:
                        #port.write([0x02])
                        pulse_ended = True
                
                
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in prac_cueRoutineComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "prac_cueRoutine"-------
            for thisComponent in prac_cueRoutineComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            prac_cueLoop.addData('LeftReminder_text_6.started', LeftReminder_text_6.tStartRefresh)
            prac_cueLoop.addData('LeftReminder_text_6.stopped', LeftReminder_text_6.tStopRefresh)
            prac_cueLoop.addData('rightReminder_text_6.started', rightReminder_text_6.tStartRefresh)
            prac_cueLoop.addData('rightReminder_text_6.stopped', rightReminder_text_6.tStopRefresh)
            prac_cueLoop.addData('cuePresented_2.started', cuePresented_2.tStartRefresh)
            prac_cueLoop.addData('cuePresented_2.stopped', cuePresented_2.tStopRefresh)
            port.write([0xFF])
            time.sleep(PulseWidth)
            # the Routine "prac_cueRoutine" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # ------Prepare to start Routine "break_prac_cueLoop"-------
            continueRoutine = True
            # update component parameters for each repeat
            # keep track of which components have finished
            break_prac_cueLoopComponents = []
            for thisComponent in break_prac_cueLoopComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            break_prac_cueLoopClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "break_prac_cueLoop"-------
            while continueRoutine:
                # get current time
                t = break_prac_cueLoopClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=break_prac_cueLoopClock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in break_prac_cueLoopComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "break_prac_cueLoop"-------
            for thisComponent in break_prac_cueLoopComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            prac_cueLoop.finished=True
            
            # the Routine "break_prac_cueLoop" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            thisExp.nextEntry()
            
        # completed 1.0 repeats of 'prac_cueLoop'
        
        
        # set up handler to look after randomisation of conditions etc
        prac_stimLoop = data.TrialHandler(nReps=1.0, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions(whichFace),
            seed=None, name='prac_stimLoop')
        thisExp.addLoop(prac_stimLoop)  # add the loop to the experiment
        thisPrac_stimLoop = prac_stimLoop.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisPrac_stimLoop.rgb)
        if thisPrac_stimLoop != None:
            for paramName in thisPrac_stimLoop:
                exec('{} = thisPrac_stimLoop[paramName]'.format(paramName))
        
        for thisPrac_stimLoop in prac_stimLoop:
            currentLoop = prac_stimLoop
            # abbreviate parameter names if possible (e.g. rgb = thisPrac_stimLoop.rgb)
            if thisPrac_stimLoop != None:
                for paramName in thisPrac_stimLoop:
                    exec('{} = thisPrac_stimLoop[paramName]'.format(paramName))
            
            # ------Prepare to start Routine "prac_StimRoutine"-------
            continueRoutine = True
            # update component parameters for each repeat
            # pick the ISI for the next routine
            # this code component is set to 'both' because we need to remove the 'np'
            # at the start of np.linspace (this is a python library JS won't know what to call. 
            
            # make range from a to b in n stepsizes
            ISIRange = np.linspace(1000, 1500, 500)
            # picking from a shuffled array is easier for random selection in JS
            shuffle(ISIRange)
            thisISI = ISIRange[0]/1000 # the first item of the shuffled array 
            
            reminderDur = thisISI +1
            
            # show in console for debugging
            print('thisISI: ', thisISI)
            
            # save this ISI to our output file
            prac_stimLoop.addData('ISI', thisISI)
            if whichCue == 'SHAPE':
                if rotCenter == 315:
                    corrAns = diagKey
                else:
                    corrAns = squareKey
            elif whichCue == 'COLOR':
                if blueCenter == 1:
                    corrAns = blueKey
                else:
                    corrAns = orangeKey
            #elif whichCue == '1BACK COLOR':
            #    if back1_blueCenter == 1:
            #        corrAns = blueKey
            #    else:
            #        corrAns = orangeKey
            #elif whichCue == '1BACK SHAPE':
            #    if back1_blueCenter == 1:
            #        corrAns = diagKey
            #    else:
            #        corrAns = squareKey
            #elif whichCue == '2BACK COLOR':
            #    if back2_blueCenter == 1:
            #        corrAns = blueKey
            #    else:
            #        corrAns = orangeKey
            #elif whichCue == '2BACK SHAPE':
            #    if back2_blueCenter == 1:
            #        corrAns = diagKey
            #    else:
            #        corrAns = squareKey
            
            # save corrAns to our output file
            prac_stimLoop.addData('corrAns', corrAns)
            
            
            #        if key_resp_3.corr:
            #            corrAns == 'm'
            #            right = 'resources/assets/BlueBoatWhite.png'
            #        else:
            #            left = 'resources/assets/RedRabbitWhite.png'
            #    elif key_resp_3.keys[0] =='m':
            #        if key_resp_3.corr:
            #            right = 'resources/assets/BlueBoatRed.png'
            #           left = 'resources/assets/RedRabbitWhite.png'
            #           audio = 'resources/assets/Thatsright.mp3'
            #       else:
            #else: # thi is classed as an incorrect response
            #    if corrAns == 'm':
            #        right = 'resources/assets/BlueBoatRed.png'
            
            
            ## make range from a to b in n stepsizes
            #ISIRange = np.linspace(1000, 1500, 500)
            ## picking from a shuffled array is easier for random selection in JS
            #shuffle(ISIRange)
            #thisISI = ISIRange[0]/1000 # the first item of the shuffled array 
            
            ## show in console for debugging
            #print('thisISI: ', thisISI)
            
            
            
            
            LeftReminder_text_7.setText(leftReminder)
            rightReminder_text_7.setText(rightReminder)
            centerPresented_2.setOri(rotCenter)
            centerPresented_2.setImage(center)
            topPresented_2.setOri(rotSurround)
            topPresented_2.setImage(surround)
            rightPresented_2.setOri(rotSurround)
            rightPresented_2.setImage(surround)
            bottomPresented_2.setOri(rotSurround)
            bottomPresented_2.setImage(surround)
            leftPresented_2.setOri(rotSurround)
            leftPresented_2.setImage(surround)
            
            # Clear ports
            #port.write([0xFF])
            
            
            
            # time to wait before clearing the ports after a trigger (in seconds)
            postTriggerPauseTime_1 = 0.04
            pauseStartTime_1 = 0
            triggerSent_1 = False
            portsCleared_1 = False
            
            
            keyResp_2.keys = []
            keyResp_2.rt = []
            _keyResp_2_allKeys = []
            #2
            mark_started = False
            mark_ended = False
            
            # Clear ports
            port.write([0x00])
            Connected = False
            thread.join(1.0)
            
            keys_counted = []
            
            # time to wait before clearing the ports after a trigger (in seconds)
            postTriggerPauseTime = 0.05
            pauseStartTime = 0
            triggerSent = False
            portsCleared = True
            # keep track of which components have finished
            prac_StimRoutineComponents = [LeftReminder_text_7, rightReminder_text_7, centerPresented_2, topPresented_2, rightPresented_2, bottomPresented_2, leftPresented_2, keyResp_2]
            for thisComponent in prac_StimRoutineComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            prac_StimRoutineClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "prac_StimRoutine"-------
            while continueRoutine:
                # get current time
                t = prac_StimRoutineClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=prac_StimRoutineClock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *LeftReminder_text_7* updates
                if LeftReminder_text_7.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                    # keep track of start time/frame for later
                    LeftReminder_text_7.frameNStart = frameN  # exact frame index
                    LeftReminder_text_7.tStart = t  # local t and not account for scr refresh
                    LeftReminder_text_7.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(LeftReminder_text_7, 'tStartRefresh')  # time at next scr refresh
                    LeftReminder_text_7.setAutoDraw(True)
                if LeftReminder_text_7.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > LeftReminder_text_7.tStartRefresh + reminderDur-frameTolerance:
                        # keep track of stop time/frame for later
                        LeftReminder_text_7.tStop = t  # not accounting for scr refresh
                        LeftReminder_text_7.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(LeftReminder_text_7, 'tStopRefresh')  # time at next scr refresh
                        LeftReminder_text_7.setAutoDraw(False)
                
                # *rightReminder_text_7* updates
                if rightReminder_text_7.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                    # keep track of start time/frame for later
                    rightReminder_text_7.frameNStart = frameN  # exact frame index
                    rightReminder_text_7.tStart = t  # local t and not account for scr refresh
                    rightReminder_text_7.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(rightReminder_text_7, 'tStartRefresh')  # time at next scr refresh
                    rightReminder_text_7.setAutoDraw(True)
                if rightReminder_text_7.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > rightReminder_text_7.tStartRefresh + reminderDur-frameTolerance:
                        # keep track of stop time/frame for later
                        rightReminder_text_7.tStop = t  # not accounting for scr refresh
                        rightReminder_text_7.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(rightReminder_text_7, 'tStopRefresh')  # time at next scr refresh
                        rightReminder_text_7.setAutoDraw(False)
                
                # *centerPresented_2* updates
                if centerPresented_2.status == NOT_STARTED and tThisFlip >= thisISI-frameTolerance:
                    # keep track of start time/frame for later
                    centerPresented_2.frameNStart = frameN  # exact frame index
                    centerPresented_2.tStart = t  # local t and not account for scr refresh
                    centerPresented_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(centerPresented_2, 'tStartRefresh')  # time at next scr refresh
                    centerPresented_2.setAutoDraw(True)
                if centerPresented_2.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > centerPresented_2.tStartRefresh + .5-frameTolerance:
                        # keep track of stop time/frame for later
                        centerPresented_2.tStop = t  # not accounting for scr refresh
                        centerPresented_2.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(centerPresented_2, 'tStopRefresh')  # time at next scr refresh
                        centerPresented_2.setAutoDraw(False)
                
                # *topPresented_2* updates
                if topPresented_2.status == NOT_STARTED and tThisFlip >= thisISI-frameTolerance:
                    # keep track of start time/frame for later
                    topPresented_2.frameNStart = frameN  # exact frame index
                    topPresented_2.tStart = t  # local t and not account for scr refresh
                    topPresented_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(topPresented_2, 'tStartRefresh')  # time at next scr refresh
                    topPresented_2.setAutoDraw(True)
                if topPresented_2.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > topPresented_2.tStartRefresh + .5-frameTolerance:
                        # keep track of stop time/frame for later
                        topPresented_2.tStop = t  # not accounting for scr refresh
                        topPresented_2.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(topPresented_2, 'tStopRefresh')  # time at next scr refresh
                        topPresented_2.setAutoDraw(False)
                
                # *rightPresented_2* updates
                if rightPresented_2.status == NOT_STARTED and tThisFlip >= thisISI-frameTolerance:
                    # keep track of start time/frame for later
                    rightPresented_2.frameNStart = frameN  # exact frame index
                    rightPresented_2.tStart = t  # local t and not account for scr refresh
                    rightPresented_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(rightPresented_2, 'tStartRefresh')  # time at next scr refresh
                    rightPresented_2.setAutoDraw(True)
                if rightPresented_2.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > rightPresented_2.tStartRefresh + .5-frameTolerance:
                        # keep track of stop time/frame for later
                        rightPresented_2.tStop = t  # not accounting for scr refresh
                        rightPresented_2.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(rightPresented_2, 'tStopRefresh')  # time at next scr refresh
                        rightPresented_2.setAutoDraw(False)
                
                # *bottomPresented_2* updates
                if bottomPresented_2.status == NOT_STARTED and tThisFlip >= thisISI-frameTolerance:
                    # keep track of start time/frame for later
                    bottomPresented_2.frameNStart = frameN  # exact frame index
                    bottomPresented_2.tStart = t  # local t and not account for scr refresh
                    bottomPresented_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(bottomPresented_2, 'tStartRefresh')  # time at next scr refresh
                    bottomPresented_2.setAutoDraw(True)
                if bottomPresented_2.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > bottomPresented_2.tStartRefresh + .5-frameTolerance:
                        # keep track of stop time/frame for later
                        bottomPresented_2.tStop = t  # not accounting for scr refresh
                        bottomPresented_2.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(bottomPresented_2, 'tStopRefresh')  # time at next scr refresh
                        bottomPresented_2.setAutoDraw(False)
                
                # *leftPresented_2* updates
                if leftPresented_2.status == NOT_STARTED and tThisFlip >= thisISI-frameTolerance:
                    # keep track of start time/frame for later
                    leftPresented_2.frameNStart = frameN  # exact frame index
                    leftPresented_2.tStart = t  # local t and not account for scr refresh
                    leftPresented_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(leftPresented_2, 'tStartRefresh')  # time at next scr refresh
                    leftPresented_2.setAutoDraw(True)
                if leftPresented_2.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > leftPresented_2.tStartRefresh + .5-frameTolerance:
                        # keep track of stop time/frame for later
                        leftPresented_2.tStop = t  # not accounting for scr refresh
                        leftPresented_2.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(leftPresented_2, 'tStopRefresh')  # time at next scr refresh
                        leftPresented_2.setAutoDraw(False)
                #3
                if centerPresented_2.status == STARTED and not triggerSent_1:#
                    if ethnicity == 1 and rotCenter == 0:
                        port.write([0x17]) #S23
                        time.sleep(PulseWidth)
                        triggerSent_1 = True
                        pauseStartTime_1 = t
                    elif ethnicity == 1 and rotCenter == 45:#
                        port.write([0x1B])#S27
                        time.sleep(PulseWidth)
                        triggerSent_1 = True
                        pauseStartTime_1 = t
                    elif ethnicity == 2 and rotCenter == 0:#
                        port.write([0x21])#S33
                        time.sleep(PulseWidth)
                        triggerSent_1 = True
                        pauseStartTime_1 = t
                    elif ethnicity == 2 and rotCenter == 45:#
                        port.write([0x25])#S37
                        time.sleep(PulseWidth)
                        triggerSent_1 = True
                        pauseStartTime_1 = t
                    elif ethnicity == 3 and rotCenter == 0:#
                        port.write([0x2B])#S43
                        time.sleep(PulseWidth)
                        triggerSent_1 = True
                        pauseStartTime_1 = t
                    elif ethnicity == 3 and rotCenter == 45:#
                        port.write([0x2F])#S47
                        time.sleep(PulseWidth)
                        triggerSent_1 = True
                        pauseStartTime_1 = t
                    elif ethnicity == 4 and rotCenter == 0:#
                        port.write([0x35])#S53
                        time.sleep(PulseWidth)
                        triggerSent_1 = True
                        pauseStartTime_1 = t
                    elif ethnicity == 4 and rotCenter == 45:#
                        port.write([0x39])#S57
                        time.sleep(PulseWidth)
                        triggerSent_1 = True
                        pauseStartTime_1 = t
                        
                # we send the 2nd trigger after 40 ms.
                if triggerSent_1 and not portsCleared_1:
                    if t > (pauseStartTime_1 + postTriggerPauseTime_1):
                        if male == 0:
                            if scramFace == 0:
                                if blueCenter == 0:
                                    if blueSurround ==0:
                                        if rotSurround == 0:
                                            port.write([0x68])# S104 for non resp
                                            time.sleep(PulseWidth)
                                            #triggerSent_1 = False
                                            portsCleared_1 = True
                                        elif rotSurround == 45:
                                            port.write([0x6C])#S108
                                            time.sleep(PulseWidth)
                                            #triggerSent_1 = False
                                            portsCleared_1 = True
                                    elif blueSurround == 1:
                                        if rotSurround == 0:
                                            port.write([0x70])# S112 
                                            time.sleep(PulseWidth)
                                            #triggerSent_1 = False
                                            portsCleared_1 = True
                                        elif rotSurround == 45:
                                            port.write([0x75])#S117
                                            time.sleep(PulseWidth)
                                            #triggerSent_1 = False
                                            portsCleared_1 = True
                                elif blueCenter == 1:
                                    if blueSurround ==0:
                                        if rotSurround == 0:
                                            port.write([0x79])# S121 for non resp
                                            time.sleep(PulseWidth)
                                            #triggerSent_1 = False
                                            portsCleared_1 = True
                                        elif rotSurround == 45:
                                            port.write([0x7D])#S125
                                            time.sleep(PulseWidth)
                                            #triggerSent_1 = False
                                            portsCleared_1 = True
                                    elif blueSurround == 1:
                                        if rotSurround == 0:
                                            port.write([0x82])# S130 
                                            time.sleep(PulseWidth)
                                            #triggerSent_1 = False
                                            portsCleared_1 = True
                                        elif rotSurround == 45:
                                            port.write([0x86])#S134
                                            time.sleep(PulseWidth)
                                            #triggerSent_1 = False
                                            portsCleared_1 = True
                            elif scramFace == 1:
                                if blueCenter == 0:
                                    if blueSurround ==0:
                                        if rotSurround == 0:
                                            port.write([0x8A])# S138 for non resp
                                            time.sleep(PulseWidth)
                                            #triggerSent_1 = False
                                            portsCleared_1 = True
                                        elif rotSurround == 45:
                                            port.write([0x8E])#S142
                                            time.sleep(PulseWidth)
                                            #triggerSent_1 = False
                                            portsCleared_1 = True
                                    elif blueSurround == 1:
                                        if rotSurround == 0:
                                            port.write([0x92])# S146 
                                            time.sleep(PulseWidth)
                                            #triggerSent_1 = False
                                            portsCleared_1 = True
                                        elif rotSurround == 45:
                                            port.write([0x96])#S150
                                            time.sleep(PulseWidth)
                                            #triggerSent_1 = False
                                            portsCleared_1 = True
                                elif blueCenter == 1:
                                    if blueSurround ==0:
                                        if rotSurround == 0:
                                            port.write([0x9A])# S154 for non resp
                                            time.sleep(PulseWidth)
                                            #triggerSent_1 = False
                                            portsCleared_1 = True
                                        elif rotSurround == 45:
                                            port.write([0x9E])#S158
                                            time.sleep(PulseWidth)
                                            #triggerSent_1 = False
                                            portsCleared_1 = True
                                    elif blueSurround == 1:
                                        if rotSurround == 0:
                                            port.write([0xA2])# S162 
                                            time.sleep(PulseWidth)
                                            #triggerSent_1 = False
                                            portsCleared_1 = True
                                        elif rotSurround == 45:
                                            port.write([0xA6])#S166
                                            time.sleep(PulseWidth)
                                            #triggerSent_1 = False
                                            portsCleared_1 = True
                        elif male ==1:
                            if scramFace == 0:
                                if blueCenter == 0:
                                    if blueSurround ==0:
                                        if rotSurround == 0:
                                            port.write([0xAA])# S170 for non resp
                                            time.sleep(PulseWidth)
                                            #triggerSent_1 = False
                                            portsCleared_1 = True
                                        elif rotSurround == 45:
                                            port.write([0xAE])#S174
                                            time.sleep(PulseWidth)
                                            #triggerSent_1 = False
                                            portsCleared_1 = True
                                    elif blueSurround == 1:
                                        if rotSurround == 0:
                                            port.write([0xB2])# S178 
                                            time.sleep(PulseWidth)
                                            #triggerSent_1 = False
                                            portsCleared_1 = True
                                        elif rotSurround == 45:
                                            port.write([0xB6])#S182
                                            time.sleep(PulseWidth)
                                            #triggerSent_1 = False
                                            portsCleared_1 = True
                                elif blueCenter == 1:
                                    if blueSurround ==0:
                                        if rotSurround == 0:
                                            port.write([0xBA])# S186 for non resp
                                            time.sleep(PulseWidth)
                                            #triggerSent_1 = False
                                            portsCleared_1 = True
                                        elif rotSurround == 45:
                                            port.write([0xBE])#S190
                                            time.sleep(PulseWidth)
                                            #triggerSent_1 = False
                                            portsCleared_1 = True
                                    elif blueSurround == 1:
                                        if rotSurround == 0:
                                            port.write([0xC2])# S194 
                                            time.sleep(PulseWidth)
                                            #triggerSent_1 = False
                                            portsCleared_1 = True
                                        elif rotSurround == 45:
                                            port.write([0xC6])#S198
                                            time.sleep(PulseWidth)
                                            #triggerSent_1 = False
                                            portsCleared_1 = True
                            elif scramFace == 1:
                                if blueCenter == 0:
                                    if blueSurround ==0:
                                        if rotSurround == 0:
                                            port.write([0xCA])# S202 for non resp
                                            time.sleep(PulseWidth)
                                            #triggerSent_1 = False
                                            portsCleared_1 = True
                                        elif rotSurround == 45:
                                            port.write([0xCE])#S206
                                            time.sleep(PulseWidth)
                                            #triggerSent_1 = False
                                            portsCleared_1 = True
                                    elif blueSurround == 1:
                                        if rotSurround == 0:
                                            port.write([0xD2])# S210 
                                            time.sleep(PulseWidth)
                                            #triggerSent_1 = False
                                            portsCleared_1 = True
                                        elif rotSurround == 45:
                                            port.write([0xD6])#S214
                                            time.sleep(PulseWidth)
                                            #triggerSent_1 = False
                                            portsCleared_1 = True
                                elif blueCenter == 1:
                                    if blueSurround ==0:
                                        if rotSurround == 0:
                                            port.write([0xDA])# S218 for non resp
                                            time.sleep(PulseWidth)
                                            #triggerSent_1 = False
                                            portsCleared_1 = True
                                        elif rotSurround == 45:
                                            port.write([0xDE])#S222
                                            time.sleep(PulseWidth)
                                            #triggerSent_1 = False
                                            portsCleared_1 = True
                                    elif blueSurround == 1:
                                        if rotSurround == 0:
                                            port.write([0xE2])# S226 
                                            time.sleep(PulseWidth)
                                            #triggerSent_1 = False
                                            portsCleared_1 = True
                                        elif rotSurround == 45:
                                            port.write([0xE6])#S230
                                            time.sleep(PulseWidth)
                                            #triggerSent_1 = False
                                            portsCleared_1 = True
                
                # *keyResp_2* updates
                waitOnFlip = False
                if keyResp_2.status == NOT_STARTED and tThisFlip >= thisISI-frameTolerance:
                    # keep track of start time/frame for later
                    keyResp_2.frameNStart = frameN  # exact frame index
                    keyResp_2.tStart = t  # local t and not account for scr refresh
                    keyResp_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(keyResp_2, 'tStartRefresh')  # time at next scr refresh
                    keyResp_2.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(keyResp_2.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(keyResp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if keyResp_2.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > keyResp_2.tStartRefresh + .5-frameTolerance:
                        # keep track of stop time/frame for later
                        keyResp_2.tStop = t  # not accounting for scr refresh
                        keyResp_2.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(keyResp_2, 'tStopRefresh')  # time at next scr refresh
                        keyResp_2.status = FINISHED
                if keyResp_2.status == STARTED and not waitOnFlip:
                    theseKeys = keyResp_2.getKeys(keyList=['1', '8'], waitRelease=False)
                    _keyResp_2_allKeys.extend(theseKeys)
                    if len(_keyResp_2_allKeys):
                        keyResp_2.keys = _keyResp_2_allKeys[0].name  # just the first key pressed
                        keyResp_2.rt = _keyResp_2_allKeys[0].rt
                        # was this correct?
                        if (keyResp_2.keys == str(corrAns)) or (keyResp_2.keys == corrAns):
                            keyResp_2.corr = 1
                        else:
                            keyResp_2.corr = 0
                        # a response ends the routine
                        continueRoutine = False
                #3
                if keyResp_2.keys and len(keyResp_2.keys) > len(keys_counted):# A key response has been made but we haven't yet "counted" it
                    keys_counted.append(keyResp_2.keys[-1])
                    if keyResp_2.keys[-1] == corrAns:# if the last key pressed was correct
                        port.write([0x10]) # send trigger
                        mark_start_time = globalClock.getTime() # fetch time on global clock (where is this used?)
                        triggerSent = True
                        portsCleared = False
                        pauseStartTime = t
                    elif keyResp_2.keys[-1] != corrAns:# if the last key pressed was not correct
                        port.write([0x04])# send different trigger
                        mark_start_time = globalClock.getTime()
                        triggerSent = True
                        portsCleared = False
                        pauseStartTime = t
                
                # if a trigger was send, "clear" the bugger after 100ms
                if triggerSent and not portsCleared:
                    if t > (pauseStartTime + postTriggerPauseTime):
                        # Clear ports
                        #port.write([0xFF])
                        triggerSent = False
                        portsCleared = True
                
                
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in prac_StimRoutineComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "prac_StimRoutine"-------
            for thisComponent in prac_StimRoutineComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            prac_stimLoop.addData('LeftReminder_text_7.started', LeftReminder_text_7.tStartRefresh)
            prac_stimLoop.addData('LeftReminder_text_7.stopped', LeftReminder_text_7.tStopRefresh)
            prac_stimLoop.addData('rightReminder_text_7.started', rightReminder_text_7.tStartRefresh)
            prac_stimLoop.addData('rightReminder_text_7.stopped', rightReminder_text_7.tStopRefresh)
            prac_stimLoop.addData('centerPresented_2.started', centerPresented_2.tStartRefresh)
            prac_stimLoop.addData('centerPresented_2.stopped', centerPresented_2.tStopRefresh)
            prac_stimLoop.addData('topPresented_2.started', topPresented_2.tStartRefresh)
            prac_stimLoop.addData('topPresented_2.stopped', topPresented_2.tStopRefresh)
            prac_stimLoop.addData('rightPresented_2.started', rightPresented_2.tStartRefresh)
            prac_stimLoop.addData('rightPresented_2.stopped', rightPresented_2.tStopRefresh)
            prac_stimLoop.addData('bottomPresented_2.started', bottomPresented_2.tStartRefresh)
            prac_stimLoop.addData('bottomPresented_2.stopped', bottomPresented_2.tStopRefresh)
            prac_stimLoop.addData('leftPresented_2.started', leftPresented_2.tStartRefresh)
            prac_stimLoop.addData('leftPresented_2.stopped', leftPresented_2.tStopRefresh)
            #4
            
            Connected = False
            thread.join(1.0)
            # check responses
            if keyResp_2.keys in ['', [], None]:  # No response was made
                keyResp_2.keys = None
                # was no response the correct answer?!
                if str(corrAns).lower() == 'none':
                   keyResp_2.corr = 1;  # correct non-response
                else:
                   keyResp_2.corr = 0;  # failed to respond (incorrectly)
            # store data for prac_stimLoop (TrialHandler)
            prac_stimLoop.addData('keyResp_2.keys',keyResp_2.keys)
            prac_stimLoop.addData('keyResp_2.corr', keyResp_2.corr)
            if keyResp_2.keys != None:  # we had a response
                prac_stimLoop.addData('keyResp_2.rt', keyResp_2.rt)
            prac_stimLoop.addData('keyResp_2.started', keyResp_2.tStartRefresh)
            prac_stimLoop.addData('keyResp_2.stopped', keyResp_2.tStopRefresh)
            #4
            if not keyResp_2.keys or len(keyResp_2.keys) == 0:
                   port.write([0x03])# send a trigger
                   mark_start_time = globalClock.getTime()# fetch time on global clock (where is this saved)
            
            
            
            # the Routine "prac_StimRoutine" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # ------Prepare to start Routine "break_prac_stimLoop"-------
            continueRoutine = True
            # update component parameters for each repeat
            # keep track of which components have finished
            break_prac_stimLoopComponents = []
            for thisComponent in break_prac_stimLoopComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            break_prac_stimLoopClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "break_prac_stimLoop"-------
            while continueRoutine:
                # get current time
                t = break_prac_stimLoopClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=break_prac_stimLoopClock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in break_prac_stimLoopComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "break_prac_stimLoop"-------
            for thisComponent in break_prac_stimLoopComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            #store 1back stim from this trial as 2back for next trial
            #back2_rotCenter = back1_rotCenter
            #back2_blueCenter = back1_blueCenter
            
            #store current stim from this trial as 1back for next trial
            #back1_rotCenter = rotCenter
            #back1_blueCenter = blueCenter
            
            prac_stimLoop.finished=True
            
            # the Routine "break_prac_stimLoop" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            thisExp.nextEntry()
            
        # completed 1.0 repeats of 'prac_stimLoop'
        
        thisExp.nextEntry()
        
    # completed numberReps repeats of 'prac_trialLoop'
    
    
    # ------Prepare to start Routine "taskEnd_instruct"-------
    continueRoutine = True
    # update component parameters for each repeat
    if practice == 1:
        taskEnd_text_source ='You have completed this practice session. \n \n \n \n \n \n \n \n \n \n Press the left or right button to continue to the next game'
    elif practice == 0:
        taskEnd_text_source ='You have completed the game. \n \n \n \n \n \n \n \n \n \n Press the left or right button to learn about the next game'
    
    
    taskEnd_text.setText(taskEnd_text_source)
    key_resp.keys = []
    key_resp.rt = []
    _key_resp_allKeys = []
    # keep track of which components have finished
    taskEnd_instructComponents = [taskEnd_text, key_resp]
    for thisComponent in taskEnd_instructComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    taskEnd_instructClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "taskEnd_instruct"-------
    while continueRoutine:
        # get current time
        t = taskEnd_instructClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=taskEnd_instructClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *taskEnd_text* updates
        if taskEnd_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            taskEnd_text.frameNStart = frameN  # exact frame index
            taskEnd_text.tStart = t  # local t and not account for scr refresh
            taskEnd_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(taskEnd_text, 'tStartRefresh')  # time at next scr refresh
            taskEnd_text.setAutoDraw(True)
        
        # *key_resp* updates
        waitOnFlip = False
        if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp.frameNStart = frameN  # exact frame index
            key_resp.tStart = t  # local t and not account for scr refresh
            key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
            key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp.status == STARTED and not waitOnFlip:
            theseKeys = key_resp.getKeys(keyList=['1', '8'], waitRelease=False)
            _key_resp_allKeys.extend(theseKeys)
            if len(_key_resp_allKeys):
                key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
                key_resp.rt = _key_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in taskEnd_instructComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "taskEnd_instruct"-------
    for thisComponent in taskEnd_instructComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    prac_BlockLoop.addData('taskEnd_text.started', taskEnd_text.tStartRefresh)
    prac_BlockLoop.addData('taskEnd_text.stopped', taskEnd_text.tStopRefresh)
    # check responses
    if key_resp.keys in ['', [], None]:  # No response was made
        key_resp.keys = None
    prac_BlockLoop.addData('key_resp.keys',key_resp.keys)
    if key_resp.keys != None:  # we had a response
        prac_BlockLoop.addData('key_resp.rt', key_resp.rt)
    prac_BlockLoop.addData('key_resp.started', key_resp.tStartRefresh)
    prac_BlockLoop.addData('key_resp.stopped', key_resp.tStopRefresh)
    # the Routine "taskEnd_instruct" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'prac_BlockLoop'


# set up handler to look after randomisation of conditions etc
blockLoop = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('inhibblockSelect.csv'),
    seed=None, name='blockLoop')
thisExp.addLoop(blockLoop)  # add the loop to the experiment
thisBlockLoop = blockLoop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisBlockLoop.rgb)
if thisBlockLoop != None:
    for paramName in thisBlockLoop:
        exec('{} = thisBlockLoop[paramName]'.format(paramName))

for thisBlockLoop in blockLoop:
    currentLoop = blockLoop
    # abbreviate parameter names if possible (e.g. rgb = thisBlockLoop.rgb)
    if thisBlockLoop != None:
        for paramName in thisBlockLoop:
            exec('{} = thisBlockLoop[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "task_instruct"-------
    continueRoutine = True
    # update component parameters for each repeat
    if CB =='BSOD':
        blueKey = '1'
        squareKey = '1'
        orangeKey = '8'
        diagKey = '8'   
        if whichBlock == 'color.xlsx':
            leftKeyText = 'the center image is BLUE \n'
            rightKeyText = '\n \n \n \n \n \n the center image is ORANGE'
            leftReminder = 'BLUE - SQUARE'
            rightReminder = 'ORANGE - DIAMOND'
        elif whichBlock == 'shape.xlsx':
            leftKeyText = 'the center image is a SQUARE \n'
            rightKeyText = '\n \n \n \n \n \n the center image is DIAMOND'
            leftReminder = 'BLUE - SQUARE'
            rightReminder = 'ORANGE - DIAMOND'
        elif whichBlock == 'switch.xlsx':
            leftKeyText = '\n \n \n \n \n the word says COLOR and the image is BLUE, \n or if the word says SHAPE and the image is a SQUARE \n'
            rightKeyText = '\n \n \n \n \n \n \n \n \n \n \n \n \n the word says COLOR and the image is ORANGE, \n or if the word says SHAPE and the image is a DIAMOND'
            leftReminder = 'BLUE - SQUARE'
            rightReminder = 'ORANGE - DIAMOND'
    #    elif whichBlock == 'oneBackColor.xlsx':
    #        leftKeyText = 'the center image is the SAME COLOR as \n the image presented one image previously (1BACK) \n'
    #        rightKeyText = '\n \n \n \n \n \n \n \n \n \n the center image is a DIFFERENT COLOR as \n the image presented one image previously (1BACK)'
    #        leftReminder = 'SAME'
    #        rightReminder = 'DIFFERENT'
    #    elif whichBlock == 'twoBackColor.xlsx':
    #        leftKeyText = 'the center image is the SAME COLOR as \n the image presented TWO images previously (2BACK) \n'
    #        rightKeyText = '\n \n \n \n \n \n \n \n \n \n the center image is the DIFFERENT COLOR as \n the image presented TWO images previously (2BACK)'
    #        leftReminder = 'SAME'
    #        rightReminder = 'DIFFERENT'
    
    elif CB =='BDOS':
        blueKey = '1'
        squareKey = '8'
        orangeKey = '8'
        diagKey = '1'
    elif CB =='ODBS':
        blueKey = '8'
        squareKey = '8'
        orangeKey = '1'
        diagKey = '1'
    elif CB =='OSBD':
        blueKey = '8'
        squareKey = '1'
        orangeKey = '1'
        diagKey = '8'
    taskName.setText(taskNameSource)
    task_Text.setText(taskTextSource)
    leftKey_text.setText(leftKeyText)
    rightKey_text.setText(rightKeyText)
    LeftReminder_text.setText(leftReminder)
    rightReminder_text.setText(rightReminder)
    pracOrMain_keyResp.keys = []
    pracOrMain_keyResp.rt = []
    _pracOrMain_keyResp_allKeys = []
    # keep track of which components have finished
    task_instructComponents = [taskName, task_Text, leftKey_text, rightKey_text, task_text5, LeftReminder_text, rightReminder_text, pracOrMain_keyResp]
    for thisComponent in task_instructComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    task_instructClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "task_instruct"-------
    while continueRoutine:
        # get current time
        t = task_instructClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=task_instructClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *taskName* updates
        if taskName.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            taskName.frameNStart = frameN  # exact frame index
            taskName.tStart = t  # local t and not account for scr refresh
            taskName.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(taskName, 'tStartRefresh')  # time at next scr refresh
            taskName.setAutoDraw(True)
        
        # *task_Text* updates
        if task_Text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            task_Text.frameNStart = frameN  # exact frame index
            task_Text.tStart = t  # local t and not account for scr refresh
            task_Text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(task_Text, 'tStartRefresh')  # time at next scr refresh
            task_Text.setAutoDraw(True)
        
        # *leftKey_text* updates
        if leftKey_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            leftKey_text.frameNStart = frameN  # exact frame index
            leftKey_text.tStart = t  # local t and not account for scr refresh
            leftKey_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(leftKey_text, 'tStartRefresh')  # time at next scr refresh
            leftKey_text.setAutoDraw(True)
        
        # *rightKey_text* updates
        if rightKey_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            rightKey_text.frameNStart = frameN  # exact frame index
            rightKey_text.tStart = t  # local t and not account for scr refresh
            rightKey_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(rightKey_text, 'tStartRefresh')  # time at next scr refresh
            rightKey_text.setAutoDraw(True)
        
        # *task_text5* updates
        if task_text5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            task_text5.frameNStart = frameN  # exact frame index
            task_text5.tStart = t  # local t and not account for scr refresh
            task_text5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(task_text5, 'tStartRefresh')  # time at next scr refresh
            task_text5.setAutoDraw(True)
        
        # *LeftReminder_text* updates
        if LeftReminder_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            LeftReminder_text.frameNStart = frameN  # exact frame index
            LeftReminder_text.tStart = t  # local t and not account for scr refresh
            LeftReminder_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(LeftReminder_text, 'tStartRefresh')  # time at next scr refresh
            LeftReminder_text.setAutoDraw(True)
        
        # *rightReminder_text* updates
        if rightReminder_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            rightReminder_text.frameNStart = frameN  # exact frame index
            rightReminder_text.tStart = t  # local t and not account for scr refresh
            rightReminder_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(rightReminder_text, 'tStartRefresh')  # time at next scr refresh
            rightReminder_text.setAutoDraw(True)
        
        # *pracOrMain_keyResp* updates
        waitOnFlip = False
        if pracOrMain_keyResp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            pracOrMain_keyResp.frameNStart = frameN  # exact frame index
            pracOrMain_keyResp.tStart = t  # local t and not account for scr refresh
            pracOrMain_keyResp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(pracOrMain_keyResp, 'tStartRefresh')  # time at next scr refresh
            pracOrMain_keyResp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(pracOrMain_keyResp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(pracOrMain_keyResp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if pracOrMain_keyResp.status == STARTED and not waitOnFlip:
            theseKeys = pracOrMain_keyResp.getKeys(keyList=['1', '8'], waitRelease=False)
            _pracOrMain_keyResp_allKeys.extend(theseKeys)
            if len(_pracOrMain_keyResp_allKeys):
                pracOrMain_keyResp.keys = _pracOrMain_keyResp_allKeys[-1].name  # just the last key pressed
                pracOrMain_keyResp.rt = _pracOrMain_keyResp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in task_instructComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "task_instruct"-------
    for thisComponent in task_instructComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    blockLoop.addData('taskName.started', taskName.tStartRefresh)
    blockLoop.addData('taskName.stopped', taskName.tStopRefresh)
    blockLoop.addData('task_Text.started', task_Text.tStartRefresh)
    blockLoop.addData('task_Text.stopped', task_Text.tStopRefresh)
    blockLoop.addData('leftKey_text.started', leftKey_text.tStartRefresh)
    blockLoop.addData('leftKey_text.stopped', leftKey_text.tStopRefresh)
    blockLoop.addData('rightKey_text.started', rightKey_text.tStartRefresh)
    blockLoop.addData('rightKey_text.stopped', rightKey_text.tStopRefresh)
    blockLoop.addData('task_text5.started', task_text5.tStartRefresh)
    blockLoop.addData('task_text5.stopped', task_text5.tStopRefresh)
    blockLoop.addData('LeftReminder_text.started', LeftReminder_text.tStartRefresh)
    blockLoop.addData('LeftReminder_text.stopped', LeftReminder_text.tStopRefresh)
    blockLoop.addData('rightReminder_text.started', rightReminder_text.tStartRefresh)
    blockLoop.addData('rightReminder_text.stopped', rightReminder_text.tStopRefresh)
    # check responses
    if pracOrMain_keyResp.keys in ['', [], None]:  # No response was made
        pracOrMain_keyResp.keys = None
    blockLoop.addData('pracOrMain_keyResp.keys',pracOrMain_keyResp.keys)
    if pracOrMain_keyResp.keys != None:  # we had a response
        blockLoop.addData('pracOrMain_keyResp.rt', pracOrMain_keyResp.rt)
    blockLoop.addData('pracOrMain_keyResp.started', pracOrMain_keyResp.tStartRefresh)
    blockLoop.addData('pracOrMain_keyResp.stopped', pracOrMain_keyResp.tStopRefresh)
    # the Routine "task_instruct" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "task_instruct2"-------
    continueRoutine = True
    # update component parameters for each repeat
    if practice == 1:
        startText ='\n \n \n \n \n \n \n \n \n \n \n \n \n \n Press either the left or right button to practice this game'
    elif practice == 0:
            startText ='\n \n \n \n \n \n \n \n \n \n \n \n \n \n Press either the left or right button to start the real game'
    
    
    taskName_2.setText(taskNameSource)
    task_Text_2.setText('\n\nPlease rest your left finger on the left button and your right finger on the right button.\nWhen an image is shown, you should respond as quickly as you can while also being correct.')
    task_text_3.setText(cueReminderTextSource)
    task_text_4.setText(startText)
    LeftReminder_text_5.setText(leftReminder)
    rightReminder_text_5.setText(rightReminder)
    pracOrMain_keyResp_3.keys = []
    pracOrMain_keyResp_3.rt = []
    _pracOrMain_keyResp_3_allKeys = []
    # keep track of which components have finished
    task_instruct2Components = [taskName_2, task_Text_2, task_text_3, task_text_4, LeftReminder_text_5, rightReminder_text_5, pracOrMain_keyResp_3]
    for thisComponent in task_instruct2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    task_instruct2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "task_instruct2"-------
    while continueRoutine:
        # get current time
        t = task_instruct2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=task_instruct2Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *taskName_2* updates
        if taskName_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            taskName_2.frameNStart = frameN  # exact frame index
            taskName_2.tStart = t  # local t and not account for scr refresh
            taskName_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(taskName_2, 'tStartRefresh')  # time at next scr refresh
            taskName_2.setAutoDraw(True)
        
        # *task_Text_2* updates
        if task_Text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            task_Text_2.frameNStart = frameN  # exact frame index
            task_Text_2.tStart = t  # local t and not account for scr refresh
            task_Text_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(task_Text_2, 'tStartRefresh')  # time at next scr refresh
            task_Text_2.setAutoDraw(True)
        
        # *task_text_3* updates
        if task_text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            task_text_3.frameNStart = frameN  # exact frame index
            task_text_3.tStart = t  # local t and not account for scr refresh
            task_text_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(task_text_3, 'tStartRefresh')  # time at next scr refresh
            task_text_3.setAutoDraw(True)
        
        # *task_text_4* updates
        if task_text_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            task_text_4.frameNStart = frameN  # exact frame index
            task_text_4.tStart = t  # local t and not account for scr refresh
            task_text_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(task_text_4, 'tStartRefresh')  # time at next scr refresh
            task_text_4.setAutoDraw(True)
        
        # *LeftReminder_text_5* updates
        if LeftReminder_text_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            LeftReminder_text_5.frameNStart = frameN  # exact frame index
            LeftReminder_text_5.tStart = t  # local t and not account for scr refresh
            LeftReminder_text_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(LeftReminder_text_5, 'tStartRefresh')  # time at next scr refresh
            LeftReminder_text_5.setAutoDraw(True)
        
        # *rightReminder_text_5* updates
        if rightReminder_text_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            rightReminder_text_5.frameNStart = frameN  # exact frame index
            rightReminder_text_5.tStart = t  # local t and not account for scr refresh
            rightReminder_text_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(rightReminder_text_5, 'tStartRefresh')  # time at next scr refresh
            rightReminder_text_5.setAutoDraw(True)
        
        # *pracOrMain_keyResp_3* updates
        waitOnFlip = False
        if pracOrMain_keyResp_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            pracOrMain_keyResp_3.frameNStart = frameN  # exact frame index
            pracOrMain_keyResp_3.tStart = t  # local t and not account for scr refresh
            pracOrMain_keyResp_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(pracOrMain_keyResp_3, 'tStartRefresh')  # time at next scr refresh
            pracOrMain_keyResp_3.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(pracOrMain_keyResp_3.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(pracOrMain_keyResp_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if pracOrMain_keyResp_3.status == STARTED and not waitOnFlip:
            theseKeys = pracOrMain_keyResp_3.getKeys(keyList=['1', '8'], waitRelease=False)
            _pracOrMain_keyResp_3_allKeys.extend(theseKeys)
            if len(_pracOrMain_keyResp_3_allKeys):
                pracOrMain_keyResp_3.keys = _pracOrMain_keyResp_3_allKeys[-1].name  # just the last key pressed
                pracOrMain_keyResp_3.rt = _pracOrMain_keyResp_3_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in task_instruct2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "task_instruct2"-------
    for thisComponent in task_instruct2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    blockLoop.addData('taskName_2.started', taskName_2.tStartRefresh)
    blockLoop.addData('taskName_2.stopped', taskName_2.tStopRefresh)
    blockLoop.addData('task_Text_2.started', task_Text_2.tStartRefresh)
    blockLoop.addData('task_Text_2.stopped', task_Text_2.tStopRefresh)
    blockLoop.addData('task_text_3.started', task_text_3.tStartRefresh)
    blockLoop.addData('task_text_3.stopped', task_text_3.tStopRefresh)
    blockLoop.addData('task_text_4.started', task_text_4.tStartRefresh)
    blockLoop.addData('task_text_4.stopped', task_text_4.tStopRefresh)
    blockLoop.addData('LeftReminder_text_5.started', LeftReminder_text_5.tStartRefresh)
    blockLoop.addData('LeftReminder_text_5.stopped', LeftReminder_text_5.tStopRefresh)
    blockLoop.addData('rightReminder_text_5.started', rightReminder_text_5.tStartRefresh)
    blockLoop.addData('rightReminder_text_5.stopped', rightReminder_text_5.tStopRefresh)
    # check responses
    if pracOrMain_keyResp_3.keys in ['', [], None]:  # No response was made
        pracOrMain_keyResp_3.keys = None
    blockLoop.addData('pracOrMain_keyResp_3.keys',pracOrMain_keyResp_3.keys)
    if pracOrMain_keyResp_3.keys != None:  # we had a response
        blockLoop.addData('pracOrMain_keyResp_3.rt', pracOrMain_keyResp_3.rt)
    blockLoop.addData('pracOrMain_keyResp_3.started', pracOrMain_keyResp_3.tStartRefresh)
    blockLoop.addData('pracOrMain_keyResp_3.stopped', pracOrMain_keyResp_3.tStopRefresh)
    # the Routine "task_instruct2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    trialLoop = data.TrialHandler(nReps=numberReps, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('faceSelect.xlsx'),
        seed=None, name='trialLoop')
    thisExp.addLoop(trialLoop)  # add the loop to the experiment
    thisTrialLoop = trialLoop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrialLoop.rgb)
    if thisTrialLoop != None:
        for paramName in thisTrialLoop:
            exec('{} = thisTrialLoop[paramName]'.format(paramName))
    
    for thisTrialLoop in trialLoop:
        currentLoop = trialLoop
        # abbreviate parameter names if possible (e.g. rgb = thisTrialLoop.rgb)
        if thisTrialLoop != None:
            for paramName in thisTrialLoop:
                exec('{} = thisTrialLoop[paramName]'.format(paramName))
        
        # set up handler to look after randomisation of conditions etc
        cueLoop = data.TrialHandler(nReps=1, method='fullRandom', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions(whichBlock),
            seed=None, name='cueLoop')
        thisExp.addLoop(cueLoop)  # add the loop to the experiment
        thisCueLoop = cueLoop.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisCueLoop.rgb)
        if thisCueLoop != None:
            for paramName in thisCueLoop:
                exec('{} = thisCueLoop[paramName]'.format(paramName))
        
        for thisCueLoop in cueLoop:
            currentLoop = cueLoop
            # abbreviate parameter names if possible (e.g. rgb = thisCueLoop.rgb)
            if thisCueLoop != None:
                for paramName in thisCueLoop:
                    exec('{} = thisCueLoop[paramName]'.format(paramName))
            
            # ------Prepare to start Routine "cueRoutine"-------
            continueRoutine = True
            # update component parameters for each repeat
            # pick the ISI for the next routine
            # this code component is set to 'both' because we need to remove the 'np'
            # at the start of np.linspace (this is a python library JS won't know what to call. 
            
            # make range from a to b in n stepsizes
            RSIRange = np.linspace(1000, 1500, 500)
            # picking from a shuffled array is easier for random selection in JS
            shuffle(RSIRange)
            thisRSI = RSIRange[0]/1000 # the first item of the shuffled array 
            
            reminderDur = thisRSI +1
            
            # show in console for debugging
            print('thisRSI: ', thisRSI)
            
            # save this ISI to our output file
            cueLoop.addData('RSI', thisRSI)
            LeftReminder_text_3.setText(leftReminder)
            rightReminder_text_3.setText(rightReminder)
            cuePresented.setText(whichCue)
            #2
            pulse_started = False
            pulse_ended = False
            
            
            # keep track of which components have finished
            cueRoutineComponents = [LeftReminder_text_3, rightReminder_text_3, cuePresented]
            for thisComponent in cueRoutineComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            cueRoutineClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "cueRoutine"-------
            while continueRoutine:
                # get current time
                t = cueRoutineClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=cueRoutineClock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *LeftReminder_text_3* updates
                if LeftReminder_text_3.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                    # keep track of start time/frame for later
                    LeftReminder_text_3.frameNStart = frameN  # exact frame index
                    LeftReminder_text_3.tStart = t  # local t and not account for scr refresh
                    LeftReminder_text_3.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(LeftReminder_text_3, 'tStartRefresh')  # time at next scr refresh
                    LeftReminder_text_3.setAutoDraw(True)
                if LeftReminder_text_3.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > LeftReminder_text_3.tStartRefresh + reminderDur-frameTolerance:
                        # keep track of stop time/frame for later
                        LeftReminder_text_3.tStop = t  # not accounting for scr refresh
                        LeftReminder_text_3.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(LeftReminder_text_3, 'tStopRefresh')  # time at next scr refresh
                        LeftReminder_text_3.setAutoDraw(False)
                
                # *rightReminder_text_3* updates
                if rightReminder_text_3.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                    # keep track of start time/frame for later
                    rightReminder_text_3.frameNStart = frameN  # exact frame index
                    rightReminder_text_3.tStart = t  # local t and not account for scr refresh
                    rightReminder_text_3.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(rightReminder_text_3, 'tStartRefresh')  # time at next scr refresh
                    rightReminder_text_3.setAutoDraw(True)
                if rightReminder_text_3.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > rightReminder_text_3.tStartRefresh + reminderDur-frameTolerance:
                        # keep track of stop time/frame for later
                        rightReminder_text_3.tStop = t  # not accounting for scr refresh
                        rightReminder_text_3.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(rightReminder_text_3, 'tStopRefresh')  # time at next scr refresh
                        rightReminder_text_3.setAutoDraw(False)
                
                # *cuePresented* updates
                if cuePresented.status == NOT_STARTED and tThisFlip >= thisRSI-frameTolerance:
                    # keep track of start time/frame for later
                    cuePresented.frameNStart = frameN  # exact frame index
                    cuePresented.tStart = t  # local t and not account for scr refresh
                    cuePresented.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(cuePresented, 'tStartRefresh')  # time at next scr refresh
                    cuePresented.setAutoDraw(True)
                if cuePresented.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > cuePresented.tStartRefresh + .5-frameTolerance:
                        # keep track of stop time/frame for later
                        cuePresented.tStop = t  # not accounting for scr refresh
                        cuePresented.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(cuePresented, 'tStopRefresh')  # time at next scr refresh
                        cuePresented.setAutoDraw(False)
                #3
                if cuePresented.status == STARTED and not pulse_started:
                    if whichCue == 'SHAPE':
                        port.write([0x01])#S1 for 'SHAPE' cue. 
                        pulse_start_time = globalClock.getTime()
                        pulse_started = True
                    elif whichCue == 'COLOR':
                        port.write([0x02])#S2 for 'COLOR' cue. 
                        pulse_start_time = globalClock.getTime()
                        pulse_started = True
                if pulse_started and not pulse_ended:
                    if globalClock.getTime() - pulse_start_time >= 0.005:
                        #port.write([0x02])
                        pulse_ended = True
                
                
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in cueRoutineComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "cueRoutine"-------
            for thisComponent in cueRoutineComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            cueLoop.addData('LeftReminder_text_3.started', LeftReminder_text_3.tStartRefresh)
            cueLoop.addData('LeftReminder_text_3.stopped', LeftReminder_text_3.tStopRefresh)
            cueLoop.addData('rightReminder_text_3.started', rightReminder_text_3.tStartRefresh)
            cueLoop.addData('rightReminder_text_3.stopped', rightReminder_text_3.tStopRefresh)
            cueLoop.addData('cuePresented.started', cuePresented.tStartRefresh)
            cueLoop.addData('cuePresented.stopped', cuePresented.tStopRefresh)
            #4
            
            
            # the Routine "cueRoutine" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # ------Prepare to start Routine "break_cueLoop"-------
            continueRoutine = True
            # update component parameters for each repeat
            # keep track of which components have finished
            break_cueLoopComponents = []
            for thisComponent in break_cueLoopComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            break_cueLoopClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "break_cueLoop"-------
            while continueRoutine:
                # get current time
                t = break_cueLoopClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=break_cueLoopClock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in break_cueLoopComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "break_cueLoop"-------
            for thisComponent in break_cueLoopComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            cueLoop.finished=True
            
            # the Routine "break_cueLoop" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            thisExp.nextEntry()
            
        # completed 1 repeats of 'cueLoop'
        
        
        # set up handler to look after randomisation of conditions etc
        stimLoop = data.TrialHandler(nReps=1, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions(whichFace),
            seed=None, name='stimLoop')
        thisExp.addLoop(stimLoop)  # add the loop to the experiment
        thisStimLoop = stimLoop.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisStimLoop.rgb)
        if thisStimLoop != None:
            for paramName in thisStimLoop:
                exec('{} = thisStimLoop[paramName]'.format(paramName))
        
        for thisStimLoop in stimLoop:
            currentLoop = stimLoop
            # abbreviate parameter names if possible (e.g. rgb = thisStimLoop.rgb)
            if thisStimLoop != None:
                for paramName in thisStimLoop:
                    exec('{} = thisStimLoop[paramName]'.format(paramName))
            
            # ------Prepare to start Routine "StimRoutine"-------
            continueRoutine = True
            # update component parameters for each repeat
            # pick the ISI for the next routine
            # this code component is set to 'both' because we need to remove the 'np'
            # at the start of np.linspace (this is a python library JS won't know what to call. 
            
            # make range from a to b in n stepsizes
            ISIRange = np.linspace(1000, 1500, 500)
            # picking from a shuffled array is easier for random selection in JS
            shuffle(ISIRange)
            thisISI = ISIRange[0]/1000 # the first item of the shuffled array 
            
            reminderDur = thisISI +1
            
            # show in console for debugging
            print('thisISI: ', thisISI)
            
            # save this ISI to our output file
            stimLoop.addData('ISI', thisISI)
            if whichCue == 'SHAPE':
                if rotCenter == 315:
                    corrAns = diagKey
                else:
                    corrAns = squareKey
            elif whichCue == 'COLOR':
                if blueCenter == 1:
                    corrAns = blueKey
                else:
                    corrAns = orangeKey
            #elif whichCue == '1BACK COLOR':
            #    if back1_blueCenter == 1:
            #        corrAns = blueKey
            #    else:
            #        corrAns = orangeKey
            #elif whichCue == '1BACK SHAPE':
            #    if back1_blueCenter == 1:
            #        corrAns = diagKey
            #    else:
            #        corrAns = squareKey
            #elif whichCue == '2BACK COLOR':
            #    if back2_blueCenter == 1:
            #        corrAns = blueKey
            #    else:
            #        corrAns = orangeKey
            #elif whichCue == '2BACK SHAPE':
            #    if back2_blueCenter == 1:
            #        corrAns = diagKey
            #    else:
            #        corrAns = squareKey
            
            # save corrAns to our output file
            stimLoop.addData('corrAns', corrAns)
            
            
            #        if key_resp_3.corr:
            #            corrAns == 'm'
            #            right = 'resources/assets/BlueBoatWhite.png'
            #        else:
            #            left = 'resources/assets/RedRabbitWhite.png'
            #    elif key_resp_3.keys[0] =='m':
            #        if key_resp_3.corr:
            #            right = 'resources/assets/BlueBoatRed.png'
            #           left = 'resources/assets/RedRabbitWhite.png'
            #           audio = 'resources/assets/Thatsright.mp3'
            #       else:
            #else: # thi is classed as an incorrect response
            #    if corrAns == 'm':
            #        right = 'resources/assets/BlueBoatRed.png'
            
            
            ## make range from a to b in n stepsizes
            #ISIRange = np.linspace(1000, 1500, 500)
            ## picking from a shuffled array is easier for random selection in JS
            #shuffle(ISIRange)
            #thisISI = ISIRange[0]/1000 # the first item of the shuffled array 
            
            ## show in console for debugging
            #print('thisISI: ', thisISI)
            
            
            
            
            LeftReminder_text_4.setText(leftReminder)
            rightReminder_text_4.setText(rightReminder)
            centerPresented.setOri(rotCenter)
            centerPresented.setImage(center)
            topPresented.setOri(rotSurround)
            topPresented.setImage(surround)
            rightPresented.setOri(rotSurround)
            rightPresented.setImage(surround)
            bottomPresented.setOri(rotSurround)
            bottomPresented.setImage(surround)
            leftPresented.setOri(rotSurround)
            leftPresented.setImage(surround)
            
            # Clear ports
            #port.write([0xFF])
            
            
            
            # time to wait before clearing the ports after a trigger (in seconds)
            postTriggerPauseTime_1 = 0.04
            pauseStartTime_1 = 0
            triggerSent_1 = False
            portsCleared_1 = False
            
            
            keyResp.keys = []
            keyResp.rt = []
            _keyResp_allKeys = []
            #2
            mark_started = False
            mark_ended = False
            
            # Clear ports
            port.write([0x00])
            Connected = False
            thread.join(1.0)
            
            keys_counted = []
            
            # time to wait before clearing the ports after a trigger (in seconds)
            postTriggerPauseTime = 0.05
            pauseStartTime = 0
            triggerSent = False
            portsCleared = True
            # keep track of which components have finished
            StimRoutineComponents = [LeftReminder_text_4, rightReminder_text_4, centerPresented, topPresented, rightPresented, bottomPresented, leftPresented, keyResp]
            for thisComponent in StimRoutineComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            StimRoutineClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "StimRoutine"-------
            while continueRoutine:
                # get current time
                t = StimRoutineClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=StimRoutineClock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *LeftReminder_text_4* updates
                if LeftReminder_text_4.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                    # keep track of start time/frame for later
                    LeftReminder_text_4.frameNStart = frameN  # exact frame index
                    LeftReminder_text_4.tStart = t  # local t and not account for scr refresh
                    LeftReminder_text_4.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(LeftReminder_text_4, 'tStartRefresh')  # time at next scr refresh
                    LeftReminder_text_4.setAutoDraw(True)
                if LeftReminder_text_4.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > LeftReminder_text_4.tStartRefresh + reminderDur-frameTolerance:
                        # keep track of stop time/frame for later
                        LeftReminder_text_4.tStop = t  # not accounting for scr refresh
                        LeftReminder_text_4.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(LeftReminder_text_4, 'tStopRefresh')  # time at next scr refresh
                        LeftReminder_text_4.setAutoDraw(False)
                
                # *rightReminder_text_4* updates
                if rightReminder_text_4.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                    # keep track of start time/frame for later
                    rightReminder_text_4.frameNStart = frameN  # exact frame index
                    rightReminder_text_4.tStart = t  # local t and not account for scr refresh
                    rightReminder_text_4.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(rightReminder_text_4, 'tStartRefresh')  # time at next scr refresh
                    rightReminder_text_4.setAutoDraw(True)
                if rightReminder_text_4.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > rightReminder_text_4.tStartRefresh + reminderDur-frameTolerance:
                        # keep track of stop time/frame for later
                        rightReminder_text_4.tStop = t  # not accounting for scr refresh
                        rightReminder_text_4.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(rightReminder_text_4, 'tStopRefresh')  # time at next scr refresh
                        rightReminder_text_4.setAutoDraw(False)
                
                # *centerPresented* updates
                if centerPresented.status == NOT_STARTED and tThisFlip >= thisISI-frameTolerance:
                    # keep track of start time/frame for later
                    centerPresented.frameNStart = frameN  # exact frame index
                    centerPresented.tStart = t  # local t and not account for scr refresh
                    centerPresented.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(centerPresented, 'tStartRefresh')  # time at next scr refresh
                    centerPresented.setAutoDraw(True)
                if centerPresented.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > centerPresented.tStartRefresh + .5-frameTolerance:
                        # keep track of stop time/frame for later
                        centerPresented.tStop = t  # not accounting for scr refresh
                        centerPresented.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(centerPresented, 'tStopRefresh')  # time at next scr refresh
                        centerPresented.setAutoDraw(False)
                
                # *topPresented* updates
                if topPresented.status == NOT_STARTED and tThisFlip >= thisISI-frameTolerance:
                    # keep track of start time/frame for later
                    topPresented.frameNStart = frameN  # exact frame index
                    topPresented.tStart = t  # local t and not account for scr refresh
                    topPresented.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(topPresented, 'tStartRefresh')  # time at next scr refresh
                    topPresented.setAutoDraw(True)
                if topPresented.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > topPresented.tStartRefresh + .5-frameTolerance:
                        # keep track of stop time/frame for later
                        topPresented.tStop = t  # not accounting for scr refresh
                        topPresented.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(topPresented, 'tStopRefresh')  # time at next scr refresh
                        topPresented.setAutoDraw(False)
                
                # *rightPresented* updates
                if rightPresented.status == NOT_STARTED and tThisFlip >= thisISI-frameTolerance:
                    # keep track of start time/frame for later
                    rightPresented.frameNStart = frameN  # exact frame index
                    rightPresented.tStart = t  # local t and not account for scr refresh
                    rightPresented.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(rightPresented, 'tStartRefresh')  # time at next scr refresh
                    rightPresented.setAutoDraw(True)
                if rightPresented.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > rightPresented.tStartRefresh + .5-frameTolerance:
                        # keep track of stop time/frame for later
                        rightPresented.tStop = t  # not accounting for scr refresh
                        rightPresented.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(rightPresented, 'tStopRefresh')  # time at next scr refresh
                        rightPresented.setAutoDraw(False)
                
                # *bottomPresented* updates
                if bottomPresented.status == NOT_STARTED and tThisFlip >= thisISI-frameTolerance:
                    # keep track of start time/frame for later
                    bottomPresented.frameNStart = frameN  # exact frame index
                    bottomPresented.tStart = t  # local t and not account for scr refresh
                    bottomPresented.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(bottomPresented, 'tStartRefresh')  # time at next scr refresh
                    bottomPresented.setAutoDraw(True)
                if bottomPresented.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > bottomPresented.tStartRefresh + .5-frameTolerance:
                        # keep track of stop time/frame for later
                        bottomPresented.tStop = t  # not accounting for scr refresh
                        bottomPresented.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(bottomPresented, 'tStopRefresh')  # time at next scr refresh
                        bottomPresented.setAutoDraw(False)
                
                # *leftPresented* updates
                if leftPresented.status == NOT_STARTED and tThisFlip >= thisISI-frameTolerance:
                    # keep track of start time/frame for later
                    leftPresented.frameNStart = frameN  # exact frame index
                    leftPresented.tStart = t  # local t and not account for scr refresh
                    leftPresented.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(leftPresented, 'tStartRefresh')  # time at next scr refresh
                    leftPresented.setAutoDraw(True)
                if leftPresented.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > leftPresented.tStartRefresh + .5-frameTolerance:
                        # keep track of stop time/frame for later
                        leftPresented.tStop = t  # not accounting for scr refresh
                        leftPresented.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(leftPresented, 'tStopRefresh')  # time at next scr refresh
                        leftPresented.setAutoDraw(False)
                #3
                if centerPresented.status == STARTED and not triggerSent_1:#
                    if ethnicity == 1 and rotCenter == 0:
                        port.write([0x17]) #S23
                        time.sleep(PulseWidth)
                        triggerSent_1 = True
                        pauseStartTime_1 = t
                    elif ethnicity == 1 and rotCenter == 45:#
                        port.write([0x1B])#S27
                        time.sleep(PulseWidth)
                        triggerSent_1 = True
                        pauseStartTime_1 = t
                    elif ethnicity == 2 and rotCenter == 0:#
                        port.write([0x21])#S33
                        time.sleep(PulseWidth)
                        triggerSent_1 = True
                        pauseStartTime_1 = t
                    elif ethnicity == 2 and rotCenter == 45:#
                        port.write([0x25])#S37
                        time.sleep(PulseWidth)
                        triggerSent_1 = True
                        pauseStartTime_1 = t
                    elif ethnicity == 3 and rotCenter == 0:#
                        port.write([0x2B])#S43
                        time.sleep(PulseWidth)
                        triggerSent_1 = True
                        pauseStartTime_1 = t
                    elif ethnicity == 3 and rotCenter == 45:#
                        port.write([0x2F])#S47
                        time.sleep(PulseWidth)
                        triggerSent_1 = True
                        pauseStartTime_1 = t
                    elif ethnicity == 4 and rotCenter == 0:#
                        port.write([0x35])#S53
                        time.sleep(PulseWidth)
                        triggerSent_1 = True
                        pauseStartTime_1 = t
                    elif ethnicity == 4 and rotCenter == 45:#
                        port.write([0x39])#S57
                        time.sleep(PulseWidth)
                        triggerSent_1 = True
                        pauseStartTime_1 = t
                        
                # we send the 2nd trigger after 40 ms.
                if triggerSent_1 and not portsCleared_1:
                    if t > (pauseStartTime_1 + postTriggerPauseTime_1):
                        if male == 0:
                            if scramFace == 0:
                                if blueCenter == 0:
                                    if blueSurround ==0:
                                        if rotSurround == 0:
                                            port.write([0x68])# S104 for non resp
                                            time.sleep(PulseWidth)
                                            #triggerSent_1 = False
                                            portsCleared_1 = True
                                        elif rotSurround == 45:
                                            port.write([0x6C])#S108
                                            time.sleep(PulseWidth)
                                            #triggerSent_1 = False
                                            portsCleared_1 = True
                                    elif blueSurround == 1:
                                        if rotSurround == 0:
                                            port.write([0x70])# S112 
                                            time.sleep(PulseWidth)
                                            #triggerSent_1 = False
                                            portsCleared_1 = True
                                        elif rotSurround == 45:
                                            port.write([0x75])#S117
                                            time.sleep(PulseWidth)
                                            #triggerSent_1 = False
                                            portsCleared_1 = True
                                elif blueCenter == 1:
                                    if blueSurround ==0:
                                        if rotSurround == 0:
                                            port.write([0x79])# S121 for non resp
                                            time.sleep(PulseWidth)
                                            #triggerSent_1 = False
                                            portsCleared_1 = True
                                        elif rotSurround == 45:
                                            port.write([0x7D])#S125
                                            time.sleep(PulseWidth)
                                            #triggerSent_1 = False
                                            portsCleared_1 = True
                                    elif blueSurround == 1:
                                        if rotSurround == 0:
                                            port.write([0x82])# S130 
                                            time.sleep(PulseWidth)
                                            #triggerSent_1 = False
                                            portsCleared_1 = True
                                        elif rotSurround == 45:
                                            port.write([0x86])#S134
                                            time.sleep(PulseWidth)
                                            #triggerSent_1 = False
                                            portsCleared_1 = True
                            elif scramFace == 1:
                                if blueCenter == 0:
                                    if blueSurround ==0:
                                        if rotSurround == 0:
                                            port.write([0x8A])# S138 for non resp
                                            time.sleep(PulseWidth)
                                            #triggerSent_1 = False
                                            portsCleared_1 = True
                                        elif rotSurround == 45:
                                            port.write([0x8E])#S142
                                            time.sleep(PulseWidth)
                                            #triggerSent_1 = False
                                            portsCleared_1 = True
                                    elif blueSurround == 1:
                                        if rotSurround == 0:
                                            port.write([0x92])# S146 
                                            time.sleep(PulseWidth)
                                            #triggerSent_1 = False
                                            portsCleared_1 = True
                                        elif rotSurround == 45:
                                            port.write([0x96])#S150
                                            time.sleep(PulseWidth)
                                            #triggerSent_1 = False
                                            portsCleared_1 = True
                                elif blueCenter == 1:
                                    if blueSurround ==0:
                                        if rotSurround == 0:
                                            port.write([0x9A])# S154 for non resp
                                            time.sleep(PulseWidth)
                                            #triggerSent_1 = False
                                            portsCleared_1 = True
                                        elif rotSurround == 45:
                                            port.write([0x9E])#S158
                                            time.sleep(PulseWidth)
                                            #triggerSent_1 = False
                                            portsCleared_1 = True
                                    elif blueSurround == 1:
                                        if rotSurround == 0:
                                            port.write([0xA2])# S162 
                                            time.sleep(PulseWidth)
                                            #triggerSent_1 = False
                                            portsCleared_1 = True
                                        elif rotSurround == 45:
                                            port.write([0xA6])#S166
                                            time.sleep(PulseWidth)
                                            #triggerSent_1 = False
                                            portsCleared_1 = True
                        elif male ==1:
                            if scramFace == 0:
                                if blueCenter == 0:
                                    if blueSurround ==0:
                                        if rotSurround == 0:
                                            port.write([0xAA])# S170 for non resp
                                            time.sleep(PulseWidth)
                                            #triggerSent_1 = False
                                            portsCleared_1 = True
                                        elif rotSurround == 45:
                                            port.write([0xAE])#S174
                                            time.sleep(PulseWidth)
                                            #triggerSent_1 = False
                                            portsCleared_1 = True
                                    elif blueSurround == 1:
                                        if rotSurround == 0:
                                            port.write([0xB2])# S178 
                                            time.sleep(PulseWidth)
                                            #triggerSent_1 = False
                                            portsCleared_1 = True
                                        elif rotSurround == 45:
                                            port.write([0xB6])#S182
                                            time.sleep(PulseWidth)
                                            #triggerSent_1 = False
                                            portsCleared_1 = True
                                elif blueCenter == 1:
                                    if blueSurround ==0:
                                        if rotSurround == 0:
                                            port.write([0xBA])# S186 for non resp
                                            time.sleep(PulseWidth)
                                            #triggerSent_1 = False
                                            portsCleared_1 = True
                                        elif rotSurround == 45:
                                            port.write([0xBE])#S190
                                            time.sleep(PulseWidth)
                                            #triggerSent_1 = False
                                            portsCleared_1 = True
                                    elif blueSurround == 1:
                                        if rotSurround == 0:
                                            port.write([0xC2])# S194 
                                            time.sleep(PulseWidth)
                                            #triggerSent_1 = False
                                            portsCleared_1 = True
                                        elif rotSurround == 45:
                                            port.write([0xC6])#S198
                                            time.sleep(PulseWidth)
                                            #triggerSent_1 = False
                                            portsCleared_1 = True
                            elif scramFace == 1:
                                if blueCenter == 0:
                                    if blueSurround ==0:
                                        if rotSurround == 0:
                                            port.write([0xCA])# S202 for non resp
                                            time.sleep(PulseWidth)
                                            #triggerSent_1 = False
                                            portsCleared_1 = True
                                        elif rotSurround == 45:
                                            port.write([0xCE])#S206
                                            time.sleep(PulseWidth)
                                            #triggerSent_1 = False
                                            portsCleared_1 = True
                                    elif blueSurround == 1:
                                        if rotSurround == 0:
                                            port.write([0xD2])# S210 
                                            time.sleep(PulseWidth)
                                            #triggerSent_1 = False
                                            portsCleared_1 = True
                                        elif rotSurround == 45:
                                            port.write([0xD6])#S214
                                            time.sleep(PulseWidth)
                                            #triggerSent_1 = False
                                            portsCleared_1 = True
                                elif blueCenter == 1:
                                    if blueSurround ==0:
                                        if rotSurround == 0:
                                            port.write([0xDA])# S218 for non resp
                                            time.sleep(PulseWidth)
                                            #triggerSent_1 = False
                                            portsCleared_1 = True
                                        elif rotSurround == 45:
                                            port.write([0xDE])#S222
                                            time.sleep(PulseWidth)
                                            #triggerSent_1 = False
                                            portsCleared_1 = True
                                    elif blueSurround == 1:
                                        if rotSurround == 0:
                                            port.write([0xE2])# S226 
                                            time.sleep(PulseWidth)
                                            #triggerSent_1 = False
                                            portsCleared_1 = True
                                        elif rotSurround == 45:
                                            port.write([0xE6])#S230
                                            time.sleep(PulseWidth)
                                            #triggerSent_1 = False
                                            portsCleared_1 = True
                
                # *keyResp* updates
                waitOnFlip = False
                if keyResp.status == NOT_STARTED and tThisFlip >= thisISI-frameTolerance:
                    # keep track of start time/frame for later
                    keyResp.frameNStart = frameN  # exact frame index
                    keyResp.tStart = t  # local t and not account for scr refresh
                    keyResp.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(keyResp, 'tStartRefresh')  # time at next scr refresh
                    keyResp.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(keyResp.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(keyResp.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if keyResp.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > keyResp.tStartRefresh + .5-frameTolerance:
                        # keep track of stop time/frame for later
                        keyResp.tStop = t  # not accounting for scr refresh
                        keyResp.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(keyResp, 'tStopRefresh')  # time at next scr refresh
                        keyResp.status = FINISHED
                if keyResp.status == STARTED and not waitOnFlip:
                    theseKeys = keyResp.getKeys(keyList=['1', '8'], waitRelease=False)
                    _keyResp_allKeys.extend(theseKeys)
                    if len(_keyResp_allKeys):
                        keyResp.keys = _keyResp_allKeys[0].name  # just the first key pressed
                        keyResp.rt = _keyResp_allKeys[0].rt
                        # was this correct?
                        if (keyResp.keys == str(corrAns)) or (keyResp.keys == corrAns):
                            keyResp.corr = 1
                        else:
                            keyResp.corr = 0
                        # a response ends the routine
                        continueRoutine = False
                #3
                if keyResp.keys and len(keyResp.keys) > len(keys_counted):# A key response has been made but we haven't yet "counted" it
                    keys_counted.append(keyResp.keys[-1])
                    if keyResp.keys[-1] == corrAns:# if the last key pressed was correct
                        port.write([0x10]) # send trigger
                        time.sleep(PulseWidth) 
                        triggerSent = True
                        portsCleared = False
                        pauseStartTime = t
                    elif keyResp.keys[-1] != corrAns:# if the last key pressed was not correct
                        port.write([0x04])# send different trigger
                        time.sleep(PulseWidth)
                        triggerSent = True
                        portsCleared = False
                        pauseStartTime = t
                
                # if a trigger was send, "clear" the bugger after 100ms
                if triggerSent and not portsCleared:
                    if t > (pauseStartTime + postTriggerPauseTime):
                        triggerSent = False
                        portsCleared = True
                
                
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in StimRoutineComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "StimRoutine"-------
            for thisComponent in StimRoutineComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            stimLoop.addData('LeftReminder_text_4.started', LeftReminder_text_4.tStartRefresh)
            stimLoop.addData('LeftReminder_text_4.stopped', LeftReminder_text_4.tStopRefresh)
            stimLoop.addData('rightReminder_text_4.started', rightReminder_text_4.tStartRefresh)
            stimLoop.addData('rightReminder_text_4.stopped', rightReminder_text_4.tStopRefresh)
            stimLoop.addData('centerPresented.started', centerPresented.tStartRefresh)
            stimLoop.addData('centerPresented.stopped', centerPresented.tStopRefresh)
            stimLoop.addData('topPresented.started', topPresented.tStartRefresh)
            stimLoop.addData('topPresented.stopped', topPresented.tStopRefresh)
            stimLoop.addData('rightPresented.started', rightPresented.tStartRefresh)
            stimLoop.addData('rightPresented.stopped', rightPresented.tStopRefresh)
            stimLoop.addData('bottomPresented.started', bottomPresented.tStartRefresh)
            stimLoop.addData('bottomPresented.stopped', bottomPresented.tStopRefresh)
            stimLoop.addData('leftPresented.started', leftPresented.tStartRefresh)
            stimLoop.addData('leftPresented.stopped', leftPresented.tStopRefresh)
            #4
            
            Connected = False
            thread.join(1.0)
            # check responses
            if keyResp.keys in ['', [], None]:  # No response was made
                keyResp.keys = None
                # was no response the correct answer?!
                if str(corrAns).lower() == 'none':
                   keyResp.corr = 1;  # correct non-response
                else:
                   keyResp.corr = 0;  # failed to respond (incorrectly)
            # store data for stimLoop (TrialHandler)
            stimLoop.addData('keyResp.keys',keyResp.keys)
            stimLoop.addData('keyResp.corr', keyResp.corr)
            if keyResp.keys != None:  # we had a response
                stimLoop.addData('keyResp.rt', keyResp.rt)
            stimLoop.addData('keyResp.started', keyResp.tStartRefresh)
            stimLoop.addData('keyResp.stopped', keyResp.tStopRefresh)
            #4
            if not keyResp.keys or len(keyResp.keys) == 0:
                   port.write([0x03])# send a trigger
                   time.sleep(PulseWidth)
            
            # the Routine "StimRoutine" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # ------Prepare to start Routine "break_stimLoop"-------
            continueRoutine = True
            # update component parameters for each repeat
            # keep track of which components have finished
            break_stimLoopComponents = []
            for thisComponent in break_stimLoopComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            break_stimLoopClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "break_stimLoop"-------
            while continueRoutine:
                # get current time
                t = break_stimLoopClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=break_stimLoopClock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in break_stimLoopComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "break_stimLoop"-------
            for thisComponent in break_stimLoopComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            #store 1back stim from this trial as 2back for next trial
            #back2_rotCenter = back1_rotCenter
            #back2_blueCenter = back1_blueCenter
            
            #store current stim from this trial as 1back for next trial
            #back1_rotCenter = rotCenter
            #back1_blueCenter = blueCenter
            
            stimLoop.finished=True
            
            # the Routine "break_stimLoop" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            thisExp.nextEntry()
            
        # completed 1 repeats of 'stimLoop'
        
        
        # ------Prepare to start Routine "restBreak"-------
        continueRoutine = True
        # update component parameters for each repeat
        if trialLoop.thisN == 0 or trialLoop.thisN % 32 != 0:
            continueRoutine = False
        text.setText('You may take a brief break\n\n\nPress the left or right button continue')
        text.setFont('Arial')
        text.setHeight(0.025)
        key_resp_3.keys = []
        key_resp_3.rt = []
        _key_resp_3_allKeys = []
        # keep track of which components have finished
        restBreakComponents = [text, key_resp_3]
        for thisComponent in restBreakComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        restBreakClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "restBreak"-------
        while continueRoutine:
            # get current time
            t = restBreakClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=restBreakClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text* updates
            if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text.frameNStart = frameN  # exact frame index
                text.tStart = t  # local t and not account for scr refresh
                text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
                text.setAutoDraw(True)
            
            # *key_resp_3* updates
            waitOnFlip = False
            if key_resp_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_3.frameNStart = frameN  # exact frame index
                key_resp_3.tStart = t  # local t and not account for scr refresh
                key_resp_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_3, 'tStartRefresh')  # time at next scr refresh
                key_resp_3.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_3.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_3.getKeys(keyList=['1', '8'], waitRelease=False)
                _key_resp_3_allKeys.extend(theseKeys)
                if len(_key_resp_3_allKeys):
                    key_resp_3.keys = _key_resp_3_allKeys[-1].name  # just the last key pressed
                    key_resp_3.rt = _key_resp_3_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in restBreakComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "restBreak"-------
        for thisComponent in restBreakComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        trialLoop.addData('text.started', text.tStartRefresh)
        trialLoop.addData('text.stopped', text.tStopRefresh)
        # check responses
        if key_resp_3.keys in ['', [], None]:  # No response was made
            key_resp_3.keys = None
        trialLoop.addData('key_resp_3.keys',key_resp_3.keys)
        if key_resp_3.keys != None:  # we had a response
            trialLoop.addData('key_resp_3.rt', key_resp_3.rt)
        trialLoop.addData('key_resp_3.started', key_resp_3.tStartRefresh)
        trialLoop.addData('key_resp_3.stopped', key_resp_3.tStopRefresh)
        # the Routine "restBreak" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed numberReps repeats of 'trialLoop'
    
    
    # ------Prepare to start Routine "taskEnd_instruct"-------
    continueRoutine = True
    # update component parameters for each repeat
    if practice == 1:
        taskEnd_text_source ='You have completed this practice session. \n \n \n \n \n \n \n \n \n \n Press the left or right button to continue to the next game'
    elif practice == 0:
        taskEnd_text_source ='You have completed the game. \n \n \n \n \n \n \n \n \n \n Press the left or right button to learn about the next game'
    
    
    taskEnd_text.setText(taskEnd_text_source)
    key_resp.keys = []
    key_resp.rt = []
    _key_resp_allKeys = []
    # keep track of which components have finished
    taskEnd_instructComponents = [taskEnd_text, key_resp]
    for thisComponent in taskEnd_instructComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    taskEnd_instructClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "taskEnd_instruct"-------
    while continueRoutine:
        # get current time
        t = taskEnd_instructClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=taskEnd_instructClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *taskEnd_text* updates
        if taskEnd_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            taskEnd_text.frameNStart = frameN  # exact frame index
            taskEnd_text.tStart = t  # local t and not account for scr refresh
            taskEnd_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(taskEnd_text, 'tStartRefresh')  # time at next scr refresh
            taskEnd_text.setAutoDraw(True)
        
        # *key_resp* updates
        waitOnFlip = False
        if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp.frameNStart = frameN  # exact frame index
            key_resp.tStart = t  # local t and not account for scr refresh
            key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
            key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp.status == STARTED and not waitOnFlip:
            theseKeys = key_resp.getKeys(keyList=['1', '8'], waitRelease=False)
            _key_resp_allKeys.extend(theseKeys)
            if len(_key_resp_allKeys):
                key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
                key_resp.rt = _key_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in taskEnd_instructComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "taskEnd_instruct"-------
    for thisComponent in taskEnd_instructComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    blockLoop.addData('taskEnd_text.started', taskEnd_text.tStartRefresh)
    blockLoop.addData('taskEnd_text.stopped', taskEnd_text.tStopRefresh)
    # check responses
    if key_resp.keys in ['', [], None]:  # No response was made
        key_resp.keys = None
    blockLoop.addData('key_resp.keys',key_resp.keys)
    if key_resp.keys != None:  # we had a response
        blockLoop.addData('key_resp.rt', key_resp.rt)
    blockLoop.addData('key_resp.started', key_resp.tStartRefresh)
    blockLoop.addData('key_resp.stopped', key_resp.tStopRefresh)
    # the Routine "taskEnd_instruct" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'blockLoop'


# ------Prepare to start Routine "expEnd_intruct"-------
continueRoutine = True
# update component parameters for each repeat
taskEnd_text_2.setText('You have completed the last game.\n\n\nPress the left or right button to exit.\n')
key_resp_2.keys = []
key_resp_2.rt = []
_key_resp_2_allKeys = []
# keep track of which components have finished
expEnd_intructComponents = [taskEnd_text_2, key_resp_2]
for thisComponent in expEnd_intructComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
expEnd_intructClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "expEnd_intruct"-------
while continueRoutine:
    # get current time
    t = expEnd_intructClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=expEnd_intructClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *taskEnd_text_2* updates
    if taskEnd_text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        taskEnd_text_2.frameNStart = frameN  # exact frame index
        taskEnd_text_2.tStart = t  # local t and not account for scr refresh
        taskEnd_text_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(taskEnd_text_2, 'tStartRefresh')  # time at next scr refresh
        taskEnd_text_2.setAutoDraw(True)
    
    # *key_resp_2* updates
    waitOnFlip = False
    if key_resp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_2.frameNStart = frameN  # exact frame index
        key_resp_2.tStart = t  # local t and not account for scr refresh
        key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
        key_resp_2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_2.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_2.getKeys(keyList=['1', '8'], waitRelease=False)
        _key_resp_2_allKeys.extend(theseKeys)
        if len(_key_resp_2_allKeys):
            key_resp_2.keys = _key_resp_2_allKeys[-1].name  # just the last key pressed
            key_resp_2.rt = _key_resp_2_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in expEnd_intructComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "expEnd_intruct"-------
for thisComponent in expEnd_intructComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('taskEnd_text_2.started', taskEnd_text_2.tStartRefresh)
thisExp.addData('taskEnd_text_2.stopped', taskEnd_text_2.tStopRefresh)
# check responses
if key_resp_2.keys in ['', [], None]:  # No response was made
    key_resp_2.keys = None
thisExp.addData('key_resp_2.keys',key_resp_2.keys)
if key_resp_2.keys != None:  # we had a response
    thisExp.addData('key_resp_2.rt', key_resp_2.rt)
thisExp.addData('key_resp_2.started', key_resp_2.tStartRefresh)
thisExp.addData('key_resp_2.stopped', key_resp_2.tStopRefresh)
thisExp.nextEntry()
# the Routine "expEnd_intruct" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()
#5
port.close() 
#5
port.close() 
#5
port.close()
#5
port.close()
#5
port.close()
#5
port.close()
#5
port.close()
#5
port.close()

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
