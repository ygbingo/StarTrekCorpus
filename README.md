# StarTrekCorpus
Explore star trek corpus from st-minutiae.
Dataset from [st-minutiae](https://www.st-minutiae.com/resources/scripts/). And Process the data to dialogue list like "["A":"How's going?", "B":"Pretty well."]".
![starTrekMinutiae](https://www.st-minutiae.com/graphics/titles/resources-scripts.png)

# Envirnment
- Python3

# Usage
### Get dataset
```shell
# download
wget https://www.st-minutiae.com/resources/scripts/scripts_mov.zip
wget https://www.st-minutiae.com/resources/scripts/scripts_tng.zip
wget https://www.st-minutiae.com/resources/scripts/scripts_ds9.zip

# unzip
unzip -o -d ./scripts_mov scripts_mov.zip
unzip -o -d ./scripts_tng scripts_tng.zip
unzip -o -d ./scripts_ds9 scripts_ds9.zip
```

### Generate dataset
```shell
python main.py
```

# Result Sample
```json
["BGM: The image of Earth is actually on a monitor, which is only one of DOZENS of MONITORS covering a huge wall. We don't see anything of the rest of the room, but the technology in view is distinctly alien and bizarre -- a mixture of organic and mechanical elements. Circuitry and optical cabling are side-by-side with what looks almost like arteries and organs. We can still hear the creepy skittering and gurgling noises. Occasionally, a SHADOWY FORM sweeps past the camera, vaguely humanoid but we can't tell who or what it is. ", "BGM: All of the monitors are active, and they present myriad IMAGES and SOUND -- all related to EARTH HISTORY. The screens show everything from written Chinese... to Renaissance paintings... to black and white newsreel footage of World War Two... to what look like clips of space battles from the 24th century. The entire range of human history dancing across the monitors. The effect is dizzying -- we get the feeling that whoever is watching this is studying the human race. ", "BGM: There is another THUMP and the wall of monitors SHUDDERS slightly. We hear the VOICE of what we will come to know as the BORG COLLECTIVE -- thousands of voices speaking at once : ", "BORG: Restrict search parameters to 1-9- 9-8 through 2-0-8-4. ", "BGM: The images on the monitors now change to show us images from 21ST CENTURY Earth history. ", "BGM: Again, it's a collection of still photography, video footage, text, artwork, etc. We hear snippets of sound- bites, music, speeches from the period. A lot of enticing details. As the images race across the monitors, we should learn the following. ", "BGM: Regional wars, the collapse of the United Nations. Societal break-down. Crime, starvation, desperation. ", "BGM: environmental disasters, tens of millions dead. The United States ceases to exist. All political authority vanishes. Humanity teetering on the edge of the Second Dark Age. ", "BGM: visionary scientist. He see the spacecraft he created out of a nuclear missile. He flies the first warp test, breaking the light barrier. It changes history. ", "BGM: landing on Earth. They saw Cochrane's flight, followed him back to Earth, and made First Contact with the human race. ", "BGM: alien civilization brings the planet together as never before. Humans and Vulcans working together, beginning to solve long-standing problems with new technology. We see an early replicator producing food for the starving millions. A new World Government is formed. ", "BGM: an Alliance. They call it the United Federation of Planets. And they commission a fleet of starships for protection and exploration. They call it Starfleet. ", "BGM: Trek universe. ", "BGM: Another muffled EXPLOSION, this one stronger, SHAKES the entire wall. One of the monitors BLOWS OUT in a shower of sparks. And now a new voice, a woman's voice, low, threatening, with a slight metallic inflection, speaks for the first time: ", "WOMAN'S VOICE: Stop search. Calculate temporal coordinates. J-Fourteen. ", "BGM: Another explosion ROCKS the room and it takes us to: "]
["BGM: involving dozens of Starfleet and Borg vessels, engaged in a fierce FIREFIGHT as far as the eye can see. Ships turning, twisting, firing, exploding. Lots of movement. It's a spectacular sight. ", "BGM: The Borg Sphere is moving away from the battle, heading off in another direction. "]
["BGM: In the middle of the battle. A BORG CUBE is attacking a smaller Federation starship. The starship is taking quite a beating... explosions all along the hull... it doesn't look like it can take much  more of this. ", "BGM: Suddenly a spread of FOUR TORPEDOES come blazing in from O.C. The torpedoes SLAM into the Borg ship, causing massive damage. "]
["BGM: SOARS into view and moves to protect the beleaguered starship. ", "BGM: The Enterprise is Starfleet's newest and most powerful vessel. An elegant and majestic ship. But unlike the last Enterprise, Starfleet has opted for a more muscular vessel and the hull is studded with weapons and other defensive armory. We get the feeling this Enterprise is ready for anything. "]
["BGM: The Bridge has been redesigned. A single Captain's chair dominates the room, and surrounding consoles and stations all face inward instead of out, giving Picard instant access to his officers. PICARD in the Captain's chair. RIKER at a new Ops station. DATA at the helm. WORF at Tactical. TROI at Communications, various CREWMEMBERS at their posts. The ship is at Red Alert and everyone is tense. ", "PICARD: Signal the Endeavor to fall back. We'll cover them. ", "TROI: Aye, sir. ", "BGM: She works her console. "]
["BGM: The ship is ROCKED by the blast. ", "DATA: Dispersive armor is holding. ", "PICARD: Bring us about. Target Borg ship alpha four, port side battery. ", "WORF: Port battery, ready sir! ", "PICARD: Fire. "]
["BGM: Including MAIN VIEWSCREEN, which has a view of the chaotic battle surrounding them. Another Borg vessel looms into view. ", "PICARD: Starboard battery -- fire. "]
...
```




