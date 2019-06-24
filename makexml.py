from random import randint

fifthsdict = {"Cb": -7, "Gb": -6, "Db": -5, "Ab": -4, "Eb": -3, "Bb": -2, "F": -1, "C": 0, "G": 1, "D": 2, "A": 3, "E": 4, "B": 5, "F#": 6, "C#": 7,}

header = '<?xml version="1.0" encoding="UTF-8" standalone="no"?>\n<!DOCTYPE score-partwise PUBLIC\n"-//Recordare//DTD MusicXML 3.1 Partwise//EN"\n"http://www.musicxml.org/dtds/partwise.dtd">\n<score-partwise version="3.1">\n<part-list>\n<score-part id="P1">\n<part-name>Music</part-name>\n</score-part>\n</part-list>\n<part id="P1">\n'

divisions = 8
fifths = 0
timesigtop = 4
timesigbottom = 4
sign = ""
clefpos = 0


def divcrotch():
      global divisions
      divisions = input("Divisions of crotchet: ")
      return divisions
def key():
      global fifthsdict
      return fifthsdict[str(raw_input("Key: "))]
def beattop():
      global timesigtop
      timesigtop = int(input("Beats: "))
      return timesigtop
def beatbottom():
      global timesigbottom
      timesigbottom = int(input("Beat Type: "))
      return timesigbottom
def clef():
      global sign
      output = str(input("1 Treble, 2 Bass: "))
      if output == 1:
        sign = "G"
        return sign
      else:
        sign = "F"
        return sign
def linenum(): 
      global clefpos
      clefpos = input("Clef position: ") 
      return clefpos



#or with notes use 'keypositions+x % 21'
#x being the step between the keys in a circle
#(%21 is so that you don't leave length of the array)

octaveposition = 4
measurenumber = 1
TotalBeats = 0

def setupattributes():
  global measurenumber  
  output = """<measure number=""" + "'" + str(measurenumber) + "'" + """>
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
  return output

notesxml = {
  "Af": "<step>A</step>"+'\n'+"<accidental>flat</accidental>"+'\n'+"<alter>-1</accidental>",
  "A": "<step>A</step>",
  "As": "<step>A</step>"+'\n'+"<accidental>sharp</accidental>"+'\n'+"<alter>+1</alter>",
  "Bf": "<step>B</step>"+'\n'+"<accidental>flat</accidental>"+'\n'+"<alter>-1</alter>",
  "B": "<step>B</step>",
  "Bs": "<step>B</step>"+'\n'+"<accidental>sharp</accidental>"+'\n'+"<alter>+1</alter>",
  "Cf": "<step>C</step>"+'\n'+"<accidental>flat</accidental>"+'\n'+"<alter>-1</alter>",
  "C": "<step>C</step>",
  "Cs": "<step>C</step>"+'\n'+"<accidental>sharp</accidental>",
  "Df": "<step>D</step>"+'\n'+"<accidental>flat</accidental>"+'\n'+"<alter>-1</alter>",
  "D": "<step>D</step>",
  "Ds": "<step>D</step>"+'\n'+"<accidental>sharp</accidental>"+'\n'+"<alter>+1</alter>",
  "Ef": "<step>E</step>"+'\n'+"<accidental>flat</accidental>"+'\n'+"<alter>-1</alter>",
  "E": "<step>E</step>",
  "Es": "<step>E</step>"+'\n'+"<accidental>sharp</accidental>"+'\n'+"<alter>+1</alter>",
  "Ff": "<step>F</step>"+'\n'+"<accidental>flat</accidental>"+'\n'+"<alter>-1</alter>",
  "F": "<step>F</step>",
  "Fs": "<step>F</step>"+'\n'+"<accidental>sharp</accidental>"+'\n'+"<alter>+1</alter>",
  "Gf": "<step>G</step>"+'\n'+"<accidental>flat</accidental>"+'\n'+"<alter>-1</alter>",
  "G": "<step>G</step>",
  "Gs": "<step>G</step>"+'\n'+"<accidental>sharp</accidental>"+'\n'+"<alter>+1</alter>"}
notenames = ['Af', 'A', 'Bf', 'B', 'C', 'Cs', 'D', 'Ef', 'E', 'F', 'Fs', 'G']
lengthxml = {
  "sb": "<duration>" + str(divisions * 4) + "</duration>",
  "m": "<duration>" + str(divisions * 2) + "</duration>",
  "c": "<duration>" + str(divisions) + "</duration>",
  "q": "<duration>" + str(divisions / 2) + "</duration>",
  "sq": "<duration>" + str(divisions / 4) + "</duration>",
  "dsq": "<duration>" + str(divisions / 8) + "</duration>",}
lengthnames = ['sb', 'm', 'c', 'q', 'sq', 'dsq']
lengths_as_divisions = {
  "sb": divisions * 4,
  "m": divisions * 2,
  "c": divisions,
  "q": divisions / 2,
  "sq": divisions / 4,
  "dsq": divisions / 8 }

# Duration is a multiple of the maximum division of quarter note e.g. if division is 24, duration24 is a crotchet.

divisions_left_in_bar = timesigtop * (divisions / (timesigbottom / 4))

def make_note(step, len):
    global octaveposition
    global lengthxml
    global notesxml
    global divisions_left_in_bar
    global measurenumber
    output = """\n     <note>
    <pitch>
      """+str(notesxml[step])+"""
      <octave>""" + str(octaveposition) + """</octave>
    </pitch>
    """ + str(lengthxml[len]) + """
  </note>"""
    divisions_left_in_bar -= lengths_as_divisions[str(len)]
    if divisions_left_in_bar == 0:
      output += "\n</measure>\n\t" + "<measure number =" + "'" + str(measurenumber) + "'" ">"
      measurenumber += 1
      divisions_left_in_bar += timesigtop * (divisions / (timesigbottom / 4))
      return output
    else:        
      return output


notes = ""

for i in range (0, 1000):
      step = str(notenames[randint(0, 11)])
      notes += make_note(step, "sq")


notes += "</measure>\n</part>\n</score-partwise>"



file = open("test.xml", "a")
file.write(header + setupattributes() + notes)
file.close





