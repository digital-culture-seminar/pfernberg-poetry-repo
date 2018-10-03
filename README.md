# Artist Statement

Our workplaces and social spaces are in the midst of turning a proverbial corner. In not so may years, the skills lines of resumes are going to be backspacing "Microsoft Word" and "customer service extraordinaire" and instead reading "programming" and "computational thinker". Assembly line workers will become digital machine operators. Secretaries will leave the scheduling to robots and become social media accounts managers. School children will trade in their chalkboards for tablets and become juvenile coders. CSS certifications will be the new high school diplomas and Processing windows the new artistic canvas. Some would say resistance is futile.

If such a transition is truly inevitable, it is vital that we learn to humanize and demystify the abstract world of computation. The public at large needs to understand that although the average worker of tomorrow may no longer build with hammer and nail or weave on a loom, they will still wield tools that--whether they notice or not--shape civilization just as tangibly. We need a Digital Transition Guide for Dummies stat! And who better for the job than the Artist?

I believe just as Yo-Yo Ma does that the job of the Artist is to go to the edge and report back; they should scour the fringes of the human psyche, survey the nuances of the boolean logic landscape and then re-center themselves within the citizenry, teaching us how to express the inexpressible and know the unknowable through words, music, dance, and visual media.

My art will be an art of open computation and philomathy; an art that is no respecter of media or author, whose accessibility is only limited by the participant's lack of interest in learning.

An art which begets a repository of poems perpetually in iteration, like speculations on what Imagist and Modernist poets would do if they could collaborate with markov...

# import libraries
import markovify as m

with open("TheWasteland_TSEliot.txt") as wasteland:
    wasteland = wasteland.read()

with open("Poems1918-21_EzraPound.txt") as pound:
    pound = pound.read()

with open("williams_improvisations.txt") as improv:
    improv = improv.read()

# build the model
wasteland_model = m.NewlineText(wasteland) #text_model = markovify.Text(text)
pound_model = m.NewlineText(pound)
improv_model = m.NewlineText(improv)

# synthesize the model
synthesized_model = m.combine([wasteland_model, pound_model, improv_model], [1,1,1.5])

of sounds to be added to,

(python code)

and of fabrications to be continually riffed on.

(python code)

My art will be an art that has no value unless I cease to be the sole owner and producer of it.

And with that I have only one question:

**WHY ARE YOU STILL READING THIS? LET'S GET STARTED! LET'S MAKE SOMETHING VALUABLE TOGETHER!**
