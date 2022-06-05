from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QLabel, QSpinBox, QToolBar
from PyQt5.QtCore import QThread, Qt, QTimer
import time
from pygame import mixer

from AppStyle import AppStyle


class BeatMaker(QWidget):
    def __init__(self, MainWindow, bpm=108, style=None) -> None:
        super().__init__()
        self.MainWindow = MainWindow

        self.Layout = QGridLayout()
        self.Layout.setAlignment(Qt.AlignTop)
        self.setLayout(self.Layout)

        self.BeatTimer = QTimer()
        self.BeatThread = BeatThread(beat_maker=self)
        self.BeatTimer.timeout.connect(self.playBeat)

        self.setBPM(bpm)
        self.setBeatCount(8)
        self.setCurrentBeat(0)

        mixer.init()

        self.instruments = [
                Instrument('Bass', sound=mixer.Sound('808 Samples\\bass (1).wav')), 
                Instrument('Clap', sound=mixer.Sound('808 Samples\\clap (1).wav'))
                ]

        self.constructBeatPad(self.instruments, num_beats=self.beat_count)

        self.constructControls()
        
        self.style = style
        if style is not None:
            self.setStyle(style)

        self.BeatTimer.start(1 / (self.bpm / 60 / 1000))

    def constructBeatPad(self, instruments: list, num_beats=8) -> None:
        self.BeatPad = QGridLayout()
        self.BeatPad.setAlignment(Qt.AlignCenter)
        self.Layout.addLayout(self.BeatPad, 0, 0)

        for i, instrument in enumerate(instruments):
            self.BeatPad.addWidget(instrument, i, 0)
            for beat in range(num_beats):
                self.BeatPad.addWidget(BeatButton(), i, beat+1)
    
    def constructControls(self) -> None:
        self.ControlMenu = QToolBar()
        self.MainWindow.addToolBar(self.ControlMenu)

        self.bpmInput = QSpinBox()
        self.bpmInput.setMaximum(200)
        self.bpmInput.setValue(self.bpm)
        self.bpmInput.valueChanged.connect(lambda: self.setBPM(self.bpmInput.value()))
        self.ControlMenu.addWidget(self.bpmInput)
            
    def playBeat(self) -> None:
        for instrument in self.instruments:
            instrument.sound.play()
    
    def pause(self, pause: bool) -> None:
        if pause:
            self.BeatTimer.stop()
        else:
            self.BeatTimer.start()
    
    def setBPM(self, bpm: int) -> None:
        self.bpm = bpm
        self.BeatTimer.setInterval(1 / (self.bpm / 60 / 1000))
    
    def setBeatCount(self, num_beats: int) -> None:
        # amount of beats in a cycle
        self.beat_count = num_beats
    
    def setCurrentBeat(self, curr_beat: int) -> None:
        if curr_beat >= self.beat_count or curr_beat < 0:
            return
        else:
            self.current_beat = curr_beat
    
    def beatBitMap(self) -> None:
        return 

    def setStyle(self, style: AppStyle) -> None:
        for i in range(self.BeatPad.count()):
            widget = self.BeatPad.itemAt(i).widget()
            if isinstance(widget, BeatButton):
                widget.setStyleSheet(style.Button.beat)
            elif isinstance(widget, Instrument):
                widget.setFont(style.Font.instrument)
                widget.setStyleSheet(style.Label.instrument)
        

class Instrument(QWidget):
    # sound can be a mixer.Sound object or a file path to the audio file
    def __init__(self, name='Instrument', sound=None):
        super().__init__()
        self.Layout = QGridLayout()
        self.setLayout(self.Layout)

        self.name = QLabel(name)
        self.name.setFont(AppStyle.Font.instrument)
        self.name.setStyleSheet(AppStyle.Label.instrument)
        self.name.setAlignment(Qt.AlignCenter)
        self.Layout.addWidget(self.name)

        self.setSound(sound)

    def setName(self, name: str) -> None:
        self.name.setText(name)
    
    def setSound(self, sound) -> None:
        if isinstance(sound, mixer.Sound):
            self.sound = sound
        else:
            try:
                self.sound = mixer.Sound(sound)
            except:
                self.sound = None


class BeatButton(QPushButton):
    def __init__(self):
        super().__init__()
        self.setCheckable(True)
        self.setMaximumHeight(50)


class BeatThread(QThread):
    def __init__(self, beat_maker=None): 
        super().__init__()
        self.BeatMaker = beat_maker

    def playSound(self, sound):
        pass