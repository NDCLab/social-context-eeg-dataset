﻿#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.2.3),
    on March 02, 2022, at 11:19
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
    originPath='C:\\Users\\NDClab\\Desktop\\social-context-eeg\\Multi_EF_with_ALL_triggers_faster_gb\\Multi_EF_with_ALL_triggers\\multi-ef-o_s1_r2_e1-EEG-Inhib-Task_faster_noRSI_lastrun.py',
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
LeftReminder_text_3 = visual.TextStim(win=win, name='LeftReminder_text_3',
    text='',
    font='Arial',
    pos=(-.45, -.45), height=.035, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
rightReminder_text_3 = visual.TextStim(win=win, name='rightReminder_text_3',
    text='',
    font='Arial',
    pos=(.45, -.45), height=.035, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
cuePresented = visual.TextStim(win=win, name='cuePresented',
    text='',
    font='Arial',
    pos=(0, 0), height=.035, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

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
    depth=-3.0);
rightReminder_text_4 = visual.TextStim(win=win, name='rightReminder_text_4',
    text='',
    font='Arial',
    pos=(.45, -.45), height=.035, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
centerPresented = visual.ImageStim(
    win=win,
    name='centerPresented', 
    image='sin', mask=None,
    ori=1.0, pos=(0, 0), size=(.075, .075),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-5.0)
rightPresented = visual.ImageStim(
    win=win,
    name='rightPresented', 
    image='sin', mask=None,
    ori=1.0, pos=(.125, 0), size=(.075, .075),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-6.0)
leftPresented = visual.ImageStim(
    win=win,
    name='leftPresented', 
    image='sin', mask=None,
    ori=1.0, pos=(-.125, 0), size=(.075, .075),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-7.0)
keyResp = keyboard.Keyboard()

# Initialize components for Routine "break_stimLoop"
break_stimLoopClock = core.Clock()
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
            leftReminder = 'BLUE'
            rightReminder = 'ORANGE'
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
            routineTimer.add(0.300000)
            # update component parameters for each repeat
            LeftReminder_text_3.setText(leftReminder)
            rightReminder_text_3.setText(rightReminder)
            cuePresented.setText(whichCue)
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
            while continueRoutine and routineTimer.getTime() > 0:
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
                    if tThisFlipGlobal > LeftReminder_text_3.tStartRefresh + .3-frameTolerance:
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
                    if tThisFlipGlobal > rightReminder_text_3.tStartRefresh + .3-frameTolerance:
                        # keep track of stop time/frame for later
                        rightReminder_text_3.tStop = t  # not accounting for scr refresh
                        rightReminder_text_3.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(rightReminder_text_3, 'tStopRefresh')  # time at next scr refresh
                        rightReminder_text_3.setAutoDraw(False)
                
                # *cuePresented* updates
                if cuePresented.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                    # keep track of start time/frame for later
                    cuePresented.frameNStart = frameN  # exact frame index
                    cuePresented.tStart = t  # local t and not account for scr refresh
                    cuePresented.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(cuePresented, 'tStartRefresh')  # time at next scr refresh
                    cuePresented.setAutoDraw(True)
                if cuePresented.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > cuePresented.tStartRefresh + .3-frameTolerance:
                        # keep track of stop time/frame for later
                        cuePresented.tStop = t  # not accounting for scr refresh
                        cuePresented.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(cuePresented, 'tStopRefresh')  # time at next scr refresh
                        cuePresented.setAutoDraw(False)
                
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
            ISIRange = np.linspace(300, 700, 400)
            # picking from a shuffled array is easier for random selection in JS
            shuffle(ISIRange)
            thisISI = ISIRange[0]/1000 # the first item of the shuffled array 
            
            # show in console for debugging
            print('thisISI: ', thisISI)
            
            # save this ISI to our output file
            stimLoop.addData('ISI', thisISI)
            # pick the ISI for the next routine
            # this code component is set to 'both' because we need to remove the 'np'
            # at the start of np.linspace (this is a python library JS won't know what to call. 
            
            # make range from a to b in n stepsizes
            ITIRange = np.linspace(1500, 2000, 500)
            # picking from a shuffled array is easier for random selection in JS
            shuffle(ITIRange)
            thisITI = ITIRange[0]/1000 # the first item of the shuffled array 
            
            reminderDur = thisITI + thisISI
            
            # show in console for debugging
            print('thisITI: ', ITIRange)
            
            # save this ISI to our output file
            stimLoop.addData('ITI', ITIRange)
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
            rightPresented.setOri(rotSurround)
            rightPresented.setImage(surround)
            leftPresented.setOri(rotSurround)
            leftPresented.setImage(surround)
            keyResp.keys = []
            keyResp.rt = []
            _keyResp_allKeys = []
            # keep track of which components have finished
            StimRoutineComponents = [LeftReminder_text_4, rightReminder_text_4, centerPresented, rightPresented, leftPresented, keyResp]
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
                    if tThisFlipGlobal > centerPresented.tStartRefresh + .3-frameTolerance:
                        # keep track of stop time/frame for later
                        centerPresented.tStop = t  # not accounting for scr refresh
                        centerPresented.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(centerPresented, 'tStopRefresh')  # time at next scr refresh
                        centerPresented.setAutoDraw(False)
                
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
                    if tThisFlipGlobal > rightPresented.tStartRefresh + .3-frameTolerance:
                        # keep track of stop time/frame for later
                        rightPresented.tStop = t  # not accounting for scr refresh
                        rightPresented.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(rightPresented, 'tStopRefresh')  # time at next scr refresh
                        rightPresented.setAutoDraw(False)
                
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
                    if tThisFlipGlobal > leftPresented.tStartRefresh + .3-frameTolerance:
                        # keep track of stop time/frame for later
                        leftPresented.tStop = t  # not accounting for scr refresh
                        leftPresented.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(leftPresented, 'tStopRefresh')  # time at next scr refresh
                        leftPresented.setAutoDraw(False)
                
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
                    if tThisFlipGlobal > keyResp.tStartRefresh + thisITI-frameTolerance:
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
            stimLoop.addData('rightPresented.started', rightPresented.tStartRefresh)
            stimLoop.addData('rightPresented.stopped', rightPresented.tStopRefresh)
            stimLoop.addData('leftPresented.started', leftPresented.tStartRefresh)
            stimLoop.addData('leftPresented.stopped', leftPresented.tStopRefresh)
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
