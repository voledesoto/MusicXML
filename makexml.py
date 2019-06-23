from random import randint

fifthsdict = {"Cb": -7, "Gb": -6, "Db": -5, "Ab": -4, "Eb": -3, "Bb": -2, "F": -1, "C": 0, "G": 1, "D": 2, "A": 3, "E": 4, "B": 5, "F#": 6, "C#": 7,}

header = '<?xml version="1.0" encoding="UTF-8" standalone="no"?>\n<!DOCTYPE score-partwise PUBLIC\n"-//Recordare//DTD MusicXML 3.1 Partwise//EN"\n"http://www.musicxml.org/dtds/partwise.dtd">\n<score-partwise version="3.1">\n<part-list>\n<score-part id="P1">\n<part-name>Music</part-name>\n</score-part>\n</part-list>\n<part id="P1">\n'


def divcrotch():
      return input("Divisions of crotchet: ")
def key():
      global fifthsdict
      return fifthsdict[str(raw_input("Key: "))]
def beattop():
      return input("Beats: ")
def beatbottom():
      return input("Beat Type: ")
def clef():
      output = str(input("1 Treble, 2 Bass: "))
      if output == 1:
        return "G"
      else:
        return "F"
def linenum():   
      return input("Clef position: ")    



#or with notes use 'keypositions+x % 21'
#x being the step between the keys in a circle
#(%21 is so that you don't leave length of the array)
octaveposition = 4
measurenumber = 1
TotalBeats = str()

def setupstart():
  global measurenumber  
  cleftime = """<measure number=""" + str(measurenumber) +""">
      <attributes>
          <divisions>""" + str(divcrotch()) +"""</divisions>
            <key>
              <fifths>""" + str(key()) + """</fifths>
            </key>
            <time>
              <beats>""" + str(beattop()) + """</beats>
              <beat-type>""" + str(beatbottom()) + """</beat-type>
            </time>
            <clef>
              <sign>""" + str(clef()) + """</sign>
              <line>""" + str(linenum()) + """</line>
            </clef>
        </attributes>"""
  return cleftime

print(header + "\n" + setupstart())

#notesxml[notesarray[random]]

notesarray = ["Af", "A", "As", "Bf", "B", "Bs", "Cf", "C", "Cs", "Df", "D", "Ds", "Ef", "E", "Es", "Ff", "F", "Fs", "Gf", "G", "Gs"]
natnotesarray = ["A", "B", "C", "D", "E", "F", "G"]
notesxml = {
  "Af": "<step>A</step>"+'\n'+"<accidental>flat</accidental>",
  "A": "<step>A</step>",
  "As": "<step>A</step>"+'\n'+"<accidental>sharp</accidental>",
  "Bf": "<step>B</step>"+'\n'+"<accidental>flat</accidental>",
  "B": "<step>B</step>",
  "Bs": "<step>B</step>"+'\n'+"<accidental>sharp</accidental>",
  "Cf": "<step>C</step>"+'\n'+"<accidental>flat</accidental>",
  "C": "<step>C</step>",
  "Cs": "<step>C</step>"+'\n'+"<accidental>sharp</accidental>",
  "Df": "<step>D</step>"+'\n'+"<accidental>flat</accidental>",
  "D": "<step>D</step>",
  "Ds": "<step>D</step>"+'\n'+"<accidental>sharp</accidental>",
  "Ef": "<step>E</step>"+'\n'+"<accidental>flat</accidental>",
  "E": "<step>E</step>",
  "Es": "<step>E</step>"+'\n'+"<accidental>sharp</accidental>",
  "Ff": "<step>F</step>"+'\n'+"<accidental>flat</accidental>",
  "F": "<step>F</step>",
  "Fs": "<step>F</step>"+'\n'+"<accidental>sharp</accidental>",
  "Gf": "<step>G</step>"+'\n'+"<accidental>flat</accidental>",
  "G": "<step>G</step>",
  "Gs": "<step>G</step>"+'\n'+"<accidental>sharp</accidental>"}
natnotesxml = {
    "A": "<step>A</step>",
    "B": "<step>B</step>",
    "C": "<step>C</step>",
    "D": "<step>D</step>",
    "E": "<step>E</step>",
    "F": "<step>F</step>",
    "G": "<step>G</step>",
 }
accidentalsarrays = {"f": "<accidental>flat</accidental>", "s": "<accidental>sharp</accidental>", "ff": "<accidental>double-flat</accidental>", "ss": "<accidental>double-sharp</accidental>"}

keypositions = notesarray.index(starting_note_key)

#add the notes as strings that you want in the arrays for each key
keysdict = { "Af": ["Af", "C"], "A": [], "As": [], "Bf": [], "B": [], "Bs": [], "Cf": [], "C": [], "Cs": [], "Df": [], "D": [], "Ds": [], "Ef": [], "E": [], "Es": [], "Ff": [], "F": [], "Fs": [], "Gf": [], "G": [], "Gs": []}


lengtharrary = ["Sb", "M", "C", "Q", "Sq", "Dq"]
#i guessed these duration and type values
lengthxml = {
  "Sb": "<duration>4</duration>"+'\n'+"    <type>whole</type>",
  "M": "<duration>2</duration>"+'\n'+"    <type>whole</type>",
  "C": "<duration>1</duration>"+'\n'+"    <type>whole</type>",
  "Q": "<duration>1</duration>"+'\n'+"    <type>half</type>",
  "Sq": "<duration>1</duration>"+'\n'+"    <type>quater</type>",
  "Dq": "<duration>1</duration>"+'\n'+"    <type>eigth</type>"
}

lengthvals = {"Sb": 1, "M": 1/2, "C": 1/4, "Q": 1/8, "Sq": 1/16, "Dq": 1/32}
leftlengthvals = [float(1), float(1/2), float(1/4), float(1/8), float(1/16), float(1/32)]


def make_note(notenum, lengthnum):
    note_string = """  <note>
    <pitch>
      """+str(natnotesxml[natnotesarray[notenum]])+"""
      <octave>"""+str(octaveposition)+"""</octave>
    </pitch>
    """+lengthxml[lengtharrary[lengthnum]]+"""
  </note>"""
    return note_string

testnote = make_note(2, 2)
#print(testnote)


def first_bar(beatss):
    bar_string = ""
    beatsleft = beatss
    while beatsleft > 0:
        notenum = randint(0,6)
        lengthnum = randint(0,5)
        if (leftlengthvals[lengthnum]-beatsleft) >= 0:
            bar_string += make_note(notenum, lengthnum)
            timeprogress = lengthvals[lengtharrary[lengthnum]]
            beatsleft -= timeprogress
        else:
            continue
    bar_string += "\n</measure>"
    global measurenumber
    measurenumber = 2
    return bar_string

testfirstbar = first_bar(TotalBeats)
print(testfirstbar)

def make_bar(beatss):
    bar_string = "<measure number = "+"\""+str(measurenumber)+"\""+">"
    beatsleft = beatss
    while beatsleft > 0:
        notenum = randint(0,6)
        lengthnum = randint(0,5)
        if (leftlengthvals[lengthnum]-beatsleft) >= 0:
            bar_string += make_note(notenum, lengthnum)
            timeprogress = lengthvals[lengtharrary[lengthnum]]
            beatsleft -= timeprogress
        else:
            continue
    bar_string += "\n</measure>"
    global measurenumber
    measurenumber += 1
    return bar_string






def addtuple(actual, normal):
  tuplestring = "<time-modification>"+'\n'+"\t<actual-notes>"+str(actual)+"</actual-notes>"+'\n'+"<normal-notes>"+str(normal)+"\t</normal-notes>"+'\n'+"</time-modification>"
  return tuplestring


#so far only just printing strings that will be written to file

#f = open("output.xml", "a")
#f.write(contents)
#f.close
