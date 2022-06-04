from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QLabel
from PyQt5.QtCore import QThread
from PyQt5.QtCore import Qt
from pygame import mixer


class BeatMaker(QWidget):
    def __init__(self, bpm=108, style=None):
        super().__init__()
        self.Layout = QGridLayout()
        self.Layout.setAlignment(Qt.AlignTop)
        self.setLayout(self.Layout)

        self.bpm = bpm
        self.current_beat = 0
        self.beat_count = 8

        self.constructBeatPad([Instrument('guitar')], num_beats=self.beat_count)

        self.style = style
        if style is not None:
            self.setStyle(style)
        

    def constructBeatPad(self, instruments, num_beats=8):
        self.BeatPad = QGridLayout()
        self.BeatPad.setAlignment(Qt.AlignCenter)
        self.Layout.addLayout(self.BeatPad, 0, 0)

        for i, instrument in enumerate(instruments):
            self.BeatPad.addWidget(instrument, i, 0)
            for beat in range(num_beats):
                self.BeatPad.addWidget(BeatButton(), i, beat+1)
    
    def setBPM(self, bpm):
        self.BPM = bpm
    
    def setBeatCount(self, num_beats):
        # amount of beats in a cycle
        pass
    
    def beatBitMap(self):
        return 

    def setStyle(self, style):
        for i in range(self.BeatPad.count()):
            widget = self.BeatPad.itemAt(i).widget()
            if isinstance(widget, BeatButton):
                widget.setStyleSheet(style.Button.beat)
            elif isinstance(widget, Instrument):
                widget.setFont(style.Font.instrument)
        

class Instrument(QWidget):
    def __init__(self, name='Instrument', audio_file=None):
        super().__init__()
        self.Layout = QGridLayout()
        self.setLayout(self.Layout)

        self.name = QLabel(name)
        self.name.setAlignment(Qt.AlignCenter)
        self.Layout.addWidget(self.name)

        self.audio_file = audio_file

    def setName(self, name):
        self.name = name
    
    def setAudio(self, audio):
        self.audio = audio


class BeatButton(QPushButton):
    def __init__(self):
        super().__init__()
        self.setCheckable(True)
        self.setMaximumHeight(50)


class BeatThread(QThread):
    def __init__(self, beat_maker=None): 
        self.BeatMaker = beat_maker
        self.Mixer = mixer()
        mixer.start()
    
    def playBeat(self):
        pass