#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2023.1.3),
    on Dezember 02, 2024, at 17:36
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import plugins
plugins.activatePlugins()
prefs.hardware['audioLib'] = 'ptb'
prefs.hardware['audioLatencyMode'] = '3'
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.tools import environmenttools
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard

# Run 'Before Experiment' code from CodeNBack
#stores the currtentrail number
#gets save in the data for later usage 
trailNumber = 0


# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2023.1.3'
expName = 'NBack'  # from the Builder filename that created this script
expInfo = {
    'participant': f"{randint(0, 999999):06.0f}",
    'session': '001',
}
# --- Show participant info dialog --
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
    originPath='C:\\Users\\Florian\\Desktop\\Test_NBack\\NBack_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# --- Setup the Window ---
win = visual.Window(
    size=(1024, 768), fullscr=True, screen=0, 
    winType='pyglet', allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    backgroundImage='', backgroundFit='none',
    blendMode='avg', useFBO=True, 
    units='height')
win.mouseVisible = False
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# --- Setup input devices ---
ioConfig = {}

# Setup iohub keyboard
ioConfig['Keyboard'] = dict(use_keymap='psychopy')

ioSession = '1'
if 'session' in expInfo:
    ioSession = str(expInfo['session'])
ioServer = io.launchHubServer(window=win, **ioConfig)
eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='iohub')

# --- Initialize components for Routine "Welcome" ---
Txt_Welcome = visual.TextStim(win=win, name='Txt_Welcome',
    text='Welcome \npress space',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp = keyboard.Keyboard()

# --- Initialize components for Routine "DisplayNBack" ---
Txt_DigitDisplay = visual.TextStim(win=win, name='Txt_DigitDisplay',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
KeyCheckCorrentNBack = keyboard.Keyboard()
# Run 'Begin Experiment' code from CodeNBack
#Holds the NBackOrder
NBackOrder = []

#What lvl of Nback currently used 1-anything 
NBackNumber = 2

#Holds the number of loops in the nBack
#Is used to stop the loop 
NBackLoops = 0

#holds the correct response for the keyinput 
correctResponceNBack = "space"

debug = 0 

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

# --- Prepare to start Routine "Welcome" ---
continueRoutine = True
# update component parameters for each repeat
key_resp.keys = []
key_resp.rt = []
_key_resp_allKeys = []
# keep track of which components have finished
WelcomeComponents = [Txt_Welcome, key_resp]
for thisComponent in WelcomeComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Welcome" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Txt_Welcome* updates
    
    # if Txt_Welcome is starting this frame...
    if Txt_Welcome.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Txt_Welcome.frameNStart = frameN  # exact frame index
        Txt_Welcome.tStart = t  # local t and not account for scr refresh
        Txt_Welcome.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Txt_Welcome, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'Txt_Welcome.started')
        # update status
        Txt_Welcome.status = STARTED
        Txt_Welcome.setAutoDraw(True)
    
    # if Txt_Welcome is active this frame...
    if Txt_Welcome.status == STARTED:
        # update params
        pass
    
    # *key_resp* updates
    waitOnFlip = False
    
    # if key_resp is starting this frame...
    if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp.frameNStart = frameN  # exact frame index
        key_resp.tStart = t  # local t and not account for scr refresh
        key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
        # update status
        key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp.status == STARTED and not waitOnFlip:
        theseKeys = key_resp.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_allKeys.extend(theseKeys)
        if len(_key_resp_allKeys):
            key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
            key_resp.rt = _key_resp_allKeys[-1].rt
            key_resp.duration = _key_resp_allKeys[-1].duration
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
        if eyetracker:
            eyetracker.setConnectionState(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in WelcomeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Welcome" ---
for thisComponent in WelcomeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp.keys in ['', [], None]:  # No response was made
    key_resp.keys = None
thisExp.addData('key_resp.keys',key_resp.keys)
if key_resp.keys != None:  # we had a response
    thisExp.addData('key_resp.rt', key_resp.rt)
    thisExp.addData('key_resp.duration', key_resp.duration)
thisExp.nextEntry()
# the Routine "Welcome" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
NBack = data.TrialHandler(nReps=9.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('Conditions_Digits.xlsx'),
    seed=None, name='NBack')
thisExp.addLoop(NBack)  # add the loop to the experiment
thisNBack = NBack.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisNBack.rgb)
if thisNBack != None:
    for paramName in thisNBack:
        exec('{} = thisNBack[paramName]'.format(paramName))

for thisNBack in NBack:
    currentLoop = NBack
    # abbreviate parameter names if possible (e.g. rgb = thisNBack.rgb)
    if thisNBack != None:
        for paramName in thisNBack:
            exec('{} = thisNBack[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "DisplayNBack" ---
    continueRoutine = True
    # update component parameters for each repeat
    Txt_DigitDisplay.setText(Digits)
    KeyCheckCorrentNBack.keys = []
    KeyCheckCorrentNBack.rt = []
    _KeyCheckCorrentNBack_allKeys = []
    # Run 'Begin Routine' code from CodeNBack
    NBackOrder.append(int(Digits))
    
    if(len(NBackOrder) > NBackNumber): 
        #if the NBackOrder is long enouth to start testing 
        if(NBackOrder[len(NBackOrder) - NBackNumber - 1] == int(Digits)):
            #handels repose = correct
            correctResponceNBack = "y"
        else: 
            #handels repose = wrong 
            correctResponceNBack = "n"
        
    # keep track of which components have finished
    DisplayNBackComponents = [Txt_DigitDisplay, KeyCheckCorrentNBack]
    for thisComponent in DisplayNBackComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "DisplayNBack" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 1.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Txt_DigitDisplay* updates
        
        # if Txt_DigitDisplay is starting this frame...
        if Txt_DigitDisplay.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Txt_DigitDisplay.frameNStart = frameN  # exact frame index
            Txt_DigitDisplay.tStart = t  # local t and not account for scr refresh
            Txt_DigitDisplay.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Txt_DigitDisplay, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Txt_DigitDisplay.started')
            # update status
            Txt_DigitDisplay.status = STARTED
            Txt_DigitDisplay.setAutoDraw(True)
        
        # if Txt_DigitDisplay is active this frame...
        if Txt_DigitDisplay.status == STARTED:
            # update params
            pass
        
        # if Txt_DigitDisplay is stopping this frame...
        if Txt_DigitDisplay.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Txt_DigitDisplay.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                Txt_DigitDisplay.tStop = t  # not accounting for scr refresh
                Txt_DigitDisplay.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Txt_DigitDisplay.stopped')
                # update status
                Txt_DigitDisplay.status = FINISHED
                Txt_DigitDisplay.setAutoDraw(False)
        
        # *KeyCheckCorrentNBack* updates
        waitOnFlip = False
        
        # if KeyCheckCorrentNBack is starting this frame...
        if KeyCheckCorrentNBack.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            KeyCheckCorrentNBack.frameNStart = frameN  # exact frame index
            KeyCheckCorrentNBack.tStart = t  # local t and not account for scr refresh
            KeyCheckCorrentNBack.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(KeyCheckCorrentNBack, 'tStartRefresh')  # time at next scr refresh
            # update status
            KeyCheckCorrentNBack.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(KeyCheckCorrentNBack.clock.reset)  # t=0 on next screen flip
        
        # if KeyCheckCorrentNBack is stopping this frame...
        if KeyCheckCorrentNBack.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > KeyCheckCorrentNBack.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                KeyCheckCorrentNBack.tStop = t  # not accounting for scr refresh
                KeyCheckCorrentNBack.frameNStop = frameN  # exact frame index
                # update status
                KeyCheckCorrentNBack.status = FINISHED
                KeyCheckCorrentNBack.status = FINISHED
        if KeyCheckCorrentNBack.status == STARTED and not waitOnFlip:
            theseKeys = KeyCheckCorrentNBack.getKeys(keyList=['y','n'], waitRelease=False)
            _KeyCheckCorrentNBack_allKeys.extend(theseKeys)
            if len(_KeyCheckCorrentNBack_allKeys):
                KeyCheckCorrentNBack.keys = _KeyCheckCorrentNBack_allKeys[0].name  # just the first key pressed
                KeyCheckCorrentNBack.rt = _KeyCheckCorrentNBack_allKeys[0].rt
                KeyCheckCorrentNBack.duration = _KeyCheckCorrentNBack_allKeys[0].duration
                # was this correct?
                if (KeyCheckCorrentNBack.keys == str(correctResponceNBack)) or (KeyCheckCorrentNBack.keys == correctResponceNBack):
                    KeyCheckCorrentNBack.corr = 1
                else:
                    KeyCheckCorrentNBack.corr = 0
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
            if eyetracker:
                eyetracker.setConnectionState(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in DisplayNBackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "DisplayNBack" ---
    for thisComponent in DisplayNBackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if KeyCheckCorrentNBack.keys in ['', [], None]:  # No response was made
        KeyCheckCorrentNBack.keys = None
        # was no response the correct answer?!
        if str(correctResponceNBack).lower() == 'none':
           KeyCheckCorrentNBack.corr = 1;  # correct non-response
        else:
           KeyCheckCorrentNBack.corr = 0;  # failed to respond (incorrectly)
    # store data for NBack (TrialHandler)
    NBack.addData('KeyCheckCorrentNBack.keys',KeyCheckCorrentNBack.keys)
    NBack.addData('KeyCheckCorrentNBack.corr', KeyCheckCorrentNBack.corr)
    if KeyCheckCorrentNBack.keys != None:  # we had a response
        NBack.addData('KeyCheckCorrentNBack.rt', KeyCheckCorrentNBack.rt)
        NBack.addData('KeyCheckCorrentNBack.duration', KeyCheckCorrentNBack.duration)
    # Run 'End Routine' code from CodeNBack
    NBackLoops = NBackLoops + 1
    trailNumber = trailNumber  + 1
    thisExp.addData('trailNumberNBack', trailNumber)
    thisExp.addData('nBackLoop', NBackLoops)
    
    if(NBackLoops  >= 10): 
        NBack.finished = True
    
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-1.000000)
    thisExp.nextEntry()
    
# completed 9.0 repeats of 'NBack'


# --- End experiment ---
# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
