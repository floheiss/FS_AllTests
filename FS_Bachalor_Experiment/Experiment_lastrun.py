#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2023.1.3),
    on Dezember 12, 2024, at 14:15
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

# Run 'Before Experiment' code from Python_Eyetracking_setUp
# Imports
import pylink
import platform
from EyeLinkCoreGraphicsPsychoPy import EyeLinkCoreGraphicsPsychoPy
from string import ascii_letters, digits
import eyetracking
# Set to False if you want to use eyetracking
dummy_mode = True
# Set name for data folder for EDFs
eyetracker_data_folder = eyetracking.create_eyetracking_folder()
# Creates by default a folder with the name "eyetracker data"
# Run 'Before Experiment' code from SetUpDigitSpanFinder
#is used for the max number of digits 
#maxes at 9 
CurrentDigitChecking = 3

#Saves the current loop number max 3 
NumberOfLoopComplete = 0

#Saves the correct loops 
#if 2/3 --> +1 CurrentDigitChecking
CorrectLoops = 0

#saves the current number of digits displayed 
LoopCounter = 0

#Array of correct Digits
CorrectDigits = []
# Run 'Before Experiment' code from CodeEndDigitSpanFindMax
file = open("DigitSpanMax.txt","w")
# Run 'Before Experiment' code from DT_ManageVarsCode
#holds the overall trail number 
#1-30
DTTrailNumber = 0

#holds the current NBack number 
#1-10
DTNBackNumber = 0

#holds id of the response in DS
#1
#pls note i am not sure how where to get this data as is audio quelle :( 
DTDigitSpanNumberResponse = 0

#holds the response in the digitspan scala
#1-4
DTDigitSpanSacalaResponse = 0



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2023.1.3'
expName = 'Experiment'  # from the Builder filename that created this script
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
    originPath='C:\\Users\\Florian\\Desktop\\FS_Bachalor_Experiment\\Experiment_lastrun.py',
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
    size=[1128, 752], fullscr=True, screen=0, 
    winType='pyglet', allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    backgroundImage='Conditions/background.bmp', backgroundFit='cover',
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
WelcomeText = visual.TextStim(win=win, name='WelcomeText',
    text='Willkommen bei unserem Experiment \n\nDanke für die Teilnahme \n\nbla bla bla \n\nDrücken Sie Space um weiter zu kommen ',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
Next_Welcome = keyboard.Keyboard()
# Run 'Begin Experiment' code from Python_Eyetracking_setUp
# Variable for naming EDF
edf_fname = expInfo['participant']
# States that EDF name should be the same as the behavioral experiment
# Check if EDF-name is valid
eyetracking.edf_name_check(edf_fname)
# => should not be longer than 8 characters and only contain letters, digits and
# underscores
# Connects host PC and stimulus PC
el_tracker = eyetracking.connect_tracker(dummy_mode)
edf_file = eyetracking.open_edf_file(el_tracker, edf_fname)
eyetracking.configure_tracker(el_tracker, dummy_mode)

# --- Initialize components for Routine "DSSetUpVars" ---

# --- Initialize components for Routine "DSExplaineFindMax" ---
TextExplainDigitSpanMaxFind = visual.TextStim(win=win, name='TextExplainDigitSpanMaxFind',
    text='Erklärt was in der näcshte aufgabe getan wird :)\n\nSpace to continue\n',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
KeyDigitspanFindMax = keyboard.Keyboard()

# --- Initialize components for Routine "DSDisplayLetter" ---
DisplayedItem = visual.TextStim(win=win, name='DisplayedItem',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "FocusCross" ---
FocusCrossImg = visual.ImageStim(
    win=win,
    name='FocusCrossImg', 
    image='Conditions/sailor_void.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)

# --- Initialize components for Routine "DSFindMaxEndInnerLoop" ---

# --- Initialize components for Routine "DSCheckFindMax" ---
TextAskForDigitSpan = visual.TextStim(win=win, name='TextAskForDigitSpan',
    text='Bitte mit dem Keyboard die gezeiten Zahlen wiederholen\n',
    font='Open Sans',
    pos=(0, 0.2), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
TextRespose = visual.TextStim(win=win, name='TextRespose',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
KeyCheckCorrent = keyboard.Keyboard()
Testing_1 = visual.TextStim(win=win, name='Testing_1',
    text='',
    font='Open Sans',
    pos=(0, -0.1), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
Testing_2 = visual.TextStim(win=win, name='Testing_2',
    text='',
    font='Open Sans',
    pos=(0, -0.2), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);
Testing_3 = visual.TextStim(win=win, name='Testing_3',
    text='',
    font='Open Sans',
    pos=(0, -0.3), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-6.0);

# --- Initialize components for Routine "DSScala" ---
DSTextScala = visual.TextStim(win=win, name='DSTextScala',
    text='Wie sicher sind Sie mit der Antwort:) ? ',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
Slider_Respone_Certainty = visual.Slider(win=win, name='Slider_Respone_Certainty',
    startValue=None, size=1.0, pos=(0, -0.2), units=win.units,
    labels=("sehr", "wenig", "mittel", "viel"), ticks=(1, 2, 3, 4), granularity=1.0,
    style='choice', styleTweaks=(), opacity=None,
    labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.05,
    flip=False, ori=0.0, depth=-1, readOnly=False)

# --- Initialize components for Routine "DSFindMaxEndOuterLoop" ---

# --- Initialize components for Routine "DSExplaineExample" ---
TextDigtSpanExample = visual.TextStim(win=win, name='TextDigtSpanExample',
    text='erklärt den unterschied zum normalen DigitSpan\n\nEs folgen ein paar teil runs zum testen ob es verstanden wurde\n\nspace to go next',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
KeyDigitSpanExplainExample = keyboard.Keyboard()

# --- Initialize components for Routine "DSAudioDisplayExplain" ---
DSSoundExplain = sound.Sound('A', secs=1.0, stereo=True, hamming=True,
    name='DSSoundExplain')
DSSoundExplain.setVolume(1.0)

# --- Initialize components for Routine "FocusCross" ---
FocusCrossImg = visual.ImageStim(
    win=win,
    name='FocusCrossImg', 
    image='Conditions/sailor_void.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)

# --- Initialize components for Routine "DSExplainEndInnerLoop" ---

# --- Initialize components for Routine "DSResponseAudio" ---
DSTextResponseAudio = visual.TextStim(win=win, name='DSTextResponseAudio',
    text='Bitte der Testperson ihre Zahlen wieder geben :) \n\nDanach Space drücken um weiter zu kommen',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
DSAudioKeyNext = keyboard.Keyboard()

# --- Initialize components for Routine "DSScala" ---
DSTextScala = visual.TextStim(win=win, name='DSTextScala',
    text='Wie sicher sind Sie mit der Antwort:) ? ',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
Slider_Respone_Certainty = visual.Slider(win=win, name='Slider_Respone_Certainty',
    startValue=None, size=1.0, pos=(0, -0.2), units=win.units,
    labels=("sehr", "wenig", "mittel", "viel"), ticks=(1, 2, 3, 4), granularity=1.0,
    style='choice', styleTweaks=(), opacity=None,
    labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.05,
    flip=False, ori=0.0, depth=-1, readOnly=False)

# --- Initialize components for Routine "DSDisplayReal" ---
text = visual.TextStim(win=win, name='text',
    text='Es folgen nun 30 Tests mit der gleichen Aufgabe. \nWir würden sie bitten diese gleich aus zufüllen.\n\nPress space to continue',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
Next_DigitSpanReal = keyboard.Keyboard()

# --- Initialize components for Routine "EyeTrackingStart" ---

# --- Initialize components for Routine "DSDisplayDigitAudioFull" ---
DSDisplaySoundFull = sound.Sound('A', secs=1.0, stereo=True, hamming=True,
    name='DSDisplaySoundFull')
DSDisplaySoundFull.setVolume(1.0)

# --- Initialize components for Routine "FocusCross" ---
FocusCrossImg = visual.ImageStim(
    win=win,
    name='FocusCrossImg', 
    image='Conditions/sailor_void.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)

# --- Initialize components for Routine "DSTrailsEndInnerLoop" ---

# --- Initialize components for Routine "DSResponseAudio" ---
DSTextResponseAudio = visual.TextStim(win=win, name='DSTextResponseAudio',
    text='Bitte der Testperson ihre Zahlen wieder geben :) \n\nDanach Space drücken um weiter zu kommen',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
DSAudioKeyNext = keyboard.Keyboard()

# --- Initialize components for Routine "DSScala" ---
DSTextScala = visual.TextStim(win=win, name='DSTextScala',
    text='Wie sicher sind Sie mit der Antwort:) ? ',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
Slider_Respone_Certainty = visual.Slider(win=win, name='Slider_Respone_Certainty',
    startValue=None, size=1.0, pos=(0, -0.2), units=win.units,
    labels=("sehr", "wenig", "mittel", "viel"), ticks=(1, 2, 3, 4), granularity=1.0,
    style='choice', styleTweaks=(), opacity=None,
    labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.05,
    flip=False, ori=0.0, depth=-1, readOnly=False)

# --- Initialize components for Routine "EyeTrackingStop" ---

# --- Initialize components for Routine "NBExplain" ---
TextNBackExplain = visual.TextStim(win=win, name='TextNBackExplain',
    text='Erklärt den NBack\n\nSpace for next',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
KeyNextNBackExplain = keyboard.Keyboard()

# --- Initialize components for Routine "NBDisplayDigitExplain" ---
TextNBackDisplayDigit = visual.TextStim(win=win, name='TextNBackDisplayDigit',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
KeyResponseNBExplain = keyboard.Keyboard()
# Run 'Begin Experiment' code from NBCodeExplain
#Holds the NBackOrder
NBackOrder = []

#What lvl of Nback currently used 1-anything 
NBackNumber = 2

#Holds the number of loops in the nBack
#Is used to stop the loop 
NBackLoops = 0

#holds the correct response for the keyinput 
correctResponceNBack = "space"

# --- Initialize components for Routine "NBFullTest" ---
TextNBFullTest = visual.TextStim(win=win, name='TextNBFullTest',
    text='Es kommten weiter NBacks \n\nSpace to next',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
KeyResponseNBFull = keyboard.Keyboard()

# --- Initialize components for Routine "EyeTrackingStart" ---

# --- Initialize components for Routine "NBackFullDisplayDigit" ---
TextNBackDisplayDigitFull = visual.TextStim(win=win, name='TextNBackDisplayDigitFull',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
KeyResponseNBFullTest = keyboard.Keyboard()
# Run 'Begin Experiment' code from NBCodeFull
#Holds the NBackOrder
NBackOrder = []

#What lvl of Nback currently used 1-anything 
NBackNumber = 2

#Holds the number of loops in the nBack
#Is used to stop the loop 
NBackLoops = 0

#holds the correct response for the keyinput 
correctResponceNBack = "space"

# --- Initialize components for Routine "EyeTrackingStop" ---

# --- Initialize components for Routine "DTExplain" ---
TextDTExplain = visual.TextStim(win=win, name='TextDTExplain',
    text='Explains the DT\n\nspace to next \n',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
KeyResponseDTExplain = keyboard.Keyboard()

# --- Initialize components for Routine "EyeTrackingStart" ---

# --- Initialize components for Routine "DT_ManageVars" ---

# --- Initialize components for Routine "DT_DS_DisplayAudio" ---
DT_DS_Audio = sound.Sound('A', secs=1.0, stereo=True, hamming=True,
    name='DT_DS_Audio')
DT_DS_Audio.setVolume(1.0)

# --- Initialize components for Routine "FocusCross" ---
FocusCrossImg = visual.ImageStim(
    win=win,
    name='FocusCrossImg', 
    image='Conditions/sailor_void.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)

# --- Initialize components for Routine "DT_DS_InnerLoopEnd" ---

# --- Initialize components for Routine "DT_NB_Display" ---
DT_NB_TextDisplay = visual.TextStim(win=win, name='DT_NB_TextDisplay',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
DT_NB_KeyResponse = keyboard.Keyboard()
# Run 'Begin Experiment' code from DT_NB_CodeEndNB
#Holds the NBackOrder
NBackOrder = []

#What lvl of Nback currently used 1-anything 
NBackNumber = 2

#Holds the number of loops in the nBack
#Is used to stop the loop 
NBackLoops = 0

#holds the correct response for the keyinput 
correctResponceNBack = "space"

# --- Initialize components for Routine "DT_DS_ResponeInAudio" ---
DT_DS_TextResponseInAudio = visual.TextStim(win=win, name='DT_DS_TextResponseInAudio',
    text='Bitte der Testperson ihre Zahlen wieder geben :) \n\nDanach Space drücken um weiter zu kommen',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
KeyResponseNext = keyboard.Keyboard()

# --- Initialize components for Routine "DT_DS_ResponseScala" ---
DT_DS_TextScala = visual.TextStim(win=win, name='DT_DS_TextScala',
    text='Wie sicher sind Sie mit der Antwort:) ? ',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
DT_DS_Scala = visual.Slider(win=win, name='DT_DS_Scala',
    startValue=None, size=1.0, pos=(0, -0.2), units=win.units,
    labels=("sehr", "wenig", "mittel", "viel"), ticks=(1, 2, 3, 4), granularity=1.0,
    style='choice', styleTweaks=(), opacity=None,
    labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.05,
    flip=False, ori=0.0, depth=-1, readOnly=False)

# --- Initialize components for Routine "EyeTrackingStop" ---

# --- Initialize components for Routine "EndScreen" ---
TextEndScreen = visual.TextStim(win=win, name='TextEndScreen',
    text='Dane für die Teilnahme :) \n\n"Esc" zum verlassen',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

# --- Prepare to start Routine "Welcome" ---
continueRoutine = True
# update component parameters for each repeat
Next_Welcome.keys = []
Next_Welcome.rt = []
_Next_Welcome_allKeys = []
# keep track of which components have finished
WelcomeComponents = [WelcomeText, Next_Welcome]
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
    
    # *WelcomeText* updates
    
    # if WelcomeText is starting this frame...
    if WelcomeText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        WelcomeText.frameNStart = frameN  # exact frame index
        WelcomeText.tStart = t  # local t and not account for scr refresh
        WelcomeText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(WelcomeText, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'WelcomeText.started')
        # update status
        WelcomeText.status = STARTED
        WelcomeText.setAutoDraw(True)
    
    # if WelcomeText is active this frame...
    if WelcomeText.status == STARTED:
        # update params
        pass
    
    # *Next_Welcome* updates
    waitOnFlip = False
    
    # if Next_Welcome is starting this frame...
    if Next_Welcome.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        Next_Welcome.frameNStart = frameN  # exact frame index
        Next_Welcome.tStart = t  # local t and not account for scr refresh
        Next_Welcome.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Next_Welcome, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'Next_Welcome.started')
        # update status
        Next_Welcome.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(Next_Welcome.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(Next_Welcome.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if Next_Welcome.status == STARTED and not waitOnFlip:
        theseKeys = Next_Welcome.getKeys(keyList=['space'], waitRelease=False)
        _Next_Welcome_allKeys.extend(theseKeys)
        if len(_Next_Welcome_allKeys):
            Next_Welcome.keys = _Next_Welcome_allKeys[-1].name  # just the last key pressed
            Next_Welcome.rt = _Next_Welcome_allKeys[-1].rt
            Next_Welcome.duration = _Next_Welcome_allKeys[-1].duration
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
if Next_Welcome.keys in ['', [], None]:  # No response was made
    Next_Welcome.keys = None
thisExp.addData('Next_Welcome.keys',Next_Welcome.keys)
if Next_Welcome.keys != None:  # we had a response
    thisExp.addData('Next_Welcome.rt', Next_Welcome.rt)
    thisExp.addData('Next_Welcome.duration', Next_Welcome.duration)
thisExp.nextEntry()
# the Routine "Welcome" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "DSSetUpVars" ---
continueRoutine = True
# update component parameters for each repeat
# Run 'Begin Routine' code from SetUpDigitSpanFinder
#calibration adn validation
eyetracking.calibration_validation(el_tracker, win, dummy_mode)
# keep track of which components have finished
DSSetUpVarsComponents = []
for thisComponent in DSSetUpVarsComponents:
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

# --- Run Routine "DSSetUpVars" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
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
    for thisComponent in DSSetUpVarsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "DSSetUpVars" ---
for thisComponent in DSSetUpVarsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "DSSetUpVars" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "DSExplaineFindMax" ---
continueRoutine = True
# update component parameters for each repeat
KeyDigitspanFindMax.keys = []
KeyDigitspanFindMax.rt = []
_KeyDigitspanFindMax_allKeys = []
# keep track of which components have finished
DSExplaineFindMaxComponents = [TextExplainDigitSpanMaxFind, KeyDigitspanFindMax]
for thisComponent in DSExplaineFindMaxComponents:
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

# --- Run Routine "DSExplaineFindMax" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *TextExplainDigitSpanMaxFind* updates
    
    # if TextExplainDigitSpanMaxFind is starting this frame...
    if TextExplainDigitSpanMaxFind.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        TextExplainDigitSpanMaxFind.frameNStart = frameN  # exact frame index
        TextExplainDigitSpanMaxFind.tStart = t  # local t and not account for scr refresh
        TextExplainDigitSpanMaxFind.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(TextExplainDigitSpanMaxFind, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'TextExplainDigitSpanMaxFind.started')
        # update status
        TextExplainDigitSpanMaxFind.status = STARTED
        TextExplainDigitSpanMaxFind.setAutoDraw(True)
    
    # if TextExplainDigitSpanMaxFind is active this frame...
    if TextExplainDigitSpanMaxFind.status == STARTED:
        # update params
        pass
    
    # *KeyDigitspanFindMax* updates
    waitOnFlip = False
    
    # if KeyDigitspanFindMax is starting this frame...
    if KeyDigitspanFindMax.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        KeyDigitspanFindMax.frameNStart = frameN  # exact frame index
        KeyDigitspanFindMax.tStart = t  # local t and not account for scr refresh
        KeyDigitspanFindMax.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(KeyDigitspanFindMax, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'KeyDigitspanFindMax.started')
        # update status
        KeyDigitspanFindMax.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(KeyDigitspanFindMax.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(KeyDigitspanFindMax.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if KeyDigitspanFindMax.status == STARTED and not waitOnFlip:
        theseKeys = KeyDigitspanFindMax.getKeys(keyList=['space'], waitRelease=False)
        _KeyDigitspanFindMax_allKeys.extend(theseKeys)
        if len(_KeyDigitspanFindMax_allKeys):
            KeyDigitspanFindMax.keys = _KeyDigitspanFindMax_allKeys[-1].name  # just the last key pressed
            KeyDigitspanFindMax.rt = _KeyDigitspanFindMax_allKeys[-1].rt
            KeyDigitspanFindMax.duration = _KeyDigitspanFindMax_allKeys[-1].duration
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
    for thisComponent in DSExplaineFindMaxComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "DSExplaineFindMax" ---
for thisComponent in DSExplaineFindMaxComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if KeyDigitspanFindMax.keys in ['', [], None]:  # No response was made
    KeyDigitspanFindMax.keys = None
thisExp.addData('KeyDigitspanFindMax.keys',KeyDigitspanFindMax.keys)
if KeyDigitspanFindMax.keys != None:  # we had a response
    thisExp.addData('KeyDigitspanFindMax.rt', KeyDigitspanFindMax.rt)
    thisExp.addData('KeyDigitspanFindMax.duration', KeyDigitspanFindMax.duration)
thisExp.nextEntry()
# the Routine "DSExplaineFindMax" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
LoopMaxDigitSpanFind = data.TrialHandler(nReps=9.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='LoopMaxDigitSpanFind')
thisExp.addLoop(LoopMaxDigitSpanFind)  # add the loop to the experiment
thisLoopMaxDigitSpanFind = LoopMaxDigitSpanFind.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisLoopMaxDigitSpanFind.rgb)
if thisLoopMaxDigitSpanFind != None:
    for paramName in thisLoopMaxDigitSpanFind:
        exec('{} = thisLoopMaxDigitSpanFind[paramName]'.format(paramName))

for thisLoopMaxDigitSpanFind in LoopMaxDigitSpanFind:
    currentLoop = LoopMaxDigitSpanFind
    # abbreviate parameter names if possible (e.g. rgb = thisLoopMaxDigitSpanFind.rgb)
    if thisLoopMaxDigitSpanFind != None:
        for paramName in thisLoopMaxDigitSpanFind:
            exec('{} = thisLoopMaxDigitSpanFind[paramName]'.format(paramName))
    
    # set up handler to look after randomisation of conditions etc
    LoopDigitSpan = data.TrialHandler(nReps=1.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('Conditions/Conditions_Digits.xlsx'),
        seed=None, name='LoopDigitSpan')
    thisExp.addLoop(LoopDigitSpan)  # add the loop to the experiment
    thisLoopDigitSpan = LoopDigitSpan.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisLoopDigitSpan.rgb)
    if thisLoopDigitSpan != None:
        for paramName in thisLoopDigitSpan:
            exec('{} = thisLoopDigitSpan[paramName]'.format(paramName))
    
    for thisLoopDigitSpan in LoopDigitSpan:
        currentLoop = LoopDigitSpan
        # abbreviate parameter names if possible (e.g. rgb = thisLoopDigitSpan.rgb)
        if thisLoopDigitSpan != None:
            for paramName in thisLoopDigitSpan:
                exec('{} = thisLoopDigitSpan[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "DSDisplayLetter" ---
        continueRoutine = True
        # update component parameters for each repeat
        DisplayedItem.setText(Digits)
        # keep track of which components have finished
        DSDisplayLetterComponents = [DisplayedItem]
        for thisComponent in DSDisplayLetterComponents:
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
        
        # --- Run Routine "DSDisplayLetter" ---
        routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 1.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *DisplayedItem* updates
            
            # if DisplayedItem is starting this frame...
            if DisplayedItem.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                DisplayedItem.frameNStart = frameN  # exact frame index
                DisplayedItem.tStart = t  # local t and not account for scr refresh
                DisplayedItem.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(DisplayedItem, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'DisplayedItem.started')
                # update status
                DisplayedItem.status = STARTED
                DisplayedItem.setAutoDraw(True)
            
            # if DisplayedItem is active this frame...
            if DisplayedItem.status == STARTED:
                # update params
                pass
            
            # if DisplayedItem is stopping this frame...
            if DisplayedItem.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > DisplayedItem.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    DisplayedItem.tStop = t  # not accounting for scr refresh
                    DisplayedItem.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'DisplayedItem.stopped')
                    # update status
                    DisplayedItem.status = FINISHED
                    DisplayedItem.setAutoDraw(False)
            
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
            for thisComponent in DSDisplayLetterComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "DSDisplayLetter" ---
        for thisComponent in DSDisplayLetterComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-1.000000)
        
        # --- Prepare to start Routine "FocusCross" ---
        continueRoutine = True
        # update component parameters for each repeat
        # keep track of which components have finished
        FocusCrossComponents = [FocusCrossImg]
        for thisComponent in FocusCrossComponents:
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
        
        # --- Run Routine "FocusCross" ---
        routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 1.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *FocusCrossImg* updates
            
            # if FocusCrossImg is starting this frame...
            if FocusCrossImg.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                FocusCrossImg.frameNStart = frameN  # exact frame index
                FocusCrossImg.tStart = t  # local t and not account for scr refresh
                FocusCrossImg.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(FocusCrossImg, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'FocusCrossImg.started')
                # update status
                FocusCrossImg.status = STARTED
                FocusCrossImg.setAutoDraw(True)
            
            # if FocusCrossImg is active this frame...
            if FocusCrossImg.status == STARTED:
                # update params
                pass
            
            # if FocusCrossImg is stopping this frame...
            if FocusCrossImg.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > FocusCrossImg.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    FocusCrossImg.tStop = t  # not accounting for scr refresh
                    FocusCrossImg.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'FocusCrossImg.stopped')
                    # update status
                    FocusCrossImg.status = FINISHED
                    FocusCrossImg.setAutoDraw(False)
            # Run 'Each Frame' code from EyeTrackingFlagFocusCross
            if t == FocusCrossImg.tStart:
                el_tracker.sendMessage('fxon')
            elif t == FocusCrossImg.tStop:
                el_tracker.sendMessage('fxoff')
            
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
            for thisComponent in FocusCrossComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "FocusCross" ---
        for thisComponent in FocusCrossComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-1.000000)
        
        # --- Prepare to start Routine "DSFindMaxEndInnerLoop" ---
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from CodeAfterDisplayLoop
        LoopCounter = LoopCounter + 1
        
        CorrectDigits.append(str(int(Digits)))
        
        if LoopCounter >= CurrentDigitChecking:
            LoopCounter = 0 
            LoopDigitSpan.finished = True
        # keep track of which components have finished
        DSFindMaxEndInnerLoopComponents = []
        for thisComponent in DSFindMaxEndInnerLoopComponents:
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
        
        # --- Run Routine "DSFindMaxEndInnerLoop" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
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
            for thisComponent in DSFindMaxEndInnerLoopComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "DSFindMaxEndInnerLoop" ---
        for thisComponent in DSFindMaxEndInnerLoopComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # the Routine "DSFindMaxEndInnerLoop" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
    # completed 1.0 repeats of 'LoopDigitSpan'
    
    
    # --- Prepare to start Routine "DSCheckFindMax" ---
    continueRoutine = True
    # update component parameters for each repeat
    KeyCheckCorrent.keys = []
    KeyCheckCorrent.rt = []
    _KeyCheckCorrent_allKeys = []
    # Run 'Begin Routine' code from CodeCorrectAnswer
    respons = ""
    
    last_len = 0
    key_list = []
    
    responeCorrect = False
    # keep track of which components have finished
    DSCheckFindMaxComponents = [TextAskForDigitSpan, TextRespose, KeyCheckCorrent, Testing_1, Testing_2, Testing_3]
    for thisComponent in DSCheckFindMaxComponents:
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
    
    # --- Run Routine "DSCheckFindMax" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *TextAskForDigitSpan* updates
        
        # if TextAskForDigitSpan is starting this frame...
        if TextAskForDigitSpan.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            TextAskForDigitSpan.frameNStart = frameN  # exact frame index
            TextAskForDigitSpan.tStart = t  # local t and not account for scr refresh
            TextAskForDigitSpan.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(TextAskForDigitSpan, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'TextAskForDigitSpan.started')
            # update status
            TextAskForDigitSpan.status = STARTED
            TextAskForDigitSpan.setAutoDraw(True)
        
        # if TextAskForDigitSpan is active this frame...
        if TextAskForDigitSpan.status == STARTED:
            # update params
            pass
        
        # *TextRespose* updates
        
        # if TextRespose is starting this frame...
        if TextRespose.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            TextRespose.frameNStart = frameN  # exact frame index
            TextRespose.tStart = t  # local t and not account for scr refresh
            TextRespose.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(TextRespose, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'TextRespose.started')
            # update status
            TextRespose.status = STARTED
            TextRespose.setAutoDraw(True)
        
        # if TextRespose is active this frame...
        if TextRespose.status == STARTED:
            # update params
            TextRespose.setText(respons
, log=False)
        
        # *KeyCheckCorrent* updates
        waitOnFlip = False
        
        # if KeyCheckCorrent is starting this frame...
        if KeyCheckCorrent.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            KeyCheckCorrent.frameNStart = frameN  # exact frame index
            KeyCheckCorrent.tStart = t  # local t and not account for scr refresh
            KeyCheckCorrent.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(KeyCheckCorrent, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'KeyCheckCorrent.started')
            # update status
            KeyCheckCorrent.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(KeyCheckCorrent.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(KeyCheckCorrent.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if KeyCheckCorrent.status == STARTED and not waitOnFlip:
            theseKeys = KeyCheckCorrent.getKeys(keyList=['1','2','3','4','5','6','7','8','9'], waitRelease=False)
            _KeyCheckCorrent_allKeys.extend(theseKeys)
            if len(_KeyCheckCorrent_allKeys):
                KeyCheckCorrent.keys = [key.name for key in _KeyCheckCorrent_allKeys]  # storing all keys
                KeyCheckCorrent.rt = [key.rt for key in _KeyCheckCorrent_allKeys]
                KeyCheckCorrent.duration = [key.duration for key in _KeyCheckCorrent_allKeys]
        # Run 'Each Frame' code from CodeCorrectAnswer
        if(len(KeyCheckCorrent.keys) > last_len): 
            #handels keyupdates
            last_len = len(KeyCheckCorrent.keys);
            key_list.append(KeyCheckCorrent.keys.pop());
            
            respons = "".join(key_list)
            
            if(len(key_list) >= CurrentDigitChecking):
               if (key_list == CorrectDigits):
                    #handels when response correct;
                    CorrectLoops = CorrectLoops + 1;
               CorrectDigits.clear()
               continueRoutine = False
        
        # *Testing_1* updates
        
        # if Testing_1 is starting this frame...
        if Testing_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Testing_1.frameNStart = frameN  # exact frame index
            Testing_1.tStart = t  # local t and not account for scr refresh
            Testing_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Testing_1, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Testing_1.started')
            # update status
            Testing_1.status = STARTED
            Testing_1.setAutoDraw(True)
        
        # if Testing_1 is active this frame...
        if Testing_1.status == STARTED:
            # update params
            Testing_1.setText(CorrectLoops, log=False)
        
        # *Testing_2* updates
        
        # if Testing_2 is starting this frame...
        if Testing_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Testing_2.frameNStart = frameN  # exact frame index
            Testing_2.tStart = t  # local t and not account for scr refresh
            Testing_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Testing_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Testing_2.started')
            # update status
            Testing_2.status = STARTED
            Testing_2.setAutoDraw(True)
        
        # if Testing_2 is active this frame...
        if Testing_2.status == STARTED:
            # update params
            Testing_2.setText(CorrectDigits
, log=False)
        
        # *Testing_3* updates
        
        # if Testing_3 is starting this frame...
        if Testing_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Testing_3.frameNStart = frameN  # exact frame index
            Testing_3.tStart = t  # local t and not account for scr refresh
            Testing_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Testing_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Testing_3.started')
            # update status
            Testing_3.status = STARTED
            Testing_3.setAutoDraw(True)
        
        # if Testing_3 is active this frame...
        if Testing_3.status == STARTED:
            # update params
            Testing_3.setText(key_list, log=False)
        
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
        for thisComponent in DSCheckFindMaxComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "DSCheckFindMax" ---
    for thisComponent in DSCheckFindMaxComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if KeyCheckCorrent.keys in ['', [], None]:  # No response was made
        KeyCheckCorrent.keys = None
    LoopMaxDigitSpanFind.addData('KeyCheckCorrent.keys',KeyCheckCorrent.keys)
    if KeyCheckCorrent.keys != None:  # we had a response
        LoopMaxDigitSpanFind.addData('KeyCheckCorrent.rt', KeyCheckCorrent.rt)
        LoopMaxDigitSpanFind.addData('KeyCheckCorrent.duration', KeyCheckCorrent.duration)
    # Run 'End Routine' code from CodeCorrectAnswer
    NumberOfLoopComplete = NumberOfLoopComplete + 1
    # the Routine "DSCheckFindMax" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "DSScala" ---
    continueRoutine = True
    # update component parameters for each repeat
    Slider_Respone_Certainty.reset()
    # keep track of which components have finished
    DSScalaComponents = [DSTextScala, Slider_Respone_Certainty]
    for thisComponent in DSScalaComponents:
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
    
    # --- Run Routine "DSScala" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *DSTextScala* updates
        
        # if DSTextScala is starting this frame...
        if DSTextScala.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            DSTextScala.frameNStart = frameN  # exact frame index
            DSTextScala.tStart = t  # local t and not account for scr refresh
            DSTextScala.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(DSTextScala, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'DSTextScala.started')
            # update status
            DSTextScala.status = STARTED
            DSTextScala.setAutoDraw(True)
        
        # if DSTextScala is active this frame...
        if DSTextScala.status == STARTED:
            # update params
            pass
        
        # *Slider_Respone_Certainty* updates
        
        # if Slider_Respone_Certainty is starting this frame...
        if Slider_Respone_Certainty.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Slider_Respone_Certainty.frameNStart = frameN  # exact frame index
            Slider_Respone_Certainty.tStart = t  # local t and not account for scr refresh
            Slider_Respone_Certainty.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Slider_Respone_Certainty, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Slider_Respone_Certainty.started')
            # update status
            Slider_Respone_Certainty.status = STARTED
            Slider_Respone_Certainty.setAutoDraw(True)
        
        # if Slider_Respone_Certainty is active this frame...
        if Slider_Respone_Certainty.status == STARTED:
            # update params
            Slider_Respone_Certainty.setSize((1.0, 0.1), log=False)
        
        # Check Slider_Respone_Certainty for response to end routine
        if Slider_Respone_Certainty.getRating() is not None and Slider_Respone_Certainty.status == STARTED:
            continueRoutine = False
        # Run 'Each Frame' code from DSCodeFlagScala
        if t == DSTextScala.tStart:
            el_tracker.sendMessage('DTDSResponseon')
        elif t == DSTextScala.tStop:
            el_tracker.sendMessage('DTDSResponseoff')
        
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
        for thisComponent in DSScalaComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "DSScala" ---
    for thisComponent in DSScalaComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    LoopMaxDigitSpanFind.addData('Slider_Respone_Certainty.response', Slider_Respone_Certainty.getRating())
    LoopMaxDigitSpanFind.addData('Slider_Respone_Certainty.rt', Slider_Respone_Certainty.getRT())
    # the Routine "DSScala" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "DSFindMaxEndOuterLoop" ---
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from CodeEndDigitSpanFindMax
    if(NumberOfLoopComplete >= 3):
        NumberOfLoopComplete = 0
        CorrectDigits = []
        #pls note this is debugging to make progress :)
        if(CorrectLoops >= 2):
            CorrectLoops = 0
            CurrentDigitChecking = CurrentDigitChecking + 1
            #pls note this is debugging to make progress :)
            if CurrentDigitChecking >= 9: 
                #ends the loop even if all correct 
                #--> caps at max digitSpan
                #saves the CurrentDigitChecking as a file for later useage 
                file.write(str(CurrentDigitChecking))
                file.close()
                
                LoopMaxDigitSpanFind.finished = True
        else: 
            CorrectLoops = 0
           
            #saves the CurrentDigitChecking as a file for later useage 
            file.write(str(CurrentDigitChecking))
            file.close()
            
            LoopMaxDigitSpanFind.finished = True
    # keep track of which components have finished
    DSFindMaxEndOuterLoopComponents = []
    for thisComponent in DSFindMaxEndOuterLoopComponents:
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
    
    # --- Run Routine "DSFindMaxEndOuterLoop" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
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
        for thisComponent in DSFindMaxEndOuterLoopComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "DSFindMaxEndOuterLoop" ---
    for thisComponent in DSFindMaxEndOuterLoopComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "DSFindMaxEndOuterLoop" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 9.0 repeats of 'LoopMaxDigitSpanFind'


# --- Prepare to start Routine "DSExplaineExample" ---
continueRoutine = True
# update component parameters for each repeat
KeyDigitSpanExplainExample.keys = []
KeyDigitSpanExplainExample.rt = []
_KeyDigitSpanExplainExample_allKeys = []
# keep track of which components have finished
DSExplaineExampleComponents = [TextDigtSpanExample, KeyDigitSpanExplainExample]
for thisComponent in DSExplaineExampleComponents:
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

# --- Run Routine "DSExplaineExample" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *TextDigtSpanExample* updates
    
    # if TextDigtSpanExample is starting this frame...
    if TextDigtSpanExample.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        TextDigtSpanExample.frameNStart = frameN  # exact frame index
        TextDigtSpanExample.tStart = t  # local t and not account for scr refresh
        TextDigtSpanExample.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(TextDigtSpanExample, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'TextDigtSpanExample.started')
        # update status
        TextDigtSpanExample.status = STARTED
        TextDigtSpanExample.setAutoDraw(True)
    
    # if TextDigtSpanExample is active this frame...
    if TextDigtSpanExample.status == STARTED:
        # update params
        pass
    
    # *KeyDigitSpanExplainExample* updates
    waitOnFlip = False
    
    # if KeyDigitSpanExplainExample is starting this frame...
    if KeyDigitSpanExplainExample.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        KeyDigitSpanExplainExample.frameNStart = frameN  # exact frame index
        KeyDigitSpanExplainExample.tStart = t  # local t and not account for scr refresh
        KeyDigitSpanExplainExample.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(KeyDigitSpanExplainExample, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'KeyDigitSpanExplainExample.started')
        # update status
        KeyDigitSpanExplainExample.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(KeyDigitSpanExplainExample.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(KeyDigitSpanExplainExample.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if KeyDigitSpanExplainExample.status == STARTED and not waitOnFlip:
        theseKeys = KeyDigitSpanExplainExample.getKeys(keyList=['space'], waitRelease=False)
        _KeyDigitSpanExplainExample_allKeys.extend(theseKeys)
        if len(_KeyDigitSpanExplainExample_allKeys):
            KeyDigitSpanExplainExample.keys = _KeyDigitSpanExplainExample_allKeys[-1].name  # just the last key pressed
            KeyDigitSpanExplainExample.rt = _KeyDigitSpanExplainExample_allKeys[-1].rt
            KeyDigitSpanExplainExample.duration = _KeyDigitSpanExplainExample_allKeys[-1].duration
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
    for thisComponent in DSExplaineExampleComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "DSExplaineExample" ---
for thisComponent in DSExplaineExampleComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if KeyDigitSpanExplainExample.keys in ['', [], None]:  # No response was made
    KeyDigitSpanExplainExample.keys = None
thisExp.addData('KeyDigitSpanExplainExample.keys',KeyDigitSpanExplainExample.keys)
if KeyDigitSpanExplainExample.keys != None:  # we had a response
    thisExp.addData('KeyDigitSpanExplainExample.rt', KeyDigitSpanExplainExample.rt)
    thisExp.addData('KeyDigitSpanExplainExample.duration', KeyDigitSpanExplainExample.duration)
thisExp.nextEntry()
# the Routine "DSExplaineExample" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
LoopExplainDigitSpanOuter = data.TrialHandler(nReps=3.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='LoopExplainDigitSpanOuter')
thisExp.addLoop(LoopExplainDigitSpanOuter)  # add the loop to the experiment
thisLoopExplainDigitSpanOuter = LoopExplainDigitSpanOuter.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisLoopExplainDigitSpanOuter.rgb)
if thisLoopExplainDigitSpanOuter != None:
    for paramName in thisLoopExplainDigitSpanOuter:
        exec('{} = thisLoopExplainDigitSpanOuter[paramName]'.format(paramName))

for thisLoopExplainDigitSpanOuter in LoopExplainDigitSpanOuter:
    currentLoop = LoopExplainDigitSpanOuter
    # abbreviate parameter names if possible (e.g. rgb = thisLoopExplainDigitSpanOuter.rgb)
    if thisLoopExplainDigitSpanOuter != None:
        for paramName in thisLoopExplainDigitSpanOuter:
            exec('{} = thisLoopExplainDigitSpanOuter[paramName]'.format(paramName))
    
    # set up handler to look after randomisation of conditions etc
    LoopExplainDigitSpan = data.TrialHandler(nReps=9.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('Conditions/Conditions_Digits.xlsx'),
        seed=None, name='LoopExplainDigitSpan')
    thisExp.addLoop(LoopExplainDigitSpan)  # add the loop to the experiment
    thisLoopExplainDigitSpan = LoopExplainDigitSpan.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisLoopExplainDigitSpan.rgb)
    if thisLoopExplainDigitSpan != None:
        for paramName in thisLoopExplainDigitSpan:
            exec('{} = thisLoopExplainDigitSpan[paramName]'.format(paramName))
    
    for thisLoopExplainDigitSpan in LoopExplainDigitSpan:
        currentLoop = LoopExplainDigitSpan
        # abbreviate parameter names if possible (e.g. rgb = thisLoopExplainDigitSpan.rgb)
        if thisLoopExplainDigitSpan != None:
            for paramName in thisLoopExplainDigitSpan:
                exec('{} = thisLoopExplainDigitSpan[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "DSAudioDisplayExplain" ---
        continueRoutine = True
        # update component parameters for each repeat
        DSSoundExplain.setSound('A', secs=1.0, hamming=True)
        DSSoundExplain.setVolume(1.0, log=False)
        # keep track of which components have finished
        DSAudioDisplayExplainComponents = [DSSoundExplain]
        for thisComponent in DSAudioDisplayExplainComponents:
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
        
        # --- Run Routine "DSAudioDisplayExplain" ---
        routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 1.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # if DSSoundExplain is starting this frame...
            if DSSoundExplain.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                DSSoundExplain.frameNStart = frameN  # exact frame index
                DSSoundExplain.tStart = t  # local t and not account for scr refresh
                DSSoundExplain.tStartRefresh = tThisFlipGlobal  # on global time
                # add timestamp to datafile
                thisExp.addData('DSSoundExplain.started', tThisFlipGlobal)
                # update status
                DSSoundExplain.status = STARTED
                DSSoundExplain.play(when=win)  # sync with win flip
            
            # if DSSoundExplain is stopping this frame...
            if DSSoundExplain.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > DSSoundExplain.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    DSSoundExplain.tStop = t  # not accounting for scr refresh
                    DSSoundExplain.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'DSSoundExplain.stopped')
                    # update status
                    DSSoundExplain.status = FINISHED
                    DSSoundExplain.stop()
            # update DSSoundExplain status according to whether it's playing
            if DSSoundExplain.isPlaying:
                DSSoundExplain.status = STARTED
            elif DSSoundExplain.isFinished:
                DSSoundExplain.status = FINISHED
            
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
            for thisComponent in DSAudioDisplayExplainComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "DSAudioDisplayExplain" ---
        for thisComponent in DSAudioDisplayExplainComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        DSSoundExplain.stop()  # ensure sound has stopped at end of routine
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-1.000000)
        
        # --- Prepare to start Routine "FocusCross" ---
        continueRoutine = True
        # update component parameters for each repeat
        # keep track of which components have finished
        FocusCrossComponents = [FocusCrossImg]
        for thisComponent in FocusCrossComponents:
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
        
        # --- Run Routine "FocusCross" ---
        routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 1.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *FocusCrossImg* updates
            
            # if FocusCrossImg is starting this frame...
            if FocusCrossImg.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                FocusCrossImg.frameNStart = frameN  # exact frame index
                FocusCrossImg.tStart = t  # local t and not account for scr refresh
                FocusCrossImg.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(FocusCrossImg, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'FocusCrossImg.started')
                # update status
                FocusCrossImg.status = STARTED
                FocusCrossImg.setAutoDraw(True)
            
            # if FocusCrossImg is active this frame...
            if FocusCrossImg.status == STARTED:
                # update params
                pass
            
            # if FocusCrossImg is stopping this frame...
            if FocusCrossImg.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > FocusCrossImg.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    FocusCrossImg.tStop = t  # not accounting for scr refresh
                    FocusCrossImg.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'FocusCrossImg.stopped')
                    # update status
                    FocusCrossImg.status = FINISHED
                    FocusCrossImg.setAutoDraw(False)
            # Run 'Each Frame' code from EyeTrackingFlagFocusCross
            if t == FocusCrossImg.tStart:
                el_tracker.sendMessage('fxon')
            elif t == FocusCrossImg.tStop:
                el_tracker.sendMessage('fxoff')
            
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
            for thisComponent in FocusCrossComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "FocusCross" ---
        for thisComponent in FocusCrossComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-1.000000)
        
        # --- Prepare to start Routine "DSExplainEndInnerLoop" ---
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from CodeDSExplainInnerLoopEnd
        LoopCounter = LoopCounter + 1
        
        CorrectDigits.append(str(int(Digits)))
        
        if LoopCounter >= CurrentDigitChecking:
            LoopCounter = 0 
            LoopExplainDigitSpan.finished = True
        # keep track of which components have finished
        DSExplainEndInnerLoopComponents = []
        for thisComponent in DSExplainEndInnerLoopComponents:
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
        
        # --- Run Routine "DSExplainEndInnerLoop" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
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
            for thisComponent in DSExplainEndInnerLoopComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "DSExplainEndInnerLoop" ---
        for thisComponent in DSExplainEndInnerLoopComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # the Routine "DSExplainEndInnerLoop" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
    # completed 9.0 repeats of 'LoopExplainDigitSpan'
    
    
    # --- Prepare to start Routine "DSResponseAudio" ---
    continueRoutine = True
    # update component parameters for each repeat
    DSAudioKeyNext.keys = []
    DSAudioKeyNext.rt = []
    _DSAudioKeyNext_allKeys = []
    # keep track of which components have finished
    DSResponseAudioComponents = [DSTextResponseAudio, DSAudioKeyNext]
    for thisComponent in DSResponseAudioComponents:
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
    
    # --- Run Routine "DSResponseAudio" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *DSTextResponseAudio* updates
        
        # if DSTextResponseAudio is starting this frame...
        if DSTextResponseAudio.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            DSTextResponseAudio.frameNStart = frameN  # exact frame index
            DSTextResponseAudio.tStart = t  # local t and not account for scr refresh
            DSTextResponseAudio.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(DSTextResponseAudio, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'DSTextResponseAudio.started')
            # update status
            DSTextResponseAudio.status = STARTED
            DSTextResponseAudio.setAutoDraw(True)
        
        # if DSTextResponseAudio is active this frame...
        if DSTextResponseAudio.status == STARTED:
            # update params
            pass
        
        # *DSAudioKeyNext* updates
        waitOnFlip = False
        
        # if DSAudioKeyNext is starting this frame...
        if DSAudioKeyNext.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            DSAudioKeyNext.frameNStart = frameN  # exact frame index
            DSAudioKeyNext.tStart = t  # local t and not account for scr refresh
            DSAudioKeyNext.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(DSAudioKeyNext, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'DSAudioKeyNext.started')
            # update status
            DSAudioKeyNext.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(DSAudioKeyNext.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(DSAudioKeyNext.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if DSAudioKeyNext.status == STARTED and not waitOnFlip:
            theseKeys = DSAudioKeyNext.getKeys(keyList=['space'], waitRelease=False)
            _DSAudioKeyNext_allKeys.extend(theseKeys)
            if len(_DSAudioKeyNext_allKeys):
                DSAudioKeyNext.keys = _DSAudioKeyNext_allKeys[-1].name  # just the last key pressed
                DSAudioKeyNext.rt = _DSAudioKeyNext_allKeys[-1].rt
                DSAudioKeyNext.duration = _DSAudioKeyNext_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        # Run 'Each Frame' code from DSCodeFlag
        if t == DSTextResponseAudio.tStart:
            el_tracker.sendMessage('DTDSResponseon')
        elif t == DSTextResponseAudio.tStop:
            el_tracker.sendMessage('DTDSResponseoff')
        
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
        for thisComponent in DSResponseAudioComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "DSResponseAudio" ---
    for thisComponent in DSResponseAudioComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if DSAudioKeyNext.keys in ['', [], None]:  # No response was made
        DSAudioKeyNext.keys = None
    LoopExplainDigitSpanOuter.addData('DSAudioKeyNext.keys',DSAudioKeyNext.keys)
    if DSAudioKeyNext.keys != None:  # we had a response
        LoopExplainDigitSpanOuter.addData('DSAudioKeyNext.rt', DSAudioKeyNext.rt)
        LoopExplainDigitSpanOuter.addData('DSAudioKeyNext.duration', DSAudioKeyNext.duration)
    # the Routine "DSResponseAudio" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "DSScala" ---
    continueRoutine = True
    # update component parameters for each repeat
    Slider_Respone_Certainty.reset()
    # keep track of which components have finished
    DSScalaComponents = [DSTextScala, Slider_Respone_Certainty]
    for thisComponent in DSScalaComponents:
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
    
    # --- Run Routine "DSScala" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *DSTextScala* updates
        
        # if DSTextScala is starting this frame...
        if DSTextScala.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            DSTextScala.frameNStart = frameN  # exact frame index
            DSTextScala.tStart = t  # local t and not account for scr refresh
            DSTextScala.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(DSTextScala, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'DSTextScala.started')
            # update status
            DSTextScala.status = STARTED
            DSTextScala.setAutoDraw(True)
        
        # if DSTextScala is active this frame...
        if DSTextScala.status == STARTED:
            # update params
            pass
        
        # *Slider_Respone_Certainty* updates
        
        # if Slider_Respone_Certainty is starting this frame...
        if Slider_Respone_Certainty.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Slider_Respone_Certainty.frameNStart = frameN  # exact frame index
            Slider_Respone_Certainty.tStart = t  # local t and not account for scr refresh
            Slider_Respone_Certainty.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Slider_Respone_Certainty, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Slider_Respone_Certainty.started')
            # update status
            Slider_Respone_Certainty.status = STARTED
            Slider_Respone_Certainty.setAutoDraw(True)
        
        # if Slider_Respone_Certainty is active this frame...
        if Slider_Respone_Certainty.status == STARTED:
            # update params
            Slider_Respone_Certainty.setSize((1.0, 0.1), log=False)
        
        # Check Slider_Respone_Certainty for response to end routine
        if Slider_Respone_Certainty.getRating() is not None and Slider_Respone_Certainty.status == STARTED:
            continueRoutine = False
        # Run 'Each Frame' code from DSCodeFlagScala
        if t == DSTextScala.tStart:
            el_tracker.sendMessage('DTDSResponseon')
        elif t == DSTextScala.tStop:
            el_tracker.sendMessage('DTDSResponseoff')
        
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
        for thisComponent in DSScalaComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "DSScala" ---
    for thisComponent in DSScalaComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    LoopExplainDigitSpanOuter.addData('Slider_Respone_Certainty.response', Slider_Respone_Certainty.getRating())
    LoopExplainDigitSpanOuter.addData('Slider_Respone_Certainty.rt', Slider_Respone_Certainty.getRT())
    # the Routine "DSScala" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
# completed 3.0 repeats of 'LoopExplainDigitSpanOuter'


# --- Prepare to start Routine "DSDisplayReal" ---
continueRoutine = True
# update component parameters for each repeat
Next_DigitSpanReal.keys = []
Next_DigitSpanReal.rt = []
_Next_DigitSpanReal_allKeys = []
# keep track of which components have finished
DSDisplayRealComponents = [text, Next_DigitSpanReal]
for thisComponent in DSDisplayRealComponents:
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

# --- Run Routine "DSDisplayReal" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    
    # if text is starting this frame...
    if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text.frameNStart = frameN  # exact frame index
        text.tStart = t  # local t and not account for scr refresh
        text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text.started')
        # update status
        text.status = STARTED
        text.setAutoDraw(True)
    
    # if text is active this frame...
    if text.status == STARTED:
        # update params
        pass
    
    # *Next_DigitSpanReal* updates
    waitOnFlip = False
    
    # if Next_DigitSpanReal is starting this frame...
    if Next_DigitSpanReal.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Next_DigitSpanReal.frameNStart = frameN  # exact frame index
        Next_DigitSpanReal.tStart = t  # local t and not account for scr refresh
        Next_DigitSpanReal.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Next_DigitSpanReal, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'Next_DigitSpanReal.started')
        # update status
        Next_DigitSpanReal.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(Next_DigitSpanReal.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(Next_DigitSpanReal.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if Next_DigitSpanReal.status == STARTED and not waitOnFlip:
        theseKeys = Next_DigitSpanReal.getKeys(keyList=['space'], waitRelease=False)
        _Next_DigitSpanReal_allKeys.extend(theseKeys)
        if len(_Next_DigitSpanReal_allKeys):
            Next_DigitSpanReal.keys = _Next_DigitSpanReal_allKeys[-1].name  # just the last key pressed
            Next_DigitSpanReal.rt = _Next_DigitSpanReal_allKeys[-1].rt
            Next_DigitSpanReal.duration = _Next_DigitSpanReal_allKeys[-1].duration
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
    for thisComponent in DSDisplayRealComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "DSDisplayReal" ---
for thisComponent in DSDisplayRealComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if Next_DigitSpanReal.keys in ['', [], None]:  # No response was made
    Next_DigitSpanReal.keys = None
thisExp.addData('Next_DigitSpanReal.keys',Next_DigitSpanReal.keys)
if Next_DigitSpanReal.keys != None:  # we had a response
    thisExp.addData('Next_DigitSpanReal.rt', Next_DigitSpanReal.rt)
    thisExp.addData('Next_DigitSpanReal.duration', Next_DigitSpanReal.duration)
thisExp.nextEntry()
# the Routine "DSDisplayReal" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "EyeTrackingStart" ---
continueRoutine = True
# update component parameters for each repeat
# Run 'Begin Routine' code from EyeTrackingStartCode
eyetracking.start_recording(el_tracker)
# keep track of which components have finished
EyeTrackingStartComponents = []
for thisComponent in EyeTrackingStartComponents:
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

# --- Run Routine "EyeTrackingStart" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
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
    for thisComponent in EyeTrackingStartComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "EyeTrackingStart" ---
for thisComponent in EyeTrackingStartComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "EyeTrackingStart" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
DSLoopTrailsOuter = data.TrialHandler(nReps=30.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='DSLoopTrailsOuter')
thisExp.addLoop(DSLoopTrailsOuter)  # add the loop to the experiment
thisDSLoopTrailsOuter = DSLoopTrailsOuter.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisDSLoopTrailsOuter.rgb)
if thisDSLoopTrailsOuter != None:
    for paramName in thisDSLoopTrailsOuter:
        exec('{} = thisDSLoopTrailsOuter[paramName]'.format(paramName))

for thisDSLoopTrailsOuter in DSLoopTrailsOuter:
    currentLoop = DSLoopTrailsOuter
    # abbreviate parameter names if possible (e.g. rgb = thisDSLoopTrailsOuter.rgb)
    if thisDSLoopTrailsOuter != None:
        for paramName in thisDSLoopTrailsOuter:
            exec('{} = thisDSLoopTrailsOuter[paramName]'.format(paramName))
    
    # set up handler to look after randomisation of conditions etc
    DSLoopTrailsInner = data.TrialHandler(nReps=1.0, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('Conditions/Conditions_Digits.xlsx'),
        seed=None, name='DSLoopTrailsInner')
    thisExp.addLoop(DSLoopTrailsInner)  # add the loop to the experiment
    thisDSLoopTrailsInner = DSLoopTrailsInner.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisDSLoopTrailsInner.rgb)
    if thisDSLoopTrailsInner != None:
        for paramName in thisDSLoopTrailsInner:
            exec('{} = thisDSLoopTrailsInner[paramName]'.format(paramName))
    
    for thisDSLoopTrailsInner in DSLoopTrailsInner:
        currentLoop = DSLoopTrailsInner
        # abbreviate parameter names if possible (e.g. rgb = thisDSLoopTrailsInner.rgb)
        if thisDSLoopTrailsInner != None:
            for paramName in thisDSLoopTrailsInner:
                exec('{} = thisDSLoopTrailsInner[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "DSDisplayDigitAudioFull" ---
        continueRoutine = True
        # update component parameters for each repeat
        DSDisplaySoundFull.setSound('A', secs=1.0, hamming=True)
        DSDisplaySoundFull.setVolume(1.0, log=False)
        # keep track of which components have finished
        DSDisplayDigitAudioFullComponents = [DSDisplaySoundFull]
        for thisComponent in DSDisplayDigitAudioFullComponents:
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
        
        # --- Run Routine "DSDisplayDigitAudioFull" ---
        routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 1.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # if DSDisplaySoundFull is starting this frame...
            if DSDisplaySoundFull.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                DSDisplaySoundFull.frameNStart = frameN  # exact frame index
                DSDisplaySoundFull.tStart = t  # local t and not account for scr refresh
                DSDisplaySoundFull.tStartRefresh = tThisFlipGlobal  # on global time
                # add timestamp to datafile
                thisExp.addData('DSDisplaySoundFull.started', tThisFlipGlobal)
                # update status
                DSDisplaySoundFull.status = STARTED
                DSDisplaySoundFull.play(when=win)  # sync with win flip
            
            # if DSDisplaySoundFull is stopping this frame...
            if DSDisplaySoundFull.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > DSDisplaySoundFull.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    DSDisplaySoundFull.tStop = t  # not accounting for scr refresh
                    DSDisplaySoundFull.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'DSDisplaySoundFull.stopped')
                    # update status
                    DSDisplaySoundFull.status = FINISHED
                    DSDisplaySoundFull.stop()
            # update DSDisplaySoundFull status according to whether it's playing
            if DSDisplaySoundFull.isPlaying:
                DSDisplaySoundFull.status = STARTED
            elif DSDisplaySoundFull.isFinished:
                DSDisplaySoundFull.status = FINISHED
            # Run 'Each Frame' code from DSEyeTrackingFlagFull
            if t == DSSound.tStart:
                el_tracker.sendMessage('NBFullon')
            elif t == DSSound.tStop:
                el_tracker.sendMessage('NBFulloff')
            
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
            for thisComponent in DSDisplayDigitAudioFullComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "DSDisplayDigitAudioFull" ---
        for thisComponent in DSDisplayDigitAudioFullComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        DSDisplaySoundFull.stop()  # ensure sound has stopped at end of routine
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-1.000000)
        
        # --- Prepare to start Routine "FocusCross" ---
        continueRoutine = True
        # update component parameters for each repeat
        # keep track of which components have finished
        FocusCrossComponents = [FocusCrossImg]
        for thisComponent in FocusCrossComponents:
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
        
        # --- Run Routine "FocusCross" ---
        routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 1.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *FocusCrossImg* updates
            
            # if FocusCrossImg is starting this frame...
            if FocusCrossImg.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                FocusCrossImg.frameNStart = frameN  # exact frame index
                FocusCrossImg.tStart = t  # local t and not account for scr refresh
                FocusCrossImg.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(FocusCrossImg, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'FocusCrossImg.started')
                # update status
                FocusCrossImg.status = STARTED
                FocusCrossImg.setAutoDraw(True)
            
            # if FocusCrossImg is active this frame...
            if FocusCrossImg.status == STARTED:
                # update params
                pass
            
            # if FocusCrossImg is stopping this frame...
            if FocusCrossImg.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > FocusCrossImg.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    FocusCrossImg.tStop = t  # not accounting for scr refresh
                    FocusCrossImg.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'FocusCrossImg.stopped')
                    # update status
                    FocusCrossImg.status = FINISHED
                    FocusCrossImg.setAutoDraw(False)
            # Run 'Each Frame' code from EyeTrackingFlagFocusCross
            if t == FocusCrossImg.tStart:
                el_tracker.sendMessage('fxon')
            elif t == FocusCrossImg.tStop:
                el_tracker.sendMessage('fxoff')
            
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
            for thisComponent in FocusCrossComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "FocusCross" ---
        for thisComponent in FocusCrossComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-1.000000)
        
        # --- Prepare to start Routine "DSTrailsEndInnerLoop" ---
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from DSEndInnerLoops
        LoopCounter = LoopCounter + 1
        
        CorrectDigits.append(str(int(Digits)))
        
        if LoopCounter >= CurrentDigitChecking:
            LoopCounter = 0 
            DSLoopTrailsInner.finished = True
        # keep track of which components have finished
        DSTrailsEndInnerLoopComponents = []
        for thisComponent in DSTrailsEndInnerLoopComponents:
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
        
        # --- Run Routine "DSTrailsEndInnerLoop" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
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
            for thisComponent in DSTrailsEndInnerLoopComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "DSTrailsEndInnerLoop" ---
        for thisComponent in DSTrailsEndInnerLoopComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # the Routine "DSTrailsEndInnerLoop" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
    # completed 1.0 repeats of 'DSLoopTrailsInner'
    
    
    # --- Prepare to start Routine "DSResponseAudio" ---
    continueRoutine = True
    # update component parameters for each repeat
    DSAudioKeyNext.keys = []
    DSAudioKeyNext.rt = []
    _DSAudioKeyNext_allKeys = []
    # keep track of which components have finished
    DSResponseAudioComponents = [DSTextResponseAudio, DSAudioKeyNext]
    for thisComponent in DSResponseAudioComponents:
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
    
    # --- Run Routine "DSResponseAudio" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *DSTextResponseAudio* updates
        
        # if DSTextResponseAudio is starting this frame...
        if DSTextResponseAudio.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            DSTextResponseAudio.frameNStart = frameN  # exact frame index
            DSTextResponseAudio.tStart = t  # local t and not account for scr refresh
            DSTextResponseAudio.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(DSTextResponseAudio, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'DSTextResponseAudio.started')
            # update status
            DSTextResponseAudio.status = STARTED
            DSTextResponseAudio.setAutoDraw(True)
        
        # if DSTextResponseAudio is active this frame...
        if DSTextResponseAudio.status == STARTED:
            # update params
            pass
        
        # *DSAudioKeyNext* updates
        waitOnFlip = False
        
        # if DSAudioKeyNext is starting this frame...
        if DSAudioKeyNext.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            DSAudioKeyNext.frameNStart = frameN  # exact frame index
            DSAudioKeyNext.tStart = t  # local t and not account for scr refresh
            DSAudioKeyNext.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(DSAudioKeyNext, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'DSAudioKeyNext.started')
            # update status
            DSAudioKeyNext.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(DSAudioKeyNext.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(DSAudioKeyNext.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if DSAudioKeyNext.status == STARTED and not waitOnFlip:
            theseKeys = DSAudioKeyNext.getKeys(keyList=['space'], waitRelease=False)
            _DSAudioKeyNext_allKeys.extend(theseKeys)
            if len(_DSAudioKeyNext_allKeys):
                DSAudioKeyNext.keys = _DSAudioKeyNext_allKeys[-1].name  # just the last key pressed
                DSAudioKeyNext.rt = _DSAudioKeyNext_allKeys[-1].rt
                DSAudioKeyNext.duration = _DSAudioKeyNext_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        # Run 'Each Frame' code from DSCodeFlag
        if t == DSTextResponseAudio.tStart:
            el_tracker.sendMessage('DTDSResponseon')
        elif t == DSTextResponseAudio.tStop:
            el_tracker.sendMessage('DTDSResponseoff')
        
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
        for thisComponent in DSResponseAudioComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "DSResponseAudio" ---
    for thisComponent in DSResponseAudioComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if DSAudioKeyNext.keys in ['', [], None]:  # No response was made
        DSAudioKeyNext.keys = None
    DSLoopTrailsOuter.addData('DSAudioKeyNext.keys',DSAudioKeyNext.keys)
    if DSAudioKeyNext.keys != None:  # we had a response
        DSLoopTrailsOuter.addData('DSAudioKeyNext.rt', DSAudioKeyNext.rt)
        DSLoopTrailsOuter.addData('DSAudioKeyNext.duration', DSAudioKeyNext.duration)
    # the Routine "DSResponseAudio" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "DSScala" ---
    continueRoutine = True
    # update component parameters for each repeat
    Slider_Respone_Certainty.reset()
    # keep track of which components have finished
    DSScalaComponents = [DSTextScala, Slider_Respone_Certainty]
    for thisComponent in DSScalaComponents:
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
    
    # --- Run Routine "DSScala" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *DSTextScala* updates
        
        # if DSTextScala is starting this frame...
        if DSTextScala.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            DSTextScala.frameNStart = frameN  # exact frame index
            DSTextScala.tStart = t  # local t and not account for scr refresh
            DSTextScala.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(DSTextScala, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'DSTextScala.started')
            # update status
            DSTextScala.status = STARTED
            DSTextScala.setAutoDraw(True)
        
        # if DSTextScala is active this frame...
        if DSTextScala.status == STARTED:
            # update params
            pass
        
        # *Slider_Respone_Certainty* updates
        
        # if Slider_Respone_Certainty is starting this frame...
        if Slider_Respone_Certainty.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Slider_Respone_Certainty.frameNStart = frameN  # exact frame index
            Slider_Respone_Certainty.tStart = t  # local t and not account for scr refresh
            Slider_Respone_Certainty.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Slider_Respone_Certainty, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Slider_Respone_Certainty.started')
            # update status
            Slider_Respone_Certainty.status = STARTED
            Slider_Respone_Certainty.setAutoDraw(True)
        
        # if Slider_Respone_Certainty is active this frame...
        if Slider_Respone_Certainty.status == STARTED:
            # update params
            Slider_Respone_Certainty.setSize((1.0, 0.1), log=False)
        
        # Check Slider_Respone_Certainty for response to end routine
        if Slider_Respone_Certainty.getRating() is not None and Slider_Respone_Certainty.status == STARTED:
            continueRoutine = False
        # Run 'Each Frame' code from DSCodeFlagScala
        if t == DSTextScala.tStart:
            el_tracker.sendMessage('DTDSResponseon')
        elif t == DSTextScala.tStop:
            el_tracker.sendMessage('DTDSResponseoff')
        
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
        for thisComponent in DSScalaComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "DSScala" ---
    for thisComponent in DSScalaComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    DSLoopTrailsOuter.addData('Slider_Respone_Certainty.response', Slider_Respone_Certainty.getRating())
    DSLoopTrailsOuter.addData('Slider_Respone_Certainty.rt', Slider_Respone_Certainty.getRT())
    # the Routine "DSScala" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 30.0 repeats of 'DSLoopTrailsOuter'


# --- Prepare to start Routine "EyeTrackingStop" ---
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
EyeTrackingStopComponents = []
for thisComponent in EyeTrackingStopComponents:
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

# --- Run Routine "EyeTrackingStop" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
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
    for thisComponent in EyeTrackingStopComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "EyeTrackingStop" ---
for thisComponent in EyeTrackingStopComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# Run 'End Routine' code from EyeTrackingStopCode
eyetracking.stop_recording(el_tracker)

# the Routine "EyeTrackingStop" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "NBExplain" ---
continueRoutine = True
# update component parameters for each repeat
KeyNextNBackExplain.keys = []
KeyNextNBackExplain.rt = []
_KeyNextNBackExplain_allKeys = []
# keep track of which components have finished
NBExplainComponents = [TextNBackExplain, KeyNextNBackExplain]
for thisComponent in NBExplainComponents:
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

# --- Run Routine "NBExplain" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *TextNBackExplain* updates
    
    # if TextNBackExplain is starting this frame...
    if TextNBackExplain.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        TextNBackExplain.frameNStart = frameN  # exact frame index
        TextNBackExplain.tStart = t  # local t and not account for scr refresh
        TextNBackExplain.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(TextNBackExplain, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'TextNBackExplain.started')
        # update status
        TextNBackExplain.status = STARTED
        TextNBackExplain.setAutoDraw(True)
    
    # if TextNBackExplain is active this frame...
    if TextNBackExplain.status == STARTED:
        # update params
        pass
    
    # *KeyNextNBackExplain* updates
    waitOnFlip = False
    
    # if KeyNextNBackExplain is starting this frame...
    if KeyNextNBackExplain.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        KeyNextNBackExplain.frameNStart = frameN  # exact frame index
        KeyNextNBackExplain.tStart = t  # local t and not account for scr refresh
        KeyNextNBackExplain.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(KeyNextNBackExplain, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'KeyNextNBackExplain.started')
        # update status
        KeyNextNBackExplain.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(KeyNextNBackExplain.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(KeyNextNBackExplain.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if KeyNextNBackExplain.status == STARTED and not waitOnFlip:
        theseKeys = KeyNextNBackExplain.getKeys(keyList=['space'], waitRelease=False)
        _KeyNextNBackExplain_allKeys.extend(theseKeys)
        if len(_KeyNextNBackExplain_allKeys):
            KeyNextNBackExplain.keys = _KeyNextNBackExplain_allKeys[-1].name  # just the last key pressed
            KeyNextNBackExplain.rt = _KeyNextNBackExplain_allKeys[-1].rt
            KeyNextNBackExplain.duration = _KeyNextNBackExplain_allKeys[-1].duration
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
    for thisComponent in NBExplainComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "NBExplain" ---
for thisComponent in NBExplainComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if KeyNextNBackExplain.keys in ['', [], None]:  # No response was made
    KeyNextNBackExplain.keys = None
thisExp.addData('KeyNextNBackExplain.keys',KeyNextNBackExplain.keys)
if KeyNextNBackExplain.keys != None:  # we had a response
    thisExp.addData('KeyNextNBackExplain.rt', KeyNextNBackExplain.rt)
    thisExp.addData('KeyNextNBackExplain.duration', KeyNextNBackExplain.duration)
thisExp.nextEntry()
# the Routine "NBExplain" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
NBLoopExplain = data.TrialHandler(nReps=9.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('Conditions/Conditions_Digits.xlsx'),
    seed=None, name='NBLoopExplain')
thisExp.addLoop(NBLoopExplain)  # add the loop to the experiment
thisNBLoopExplain = NBLoopExplain.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisNBLoopExplain.rgb)
if thisNBLoopExplain != None:
    for paramName in thisNBLoopExplain:
        exec('{} = thisNBLoopExplain[paramName]'.format(paramName))

for thisNBLoopExplain in NBLoopExplain:
    currentLoop = NBLoopExplain
    # abbreviate parameter names if possible (e.g. rgb = thisNBLoopExplain.rgb)
    if thisNBLoopExplain != None:
        for paramName in thisNBLoopExplain:
            exec('{} = thisNBLoopExplain[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "NBDisplayDigitExplain" ---
    continueRoutine = True
    # update component parameters for each repeat
    TextNBackDisplayDigit.setText(Digits)
    KeyResponseNBExplain.keys = []
    KeyResponseNBExplain.rt = []
    _KeyResponseNBExplain_allKeys = []
    # Run 'Begin Routine' code from NBCodeExplain
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
    NBDisplayDigitExplainComponents = [TextNBackDisplayDigit, KeyResponseNBExplain]
    for thisComponent in NBDisplayDigitExplainComponents:
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
    
    # --- Run Routine "NBDisplayDigitExplain" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *TextNBackDisplayDigit* updates
        
        # if TextNBackDisplayDigit is starting this frame...
        if TextNBackDisplayDigit.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            TextNBackDisplayDigit.frameNStart = frameN  # exact frame index
            TextNBackDisplayDigit.tStart = t  # local t and not account for scr refresh
            TextNBackDisplayDigit.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(TextNBackDisplayDigit, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'TextNBackDisplayDigit.started')
            # update status
            TextNBackDisplayDigit.status = STARTED
            TextNBackDisplayDigit.setAutoDraw(True)
        
        # if TextNBackDisplayDigit is active this frame...
        if TextNBackDisplayDigit.status == STARTED:
            # update params
            pass
        
        # if TextNBackDisplayDigit is stopping this frame...
        if TextNBackDisplayDigit.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > TextNBackDisplayDigit.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                TextNBackDisplayDigit.tStop = t  # not accounting for scr refresh
                TextNBackDisplayDigit.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'TextNBackDisplayDigit.stopped')
                # update status
                TextNBackDisplayDigit.status = FINISHED
                TextNBackDisplayDigit.setAutoDraw(False)
        
        # *KeyResponseNBExplain* updates
        waitOnFlip = False
        
        # if KeyResponseNBExplain is starting this frame...
        if KeyResponseNBExplain.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            KeyResponseNBExplain.frameNStart = frameN  # exact frame index
            KeyResponseNBExplain.tStart = t  # local t and not account for scr refresh
            KeyResponseNBExplain.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(KeyResponseNBExplain, 'tStartRefresh')  # time at next scr refresh
            # update status
            KeyResponseNBExplain.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(KeyResponseNBExplain.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(KeyResponseNBExplain.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if KeyResponseNBExplain.status == STARTED and not waitOnFlip:
            theseKeys = KeyResponseNBExplain.getKeys(keyList=['y','n'], waitRelease=False)
            _KeyResponseNBExplain_allKeys.extend(theseKeys)
            if len(_KeyResponseNBExplain_allKeys):
                KeyResponseNBExplain.keys = _KeyResponseNBExplain_allKeys[-1].name  # just the last key pressed
                KeyResponseNBExplain.rt = _KeyResponseNBExplain_allKeys[-1].rt
                KeyResponseNBExplain.duration = _KeyResponseNBExplain_allKeys[-1].duration
                # was this correct?
                if (KeyResponseNBExplain.keys == str(correctResponceNBack)) or (KeyResponseNBExplain.keys == correctResponceNBack):
                    KeyResponseNBExplain.corr = 1
                else:
                    KeyResponseNBExplain.corr = 0
        
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
        for thisComponent in NBDisplayDigitExplainComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "NBDisplayDigitExplain" ---
    for thisComponent in NBDisplayDigitExplainComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if KeyResponseNBExplain.keys in ['', [], None]:  # No response was made
        KeyResponseNBExplain.keys = None
        # was no response the correct answer?!
        if str(correctResponceNBack).lower() == 'none':
           KeyResponseNBExplain.corr = 1;  # correct non-response
        else:
           KeyResponseNBExplain.corr = 0;  # failed to respond (incorrectly)
    # store data for NBLoopExplain (TrialHandler)
    NBLoopExplain.addData('KeyResponseNBExplain.keys',KeyResponseNBExplain.keys)
    NBLoopExplain.addData('KeyResponseNBExplain.corr', KeyResponseNBExplain.corr)
    if KeyResponseNBExplain.keys != None:  # we had a response
        NBLoopExplain.addData('KeyResponseNBExplain.rt', KeyResponseNBExplain.rt)
        NBLoopExplain.addData('KeyResponseNBExplain.duration', KeyResponseNBExplain.duration)
    # Run 'End Routine' code from NBCodeExplain
    NBackLoops = NBackLoops + 1
    
    #finishes the test run after 20 NBacks 
    if(NBackLoops  >= 20): 
        NBack.finished = True
    
    # the Routine "NBDisplayDigitExplain" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
# completed 9.0 repeats of 'NBLoopExplain'


# --- Prepare to start Routine "NBFullTest" ---
continueRoutine = True
# update component parameters for each repeat
KeyResponseNBFull.keys = []
KeyResponseNBFull.rt = []
_KeyResponseNBFull_allKeys = []
# keep track of which components have finished
NBFullTestComponents = [TextNBFullTest, KeyResponseNBFull]
for thisComponent in NBFullTestComponents:
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

# --- Run Routine "NBFullTest" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *TextNBFullTest* updates
    
    # if TextNBFullTest is starting this frame...
    if TextNBFullTest.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        TextNBFullTest.frameNStart = frameN  # exact frame index
        TextNBFullTest.tStart = t  # local t and not account for scr refresh
        TextNBFullTest.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(TextNBFullTest, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'TextNBFullTest.started')
        # update status
        TextNBFullTest.status = STARTED
        TextNBFullTest.setAutoDraw(True)
    
    # if TextNBFullTest is active this frame...
    if TextNBFullTest.status == STARTED:
        # update params
        pass
    
    # *KeyResponseNBFull* updates
    waitOnFlip = False
    
    # if KeyResponseNBFull is starting this frame...
    if KeyResponseNBFull.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        KeyResponseNBFull.frameNStart = frameN  # exact frame index
        KeyResponseNBFull.tStart = t  # local t and not account for scr refresh
        KeyResponseNBFull.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(KeyResponseNBFull, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'KeyResponseNBFull.started')
        # update status
        KeyResponseNBFull.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(KeyResponseNBFull.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(KeyResponseNBFull.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if KeyResponseNBFull.status == STARTED and not waitOnFlip:
        theseKeys = KeyResponseNBFull.getKeys(keyList=['space'], waitRelease=False)
        _KeyResponseNBFull_allKeys.extend(theseKeys)
        if len(_KeyResponseNBFull_allKeys):
            KeyResponseNBFull.keys = _KeyResponseNBFull_allKeys[-1].name  # just the last key pressed
            KeyResponseNBFull.rt = _KeyResponseNBFull_allKeys[-1].rt
            KeyResponseNBFull.duration = _KeyResponseNBFull_allKeys[-1].duration
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
    for thisComponent in NBFullTestComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "NBFullTest" ---
for thisComponent in NBFullTestComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if KeyResponseNBFull.keys in ['', [], None]:  # No response was made
    KeyResponseNBFull.keys = None
thisExp.addData('KeyResponseNBFull.keys',KeyResponseNBFull.keys)
if KeyResponseNBFull.keys != None:  # we had a response
    thisExp.addData('KeyResponseNBFull.rt', KeyResponseNBFull.rt)
    thisExp.addData('KeyResponseNBFull.duration', KeyResponseNBFull.duration)
thisExp.nextEntry()
# the Routine "NBFullTest" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "EyeTrackingStart" ---
continueRoutine = True
# update component parameters for each repeat
# Run 'Begin Routine' code from EyeTrackingStartCode
eyetracking.start_recording(el_tracker)
# keep track of which components have finished
EyeTrackingStartComponents = []
for thisComponent in EyeTrackingStartComponents:
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

# --- Run Routine "EyeTrackingStart" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
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
    for thisComponent in EyeTrackingStartComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "EyeTrackingStart" ---
for thisComponent in EyeTrackingStartComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "EyeTrackingStart" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
NBLoopFull = data.TrialHandler(nReps=20.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('Conditions/Conditions_Digits.xlsx'),
    seed=None, name='NBLoopFull')
thisExp.addLoop(NBLoopFull)  # add the loop to the experiment
thisNBLoopFull = NBLoopFull.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisNBLoopFull.rgb)
if thisNBLoopFull != None:
    for paramName in thisNBLoopFull:
        exec('{} = thisNBLoopFull[paramName]'.format(paramName))

for thisNBLoopFull in NBLoopFull:
    currentLoop = NBLoopFull
    # abbreviate parameter names if possible (e.g. rgb = thisNBLoopFull.rgb)
    if thisNBLoopFull != None:
        for paramName in thisNBLoopFull:
            exec('{} = thisNBLoopFull[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "NBackFullDisplayDigit" ---
    continueRoutine = True
    # update component parameters for each repeat
    TextNBackDisplayDigitFull.setText(Digits)
    KeyResponseNBFullTest.keys = []
    KeyResponseNBFullTest.rt = []
    _KeyResponseNBFullTest_allKeys = []
    # Run 'Begin Routine' code from NBCodeFull
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
    NBackFullDisplayDigitComponents = [TextNBackDisplayDigitFull, KeyResponseNBFullTest]
    for thisComponent in NBackFullDisplayDigitComponents:
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
    
    # --- Run Routine "NBackFullDisplayDigit" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *TextNBackDisplayDigitFull* updates
        
        # if TextNBackDisplayDigitFull is starting this frame...
        if TextNBackDisplayDigitFull.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            TextNBackDisplayDigitFull.frameNStart = frameN  # exact frame index
            TextNBackDisplayDigitFull.tStart = t  # local t and not account for scr refresh
            TextNBackDisplayDigitFull.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(TextNBackDisplayDigitFull, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'TextNBackDisplayDigitFull.started')
            # update status
            TextNBackDisplayDigitFull.status = STARTED
            TextNBackDisplayDigitFull.setAutoDraw(True)
        
        # if TextNBackDisplayDigitFull is active this frame...
        if TextNBackDisplayDigitFull.status == STARTED:
            # update params
            pass
        
        # if TextNBackDisplayDigitFull is stopping this frame...
        if TextNBackDisplayDigitFull.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > TextNBackDisplayDigitFull.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                TextNBackDisplayDigitFull.tStop = t  # not accounting for scr refresh
                TextNBackDisplayDigitFull.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'TextNBackDisplayDigitFull.stopped')
                # update status
                TextNBackDisplayDigitFull.status = FINISHED
                TextNBackDisplayDigitFull.setAutoDraw(False)
        
        # *KeyResponseNBFullTest* updates
        waitOnFlip = False
        
        # if KeyResponseNBFullTest is starting this frame...
        if KeyResponseNBFullTest.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            KeyResponseNBFullTest.frameNStart = frameN  # exact frame index
            KeyResponseNBFullTest.tStart = t  # local t and not account for scr refresh
            KeyResponseNBFullTest.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(KeyResponseNBFullTest, 'tStartRefresh')  # time at next scr refresh
            # update status
            KeyResponseNBFullTest.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(KeyResponseNBFullTest.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(KeyResponseNBFullTest.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if KeyResponseNBFullTest.status == STARTED and not waitOnFlip:
            theseKeys = KeyResponseNBFullTest.getKeys(keyList=['y','n'], waitRelease=False)
            _KeyResponseNBFullTest_allKeys.extend(theseKeys)
            if len(_KeyResponseNBFullTest_allKeys):
                KeyResponseNBFullTest.keys = _KeyResponseNBFullTest_allKeys[-1].name  # just the last key pressed
                KeyResponseNBFullTest.rt = _KeyResponseNBFullTest_allKeys[-1].rt
                KeyResponseNBFullTest.duration = _KeyResponseNBFullTest_allKeys[-1].duration
                # was this correct?
                if (KeyResponseNBFullTest.keys == str(correctResponceNBack)) or (KeyResponseNBFullTest.keys == correctResponceNBack):
                    KeyResponseNBFullTest.corr = 1
                else:
                    KeyResponseNBFullTest.corr = 0
        # Run 'Each Frame' code from NBCodeFull
        if t == TextNBackDisplayDigitFull.tStart:
            el_tracker.sendMessage('NBFullon')
        elif t == TextNBackDisplayDigitFull.tStop:
            el_tracker.sendMessage('NBFulloff')
        
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
        for thisComponent in NBackFullDisplayDigitComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "NBackFullDisplayDigit" ---
    for thisComponent in NBackFullDisplayDigitComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if KeyResponseNBFullTest.keys in ['', [], None]:  # No response was made
        KeyResponseNBFullTest.keys = None
        # was no response the correct answer?!
        if str(correctResponceNBack).lower() == 'none':
           KeyResponseNBFullTest.corr = 1;  # correct non-response
        else:
           KeyResponseNBFullTest.corr = 0;  # failed to respond (incorrectly)
    # store data for NBLoopFull (TrialHandler)
    NBLoopFull.addData('KeyResponseNBFullTest.keys',KeyResponseNBFullTest.keys)
    NBLoopFull.addData('KeyResponseNBFullTest.corr', KeyResponseNBFullTest.corr)
    if KeyResponseNBFullTest.keys != None:  # we had a response
        NBLoopFull.addData('KeyResponseNBFullTest.rt', KeyResponseNBFullTest.rt)
        NBLoopFull.addData('KeyResponseNBFullTest.duration', KeyResponseNBFullTest.duration)
    # Run 'End Routine' code from NBCodeFull
    NBackLoops = NBackLoops + 1
    
    thisExp.addData('NBackFull', NBackLoops)
    
    #finishes the NBack after getting all the single task data
    #now 100
    if(NBackLoops  >= 100): 
        NBack.finished = True
    
    # the Routine "NBackFullDisplayDigit" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
# completed 20.0 repeats of 'NBLoopFull'


# --- Prepare to start Routine "EyeTrackingStop" ---
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
EyeTrackingStopComponents = []
for thisComponent in EyeTrackingStopComponents:
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

# --- Run Routine "EyeTrackingStop" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
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
    for thisComponent in EyeTrackingStopComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "EyeTrackingStop" ---
for thisComponent in EyeTrackingStopComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# Run 'End Routine' code from EyeTrackingStopCode
eyetracking.stop_recording(el_tracker)

# the Routine "EyeTrackingStop" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "DTExplain" ---
continueRoutine = True
# update component parameters for each repeat
KeyResponseDTExplain.keys = []
KeyResponseDTExplain.rt = []
_KeyResponseDTExplain_allKeys = []
# keep track of which components have finished
DTExplainComponents = [TextDTExplain, KeyResponseDTExplain]
for thisComponent in DTExplainComponents:
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

# --- Run Routine "DTExplain" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *TextDTExplain* updates
    
    # if TextDTExplain is starting this frame...
    if TextDTExplain.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        TextDTExplain.frameNStart = frameN  # exact frame index
        TextDTExplain.tStart = t  # local t and not account for scr refresh
        TextDTExplain.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(TextDTExplain, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'TextDTExplain.started')
        # update status
        TextDTExplain.status = STARTED
        TextDTExplain.setAutoDraw(True)
    
    # if TextDTExplain is active this frame...
    if TextDTExplain.status == STARTED:
        # update params
        pass
    
    # *KeyResponseDTExplain* updates
    waitOnFlip = False
    
    # if KeyResponseDTExplain is starting this frame...
    if KeyResponseDTExplain.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        KeyResponseDTExplain.frameNStart = frameN  # exact frame index
        KeyResponseDTExplain.tStart = t  # local t and not account for scr refresh
        KeyResponseDTExplain.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(KeyResponseDTExplain, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'KeyResponseDTExplain.started')
        # update status
        KeyResponseDTExplain.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(KeyResponseDTExplain.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(KeyResponseDTExplain.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if KeyResponseDTExplain.status == STARTED and not waitOnFlip:
        theseKeys = KeyResponseDTExplain.getKeys(keyList=['space'], waitRelease=False)
        _KeyResponseDTExplain_allKeys.extend(theseKeys)
        if len(_KeyResponseDTExplain_allKeys):
            KeyResponseDTExplain.keys = _KeyResponseDTExplain_allKeys[-1].name  # just the last key pressed
            KeyResponseDTExplain.rt = _KeyResponseDTExplain_allKeys[-1].rt
            KeyResponseDTExplain.duration = _KeyResponseDTExplain_allKeys[-1].duration
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
    for thisComponent in DTExplainComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "DTExplain" ---
for thisComponent in DTExplainComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if KeyResponseDTExplain.keys in ['', [], None]:  # No response was made
    KeyResponseDTExplain.keys = None
thisExp.addData('KeyResponseDTExplain.keys',KeyResponseDTExplain.keys)
if KeyResponseDTExplain.keys != None:  # we had a response
    thisExp.addData('KeyResponseDTExplain.rt', KeyResponseDTExplain.rt)
    thisExp.addData('KeyResponseDTExplain.duration', KeyResponseDTExplain.duration)
thisExp.nextEntry()
# the Routine "DTExplain" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "EyeTrackingStart" ---
continueRoutine = True
# update component parameters for each repeat
# Run 'Begin Routine' code from EyeTrackingStartCode
eyetracking.start_recording(el_tracker)
# keep track of which components have finished
EyeTrackingStartComponents = []
for thisComponent in EyeTrackingStartComponents:
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

# --- Run Routine "EyeTrackingStart" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
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
    for thisComponent in EyeTrackingStartComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "EyeTrackingStart" ---
for thisComponent in EyeTrackingStartComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "EyeTrackingStart" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
DT_Full_Loop = data.TrialHandler(nReps=30.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='DT_Full_Loop')
thisExp.addLoop(DT_Full_Loop)  # add the loop to the experiment
thisDT_Full_Loop = DT_Full_Loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisDT_Full_Loop.rgb)
if thisDT_Full_Loop != None:
    for paramName in thisDT_Full_Loop:
        exec('{} = thisDT_Full_Loop[paramName]'.format(paramName))

for thisDT_Full_Loop in DT_Full_Loop:
    currentLoop = DT_Full_Loop
    # abbreviate parameter names if possible (e.g. rgb = thisDT_Full_Loop.rgb)
    if thisDT_Full_Loop != None:
        for paramName in thisDT_Full_Loop:
            exec('{} = thisDT_Full_Loop[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "DT_ManageVars" ---
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from DT_ManageVarsCode
    DTTrailNumber = DTTrailNumber + 1
    thisExp.addData('DTTrailNumber ', DTTrailNumber)
    
    # keep track of which components have finished
    DT_ManageVarsComponents = []
    for thisComponent in DT_ManageVarsComponents:
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
    
    # --- Run Routine "DT_ManageVars" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
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
        for thisComponent in DT_ManageVarsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "DT_ManageVars" ---
    for thisComponent in DT_ManageVarsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "DT_ManageVars" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    DT_DS_InnerLoop = data.TrialHandler(nReps=9.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('Conditions/Conditions_Digits.xlsx'),
        seed=None, name='DT_DS_InnerLoop')
    thisExp.addLoop(DT_DS_InnerLoop)  # add the loop to the experiment
    thisDT_DS_InnerLoop = DT_DS_InnerLoop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisDT_DS_InnerLoop.rgb)
    if thisDT_DS_InnerLoop != None:
        for paramName in thisDT_DS_InnerLoop:
            exec('{} = thisDT_DS_InnerLoop[paramName]'.format(paramName))
    
    for thisDT_DS_InnerLoop in DT_DS_InnerLoop:
        currentLoop = DT_DS_InnerLoop
        # abbreviate parameter names if possible (e.g. rgb = thisDT_DS_InnerLoop.rgb)
        if thisDT_DS_InnerLoop != None:
            for paramName in thisDT_DS_InnerLoop:
                exec('{} = thisDT_DS_InnerLoop[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "DT_DS_DisplayAudio" ---
        continueRoutine = True
        # update component parameters for each repeat
        DT_DS_Audio.setSound('A', secs=1.0, hamming=True)
        DT_DS_Audio.setVolume(1.0, log=False)
        # keep track of which components have finished
        DT_DS_DisplayAudioComponents = [DT_DS_Audio]
        for thisComponent in DT_DS_DisplayAudioComponents:
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
        
        # --- Run Routine "DT_DS_DisplayAudio" ---
        routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 1.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # if DT_DS_Audio is starting this frame...
            if DT_DS_Audio.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                DT_DS_Audio.frameNStart = frameN  # exact frame index
                DT_DS_Audio.tStart = t  # local t and not account for scr refresh
                DT_DS_Audio.tStartRefresh = tThisFlipGlobal  # on global time
                # add timestamp to datafile
                thisExp.addData('DT_DS_Audio.started', tThisFlipGlobal)
                # update status
                DT_DS_Audio.status = STARTED
                DT_DS_Audio.play(when=win)  # sync with win flip
            
            # if DT_DS_Audio is stopping this frame...
            if DT_DS_Audio.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > DT_DS_Audio.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    DT_DS_Audio.tStop = t  # not accounting for scr refresh
                    DT_DS_Audio.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'DT_DS_Audio.stopped')
                    # update status
                    DT_DS_Audio.status = FINISHED
                    DT_DS_Audio.stop()
            # update DT_DS_Audio status according to whether it's playing
            if DT_DS_Audio.isPlaying:
                DT_DS_Audio.status = STARTED
            elif DT_DS_Audio.isFinished:
                DT_DS_Audio.status = FINISHED
            # Run 'Each Frame' code from DT_DS_EyeTrackingFlag
            if t == DT_DS_Audio.tStart:
                el_tracker.sendMessage('DTDSon')
            elif t == DT_DS_Audio.tStop:
                el_tracker.sendMessage('DTDSoff')
            
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
            for thisComponent in DT_DS_DisplayAudioComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "DT_DS_DisplayAudio" ---
        for thisComponent in DT_DS_DisplayAudioComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        DT_DS_Audio.stop()  # ensure sound has stopped at end of routine
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-1.000000)
        
        # --- Prepare to start Routine "FocusCross" ---
        continueRoutine = True
        # update component parameters for each repeat
        # keep track of which components have finished
        FocusCrossComponents = [FocusCrossImg]
        for thisComponent in FocusCrossComponents:
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
        
        # --- Run Routine "FocusCross" ---
        routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 1.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *FocusCrossImg* updates
            
            # if FocusCrossImg is starting this frame...
            if FocusCrossImg.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                FocusCrossImg.frameNStart = frameN  # exact frame index
                FocusCrossImg.tStart = t  # local t and not account for scr refresh
                FocusCrossImg.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(FocusCrossImg, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'FocusCrossImg.started')
                # update status
                FocusCrossImg.status = STARTED
                FocusCrossImg.setAutoDraw(True)
            
            # if FocusCrossImg is active this frame...
            if FocusCrossImg.status == STARTED:
                # update params
                pass
            
            # if FocusCrossImg is stopping this frame...
            if FocusCrossImg.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > FocusCrossImg.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    FocusCrossImg.tStop = t  # not accounting for scr refresh
                    FocusCrossImg.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'FocusCrossImg.stopped')
                    # update status
                    FocusCrossImg.status = FINISHED
                    FocusCrossImg.setAutoDraw(False)
            # Run 'Each Frame' code from EyeTrackingFlagFocusCross
            if t == FocusCrossImg.tStart:
                el_tracker.sendMessage('fxon')
            elif t == FocusCrossImg.tStop:
                el_tracker.sendMessage('fxoff')
            
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
            for thisComponent in FocusCrossComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "FocusCross" ---
        for thisComponent in FocusCrossComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-1.000000)
        
        # --- Prepare to start Routine "DT_DS_InnerLoopEnd" ---
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from DT_DS_CodeEndInnerLoop
        LoopCounter = LoopCounter + 1
        
        CorrectDigits.append(str(int(Digits)))
        
        #displaies the max found digits - 2
        if LoopCounter >= (CurrentDigitChecking - 2):
            LoopCounter = 0 
            DT_DS_InnerLoop.finished = True
        # keep track of which components have finished
        DT_DS_InnerLoopEndComponents = []
        for thisComponent in DT_DS_InnerLoopEndComponents:
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
        
        # --- Run Routine "DT_DS_InnerLoopEnd" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
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
            for thisComponent in DT_DS_InnerLoopEndComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "DT_DS_InnerLoopEnd" ---
        for thisComponent in DT_DS_InnerLoopEndComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # the Routine "DT_DS_InnerLoopEnd" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
    # completed 9.0 repeats of 'DT_DS_InnerLoop'
    
    
    # set up handler to look after randomisation of conditions etc
    DT_NB_NBackLoop = data.TrialHandler(nReps=5.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('Conditions/Conditions_Digits.xlsx'),
        seed=None, name='DT_NB_NBackLoop')
    thisExp.addLoop(DT_NB_NBackLoop)  # add the loop to the experiment
    thisDT_NB_NBackLoop = DT_NB_NBackLoop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisDT_NB_NBackLoop.rgb)
    if thisDT_NB_NBackLoop != None:
        for paramName in thisDT_NB_NBackLoop:
            exec('{} = thisDT_NB_NBackLoop[paramName]'.format(paramName))
    
    for thisDT_NB_NBackLoop in DT_NB_NBackLoop:
        currentLoop = DT_NB_NBackLoop
        # abbreviate parameter names if possible (e.g. rgb = thisDT_NB_NBackLoop.rgb)
        if thisDT_NB_NBackLoop != None:
            for paramName in thisDT_NB_NBackLoop:
                exec('{} = thisDT_NB_NBackLoop[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "DT_NB_Display" ---
        continueRoutine = True
        # update component parameters for each repeat
        DT_NB_TextDisplay.setText(Digits)
        DT_NB_KeyResponse.keys = []
        DT_NB_KeyResponse.rt = []
        _DT_NB_KeyResponse_allKeys = []
        # Run 'Begin Routine' code from DT_NB_CodeEndNB
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
        DT_NB_DisplayComponents = [DT_NB_TextDisplay, DT_NB_KeyResponse]
        for thisComponent in DT_NB_DisplayComponents:
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
        
        # --- Run Routine "DT_NB_Display" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *DT_NB_TextDisplay* updates
            
            # if DT_NB_TextDisplay is starting this frame...
            if DT_NB_TextDisplay.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                DT_NB_TextDisplay.frameNStart = frameN  # exact frame index
                DT_NB_TextDisplay.tStart = t  # local t and not account for scr refresh
                DT_NB_TextDisplay.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(DT_NB_TextDisplay, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'DT_NB_TextDisplay.started')
                # update status
                DT_NB_TextDisplay.status = STARTED
                DT_NB_TextDisplay.setAutoDraw(True)
            
            # if DT_NB_TextDisplay is active this frame...
            if DT_NB_TextDisplay.status == STARTED:
                # update params
                pass
            
            # if DT_NB_TextDisplay is stopping this frame...
            if DT_NB_TextDisplay.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > DT_NB_TextDisplay.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    DT_NB_TextDisplay.tStop = t  # not accounting for scr refresh
                    DT_NB_TextDisplay.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'DT_NB_TextDisplay.stopped')
                    # update status
                    DT_NB_TextDisplay.status = FINISHED
                    DT_NB_TextDisplay.setAutoDraw(False)
            
            # *DT_NB_KeyResponse* updates
            waitOnFlip = False
            
            # if DT_NB_KeyResponse is starting this frame...
            if DT_NB_KeyResponse.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                DT_NB_KeyResponse.frameNStart = frameN  # exact frame index
                DT_NB_KeyResponse.tStart = t  # local t and not account for scr refresh
                DT_NB_KeyResponse.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(DT_NB_KeyResponse, 'tStartRefresh')  # time at next scr refresh
                # update status
                DT_NB_KeyResponse.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(DT_NB_KeyResponse.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(DT_NB_KeyResponse.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if DT_NB_KeyResponse.status == STARTED and not waitOnFlip:
                theseKeys = DT_NB_KeyResponse.getKeys(keyList=['y','n'], waitRelease=False)
                _DT_NB_KeyResponse_allKeys.extend(theseKeys)
                if len(_DT_NB_KeyResponse_allKeys):
                    DT_NB_KeyResponse.keys = _DT_NB_KeyResponse_allKeys[-1].name  # just the last key pressed
                    DT_NB_KeyResponse.rt = _DT_NB_KeyResponse_allKeys[-1].rt
                    DT_NB_KeyResponse.duration = _DT_NB_KeyResponse_allKeys[-1].duration
                    # was this correct?
                    if (DT_NB_KeyResponse.keys == str(correctResponceNBack)) or (DT_NB_KeyResponse.keys == correctResponceNBack):
                        DT_NB_KeyResponse.corr = 1
                    else:
                        DT_NB_KeyResponse.corr = 0
            # Run 'Each Frame' code from DT_NB_CodeEndNB
            if t == DT_NB_TextDisplay.tStart:
                el_tracker.sendMessage('DTNBon')
            elif t == DT_NB_TextDisplay.tStop:
                el_tracker.sendMessage('DTNBoff')
            
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
            for thisComponent in DT_NB_DisplayComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "DT_NB_Display" ---
        for thisComponent in DT_NB_DisplayComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if DT_NB_KeyResponse.keys in ['', [], None]:  # No response was made
            DT_NB_KeyResponse.keys = None
            # was no response the correct answer?!
            if str(correctResponceNBack).lower() == 'none':
               DT_NB_KeyResponse.corr = 1;  # correct non-response
            else:
               DT_NB_KeyResponse.corr = 0;  # failed to respond (incorrectly)
        # store data for DT_NB_NBackLoop (TrialHandler)
        DT_NB_NBackLoop.addData('DT_NB_KeyResponse.keys',DT_NB_KeyResponse.keys)
        DT_NB_NBackLoop.addData('DT_NB_KeyResponse.corr', DT_NB_KeyResponse.corr)
        if DT_NB_KeyResponse.keys != None:  # we had a response
            DT_NB_NBackLoop.addData('DT_NB_KeyResponse.rt', DT_NB_KeyResponse.rt)
            DT_NB_NBackLoop.addData('DT_NB_KeyResponse.duration', DT_NB_KeyResponse.duration)
        # Run 'End Routine' code from DT_NB_CodeEndNB
        DTNBackNumber = DTNBackNumber + 1
        
        thisExp.addData('DTNBackNumber', DTNBackNumber)
        
        #finishes the NBack after the size of DT
        #currently 10
        if(DTNBackNumber  >= 10): 
            DT_NB_NBackLoop.finished = True
        
        # the Routine "DT_NB_Display" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 5.0 repeats of 'DT_NB_NBackLoop'
    
    
    # --- Prepare to start Routine "DT_DS_ResponeInAudio" ---
    continueRoutine = True
    # update component parameters for each repeat
    KeyResponseNext.keys = []
    KeyResponseNext.rt = []
    _KeyResponseNext_allKeys = []
    # keep track of which components have finished
    DT_DS_ResponeInAudioComponents = [DT_DS_TextResponseInAudio, KeyResponseNext]
    for thisComponent in DT_DS_ResponeInAudioComponents:
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
    
    # --- Run Routine "DT_DS_ResponeInAudio" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *DT_DS_TextResponseInAudio* updates
        
        # if DT_DS_TextResponseInAudio is starting this frame...
        if DT_DS_TextResponseInAudio.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            DT_DS_TextResponseInAudio.frameNStart = frameN  # exact frame index
            DT_DS_TextResponseInAudio.tStart = t  # local t and not account for scr refresh
            DT_DS_TextResponseInAudio.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(DT_DS_TextResponseInAudio, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'DT_DS_TextResponseInAudio.started')
            # update status
            DT_DS_TextResponseInAudio.status = STARTED
            DT_DS_TextResponseInAudio.setAutoDraw(True)
        
        # if DT_DS_TextResponseInAudio is active this frame...
        if DT_DS_TextResponseInAudio.status == STARTED:
            # update params
            pass
        
        # *KeyResponseNext* updates
        waitOnFlip = False
        
        # if KeyResponseNext is starting this frame...
        if KeyResponseNext.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            KeyResponseNext.frameNStart = frameN  # exact frame index
            KeyResponseNext.tStart = t  # local t and not account for scr refresh
            KeyResponseNext.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(KeyResponseNext, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'KeyResponseNext.started')
            # update status
            KeyResponseNext.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(KeyResponseNext.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(KeyResponseNext.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if KeyResponseNext.status == STARTED and not waitOnFlip:
            theseKeys = KeyResponseNext.getKeys(keyList=['space'], waitRelease=False)
            _KeyResponseNext_allKeys.extend(theseKeys)
            if len(_KeyResponseNext_allKeys):
                KeyResponseNext.keys = _KeyResponseNext_allKeys[-1].name  # just the last key pressed
                KeyResponseNext.rt = _KeyResponseNext_allKeys[-1].rt
                KeyResponseNext.duration = _KeyResponseNext_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        # Run 'Each Frame' code from DT_DS_EyeTrackingFlagResponse
        if t == DT_DS_TextResponseInAudio.tStart:
            el_tracker.sendMessage('DTDSResponseon')
        elif t == DT_DS_TextResponseInAudio.tStop:
            el_tracker.sendMessage('DTDSResponseoff')
        
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
        for thisComponent in DT_DS_ResponeInAudioComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "DT_DS_ResponeInAudio" ---
    for thisComponent in DT_DS_ResponeInAudioComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if KeyResponseNext.keys in ['', [], None]:  # No response was made
        KeyResponseNext.keys = None
    DT_Full_Loop.addData('KeyResponseNext.keys',KeyResponseNext.keys)
    if KeyResponseNext.keys != None:  # we had a response
        DT_Full_Loop.addData('KeyResponseNext.rt', KeyResponseNext.rt)
        DT_Full_Loop.addData('KeyResponseNext.duration', KeyResponseNext.duration)
    # the Routine "DT_DS_ResponeInAudio" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "DT_DS_ResponseScala" ---
    continueRoutine = True
    # update component parameters for each repeat
    DT_DS_Scala.reset()
    # keep track of which components have finished
    DT_DS_ResponseScalaComponents = [DT_DS_TextScala, DT_DS_Scala]
    for thisComponent in DT_DS_ResponseScalaComponents:
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
    
    # --- Run Routine "DT_DS_ResponseScala" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *DT_DS_TextScala* updates
        
        # if DT_DS_TextScala is starting this frame...
        if DT_DS_TextScala.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            DT_DS_TextScala.frameNStart = frameN  # exact frame index
            DT_DS_TextScala.tStart = t  # local t and not account for scr refresh
            DT_DS_TextScala.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(DT_DS_TextScala, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'DT_DS_TextScala.started')
            # update status
            DT_DS_TextScala.status = STARTED
            DT_DS_TextScala.setAutoDraw(True)
        
        # if DT_DS_TextScala is active this frame...
        if DT_DS_TextScala.status == STARTED:
            # update params
            pass
        
        # *DT_DS_Scala* updates
        
        # if DT_DS_Scala is starting this frame...
        if DT_DS_Scala.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            DT_DS_Scala.frameNStart = frameN  # exact frame index
            DT_DS_Scala.tStart = t  # local t and not account for scr refresh
            DT_DS_Scala.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(DT_DS_Scala, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'DT_DS_Scala.started')
            # update status
            DT_DS_Scala.status = STARTED
            DT_DS_Scala.setAutoDraw(True)
        
        # if DT_DS_Scala is active this frame...
        if DT_DS_Scala.status == STARTED:
            # update params
            DT_DS_Scala.setSize((1.0, 0.1), log=False)
        
        # Check DT_DS_Scala for response to end routine
        if DT_DS_Scala.getRating() is not None and DT_DS_Scala.status == STARTED:
            continueRoutine = False
        # Run 'Each Frame' code from DT_DS_CodeSaveScala
        if t == DT_DS_TextScala.tStart:
            el_tracker.sendMessage('DTDSScalaon')
        elif t == DT_DS_TextScala.tStop:
            el_tracker.sendMessage('DTDSScalaoff')
        
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
        for thisComponent in DT_DS_ResponseScalaComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "DT_DS_ResponseScala" ---
    for thisComponent in DT_DS_ResponseScalaComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    DT_Full_Loop.addData('DT_DS_Scala.response', DT_DS_Scala.getRating())
    DT_Full_Loop.addData('DT_DS_Scala.rt', DT_DS_Scala.getRT())
    # Run 'End Routine' code from DT_DS_CodeSaveScala
    DTDigitSpanSacalaResponse = DT_DS_Scala.getRating()
    thisExp.addData('DTDigitSpanSacalaResponse', DTNBackNumber)
    # the Routine "DT_DS_ResponseScala" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 30.0 repeats of 'DT_Full_Loop'


# --- Prepare to start Routine "EyeTrackingStop" ---
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
EyeTrackingStopComponents = []
for thisComponent in EyeTrackingStopComponents:
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

# --- Run Routine "EyeTrackingStop" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
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
    for thisComponent in EyeTrackingStopComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "EyeTrackingStop" ---
for thisComponent in EyeTrackingStopComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# Run 'End Routine' code from EyeTrackingStopCode
eyetracking.stop_recording(el_tracker)

# the Routine "EyeTrackingStop" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "EndScreen" ---
continueRoutine = True
# update component parameters for each repeat
# Run 'Begin Routine' code from EyeTrackingEndScreen
eyetracking.close_tracker_download_edf(el_tracker, edf_file, edf_fname,
eyetracker_data_folder)
# keep track of which components have finished
EndScreenComponents = [TextEndScreen]
for thisComponent in EndScreenComponents:
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

# --- Run Routine "EndScreen" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *TextEndScreen* updates
    
    # if TextEndScreen is starting this frame...
    if TextEndScreen.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        TextEndScreen.frameNStart = frameN  # exact frame index
        TextEndScreen.tStart = t  # local t and not account for scr refresh
        TextEndScreen.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(TextEndScreen, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'TextEndScreen.started')
        # update status
        TextEndScreen.status = STARTED
        TextEndScreen.setAutoDraw(True)
    
    # if TextEndScreen is active this frame...
    if TextEndScreen.status == STARTED:
        # update params
        pass
    
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
    for thisComponent in EndScreenComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "EndScreen" ---
for thisComponent in EndScreenComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "EndScreen" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

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
