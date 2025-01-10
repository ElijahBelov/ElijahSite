from ntpath import realpath
import random

from django.conf import settings

from os import listdir, getcwd, pardir
from os.path import isfile, join, dirname, realpath, abspath

animalpath = "sortedanimals"

def get_animal():
	#par_path = abspath(join(getcwd(), ))
	fulla = join(settings.BASE_DIR, settings.STATIC_ROOT)
	fulla = join(fulla, animalpath)
	animalfiles = [f for f in listdir(fulla) if isfile(join(fulla, f))]
	return join(animalpath , random.choice(animalfiles))

colours = [
	'rgba(165,42,42,1)',
	'rgba(178,34,34,1)',
	'rgba(220,20,60,1)',
	'rgba(255,0,0,1)',
	'rgba(255,99,71,1)',
	'rgba(255,127,80,1)',
	'rgba(205,92,92,1)',
	'rgba(240,128,128,1)',
	'rgba(233,150,122,1)',
	'rgba(250,128,114,1)',
	'rgba(255,160,122,1)',
	'rgba(255,69,0,1)',
	'rgba(255,140,0,1)',
	'rgba(255,165,0,1)',
	'rgba(255,215,0,1)',
	'rgba(184,134,11,1)',
	'rgba(218,165,32,1)',
	'rgba(238,232,170,1)',
	'rgba(189,183,107,1)',
	'rgba(240,230,140,1)',
	'rgba(128,128,0,1)',
	'rgba(255,255,0,1)',
	'rgba(154,205,50,1)',
	'rgba(85,107,47,1)',
	'rgba(107,142,35,1)',
	'rgba(124,252,0,1)',
	'rgba(127,255,0,1)',
	'rgba(173,255,47,1)',
	'rgba(0,100,0,1)',
	'rgba(0,128,0,1)',
	'rgba(34,139,34,1)',
	'rgba(0,255,0,1)',
	'rgba(50,205,50,1)',
	'rgba(144,238,144,1)',
	'rgba(152,251,152,1)',
	'rgba(143,188,143,1)',
	'rgba(250,154,1)',
	'rgba(255,127,1)',
	'rgba(46,139,87,1)',
	'rgba(102,205,170,1)',
	'rgba(60,179,113,1)',
	'rgba(32,178,170,1)',
	'rgba(128,128,1)',
	'rgba(139,139,1)',
	'rgba(255,255,1)',
	'rgba(255,255,1)',
	'rgba(206,209,1)',
	'rgba(64,224,208,1)',
	'rgba(72,209,204,1)',
	'rgba(175,238,238,1)',
	'rgba(127,255,212,1)',
	'rgba(176,224,230,1)',
	'rgba(95,158,160,1)',
	'rgba(70,130,180,1)',
	'rgba(100,149,237,1)',
	'rgba(191,255,1)',
	'rgba(30,144,255,1)',
	'rgba(173,216,230,1)',
	'rgba(135,206,235,1)',
	'rgba(135,206,250,1)',
	'rgba(65,105,225,1)',
	'rgba(138,43,226,1)',
	'rgba(72,61,139,1)',
	'rgba(106,90,205,1)',
	'rgba(123,104,238,1)',
	'rgba(147,112,219,1)',
	'rgba(148,0,211,1)',
	'rgba(153,50,204,1)',
	'rgba(186,85,211,1)',
	'rgba(216,191,216,1)',
	'rgba(221,160,221,1)',
	'rgba(238,130,238,1)',
	'rgba(255,0,255,1)',
	'rgba(218,112,214,1)',
	'rgba(199,21,133,1)',
	'rgba(219,112,147,1)',
	'rgba(255,20,147,1)',
	'rgba(255,105,180,1)',
	'rgba(255,182,193,1)',
	'rgba(255,192,203,1)',
	'rgba(250,235,215,1)',
	'rgba(255,228,196,1)',
	'rgba(255,235,205,1)',
	'rgba(245,222,179,1)',
	'rgba(139,69,19,1)',
	'rgba(160,82,45,1)',
	'rgba(210,105,30,1)',
	'rgba(205,133,63,1)',
	'rgba(244,164,96,1)',
	'rgba(222,184,135,1)',
	'rgba(210,180,140,1)',
	'rgba(188,143,143,1)',
	'rgba(255,228,181,1)',
	'rgba(255,222,173,1)',
	'rgba(255,218,185,1)',
	'rgba(255,228,225,1)',
	'rgba(112,128,144,1)',
	'rgba(119,136,153,1)',
	'rgba(176,196,222,1)',
	'rgba(230,230,250,1)',
	'rgba(105,105,105,1)',
	'rgba(128,128,128,1)',
	'rgba(169,169,169,1)',
	'rgba(192,192,192,1)',
	'rgba(211,211,211,1)',
	'rgba(220,220,220,1)',
	]

def too_close(curr_colours, new_choice):
	for c in curr_colours:
		if abs(c - new_choice) < 4:
			return True
	return False

def get_gradient():
	deg = random.choice(["0", "45", "90", "135", "180", "225", "270", "315", "360"])
	num_colours = random.randint(2, 4)
	chosen_colours = []
	for c in range(num_colours):
		temp_choice = random.choice(range(len(colours)))
		while too_close(chosen_colours, temp_choice):
			temp_choice = random.choice(range(len(colours)))
		chosen_colours.append(temp_choice)
	my_css = "/* gradient styling */ \n background: " + colours[chosen_colours[0]] + "; \n background: linear-gradient(" + deg + "deg, "
	max_rel_dist = 100 / num_colours;
	for i, c in enumerate(chosen_colours):
		my_css += colours[c] + " " + str(random.randint(int(i * max_rel_dist), int((i + 1) * max_rel_dist))) + "%, "
	my_css = my_css[:-2] + ");"
	return my_css



