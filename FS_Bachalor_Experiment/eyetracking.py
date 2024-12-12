# Imports
import pylink
import os
import sys
from EyeLinkCoreGraphicsPsychoPy import EyeLinkCoreGraphicsPsychoPy
from string import ascii_letters, digits
from psychopy import core
from psychopy.hardware import keyboard


def create_eyetracking_folder(a_folder_name='eyetracker data'):
    """
    Creates folder (if there is not one already) that saves eyetracking-data and names the EDF file for the participant.

    :param a_folder_name: Name the data folder with the EDFs will get
    :type a_folder_name: str

    :return: name of the eyetracking-data-folder
    """
    eyetracker_data_folder0 = a_folder_name
    if not os.path.exists(eyetracker_data_folder0):
        os.makedirs(eyetracker_data_folder0)

    return eyetracker_data_folder0


def edf_name_check(a_edf_fname):
    """
    Checks if name of EDF only contains letters, digits and underscores.
    Name is taken from the global variable "edf_fname" which is specified in PsychoPy script.
    """
    allowed_characters = ascii_letters + digits + "_"

    if len(a_edf_fname) > 8:
        raise RuntimeError("EDF filename too long")
    if not all([c in allowed_characters for c in a_edf_fname]):
        raise RuntimeError("Invalid characters in name, please only use letters, numbers and underscores")


def connect_tracker(dummy_mode):
    """
    Connects stimulus- and host-PC
    :return: el_tracker0, which has to be assigned to the outer "el_tracker" variable, so that other functions can use it
    """
    # Connect tracker
    if dummy_mode:
        el_tracker0 = pylink.EyeLink(None)
    else:
        try:
            el_tracker0 = pylink.EyeLink("100.1.1.1")
        except RuntimeError as error:
            print('ERROR:', error)
            core.quit()
            sys.exit()

    return el_tracker0


def open_edf_file(a_el_tracker, a_edf_fname):
    """
    Opens an EDF file to write in
    """
    # Name and open EDF
    edf_file0 = a_edf_fname + ".EDF"

    try:
        a_el_tracker.openDataFile(edf_file0)
        return edf_file0
    except RuntimeError as err:
        print('ERROR:', err)
        if a_el_tracker.isConnected():
            a_el_tracker.close()
        core.quit()
        sys.exit()


def configure_tracker(a_el_tracker, dummy_mode):
    """
    Sets specifications of the used eyetracker
    """
    a_el_tracker.setOfflineMode()

    eyelink_ver = 0
    if not dummy_mode:
        vstr = a_el_tracker.getTrackerVersionString()
        eyelink_ver = int(vstr.split()[-1].split('.')[0])
        print('Running experiment on %s, version %d' % (vstr, eyelink_ver))

    file_event_flags = 'LEFT,RIGHT,FIXATION,SACCADE,BLINK,MESSAGE,BUTTON,INPUT'
    link_event_flags = 'LEFT,RIGHT,FIXATION,SACCADE,BLINK,BUTTON,FIXUPDATE,INPUT'
    if eyelink_ver > 3:
        file_sample_flags = 'LEFT,RIGHT,GAZE,HREF,RAW,AREA,HTARGET,GAZERES,BUTTON,STATUS,INPUT'
        link_sample_flags = 'LEFT,RIGHT,GAZE,GAZERES,AREA,HTARGET,STATUS,INPUT'
    else:
        file_sample_flags = 'LEFT,RIGHT,GAZE,HREF,RAW,AREA,GAZERES,BUTTON,STATUS,INPUT'
        link_sample_flags = 'LEFT,RIGHT,GAZE,GAZERES,AREA,STATUS,INPUT'
    a_el_tracker.sendCommand("file_event_filter = %s" % file_event_flags)
    a_el_tracker.sendCommand("file_sample_data = %s" % file_sample_flags)
    a_el_tracker.sendCommand("link_event_filter = %s" % link_event_flags)
    a_el_tracker.sendCommand("link_sample_data = %s" % link_sample_flags)


def calibration_validation(a_el_tracker, a_win, dummy_mode):
    """
    Sets up menu for calibration and validation to happen
    """
    genv = EyeLinkCoreGraphicsPsychoPy(a_el_tracker, a_win)
    genv.setTargetType('circle')
    pylink.openGraphicsEx(genv)

    if not dummy_mode:
        try:
            a_el_tracker.doTrackerSetup()
        except RuntimeError as err:
            print('ERROR:', err)
            a_el_tracker.exitCalibration()


def start_recording(a_el_tracker):
    """
    After previous set up, starts recording of the eyetracker
    """
    a_el_tracker = pylink.getEYELINK()
    a_el_tracker.setOfflineMode()
    a_el_tracker.startRecording(1, 1, 1, 1)
    pylink.pumpDelay(100)
    a_el_tracker.sendMessage('0  100')


def stop_recording(a_el_tracker):
    """
    Stops recording, if it has been started before
    """
    # if trial went flawlessly, this will message "TRIAL RESULT 0"
    a_el_tracker.sendMessage('TRIAL_RESULT %d' % pylink.TRIAL_OK)
    pylink.pumpDelay(100)
    a_el_tracker.stopRecording()


def close_tracker_download_edf(a_el_tracker, a_edf_file, a_edf_fname, a_eyetracker_data_folder):
    """
    Closes tracker and downloads EDF to stimulus PC
    """
    a_el_tracker.setOfflineMode()
    a_el_tracker.closeDataFile()
    local_edf = os.path.join(a_eyetracker_data_folder, a_edf_fname + '.EDF')
    try:
        a_el_tracker.receiveDataFile(a_edf_file, local_edf)
    except RuntimeError as error:
        print('ERROR:', error)
    a_el_tracker.close()


def if_force_end_while_recording(a_el_tracker, a_edf_file, a_edf_fname, a_eyetracker_data_folder):
    """
    Safeguards forced exits of the experiment by stopping recording, closing eyetracker and downloading EDF before closing
    """
    defaultKeyboard = keyboard.Keyboard(backend='iohub')

    if defaultKeyboard.getKeys(keyList=["escape"]):
        stop_recording(a_el_tracker)
        close_tracker_download_edf(a_el_tracker, a_edf_file, a_edf_fname, a_eyetracker_data_folder)
        core.quit()


if __name__ == "__main__":
    from psychopy import visual

    eyetracker_data_folder = create_eyetracking_folder()
    edf_fname = "TEST"
    el_tracker = connect_tracker()
    edf_file = open_edf_file()
    win = visual.Window(
    size=[1536, 864], fullscr=True, screen=0,
    winType='pyglet', allowStencil=True,
    monitor='testMonitor', color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb',
    backgroundImage='background.bmp', backgroundFit='fill',
    blendMode='avg', useFBO=True,
    units='height')
    endExpNow = False
