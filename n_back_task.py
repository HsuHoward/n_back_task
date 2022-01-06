#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.0.0b9),
    on Thu Nov 29 15:28:25 2018
If you publish work using this script please cite the PsychoPy publications:
    Peirce, JW (2007) PsychoPy - Psychophysics software in Python.
        Journal of Neuroscience Methods, 162(1-2), 8-13.
    Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy.
        Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import absolute_import, division
from psychopy import locale_setup, sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
expName = 'nback'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
                                 extraInfo=expInfo, runtimeInfo=None,
                                 originPath='/Users/howardhsu/Desktop/pychopy/n_back_task project/n_back_task.py',
                                 savePickle=True, saveWideText=True,
                                 dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename + '.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[1280, 800], fullscr=True, screen=0,
    allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[-1, -1, -1], colorSpace='rgb',
    blendMode='avg', useFBO=True)
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Initialize components for Routine "instruction"
instructionClock = core.Clock()
blockloop_N = 0

instuction = visual.TextStim(win=win, name='instuction',
                             text='please recognize if the present stimuli is as same as the one 2 trials before\nif yes, press "z" button\nif no, press "x" button\nplease do response quickly and accurately\n\npress "space" to start ',
                             font='Arial',
                             pos=(0, 0), height=0.1, wrapWidth=None, ori=0,
                             color='white', colorSpace='rgb', opacity=1,
                             languageStyle='LTR',
                             depth=-1.0);

# Initialize components for Routine "target"
targetClock = core.Clock()

stimulus_list = []
target_n = 0

i = 0  # stimulus index

fixation1_target = visual.TextStim(win=win, name='fixation1_target',
                                   text='+',
                                   font='Arial',
                                   pos=(0, 0), height=0.5, wrapWidth=None, ori=0,
                                   color='white', colorSpace='rgb', opacity=1,
                                   languageStyle='LTR',
                                   depth=-1.0);
target_1 = visual.TextStim(win=win, name='target_1',
                           text='default text',
                           font='Arial',
                           pos=(0, 0), height=0.5, wrapWidth=None, ori=0,
                           color='white', colorSpace='rgb', opacity=1,
                           languageStyle='LTR',
                           depth=-2.0);
ISI_target = visual.TextStim(win=win, name='ISI_target',
                             text=None,
                             font='Arial',
                             pos=(0, 0), height=0.5, wrapWidth=None, ori=0,
                             color='white', colorSpace='rgb', opacity=1,
                             languageStyle='LTR',
                             depth=-3.0);

# Initialize components for Routine "n_back_task"
n_backClock = core.Clock()

import random

zeroback_index = 0
oneback_index = 0
twoback_index = 0

zeroback_TypeControl_list = ['0'] * 128 + ['1'] * 32  # 0 is nontarget; 1 is target
random.shuffle(zeroback_TypeControl_list)

oneback_TypeControl_list = ['0'] * 128 + ['1'] * 32  # 0 is nontarget; 1 is target
random.shuffle(oneback_TypeControl_list)

twoback_TypeControl_list = ['0'] * 128 + ['1'] * 32  # 0 is nontarget; 1 is target
random.shuffle(twoback_TypeControl_list)
fixation = visual.TextStim(win=win, name='fixation',
                           text='+',
                           font='Arial',
                           pos=(0, 0), height=0.5, wrapWidth=None, ori=0,
                           color='white', colorSpace='rgb', opacity=1,
                           languageStyle='LTR',
                           depth=-1.0);
question = visual.TextStim(win=win, name='question',
                           text='default text',
                           font='Arial',
                           pos=(0, 0), height=0.5, wrapWidth=None, ori=0,
                           color='white', colorSpace='rgb', opacity=1,
                           languageStyle='LTR',
                           depth=-2.0);

# Initialize components for Routine "ISI"
ISIClock = core.Clock()
rest = visual.TextStim(win=win, name='rest',
                       text=None,
                       font='Arial',
                       pos=(0, 0), height=0.1, wrapWidth=None, ori=0,
                       color='white', colorSpace='rgb', opacity=1,
                       languageStyle='LTR',
                       depth=0.0);

# Initialize components for Routine "block_rest"
block_restClock = core.Clock()
block_rest_control = visual.TextStim(win=win, name='block_rest_control',
                                     text='take a break\npress "space" to start next block',
                                     font='Arial',
                                     pos=(0, 0), height=0.1, wrapWidth=None, ori=0,
                                     color='white', colorSpace='rgb', opacity=1,
                                     languageStyle='LTR',
                                     depth=0.0);

# Initialize components for Routine "end"
endClock = core.Clock()
final = visual.TextStim(win=win, name='final',
                        text='The experiment is done\nPlease wait to the conductor ',
                        font='Arial',
                        pos=(0, 0), height=0.1, wrapWidth=None, ori=0,
                        color='white', colorSpace='rgb', opacity=1,
                        languageStyle='LTR',
                        depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine

# set up handler to look after randomisation of conditions etc
blockloop = data.TrialHandler(nReps=3, method='random',
                              extraInfo=expInfo, originPath=-1,
                              trialList=[None],
                              seed=None, name='blockloop')
thisExp.addLoop(blockloop)  # add the loop to the experiment
thisBlockloop = blockloop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisBlockloop.rgb)
if thisBlockloop != None:
    for paramName in thisBlockloop:
        exec('{} = thisBlockloop[paramName]'.format(paramName))

for thisBlockloop in blockloop:
    currentLoop = blockloop
    # abbreviate parameter names if possible (e.g. rgb = thisBlockloop.rgb)
    if thisBlockloop != None:
        for paramName in thisBlockloop:
            exec('{} = thisBlockloop[paramName]'.format(paramName))

    # ------Prepare to start Routine "instruction"-------
    t = 0
    instructionClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    if blockloop_N == 0:
        instructionTXT = 'this is zero back'
        target_n = 0
    elif blockloop_N == 1:
        instructionTXT = 'this is one back'
        target_n = 1
    elif blockloop_N == 2:
        instruction = 'this is two back'
        target_n = 2
    startkey = event.BuilderKeyResponse()
    # keep track of which components have finished
    instructionComponents = [instuction, startkey]
    for thisComponent in instructionComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED

    # -------Start Routine "instruction"-------
    while continueRoutine:
        # get current time
        t = instructionClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame

        # *instuction* updates
        if t >= 0.0 and instuction.status == NOT_STARTED:
            # keep track of start time/frame for later
            instuction.tStart = t
            instuction.frameNStart = frameN  # exact frame index
            instuction.setAutoDraw(True)

        # *startkey* updates
        if t >= 0.0 and startkey.status == NOT_STARTED:
            # keep track of start time/frame for later
            startkey.tStart = t
            startkey.frameNStart = frameN  # exact frame index
            startkey.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(startkey.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        if startkey.status == STARTED:
            theseKeys = event.getKeys(keyList=['space'])

            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                startkey.keys = theseKeys[-1]  # just the last key pressed
                startkey.rt = startkey.clock.getTime()
                # a response ends the routine
                continueRoutine = False

        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in instructionComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished

        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()

        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # -------Ending Routine "instruction"-------
    for thisComponent in instructionComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)

    # check responses
    if startkey.keys in ['', [], None]:  # No response was made
        startkey.keys = None
    blockloop.addData('startkey.keys', startkey.keys)
    if startkey.keys != None:  # we had a response
        blockloop.addData('startkey.rt', startkey.rt)
    # the Routine "instruction" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()

    # set up handler to look after randomisation of conditions etc
    target_loop = data.TrialHandler(nReps=target_n, method='random',
                                    extraInfo=expInfo, originPath=-1,
                                    trialList=[None],
                                    seed=None, name='target_loop')
    thisExp.addLoop(target_loop)  # add the loop to the experiment
    thisTarget_loop = target_loop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTarget_loop.rgb)
    if thisTarget_loop != None:
        for paramName in thisTarget_loop:
            exec('{} = thisTarget_loop[paramName]'.format(paramName))

    for thisTarget_loop in target_loop:
        currentLoop = target_loop
        # abbreviate parameter names if possible (e.g. rgb = thisTarget_loop.rgb)
        if thisTarget_loop != None:
            for paramName in thisTarget_loop:
                exec('{} = thisTarget_loop[paramName]'.format(paramName))

        # ------Prepare to start Routine "target"-------
        t = 0
        targetClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        routineTimer.add(1.550000)
        # update component parameters for each repeat
        import random, string

        if blockloop_N == 0:
            target_n = 0
        elif blockloop_N == 1:
            target_n = 1
            target = random.sample(string.ascii_uppercase, 1)[0]
        elif blockloop_N == 2:
            target_n = 2
            target = random.sample(string.ascii_uppercase, 1)[0]

        target_1.setText(target
                         )
        # keep track of which components have finished
        targetComponents = [fixation1_target, target_1, ISI_target]
        for thisComponent in targetComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED

        # -------Start Routine "target"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = targetClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame

            # *fixation1_target* updates
            if t >= 0 and fixation1_target.status == NOT_STARTED:
                # keep track of start time/frame for later
                fixation1_target.tStart = t
                fixation1_target.frameNStart = frameN  # exact frame index
                fixation1_target.setAutoDraw(True)
            frameRemains = 0 + 0.25 - win.monitorFramePeriod * 0.75  # most of one frame period left
            if fixation1_target.status == STARTED and t >= frameRemains:
                fixation1_target.setAutoDraw(False)

            # *target_1* updates
            if t >= 0.25 and target_1.status == NOT_STARTED:
                # keep track of start time/frame for later
                target_1.tStart = t
                target_1.frameNStart = frameN  # exact frame index
                target_1.setAutoDraw(True)
            frameRemains = 0.25 + 1 - win.monitorFramePeriod * 0.75  # most of one frame period left
            if target_1.status == STARTED and t >= frameRemains:
                target_1.setAutoDraw(False)

            # *ISI_target* updates
            if t >= 1.25 and ISI_target.status == NOT_STARTED:
                # keep track of start time/frame for later
                ISI_target.tStart = t
                ISI_target.frameNStart = frameN  # exact frame index
                ISI_target.setAutoDraw(True)
            frameRemains = 1.25 + 0.3 - win.monitorFramePeriod * 0.75  # most of one frame period left
            if ISI_target.status == STARTED and t >= frameRemains:
                ISI_target.setAutoDraw(False)

            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in targetComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished

            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()

            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()

        # -------Ending Routine "target"-------
        for thisComponent in targetComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)

        stimulus_list.append(target[0])
        thisExp.addData('target', target)

        i += 1
        thisExp.nextEntry()

    # completed target_n repeats of 'target_loop'

    # set up handler to look after randomisation of conditions etc
    nback_loop = data.TrialHandler(nReps=2, method='random',
                                   extraInfo=expInfo, originPath=-1,
                                   trialList=[None],
                                   seed=None, name='nback_loop')
    thisExp.addLoop(nback_loop)  # add the loop to the experiment
    thisNback_loop = nback_loop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisNback_loop.rgb)
    if thisNback_loop != None:
        for paramName in thisNback_loop:
            exec('{} = thisNback_loop[paramName]'.format(paramName))

    for thisNback_loop in nback_loop:
        currentLoop = nback_loop
        # abbreviate parameter names if possible (e.g. rgb = thisNback_loop.rgb)
        if thisNback_loop != None:
            for paramName in thisNback_loop:
                exec('{} = thisNback_loop[paramName]'.format(paramName))

        # ------Prepare to start Routine "n_back_task"-------
        t = 0
        n_backClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        routineTimer.add(3.750000)
        # update component parameters for each repeat
        import random, string

        if blockloop_N == 0:
            if zeroback_TypeControl_list[zeroback_index] == '1':  # target
                stimulus = 'X'
                corResponse = 'z'
                i += 1
                stimulus_list.append(stimulus)
            elif zeroback_TypeControl_list[zeroback_index] == '0':  # nontarget
                stimulus = random.sample([l for l in string.ascii_uppercase if l not in ['X']], 1)[0]
                corResponse = 'x'
                i += 1
                stimulus_list.append(stimulus)
            condition = 'zero_Back'
        elif blockloop_N == 1:
            if oneback_TypeControl_list[oneback_index] == '1':  # target
                stimulus = stimulus_list[i - 1]
                corResponse = 'z'
                i += 1
                stimulus_list.append(stimulus)
            elif oneback_TypeControl_list[oneback_index] == '0':  # nontarget
                stimulus = random.sample([l for l in string.ascii_uppercase if l not in stimulus_list[i - 1]], 1)[0]
                corResponse = 'x'
                i += 1
                stimulus_list.append(stimulus)
            condition = 'one_back'
        elif blockloop_N == 2:
            if twoback_TypeControl_list[twoback_index] == '1':  # target
                stimulus = stimulus_list[i - 2]
                corResponse = 'z'
                i += 1
                stimulus_list.append(stimulus)
            elif twoback_TypeControl_list[twoback_index] == '0':  # nontarget
                stimulus = random.sample([l for l in string.ascii_uppercase if l not in stimulus_list[i - 2]], 1)[0]
                corResponse = 'x'
                i += 1
                stimulus_list.append(stimulus)
            condition = 'two_back'
        question.setText(stimulus)
        response = event.BuilderKeyResponse()
        # keep track of which components have finished
        n_backComponents = [fixation, question, response]
        for thisComponent in n_backComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED

        # -------Start Routine "n_back_task"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = n_backClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame

            # *fixation* updates
            if t >= 0.0 and fixation.status == NOT_STARTED:
                # keep track of start time/frame for later
                fixation.tStart = t
                fixation.frameNStart = frameN  # exact frame index
                fixation.setAutoDraw(True)
            frameRemains = 0.0 + 0.25 - win.monitorFramePeriod * 0.75  # most of one frame period left
            if fixation.status == STARTED and t >= frameRemains:
                fixation.setAutoDraw(False)

            # *question* updates
            if t >= 0.25 and question.status == NOT_STARTED:
                # keep track of start time/frame for later
                question.tStart = t
                question.frameNStart = frameN  # exact frame index
                question.setAutoDraw(True)
            frameRemains = 0.25 + 1 - win.monitorFramePeriod * 0.75  # most of one frame period left
            if question.status == STARTED and t >= frameRemains:
                question.setAutoDraw(False)

            # *response* updates
            if t >= 0.25 and response.status == NOT_STARTED:
                # keep track of start time/frame for later
                response.tStart = t
                response.frameNStart = frameN  # exact frame index
                response.status = STARTED
                # keyboard checking is just starting
                win.callOnFlip(response.clock.reset)  # t=0 on next screen flip
                event.clearEvents(eventType='keyboard')
            frameRemains = 0.25 + 3.5 - win.monitorFramePeriod * 0.75  # most of one frame period left
            if response.status == STARTED and t >= frameRemains:
                response.status = STOPPED
            if response.status == STARTED:
                theseKeys = event.getKeys(keyList=['z', 'x'])

                # check for quit:
                if "escape" in theseKeys:
                    endExpNow = True
                if len(theseKeys) > 0:  # at least one key was pressed
                    if response.keys == []:  # then this was the first keypress
                        response.keys = theseKeys[0]  # just the first key pressed
                        response.rt = response.clock.getTime()
                        # was this 'correct'?
                        if (response.keys == str(corResponse)) or (response.keys == corResponse):
                            response.corr = 1
                        else:
                            response.corr = 0
                        # a response ends the routine
                        continueRoutine = False

            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in n_backComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished

            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()

            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()

        # -------Ending Routine "n_back_task"-------
        for thisComponent in n_backComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)

        thisExp.addData('stimulus', stimulus)

        if blockloop_N == 0:
            oneback_index += 1
            if zeroback_TypeControl_list[0] == '1':  # target
                Is_nBack = 1
                thisExp.addData('Is_nBack', Is_nBack)
            elif zeroback_TypeControl_list[0] == '0':  # nontarget
                Is_nBack = 0
                thisExp.addData('Is_nBack', Is_nBack)
        elif blockloop_N == 1:
            oneback_index += 1
            if oneback_TypeControl_list[0] == '1':  # target
                Is_nBack = 1
                thisExp.addData('Is_nBack', Is_nBack)
            elif oneback_TypeControl_list[0] == '0':  # nontarget
                Is_nBack = 0
                thisExp.addData('Is_nBack', Is_nBack)
        elif blockloop_N == 2:
            twoback_index += 1
            if twoback_TypeControl_list[0] == '1':  # target
                Is_nBack = 1
                thisExp.addData('Is_nBack', Is_nBack)
            elif twoback_TypeControl_list[0] == '0':  # nontarget
                Is_nBack = 0
                thisExp.addData('Is_nBack', Is_nBack)

        thisExp.addData('condition', condition)
        # check responses
        if response.keys in ['', [], None]:  # No response was made
            response.keys = None
            # was no response the correct answer?!
            if str(corResponse).lower() == 'none':
                response.corr = 1;  # correct non-response
            else:
                response.corr = 0;  # failed to respond (incorrectly)
        # store data for nback_loop (TrialHandler)
        nback_loop.addData('response.keys', response.keys)
        nback_loop.addData('response.corr', response.corr)
        if response.keys != None:  # we had a response
            nback_loop.addData('response.rt', response.rt)

        # ------Prepare to start Routine "ISI"-------
        t = 0
        ISIClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        routineTimer.add(0.300000)
        # update component parameters for each repeat
        # keep track of which components have finished
        ISIComponents = [rest]
        for thisComponent in ISIComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED

        # -------Start Routine "ISI"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = ISIClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame

            # *rest* updates
            if t >= 0.0 and rest.status == NOT_STARTED:
                # keep track of start time/frame for later
                rest.tStart = t
                rest.frameNStart = frameN  # exact frame index
                rest.setAutoDraw(True)
            frameRemains = 0.0 + 0.3 - win.monitorFramePeriod * 0.75  # most of one frame period left
            if rest.status == STARTED and t >= frameRemains:
                rest.setAutoDraw(False)

            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in ISIComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished

            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()

            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()

        # -------Ending Routine "ISI"-------
        for thisComponent in ISIComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.nextEntry()

    # completed 2 repeats of 'nback_loop'

    # ------Prepare to start Routine "block_rest"-------
    t = 0
    block_restClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    block_rest_control_key = event.BuilderKeyResponse()

    # keep track of which components have finished
    block_restComponents = [block_rest_control, block_rest_control_key]
    for thisComponent in block_restComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED

    # -------Start Routine "block_rest"-------
    while continueRoutine:
        # get current time
        t = block_restClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame

        # *block_rest_control* updates
        if t >= 0.0 and block_rest_control.status == NOT_STARTED:
            # keep track of start time/frame for later
            block_rest_control.tStart = t
            block_rest_control.frameNStart = frameN  # exact frame index
            block_rest_control.setAutoDraw(True)

        # *block_rest_control_key* updates
        if t >= 0.0 and block_rest_control_key.status == NOT_STARTED:
            # keep track of start time/frame for later
            block_rest_control_key.tStart = t
            block_rest_control_key.frameNStart = frameN  # exact frame index
            block_rest_control_key.status = STARTED
            # keyboard checking is just starting
            event.clearEvents(eventType='keyboard')
        if block_rest_control_key.status == STARTED:
            theseKeys = event.getKeys(keyList=['space'])

            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                # a response ends the routine
                continueRoutine = False

        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in block_restComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished

        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()

        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # -------Ending Routine "block_rest"-------
    for thisComponent in block_restComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    blockloop_N += 1
    # the Routine "block_rest" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()

# completed 3 repeats of 'blockloop'


# ------Prepare to start Routine "end"-------
t = 0
endClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
leavekey = event.BuilderKeyResponse()
# keep track of which components have finished
endComponents = [final, leavekey]
for thisComponent in endComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "end"-------
while continueRoutine:
    # get current time
    t = endClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame

    # *final* updates
    if t >= 0.0 and final.status == NOT_STARTED:
        # keep track of start time/frame for later
        final.tStart = t
        final.frameNStart = frameN  # exact frame index
        final.setAutoDraw(True)

    # *leavekey* updates
    if t >= 0.0 and leavekey.status == NOT_STARTED:
        # keep track of start time/frame for later
        leavekey.tStart = t
        leavekey.frameNStart = frameN  # exact frame index
        leavekey.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(leavekey.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if leavekey.status == STARTED:
        theseKeys = event.getKeys(keyList=['q'])

        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            if leavekey.keys == []:  # then this was the first keypress
                leavekey.keys = theseKeys[0]  # just the first key pressed
                leavekey.rt = leavekey.clock.getTime()
                # a response ends the routine
                continueRoutine = False

    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in endComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished

    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()

    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "end"-------
for thisComponent in endComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if leavekey.keys in ['', [], None]:  # No response was made
    leavekey.keys = None
thisExp.addData('leavekey.keys', leavekey.keys)
if leavekey.keys != None:  # we had a response
    thisExp.addData('leavekey.rt', leavekey.rt)
thisExp.nextEntry()
# the Routine "end" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename + '.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
