header = '<?xml version="1.0" encoding="UTF-8" standalone="no"?>\n<!DOCTYPE score-partwise PUBLIC\n"-//Recordare//DTD MusicXML 3.1 Partwise//EN"\n"http://www.musicxml.org/dtds/partwise.dtd">\n<score-partwise version="3.1">\n<part-list>\n<score-part id="P1">\n<part-name>Music</part-name>\n</score-part>\n</part-list>\n<part id="P1">\n'

DivCrotch = str(input("Divisions of crotchet: "))
Key = str(input("Key: "))
BeatTop = str(input("Beats: "))
BeatBottom = str(input("Beat type: "))
CleftType = str(input("Treble clef (1), bass clef (2)"))
LineNum = str(input("On which line: "))
if CleftType == "1":
 clef = "G"
else:
 clef = "F"

#or with notes use 'keypositions+x % 21'
#x being the step between the keys in a circle
#(%21 is so that you don't leave length of the array)
octaveposition = 4
starting_note_key = str(input("Which key to start in: "))
measurenumber = 1

def setupstart(div, key, beat, beattype, cleft, line):
 cleftime = """<measure number="""+str(measurenumber)+""">
 <attributes>
    <divisions>"""+str(div)+"""</divisions>
      <key>
        <fifths>"""+str(key)+"""</fifths>
      </key>
      <time>
        <beats>"""+str(beat)+"""</beats>
        <beat-type>"""+str(beattype)+"""</beat-type>
      </time>
      <clef>
        <sign>"""+str(cleft)+"""</sign>
        <line>"""+str(line)+"""</line>
      </clef>
  </attributes>
</measure>"""
 return cleftime

cleftime = setupstart(DivCrotch, Key, BeatTop, BeatBottom, CleftType, LineNum)
print(cleftime)


#notesxml[notesarray[random]]

notesarray = ["Af", "A", "As", "Bf", "B", "Bs", "Cf", "C", "Cs", "Df", "D", "Ds", "Ef", "E", "Es", "Ff", "F", "Fs", "Gf", "G", "Gs"]
notesxml = { "Af": "<step>A</step>"+'\n'+"<accidental>flat</accidental>",
  "A": "<step>A</step>",
  "As": "<step>A</step>"+'\n'+"<accidental>sharp</accidental>",
  "Bf": "<step>B</step>"+'\n'+"<accidental>flat</accidental>",
  "B": "<step>B</step>", "Bs": "<step>B</step>"+'\n'+"<accidental>sharp</accidental>",
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
accidentalsarrays = {"f": "<accidental>flat</accidental>", "s": "<accidental>sharp</accidental>", "ff": "<accidental>double-flat</accidental>", "ss": "<accidental>double-sharp</accidental>"}

keypositions = notesarray.index(starting_note_key)

#add the notes as strings that you want in the arrays for each key
keysdict = { "Af": ["Af", "C"], "A": [], "As": [], "Bf": [], "B": [], "Bs": [], "Cf": [], "C": [], "Cs": [], "Df": [], "D": [], "Ds": [], "Ef": [], "E": [], "Es": [], "Ff": [], "F": [], "Fs": [], "Gf": [], "G": [], "Gs": []}


lengtharrary = ["Sb", "M", "C", "Q", "Sq", "Dq"]
#i guessed these duration and type values
lengthxml = {
  "Sb": "<duration>4</duration>"+'\n'+"<type>whole</type>",
  "M": "<duration>2</duration>"+'\n'+"<type>whole</type>",
  "C": "<duration>1</duration>"+'\n'+"<type>whole</type>",
  "Q": "<duration>1</duration>"+'\n'+"<type>half</type>",
  "Sq": "<duration>1</duration>"+'\n'+"<type>quater</type>",
  "Dq": "<duration>1</duration>"+'\n'+"<type>eigth</type>"
}

def addtuple(actual, normal):
  tuplestring = "<time-modification>"+'\n'+"\t<actual-notes>"+str(actual)+"</actual-notes>"+'\n'+"<normal-notes>"+str(normal)+"\t</normal-notes>"+'\n'+"</time-modification>"
  return tuplestring


#so far only just printing strings that will be written to file

#f = open("output.xml", "a")
#f.write(contents)
#f.close
